# ./backend/app/modules/tags/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Text, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.users.models import (
    DoctorProfile,
    PatientProfile,
    Speciality,
)


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

    patient_overrides: list["PatientTagOverride"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    life_aspect_links: list["LifeAspectTagLink"] = Relationship(
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

class PatientTagOverride(SQLModel, table=True):
    __tablename__ = "patient_tag_overrides"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "tag_id",
            name="uq_patient_tag_override",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    # Используем тот же enum ADD/REMOVE,
    # что и для индивидуальных тегов врача.
    action: DoctorTagOverrideAction = Field(
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now,
    )
    updated_at: datetime = Field(
        default_factory=utc_now,
    )

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientTagOverride.patient_id]"
            ),
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="patient_overrides",
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientTagOverride.tag_id]"
            ),
        },
    )

class LifeAspect(SQLModel, table=True):
    __tablename__ = "life_aspects"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    name: str = Field(
        max_length=100,
        unique=True,
        index=True,
    )

    # HTML из редактора.
    # На frontend выводим через RichTextRenderer.
    description: Optional[str] = Field(
        default=None,
        sa_type=Text,
    )

    order_index: int = Field(
        default=0,
        index=True,
    )

    is_hidden: bool = Field(
        default=False,
        index=True,
    )
    hidden_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    tag_links: list["LifeAspectTagLink"] = Relationship(
        back_populates="life_aspect",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class LifeAspectTagLink(SQLModel, table=True):
    __tablename__ = "life_aspect_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "life_aspect_id",
            "tag_id",
            name="uq_life_aspect_tag",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    life_aspect_id: uuid.UUID = Field(
        foreign_key="life_aspects.id",
        ondelete="CASCADE",
        index=True,
    )

    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        ondelete="CASCADE",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    life_aspect: Optional[LifeAspect] = Relationship(
        back_populates="tag_links",
    )

    tag: Optional[Tag] = Relationship(
        back_populates="life_aspect_links",
    )