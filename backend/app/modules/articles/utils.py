# ./backend/app/modules/articles/utils.py
import uuid

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.articles.models import (
    Article,
    ArticleTagLink,
)
from app.modules.articles.schemas import (
    ArticleListItem,
    ArticleResponse,
    ArticleTagResponse,
)
from app.modules.tags.models import Tag


def get_article_tag_ids(
    *,
    session: Session,
    article_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_article_tags(
    *,
    session: Session,
    article_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article_id
        )
    ).all()

    tags: list[Tag] = []

    for link in links:
        tag = session.get(Tag, link.tag_id)

        if tag:
            tags.append(tag)

    return sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )


def validate_tag_ids(
    *,
    session: Session,
    tag_ids: list[uuid.UUID],
) -> list[Tag]:
    unique_tag_ids = list(dict.fromkeys(tag_ids))
    tags: list[Tag] = []

    for tag_id in unique_tag_ids:
        tag = session.get(Tag, tag_id)

        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Тег {tag_id} не найден",
            )

        tags.append(tag)

    return tags


def replace_article_tags(
    *,
    session: Session,
    article: Article,
    tag_ids: list[uuid.UUID],
) -> None:
    unique_tag_ids = list(
        dict.fromkeys(tag_ids)
    )

    validate_tag_ids(
        session=session,
        tag_ids=unique_tag_ids,
    )

    old_links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article.id
        )
    ).all()

    old_by_tag_id = {
        link.tag_id: link
        for link in old_links
    }

    old_tag_ids = set(old_by_tag_id)
    new_tag_ids = set(unique_tag_ids)

    # Удаляем только те связи, которых
    # больше нет в payload.
    for tag_id in old_tag_ids - new_tag_ids:
        session.delete(
            old_by_tag_id[tag_id]
        )

    # Добавляем только действительно новые.
    for tag_id in new_tag_ids - old_tag_ids:
        session.add(
            ArticleTagLink(
                article_id=article.id,
                tag_id=tag_id,
            )
        )


def serialize_article(
    *,
    session: Session,
    article: Article,
) -> ArticleResponse:
    tags = get_article_tags(
        session=session,
        article_id=article.id,
    )

    return ArticleResponse(
        id=article.id,
        title=article.title,
        content=article.content,
        pro_content=article.pro_content,
        is_hidden=article.is_hidden,
        tags=[
            ArticleTagResponse(
                id=tag.id,
                name=tag.name,
                description=tag.description,
            )
            for tag in tags
        ],
        created_by_user_id=article.created_by_user_id,
        created_at=article.created_at,
        updated_at=article.updated_at,
        hidden_at=article.hidden_at,
    )


def serialize_article_list_item(
    *,
    session: Session,
    article: Article,
    can_access: bool = True,
) -> ArticleListItem:
    full_response = serialize_article(
        session=session,
        article=article,
    )

    return ArticleListItem(
        id=full_response.id,
        title=full_response.title,
        pro_content=full_response.pro_content,
        is_hidden=full_response.is_hidden,
        can_access=can_access,
        tags=full_response.tags,
        created_at=full_response.created_at,
        updated_at=full_response.updated_at,
    )