# ./backend/app/modules/consents/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel

from app.modules.consents.enums import ConsentType


class ConsentDocumentResponse(BaseModel):
    consent_type: ConsentType
    title: str
    description: str
    version: str


class ConsentSetRequest(BaseModel):
    consent_type: ConsentType
    accepted: bool


class ConsentRecordResponse(BaseModel):
    id: uuid.UUID
    consent_type: ConsentType
    accepted: bool
    document_version: str
    created_at: datetime


class ContactPreferenceResponse(BaseModel):
    allow_assistant_contact: bool
    do_not_call: bool
    updated_at: datetime | None


class MyConsentsResponse(BaseModel):
    consents: list[ConsentRecordResponse]
    contact_preference: ContactPreferenceResponse