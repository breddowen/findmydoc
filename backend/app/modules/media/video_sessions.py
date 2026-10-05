# ./backend/app/modules/media/video_sessions.py

import hashlib
import re
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    Response,
)
from pydantic import BaseModel
from sqlalchemy import delete
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    ensure_user_can_authenticate,
    require_roles,
)
from app.modules.media.models import utc_now_naive
from app.modules.media.session_models import (
    MediaPlaybackSession,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.utils import user_has_role


router = APIRouter(
    prefix="/api/v1/videos/media-session",
    tags=["Videos: playback session"],
)

COOKIE_NAME = "findmydoc_video_session"
COOKIE_PATH = "/api/v1/videos"

TOKEN_PATTERN = re.compile(r"^[A-Za-z0-9_-]{43}$")

PLAYBACK_ROLES = (
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
    UserRole.DOCTOR,
    UserRole.PATIENT,
)


class MediaSessionResponse(BaseModel):
    expires_at: datetime
    expires_in_seconds: int


def playback_token_hash(value: str | None) -> str | None:
    if not value or not TOKEN_PATTERN.fullmatch(value):
        return None

    return hashlib.sha256(
        value.encode("ascii")
    ).hexdigest()


def ensure_allowed_origin(request: Request) -> None:
    """
    Защита cookie-операций от запросов с чужого origin.

    Отсутствие Origin допустимо для CLI-клиентов.
    Браузерный межсайтовый fetch отправляет Origin.
    Дополнительная защита — SameSite=Strict.
    """
    origin = request.headers.get("origin")

    if origin is None:
        return

    configured = urlsplit(settings.FRONTEND_URL)
    expected = f"{configured.scheme}://{configured.netloc}"

    if origin != expected:
        raise HTTPException(
            status_code=403,
            detail="Недопустимый источник запроса",
        )


def delete_session_by_cookie(
    *,
    session: Session,
    request: Request,
) -> None:
    token_hash = playback_token_hash(
        request.cookies.get(COOKIE_NAME)
    )

    if token_hash is None:
        return

    session.execute(
        delete(MediaPlaybackSession).where(
            MediaPlaybackSession.token_hash == token_hash
        )
    )


@router.post(
    "",
    response_model=MediaSessionResponse,
)
def create_playback_session(
    request: Request,
    response: Response,
    auth: AuthContext = Depends(
        require_roles(*PLAYBACK_ROLES)
    ),
    session: Session = Depends(get_session),
) -> MediaSessionResponse:
    ensure_allowed_origin(request)

    now = datetime.now(timezone.utc)

    try:
        access_expires_at = datetime.fromtimestamp(
            float(auth.token_payload["exp"]),
            tz=timezone.utc,
        )
    except (KeyError, ValueError, TypeError, OverflowError) as error:
        raise HTTPException(
            status_code=401,
            detail="Некорректный срок действия сессии",
        ) from error

    expires_at = min(
        now + timedelta(
            seconds=settings.MEDIA_VIDEO_SESSION_SECONDS
        ),
        access_expires_at,
    )

    expires_in = int(
        (expires_at - now).total_seconds()
    )

    if expires_in < 1:
        raise HTTPException(
            status_code=401,
            detail="Сессия истекла",
        )

    secret = secrets.token_urlsafe(32)
    token_hash = playback_token_hash(secret)

    try:
        # Меняем только медиасессию этого браузера.
        # Другие устройства пользователя не отключаем.
        delete_session_by_cookie(
            session=session,
            request=request,
        )

        session.add(
            MediaPlaybackSession(
                token_hash=token_hash,
                user_id=auth.user.id,
                active_role=auth.active_role.value,
                auth_version=auth.user.auth_version,
                expires_at=expires_at.replace(tzinfo=None),
            )
        )

        session.commit()

    except Exception:
        session.rollback()
        raise

    response.set_cookie(
        key=COOKIE_NAME,
        value=secret,
        max_age=expires_in,
        path=COOKIE_PATH,
        secure=settings.MEDIA_VIDEO_COOKIE_SECURE,
        httponly=True,
        samesite="strict",
    )

    response.headers["Cache-Control"] = "private, no-store"
    response.headers["Vary"] = "Cookie"

    return MediaSessionResponse(
        expires_at=expires_at,
        expires_in_seconds=expires_in,
    )


@router.delete(
    "",
    status_code=204,
)
def revoke_playback_session(
    request: Request,
    session: Session = Depends(get_session),
) -> Response:
    ensure_allowed_origin(request)

    # Bearer здесь намеренно не обязателен:
    # удалить медиасессию нужно и после истечения
    # основного access token.
    try:
        delete_session_by_cookie(
            session=session,
            request=request,
        )
        session.commit()

    except Exception:
        session.rollback()
        raise

    response = Response(status_code=204)

    response.delete_cookie(
        key=COOKIE_NAME,
        path=COOKIE_PATH,
        secure=settings.MEDIA_VIDEO_COOKIE_SECURE,
        httponly=True,
        samesite="strict",
    )

    response.headers["Cache-Control"] = "private, no-store"

    return response


def get_current_media_auth(
    request: Request,
    session: Session = Depends(get_session),
) -> AuthContext:
    token_hash = playback_token_hash(
        request.cookies.get(COOKIE_NAME)
    )

    if token_hash is None:
        raise HTTPException(
            status_code=401,
            detail="Требуется медиасессия",
        )

    media_session = session.get(
        MediaPlaybackSession,
        token_hash,
    )

    if (
        media_session is None
        or media_session.expires_at <= utc_now_naive()
    ):
        raise HTTPException(
            status_code=401,
            detail="Медиасессия истекла",
        )

    user = ensure_user_can_authenticate(
        session.get(User, media_session.user_id)
    )

    if user.auth_version != media_session.auth_version:
        raise HTTPException(
            status_code=401,
            detail="Медиасессия больше не действительна",
        )

    try:
        active_role = UserRole(media_session.active_role)
    except ValueError as error:
        raise HTTPException(
            status_code=401,
            detail="Некорректная роль медиасессии",
        ) from error

    if (
        active_role not in PLAYBACK_ROLES
        or not user_has_role(
            session,
            user.id,
            active_role,
        )
    ):
        raise HTTPException(
            status_code=403,
            detail="Роль больше не доступна",
        )

    return AuthContext(
        user=user,
        active_role=active_role,
        token_payload={
            "type": "media",
            "sub": str(user.id),
            "role": active_role.value,
            "auth_version": user.auth_version,
        },
    )