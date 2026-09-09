# backend\app\modules\tags\life_aspect_schemas.py

import uuid
from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)

from app.modules.tags.schemas import TagResponse


class LifeAspectCreateRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=50_000,
    )

    order_index: int = Field(
        default=0,
        ge=0,
        le=100_000,
    )

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value):
        if isinstance(value, str):
            return value.strip()

        return value


class LifeAspectUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=50_000,
    )

    order_index: int | None = Field(
        default=None,
        ge=0,
        le=100_000,
    )

    is_hidden: bool | None = None

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value):
        if isinstance(value, str):
            return value.strip()

        return value

    @model_validator(mode="after")
    def reject_null_required_fields(self):
        # Отсутствие поля означает "не изменять".
        # Явный null допустим только для description.
        for field_name in (
            "name",
            "order_index",
            "is_hidden",
        ):
            if (
                field_name in self.model_fields_set
                and getattr(self, field_name) is None
            ):
                raise ValueError(
                    f"Поле {field_name} не может быть null"
                )

        return self


class LifeAspectResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None

    order_index: int

    is_hidden: bool
    hidden_at: datetime | None

    created_at: datetime
    updated_at: datetime

    tags: list[TagResponse]

class LifeAspectProgramResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    is_paid: bool
    is_popular: bool
    is_start: bool
    home_priority: int

    is_recommended: bool

    # Можно ли открыть существующий пациентский
    # endpoint подробного просмотра программы.
    # Это НЕ разрешение на платные материалы.
    can_open_program: bool

    has_program_access: bool


class LifeAspectPatientResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    order_index: int

    programs: list[LifeAspectProgramResponse]