# ./backend/app/modules/referrals/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.config import settings
from app.core.db import get_session
from app.core.email import send_console_email
from app.core.security import (
    AuthContext,
    require_roles,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.invitations.enums import InvitationType
from app.modules.invitations.utils import create_invitation
from app.modules.referrals.enums import (
    ReferralSource,
    ReferralStatus,
)
from app.modules.referrals.models import Referral
from app.modules.referrals.schemas import (
    ReferralConfirmationRequiredResponse,
    ReferralCreateRequest,
    ReferralCreatedResponse,
    ReferralListItem,
    ReferralResolveResponse,
    ReferralSourceUpdateRequest,
)
from app.modules.referrals.utils import (
    determine_referral_source,
    generate_referral_token,
    hash_referral_token,
    is_psychiatric_speciality,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    UserRole,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    User,
)
from app.modules.users.utils import normalize_email


router = APIRouter(
    prefix="/api/v1/referrals",
    tags=["Referrals"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_current_doctor(
    *,
    session: Session,
    auth: AuthContext,
) -> DoctorProfile:
    doctor = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == auth.user.id
        )
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль врача не найден",
        )

    if not doctor.speciality:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У врача отсутствует специальность",
        )

    return doctor


def build_referral_url(token: str) -> str:
    return (
        f"{settings.FRONTEND_URL.rstrip('/')}"
        f"/r/{token}"
    )


@router.post(
    "",
    response_model=(
        ReferralConfirmationRequiredResponse
        | ReferralCreatedResponse
    ),
    status_code=status.HTTP_201_CREATED,
)
async def create_referral(
    payload: ReferralCreateRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
):
    doctor = get_current_doctor(
        session=session,
        auth=auth,
    )

    record_id = payload.record_id.strip()
    email = normalize_email(str(payload.email))

    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.record_id == record_id
        )
    ).first()

    invitation_id = None
    patient_id = None

    if patient:
        patient_user = session.get(
            User,
            patient.user_id,
        )

        if not patient_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="У пациента отсутствует аккаунт",
            )

        existing_link = session.exec(
            select(DoctorPatientLink).where(
                DoctorPatientLink.doctor_id == doctor.id,
                DoctorPatientLink.patient_id == patient.id,
            )
        ).first()

        already_linked = bool(
            existing_link
            and existing_link.status
            == DoctorPatientStatus.ACTIVE
        )

        if not payload.confirm_existing:
            return ReferralConfirmationRequiredResponse(
                status="confirmation_required",
                message=(
                    "Пациент уже зарегистрирован. "
                    "Создать направление и привязать его к врачу?"
                ),
                patient_id=patient.id,
                record_id=patient.record_id,
                email_matches=patient_user.email == email,
                already_linked=already_linked,
            )

        if existing_link:
            existing_link.status = (
                DoctorPatientStatus.ACTIVE
            )
            existing_link.detached_at = None
            existing_link.updated_at = utc_now()
            session.add(existing_link)
        else:
            session.add(
                DoctorPatientLink(
                    doctor_id=doctor.id,
                    patient_id=patient.id,
                    status=DoctorPatientStatus.ACTIVE,
                )
            )

        patient_id = patient.id
        raw_token = generate_referral_token()
    else:
        invitation, raw_token = create_invitation(
            session=session,
            invitation_type=InvitationType.PATIENT,
            created_by_user_id=auth.user.id,
            email=email,
            record_id=record_id,
            fullname=payload.fullname,
            dob=payload.dob,
            gender=payload.gender,
            doctor_profile_id=doctor.id,
            send_email=False,
        )

        invitation_id = invitation.id

    now = utc_now()
    speciality = doctor.speciality

    referral_source = determine_referral_source(
        speciality.name
    )

    referral = Referral(
        token_hash=hash_referral_token(raw_token),
        status=ReferralStatus.LINK_SENT,
        source=referral_source,
        created_by_user_id=auth.user.id,
        doctor_id=doctor.id,
        patient_id=patient_id,
        invitation_id=invitation_id,
        speciality_id=speciality.id,
        speciality_name_snapshot=speciality.name,
        is_psychiatric_speciality_snapshot=(
            is_psychiatric_speciality(speciality.name)
        ),
        record_id_snapshot=record_id,
        link_sent_at=now,
    )

    session.add(referral)
    session.flush()

    # События создаются на backend в момент успешной
    # бизнес-операции, а не напрямую на frontend.
    record_event(
        session=session,
        event_type=EventType.REFERRAL_CREATED,
        patient_id=patient_id,
        actor_user_id=auth.user.id,
        referral_id=referral.id,
        doctor_id=doctor.id,
        speciality_id=speciality.id,
    )

    record_event(
        session=session,
        event_type=EventType.LINK_SENT,
        patient_id=patient_id,
        actor_user_id=auth.user.id,
        referral_id=referral.id,
        doctor_id=doctor.id,
        speciality_id=speciality.id,
    )

    session.commit()
    session.refresh(referral)

    registration_url = build_referral_url(raw_token)

    send_console_email(
        recipient=email,
        subject="Направление в FindMyDoc",
        message=(
            "Врач подготовил для вас персональное "
            "направление. Перейдите по ссылке:"
        ),
        action_url=registration_url,
    )

    print(f"Referral link: {registration_url}")

    return ReferralCreatedResponse(
        status="referral_created",
        referral_id=referral.id,
        referral_status=referral.status,
        source=referral.source,
        patient_id=referral.patient_id,
        invitation_id=referral.invitation_id,
        registration_url=registration_url,
        created_at=referral.created_at,
    )


