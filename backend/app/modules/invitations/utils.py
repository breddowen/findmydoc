# ./backend/app/modules/invitations/utils.py
import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.core.config import settings
from app.core.email import send_console_email
from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.invitations.models import Invitation
from app.modules.users.enums import UserRole
from app.modules.users.models import User, UserRoleLink


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def normalize_datetime(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value


def hash_invitation_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def generate_invitation_token() -> str:
    return secrets.token_urlsafe(48)


def build_registration_url(token: str) -> str:
    frontend_url = settings.FRONTEND_URL.rstrip("/")
    return f"{frontend_url}/register/invitation?token={token}"


def revoke_similar_pending_invitations(
    *,
    session: Session,
    invitation_type: InvitationType,
    email: str,
    record_id: str | None = None,
) -> None:
    statement = select(Invitation).where(
        Invitation.invitation_type == invitation_type,
        Invitation.email == email,
        Invitation.status == InvitationStatus.PENDING,
    )

    if record_id is not None:
        statement = statement.where(
            Invitation.record_id == record_id
        )

    invitations = session.exec(statement).all()
    now = utc_now()

    for invitation in invitations:
        invitation.status = InvitationStatus.REVOKED
        invitation.revoked_at = now
        session.add(invitation)


def create_invitation(
    *,
    session: Session,
    invitation_type: InvitationType,
    created_by_user_id: uuid.UUID,
    email: str,
    record_id: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    middle_name: str | None = None,
    fullname: str | None = None,
    gender=None,
    dob=None,
    speciality_id: uuid.UUID | None = None,
    doctor_profile_id: uuid.UUID | None = None,
    patient_profile_id: uuid.UUID | None = None,
    relationship_degree: str | None = None,
    send_email: bool = True,
) -> tuple[Invitation, str]:
    normalized_email = email.strip().lower()

    revoke_similar_pending_invitations(
        session=session,
        invitation_type=invitation_type,
        email=normalized_email,
        record_id=record_id,
    )

    raw_token = generate_invitation_token()

    invitation = Invitation(
        invitation_type=invitation_type,
        status=InvitationStatus.PENDING,
        token_hash=hash_invitation_token(raw_token),
        created_by_user_id=created_by_user_id,
        email=normalized_email,
        record_id=record_id.strip() if record_id else None,
        first_name=first_name.strip() if first_name else None,
        last_name=last_name.strip() if last_name else None,
        middle_name=middle_name.strip() if middle_name else None,
        fullname=fullname.strip() if fullname else None,
        gender=gender,
        dob=dob,
        speciality_id=speciality_id,
        doctor_profile_id=doctor_profile_id,
        patient_profile_id=patient_profile_id,
        relationship_degree=(
            relationship_degree.strip()
            if relationship_degree
            else None
        ),
        expires_at=utc_now()
        + timedelta(hours=settings.INVITATION_EXPIRE_HOURS),
    )

    session.add(invitation)
    session.commit()
    session.refresh(invitation)

    if send_email:
        send_console_email(
            recipient=invitation.email,
            subject="Приглашение в MentalMe",
            message=(
                "Для регистрации или добавления новой роли "
                "перейдите по ссылке:"
            ),
            action_path="/register/invitation",
            token=raw_token,
        )

    return invitation, raw_token


def get_invitation_by_token(
    *,
    session: Session,
    token: str,
    require_pending: bool = True,
) -> Invitation:
    invitation = session.exec(
        select(Invitation).where(
            Invitation.token_hash == hash_invitation_token(token)
        )
    ).first()

    if not invitation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Приглашение не найдено",
        )

    if require_pending and invitation.status != InvitationStatus.PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Приглашение уже использовано или отозвано",
        )

    if normalize_datetime(invitation.expires_at) <= utc_now():
        if invitation.status == InvitationStatus.PENDING:
            invitation.status = InvitationStatus.EXPIRED
            session.add(invitation)
            session.commit()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Срок действия приглашения истёк",
        )

    return invitation


def ensure_user_role(
    *,
    session: Session,
    user: User,
    role: UserRole,
) -> UserRoleLink:
    role_link = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.user_id == user.id,
            UserRoleLink.role == role,
        )
    ).first()

    if role_link:
        return role_link

    has_any_role = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.user_id == user.id
        )
    ).first()

    role_link = UserRoleLink(
        user_id=user.id,
        role=role,
        is_primary=has_any_role is None,
    )

    session.add(role_link)
    session.flush()

    return role_link