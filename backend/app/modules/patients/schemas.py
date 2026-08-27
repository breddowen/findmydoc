# ./backend/app/modules/patients/schemas.py
import uuid
from datetime import date, datetime
from typing import Any

from pydantic import BaseModel, EmailStr, Field

from app.modules.events.enums import EventType
from app.modules.patients.enums import (
    PatientRegistrationStatus,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)
from app.modules.users.enums import Gender


class PatientListItem(BaseModel):
    patient_id: uuid.UUID
    user_id: uuid.UUID

    record_id: str
    email: EmailStr
    fullname: str
    dob: date | None
    gender: Gender | None

    registration_status: PatientRegistrationStatus
    registered_at: datetime
    last_activity_at: datetime

    assistant_contact_allowed: bool
    do_not_call: bool

    pro_enabled: bool
    doctors_count: int


class PatientPageResponse(BaseModel):
    items: list[PatientListItem]

    page: int
    page_size: int
    total_items: int
    total_pages: int


class PatientDoctorItem(BaseModel):
    doctor_id: uuid.UUID
    user_id: uuid.UUID

    fullname: str
    email: EmailStr

    speciality_id: uuid.UUID
    speciality_name: str

    linked_at: datetime


class PatientArticleProgressItem(BaseModel):
    article_id: uuid.UUID
    title: str

    progress_percent: float
    max_progress_percent: float

    started_at: datetime
    updated_at: datetime
    completed_at: datetime | None


class PatientQuestionnaireProgressItem(BaseModel):
    submission_id: uuid.UUID
    questionnaire_id: uuid.UUID
    questionnaire_title: str

    status: QuestionnaireSubmissionStatus

    answered_questions: int
    questions_count: int
    progress_percent: float

    started_at: datetime
    completed_at: datetime | None


class PatientEventItem(BaseModel):
    id: uuid.UUID
    event_type: EventType

    subject_type: str | None
    subject_id: uuid.UUID | None

    metadata: dict[str, Any]
    occurred_at: datetime


class PatientDetailResponse(BaseModel):
    patient_id: uuid.UUID
    user_id: uuid.UUID

    record_id: str
    email: EmailStr
    fullname: str
    dob: date | None
    gender: Gender | None

    registration_status: PatientRegistrationStatus
    registered_at: datetime
    last_activity_at: datetime

    assistant_contact_allowed: bool
    do_not_call: bool
    pro_enabled: bool

    doctors: list[PatientDoctorItem]
    articles: list[PatientArticleProgressItem]
    questionnaires: list[
        PatientQuestionnaireProgressItem
    ]
    recent_events: list[PatientEventItem]


class PatientProUpdateRequest(BaseModel):
    pro_enabled: bool


class PatientProResponse(BaseModel):
    patient_id: uuid.UUID
    pro_enabled: bool


class PatientSearchQuery(BaseModel):
    search: str | None = Field(
        default=None,
        max_length=200,
    )