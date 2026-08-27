# ./backend/app/modules/events/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from app.modules.events.enums import EventType


class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    event_type: EventType

    patient_id: uuid.UUID | None
    actor_user_id: uuid.UUID | None
    referral_id: uuid.UUID | None
    doctor_id: uuid.UUID | None
    speciality_id: uuid.UUID | None

    product_id: uuid.UUID | None
    program_id: uuid.UUID | None

    subject_type: str | None
    subject_id: uuid.UUID | None

    metadata_json: dict[str, Any]

    occurred_at: datetime
    created_at: datetime