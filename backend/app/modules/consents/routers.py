# ./backend/app/modules/consents/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.consents.enums import ConsentType
from app.modules.consents.models import (
    ConsentRecord,
    ContactPreference,
)
from app.modules.consents.schemas import (
    ConsentDocumentResponse,
    ConsentRecordResponse,
    ConsentSetRequest,
    ContactPreferenceResponse,
    MyConsentsResponse,
)
from app.modules.consents.utils import (
    CONSENT_DOCUMENTS,
    get_consent_document,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.referrals.models import Referral
from app.modules.users.enums import UserRole
from app.modules.users.models import PatientProfile


router = APIRouter(
    prefix="/api/v1/consents",
    tags=["Consents"],
)


def get_current_patient(
    *,
    session: Session,
    auth: AuthContext,
) -> PatientProfile:
    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == auth.user.id
        )
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль пациента не найден",
        )

    return patient


@router.get(
    "/available",
    response_model=list[ConsentDocumentResponse],
)
async def list_available_consents(
    _: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
) -> list[ConsentDocumentResponse]:
    return [
        ConsentDocumentResponse(
            consent_type=consent_type,
            title=document["title"],
            description=document["description"],
            version=document["version"],
        )
        for consent_type, document
        in CONSENT_DOCUMENTS.items()
    ]


@router.get(
    "/me",
    response_model=MyConsentsResponse,
)
async def get_my_consents(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> MyConsentsResponse:
    patient = get_current_patient(
        session=session,
        auth=auth,
    )

    consent_responses: list[ConsentRecordResponse] = []

    for consent_type in CONSENT_DOCUMENTS:
        latest_record = session.exec(
            select(ConsentRecord)
            .where(
                ConsentRecord.patient_id == patient.id,
                ConsentRecord.consent_type
                == consent_type,
            )
            .order_by(ConsentRecord.created_at.desc())
        ).first()

        if latest_record:
            consent_responses.append(
                ConsentRecordResponse(
                    id=latest_record.id,
                    consent_type=latest_record.consent_type,
                    accepted=latest_record.accepted,
                    document_version=(
                        latest_record.document_version
                    ),
                    created_at=latest_record.created_at,
                )
            )

    preference = session.exec(
        select(ContactPreference).where(
            ContactPreference.patient_id == patient.id
        )
    ).first()

    return MyConsentsResponse(
        consents=consent_responses,
        contact_preference=ContactPreferenceResponse(
            allow_assistant_contact=(
                preference.allow_assistant_contact
                if preference
                else False
            ),
            do_not_call=(
                preference.do_not_call
                if preference
                else False
            ),
            updated_at=(
                preference.updated_at
                if preference
                else None
            ),
        ),
    )


@router.post(
    "/me",
    response_model=ConsentRecordResponse,
)
async def set_my_consent(
    payload: ConsentSetRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ConsentRecordResponse:
    if (
        payload.consent_type
        == ConsentType.ANALYTICS_PROCESSING
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Согласие на аналитику пока "
                "не используется"
            ),
        )

    document = get_consent_document(
        payload.consent_type
    )

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Документ согласия не найден",
        )

    patient = get_current_patient(
        session=session,
        auth=auth,
    )

    consent_record = ConsentRecord(
        patient_id=patient.id,
        consent_type=payload.consent_type,
        accepted=payload.accepted,
        document_version=document["version"],
        recorded_by_user_id=auth.user.id,
    )

    session.add(consent_record)

    if (
        payload.consent_type
        == ConsentType.ASSISTANT_CONTACT
    ):
        preference = session.exec(
            select(ContactPreference).where(
                ContactPreference.patient_id
                == patient.id
            )
        ).first()

        if not preference:
            preference = ContactPreference(
                patient_id=patient.id,
                updated_by_user_id=auth.user.id,
            )

        preference.allow_assistant_contact = (
            payload.accepted
        )

        if payload.accepted:
            preference.do_not_call = False

        preference.updated_by_user_id = auth.user.id

        session.add(preference)

        if payload.accepted:
            latest_referral = session.exec(
                select(Referral)
                .where(
                    Referral.patient_id == patient.id
                )
                .order_by(Referral.created_at.desc())
            ).first()

            record_event(
                session=session,
                event_type=EventType.CONTACT_REQUESTED,
                patient_id=patient.id,
                actor_user_id=auth.user.id,
                referral_id=(
                    latest_referral.id
                    if latest_referral
                    else None
                ),
                doctor_id=(
                    latest_referral.doctor_id
                    if latest_referral
                    else None
                ),
                speciality_id=(
                    latest_referral.speciality_id
                    if latest_referral
                    else None
                ),
            )

    if payload.accepted:
        record_event(
            session=session,
            event_type=EventType.CONSENT_GIVEN,
            patient_id=patient.id,
            actor_user_id=auth.user.id,
            metadata={
                "consent_type": (
                    payload.consent_type.value
                )
            },
        )

    session.commit()
    session.refresh(consent_record)

    return ConsentRecordResponse(
        id=consent_record.id,
        consent_type=consent_record.consent_type,
        accepted=consent_record.accepted,
        document_version=(
            consent_record.document_version
        ),
        created_at=consent_record.created_at,
    )