# ./backend/app/modules/media/video_upload_routers.py

import asyncio
import logging
import threading
import time
import uuid
from datetime import timedelta
from pathlib import Path

from anyio import to_thread
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
)
from sqlmodel import Session
from starlette.requests import ClientDisconnect

from app.core.config import settings
from app.core.db import get_session, sqlite_engine
from app.core.security import (
    AuthContext,
    ensure_user_can_authenticate,
    require_roles,
)
from app.modules.media.models import utc_now_naive
from app.modules.media.video_container import (
    VideoValidationError,
)
from app.modules.media.video_models import MediaVideoFile
from app.modules.media.video_probe import (
    VideoProbeUnavailableError,
)
from app.modules.media.video_storage import (
    flush_video_upload,
    open_temporary_video,
    publish_staged_video_upload,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.utils import user_has_role
from app.modules.videos.schemas import (
    VideoUploadLimitsResponse,
    VideoUploadResponse,
)


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/media/video-uploads",
    tags=["Media: video uploads"],
)

MANAGER_ROLES = (
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
)

# Для текущего запуска uvicorn с одним worker.
# Загрузка и проверка одного ролика за раз.
#
# Это ограничение процесса, а не всего кластера.
# При переходе на несколько workers потребуется
# общее ограничение или отдельный upload-worker.
UPLOAD_SLOT = threading.BoundedSemaphore(1)

UPLOAD_IDLE_TIMEOUT_SECONDS = 60.0
UPLOAD_TOTAL_TIMEOUT_SECONDS = 15 * 60.0


def serialize_upload(file: MediaVideoFile) -> VideoUploadResponse:
    return VideoUploadResponse(
        id=file.id,
        width=file.width,
        height=file.height,
        rotation_degrees=file.rotation_degrees,
        duration_seconds=file.duration_seconds,
        fps=file.fps,
        size_bytes=file.size_bytes,
        has_audio=file.has_audio,
        created_at=file.created_at,
        expires_at=(
            file.created_at
            + timedelta(
                hours=settings.MEDIA_UPLOAD_TTL_HOURS,
            )
        ),
        suggested_slot=(
            "wide"
            if file.width >= file.height
            else "mobile"
        ),
    )


def finish_upload(
    *,
    path: Path,
    user_id: uuid.UUID,
    active_role: UserRole,
    auth_version: int,
    token_expires_at: float,
) -> VideoUploadResponse:
    # Длительную проверку выполняем без открытой
    # транзакции базы данных.
    stored = publish_staged_video_upload(path)

    # Здесь файл уже опубликован под случайным UUID.
    # Если запись в БД не состоится, файл позже должен
    # забрать сборщик непривязанных файлов.
    try:
        with Session(sqlite_engine) as session:
            user = ensure_user_can_authenticate(
                session.get(User, user_id)
            )

            if (
                user.auth_version != auth_version
                or token_expires_at <= time.time()
            ):
                raise HTTPException(
                    status_code=401,
                    detail=(
                        "Сессия истекла во время загрузки. "
                        "Войдите повторно."
                    ),
                )

            if not user_has_role(
                session,
                user.id,
                active_role,
            ):
                raise HTTPException(
                    status_code=403,
                    detail="Роль больше не доступна",
                )

            metadata = stored.metadata

            file = MediaVideoFile(
                id=stored.id,
                uploaded_by_user_id=user.id,
                width=metadata.width,
                height=metadata.height,
                rotation_degrees=metadata.rotation_degrees,
                duration_seconds=metadata.duration_seconds,
                fps=metadata.fps,
                size_bytes=metadata.size_bytes,
                has_audio=metadata.has_audio,
            )

            session.add(file)
            session.commit()
            session.refresh(file)

            return serialize_upload(file)

    except Exception:
        # Не удаляем опубликованный файл при ошибке commit:
        # его результат при потере соединения может
        # оказаться неопределённым.
        logger.exception(
            "Cannot register video upload %s",
            stored.id,
        )
        raise


@router.get(
    "/limits",
    response_model=VideoUploadLimitsResponse,
)
def get_video_upload_limits(
    _: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
) -> VideoUploadLimitsResponse:
    return VideoUploadLimitsResponse(
        max_bytes=settings.MEDIA_VIDEO_MAX_BYTES,
        max_duration_seconds=(
            settings.MEDIA_VIDEO_MAX_DURATION_SECONDS
        ),
        max_long_side=settings.MEDIA_VIDEO_MAX_LONG_SIDE,
        max_short_side=settings.MEDIA_VIDEO_MAX_SHORT_SIDE,
        max_fps=settings.MEDIA_VIDEO_MAX_FPS,
    )


