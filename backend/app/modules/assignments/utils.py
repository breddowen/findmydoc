# ./backend/app/modules/assignments/utils.py
import uuid
from datetime import datetime, timezone

from sqlmodel import Session, select

from app.modules.assignments.enums import (
    AssignmentStatus,
    AssignmentType,
)
from app.modules.assignments.models import ContentAssignment


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_active_assignment(
    *,
    session: Session,
    patient_id: uuid.UUID,
    assignment_type: AssignmentType,
    content_id: uuid.UUID,
) -> ContentAssignment | None:
    statement = select(ContentAssignment).where(
        ContentAssignment.patient_id == patient_id,
        ContentAssignment.assignment_type
        == assignment_type,
        ContentAssignment.status
        != AssignmentStatus.CANCELLED,
    )

    if assignment_type == AssignmentType.ARTICLE:
        statement = statement.where(
            ContentAssignment.article_id == content_id
        )
    else:
        statement = statement.where(
            ContentAssignment.questionnaire_id
            == content_id
        )

    return session.exec(statement).first()


def patient_has_active_assignment(
    *,
    session: Session,
    patient_id: uuid.UUID,
    assignment_type: AssignmentType,
    content_id: uuid.UUID,
) -> bool:
    return get_active_assignment(
        session=session,
        patient_id=patient_id,
        assignment_type=assignment_type,
        content_id=content_id,
    ) is not None


def mark_assignment_in_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    assignment_type: AssignmentType,
    content_id: uuid.UUID,
) -> None:
    assignment = get_active_assignment(
        session=session,
        patient_id=patient_id,
        assignment_type=assignment_type,
        content_id=content_id,
    )

    if (
        assignment
        and assignment.status
        == AssignmentStatus.ASSIGNED
    ):
        assignment.status = AssignmentStatus.IN_PROGRESS
        assignment.started_at = utc_now()
        session.add(assignment)


def mark_assignment_completed(
    *,
    session: Session,
    patient_id: uuid.UUID,
    assignment_type: AssignmentType,
    content_id: uuid.UUID,
) -> None:
    assignment = get_active_assignment(
        session=session,
        patient_id=patient_id,
        assignment_type=assignment_type,
        content_id=content_id,
    )

    if assignment:
        assignment.status = AssignmentStatus.COMPLETED
        assignment.completed_at = utc_now()

        if assignment.started_at is None:
            assignment.started_at = assignment.completed_at

        session.add(assignment)