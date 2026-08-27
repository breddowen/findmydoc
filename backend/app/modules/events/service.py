# ./backend/app/modules/events/service.py
import uuid
from typing import Any

from sqlmodel import Session

from app.modules.events.enums import EventType
from app.modules.events.models import Event


def record_event(
    *,
    session: Session,
    event_type: EventType,
    patient_id: uuid.UUID | None = None,
    actor_user_id: uuid.UUID | None = None,
    referral_id: uuid.UUID | None = None,
    doctor_id: uuid.UUID | None = None,
    speciality_id: uuid.UUID | None = None,
    product_id: uuid.UUID | None = None,
    program_id: uuid.UUID | None = None,
    subject_type: str | None = None,
    subject_id: uuid.UUID | None = None,
    metadata: dict[str, Any] | None = None,
) -> Event:
    """
    ЕДИНАЯ ТОЧКА РЕГИСТРАЦИИ БИЗНЕС-СОБЫТИЙ.

    События создаются на backend после успешной проверки
    бизнес-операции. Frontend может сообщить о действии,
    но не должен самостоятельно считаться источником истины.

    Для отключения конкретного события достаточно убрать вызов
    record_event() из соответствующей бизнес-операции.

    Обычные просмотры страниц здесь не регистрируются.
    """
    event = Event(
        event_type=event_type,
        patient_id=patient_id,
        actor_user_id=actor_user_id,
        referral_id=referral_id,
        doctor_id=doctor_id,
        speciality_id=speciality_id,
        product_id=product_id,
        program_id=program_id,
        subject_type=subject_type,
        subject_id=subject_id,
        metadata_json=metadata or {},
    )

    session.add(event)

    return event