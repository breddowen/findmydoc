# ./backend/app/modules/articles/tracking.py
import uuid
from typing import Any

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.modules.events.enums import EventType
from app.modules.events.models import Event
from app.modules.events.service import record_event


def record_article_interaction_event(
    *,
    session: Session,
    event_type: EventType,
    interaction_id: uuid.UUID,
    patient_id: uuid.UUID,
    article_id: uuid.UUID,
    actor_user_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    assignment_id: uuid.UUID | None = None,
    source: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> Event:
    if event_type not in {
        EventType.ARTICLE_OPENED,
        EventType.ARTICLE_READ,
    }:
        raise ValueError("Неподдерживаемый тип события статьи")

    def find_existing() -> Event | None:
        return session.exec(
            select(Event).where(
                Event.event_type == event_type,
                Event.interaction_id == interaction_id,
            )
        ).first()

    def validate_existing(event: Event) -> Event:
        if (
            event.patient_id != patient_id
            or event.subject_type != "article"
            or event.subject_id != article_id
            or event.program_id != program_id
        ):
            raise HTTPException(
                status_code=409,
                detail=(
                    "Идентификатор открытия уже используется "
                    "в другом контексте"
                ),
            )

        return event

    existing = find_existing()

    if existing:
        return validate_existing(existing)

    try:
        # Ошибка уникальности откатывает только вставку события,
        # а не весь сохранённый в текущей транзакции прогресс.
        with session.begin_nested():
            event = record_event(
                session=session,
                event_type=event_type,
                patient_id=patient_id,
                actor_user_id=actor_user_id,
                program_id=program_id,
                assignment_id=assignment_id,
                interaction_id=interaction_id,
                source=source,
                subject_type="article",
                subject_id=article_id,
                metadata=metadata,
            )

            session.flush()

        return event
    except IntegrityError:
        existing = find_existing()

        if existing is None:
            # Это не ожидаемый конфликт идемпотентности.
            raise

        return validate_existing(existing)