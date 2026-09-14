# ./backend/app/modules/programs/consultation_schemas.py

import uuid

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from app.modules.programs.enums import ProgramItemType


class StageConsultationItemRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # У существующего элемента обязательно есть ID.
    # У новой консультации id = null.
    id: uuid.UUID | None = None

    item_type: ProgramItemType

    speciality_id: uuid.UUID | None = None

    consultation_title: str | None = Field(
        default=None,
        max_length=300,
    )

    consultation_description: str | None = Field(
        default=None,
        max_length=50_000,
    )

    @field_validator(
        "consultation_title",
        "consultation_description",
        mode="before",
    )
    @classmethod
    def normalize_optional_text(cls, value):
        if isinstance(value, str):
            return value.strip() or None

        return value

    @model_validator(mode="after")
    def validate_item(self):
        if self.item_type == ProgramItemType.CONSULTATION:
            if self.speciality_id is None:
                raise ValueError(
                    "Для консультации требуется speciality_id"
                )

            return self

        if self.id is None:
            raise ValueError(
                "Статьи и опросники должны иметь существующий ID"
            )

        if (
            self.speciality_id is not None
            or self.consultation_title is not None
            or self.consultation_description is not None
        ):
            raise ValueError(
                "Через этот endpoint нельзя менять "
                "поля статьи или опросника"
            )

        return self


class StageConsultationsUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    expected_revision: str = Field(
        pattern=r"^[0-9a-f]{64}$",
    )

    # Полный порядок элементов этапа.
    # Статьи и опросники передаются только как ID и тип.
    items: list[StageConsultationItemRequest] = Field(
        max_length=1000,
    )


class StageConsultationItemResponse(BaseModel):
    id: uuid.UUID
    item_type: ProgramItemType

    title: str
    is_hidden: bool = False

    speciality_id: uuid.UUID | None = None
    speciality_name: str | None = None

    consultation_title: str | None = None
    consultation_description: str | None = None


class StageConsultationsResponse(BaseModel):
    id: uuid.UUID
    title: str

    revision: str

    items: list[StageConsultationItemResponse]


class ProgramConsultationsResponse(BaseModel):
    id: uuid.UUID
    title: str

    stages: list[StageConsultationsResponse]