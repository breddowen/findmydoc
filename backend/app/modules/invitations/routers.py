# ./backend/app/modules/invitations/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.config import settings
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    ensure_user_can_authenticate,
    get_current_auth,
    hash_password,
    require_roles,
    validate_password_strength,
    verify_password,
)
from app.modules.auth.utils import send_verification_email
from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.invitations.models import Invitation
from app.modules.invitations.schemas import (
    DoctorInvitationCreateRequest,
    ExistingPatientAttachedResponse,
    ExistingPatientConfirmation,
    InvitationAcceptRequest,
    InvitationAcceptResponse,
    InvitationCreatedResponse,
    InvitationListItem,
    InvitationPreviewResponse,
    MessageResponse,
    PatientInvitationPrepareRequest,
    RelativeInvitationCreateRequest,
)
from app.modules.invitations.utils import (
    build_registration_url,
    create_invitation,
    get_invitation_by_token,
    normalize_datetime,
    ensure_user_role,
    utc_now,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    RelativePatientStatus,
    UserRole,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    RelativePatientLink,
    RelativeProfile,
    Speciality,
    User,
)
from app.modules.users.utils import (
    get_user_by_email,
    normalize_email,
)

from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.referrals.enums import ReferralStatus
from app.modules.referrals.models import Referral

router = APIRouter(
    prefix="/api/v1/invitations",
    tags=["Invitations"],
)


def get_authenticated_doctor_profile(
    *,
    session: Session,
    auth: AuthContext,
) -> DoctorProfile:
    doctor_profile = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == auth.user.id
        )
    ).first()

    if not doctor_profile:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Профиль врача не найден",
        )

    return doctor_profile


def build_invitation_created_response(
    invitation: Invitation,
    raw_token: str,
) -> InvitationCreatedResponse:
    return InvitationCreatedResponse(
        status="invitation_created",
        invitation_id=invitation.id,
        invitation_type=invitation.invitation_type,
        email=invitation.email,
        expires_at=invitation.expires_at,
        registration_url=build_registration_url(raw_token),
    )


@router.post(
    "/doctors",
    response_model=InvitationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def invite_doctor(
    payload: DoctorInvitationCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> InvitationCreatedResponse:
    speciality = session.get(
        Speciality,
        payload.speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    normalized_email = normalize_email(str(payload.email))
    existing_user = get_user_by_email(
        session,
        normalized_email,
    )

    if existing_user and existing_user.doctor_profile:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Этот пользователь уже зарегистрирован как врач",
        )

    invitation, raw_token = create_invitation(
        session=session,
        invitation_type=InvitationType.DOCTOR,
        created_by_user_id=auth.user.id,
        email=normalized_email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        middle_name=payload.middle_name,
        speciality_id=speciality.id,
    )

    return build_invitation_created_response(
        invitation,
        raw_token,
    )


@router.post(
    "/patients/prepare",
    response_model=(
        ExistingPatientConfirmation
        | ExistingPatientAttachedResponse
        | InvitationCreatedResponse
    ),
)
async def prepare_patient_invitation(
    payload: PatientInvitationPrepareRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
):
    doctor_profile = get_authenticated_doctor_profile(
        session=session,
        auth=auth,
    )

    normalized_record_id = payload.record_id.strip()
    normalized_email = normalize_email(str(payload.email))

    existing_patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.record_id == normalized_record_id
        )
    ).first()

    if existing_patient:
        patient_user = session.get(
            User,
            existing_patient.user_id,
        )

        if not patient_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="У профиля пациента отсутствует аккаунт",
            )

        existing_link = session.exec(
            select(DoctorPatientLink).where(
                DoctorPatientLink.doctor_id == doctor_profile.id,
                DoctorPatientLink.patient_id == existing_patient.id,
            )
        ).first()

        already_linked = bool(
            existing_link
            and existing_link.status
            == DoctorPatientStatus.ACTIVE
        )

        if not payload.confirm_existing:
            return ExistingPatientConfirmation(
                status="confirmation_required",
                message=(
                    "Пациент уже зарегистрирован. "
                    "Добавить его к текущему врачу?"
                ),
                patient_id=existing_patient.id,
                record_id=existing_patient.record_id,
                email_matches=(
                    patient_user.email == normalized_email
                ),
                already_linked=already_linked,
            )

        if existing_link:
            existing_link.status = DoctorPatientStatus.ACTIVE
            existing_link.detached_at = None
            existing_link.updated_at = utc_now()
            session.add(existing_link)
        else:
            existing_link = DoctorPatientLink(
                doctor_id=doctor_profile.id,
                patient_id=existing_patient.id,
                status=DoctorPatientStatus.ACTIVE,
            )
            session.add(existing_link)

        session.commit()

        return ExistingPatientAttachedResponse(
            status="patient_attached",
            message="Пациент привязан к врачу",
            patient_id=existing_patient.id,
            record_id=existing_patient.record_id,
        )

    invitation, raw_token = create_invitation(
        session=session,
        invitation_type=InvitationType.PATIENT,
        created_by_user_id=auth.user.id,
        email=normalized_email,
        record_id=normalized_record_id,
        fullname=payload.fullname,
        dob=payload.dob,
        gender=payload.gender,
        doctor_profile_id=doctor_profile.id,
    )

    return build_invitation_created_response(
        invitation,
        raw_token,
    )

