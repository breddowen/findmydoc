# ./backend/app/modules/articles/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Article(SQLModel, table=True):
    __tablename__ = "articles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str = Field(index=True, max_length=300)
    content: str

    pro_content: bool = Field(default=True, index=True)
    is_hidden: bool = Field(default=False, index=True)

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    tag_links: list["ArticleTagLink"] = Relationship(
        back_populates="article",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class ArticleTagLink(SQLModel, table=True):
    __tablename__ = "article_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "article_id",
            "tag_id",
            name="uq_article_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    article_id: uuid.UUID = Field(
        foreign_key="articles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    article: Optional[Article] = Relationship(
        back_populates="tag_links",
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleTagLink.article_id]",
        },
    )

    tag: Optional[Tag] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleTagLink.tag_id]",
        }
    )

class ArticleProgress(SQLModel, table=True):
    __tablename__ = "article_progress"
    __table_args__ = (
        UniqueConstraint(
            "article_id",
            "patient_id",
            name="uq_article_patient_progress",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    article_id: uuid.UUID = Field(
        foreign_key="articles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    # Текущая сохранённая позиция.
    progress_percent: float = Field(default=0.0)

    # Максимально достигнутый прогресс.
    max_progress_percent: float = Field(default=0.0)

    started_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)

    article: Optional[Article] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleProgress.article_id]",
        }
    )