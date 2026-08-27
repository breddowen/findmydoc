# ./backend/app/modules/events/routers.py
import uuid

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.events.models import Event
from app.modules.events.schemas import EventResponse
from app.modules.users.enums import UserRole
from app.modules.users.models import DoctorProfile


router = APIRouter(
    prefix="/api/v1/events",
    tags=["Events"],
)


@router.get("", response_model=list[EventResponse])
async def list_events(
    referral_id: uuid.UUID | None = None,
    patient_id: uuid.UUID | None = None,
    limit: int = 200,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> list[Event]:
    safe_limit = min(max(limit, 1), 500)

    statement = select(Event)

    if referral_id:
        statement = statement.where(
            Event.referral_id == referral_id
        )

    if patient_id:
        statement = statement.where(
            Event.patient_id == patient_id
        )

    if auth.active_role == UserRole.DOCTOR:
        doctor = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == auth.user.id
            )
        ).first()

        if not doctor:
            return []

        statement = statement.where(
            Event.doctor_id == doctor.id
        )

    return list(
        session.exec(
            statement
            .order_by(Event.occurred_at.desc())
            .limit(safe_limit)
        ).all()
    )