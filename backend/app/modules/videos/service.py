# ./backend/app/modules/videos/service.py

import uuid
from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy import update
from sqlmodel import Session, select

from app.core.config import settings
from app.modules.media.models import utc_now_naive
from app.modules.media.video_models import MediaVideoFile
from app.modules.media.video_storage import video_path
from app.modules.tags.models import Tag
from app.modules.videos.models import Video, VideoTagLink
from app.modules.videos.schemas import (
    VideoCreateRequest,
    VideoFileResponse,
    VideoResponse,
    VideoTagResponse,
    VideoUpdateRequest,
)
from app.modules.media.service import set_entity_image
from app.modules.media.video_posters import PreparedVideoPoster
from app.modules.videos.poster_service import (
    attach_automatic_poster,
)

def get_video_or_404(
    *,
    session: Session,
    video_id: uuid.UUID,
) -> Video:
    video = session.get(Video, video_id)

    if video is None:
        raise HTTPException(
            status_code=404,
            detail="Видео не найдено",
        )

    return video


def lock_video_for_write(
    *,
    session: Session,
    video_id: uuid.UUID,
    expected_version: int,
) -> Video:
    result = session.execute(
        update(Video)
        .where(Video.id == video_id)
        .values(version=Video.version)
        .execution_options(synchronize_session=False)
    )

    if result.rowcount != 1:
        raise HTTPException(
            status_code=404,
            detail="Видео не найдено",
        )

    video = session.get(Video, video_id)
    session.refresh(video)

    if video.version != expected_version:
        raise HTTPException(
            status_code=409,
            detail=(
                "Видео уже изменено другим запросом. "
                "Обновите страницу и повторите действие."
            ),
        )

    return video


def validate_tags(
    *,
    session: Session,
    tag_ids: list[uuid.UUID],
) -> None:
    if not tag_ids:
        return

    found_ids = set(
        session.exec(
            select(Tag.id).where(
                Tag.id.in_(tag_ids)
            )
        ).all()
    )

    if found_ids != set(tag_ids):
        raise HTTPException(
            status_code=404,
            detail="Один или несколько тегов не найдены",
        )


def replace_video_tags(
    *,
    session: Session,
    video_id: uuid.UUID,
    tag_ids: list[uuid.UUID],
) -> None:
    links = session.exec(
        select(VideoTagLink).where(
            VideoTagLink.video_id == video_id
        )
    ).all()

    old_by_tag_id = {
        link.tag_id: link
        for link in links
    }

    old_ids = set(old_by_tag_id)
    new_ids = set(tag_ids)

    for tag_id in old_ids - new_ids:
        session.delete(old_by_tag_id[tag_id])

    for tag_id in new_ids - old_ids:
        session.add(
            VideoTagLink(
                video_id=video_id,
                tag_id=tag_id,
            )
        )


def claim_video_files(
    *,
    session: Session,
    requested_ids: set[uuid.UUID],
    current_ids: set[uuid.UUID],
    uploaded_by_user_id: uuid.UUID,
) -> None:
    oldest_allowed = utc_now_naive() - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    # Стабильный порядок снижает вероятность
    # взаимных блокировок при конкурентных запросах.
    for file_id in sorted(requested_ids, key=str):
        if not video_path(file_id).is_file():
            raise HTTPException(
                status_code=409,
                detail=(
                    "Файл видео отсутствует. "
                    "Загрузите его повторно."
                ),
            )

        if file_id in current_ids:
            file = session.get(MediaVideoFile, file_id)

            if file is None or not file.is_attached:
                raise HTTPException(
                    status_code=409,
                    detail="Нарушена связь с видеофайлом",
                )

            continue

        # Новый файл можно забрать только из собственной
        # актуальной временной загрузки.
        result = session.execute(
            update(MediaVideoFile)
            .where(
                MediaVideoFile.id == file_id,
                MediaVideoFile.uploaded_by_user_id
                == uploaded_by_user_id,
                MediaVideoFile.is_attached.is_(False),
                MediaVideoFile.created_at > oldest_allowed,
            )
            .values(
                is_attached=True,
                retired_at=None,
            )
            .execution_options(synchronize_session=False)
        )

        if result.rowcount != 1:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Видеофайл нельзя использовать: "
                    "он принадлежит другому пользователю, "
                    "уже привязан или срок загрузки истёк."
                ),
            )


