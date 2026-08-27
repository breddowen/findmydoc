# ./backend/app/modules/notifications/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, Relationship, SQLModel

from app.modules.notifications.enums import (
    NotificationType,
)
from app.modules.users.models import User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    notification_type: NotificationType = Field(
        default=NotificationType.GENERAL,
        index=True,
    )

    title: str = Field(max_length=300)
    message: str

    action_url: Optional[str] = Field(
        default=None,
        max_length=1000,
    )

    payload_json: dict = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )

    channels_json: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON, nullable=False),
    )

    is_read: bool = Field(default=False, index=True)

    created_at: datetime = Field(
        default_factory=utc_now,
        index=True,
    )
    read_at: Optional[datetime] = Field(default=None)

    user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Notification.user_id]",
        }
    )