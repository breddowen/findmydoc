# ./backend/app/modules/consents/contact_service.py
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlmodel import Session, select

from app.modules.consents.enums import ConsentType
from app.modules.consents.models import (
    ConsentRecord,
    ContactPreference,
)
from app.modules.consents.utils import get_consent_document
from app.modules.events.enums import EventType
from app.modules.events.service import record_event


def ensure_assistant_contact_allowed(
    *,
    session: Session,
    patient_id: uuid.UUID,
    user_id: uuid.UUID,
    source: str,
    document_version: str | None = None,
) -> None:
    """
    Вызывать внутри транзакции с блокировкой пациента.

    Сохраняет разрешение на контакт.
    Не делает commit и не отправляет уведомления.
    """
    document = get_consent_document(
        ConsentType.ASSISTANT_CONTACT
    )

    if not document:
        raise HTTPException(
            status_code=503,
            detail="Документ разрешения на контакт недоступен",
        )

    current_version = document["version"]

    if (
        document_version is not None
        and document_version != current_version
    ):
        raise HTTPException(
            status_code=409,
            detail=(
                "Условия разрешения на контакт обновились. "
                "Закройте и снова откройте диалог."
            ),
        )

    preference = session.exec(
        select(ContactPreference).where(
            ContactPreference.patient_id == patient_id
        )
    ).first()

    latest_consent = session.exec(
        select(ConsentRecord)
        .where(
            ConsentRecord.patient_id == patient_id,
            ConsentRecord.consent_type
            == ConsentType.ASSISTANT_CONTACT,
        )
        .order_by(
            ConsentRecord.created_at.desc(),
            ConsentRecord.id.desc(),
        )
    ).first()

    already_allowed = bool(
        preference
        and preference.allow_assistant_contact
        and not preference.do_not_call
        and latest_consent
        and latest_consent.accepted
        and latest_consent.document_version == current_version
    )

    if already_allowed:
        return

    now = datetime.now(timezone.utc)

    session.add(
        ConsentRecord(
            patient_id=patient_id,
            consent_type=ConsentType.ASSISTANT_CONTACT,
            accepted=True,
            document_version=current_version,
            recorded_by_user_id=user_id,
            created_at=now,
        )
    )

    if preference is None:
        preference = ContactPreference(
            patient_id=patient_id,
            updated_by_user_id=user_id,
        )

    preference.allow_assistant_contact = True
    preference.do_not_call = False
    preference.updated_by_user_id = user_id
    preference.updated_at = now

    session.add(preference)

    record_event(
        session=session,
        event_type=EventType.CONSENT_GIVEN,
        patient_id=patient_id,
        actor_user_id=user_id,
        metadata={
            "consent_type": ConsentType.ASSISTANT_CONTACT.value,
            "source": source,
            "document_version": current_version,
        },
    )