# ./backend/app/modules/programs/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import UniqueConstraint

from app.modules.articles.models import Article
from app.modules.services.models import MedicalService
from app.modules.questionnaires.models import Questionnaire
from app.modules.tags.models import Tag
from app.modules.users.models import (
    PatientProfile,
    Speciality,
    User,
)
from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
)

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Program(SQLModel, table=True):
    __tablename__ = "programs"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    title: str = Field(
        index=True,
        max_length=300,
    )
    description: Optional[str] = Field(default=None)

    service_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="medical_services.id",
        index=True,
    )

    pro_content: bool = Field(
        default=False,
        index=True,
    )

    is_popular: bool = Field(
        default=False,
        index=True,
    )

    is_hidden: bool = Field(
        default=False,
        index=True,
    )

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    service: Optional[MedicalService] = Relationship(
        back_populates="programs",
        sa_relationship_kwargs={
            "foreign_keys": "[Program.service_id]",
        },
    )

    stages: list["ProgramStage"] = Relationship(
        back_populates="program",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "ProgramStage.order_index",
        },
    )

    tag_links: list["ProgramTagLink"] = Relationship(
        back_populates="program",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class ProgramStage(SQLModel, table=True):
    __tablename__ = "program_stages"
    __table_args__ = (
        UniqueConstraint(
            "program_id",
            "order_index",
            name="uq_program_stage_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    title: str = Field(max_length=300)
    description: Optional[str] = Field(default=None)
    doctor_description: Optional[str] = Field(default=None)

    day_from: int = Field(index=True)
    day_to: int = Field(index=True)
    order_index: int = Field(index=True)

    program: Optional[Program] = Relationship(
        back_populates="stages"
    )

    items: list["ProgramStageItem"] = Relationship(
        back_populates="stage",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "ProgramStageItem.order_index",
        },
    )


class ProgramStageItem(SQLModel, table=True):
    __tablename__ = "program_stage_items"
    __table_args__ = (
        UniqueConstraint(
            "stage_id",
            "order_index",
            name="uq_program_stage_item_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    stage_id: uuid.UUID = Field(
        foreign_key="program_stages.id",
        index=True,
    )

    item_type: ProgramItemType = Field(index=True)
    order_index: int = Field(index=True)

    article_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="articles.id",
        index=True,
    )
    questionnaire_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="questionnaires.id",
        index=True,
    )
    speciality_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="specialities.id",
        index=True,
    )

    consultation_title: Optional[str] = Field(
        default=None,
        max_length=300,
    )
    consultation_description: Optional[str] = Field(
        default=None,
    )

    stage: Optional[ProgramStage] = Relationship(
        back_populates="items"
    )

    article: Optional[Article] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramStageItem.article_id]",
        }
    )

    questionnaire: Optional[Questionnaire] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[ProgramStageItem.questionnaire_id]"
            ),
        }
    )

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramStageItem.speciality_id]",
        }
    )


class ProgramTagLink(SQLModel, table=True):
    __tablename__ = "program_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "program_id",
            "tag_id",
            name="uq_program_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    program: Optional[Program] = Relationship(
        back_populates="tag_links"
    )

    tag: Optional[Tag] = Relationship()


class PatientProgramAccess(SQLModel, table=True):
    __tablename__ = "patient_program_access"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "program_id",
            name="uq_patient_program_access",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    is_active: bool = Field(default=False, index=True)

    # Текущий активный запрос пациента на покупку.
    purchase_requested: bool = Field(
        default=False,
        index=True,
    )
    requested_at: Optional[datetime] = Field(default=None)

    activated_at: Optional[datetime] = Field(default=None)
    deactivated_at: Optional[datetime] = Field(default=None)

    updated_by_user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProgramAccess.patient_id]",
        }
    )

    program: Optional[Program] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProgramAccess.program_id]",
        }
    )

    updated_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientProgramAccess.updated_by_user_id]"
            ),
        }
    )


class ProgramEnrollment(SQLModel, table=True):
    __tablename__ = "program_enrollments"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "program_id",
            name="uq_patient_program_enrollment",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    status: ProgramEnrollmentStatus = Field(
        default=ProgramEnrollmentStatus.ACTIVE,
        index=True,
    )

    started_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)
    cancelled_at: Optional[datetime] = Field(default=None)

    # Эти поля не позволяют создавать повторные события.
    in_progress_event_at: Optional[datetime] = Field(default=None)
    completed_event_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramEnrollment.patient_id]",
        }
    )

    program: Optional[Program] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramEnrollment.program_id]",
        }
    )