@router.post(
    "",
    response_model=VideoUploadResponse,
    status_code=201,
    openapi_extra={
        "requestBody": {
            "required": True,
            "content": {
                "video/mp4": {
                    "schema": {
                        "type": "string",
                        "format": "binary",
                    },
                },
            },
        },
    },
)
async def upload_video_file(
    request: Request,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoUploadResponse:
    content_type = (
        request.headers.get("content-type", "")
        .split(";", 1)[0]
        .strip()
        .lower()
    )

    if content_type not in {
        "video/mp4",
        "application/octet-stream",
    }:
        raise HTTPException(
            status_code=415,
            detail=(
                "Отправьте MP4 непосредственно в теле запроса. "
                "multipart/form-data здесь не используется."
            ),
        )

    declared_size: int | None = None
    content_length = request.headers.get("content-length")

    if content_length is not None:
        try:
            declared_size = int(content_length)
        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail="Некорректный Content-Length",
            ) from error

        if declared_size <= 0:
            raise HTTPException(
                status_code=400,
                detail="Загружен пустой файл",
            )

        if declared_size > settings.MEDIA_VIDEO_MAX_BYTES:
            raise HTTPException(
                status_code=413,
                detail="Видео превышает допустимый размер",
            )

    if not UPLOAD_SLOT.acquire(blocking=False):
        raise HTTPException(
            status_code=429,
            detail=(
                "Сейчас загружается другое видео. "
                "Повторите попытку после его загрузки."
            ),
            headers={"Retry-After": "10"},
        )

    temporary = None
    temporary_path: Path | None = None

    try:
        # Сохраняем только нужные значения:
        # rollback ниже освобождает транзакцию авторизации.
        user_id = auth.user.id
        active_role = auth.active_role
        auth_version = auth.user.auth_version
        token_expires_at = float(
            auth.token_payload["exp"]
        )

        session.rollback()

        temporary = await to_thread.run_sync(
            open_temporary_video
        )
        temporary_path = Path(temporary.name)

        iterator = request.stream().__aiter__()
        deadline = (
            time.monotonic()
            + UPLOAD_TOTAL_TIMEOUT_SECONDS
        )

        received_bytes = 0

        while True:
            remaining_time = deadline - time.monotonic()

            if remaining_time <= 0:
                raise HTTPException(
                    status_code=408,
                    detail="Превышено время загрузки видео",
                )

            try:
                chunk = await asyncio.wait_for(
                    iterator.__anext__(),
                    timeout=min(
                        UPLOAD_IDLE_TIMEOUT_SECONDS,
                        remaining_time,
                    ),
                )
            except StopAsyncIteration:
                break
            except asyncio.TimeoutError as error:
                raise HTTPException(
                    status_code=408,
                    detail=(
                        "Загрузка прервана: данные "
                        "слишком долго не поступали."
                    ),
                ) from error

            if not chunk:
                continue

            received_bytes += len(chunk)

            if received_bytes > settings.MEDIA_VIDEO_MAX_BYTES:
                raise HTTPException(
                    status_code=413,
                    detail="Видео превышает допустимый размер",
                )

            await to_thread.run_sync(
                temporary.write,
                chunk,
            )

        if received_bytes == 0:
            raise HTTPException(
                status_code=400,
                detail="Загружен пустой файл",
            )

        if (
            declared_size is not None
            and received_bytes != declared_size
        ):
            raise HTTPException(
                status_code=400,
                detail="Видео загружено не полностью",
            )

        await to_thread.run_sync(
            flush_video_upload,
            temporary,
        )

        # Windows не позволяет повторно открыть
        # некоторые временные файлы до их закрытия.
        await to_thread.run_sync(temporary.close)
        temporary = None

        return await to_thread.run_sync(
            lambda: finish_upload(
                path=temporary_path,
                user_id=user_id,
                active_role=active_role,
                auth_version=auth_version,
                token_expires_at=token_expires_at,
            )
        )

    except ClientDisconnect as error:
        raise HTTPException(
            status_code=400,
            detail="Соединение прервано во время загрузки",
        ) from error

    except VideoValidationError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error

    except VideoProbeUnavailableError as error:
        logger.exception("Video probe is unavailable")

        raise HTTPException(
            status_code=503,
            detail=(
                "Проверка видео недоступна. "
                "Проверьте установку ffprobe на сервере."
            ),
        ) from error

    except OSError as error:
        logger.exception("Video upload storage error")

        raise HTTPException(
            status_code=503,
            detail=(
                "Не удалось сохранить видео. "
                "Возможно, недостаточно места "
                "или хранилище недоступно."
            ),
        ) from error

    finally:
        try:
            if temporary is not None:
                temporary.close()

            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
        finally:
            UPLOAD_SLOT.release()


@router.get(
    "/{file_id}",
    response_model=VideoUploadResponse,
)
def get_temporary_video_upload(
    file_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoUploadResponse:
    file = session.get(MediaVideoFile, file_id)

    if (
        file is None
        or file.uploaded_by_user_id != auth.user.id
        or file.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Временная загрузка не найдена",
        )

    expires_at = file.created_at + timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    if expires_at <= utc_now_naive():
        raise HTTPException(
            status_code=410,
            detail=(
                "Срок временной загрузки истёк. "
                "Загрузите видео повторно."
            ),
        )

    return serialize_upload(file)