@router.get(
    "/resolve/{token}",
    response_model=ReferralResolveResponse,
)
async def resolve_referral(
    token: str,
    session: Session = Depends(get_session),
) -> ReferralResolveResponse:
    referral = session.exec(
        select(Referral).where(
            Referral.token_hash
            == hash_referral_token(token)
        )
    ).first()

    if not referral:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Направление не найдено",
        )

    if referral.status == ReferralStatus.CANCELLED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Направление отменено",
        )

    # Фиксируем только первое открытие самой ссылки направления.
    # Обычные просмотры страниц событиями не считаются.
    if referral.opened_at is None:
        referral.opened_at = utc_now()

        if referral.status == ReferralStatus.LINK_SENT:
            referral.status = ReferralStatus.OPENED

        record_event(
            session=session,
            event_type=EventType.LINK_OPENED,
            patient_id=referral.patient_id,
            referral_id=referral.id,
            doctor_id=referral.doctor_id,
            speciality_id=referral.speciality_id,
        )

        session.add(referral)
        session.commit()
        session.refresh(referral)

    return ReferralResolveResponse(
        referral_id=referral.id,
        status=referral.status,
        source=referral.source,
        requires_registration=(
            referral.patient_id is None
        ),
        patient_id=referral.patient_id,
        invitation_type=(
            InvitationType.PATIENT.value
            if referral.invitation_id
            else None
        ),
        record_id=referral.record_id_snapshot,
    )


@router.get(
    "/mine",
    response_model=list[ReferralListItem],
)
async def list_my_referrals(
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> list[ReferralListItem]:
    doctor = get_current_doctor(
        session=session,
        auth=auth,
    )

    referrals = session.exec(
        select(Referral)
        .where(Referral.doctor_id == doctor.id)
        .order_by(Referral.created_at.desc())
    ).all()

    return [
        ReferralListItem(
            id=item.id,
            status=item.status,
            source=item.source,
            patient_id=item.patient_id,
            invitation_id=item.invitation_id,
            record_id=item.record_id_snapshot,
            speciality_name=(
                item.speciality_name_snapshot
            ),
            created_at=item.created_at,
            link_sent_at=item.link_sent_at,
            opened_at=item.opened_at,
            registered_at=item.registered_at,
        )
        for item in referrals
    ]


@router.get(
    "",
    response_model=list[ReferralListItem],
)
async def list_all_referrals(
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> list[ReferralListItem]:
    referrals = session.exec(
        select(Referral).order_by(
            Referral.created_at.desc()
        )
    ).all()

    return [
        ReferralListItem(
            id=item.id,
            status=item.status,
            source=item.source,
            patient_id=item.patient_id,
            invitation_id=item.invitation_id,
            record_id=item.record_id_snapshot,
            speciality_name=(
                item.speciality_name_snapshot
            ),
            created_at=item.created_at,
            link_sent_at=item.link_sent_at,
            opened_at=item.opened_at,
            registered_at=item.registered_at,
        )
        for item in referrals
    ]


@router.patch(
    "/{referral_id}/source",
    response_model=ReferralListItem,
)
async def update_referral_source(
    referral_id: uuid.UUID,
    payload: ReferralSourceUpdateRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> ReferralListItem:
    referral = session.get(Referral, referral_id)

    if not referral:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Направление не найдено",
        )

    referral.source = payload.source

    session.add(referral)
    session.commit()
    session.refresh(referral)

    return ReferralListItem(
        id=referral.id,
        status=referral.status,
        source=referral.source,
        patient_id=referral.patient_id,
        invitation_id=referral.invitation_id,
        record_id=referral.record_id_snapshot,
        speciality_name=(
            referral.speciality_name_snapshot
        ),
        created_at=referral.created_at,
        link_sent_at=referral.link_sent_at,
        opened_at=referral.opened_at,
        registered_at=referral.registered_at,
    )