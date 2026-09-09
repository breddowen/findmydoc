# backend\app\modules\tags\life_aspect_routers.py

import uuid
from datetime import datetime, timezone

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import require_roles
from app.modules.tags.life_aspect_schemas import (
    LifeAspectCreateRequest,
    LifeAspectResponse,
    LifeAspectUpdateRequest,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.tags.schemas import TagResponse
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/life-aspects/manage",
    tags=["Life aspects: management"],
    dependencies=[
        Depends(
            require_roles(
                UserRole.SUPERUSER,
                UserRole.MED_ASSISTANT,
            )
        ),
    ],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_aspect(
    *,
    session: Session,
    aspect_id: uuid.UUID,
) -> LifeAspect:
    aspect = session.get(LifeAspect, aspect_id)

    if aspect is None:
        raise HTTPException(
            status_code=404,
            detail="Сфера жизни не найдена",
        )

    return aspect


def serialize_aspects(
    *,
    session: Session,
    aspects: list[LifeAspect],
) -> list[LifeAspectResponse]:
    if not aspects:
        return []

    tags_by_aspect: dict[
        uuid.UUID,
        list[TagResponse],
    ] = {
        aspect.id: []
        for aspect in aspects
    }

    # Загружаем связи всех выбранных сфер одним запросом.
    rows = session.exec(
        select(
            LifeAspectTagLink.life_aspect_id,
            Tag,
        )
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id.in_(
                list(tags_by_aspect)
            )
        )
        .order_by(Tag.name, Tag.id)
    ).all()

    for aspect_id, tag in rows:
        tags_by_aspect[aspect_id].append(
            TagResponse.model_validate(tag)
        )

    return [
        LifeAspectResponse(
            id=aspect.id,
            name=aspect.name,
            description=aspect.description,
            order_index=aspect.order_index,
            is_hidden=aspect.is_hidden,
            hidden_at=aspect.hidden_at,
            created_at=aspect.created_at,
            updated_at=aspect.updated_at,
            tags=tags_by_aspect[aspect.id],
        )
        for aspect in aspects
    ]


def serialize_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> LifeAspectResponse:
    return serialize_aspects(
        session=session,
        aspects=[aspect],
    )[0]


def save_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> None:
    session.add(aspect)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=409,
            detail=(
                "Не удалось сохранить сферу жизни: "
                "конфликт данных. Проверьте, нет ли "
                "сферы с таким же названием."
            ),
        ) from error

    session.refresh(aspect)


@router.get(
    "",
    response_model=list[LifeAspectResponse],
)
async def list_life_aspects(
    include_hidden: bool = Query(default=False),
    session: Session = Depends(get_session),
) -> list[LifeAspectResponse]:
    statement = select(LifeAspect)

    if not include_hidden:
        statement = statement.where(
            LifeAspect.is_hidden.is_(False)
        )

    aspects = session.exec(
        statement.order_by(
            LifeAspect.order_index,
            LifeAspect.name,
            LifeAspect.id,
        )
    ).all()

    return serialize_aspects(
        session=session,
        aspects=list(aspects),
    )


@router.post(
    "",
    response_model=LifeAspectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_life_aspect(
    payload: LifeAspectCreateRequest,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = LifeAspect(
        name=payload.name,
        description=payload.description,
        order_index=payload.order_index,
    )

    save_aspect(
        session=session,
        aspect=aspect,
    )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.patch(
    "/{aspect_id}",
    response_model=LifeAspectResponse,
)
async def update_life_aspect(
    aspect_id: uuid.UUID,
    payload: LifeAspectUpdateRequest,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    changes = payload.model_dump(exclude_unset=True)

    if not changes:
        return serialize_aspect(
            session=session,
            aspect=aspect,
        )

    now = utc_now()

    if "is_hidden" in changes:
        next_is_hidden = changes.pop("is_hidden")

        if next_is_hidden != aspect.is_hidden:
            aspect.is_hidden = next_is_hidden
            aspect.hidden_at = (
                now if next_is_hidden else None
            )

    for field_name, value in changes.items():
        setattr(aspect, field_name, value)

    aspect.updated_at = now

    save_aspect(
        session=session,
        aspect=aspect,
    )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.put(
    "/{aspect_id}/tags/{tag_id}",
    response_model=LifeAspectResponse,
)
async def add_life_aspect_tag(
    aspect_id: uuid.UUID,
    tag_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    tag = session.get(Tag, tag_id)

    if tag is None:
        raise HTTPException(
            status_code=404,
            detail="Тег не найден",
        )

    if tag.is_hidden:
        raise HTTPException(
            status_code=409,
            detail=(
                "Скрытый тег нельзя добавить. "
                "Сначала восстановите его в справочнике."
            ),
        )

    statement = select(LifeAspectTagLink).where(
        LifeAspectTagLink.life_aspect_id == aspect.id,
        LifeAspectTagLink.tag_id == tag.id,
    )

    existing = session.exec(statement).first()

    if existing is None:
        session.add(
            LifeAspectTagLink(
                life_aspect_id=aspect.id,
                tag_id=tag.id,
            )
        )

        aspect.updated_at = utc_now()
        session.add(aspect)

        try:
            session.commit()
        except IntegrityError:
            session.rollback()

            # Параллельное повторное добавление той же
            # связи считаем успешной идемпотентной операцией.
            existing = session.exec(statement).first()

            if existing is None:
                raise

        aspect = get_aspect(
            session=session,
            aspect_id=aspect_id,
        )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.delete(
    "/{aspect_id}/tags/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_life_aspect_tag(
    aspect_id: uuid.UUID,
    tag_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> None:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    link = session.exec(
        select(LifeAspectTagLink).where(
            LifeAspectTagLink.life_aspect_id == aspect.id,
            LifeAspectTagLink.tag_id == tag_id,
        )
    ).first()

    if link is None:
        return

    session.delete(link)

    aspect.updated_at = utc_now()
    session.add(aspect)

    session.commit()