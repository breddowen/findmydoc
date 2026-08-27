# ./backend/app/modules/invitations/schemas.py
import uuid
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field

from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.users.enums import Gender


class DoctorInvitationCreateRequest(BaseModel):
    email: EmailStr

    first_name: str | None = Field(default=None, max_length=100)
    last_name: str | None = Field(default=None, max_length=100)
    middle_name: str | None = Field(default=None, max_length=100)

    speciality_id: uuid.UUID


class PatientInvitationPrepareRequest(BaseModel):
    record_id: str = Field(min_length=1, max_length=100)
    email: EmailStr

    fullname: str | None = Field(default=None, max_length=300)
    dob: date | None = None
    gender: Gender | None = None

    confirm_existing: bool = False

class RelativeInvitationCreateRequest(BaseModel):
    email: EmailStr

    # Пациент при активной роли patient может не передавать patient_id.
    # Врач обязан передать ID профиля пациента.
    patient_id: uuid.UUID | None = None

    relationship_degree: str | None = Field(
        default=None,
        max_length=100,
    )

class ExistingPatientConfirmation(BaseModel):
    status: Literal["confirmation_required"]
    message: str

    patient_id: uuid.UUID
    record_id: str

    email_matches: bool
    already_linked: bool


class ExistingPatientAttachedResponse(BaseModel):
    status: Literal["patient_attached"]
    message: str

    patient_id: uuid.UUID
    record_id: str


class InvitationCreatedResponse(BaseModel):
    status: Literal["invitation_created"]
    invitation_id: uuid.UUID
    invitation_type: InvitationType

    email: EmailStr
    expires_at: datetime
    registration_url: str


class InvitationPreviewResponse(BaseModel):
    invitation_id: uuid.UUID
    invitation_type: InvitationType
    status: InvitationStatus

    email: EmailStr

    first_name: str | None
    last_name: str | None
    middle_name: str | None
    fullname: str | None

    gender: Gender | None
    dob: date | None

    record_id: str | None

    speciality_id: uuid.UUID | None
    speciality_name: str | None

    relationship_degree: str | None

    expires_at: datetime
    is_existing_account: bool


class InvitationAcceptRequest(BaseModel):
    token: str

    # Для нового аккаунта это новый пароль.
    # Для существующего аккаунта — текущий пароль.
    password: str = Field(min_length=1, max_length=128)
    password_confirmation: str = Field(min_length=1, max_length=128)

    first_name: str | None = Field(default=None, max_length=100)
    last_name: str | None = Field(default=None, max_length=100)
    middle_name: str | None = Field(default=None, max_length=100)
    fullname: str | None = Field(default=None, max_length=300)

    gender: Gender | None = None
    dob: date | None = None

    # Врач может изменить предложенную специальность.
    speciality_id: uuid.UUID | None = None


class InvitationAcceptResponse(BaseModel):
    message: str
    user_id: uuid.UUID
    role_added: str
    email_verification_required: bool


class InvitationListItem(BaseModel):
    id: uuid.UUID
    invitation_type: InvitationType
    status: InvitationStatus

    email: EmailStr
    record_id: str | None

    created_at: datetime
    expires_at: datetime
    accepted_at: datetime | None


class MessageResponse(BaseModel):
    message: str