def create_video(
    *,
    session: Session,
    payload: VideoCreateRequest,
    user_id: uuid.UUID,
    prepared_poster: PreparedVideoPoster | None = None,
) -> Video:
    validate_tags(
        session=session,
        tag_ids=payload.tag_ids,
    )

    file_ids = {
        file_id
        for file_id in (
            payload.wide_file_id,
            payload.mobile_file_id,
        )
        if file_id is not None
    }

    claim_video_files(
        session=session,
        requested_ids=file_ids,
        current_ids=set(),
        uploaded_by_user_id=user_id,
    )

    video = Video(
        title=payload.title,
        pro_content=payload.pro_content,
        is_library_hidden=payload.is_library_hidden,
        wide_file_id=payload.wide_file_id,
        mobile_file_id=payload.mobile_file_id,
        created_by_user_id=user_id,
    )

    session.add(video)
    session.flush()

    replace_video_tags(
        session=session,
        video_id=video.id,
        tag_ids=payload.tag_ids,
    )

    set_entity_image(
        session=session,
        entity=video,
        purpose="video",
        image_id=payload.image_id,
        uploaded_by_user_id=user_id,
    )

    attach_automatic_poster(
        session=session,
        video=video,
        user_id=user_id,
        prepared=prepared_poster,
    )

    return video


def update_video(
    *,
    session: Session,
    video_id: uuid.UUID,
    payload: VideoUpdateRequest,
    user_id: uuid.UUID,
    prepared_poster: PreparedVideoPoster | None = None,
) -> Video:
    video = lock_video_for_write(
        session=session,
        video_id=video_id,
        expected_version=payload.expected_version,
    )

    validate_tags(
        session=session,
        tag_ids=payload.tag_ids,
    )

    current_ids = {
        file_id
        for file_id in (
            video.wide_file_id,
            video.mobile_file_id,
        )
        if file_id is not None
    }

    requested_ids = {
        file_id
        for file_id in (
            payload.wide_file_id,
            payload.mobile_file_id,
        )
        if file_id is not None
    }

    claim_video_files(
        session=session,
        requested_ids=requested_ids,
        current_ids=current_ids,
        uploaded_by_user_id=user_id,
    )

    video.title = payload.title
    video.pro_content = payload.pro_content
    video.is_library_hidden = payload.is_library_hidden

    # Оба назначения изменяются в одной транзакции.
    # Если поменять UUID местами — произойдёт перестановка,
    # а не повторная загрузка файлов.
    video.wide_file_id = payload.wide_file_id
    video.mobile_file_id = payload.mobile_file_id

    video.version += 1
    video.updated_at = utc_now_naive()

    session.add(video)

    replace_video_tags(
        session=session,
        video_id=video.id,
        tag_ids=payload.tag_ids,
    )

    retired_ids = current_ids - requested_ids

    if retired_ids:
        session.execute(
            update(MediaVideoFile)
            .where(
                MediaVideoFile.id.in_(retired_ids)
            )
            .values(retired_at=utc_now_naive())
            .execution_options(synchronize_session=False)
        )

    # Старый клиент без image_id не должен
    # случайно удалить ручную обложку.
    if "image_id" in payload.model_fields_set:
        set_entity_image(
            session=session,
            entity=video,
            purpose="video",
            image_id=payload.image_id,
            uploaded_by_user_id=user_id,
        )

    attach_automatic_poster(
        session=session,
        video=video,
        user_id=user_id,
        prepared=prepared_poster,
    )

    # Старые файлы здесь не удаляем.
    # Они перестали использоваться, но их физическое
    # удаление выполняется отдельной очисткой.
    return video


def serialize_video(
    *,
    session: Session,
    video: Video,
) -> VideoResponse:
    def serialize_file(
        file_id: uuid.UUID | None,
    ) -> VideoFileResponse | None:
        if file_id is None:
            return None

        file = session.get(MediaVideoFile, file_id)

        if file is None or not file.is_attached:
            raise HTTPException(
                status_code=409,
                detail="Нарушена связь с видеофайлом",
            )

        return VideoFileResponse.model_validate(file)

    tags = session.exec(
        select(Tag)
        .join(
            VideoTagLink,
            VideoTagLink.tag_id == Tag.id,
        )
        .where(VideoTagLink.video_id == video.id)
    ).all()

    tags = sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )

    return VideoResponse(
        id=video.id,
        title=video.title,
        pro_content=video.pro_content,
        is_hidden=video.is_hidden,
        is_library_hidden=video.is_library_hidden,
        wide_file=serialize_file(video.wide_file_id),
        mobile_file=serialize_file(video.mobile_file_id),
        tags=[
            VideoTagResponse.model_validate(tag)
            for tag in tags
        ],
        version=video.version,
        created_by_user_id=video.created_by_user_id,
        created_at=video.created_at,
        updated_at=video.updated_at,
        hidden_at=video.hidden_at,

        image_id=video.image_id,
        automatic_image_id=video.automatic_image_id,
        poster_image_id=(
            video.image_id
            or video.automatic_image_id
        ),
    )