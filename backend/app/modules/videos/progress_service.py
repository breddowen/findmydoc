# ./backend/app/modules/videos/progress_service.py

import uuid

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.modules.events.enums import EventType
from app.modules.events.models import Event
from app.modules.events.service import record_event
from app.modules.media.models import utc_now_naive
from app.modules.programs.utils import (
    sync_patient_program_enrollments,
)
from app.modules.videos.models import VideoProgress
from app.modules.videos.progress_schemas import (
    VideoProgressResponse,
)


VIDEO_COMPLETION_THRESHOLD = 90.0


def get_video_progress(
    *,
    session: Session,
    video_id: uuid.UUID,
    patient_id: uuid.UUID,
) -> VideoProgress | None:
    return session.exec(
        select(VideoProgress).where(
            VideoProgress.video_id == video_id,
            VideoProgress.patient_id == patient_id,
        )
    ).first()


def serialize_video_progress(
    *,
    video_id: uuid.UUID,
    progress: VideoProgress | None,
) -> VideoProgressResponse:
    return VideoProgressResponse(
        video_id=video_id,
        progress_percent=progress.progress_percent if progress else 0,
        max_progress_percent=(
            progress.max_progress_percent if progress else 0
        ),
        started_at=progress.started_at if progress else None,
        updated_at=progress.updated_at if progress else None,
        completed_at=progress.completed_at if progress else None,
        completion_method=progress.completion_method if progress else None,
    )


def record_video_interaction_event(
    *,
    session: Session,
    event_type: EventType,
    interaction_id: uuid.UUID,
    patient_id: uuid.UUID,
    video_id: uuid.UUID,
    actor_user_id: uuid.UUID,
    program_id: uuid.UUID | None,
    program_stage_id: uuid.UUID | None,
    source: str,
    metadata: dict | None = None,
) -> Event:
    stage_value = (
        str(program_stage_id)
        if program_stage_id is not None
        else None
    )

    def find_existing():
        return session.exec(
            select(Event).where(
                Event.event_type == event_type,
                Event.interaction_id == interaction_id,
            )
        ).first()

    def validate_existing(event):
        if (
            event.patient_id != patient_id
            or event.subject_type != "video"
            or event.subject_id != video_id
            or event.program_id != program_id
            or event.source != source
            or (event.metadata_json or {}).get("program_stage_id")
            != stage_value
        ):
            raise HTTPException(
                status_code=409,
                detail=(
                    "Идентификатор просмотра уже используется "
                    "в другом контексте"
                ),
            )

        return event

    existing = find_existing()

    if existing:
        return validate_existing(existing)

    try:
        with session.begin_nested():
            event = record_event(
                session=session,
                event_type=event_type,
                interaction_id=interaction_id,
                patient_id=patient_id,
                actor_user_id=actor_user_id,
                program_id=program_id,
                source=source,
                subject_type="video",
                subject_id=video_id,
                metadata={
                    **(metadata or {}),
                    "program_stage_id": stage_value,
                },
            )

            session.flush()

        return event

    except IntegrityError:
        existing = find_existing()

        if existing is None:
            raise

        return validate_existing(existing)


def get_video_opening(
    *,
    session: Session,
    interaction_id: uuid.UUID,
    patient_id: uuid.UUID,
    video_id: uuid.UUID,
) -> Event:
    opening = session.exec(
        select(Event).where(
            Event.event_type == EventType.VIDEO_OPENED,
            Event.interaction_id == interaction_id,
            Event.patient_id == patient_id,
            Event.subject_type == "video",
            Event.subject_id == video_id,
        )
    ).first()

    if opening is None:
        raise HTTPException(
            status_code=404,
            detail="Просмотр видео не зарегистрирован",
        )

    return opening


def opening_stage_id(opening: Event) -> uuid.UUID | None:
    value = (opening.metadata_json or {}).get("program_stage_id")

    if value is None:
        return None

    try:
        return uuid.UUID(value)
    except (ValueError, TypeError, AttributeError) as error:
        raise HTTPException(
            status_code=409,
            detail="Повреждён контекст просмотра",
        ) from error


def apply_video_progress(
    *,
    session: Session,
    opening: Event,
    actor_user_id: uuid.UUID,
    action: str,
    progress_percent: float | None,
) -> VideoProgress:
    patient_id = opening.patient_id
    video_id = opening.subject_id

    event_arguments = {
        "session": session,
        "interaction_id": opening.interaction_id,
        "patient_id": patient_id,
        "video_id": video_id,
        "actor_user_id": actor_user_id,
        "program_id": opening.program_id,
        "program_stage_id": opening_stage_id(opening),
        "source": opening.source,
    }

    if action == "progress":
        started_event = session.exec(
            select(Event.id).where(
                Event.event_type == EventType.VIDEO_STARTED,
                Event.interaction_id == opening.interaction_id,
                Event.patient_id == patient_id,
                Event.subject_id == video_id,
            )
        ).first()

        if started_event is None:
            raise HTTPException(
                status_code=409,
                detail="Сначала зарегистрируйте начало воспроизведения",
            )

    progress = get_video_progress(
        session=session,
        video_id=video_id,
        patient_id=patient_id,
    )

    if progress is None:
        progress = VideoProgress(
            video_id=video_id,
            patient_id=patient_id,
        )

    was_completed = progress.completed_at is not None
    now = utc_now_naive()

    if action == "started":
        record_video_interaction_event(
            event_type=EventType.VIDEO_STARTED,
            **event_arguments,
        )

    if action == "progress":
        normalized = round(progress_percent, 2)

        progress.progress_percent = normalized
        progress.max_progress_percent = max(
            progress.max_progress_percent,
            normalized,
        )

    should_complete = (
        action == "complete"
        or (
            action == "progress"
            and progress_percent >= VIDEO_COMPLETION_THRESHOLD
        )
    )

    if should_complete:
        method = "manual" if action == "complete" else "position"

        if not was_completed:
            progress.completed_at = now
            progress.completion_method = method

        record_video_interaction_event(
            event_type=EventType.VIDEO_COMPLETED,
            metadata={
                "completion_method": method,
                "progress_percent": progress.progress_percent,
                "max_progress_percent": progress.max_progress_percent,
            },
            **event_arguments,
        )

    progress.updated_at = now

    session.add(progress)
    session.flush()

    # Пожизненное завершение материала, как у статьи.
    # Программа пересчитывается только при первом завершении,
    # а не при каждом последующем timeupdate.
    if not was_completed and progress.completed_at is not None:
        sync_patient_program_enrollments(
            session=session,
            patient_id=patient_id,
        )

    return progress