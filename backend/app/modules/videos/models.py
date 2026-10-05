# ./backend/app/modules/videos/models.py

import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlmodel import Field, SQLModel

from app.modules.media.models import utc_now_naive


class Video(SQLModel, table=True):
    __tablename__ = "videos"

    __table_args__ = (
        CheckConstraint(
            "wide_file_id IS NOT NULL "
            "OR mobile_file_id IS NOT NULL",
            name="ck_videos_has_file",
        ),
        CheckConstraint(
            "wide_file_id IS NULL "
            "OR mobile_file_id IS NULL "
            "OR wide_file_id <> mobile_file_id",
            name="ck_videos_different_files",
        ),
        CheckConstraint(
            "version > 0",
            name="ck_videos_version",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    title: str = Field(
        max_length=300,
        index=True,
    )

    pro_content: bool = Field(
        default=True,
        index=True,
    )

    is_hidden: bool = Field(
        default=False,
        index=True,
    )

    is_library_hidden: bool = Field(
        default=False,
        index=True,
    )

    wide_file_id: uuid.UUID | None = Field(
        default=None,
        foreign_key="media_video_files.id",
        ondelete="RESTRICT",
        index=True,
    )

    mobile_file_id: uuid.UUID | None = Field(
        default=None,
        foreign_key="media_video_files.id",
        ondelete="RESTRICT",
        index=True,
    )

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        ondelete="RESTRICT",
        index=True,
    )

    # Ручная обложка.
    image_id: uuid.UUID | None = Field(
        default=None,
        foreign_key="media_images.id",
        ondelete="RESTRICT",
        index=True,
    )

    # Сохранённый кадр видео. Не зависит от дальнейшей
    # замены видеофайлов и используется как fallback.
    automatic_image_id: uuid.UUID | None = Field(
        default=None,
        foreign_key="media_images.id",
        ondelete="RESTRICT",
        index=True,
    )

    # Версия всей редактируемой карточки.
    # Не позволяет незаметно перезаписать изменения
    # другого сотрудника.
    version: int = Field(default=1)

    created_at: datetime = Field(
        default_factory=utc_now_naive,
        index=True,
    )

    updated_at: datetime = Field(
        default_factory=utc_now_naive,
    )

    hidden_at: datetime | None = Field(default=None)


class VideoTagLink(SQLModel, table=True):
    __tablename__ = "video_tag_links"

    __table_args__ = (
        UniqueConstraint(
            "video_id",
            "tag_id",
            name="uq_video_tag",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    video_id: uuid.UUID = Field(
        foreign_key="videos.id",
        ondelete="CASCADE",
        index=True,
    )

    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        ondelete="RESTRICT",
        index=True,
    )

class VideoProgress(SQLModel, table=True):
    __tablename__ = "video_progress"

    __table_args__ = (
        UniqueConstraint(
            "video_id",
            "patient_id",
            name="uq_video_patient_progress",
        ),
        CheckConstraint(
            "progress_percent >= 0 AND progress_percent <= 100",
            name="ck_video_progress_percent",
        ),
        CheckConstraint(
            "max_progress_percent >= progress_percent "
            "AND max_progress_percent <= 100",
            name="ck_video_progress_max_percent",
        ),
        CheckConstraint(
            "completion_method IS NULL "
            "OR completion_method IN ('position', 'manual')",
            name="ck_video_progress_completion_method",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    video_id: uuid.UUID = Field(
        foreign_key="videos.id",
        ondelete="CASCADE",
        index=True,
    )

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        ondelete="CASCADE",
        index=True,
    )

    progress_percent: float = Field(default=0.0)
    max_progress_percent: float = Field(default=0.0)

    started_at: datetime = Field(
        default_factory=utc_now_naive,
    )
    updated_at: datetime = Field(
        default_factory=utc_now_naive,
    )

    completed_at: datetime | None = Field(default=None)

    completion_method: str | None = Field(
        default=None,
        max_length=16,
    )