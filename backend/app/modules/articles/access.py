# ./backend/app/modules/articles/access.py
import uuid

from fastapi import HTTPException
from sqlmodel import Session

from app.modules.articles.models import Article
from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import patient_has_active_assignment
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.utils import (
    ensure_patient_program_content_access,
)
from app.modules.users.models import PatientProfile


def ensure_article_access(
    *,
    session: Session,
    article: Article,
    patient: PatientProfile,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    if article.is_hidden:
        raise HTTPException(
            status_code=403,
            detail="Статья скрыта",
        )

    if program_stage_id is not None and program_id is None:
        raise HTTPException(
            status_code=422,
            detail="Для этапа необходимо указать программу",
        )

    if program_id is not None:
        ensure_patient_program_content_access(
            session=session,
            patient=patient,
            program_id=program_id,
            stage_id=program_stage_id,
            content_type=ProgramItemType.ARTICLE,
            content_id=article.id,
            pro_content=article.pro_content,
        )
        return

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if (
        article.pro_content
        and not patient.pro_enabled
        and not is_assigned
    ):
        raise HTTPException(
            status_code=403,
            detail="Требуется Pro-доступ или назначение врача",
        )