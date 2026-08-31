# ./backend/app/modules/tags/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.users.models import DoctorProfile, Speciality


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Tag(SQLModel, table=True):
    __tablename__ = "tags"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    name: str = Field(
        unique=True,
        index=True,
        max_length=100,
    )
    description: Optional[str] = Field(default=None)

    # Системные теги нельзя удалить через обычный API.
    is_system: bool = Field(default=False, index=True)

    is_hidden: bool = Field(default=False, index=True)
    hidden_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    speciality_links: list["SpecialityTagLink"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    doctor_overrides: list["DoctorTagOverride"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class SpecialityTagLink(SQLModel, table=True):
    __tablename__ = "speciality_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "speciality_id",
            "tag_id",
            name="uq_speciality_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    speciality_id: uuid.UUID = Field(
        foreign_key="specialities.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[SpecialityTagLink.speciality_id]",
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="speciality_links",
        sa_relationship_kwargs={
            "foreign_keys": "[SpecialityTagLink.tag_id]",
        },
    )


class DoctorTagOverride(SQLModel, table=True):
    __tablename__ = "doctor_tag_overrides"
    __table_args__ = (
        UniqueConstraint(
            "doctor_id",
            "tag_id",
            name="uq_doctor_tag_override",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    doctor_id: uuid.UUID = Field(
        foreign_key="doctor_profiles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    action: DoctorTagOverrideAction = Field(index=True)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    doctor: Optional[DoctorProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorTagOverride.doctor_id]",
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="doctor_overrides",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorTagOverride.tag_id]",
        },
    )