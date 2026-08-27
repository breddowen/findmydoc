# ./backend/app/core/security.py
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.utils import user_has_role


password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/token",
)


@dataclass
class AuthContext:
    user: User
    active_role: UserRole
    token_payload: dict[str, Any]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str | None,
) -> bool:
    if not hashed_password:
        return False

    return password_hash.verify(plain_password, hashed_password)


def validate_password_strength(password: str) -> None:
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароль должен содержать не менее 8 символов",
        )

    if len(password) > 128:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароль должен содержать не более 128 символов",
        )


def create_jwt_token(
    *,
    subject: uuid.UUID,
    token_type: str,
    expires_delta: timedelta,
    extra_claims: dict[str, Any] | None = None,
) -> str:
    now = utc_now()

    payload: dict[str, Any] = {
        "sub": str(subject),
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
        "jti": str(uuid.uuid4()),
    }

    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def create_access_token(
    *,
    user: User,
    active_role: UserRole,
) -> str:
    return create_jwt_token(
        subject=user.id,
        token_type="access",
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        extra_claims={
            "role": active_role.value,
            "auth_version": user.auth_version,
        },
    )


def create_role_selection_token(*, user: User) -> str:
    return create_jwt_token(
        subject=user.id,
        token_type="role_selection",
        expires_delta=timedelta(
            minutes=settings.ROLE_SELECTION_TOKEN_EXPIRE_MINUTES
        ),
        extra_claims={
            "auth_version": user.auth_version,
        },
    )


def decode_jwt_token(
    token: str,
    *,
    expected_type: str | None = None,
) -> dict[str, Any]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Недействительный или просроченный токен",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except InvalidTokenError as error:
        raise credentials_exception from error

    if expected_type and payload.get("type") != expected_type:
        raise credentials_exception

    if not payload.get("sub"):
        raise credentials_exception

    return payload


def ensure_user_can_authenticate(user: User | None) -> User:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учётные данные",
        )

    if user.deleted_at is not None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Аккаунт деактивирован",
        )

    if user.is_blocked:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Аккаунт заблокирован",
        )

    return user


async def get_current_auth(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> AuthContext:
    payload = decode_jwt_token(
        token,
        expected_type="access",
    )

    try:
        user_id = uuid.UUID(payload["sub"])
        active_role = UserRole(payload["role"])
        token_auth_version = int(payload["auth_version"])
    except (ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Некорректное содержимое токена",
            headers={"WWW-Authenticate": "Bearer"},
        ) from error

    user = ensure_user_can_authenticate(
        session.get(User, user_id)
    )

    if user.auth_version != token_auth_version:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Сессия больше не действительна",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user_has_role(session, user.id, active_role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Роль больше не доступна",
        )

    return AuthContext(
        user=user,
        active_role=active_role,
        token_payload=payload,
    )


def require_roles(*allowed_roles: UserRole):
    async def dependency(
        auth: AuthContext = Depends(get_current_auth),
    ) -> AuthContext:
        if auth.active_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав",
            )

        return auth

    return dependency