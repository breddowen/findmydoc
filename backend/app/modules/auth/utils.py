# ./backend/app/modules/auth/utils.py
import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select

from app.core.config import settings
from app.core.email import send_console_email
from app.modules.auth.models import ActionToken, ActionTokenType
from app.modules.users.models import User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def hash_action_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_action_token(
    *,
    session: Session,
    user: User,
    token_type: ActionTokenType,
    expires_minutes: int | None = None,
) -> str:
    active_tokens = session.exec(
        select(ActionToken).where(
            ActionToken.user_id == user.id,
            ActionToken.token_type == token_type,
            ActionToken.consumed_at.is_(None),
        )
    ).all()

    now = utc_now()

    for active_token in active_tokens:
        active_token.consumed_at = now
        session.add(active_token)

    raw_token = secrets.token_urlsafe(48)

    action_token = ActionToken(
        user_id=user.id,
        token_hash=hash_action_token(raw_token),
        token_type=token_type,
        expires_at=now + timedelta(
            minutes=expires_minutes
            or settings.ACTION_TOKEN_EXPIRE_MINUTES
        ),
    )

    session.add(action_token)
    session.commit()

    return raw_token


def get_valid_action_token(
    *,
    session: Session,
    raw_token: str,
    token_type: ActionTokenType,
) -> ActionToken | None:
    token_hash = hash_action_token(raw_token)

    action_token = session.exec(
        select(ActionToken).where(
            ActionToken.token_hash == token_hash,
            ActionToken.token_type == token_type,
        )
    ).first()

    if not action_token:
        return None

    if action_token.consumed_at is not None:
        return None

    expires_at = action_token.expires_at

    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)

    if expires_at <= utc_now():
        return None

    return action_token


def send_verification_email(
    *,
    session: Session,
    user: User,
) -> None:
    token = create_action_token(
        session=session,
        user=user,
        token_type=ActionTokenType.EMAIL_VERIFICATION,
    )

    send_console_email(
        recipient=user.email,
        subject="Подтверждение email — MentalMe",
        message="Для подтверждения email перейдите по ссылке:",
        action_path="/verify-email",
        token=token,
    )


def send_password_reset_email(
    *,
    session: Session,
    user: User,
) -> None:
    token = create_action_token(
        session=session,
        user=user,
        token_type=ActionTokenType.PASSWORD_RESET,
    )

    send_console_email(
        recipient=user.email,
        subject="Восстановление пароля — MentalMe",
        message="Для установки нового пароля перейдите по ссылке:",
        action_path="/reset-password",
        token=token,
    )


def bytes_to_base64url(value: bytes) -> str:
    import base64

    return base64.urlsafe_b64encode(value).rstrip(b"=").decode("ascii")


def base64url_to_bytes(value: str) -> bytes:
    import base64

    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)


def credential_user_handle(user_id: uuid.UUID) -> bytes:
    return user_id.bytes