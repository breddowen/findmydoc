# ./backend/app/modules/videos/progress_routers.py

import uuid

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.core.transactions import lock_patient_for_write
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
)
from app.modules.events.enums import EventType
from app.modules.users.enums import UserRole
from app.modules.videos.access import ensure_video_access
from app.modules.videos.progress_schemas import (
    VideoOpenRequest,
    VideoOpenResponse,
    VideoProgressResponse,
    VideoProgressUpdateRequest,
)
from app.modules.videos.progress_service import (
    apply_video_progress,
    get_video_opening,
    get_video_progress,
    opening_stage_id,
    record_video_interaction_event,
    serialize_video_progress,
)
from app.modules.videos.service import get_video_or_404


router = APIRouter(
    prefix="/api/v1/videos",
    tags=["Videos: progress"],
)


@router.post(
    "/{video_id}/open",
    response_model=VideoOpenResponse,
)
def register_video_open(
    video_id: uuid.UUID,
    payload: VideoOpenRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> VideoOpenResponse:
    try:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        lock_patient_for_write(
            session=session,
            patient_id=patient.id,
        )

        video = get_video_or_404(
            session=session,
            video_id=video_id,
        )

        ensure_video_access(
            session=session,
            auth=auth,
            video=video,
            program_id=payload.program_id,
            program_stage_id=payload.program_stage_id,
        )

        event = record_video_interaction_event(
            session=session,
            event_type=EventType.VIDEO_OPENED,
            interaction_id=payload.interaction_id,
            patient_id=patient.id,
            video_id=video.id,
            actor_user_id=auth.user.id,
            program_id=payload.program_id,
            program_stage_id=payload.program_stage_id,
            source=(
                "program"
                if payload.program_id is not None
                else payload.source
            ),
        )

        progress = get_video_progress(
            session=session,
            video_id=video.id,
            patient_id=patient.id,
        )

        response = VideoOpenResponse(
            interaction_id=payload.interaction_id,
            event_id=event.id,
            progress=serialize_video_progress(
                video_id=video.id,
                progress=progress,
            ),
        )

        session.commit()
        return response

    except Exception:
        session.rollback()
        raise


@router.put(
    "/{video_id}/progress",
    response_model=VideoProgressResponse,
)
def update_video_progress(
    video_id: uuid.UUID,
    payload: VideoProgressUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> VideoProgressResponse:
    try:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        lock_patient_for_write(
            session=session,
            patient_id=patient.id,
        )

        opening = get_video_opening(
            session=session,
            interaction_id=payload.interaction_id,
            patient_id=patient.id,
            video_id=video_id,
        )

        video = get_video_or_404(
            session=session,
            video_id=video_id,
        )

        # Контекст берём из зарегистрированного открытия,
        # а не из произвольных новых параметров клиента.
        ensure_video_access(
            session=session,
            auth=auth,
            video=video,
            program_id=opening.program_id,
            program_stage_id=opening_stage_id(opening),
        )

        progress = apply_video_progress(
            session=session,
            opening=opening,
            actor_user_id=auth.user.id,
            action=payload.action,
            progress_percent=payload.progress_percent,
        )

        response = serialize_video_progress(
            video_id=video.id,
            progress=progress,
        )

        session.commit()
        return response

    except Exception:
        session.rollback()
        raise