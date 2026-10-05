# ./backend/app/modules/videos/delivery_routers.py

import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, Response
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.core.security import AuthContext, get_current_auth
from app.modules.media.video_models import MediaVideoFile
from app.modules.media.video_sessions import (
    get_current_media_auth,
)
from app.modules.media.video_storage import video_path
from app.modules.videos.access import ensure_video_access
from app.modules.videos.schemas import VideoResponse
from app.modules.videos.service import (
    get_video_or_404,
    serialize_video,
)
from app.modules.media.models import MediaImage
from app.modules.media.storage import image_path
from app.modules.videos.access import ensure_video_poster_access

router = APIRouter(
    prefix="/api/v1/videos",
    tags=["Videos: playback"],
)


def video_file_response(
    *,
    path: Path,
    file_id: uuid.UUID,
) -> Response:
    headers = {
        "Cache-Control": "private, no-store",
        "Vary": "Cookie",
        "X-Content-Type-Options": "nosniff",
        "Content-Disposition": "inline",
        "Cross-Origin-Resource-Policy": "same-site",
    }

    prefix = settings.MEDIA_VIDEO_X_ACCEL_PREFIX

    if prefix:
        if (
            not prefix.startswith("/")
            or not prefix.endswith("/")
            or "?" in prefix
            or "#" in prefix
            or "\r" in prefix
            or "\n" in prefix
        ):
            raise RuntimeError(
                "Некорректный MEDIA_VIDEO_X_ACCEL_PREFIX"
            )

        identifier = file_id.hex

        headers["X-Accel-Redirect"] = (
            f"{prefix}{identifier[:2]}/{identifier}.mp4"
        )

        response = Response(
            media_type="video/mp4",
            headers=headers,
        )

        # Фактическую длину и диапазон определит Nginx.
        if "content-length" in response.headers:
            del response.headers["content-length"]

        return response

    return FileResponse(
        path=path,
        media_type="video/mp4",
        headers=headers,
    )


@router.get(
    "/{video_id}",
    response_model=VideoResponse,
)
def get_video_for_playback(
    video_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> VideoResponse:
    video = get_video_or_404(
        session=session,
        video_id=video_id,
    )

    ensure_video_access(
        session=session,
        auth=auth,
        video=video,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    return serialize_video(
        session=session,
        video=video,
    )


@router.get(
    "/{video_id}/files/{file_id}",
    response_model=None,
    operation_id="get_video_file",
)
@router.head(
    "/{video_id}/files/{file_id}",
    response_model=None,
    include_in_schema=False,
)
def get_video_file(
    video_id: uuid.UUID,
    file_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_media_auth),
    session: Session = Depends(get_session),
) -> Response:
    video = get_video_or_404(
        session=session,
        video_id=video_id,
    )

    ensure_video_access(
        session=session,
        auth=auth,
        video=video,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    # Защита от подстановки чужого файла и запроса
    # старой версии после замены.
    if file_id not in {
        video.wide_file_id,
        video.mobile_file_id,
    }:
        raise HTTPException(
            status_code=404,
            detail="Видеофайл не найден",
        )

    file = session.get(MediaVideoFile, file_id)

    if file is None or not file.is_attached:
        raise HTTPException(
            status_code=404,
            detail="Видеофайл не найден",
        )

    path = video_path(file_id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл отсутствует в хранилище",
        )

    # Не держим соединение с БД на всё время
    # передачи большого файла локальным FileResponse.
    session.rollback()

    return video_file_response(
        path=path,
        file_id=file_id,
    )

@router.get(
    "/{video_id}/poster",
    response_class=FileResponse,
)
def get_video_poster(
    video_id: uuid.UUID,
    image_id: uuid.UUID | None = None,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> FileResponse:
    video = get_video_or_404(
        session=session,
        video_id=video_id,
    )

    ensure_video_poster_access(
        session=session,
        auth=auth,
        video=video,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    current_image_id = (
        video.image_id
        or video.automatic_image_id
    )

    if (
        current_image_id is None
        or (
            image_id is not None
            and image_id != current_image_id
        )
    ):
        raise HTTPException(
            status_code=404,
            detail="Обложка отсутствует или уже изменена",
        )

    image = session.get(
        MediaImage,
        current_image_id,
    )

    if (
        image is None
        or image.purpose != "video"
        or not image.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Обложка не найдена",
        )

    path = image_path(image.id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл обложки отсутствует",
        )

    session.rollback()

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