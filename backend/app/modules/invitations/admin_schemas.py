# ./backend/app/modules/invitations/admin_schemas.py
import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field, field_validator

from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.users.enums import UserRole


class AdminInvitationCreateRequest(BaseModel):
    role: UserRole
    email: EmailStr

    record_id: str | None = Field(
        default=None,
        max_length=100,
    )
    speciality_id: uuid.UUID | None = None

    @field_validator("record_id")
    @classmethod
    def normalize_record_id(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized = value.strip().upper()
        return normalized or None


class AdminInvitationCreator(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str


class AdminInvitationListItem(BaseModel):
    id: uuid.UUID
    invitation_type: InvitationType
    status: InvitationStatus

    email: EmailStr
    record_id: str | None

    speciality_id: uuid.UUID | None
    speciality_name: str | None

    creator: AdminInvitationCreator

    created_at: datetime
    expires_at: datetime
    accepted_at: datetime | None
    revoked_at: datetime | None

    email_sent_at: datetime | None
    email_send_error: str | None

    can_revoke: bool
    can_resend: bool


class AdminInvitationCreatedResponse(BaseModel):
    status: Literal["invitation_created"]
    invitation_id: uuid.UUID
    invitation_type: InvitationType

    email: EmailStr
    expires_at: datetime
    registration_url: str

    email_sent_at: datetime | None = None
    email_send_error: str | None = None


class AdminInvitationEmailResponse(
    AdminInvitationCreatedResponse
):
    status: Literal["invitation_created"] = "invitation_created"

class AdminInvitationPageResponse(BaseModel):
    items: list[AdminInvitationListItem]

    page: int
    page_size: int
    total_items: int
    total_pages: int