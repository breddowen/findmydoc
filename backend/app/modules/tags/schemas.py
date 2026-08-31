# ./backend/app/modules/tags/schemas.py
import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.modules.tags.enums import DoctorTagOverrideAction


class TagCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class TagUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    description: str | None = None


class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None
    is_system: bool
    created_at: datetime
    updated_at: datetime


class SpecialityTagResponse(BaseModel):
    speciality_id: uuid.UUID
    speciality_name: str
    tags: list[TagResponse]


class DoctorTagOverrideRequest(BaseModel):
    tag_id: uuid.UUID
    action: DoctorTagOverrideAction


class DoctorTagOverrideResponse(BaseModel):
    id: uuid.UUID
    doctor_id: uuid.UUID
    tag: TagResponse
    action: DoctorTagOverrideAction
    created_at: datetime
    updated_at: datetime


class EffectiveTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    is_system: bool

    # default, custom, doctor, patient или system.
    sources: list[str]


class EffectiveTagsResponse(BaseModel):
    owner_type: Literal["doctor", "patient", "relative"]
    owner_id: uuid.UUID
    tags: list[EffectiveTagResponse]


class MessageResponse(BaseModel):
    message: str

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None

    is_system: bool
    is_hidden: bool
    hidden_at: datetime | None

    created_at: datetime
    updated_at: datetime


class TagVisibilityRequest(BaseModel):
    is_hidden: bool