@router.post(
    "/relatives",
    response_model=InvitationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def invite_relative(
    payload: RelativeInvitationCreateRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> InvitationCreatedResponse:
    if auth.active_role not in {
        UserRole.PATIENT,
        UserRole.DOCTOR,
    }:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Приглашать родственника может "
                "только пациент или врач"
            ),
        )

    if auth.active_role == UserRole.PATIENT:
        patient_profile = session.exec(
            select(PatientProfile).where(
                PatientProfile.user_id == auth.user.id
            )
        ).first()

        if not patient_profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Профиль пациента не найден",
            )

        if (
            payload.patient_id is not None
            and payload.patient_id != patient_profile.id
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    "Пациент может приглашать родственников "
                    "только для себя"
                ),
            )

    else:
        if payload.patient_id is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Врач должен указать patient_id",
            )

        doctor_profile = get_authenticated_doctor_profile(
            session=session,
            auth=auth,
        )

        doctor_patient_link = session.exec(
            select(DoctorPatientLink).where(
                DoctorPatientLink.doctor_id
                == doctor_profile.id,
                DoctorPatientLink.patient_id
                == payload.patient_id,
                DoctorPatientLink.status
                == DoctorPatientStatus.ACTIVE,
            )
        ).first()

        if not doctor_patient_link:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Врач не связан с этим пациентом",
            )

        patient_profile = session.get(
            PatientProfile,
            payload.patient_id,
        )

        if not patient_profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пациент не найден",
            )

    patient_user = session.get(
        User,
        patient_profile.user_id,
    )

    if not patient_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У пациента отсутствует пользователь",
        )

    normalized_email = normalize_email(str(payload.email))

    if normalized_email == patient_user.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Нельзя привязать пациента "
                "в качестве родственника самого себя"
            ),
        )

    existing_user = get_user_by_email(
        session,
        normalized_email,
    )

    if existing_user:
        existing_relative = session.exec(
            select(RelativeProfile).where(
                RelativeProfile.user_id == existing_user.id
            )
        ).first()

        if existing_relative:
            existing_link = session.exec(
                select(RelativePatientLink).where(
                    RelativePatientLink.relative_id
                    == existing_relative.id,
                    RelativePatientLink.patient_id
                    == patient_profile.id,
                    RelativePatientLink.status
                    == RelativePatientStatus.ACTIVE,
                )
            ).first()

            if existing_link:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=(
                        "Этот родственник уже привязан "
                        "к пациенту"
                    ),
                )

    invitation, raw_token = create_invitation(
        session=session,
        invitation_type=InvitationType.RELATIVE,
        created_by_user_id=auth.user.id,
        email=normalized_email,
        patient_profile_id=patient_profile.id,
        relationship_degree=payload.relationship_degree,
    )

    return build_invitation_created_response(
        invitation,
        raw_token,
    )

@router.get(
    "/preview",
    response_model=InvitationPreviewResponse,
)
async def preview_invitation(
    token: str,
    session: Session = Depends(get_session),
) -> InvitationPreviewResponse:
    invitation = get_invitation_by_token(
        session=session,
        token=token,
    )

    existing_user = get_user_by_email(
        session,
        invitation.email,
    )

    speciality_name = None

    if invitation.speciality_id:
        speciality = session.get(
            Speciality,
            invitation.speciality_id,
        )
        speciality_name = speciality.name if speciality else None

    return InvitationPreviewResponse(
        invitation_id=invitation.id,
        invitation_type=invitation.invitation_type,
        status=invitation.status,
        email=invitation.email,
        first_name=invitation.first_name,
        last_name=invitation.last_name,
        middle_name=invitation.middle_name,
        fullname=invitation.fullname,
        gender=invitation.gender,
        dob=invitation.dob,
        record_id=invitation.record_id,
        speciality_id=invitation.speciality_id,
        speciality_name=speciality_name,
        relationship_degree=invitation.relationship_degree,
        expires_at=invitation.expires_at,
        is_existing_account=existing_user is not None,
    )


