# ./backend/app/modules/specialities/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SpecialityCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = None

    consultation_name: str | None = Field(
        default=None,
        max_length=300,
    )
    consultation_description: str | None = None


class SpecialityUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )
    description: str | None = None

    consultation_name: str | None = Field(
        default=None,
        max_length=300,
    )
    consultation_description: str | None = None


class SpecialityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None

    consultation_name: str | None
    consultation_description: str | None

    created_at: datetime