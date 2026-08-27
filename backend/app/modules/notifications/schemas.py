# ./backend/app/modules/notifications/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel

from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)


class NotificationResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID

    notification_type: NotificationType

    title: str
    message: str
    action_url: str | None

    payload: dict[str, Any]
    channels: list[NotificationChannel]

    is_read: bool
    created_at: datetime
    read_at: datetime | None


class NotificationPageResponse(BaseModel):
    items: list[NotificationResponse]

    page: int
    page_size: int
    total_items: int
    total_pages: int
    unread_count: int


class UnreadCountResponse(BaseModel):
    unread_count: int


class MarkAllReadResponse(BaseModel):
    updated_count: int