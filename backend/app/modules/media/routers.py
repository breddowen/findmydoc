# backend\app\modules\media\routers.py

import logging
import uuid
from datetime import timedelta

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    get_current_auth,
    require_roles,
)
from app.modules.media.constants import (
    IMAGE_PRESETS,
    ImagePurpose,
)
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.processing import (
    CropRectangle,
    ImageProcessingError,
    process_image,
)
from app.modules.media.schemas import (
    MediaImageUploadResponse,
)
from app.modules.media.storage import (
    image_path,
    write_image,
)
from app.modules.users.enums import UserRole


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/media",
    tags=["Media"],
)


def ensure_upload_permission(
    *,
    auth: AuthContext,
    purpose: ImagePurpose,
) -> None:
    if auth.active_role in {
        UserRole.SUPERUSER,
        UserRole.MED_ASSISTANT,
    }:
        return

    if (
        auth.active_role == UserRole.DOCTOR
        and purpose in {"doctor", "article"}
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Нет прав на загрузку этого изображения",
    )


def get_owned_temporary_image(
    *,
    session: Session,
    image_id: uuid.UUID,
    auth: AuthContext,
) -> MediaImage:
    image = session.get(MediaImage, image_id)

    # Возвращаем одинаковый ответ для чужого,
    # отсутствующего и уже привязанного изображения.
    if (
        image is None
        or image.uploaded_by_user_id != auth.user.id
        or image.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение не найдено",
        )

    ensure_upload_permission(
        auth=auth,
        purpose=image.purpose,
    )

    expires_at = image.created_at + timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    if expires_at <= utc_now_naive():
        raise HTTPException(
            status_code=410,
            detail=(
                "Срок временной загрузки истёк. "
                "Загрузите изображение повторно."
            ),
        )

    return image


@router.post(
    "/uploads",
    response_model=MediaImageUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_image(
    purpose: ImagePurpose = Form(...),
    crop_left: int = Form(..., ge=0),
    crop_top: int = Form(..., ge=0),
    crop_width: int = Form(..., gt=0),
    crop_height: int = Form(..., gt=0),
    file: UploadFile = File(...),
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> MediaImageUploadResponse:
    ensure_upload_permission(
        auth=auth,
        purpose=purpose,
    )

    try:
        # Читаем не больше лимита плюс один байт.
        source = file.file.read(
            settings.MEDIA_IMAGE_MAX_BYTES + 1
        )
    finally:
        file.file.close()

    if len(source) > settings.MEDIA_IMAGE_MAX_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_CONTENT_TOO_LARGE,
            detail="Размер изображения превышает 10 МБ",
        )

    try:
        processed = process_image(
            source=source,
            crop=CropRectangle(
                left=crop_left,
                top=crop_top,
                width=crop_width,
                height=crop_height,
            ),
            preset=IMAGE_PRESETS[purpose],
        )
    except ImageProcessingError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error

    image = MediaImage(
        purpose=purpose,
        uploaded_by_user_id=auth.user.id,
        width=processed.width,
        height=processed.height,
        size_bytes=len(processed.data),
    )

    try:
        write_image(
            image_id=image.id,
            data=processed.data,
        )
    except OSError as error:
        logger.exception(
            "Cannot write media image %s",
            image.id,
        )

        raise HTTPException(
            status_code=503,
            detail="Хранилище изображений временно недоступно",
        ) from error

    try:
        session.add(image)
        session.commit()
    except Exception:
        session.rollback()

        # Не удаляем файл немедленно:
        # при потере соединения во время commit
        # результат транзакции может быть неопределённым.
        #
        # Файлы без записи в БД заберёт безопасная
        # фоновая очистка с периодом ожидания.
        logger.exception(
            "Cannot save media metadata for %s",
            image.id,
        )
        raise

    return MediaImageUploadResponse(
        id=image.id,
        purpose=image.purpose,
        width=image.width,
        height=image.height,
        size_bytes=image.size_bytes,
        created_at=image.created_at,
        preview_path=(
            f"/api/v1/media/uploads/{image.id}/preview"
        ),
    )


@router.get(
    "/uploads/{image_id}/preview",
    response_class=FileResponse,
)
def preview_uploaded_image(
    image_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> FileResponse:
    image = get_owned_temporary_image(
        session=session,
        image_id=image_id,
        auth=auth,
    )

    path = image_path(image.id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл изображения не найден",
        )

    return FileResponse(
        path=path,
        media_type="image/webp",
        headers={
            "Cache-Control": "private, no-store",
            "Vary": "Authorization",
            "X-Content-Type-Options": "nosniff",
            "Content-Disposition": "inline",
        },
    )