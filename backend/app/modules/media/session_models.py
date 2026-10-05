# ./backend/app/modules/media/session_models.py

import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from app.modules.media.models import utc_now_naive


class MediaPlaybackSession(SQLModel, table=True):
    __tablename__ = "media_playback_sessions"

    # В БД хранится только SHA-256 от случайного секрета.
    # Сам секрет находится в HttpOnly-cookie браузера.
    token_hash: str = Field(
        primary_key=True,
        max_length=64,
    )

    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        ondelete="CASCADE",
        index=True,
    )

    active_role: str = Field(max_length=32)
    auth_version: int

    created_at: datetime = Field(
        default_factory=utc_now_naive,
    )

    expires_at: datetime = Field(index=True)