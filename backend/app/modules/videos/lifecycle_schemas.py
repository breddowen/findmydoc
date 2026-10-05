# ./backend/app/modules/videos/lifecycle_schemas.py

import uuid
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class VideoProgramUsage(BaseModel):
    id: uuid.UUID
    title: str
    is_hidden: bool
    item_count: int


class VideoUsageResponse(BaseModel):
    video_id: uuid.UUID
    title: str
    version: int

    program_count: int
    item_count: int
    programs: list[VideoProgramUsage]

    # Снимок связей, которые пользователь подтвердил.
    usage_token: str


class VideoDeleteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    expected_version: int = Field(gt=0)

    expected_usage_token: str = Field(
        min_length=64,
        max_length=64,
        pattern=r"^[0-9a-f]{64}$",
    )

    confirm: Literal[True]


class VideoDeleteResponse(BaseModel):
    video_id: uuid.UUID
    affected_programs: int
    removed_program_items: int
    message: str