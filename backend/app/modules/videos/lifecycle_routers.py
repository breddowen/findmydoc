# ./backend/app/modules/videos/lifecycle_routers.py

import uuid

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.users.enums import UserRole
from app.modules.videos.lifecycle import (
    delete_video_material,
    get_video_references,
    serialize_video_usage,
)
from app.modules.videos.lifecycle_schemas import (
    VideoDeleteRequest,
    VideoDeleteResponse,
    VideoUsageResponse,
)
from app.modules.videos.service import get_video_or_404


router = APIRouter(
    prefix="/api/v1/videos",
    tags=["Videos: lifecycle"],
)

MANAGER_ROLES = (
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
)


@router.get(
    "/manage/{video_id}/usage",
    response_model=VideoUsageResponse,
)
def get_video_usage(
    video_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoUsageResponse:
    video = get_video_or_404(
        session=session,
        video_id=video_id,
    )

    references = get_video_references(
        session=session,
        video_id=video.id,
    )

    return serialize_video_usage(
        video=video,
        references=references,
    )


@router.delete(
    "/manage/{video_id}",
    response_model=VideoDeleteResponse,
)
def delete_video(
    video_id: uuid.UUID,
    payload: VideoDeleteRequest,
    auth: AuthContext = Depends(
        require_roles(*MANAGER_ROLES)
    ),
    session: Session = Depends(get_session),
) -> VideoDeleteResponse:
    user_id = auth.user.id

    try:
        response = delete_video_material(
            session=session,
            video_id=video_id,
            payload=payload,
            actor_user_id=user_id,
        )

        session.commit()
        return response

    except Exception:
        session.rollback()
        raise