@router.post(
    "/accept",
    response_model=InvitationAcceptResponse,
)
async def accept_invitation(
    payload: InvitationAcceptRequest,
    session: Session = Depends(get_session),
) -> InvitationAcceptResponse:
    if payload.password != payload.password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароли не совпадают",
        )

    invitation = get_invitation_by_token(
        session=session,
        token=payload.token,
    )

    user = get_user_by_email(
        session,
        invitation.email,
    )

    is_new_user = user is None

    if user:
        ensure_user_can_authenticate(user)

        if not verify_password(
            payload.password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=(
                    "Аккаунт с таким email уже существует. "
                    "Введите пароль от существующего аккаунта."
                ),
            )
    else:
        validate_password_strength(payload.password)

        user = User(
            email=invitation.email,
            hashed_password=hash_password(payload.password),
            first_name=(
                payload.first_name
                if payload.first_name is not None
                else invitation.first_name
            ),
            last_name=(
                payload.last_name
                if payload.last_name is not None
                else invitation.last_name
            ),
            middle_name=(
                payload.middle_name
                if payload.middle_name is not None
                else invitation.middle_name
            ),
            gender=(
                payload.gender
                if payload.gender is not None
                else invitation.gender
            ),
        )

        session.add(user)
        session.flush()

    now = utc_now()

    if payload.first_name is not None:
        user.first_name = payload.first_name.strip() or None

    if payload.last_name is not None:
        user.last_name = payload.last_name.strip() or None

    if payload.middle_name is not None:
        user.middle_name = payload.middle_name.strip() or None

    if payload.gender is not None:
        user.gender = payload.gender

    role_added: UserRole

    if invitation.invitation_type == InvitationType.DOCTOR:
        role_added = UserRole.DOCTOR

        existing_doctor = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == user.id
            )
        ).first()

        if existing_doctor:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Профиль врача уже существует",
            )

        speciality_id = (
            payload.speciality_id
            or invitation.speciality_id
        )

        if not speciality_id:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Необходимо выбрать специальность",
            )

        speciality = session.get(
            Speciality,
            speciality_id,
        )

        if not speciality:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Специальность не найдена",
            )

        ensure_user_role(
            session=session,
            user=user,
            role=UserRole.DOCTOR,
        )

        doctor_profile = DoctorProfile(
            user_id=user.id,
            speciality_id=speciality.id,
        )

        session.add(doctor_profile)

    elif invitation.invitation_type == InvitationType.PATIENT:
        role_added = UserRole.PATIENT

        existing_patient = session.exec(
            select(PatientProfile).where(
                PatientProfile.user_id == user.id
            )
        ).first()

        if existing_patient:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Профиль пациента уже существует",
            )

        if not invitation.record_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="В приглашении отсутствует номер карты",
            )

        record_id_owner = session.exec(
            select(PatientProfile).where(
                PatientProfile.record_id
                == invitation.record_id
            )
        ).first()

        if record_id_owner:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Пациент с таким номером карты "
                    "уже зарегистрирован"
                ),
            )

        ensure_user_role(
            session=session,
            user=user,
            role=UserRole.PATIENT,
        )

        patient_profile = PatientProfile(
            user_id=user.id,
            record_id=invitation.record_id,
            fullname=(
                payload.fullname.strip()
                if payload.fullname
                else invitation.fullname
            ),
            dob=(
                payload.dob
                if payload.dob is not None
                else invitation.dob
            ),
        )

        session.add(patient_profile)
        session.flush()

        if invitation.doctor_profile_id:
            doctor_profile = session.get(
                DoctorProfile,
                invitation.doctor_profile_id,
            )

            if not doctor_profile:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=(
                        "Врач, создавший приглашение, "
                        "больше не существует"
                    ),
                )

            link = DoctorPatientLink(
                doctor_id=doctor_profile.id,
                patient_id=patient_profile.id,
                status=DoctorPatientStatus.ACTIVE,
            )

            session.add(link)

    elif invitation.invitation_type == InvitationType.RELATIVE:
        role_added = UserRole.RELATIVE

        if not invitation.patient_profile_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "В приглашении отсутствует "
                    "профиль пациента"
                ),
            )

        patient_profile = session.get(
            PatientProfile,
            invitation.patient_profile_id,
        )

        if not patient_profile:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Пациент больше не существует",
            )

        if patient_profile.user_id == user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Нельзя привязать пользователя "
                    "как родственника самого себя"
                ),
            )

        ensure_user_role(
            session=session,
            user=user,
            role=UserRole.RELATIVE,
        )

        relative_profile = session.exec(
            select(RelativeProfile).where(
                RelativeProfile.user_id == user.id
            )
        ).first()

        if not relative_profile:
            relative_profile = RelativeProfile(
                user_id=user.id
            )
            session.add(relative_profile)
            session.flush()

        relative_link = session.exec(
            select(RelativePatientLink).where(
                RelativePatientLink.relative_id
                == relative_profile.id,
                RelativePatientLink.patient_id
                == patient_profile.id,
            )
        ).first()

        if relative_link:
            relative_link.status = (
                RelativePatientStatus.ACTIVE
            )
            relative_link.relationship_degree = (
                invitation.relationship_degree
            )
            relative_link.detached_at = None
            relative_link.updated_at = now
        else:
            relative_link = RelativePatientLink(
                relative_id=relative_profile.id,
                patient_id=patient_profile.id,
                relationship_degree=(
                    invitation.relationship_degree
                ),
                status=RelativePatientStatus.ACTIVE,
            )

        session.add(relative_link)

    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Неизвестный тип приглашения",
        )

    user.updated_at = now
    invitation.status = InvitationStatus.ACCEPTED
    invitation.accepted_by_user_id = user.id
    invitation.accepted_at = now

    session.add(user)
    session.add(invitation)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Не удалось принять приглашение из-за "
                "конфликта данных"
            ),
        ) from error

    referral = session.exec(
        select(Referral).where(
            Referral.invitation_id == invitation.id
        )
    ).first()

    if referral:
        referral.patient_id = (
            user.patient_profile.id
            if user.patient_profile
            else None
        )

        if referral.patient_id is None:
            patient_profile = session.exec(
                select(PatientProfile).where(
                    PatientProfile.user_id == user.id
                )
            ).first()

            if patient_profile:
                referral.patient_id = patient_profile.id

        referral.status = ReferralStatus.REGISTERED
        referral.registered_at = utc_now()

        session.add(referral)

        record_event(
            session=session,
            event_type=EventType.REGISTRATION_COMPLETED,
            patient_id=referral.patient_id,
            actor_user_id=user.id,
            referral_id=referral.id,
            doctor_id=referral.doctor_id,
            speciality_id=referral.speciality_id,
        )

        session.commit()

    if is_new_user and user.email_verified_at is None:
        send_verification_email(
            session=session,
            user=user,
        )

    return InvitationAcceptResponse(
        message="Приглашение принято",
        user_id=user.id,
        role_added=role_added.value,
        email_verification_required=(
            user.email_verified_at is None
        ),
    )


