# backend\app\modules\media\models.py

import uuid
from datetime import datetime, timezone

from sqlalchemy import CheckConstraint
from sqlmodel import Field, SQLModel


def utc_now_naive() -> datetime:
    # В этой таблице храним UTC без timezone,
    # одинаково для SQLite и PostgreSQL.
    return datetime.now(timezone.utc).replace(
        tzinfo=None,
    )


class MediaImage(SQLModel, table=True):
    __tablename__ = "media_images"

    __table_args__ = (
        CheckConstraint(
            "width > 0 AND height > 0",
            name="ck_media_images_dimensions",
        ),
        CheckConstraint(
            "size_bytes > 0",
            name="ck_media_images_size",
        ),
        CheckConstraint(
            "purpose IN ("
            "'doctor', "
            "'article', "
            "'questionnaire', "
            "'program', "
            "'life_aspect'"
            ")",
            name="ck_media_images_purpose",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    # Строка, а не PostgreSQL ENUM:
    # проще расширять и поддерживать SQLite.
    purpose: str = Field(max_length=32)

    uploaded_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    width: int
    height: int
    size_bytes: int

    is_attached: bool = Field(
        default=False,
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now_naive,
        index=True,
    )