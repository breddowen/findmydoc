# ./backend/app/modules/videos/lifecycle.py

import hashlib
import json
import uuid
from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy import delete, or_, update
from sqlmodel import Session, select

from app.core.transactions import lock_patient_for_write
from app.modules.events.models import Event
from app.modules.media.models import MediaImage, utc_now_naive
from app.modules.media.video_models import MediaVideoFile
from app.modules.programs.enums import ProgramEnrollmentStatus
from app.modules.programs.models import (
    Program,
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
)
from app.modules.programs.utils import sync_program_enrollment
from app.modules.videos.lifecycle_schemas import (
    VideoDeleteRequest,
    VideoDeleteResponse,
    VideoProgramUsage,
    VideoUsageResponse,
)
from app.modules.videos.models import (
    Video,
    VideoProgress,
    VideoTagLink,
)


@dataclass(frozen=True)
class VideoReference:
    program_id: uuid.UUID
    program_title: str
    program_hidden: bool

    stage_id: uuid.UUID
    stage_title: str

    item_id: uuid.UUID


def get_video_references(
    *,
    session: Session,
    video_id: uuid.UUID,
) -> list[VideoReference]:
    rows = session.exec(
        select(
            Program.id,
            Program.title,
            Program.is_hidden,
            ProgramStage.id,
            ProgramStage.title,
            ProgramStageItem.id,
        )
        .select_from(ProgramStageItem)
        .join(
            ProgramStage,
            ProgramStage.id == ProgramStageItem.stage_id,
        )
        .join(
            Program,
            Program.id == ProgramStage.program_id,
        )
        .where(ProgramStageItem.video_id == video_id)
    ).all()

    return [
        VideoReference(*row)
        for row in rows
    ]


def make_usage_token(
    *,
    video_id: uuid.UUID,
    references: list[VideoReference],
) -> str:
    payload = {
        "video_id": str(video_id),
        "references": [
            {
                "program_id": str(item.program_id),
                "program_title": item.program_title,
                "program_hidden": item.program_hidden,
                "stage_id": str(item.stage_id),
                "stage_title": item.stage_title,
                "item_id": str(item.item_id),
            }
            for item in sorted(
                references,
                key=lambda value: str(value.item_id),
            )
        ],
    }

    encoded = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")

    return hashlib.sha256(encoded).hexdigest()


def serialize_video_usage(
    *,
    video: Video,
    references: list[VideoReference],
) -> VideoUsageResponse:
    programs = {}

    for item in references:
        if item.program_id not in programs:
            programs[item.program_id] = VideoProgramUsage(
                id=item.program_id,
                title=item.program_title,
                is_hidden=item.program_hidden,
                item_count=0,
            )

        programs[item.program_id].item_count += 1

    sorted_programs = sorted(
        programs.values(),
        key=lambda item: (
            item.title.casefold(),
            str(item.id),
        ),
    )

    return VideoUsageResponse(
        video_id=video.id,
        title=video.title,
        version=video.version,
        program_count=len(sorted_programs),
        item_count=len(references),
        programs=sorted_programs,
        usage_token=make_usage_token(
            video_id=video.id,
            references=references,
        ),
    )


def lock_video_references(
    *,
    session: Session,
    video_ids: set[uuid.UUID],
) -> None:
    """
    Вызывается при сохранении программы.

    Не позволяет одновременно добавить ссылку
    на видео, которое уже удаляется.
    """
    for video_id in sorted(video_ids, key=str):
        result = session.execute(
            update(Video)
            .where(Video.id == video_id)
            .values(version=Video.version)
            .execution_options(synchronize_session=False)
        )

        if result.rowcount != 1:
            raise HTTPException(
                status_code=404,
                detail=(
                    "Одно из видео уже удалено. "
                    "Обновите библиотеку программы."
                ),
            )

        # Обновляем также ранее прочитанный ORM-объект.
        video = session.get(Video, video_id)
        session.refresh(video)


def lock_video_with_programs(
    *,
    session: Session,
    video_id: uuid.UUID,
    expected_version: int,
) -> tuple[Video, list[VideoReference]]:
    from app.modules.videos.service import lock_video_for_write

    initial_references = get_video_references(
        session=session,
        video_id=video_id,
    )

    program_ids = {
        item.program_id
        for item in initial_references
    }

    # Единый порядок блокировок:
    # программы -> видео -> пациенты.
    for program_id in sorted(program_ids, key=str):
        result = session.execute(
            update(Program)
            .where(Program.id == program_id)
            .values(updated_at=Program.updated_at)
            .execution_options(synchronize_session=False)
        )

        if result.rowcount != 1:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Связанные программы изменились. "
                    "Обновите данные и повторите действие."
                ),
            )

    video = lock_video_for_write(
        session=session,
        video_id=video_id,
        expected_version=expected_version,
    )

    current_references = get_video_references(
        session=session,
        video_id=video_id,
    )

    current_program_ids = {
        item.program_id
        for item in current_references
    }

    if current_program_ids != program_ids:
        raise HTTPException(
            status_code=409,
            detail=(
                "Видео добавили в программу или убрали из неё. "
                "Обновите данные и повторите действие."
            ),
        )

    return video, current_references


