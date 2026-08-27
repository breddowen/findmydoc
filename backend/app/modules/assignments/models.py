# ./backend/app/modules/assignments/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules.articles.models import Article
from app.modules.assignments.enums import (
    AssignmentStatus,
    AssignmentType,
)
from app.modules.questionnaires.models import Questionnaire
from app.modules.users.models import PatientProfile, User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ContentAssignment(SQLModel, table=True):
    __tablename__ = "content_assignments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    assigned_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    assignment_type: AssignmentType = Field(index=True)
    status: AssignmentStatus = Field(
        default=AssignmentStatus.ASSIGNED,
        index=True,
    )

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

    created_at: datetime = Field(default_factory=utc_now)
    started_at: Optional[datetime] = Field(default=None)
    completed_at: Optional[datetime] = Field(default=None)
    cancelled_at: Optional[datetime] = Field(default=None)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ContentAssignment.patient_id]",
        }
    )

    assigned_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ContentAssignment.assigned_by_user_id]",
        }
    )

    article: Optional[Article] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ContentAssignment.article_id]",
        }
    )

    questionnaire: Optional[Questionnaire] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ContentAssignment.questionnaire_id]",
        }
    )