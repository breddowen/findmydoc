# ./backend/app/modules/videos/poster_service.py

import uuid
from datetime import timedelta

from fastapi import HTTPException
from sqlmodel import Session

from app.core.config import settings
from app.modules.media.models import MediaImage, utc_now_naive
from app.modules.media.storage import write_image
from app.modules.media.video_models import MediaVideoFile
from app.modules.media.video_posters import (
    PreparedVideoPoster,
    VideoPosterError,
    prepare_video_poster,
)
from app.modules.videos.models import Video


def prepare_poster_for_save(
    *,
    session: Session,
    user_id: uuid.UUID,
    wide_file_id: uuid.UUID | None,
    mobile_file_id: uuid.UUID | None,
    image_id: uuid.UUID | None,
    current_video: Video | None = None,
) -> tuple[PreparedVideoPoster | None, str | None]:
    """
    Проверяет источник, освобождает транзакцию
    и подготавливает WebP в памяти.

    На диск изображение пока не записывается.
    """
    if image_id is not None:
        return None, None

    if (
        current_video is not None
        and current_video.automatic_image_id is not None
    ):
        return None, None

    current_ids = set()

    if current_video is not None:
        current_ids = {
            file_id
            for file_id in (
                current_video.wide_file_id,
                current_video.mobile_file_id,
            )
            if file_id is not None
        }

    requested_ids = {
        file_id
        for file_id in (
            wide_file_id,
            mobile_file_id,
        )
        if file_id is not None
    }

    oldest_allowed = utc_now_naive() - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    candidates = []

    for file_id in requested_ids:
        file = session.get(MediaVideoFile, file_id)

        if file is None:
            raise HTTPException(
                status_code=409,
                detail="Видеофайл не найден",
            )

        if file_id in current_ids:
            allowed = file.is_attached
        else:
            allowed = (
                file.uploaded_by_user_id == user_id
                and not file.is_attached
                and file.created_at > oldest_allowed
            )

        if not allowed:
            raise HTTPException(
                status_code=409,
                detail="Видеофайл нельзя использовать",
            )

        candidates.append(
            (
                file.created_at,
                file.id.hex,
                file.id,
                file.duration_seconds,
            )
        )

    if not candidates:
        raise HTTPException(
            status_code=422,
            detail="Добавьте хотя бы один видеофайл",
        )

    # Первый загруженный файл из включённых в карточку.
    candidates.sort()
    _, _, source_id, duration = candidates[0]

    # Ни блокировки строк, ни соединение с БД
    # не удерживаются во время работы ffmpeg.
    session.rollback()

    try:
        return (
            prepare_video_poster(
                file_id=source_id,
                duration_seconds=duration,
            ),
            None,
        )
    except VideoPosterError as error:
        # Сам видеоматериал всё равно можно сохранить.
        return None, str(error)


def attach_automatic_poster(
    *,
    session: Session,
    video: Video,
    user_id: uuid.UUID,
    prepared: PreparedVideoPoster | None,
) -> bool:
    if prepared is None:
        return False

    if video.automatic_image_id is not None:
        return False

    if prepared.source_file_id not in {
        video.wide_file_id,
        video.mobile_file_id,
    }:
        raise HTTPException(
            status_code=409,
            detail=(
                "Источник автообложки изменился. "
                "Обновите данные и повторите действие."
            ),
        )

    image = MediaImage(
        purpose="video",
        uploaded_by_user_id=user_id,
        width=prepared.width,
        height=prepared.height,
        size_bytes=len(prepared.data),
        is_attached=True,
    )

    write_image(
        image_id=image.id,
        data=prepared.data,
    )

    session.add(image)
    session.flush()

    video.automatic_image_id = image.id
    session.add(video)

    return True