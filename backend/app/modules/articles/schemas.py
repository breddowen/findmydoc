# ./backend/app/modules/articles/schemas.py
import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ArticleCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    content: str = Field(min_length=1)

    tag_ids: list[uuid.UUID] = []

    pro_content: bool = True


class ArticleUpdateRequest(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )
    content: str | None = Field(default=None, min_length=1)

    tag_ids: list[uuid.UUID] | None = None
    pro_content: bool | None = None


class ArticleVisibilityRequest(BaseModel):
    is_hidden: bool


class ArticleTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class ArticleResponse(BaseModel):
    id: uuid.UUID

    title: str
    content: str

    pro_content: bool
    is_hidden: bool

    tags: list[ArticleTagResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    hidden_at: datetime | None


class ArticleListItem(BaseModel):
    id: uuid.UUID
    title: str

    pro_content: bool
    is_hidden: bool
    can_access: bool = True

    tags: list[ArticleTagResponse]

    created_at: datetime
    updated_at: datetime

    # Возвращаются только администраторам и медассистентам.
    opened_count: int | None = None
    read_count: int | None = None
    read_rate: float | None = None

class ArticleReadResponse(BaseModel):
    message: str
    event_id: uuid.UUID

class ArticleProgressUpdateRequest(BaseModel):
    progress_percent: float = Field(
        ge=0,
        le=100,
    )


class ArticleProgressResponse(BaseModel):
    article_id: uuid.UUID
    patient_id: uuid.UUID

    progress_percent: float
    max_progress_percent: float

    started_at: datetime
    updated_at: datetime
    completed_at: datetime | None

ArticleOpenSource = Literal[
    "library",
    "program",
    "assignment",
    "direct",
]


class ArticleOpenRequest(BaseModel):
    interaction_id: uuid.UUID

    source: ArticleOpenSource = "direct"

    program_id: uuid.UUID | None = None
    assignment_id: uuid.UUID | None = None


class ArticleOpenResponse(BaseModel):
    event_id: uuid.UUID
    interaction_id: uuid.UUID


class ArticleProgressUpdateRequest(BaseModel):
    progress_percent: float = Field(
        ge=0,
        le=100,
    )

    # Если параметры не переданы, прогресс сохранится,
    # но аналитическое событие не создастся.
    interaction_id: uuid.UUID | None = None
    is_trackable: bool = False