# ./backend/app/modules/referrals/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules.invitations.models import Invitation
from app.modules.referrals.enums import (
    ReferralSource,
    ReferralStatus,
)
from app.modules.users.models import (
    DoctorProfile,
    PatientProfile,
    Speciality,
    User,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Referral(SQLModel, table=True):
    __tablename__ = "referrals"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    token_hash: str = Field(
        unique=True,
        index=True,
        max_length=64,
    )

    status: ReferralStatus = Field(
        default=ReferralStatus.CREATED,
        index=True,
    )
    source: ReferralSource = Field(index=True)

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    doctor_id: uuid.UUID = Field(
        foreign_key="doctor_profiles.id",
        index=True,
    )

    patient_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="patient_profiles.id",
        index=True,
    )

    invitation_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="invitations.id",
        index=True,
    )

    speciality_id: uuid.UUID = Field(
        foreign_key="specialities.id",
        index=True,
    )

    speciality_name_snapshot: str = Field(max_length=200)
    is_psychiatric_speciality_snapshot: bool = Field(
        default=False,
        index=True,
    )

    record_id_snapshot: str = Field(
        index=True,
        max_length=100,
    )

    created_at: datetime = Field(default_factory=utc_now)
    link_sent_at: Optional[datetime] = Field(default=None)
    opened_at: Optional[datetime] = Field(default=None)
    registered_at: Optional[datetime] = Field(default=None)
    cancelled_at: Optional[datetime] = Field(default=None)

    created_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Referral.created_by_user_id]",
        }
    )

    doctor: Optional[DoctorProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Referral.doctor_id]",
        }
    )

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Referral.patient_id]",
        }
    )

    invitation: Optional[Invitation] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Referral.invitation_id]",
        }
    )

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Referral.speciality_id]",
        }
    )