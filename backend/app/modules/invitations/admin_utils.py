# ./backend/app/modules/invitations/admin_utils.py
import re
import uuid

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.core.security import AuthContext
from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.invitations.models import Invitation
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    PatientProfile,
    Speciality,
    User,
)
from app.modules.users.utils import (
    get_user_by_email,
    normalize_email,
)


RECORD_ID_PATTERN = re.compile(r"^[A-Z]{1,2}[0-9]{6}$")


ADMIN_INVITATION_ROLES = {
    UserRole.PATIENT,
    UserRole.DOCTOR,
    UserRole.RELATIVE,
    UserRole.MED_ASSISTANT,
    UserRole.SUPERUSER,
}


ASSISTANT_INVITATION_ROLES = {
    UserRole.PATIENT,
    UserRole.DOCTOR,
    UserRole.RELATIVE,
}


def role_to_invitation_type(
    role: UserRole,
) -> InvitationType:
    try:
        return InvitationType(role.value)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Для выбранной роли приглашения не поддерживаются",
        ) from error


def ensure_admin_can_invite_role(
    *,
    auth: AuthContext,
    role: UserRole,
) -> None:
    if role not in ADMIN_INVITATION_ROLES:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Неизвестная роль приглашения",
        )

    if auth.active_role == UserRole.SUPERUSER:
        return

    if (
        auth.active_role == UserRole.MED_ASSISTANT
        and role in ASSISTANT_INVITATION_ROLES
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Нельзя приглашать пользователя с этой ролью",
    )


def ensure_admin_can_manage_invitation(
    *,
    auth: AuthContext,
    invitation: Invitation,
) -> None:
    if auth.active_role == UserRole.SUPERUSER:
        return

    if (
        auth.active_role == UserRole.MED_ASSISTANT
        and invitation.created_by_user_id == auth.user.id
        and invitation.invitation_type
        in {
            InvitationType.PATIENT,
            InvitationType.DOCTOR,
            InvitationType.RELATIVE,
        }
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Нет доступа к этому приглашению",
    )


def ensure_email_is_available(
    *,
    session: Session,
    email: str,
) -> str:
    normalized_email = normalize_email(email)

    existing_user = get_user_by_email(
        session,
        normalized_email,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Пользователь с таким email уже зарегистрирован"
            ),
        )

    return normalized_email


def validate_admin_patient_record_id(
    *,
    session: Session,
    record_id: str | None,
) -> str:
    if not record_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Для пациента необходимо указать record_id",
        )

    normalized_record_id = record_id.strip().upper()

    if not RECORD_ID_PATTERN.fullmatch(normalized_record_id):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=(
                "record_id должен содержать одну или две "
                "латинские буквы и шесть цифр"
            ),
        )

    existing_patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.record_id == normalized_record_id
        )
    ).first()

    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Пациент с таким record_id уже зарегистрирован"
            ),
        )

    return normalized_record_id


def validate_admin_doctor_speciality(
    *,
    session: Session,
    speciality_id: uuid.UUID | None,
) -> Speciality:
    if not speciality_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Для врача необходимо выбрать специальность",
        )

    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality or speciality.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена или скрыта",
        )

    return speciality


def invitation_creator_name(user: User) -> str:
    return (
        " ".join(
            part
            for part in [
                user.last_name,
                user.first_name,
                user.middle_name,
            ]
            if part
        )
        or user.email
    )


def update_expired_invitation(
    *,
    session: Session,
    invitation: Invitation,
    now,
) -> None:
    from app.modules.invitations.utils import normalize_datetime

    if (
        invitation.status == InvitationStatus.PENDING
        and normalize_datetime(invitation.expires_at) <= now
    ):
        invitation.status = InvitationStatus.EXPIRED
        session.add(invitation)