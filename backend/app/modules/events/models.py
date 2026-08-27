# ./backend/app/modules/events/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, SQLModel

from app.modules.events.enums import EventType


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    event_type: EventType = Field(index=True)

    patient_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="patient_profiles.id",
        index=True,
    )

    actor_user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    referral_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="referrals.id",
        index=True,
    )

    doctor_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="doctor_profiles.id",
        index=True,
    )

    speciality_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="specialities.id",
        index=True,
    )

    product_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    program_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    subject_type: Optional[str] = Field(
        default=None,
        index=True,
        max_length=100,
    )

    subject_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    metadata_json: dict = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )

    occurred_at: datetime = Field(
        default_factory=utc_now,
        index=True,
    )
    created_at: datetime = Field(default_factory=utc_now)