@router.get(
    "/mine",
    response_model=list[InvitationListItem],
)
async def list_my_invitations(
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> list[InvitationListItem]:
    invitations = session.exec(
        select(Invitation)
        .where(
            Invitation.created_by_user_id == auth.user.id
        )
        .order_by(Invitation.created_at.desc())
    ).all()

    response: list[InvitationListItem] = []
    now = utc_now()

    for invitation in invitations:
        if (
            invitation.status == InvitationStatus.PENDING
            and normalize_datetime(invitation.expires_at) <= now
        ):
            invitation.status = InvitationStatus.EXPIRED
            session.add(invitation)

        response.append(
            InvitationListItem(
                id=invitation.id,
                invitation_type=invitation.invitation_type,
                status=invitation.status,
                email=invitation.email,
                record_id=invitation.record_id,
                created_at=invitation.created_at,
                expires_at=invitation.expires_at,
                accepted_at=invitation.accepted_at,
            )
        )

    session.commit()

    return response


@router.post(
    "/{invitation_id}/revoke",
    response_model=MessageResponse,
)
async def revoke_invitation(
    invitation_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    invitation = session.get(
        Invitation,
        invitation_id,
    )

    if not invitation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Приглашение не найдено",
        )

    if invitation.created_by_user_id != auth.user.id:
        if auth.active_role != UserRole.SUPERUSER:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Нельзя отозвать чужое приглашение",
            )

    if invitation.status != InvitationStatus.PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Можно отзывать только активные приглашения",
        )

    invitation.status = InvitationStatus.REVOKED
    invitation.revoked_at = utc_now()

    session.add(invitation)
    session.commit()

    return MessageResponse(message="Приглашение отозвано")