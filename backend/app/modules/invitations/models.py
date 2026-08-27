# ./backend/app/modules/invitations/models.py
import uuid
from datetime import date, datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.users.enums import Gender
from app.modules.users.models import (
    DoctorProfile,
    PatientProfile,
    Speciality,
    User,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Invitation(SQLModel, table=True):
    __tablename__ = "invitations"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    invitation_type: InvitationType = Field(index=True)
    status: InvitationStatus = Field(
        default=InvitationStatus.PENDING,
        index=True,
    )

    token_hash: str = Field(unique=True, index=True, max_length=64)

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    email: str = Field(index=True, max_length=320)

    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    middle_name: Optional[str] = Field(default=None, max_length=100)
    fullname: Optional[str] = Field(default=None, max_length=300)

    gender: Optional[Gender] = Field(default=None)
    dob: Optional[date] = Field(default=None)

    speciality_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="specialities.id",
        index=True,
    )

    doctor_profile_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="doctor_profiles.id",
        index=True,
    )

    patient_profile_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="patient_profiles.id",
        index=True,
    )

    record_id: Optional[str] = Field(
        default=None,
        index=True,
        max_length=100,
    )

    relationship_degree: Optional[str] = Field(
        default=None,
        max_length=100,
    )

    accepted_by_user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    expires_at: datetime = Field(index=True)
    accepted_at: Optional[datetime] = Field(default=None)
    revoked_at: Optional[datetime] = Field(default=None)

    created_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Invitation.created_by_user_id]",
        }
    )

    accepted_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Invitation.accepted_by_user_id]",
        }
    )

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Invitation.speciality_id]",
        }
    )

    doctor_profile: Optional[DoctorProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Invitation.doctor_profile_id]",
        }
    )

    patient_profile: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Invitation.patient_profile_id]",
        }
    )