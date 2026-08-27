# ./backend/app/modules/questionnaires/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, model_validator

from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
    QuestionType,
)


class QuestionOptionCreateRequest(BaseModel):
    text: str = Field(min_length=1)
    order_index: int = Field(ge=0)


class QuestionCreateRequest(BaseModel):
    question_type: QuestionType
    text: str = Field(min_length=1)
    is_required: bool = True
    order_index: int = Field(ge=0)

    scale_min: int | None = None
    scale_max: int | None = None
    scale_min_label: str | None = None
    scale_max_label: str | None = None

    options: list[QuestionOptionCreateRequest] = []

    @model_validator(mode="after")
    def validate_question(self):
        choice_types = {
            QuestionType.SINGLE_CHOICE,
            QuestionType.MULTIPLE_CHOICE,
        }

        if (
            self.question_type in choice_types
            and len(self.options) < 2
        ):
            raise ValueError(
                "В вопросе с вариантами ответа "
                "должно быть не менее двух вариантов"
            )

        if self.question_type == QuestionType.SCALE:
            if (
                self.scale_min is None
                or self.scale_max is None
            ):
                raise ValueError(
                    "Для шкалы нужны scale_min и scale_max"
                )

            if self.scale_max <= self.scale_min:
                raise ValueError(
                    "scale_max должен быть больше scale_min"
                )

        return self


class QuestionnaireCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    description: str | None = None

    tag_ids: list[uuid.UUID] = []
    pro_content: bool = True

    copied_from_id: uuid.UUID | None = None

    questions: list[QuestionCreateRequest] = Field(
        min_length=1
    )


class QuestionnaireCopyRequest(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )


class QuestionnaireVisibilityRequest(BaseModel):
    is_hidden: bool


class QuestionOptionResponse(BaseModel):
    id: uuid.UUID
    text: str
    order_index: int


class QuestionResponse(BaseModel):
    id: uuid.UUID
    question_type: QuestionType
    text: str
    is_required: bool
    order_index: int

    scale_min: int | None
    scale_max: int | None
    scale_min_label: str | None
    scale_max_label: str | None

    options: list[QuestionOptionResponse]


class QuestionnaireTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class QuestionnaireResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    copied_from_id: uuid.UUID | None

    tags: list[QuestionnaireTagResponse]
    questions: list[QuestionResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    hidden_at: datetime | None


class QuestionnaireListItem(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    tags: list[QuestionnaireTagResponse]

    questions_count: int
    created_at: datetime


class SubmissionStartResponse(BaseModel):
    submission_id: uuid.UUID
    questionnaire_id: uuid.UUID
    status: QuestionnaireSubmissionStatus
    started_at: datetime


class AnswerSubmitRequest(BaseModel):
    question_id: uuid.UUID
    value: Any


class SubmissionCompleteRequest(BaseModel):
    answers: list[AnswerSubmitRequest]


class AnswerResponse(BaseModel):
    question_id: uuid.UUID
    question_text: str
    question_type: QuestionType
    value: Any


class SubmissionResponse(BaseModel):
    id: uuid.UUID
    questionnaire_id: uuid.UUID
    patient_id: uuid.UUID

    program_id: uuid.UUID | None
    program_stage_id: uuid.UUID | None

    status: QuestionnaireSubmissionStatus
    started_at: datetime
    completed_at: datetime | None

    answers: list[AnswerResponse]

class AnswerSaveRequest(BaseModel):
    question_id: uuid.UUID
    value: Any


class AnswerSaveResponse(BaseModel):
    submission_id: uuid.UUID
    question_id: uuid.UUID
    value: Any
    saved_at: datetime


class SubmissionProgressItem(BaseModel):
    submission_id: uuid.UUID
    questionnaire_id: uuid.UUID
    questionnaire_title: str

    program_id: uuid.UUID | None
    program_stage_id: uuid.UUID | None

    status: QuestionnaireSubmissionStatus
    answered_questions: int
    questions_count: int
    progress_percent: float

    started_at: datetime
    completed_at: datetime | None