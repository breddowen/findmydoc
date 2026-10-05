# ./backend/app/modules/media/video_models.py

import uuid

from sqlalchemy import BigInteger, CheckConstraint, Column
from sqlmodel import Field, SQLModel

from app.modules.media.models import utc_now_naive
from datetime import datetime


class MediaVideoFile(SQLModel, table=True):
    __tablename__ = "media_video_files"

    __table_args__ = (
        CheckConstraint(
            "width > 0 AND height > 0",
            name="ck_media_video_files_dimensions",
        ),
        CheckConstraint(
            "size_bytes > 0",
            name="ck_media_video_files_size",
        ),
        CheckConstraint(
            "duration_seconds > 0",
            name="ck_media_video_files_duration",
        ),
        CheckConstraint(
            "fps > 0",
            name="ck_media_video_files_fps",
        ),
        CheckConstraint(
            "rotation_degrees IN (0, 90, 180, 270)",
            name="ck_media_video_files_rotation",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    uploaded_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        ondelete="RESTRICT",
        index=True,
    )

    # Размер отображаемого кадра с учётом rotation metadata.
    width: int
    height: int

    rotation_degrees: int = Field(default=0)

    duration_seconds: float
    fps: float
    size_bytes: int = Field(
        sa_column=Column(
            BigInteger(),
            nullable=False,
        ),
    )

    has_audio: bool = Field(default=False)

    # После привязки файл нельзя повторно забрать
    # из временных загрузок в другую карточку.
    is_attached: bool = Field(
        default=False,
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now_naive,
        index=True,
    )

    # Файл раньше использовался, но был заменён/отвязан.
    # is_attached остаётся True: повторно присвоить такой
    # файл через временные загрузки нельзя.
    retired_at: datetime | None = Field(
        default=None,
        index=True,
    )