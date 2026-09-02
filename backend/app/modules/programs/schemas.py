# ./backend/app/modules/programs/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel, Field, model_validator

from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
    ProgramStageStatus,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)

from app.modules.services.schemas import (
    MedicalServicePatientResponse,
    MedicalServiceStaffResponse,
)

class ProgramStageItemCreateRequest(BaseModel):
    item_type: ProgramItemType
    order_index: int = Field(ge=0)

    article_id: uuid.UUID | None = None
    questionnaire_id: uuid.UUID | None = None
    speciality_id: uuid.UUID | None = None

    consultation_title: str | None = Field(
        default=None,
        max_length=300,
    )
    consultation_description: str | None = None

    @model_validator(mode="after")
    def validate_reference(self):
        if self.item_type == ProgramItemType.ARTICLE:
            if (
                not self.article_id
                or self.questionnaire_id
                or self.speciality_id
            ):
                raise ValueError(
                    "Для статьи требуется только article_id"
                )

        if self.item_type == ProgramItemType.QUESTIONNAIRE:
            if (
                not self.questionnaire_id
                or self.article_id
                or self.speciality_id
            ):
                raise ValueError(
                    "Для опросника требуется только "
                    "questionnaire_id"
                )

        if self.item_type == ProgramItemType.CONSULTATION:
            if (
                not self.speciality_id
                or self.article_id
                or self.questionnaire_id
            ):
                raise ValueError(
                    "Для консультации требуется только "
                    "speciality_id"
                )

        return self


class ProgramStageCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)

    description: str | None = None
    doctor_description: str | None = None

    day_from: int = Field(ge=0)
    day_to: int = Field(ge=0)
    order_index: int = Field(ge=0)

    items: list[ProgramStageItemCreateRequest] = []

    @model_validator(mode="after")
    def validate_period(self):
        if self.day_to < self.day_from:
            raise ValueError(
                "day_to не может быть меньше day_from"
            )

        return self


class ProgramCreateRequest(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=300,
    )
    description: str | None = None

    # NULL означает бесплатную программу
    # без связанной медицинской услуги.
    service_id: uuid.UUID | None = None

    is_popular: bool = False

    tag_ids: list[uuid.UUID] = []
    stages: list[ProgramStageCreateRequest] = Field(
        min_length=1
    )

class ProgramUpdateRequest(ProgramCreateRequest):
    pass


class ProgramVisibilityRequest(BaseModel):
    is_hidden: bool


class ProgramAccessUpdateRequest(BaseModel):
    is_active: bool


class ProgramTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class ProgramStageItemResponse(BaseModel):
    id: uuid.UUID
    item_type: ProgramItemType
    order_index: int

    content_id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    speciality_id: uuid.UUID | None = None
    speciality_name: str | None = None

    can_access: bool = True
    is_completed: bool = False

    # Заполняется для опросника при просмотре
    # программы конкретного пациента.
    submission_id: uuid.UUID | None = None
    submission_status: (
        QuestionnaireSubmissionStatus | None
    ) = None


class ProgramStagePatientResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    day_from: int
    day_to: int
    order_index: int

    status: ProgramStageStatus
    progress_percent: float

    items: list[ProgramStageItemResponse]


class ProgramStageClinicalResponse(
    ProgramStagePatientResponse
):
    doctor_description: str | None


class ProgramEnrollmentResponse(BaseModel):
    id: uuid.UUID
    status: ProgramEnrollmentStatus

    started_at: datetime
    completed_at: datetime | None

    elapsed_days: int


class ProgramPatientResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    service: MedicalServicePatientResponse | None
    is_popular: bool

    tags: list[ProgramTagResponse]

    has_program_access: bool
    purchase_requested: bool

    progress_percent: float
    enrollment: ProgramEnrollmentResponse | None

    stages: list[ProgramStagePatientResponse]


class ProgramClinicalResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    service: MedicalServiceStaffResponse | None
    is_popular: bool

    is_hidden: bool

    tags: list[ProgramTagResponse]
    stages: list[ProgramStageClinicalResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    hidden_at: datetime | None


class ProgramStartResponse(BaseModel):
    enrollment_id: uuid.UUID
    program_id: uuid.UUID
    status: ProgramEnrollmentStatus
    started_at: datetime


class ProgramPurchaseRequestResponse(BaseModel):
    program_id: uuid.UUID
    requested_at: datetime
    message: str


class PatientProgramAccessItem(BaseModel):
    program_id: uuid.UUID
    title: str

    service: MedicalServiceStaffResponse | None
    is_popular: bool

    is_hidden: bool
    is_active: bool

    purchase_requested: bool
    requested_at: datetime | None
    activated_at: datetime | None

class PatientProgramClinicalResponse(
    ProgramPatientResponse
):
    service: MedicalServiceStaffResponse | None
    is_hidden: bool
    stages: list[ProgramStageClinicalResponse]