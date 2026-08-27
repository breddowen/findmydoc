# ./backend/app/modules/referrals/schemas.py
import uuid
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field

from app.modules.referrals.enums import (
    ReferralSource,
    ReferralStatus,
)
from app.modules.users.enums import Gender


class ReferralCreateRequest(BaseModel):
    record_id: str = Field(min_length=1, max_length=100)
    email: EmailStr

    fullname: str | None = Field(
        default=None,
        max_length=300,
    )
    dob: date | None = None
    gender: Gender | None = None

    confirm_existing: bool = False


class ReferralConfirmationRequiredResponse(BaseModel):
    status: Literal["confirmation_required"]
    message: str

    patient_id: uuid.UUID
    record_id: str
    email_matches: bool
    already_linked: bool


class ReferralCreatedResponse(BaseModel):
    status: Literal["referral_created"]

    referral_id: uuid.UUID
    referral_status: ReferralStatus
    source: ReferralSource

    patient_id: uuid.UUID | None
    invitation_id: uuid.UUID | None

    registration_url: str
    created_at: datetime


class ReferralResolveResponse(BaseModel):
    referral_id: uuid.UUID
    status: ReferralStatus
    source: ReferralSource

    requires_registration: bool
    patient_id: uuid.UUID | None

    invitation_type: str | None
    record_id: str


class ReferralSourceUpdateRequest(BaseModel):
    source: ReferralSource


class ReferralListItem(BaseModel):
    id: uuid.UUID
    status: ReferralStatus
    source: ReferralSource

    patient_id: uuid.UUID | None
    invitation_id: uuid.UUID | None

    record_id: str
    speciality_name: str

    created_at: datetime
    link_sent_at: datetime | None
    opened_at: datetime | None
    registered_at: datetime | None