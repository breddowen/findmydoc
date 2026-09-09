# ./backend/app/modules/consents/contact_schemas.py
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ContactRequestCreateRequest(BaseModel):
    accepted: Literal[True]

    document_version: str = Field(
        min_length=1,
        max_length=50,
    )


class ContactRequestResponse(BaseModel):
    requested_at: datetime
    already_requested: bool
    message: str