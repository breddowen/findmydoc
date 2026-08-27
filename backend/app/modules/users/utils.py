# ./backend/app/modules/users/utils.py
import uuid

from sqlmodel import Session, select

from app.modules.users.enums import UserRole
from app.modules.users.models import User, UserRoleLink
from app.modules.users.schemas import (
    DoctorProfileResponse,
    PatientProfileResponse,
    RelativeProfileResponse,
    RoleResponse,
    SpecialityResponse,
    UserResponse,
)


def normalize_email(email: str) -> str:
    return email.strip().lower()


def get_user_by_email(session: Session, email: str) -> User | None:
    normalized_email = normalize_email(email)

    return session.exec(
        select(User).where(User.email == normalized_email)
    ).first()


def get_user_by_id(session: Session, user_id: uuid.UUID) -> User | None:
    return session.get(User, user_id)


def get_user_roles(session: Session, user_id: uuid.UUID) -> list[UserRoleLink]:
    return list(
        session.exec(
            select(UserRoleLink)
            .where(UserRoleLink.user_id == user_id)
            .order_by(UserRoleLink.is_primary.desc(), UserRoleLink.created_at)
        ).all()
    )


def user_has_role(
    session: Session,
    user_id: uuid.UUID,
    role: UserRole,
) -> bool:
    role_link = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.user_id == user_id,
            UserRoleLink.role == role,
        )
    ).first()

    return role_link is not None


def get_primary_role(
    session: Session,
    user_id: uuid.UUID,
) -> UserRole | None:
    links = get_user_roles(session, user_id)

    if not links:
        return None

    primary = next((link for link in links if link.is_primary), None)

    return primary.role if primary else links[0].role


def build_user_response(
    *,
    session: Session,
    user: User,
    active_role: UserRole | None = None,
) -> UserResponse:
    role_links = get_user_roles(session, user.id)

    doctor_profile = None
    if user.doctor_profile and user.doctor_profile.speciality:
        doctor_profile = DoctorProfileResponse(
            id=user.doctor_profile.id,
            speciality=SpecialityResponse.model_validate(
                user.doctor_profile.speciality
            ),
        )

    patient_profile = None
    if user.patient_profile:
        patient_profile = PatientProfileResponse.model_validate(
            user.patient_profile
        )

    relative_profile = None
    if user.relative_profile:
        relative_profile = RelativeProfileResponse.model_validate(
            user.relative_profile
        )

    return UserResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        gender=user.gender,
        is_active=user.is_active,
        is_blocked=user.is_blocked,
        is_email_verified=user.email_verified_at is not None,
        deleted_at=user.deleted_at,
        roles=[
            RoleResponse(
                role=role_link.role,
                is_primary=role_link.is_primary,
            )
            for role_link in role_links
        ],
        active_role=active_role,
        doctor_profile=doctor_profile,
        patient_profile=patient_profile,
        relative_profile=relative_profile,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )