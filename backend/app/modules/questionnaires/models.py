# ./backend/app/modules/questionnaires/models.py
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import Column, JSON, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
    QuestionType,
)
from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Questionnaire(SQLModel, table=True):
    __tablename__ = "questionnaires"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str = Field(index=True, max_length=300)
    description: Optional[str] = Field(default=None)

    pro_content: bool = Field(default=True, index=True)
    is_hidden: bool = Field(default=False, index=True)

    copied_from_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="questionnaires.id",
        index=True,
    )

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    questions: list["Question"] = Relationship(
        back_populates="questionnaire",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "Question.order_index",
        },
    )

    tag_links: list["QuestionnaireTagLink"] = Relationship(
        back_populates="questionnaire",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class Question(SQLModel, table=True):
    __tablename__ = "questions"
    __table_args__ = (
        UniqueConstraint(
            "questionnaire_id",
            "order_index",
            name="uq_questionnaire_question_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )

    question_type: QuestionType = Field(index=True)
    text: str
    is_required: bool = Field(default=True)

    order_index: int = Field(index=True)

    scale_min: Optional[int] = Field(default=None)
    scale_max: Optional[int] = Field(default=None)
    scale_min_label: Optional[str] = Field(default=None)
    scale_max_label: Optional[str] = Field(default=None)

    questionnaire: Optional[Questionnaire] = Relationship(
        back_populates="questions"
    )

    options: list["QuestionOption"] = Relationship(
        back_populates="question",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "QuestionOption.order_index",
        },
    )


class QuestionOption(SQLModel, table=True):
    __tablename__ = "question_options"
    __table_args__ = (
        UniqueConstraint(
            "question_id",
            "order_index",
            name="uq_question_option_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    question_id: uuid.UUID = Field(
        foreign_key="questions.id",
        index=True,
    )

    text: str
    order_index: int = Field(index=True)

    question: Optional[Question] = Relationship(
        back_populates="options"
    )


class QuestionnaireTagLink(SQLModel, table=True):
    __tablename__ = "questionnaire_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "questionnaire_id",
            "tag_id",
            name="uq_questionnaire_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    questionnaire: Optional[Questionnaire] = Relationship(
        back_populates="tag_links"
    )

    tag: Optional[Tag] = Relationship()


class QuestionnaireSubmission(SQLModel, table=True):
    __tablename__ = "questionnaire_submissions"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    # Если опросник запущен внутри программы.
    program_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="programs.id",
        index=True,
    )
    program_stage_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="program_stages.id",
        index=True,
    )

    status: QuestionnaireSubmissionStatus = Field(
        default=QuestionnaireSubmissionStatus.IN_PROGRESS,
        index=True,
    )

    started_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)

    answers: list["QuestionAnswer"] = Relationship(
        back_populates="submission",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class QuestionAnswer(SQLModel, table=True):
    __tablename__ = "question_answers"
    __table_args__ = (
        UniqueConstraint(
            "submission_id",
            "question_id",
            name="uq_submission_question_answer",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    submission_id: uuid.UUID = Field(
        foreign_key="questionnaire_submissions.id",
        index=True,
    )
    question_id: uuid.UUID = Field(
        foreign_key="questions.id",
        index=True,
    )

    value_json: Any = Field(
        sa_column=Column(JSON, nullable=False)
    )

    created_at: datetime = Field(default_factory=utc_now)

    submission: Optional[QuestionnaireSubmission] = Relationship(
        back_populates="answers"
    )