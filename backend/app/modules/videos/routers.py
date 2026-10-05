# ./backend/app/modules/videos/routers.py

import uuid

from fastapi import (
    APIRouter,
    Depends,
    Query,
)
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.media.models import utc_now_naive
from app.modules.users.enums import UserRole
from app.modules.videos.models import Video
from app.modules.videos.schemas import (
    VideoCreateRequest,
    VideoResponse,
    VideoUpdateRequest,
    VideoVisibilityRequest,
)
from app.modules.videos.service import (
    create_video,
    get_video_or_404,
    lock_video_for_write,
    serialize_video,
    update_video,
)
from fastapi import HTTPException

from app.modules.videos.poster_service import (
    attach_automatic_poster,
    prepare_poster_for_save,
)
from app.modules.videos.schemas import (
    VideoAutomaticPosterRequest,
)
from app.modules.videos.lifecycle import set_video_visibility

router = APIRouter(
    prefix="/api/v1/videos",
    tags=["Videos"],
)

MANAGER_ROLES = (
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
)

STAFF_ROLES = (
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
    UserRole.DOCTOR,
)


@router.get(
    "/manage",
    response_model=list[VideoResponse],
)
def list_videos_for_staff(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    search: str | None = Query(default=None, max_length=300),
    include_hidden: bool = True,
    _: AuthContext = Depends(
        require_roles(*STAFF_ROLES)
    ),
    session: Session = Depends(get_session),
) -> list[VideoResponse]:
    statement = select(Video)

    if not include_hidden:
        statement = statement.where(
            Video.is_hidden.is_(False)
        )

    if search and search.strip():
        # autoescape не позволяет символам % и _
        # неожиданно работать как шаблоны поиска.
        statement = statement.where(
            Video.title.icontains(
                search.strip(),
                autoescape=True,
            )
        )

    videos = session.exec(
        statement
        .order_by(
            Video.created_at.desc(),
            Video.id.asc(),
        )
        .offset(offset)
        .limit(limit)
    ).all()

    return [
        serialize_video(
            session=session,
            video=video,
        )
        for video in videos
    ]


@router.get(
    "/manage/{video_id}",
    response_model=VideoResponse,
)
def get_video_for_staff(
    video_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(*STAFF_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoResponse:
    video = get_video_or_404(
        session=session,
        video_id=video_id,
    )

    return serialize_video(
        session=session,
        video=video,
    )


@router.post(
    "/manage",
    response_model=VideoResponse,
    status_code=201,
)
def create_video_material(
    payload: VideoCreateRequest,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoResponse:
    user_id = auth.user.id

    try:
        prepared, warning = prepare_poster_for_save(
            session=session,
            user_id=user_id,
            wide_file_id=payload.wide_file_id,
            mobile_file_id=payload.mobile_file_id,
            image_id=payload.image_id,
        )

        # После подготовки повторно выполняется
        # атомарная проверка/привязка файлов.
        video = create_video(
            session=session,
            payload=payload,
            user_id=user_id,
            prepared_poster=prepared,
        )

        session.commit()
        session.refresh(video)

    except Exception:
        session.rollback()
        raise

    response = serialize_video(
        session=session,
        video=video,
    )
    response.poster_warning = warning

    return response


@router.put(
    "/manage/{video_id}",
    response_model=VideoResponse,
)
def update_video_material(
    video_id: uuid.UUID,
    payload: VideoUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoResponse:
    user_id = auth.user.id

    try:
        current = get_video_or_404(
            session=session,
            video_id=video_id,
        )

        if current.version != payload.expected_version:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Видео уже изменено. "
                    "Обновите данные и повторите действие."
                ),
            )

        next_image_id = (
            payload.image_id
            if "image_id" in payload.model_fields_set
            else current.image_id
        )

        prepared, warning = prepare_poster_for_save(
            session=session,
            user_id=user_id,
            wide_file_id=payload.wide_file_id,
            mobile_file_id=payload.mobile_file_id,
            image_id=next_image_id,
            current_video=current,
        )

        # Здесь снова проверяется версия под блокировкой.
        # Между предварительным чтением и сохранением
        # другой сотрудник мог изменить карточку.
        video = update_video(
            session=session,
            video_id=video_id,
            payload=payload,
            user_id=user_id,
            prepared_poster=prepared,
        )

        session.commit()
        session.refresh(video)

    except Exception:
        session.rollback()
        raise

    response = serialize_video(
        session=session,
        video=video,
    )
    response.poster_warning = warning

    return response


@router.patch(
    "/manage/{video_id}/visibility",
    response_model=VideoResponse,
)
def change_video_visibility(
    video_id: uuid.UUID,
    payload: VideoVisibilityRequest,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoResponse:
    user_id = auth.user.id

    try:
        video = set_video_visibility(
            session=session,
            video_id=video_id,
            expected_version=payload.expected_version,
            is_hidden=payload.is_hidden,
            actor_user_id=user_id,
        )

        session.commit()
        session.refresh(video)

    except Exception:
        session.rollback()
        raise

    return serialize_video(
        session=session,
        video=video,
    )

@router.post(
    "/manage/{video_id}/automatic-poster",
    response_model=VideoResponse,
)
def ensure_automatic_video_poster(
    video_id: uuid.UUID,
    payload: VideoAutomaticPosterRequest,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoResponse:
    user_id = auth.user.id

    try:
        current = get_video_or_404(
            session=session,
            video_id=video_id,
        )

        if current.version != payload.expected_version:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Видео уже изменено. "
                    "Обновите данные."
                ),
            )

        if current.automatic_image_id is not None:
            return serialize_video(
                session=session,
                video=current,
            )

        prepared, warning = prepare_poster_for_save(
            session=session,
            user_id=user_id,
            wide_file_id=current.wide_file_id,
            mobile_file_id=current.mobile_file_id,
            image_id=None,
            current_video=current,
        )

        video = lock_video_for_write(
            session=session,
            video_id=video_id,
            expected_version=payload.expected_version,
        )

        changed = attach_automatic_poster(
            session=session,
            video=video,
            user_id=user_id,
            prepared=prepared,
        )

        if changed:
            video.version += 1
            video.updated_at = utc_now_naive()
            session.add(video)

        session.commit()
        session.refresh(video)

    except Exception:
        session.rollback()
        raise

    response = serialize_video(
        session=session,
        video=video,
    )
    response.poster_warning = warning

    return response