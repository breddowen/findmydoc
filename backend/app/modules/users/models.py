# ./backend/app/modules/users/models.py
import uuid
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.users.enums import (
    DoctorPatientStatus,
    Gender,
    RelativePatientStatus,
    UserRole,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UserRoleLink(SQLModel, table=True):
    __tablename__ = "user_role_links"
    __table_args__ = (
        UniqueConstraint("user_id", "role", name="uq_user_role"),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)
    role: UserRole = Field(index=True)
    is_primary: bool = Field(default=False)

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional["User"] = Relationship(back_populates="role_links")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    email: str = Field(unique=True, index=True, max_length=320)
    hashed_password: Optional[str] = Field(default=None)

    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    middle_name: Optional[str] = Field(default=None, max_length=100)
    gender: Optional[Gender] = Field(default=None)

    is_active: bool = Field(default=True, index=True)
    is_blocked: bool = Field(default=False, index=True)
    email_verified_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None, index=True)

    # При смене пароля значение увеличивается, старые JWT становятся невалидными.
    auth_version: int = Field(default=1)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    role_links: list[UserRoleLink] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    doctor_profile: Optional["DoctorProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[DoctorProfile.user_id]",
        },
    )

    patient_profile: Optional["PatientProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[PatientProfile.user_id]",
        },
    )

    relative_profile: Optional["RelativeProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[RelativeProfile.user_id]",
        },
    )

    med_assistant_profile: Optional["MedAssistantProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[MedAssistantProfile.user_id]",
        },
    )


class Speciality(SQLModel, table=True):
    __tablename__ = "specialities"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True, max_length=200)
    description: Optional[str] = Field(default=None)

    consultation_name: Optional[str] = Field(
        default=None,
        max_length=300,
    )
    consultation_description: Optional[str] = Field(
        default=None,
    )

    is_hidden: bool = Field(default=False, index=True)
    hidden_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)

    doctors: list["DoctorProfile"] = Relationship(
        back_populates="speciality"
    )


class DoctorProfile(SQLModel, table=True):
    __tablename__ = "doctor_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )
    speciality_id: uuid.UUID = Field(
        foreign_key="specialities.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="doctor_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorProfile.user_id]",
        },
    )

    speciality: Optional[Speciality] = Relationship(back_populates="doctors")

    patient_links: list["DoctorPatientLink"] = Relationship(
        back_populates="doctor",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.doctor_id]",
        },
    )


class PatientProfile(SQLModel, table=True):
    __tablename__ = "patient_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    record_id: str = Field(unique=True, index=True, max_length=100)
    fullname: Optional[str] = Field(default=None, max_length=300)
    dob: Optional[date] = Field(default=None)

    pro_enabled: bool = Field(default=False)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="patient_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProfile.user_id]",
        },
    )

    doctor_links: list["DoctorPatientLink"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.patient_id]",
        },
    )

    relative_links: list["RelativePatientLink"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.patient_id]",
        },
    )


class RelativeProfile(SQLModel, table=True):
    __tablename__ = "relative_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="relative_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativeProfile.user_id]",
        },
    )

    patient_links: list["RelativePatientLink"] = Relationship(
        back_populates="relative",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.relative_id]",
        },
    )


class MedAssistantProfile(SQLModel, table=True):
    __tablename__ = "med_assistant_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="med_assistant_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[MedAssistantProfile.user_id]",
        },
    )


class DoctorPatientLink(SQLModel, table=True):
    __tablename__ = "doctor_patient_links"
    __table_args__ = (
        UniqueConstraint(
            "doctor_id",
            "patient_id",
            name="uq_doctor_patient",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doctor_id: uuid.UUID = Field(
        foreign_key="doctor_profiles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    status: DoctorPatientStatus = Field(
        default=DoctorPatientStatus.ACTIVE,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    detached_at: Optional[datetime] = Field(default=None)

    doctor: Optional[DoctorProfile] = Relationship(
        back_populates="patient_links",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.doctor_id]",
        },
    )

    patient: Optional[PatientProfile] = Relationship(
        back_populates="doctor_links",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.patient_id]",
        },
    )


class RelativePatientLink(SQLModel, table=True):
    __tablename__ = "relative_patient_links"
    __table_args__ = (
        UniqueConstraint(
            "relative_id",
            "patient_id",
            name="uq_relative_patient",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    relative_id: uuid.UUID = Field(
        foreign_key="relative_profiles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    relationship_degree: Optional[str] = Field(default=None, max_length=100)
    status: RelativePatientStatus = Field(
        default=RelativePatientStatus.ACTIVE,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    detached_at: Optional[datetime] = Field(default=None)

    relative: Optional[RelativeProfile] = Relationship(
        back_populates="patient_links",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.relative_id]",
        },
    )

    patient: Optional[PatientProfile] = Relationship(
        back_populates="relative_links",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.patient_id]",
        },
    )