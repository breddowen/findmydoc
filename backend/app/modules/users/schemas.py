# ./backend/app/modules/users/schemas.py
import uuid
from datetime import date, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
)

from app.modules.users.enums import Gender, UserRole


class RoleResponse(BaseModel):
    role: UserRole
    is_primary: bool


class SpecialityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None


class DoctorProfileResponse(BaseModel):
    id: uuid.UUID
    speciality: SpecialityResponse


class PatientProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    record_id: str
    fullname: str | None
    dob: date | None
    pro_enabled: bool


class RelativeProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID


class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr

    first_name: str | None
    last_name: str | None
    middle_name: str | None
    gender: Gender | None

    is_active: bool
    is_blocked: bool
    is_email_verified: bool
    deleted_at: datetime | None

    roles: list[RoleResponse]
    active_role: UserRole | None = None

    doctor_profile: DoctorProfileResponse | None = None
    patient_profile: PatientProfileResponse | None = None
    relative_profile: RelativeProfileResponse | None = None

    created_at: datetime
    updated_at: datetime


class UserUpdateRequest(BaseModel):
    first_name: str | None = Field(
        default=None,
        max_length=100,
    )
    last_name: str | None = Field(
        default=None,
        max_length=100,
    )
    middle_name: str | None = Field(
        default=None,
        max_length=100,
    )
    gender: Gender | None = None

    # Используется только для пациента.
    dob: date | None = None

    @field_validator(
        "first_name",
        "last_name",
        "middle_name",
        mode="before",
    )
    @classmethod
    def normalize_name(
        cls,
        value,
    ):
        if value is None:
            return None

        normalized = str(value).strip()
        return normalized or None

    @field_validator("dob")
    @classmethod
    def validate_dob(
        cls,
        value: date | None,
    ) -> date | None:
        if value and value > date.today():
            raise ValueError(
                "Дата рождения не может быть в будущем"
            )

        return value


class AdminUserListItem(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    roles: list[UserRole]
    is_active: bool
    is_blocked: bool
    is_email_verified: bool
    deleted_at: datetime | None
    created_at: datetime


class AdminBlockRequest(BaseModel):
    is_blocked: bool

class AdminUserPageResponse(BaseModel):
    items: list[AdminUserListItem]

    page: int
    page_size: int
    total_items: int
    total_pages: int