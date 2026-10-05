# ./backend/app/modules/videos/progress_schemas.py

import uuid
from datetime import datetime
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
)


class VideoProgressResponse(BaseModel):
    video_id: uuid.UUID

    progress_percent: float
    max_progress_percent: float

    started_at: datetime | None
    updated_at: datetime | None
    completed_at: datetime | None

    completion_method: str | None


class VideoOpenRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    interaction_id: uuid.UUID

    source: Literal["library", "program", "direct"] = "direct"

    program_id: uuid.UUID | None = None
    program_stage_id: uuid.UUID | None = None

    @model_validator(mode="after")
    def validate_context(self):
        if self.program_stage_id and not self.program_id:
            raise ValueError(
                "Для этапа необходимо указать программу"
            )

        if self.source == "program" and not self.program_id:
            raise ValueError(
                "Для источника program требуется program_id"
            )

        return self


class VideoOpenResponse(BaseModel):
    interaction_id: uuid.UUID
    event_id: uuid.UUID
    progress: VideoProgressResponse


class VideoProgressUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    interaction_id: uuid.UUID

    action: Literal[
        "started",
        "progress",
        "complete",
    ]

    progress_percent: float | None = Field(
        default=None,
        ge=0,
        le=100,
        allow_inf_nan=False,
    )

    @model_validator(mode="after")
    def validate_action(self):
        if self.action == "progress":
            if self.progress_percent is None:
                raise ValueError(
                    "Для progress требуется progress_percent"
                )
        elif self.progress_percent is not None:
            raise ValueError(
                "Процент передаётся только для действия progress"
            )

        return self