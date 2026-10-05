# ./backend/app/modules/videos/schemas.py

import uuid
from datetime import datetime
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)


class VideoFileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID

    width: int
    height: int
    rotation_degrees: int

    duration_seconds: float
    fps: float
    size_bytes: int

    has_audio: bool


class VideoUploadResponse(VideoFileResponse):
    created_at: datetime
    expires_at: datetime

    suggested_slot: Literal["wide", "mobile"]


class VideoUploadLimitsResponse(BaseModel):
    max_bytes: int
    max_duration_seconds: float
    max_long_side: int
    max_short_side: int
    max_fps: float


class VideoWriteRequest(BaseModel):
    # Опечатки в именах полей не игнорируем.
    model_config = ConfigDict(extra="forbid")

    title: str = Field(
        min_length=1,
        max_length=300,
    )

    tag_ids: list[uuid.UUID] = Field(
        default_factory=list,
        max_length=100,
    )

    pro_content: bool = True
    is_library_hidden: bool = False

    wide_file_id: uuid.UUID | None = None
    mobile_file_id: uuid.UUID | None = None

    image_id: uuid.UUID | None = None

    @field_validator("title")
    @classmethod
    def normalize_title(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Введите название видео")

        return value

    @field_validator("tag_ids")
    @classmethod
    def normalize_tags(
        cls,
        value: list[uuid.UUID],
    ) -> list[uuid.UUID]:
        return list(dict.fromkeys(value))

    @model_validator(mode="after")
    def validate_files(self):
        if (
            self.wide_file_id is None
            and self.mobile_file_id is None
        ):
            raise ValueError(
                "Добавьте хотя бы один видеофайл"
            )

        if (
            self.wide_file_id is not None
            and self.wide_file_id == self.mobile_file_id
        ):
            raise ValueError(
                "Один файл нельзя одновременно "
                "назначить обоим вариантам"
            )

        return self


class VideoCreateRequest(VideoWriteRequest):
    pass


class VideoUpdateRequest(VideoWriteRequest):
    # PUT передаёт полное содержимое формы.
    expected_version: int = Field(gt=0)


class VideoVisibilityRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_hidden: bool
    expected_version: int = Field(gt=0)


class VideoTagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None


class VideoResponse(BaseModel):
    id: uuid.UUID
    title: str

    pro_content: bool
    is_hidden: bool
    is_library_hidden: bool

    wide_file: VideoFileResponse | None
    mobile_file: VideoFileResponse | None

    tags: list[VideoTagResponse]

    version: int

    created_by_user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    hidden_at: datetime | None

    # Ручная обложка.
    image_id: uuid.UUID | None = None

    # Сохранённый автоматический кадр.
    automatic_image_id: uuid.UUID | None = None

    # Какая обложка фактически показывается.
    poster_image_id: uuid.UUID | None = None

    # Предупреждение конкретной операции сохранения.
    # Само видео при этом сохранено.
    poster_warning: str | None = None

class VideoAutomaticPosterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    expected_version: int = Field(gt=0)

class VideoCatalogItem(VideoResponse):
    can_access: bool