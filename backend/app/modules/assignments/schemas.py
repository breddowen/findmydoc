# ./backend/app/modules/assignments/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel, model_validator

from app.modules.assignments.enums import (
    AssignmentStatus,
    AssignmentType,
)


class AssignmentCreateRequest(BaseModel):
    patient_id: uuid.UUID
    assignment_type: AssignmentType

    article_id: uuid.UUID | None = None
    questionnaire_id: uuid.UUID | None = None

    @model_validator(mode="after")
    def validate_content_reference(self):
        if self.assignment_type == AssignmentType.ARTICLE:
            if not self.article_id or self.questionnaire_id:
                raise ValueError(
                    "Для статьи требуется только article_id"
                )

        if (
            self.assignment_type
            == AssignmentType.QUESTIONNAIRE
        ):
            if not self.questionnaire_id or self.article_id:
                raise ValueError(
                    "Для опросника требуется только "
                    "questionnaire_id"
                )

        return self


class AssignmentResponse(BaseModel):
    id: uuid.UUID

    patient_id: uuid.UUID
    assigned_by_user_id: uuid.UUID

    assignment_type: AssignmentType
    status: AssignmentStatus

    content_id: uuid.UUID
    title: str
    pro_content: bool

    created_at: datetime
    started_at: datetime | None
    completed_at: datetime | None