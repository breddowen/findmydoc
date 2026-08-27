# ./backend/app/modules/assignments/routers.py
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.articles.models import Article
from app.modules.assignments.enums import (
    AssignmentStatus,
    AssignmentType,
)
from app.modules.assignments.models import ContentAssignment
from app.modules.assignments.schemas import (
    AssignmentCreateRequest,
    AssignmentResponse,
)
from app.modules.assignments.utils import (
    get_active_assignment,
)
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.service import send_notification
from app.modules.patients.utils import ensure_patient_access
from app.modules.questionnaires.models import Questionnaire
from app.modules.users.enums import UserRole
from app.modules.users.models import PatientProfile, User


router = APIRouter(
    prefix="/api/v1/assignments",
    tags=["Assignments"],
)


def serialize_assignment(
    *,
    session: Session,
    assignment: ContentAssignment,
) -> AssignmentResponse:
    if assignment.assignment_type == AssignmentType.ARTICLE:
        content = session.get(
            Article,
            assignment.article_id,
        )
    else:
        content = session.get(
            Questionnaire,
            assignment.questionnaire_id,
        )

    if not content:
        raise HTTPException(
            status_code=409,
            detail="Назначенный контент не найден",
        )

    return AssignmentResponse(
        id=assignment.id,
        patient_id=assignment.patient_id,
        assigned_by_user_id=(
            assignment.assigned_by_user_id
        ),
        assignment_type=assignment.assignment_type,
        status=assignment.status,
        content_id=content.id,
        title=content.title,
        pro_content=content.pro_content,
        created_at=assignment.created_at,
        started_at=assignment.started_at,
        completed_at=assignment.completed_at,
    )


@router.post(
    "",
    response_model=AssignmentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_assignment(
    payload: AssignmentCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> AssignmentResponse:
    ensure_patient_access(
        session=session,
        auth=auth,
        patient_id=payload.patient_id,
    )

    patient = session.get(
        PatientProfile,
        payload.patient_id,
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Пациент не найден",
        )

    if payload.assignment_type == AssignmentType.ARTICLE:
        content = session.get(
            Article,
            payload.article_id,
        )
        content_id = payload.article_id
        notification_type = (
            NotificationType.ARTICLE_ASSIGNED
        )
        action_url = (
            f"/content/articles/{content_id}"
        )
        message = "Вам назначена новая статья."
    else:
        content = session.get(
            Questionnaire,
            payload.questionnaire_id,
        )
        content_id = payload.questionnaire_id
        notification_type = (
            NotificationType.QUESTIONNAIRE_ASSIGNED
        )
        action_url = f"/questionnaires/{content_id}"
        message = "Вам назначен новый опросник."

    if not content:
        raise HTTPException(
            status_code=404,
            detail="Контент не найден",
        )

    if content.is_hidden:
        raise HTTPException(
            status_code=400,
            detail="Нельзя назначить скрытый контент",
        )

    existing = get_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=payload.assignment_type,
        content_id=content_id,
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Этот контент уже назначен пациенту",
        )

    assignment = ContentAssignment(
        patient_id=patient.id,
        assigned_by_user_id=auth.user.id,
        assignment_type=payload.assignment_type,
        article_id=payload.article_id,
        questionnaire_id=payload.questionnaire_id,
    )

    session.add(assignment)
    session.commit()
    session.refresh(assignment)

    patient_user = session.get(
        User,
        patient.user_id,
    )

    if patient_user:
        await send_notification(
            session=session,
            user_id=patient_user.id,
            title="Новое назначение",
            message=f"{message} «{content.title}»",
            notification_type=notification_type,
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url=action_url,
            payload={
                "assignment_id": str(assignment.id),
                "content_id": str(content.id),
                "content_type": (
                    payload.assignment_type.value
                ),
            },
        )

    return serialize_assignment(
        session=session,
        assignment=assignment,
    )


@router.get(
    "/me",
    response_model=list[AssignmentResponse],
)
async def list_my_assignments(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[AssignmentResponse]:
    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == auth.user.id
        )
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Профиль пациента не найден",
        )

    assignments = session.exec(
        select(ContentAssignment)
        .where(
            ContentAssignment.patient_id == patient.id,
            ContentAssignment.status
            != AssignmentStatus.CANCELLED,
        )
        .order_by(ContentAssignment.created_at.desc())
    ).all()

    return [
        serialize_assignment(
            session=session,
            assignment=assignment,
        )
        for assignment in assignments
    ]

@router.get(
    "/patient/{patient_id}",
    response_model=list[AssignmentResponse],
)
async def list_patient_assignments(
    patient_id: uuid.UUID,
    include_completed: bool = True,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> list[AssignmentResponse]:
    ensure_patient_access(
        session=session,
        auth=auth,
        patient_id=patient_id,
    )

    patient = session.get(
        PatientProfile,
        patient_id,
    )

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пациент не найден",
        )

    statement = select(ContentAssignment).where(
        ContentAssignment.patient_id == patient.id,
        ContentAssignment.status
        != AssignmentStatus.CANCELLED,
    )

    if not include_completed:
        statement = statement.where(
            ContentAssignment.status
            != AssignmentStatus.COMPLETED
        )

    assignments = session.exec(
        statement.order_by(
            ContentAssignment.created_at.desc()
        )
    ).all()

    return [
        serialize_assignment(
            session=session,
            assignment=assignment,
        )
        for assignment in assignments
    ]