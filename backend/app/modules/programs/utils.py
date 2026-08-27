# ./backend/app/modules/programs/utils.py
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlmodel import Session, select

from app.modules.articles.models import ArticleProgress
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
    ProgramStageStatus,
)
from app.modules.programs.models import (
    PatientProgramAccess,
    Program,
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
    ProgramTagLink,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)
from app.modules.questionnaires.models import (
    QuestionnaireSubmission,
)
from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def normalize_datetime(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value

def get_program_questionnaire_submission(
    *,
    session: Session,
    patient_id: uuid.UUID,
    item: ProgramStageItem,
) -> QuestionnaireSubmission | None:
    if (
        item.item_type
        != ProgramItemType.QUESTIONNAIRE
    ):
        return None

    stage = session.get(
        ProgramStage,
        item.stage_id,
    )

    if not stage:
        return None

    # Сначала ищем завершённую попытку.
    completed_submission = session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient_id,
            QuestionnaireSubmission.questionnaire_id
            == item.questionnaire_id,
            QuestionnaireSubmission.program_id
            == stage.program_id,
            QuestionnaireSubmission.program_stage_id
            == stage.id,
            QuestionnaireSubmission.status
            == QuestionnaireSubmissionStatus.COMPLETED,
        )
        .order_by(
            QuestionnaireSubmission.completed_at.desc()
        )
    ).first()

    if completed_submission:
        return completed_submission

    # Если завершённой нет, возвращаем последнюю
    # незавершённую попытку.
    return session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient_id,
            QuestionnaireSubmission.questionnaire_id
            == item.questionnaire_id,
            QuestionnaireSubmission.program_id
            == stage.program_id,
            QuestionnaireSubmission.program_stage_id
            == stage.id,
        )
        .order_by(
            QuestionnaireSubmission.started_at.desc()
        )
    ).first()

def get_program_tag_ids(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id == program_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_program_tags(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id == program_id
        )
    ).all()

    tags: list[Tag] = []

    for link in links:
        tag = session.get(Tag, link.tag_id)

        if tag:
            tags.append(tag)

    return sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )


def validate_program_periods(program_data) -> None:
    stages = sorted(
        program_data.stages,
        key=lambda item: item.day_from,
    )

    if len({
        stage.order_index
        for stage in stages
    }) != len(stages):
        raise HTTPException(
            status_code=422,
            detail="Порядок этапов должен быть уникальным",
        )

    previous = None

    for stage in stages:
        if previous and stage.day_from <= previous.day_to:
            raise HTTPException(
                status_code=422,
                detail="Периоды этапов не должны пересекаться",
            )

        if len({
            item.order_index
            for item in stage.items
        }) != len(stage.items):
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Порядок элементов этапа "
                    f"«{stage.title}» должен быть уникальным"
                ),
            )

        previous = stage


def get_patient_program_access(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> PatientProgramAccess | None:
    return session.exec(
        select(PatientProgramAccess).where(
            PatientProgramAccess.patient_id
            == patient_id,
            PatientProgramAccess.program_id
            == program_id,
        )
    ).first()


def patient_has_program_access(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> bool:
    access = get_patient_program_access(
        session=session,
        patient_id=patient_id,
        program_id=program_id,
    )

    return bool(access and access.is_active)


def get_program_enrollment(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> ProgramEnrollment | None:
    return session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.patient_id
            == patient_id,
            ProgramEnrollment.program_id
            == program_id,
        )
    ).first()


def is_program_item_completed(
    *,
    session: Session,
    patient_id: uuid.UUID,
    item: ProgramStageItem,
) -> bool:
    if item.item_type == ProgramItemType.CONSULTATION:
        return False

    if item.item_type == ProgramItemType.ARTICLE:
        progress = session.exec(
            select(ArticleProgress).where(
                ArticleProgress.patient_id
                == patient_id,
                ArticleProgress.article_id
                == item.article_id,
                ArticleProgress.completed_at.is_not(None),
            )
        ).first()

        return progress is not None

    submission = get_program_questionnaire_submission(
        session=session,
        patient_id=patient_id,
        item=item,
    )

    return bool(
        submission
        and submission.status
        == QuestionnaireSubmissionStatus.COMPLETED
    )


def get_stage_task_items(
    stage: ProgramStage,
) -> list[ProgramStageItem]:
    return [
        item
        for item in stage.items
        if item.item_type
        != ProgramItemType.CONSULTATION
    ]


def calculate_stage_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    stage: ProgramStage,
) -> tuple[int, int, float]:
    task_items = get_stage_task_items(stage)

    if not task_items:
        return 0, 0, 100.0

    completed_count = sum(
        1
        for item in task_items
        if is_program_item_completed(
            session=session,
            patient_id=patient_id,
            item=item,
        )
    )

    percentage = round(
        completed_count / len(task_items) * 100,
        2,
    )

    return (
        completed_count,
        len(task_items),
        percentage,
    )


