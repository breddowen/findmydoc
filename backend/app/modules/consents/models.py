# ./backend/app/modules/consents/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules.consents.enums import ConsentType
from app.modules.users.models import PatientProfile, User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ConsentRecord(SQLModel, table=True):
    __tablename__ = "consent_records"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    consent_type: ConsentType = Field(index=True)
    accepted: bool = Field(index=True)

    document_version: str = Field(
        default="1.0",
        max_length=50,
    )

    recorded_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now,
        index=True,
    )

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ConsentRecord.patient_id]",
        }
    )

    recorded_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ConsentRecord.recorded_by_user_id]",
        }
    )


class ContactPreference(SQLModel, table=True):
    __tablename__ = "contact_preferences"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        unique=True,
        index=True,
    )

    allow_assistant_contact: bool = Field(default=False)
    do_not_call: bool = Field(default=False, index=True)

    updated_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ContactPreference.patient_id]",
        }
    )