def synchronize_affected_programs(
    *,
    session: Session,
    program_ids: set[uuid.UUID],
    actor_user_id: uuid.UUID,
    video_id: uuid.UUID,
    reason: str,
) -> None:
    if not program_ids:
        return

    patient_ids = set(
        session.exec(
            select(ProgramEnrollment.patient_id).where(
                ProgramEnrollment.program_id.in_(program_ids),
                ProgramEnrollment.status
                == ProgramEnrollmentStatus.ACTIVE,
            )
        ).all()
    )

    for patient_id in sorted(patient_ids, key=str):
        lock_patient_for_write(
            session=session,
            patient_id=patient_id,
        )

    # После bulk DELETE/UPDATE нельзя использовать старые
    # коллекции stage.items, оставшиеся в identity map.
    session.flush()
    session.expire_all()

    enrollments = session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.program_id.in_(program_ids),
            ProgramEnrollment.status
            == ProgramEnrollmentStatus.ACTIVE,
        )
    ).all()

    for enrollment in enrollments:
        sync_program_enrollment(
            session=session,
            enrollment=enrollment,
            complete_if_empty=True,
            actor_user_id=actor_user_id,
            metadata={
                "reason": reason,
                "video_id": str(video_id),
            },
        )


def retire_unused_assets(
    *,
    session: Session,
    file_ids: set[uuid.UUID],
    image_ids: set[uuid.UUID],
) -> None:
    now = utc_now_naive()

    if file_ids:
        no_video_reference = ~(
            select(Video.id)
            .where(
                or_(
                    Video.wide_file_id == MediaVideoFile.id,
                    Video.mobile_file_id == MediaVideoFile.id,
                )
            )
            .correlate(MediaVideoFile)
            .exists()
        )

        session.execute(
            update(MediaVideoFile)
            .where(
                MediaVideoFile.id.in_(file_ids),
                no_video_reference,
            )
            .values(retired_at=now)
            .execution_options(synchronize_session=False)
        )

    if image_ids:
        no_image_reference = ~(
            select(Video.id)
            .where(
                or_(
                    Video.image_id == MediaImage.id,
                    Video.automatic_image_id == MediaImage.id,
                )
            )
            .correlate(MediaImage)
            .exists()
        )

        session.execute(
            update(MediaImage)
            .where(
                MediaImage.id.in_(image_ids),
                MediaImage.purpose == "video",
                no_image_reference,
            )
            .values(retired_at=now)
            .execution_options(synchronize_session=False)
        )


def delete_video_material(
    *,
    session: Session,
    video_id: uuid.UUID,
    payload: VideoDeleteRequest,
    actor_user_id: uuid.UUID,
) -> VideoDeleteResponse:
    video, references = lock_video_with_programs(
        session=session,
        video_id=video_id,
        expected_version=payload.expected_version,
    )

    actual_token = make_usage_token(
        video_id=video.id,
        references=references,
    )

    if actual_token != payload.expected_usage_token:
        raise HTTPException(
            status_code=409,
            detail=(
                "Список использования видео изменился. "
                "Проверьте обновлённый список программ."
            ),
        )

    title = video.title

    program_ids = {
        item.program_id
        for item in references
    }

    file_ids = {
        value
        for value in (
            video.wide_file_id,
            video.mobile_file_id,
        )
        if value is not None
    }

    image_ids = {
        value
        for value in (
            video.image_id,
            video.automatic_image_id,
        )
        if value is not None
    }

    # Историю просмотров не удаляем.
    # Добавляем сведения об удалённом материале,
    # не изменяя тип, дату и принадлежность события.
    deleted_at = utc_now_naive().isoformat() + "Z"

    events = session.exec(
        select(Event).where(
            Event.subject_type == "video",
            Event.subject_id == video.id,
        )
    ).all()

    for event in events:
        metadata = dict(event.metadata_json or {})

        metadata.setdefault("deleted_video_title", title)
        metadata.setdefault("video_deleted_at", deleted_at)
        metadata.setdefault(
            "video_deleted_by_user_id",
            str(actor_user_id),
        )

        event.metadata_json = metadata
        session.add(event)

    # Удаляются только видеошаги. Этапы и другие
    # материалы сохраняют свои UUID.
    session.execute(
        delete(ProgramStageItem)
        .where(ProgramStageItem.video_id == video.id)
        .execution_options(synchronize_session=False)
    )

    # Явные удаления нужны также для локального SQLite,
    # где foreign_keys может быть не включён.
    session.execute(
        delete(VideoProgress)
        .where(VideoProgress.video_id == video.id)
        .execution_options(synchronize_session=False)
    )

    session.execute(
        delete(VideoTagLink)
        .where(VideoTagLink.video_id == video.id)
        .execution_options(synchronize_session=False)
    )

    session.delete(video)
    session.flush()

    retire_unused_assets(
        session=session,
        file_ids=file_ids,
        image_ids=image_ids,
    )

    if program_ids:
        session.execute(
            update(Program)
            .where(Program.id.in_(program_ids))
            .values(updated_at=utc_now_naive())
            .execution_options(synchronize_session=False)
        )

    synchronize_affected_programs(
        session=session,
        program_ids=program_ids,
        actor_user_id=actor_user_id,
        video_id=video_id,
        reason="video_deleted",
    )

    return VideoDeleteResponse(
        video_id=video_id,
        affected_programs=len(program_ids),
        removed_program_items=len(references),
        message="Видео удалено",
    )


def set_video_visibility(
    *,
    session: Session,
    video_id: uuid.UUID,
    expected_version: int,
    is_hidden: bool,
    actor_user_id: uuid.UUID,
) -> Video:
    video, references = lock_video_with_programs(
        session=session,
        video_id=video_id,
        expected_version=expected_version,
    )

    if video.is_hidden == is_hidden:
        return video

    now = utc_now_naive()

    video.is_hidden = is_hidden
    video.hidden_at = now if is_hidden else None
    video.updated_at = now
    video.version += 1

    session.add(video)
    session.flush()

    synchronize_affected_programs(
        session=session,
        program_ids={
            item.program_id
            for item in references
        },
        actor_user_id=actor_user_id,
        video_id=video_id,
        reason="video_hidden" if is_hidden else "video_unhidden",
    )

    return video