def calculate_stage_status(
    *,
    session: Session,
    patient_id: uuid.UUID,
    stage: ProgramStage,
    elapsed_days: int | None,
) -> ProgramStageStatus:
    if elapsed_days is None:
        return ProgramStageStatus.UPCOMING

    completed, total, _ = calculate_stage_progress(
        session=session,
        patient_id=patient_id,
        stage=stage,
    )

    if total == 0 and elapsed_days >= stage.day_from:
        return ProgramStageStatus.COMPLETED

    if total > 0 and completed == total:
        return ProgramStageStatus.COMPLETED

    if elapsed_days < stage.day_from:
        return ProgramStageStatus.UPCOMING

    if elapsed_days > stage.day_to:
        return ProgramStageStatus.OVERDUE

    if completed > 0:
        return ProgramStageStatus.IN_PROGRESS

    return ProgramStageStatus.AVAILABLE


def calculate_program_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program: Program,
) -> tuple[int, int, float]:
    task_items = [
        item
        for stage in program.stages
        for item in stage.items
        if item.item_type
        != ProgramItemType.CONSULTATION
    ]

    if not task_items:
        return 0, 0, 100.0

    completed_count = sum(
        1
        for item in task_items
        if is_program_item_completed(
            session=session,
            patient_id=patient_id,
            item=item,
        )
    )

    return (
        completed_count,
        len(task_items),
        round(
            completed_count / len(task_items) * 100,
            2,
        ),
    )


def sync_program_enrollment(
    *,
    session: Session,
    enrollment: ProgramEnrollment,
) -> None:
    if (
        enrollment.status
        != ProgramEnrollmentStatus.ACTIVE
    ):
        return

    program = session.get(
        Program,
        enrollment.program_id,
    )

    if not program:
        return

    completed, total, _ = calculate_program_progress(
        session=session,
        patient_id=enrollment.patient_id,
        program=program,
    )

    now = utc_now()

    if (
        completed > 0
        and enrollment.in_progress_event_at is None
    ):
        enrollment.in_progress_event_at = now

        record_event(
            session=session,
            event_type=EventType.PROGRAM_IN_PROGRESS,
            patient_id=enrollment.patient_id,
            program_id=program.id,
            subject_type="program",
            subject_id=program.id,
        )

    if (
        total > 0
        and completed == total
        and enrollment.completed_event_at is None
    ):
        enrollment.status = (
            ProgramEnrollmentStatus.COMPLETED
        )
        enrollment.completed_at = now
        enrollment.completed_event_at = now

        record_event(
            session=session,
            event_type=EventType.PROGRAM_COMPLETED,
            patient_id=enrollment.patient_id,
            program_id=program.id,
            subject_type="program",
            subject_id=program.id,
        )

    enrollment.updated_at = now
    session.add(enrollment)


def sync_patient_program_enrollments(
    *,
    session: Session,
    patient_id: uuid.UUID,
) -> None:
    enrollments = session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.patient_id == patient_id,
            ProgramEnrollment.status
            == ProgramEnrollmentStatus.ACTIVE,
        )
    ).all()

    for enrollment in enrollments:
        sync_program_enrollment(
            session=session,
            enrollment=enrollment,
        )

def get_program_content_item(
    *,
    session: Session,
    program_id: uuid.UUID,
    content_type: ProgramItemType,
    content_id: uuid.UUID,
    stage_id: uuid.UUID | None = None,
) -> ProgramStageItem | None:
    statement = (
        select(ProgramStageItem)
        .join(
            ProgramStage,
            ProgramStage.id
            == ProgramStageItem.stage_id,
        )
        .where(
            ProgramStage.program_id == program_id,
            ProgramStageItem.item_type == content_type,
        )
    )

    if stage_id:
        statement = statement.where(
            ProgramStage.id == stage_id
        )

    if content_type == ProgramItemType.ARTICLE:
        statement = statement.where(
            ProgramStageItem.article_id == content_id
        )

    elif (
        content_type
        == ProgramItemType.QUESTIONNAIRE
    ):
        statement = statement.where(
            ProgramStageItem.questionnaire_id
            == content_id
        )

    return session.exec(statement).first()


def ensure_patient_program_content_access(
    *,
    session: Session,
    patient,
    program_id: uuid.UUID,
    content_type: ProgramItemType,
    content_id: uuid.UUID,
    pro_content: bool,
    stage_id: uuid.UUID | None = None,
) -> ProgramStageItem:
    from app.modules.content.utils import (
        patient_can_see_content,
    )

    program = session.get(Program, program_id)

    if not program or program.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    item = get_program_content_item(
        session=session,
        program_id=program.id,
        content_type=content_type,
        content_id=content_id,
        stage_id=stage_id,
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Контент не входит в эту программу",
        )

    has_access = patient_has_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    can_see_program = patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=get_program_tag_ids(
            session=session,
            program_id=program.id,
        ),
        is_hidden=program.is_hidden,
    )

    if not has_access and not can_see_program:
        raise HTTPException(
            status_code=403,
            detail="Программа недоступна пациенту",
        )

    # Глобальный Pro здесь намеренно не используется.
    if pro_content and not has_access:
        raise HTTPException(
            status_code=403,
            detail=(
                "Для этого материала необходима "
                "покупка программы"
            ),
        )

    return item