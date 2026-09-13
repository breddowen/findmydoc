# backend\app\modules\media\image_routers.py

import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import update
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import AuthContext, get_current_auth
from app.modules.media.access import (
    ensure_can_manage_entity_image,
    ensure_can_view_entity_image,
    get_image_entity,
)
from app.modules.media.constants import ImagePurpose
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.schemas import (
    EntityImageResponse,
    EntityImageUpdateRequest,
)
from app.modules.media.service import set_entity_image
from app.modules.media.storage import image_path


router = APIRouter(
    prefix="/api/v1/media/images",
    tags=["Media: entity images"],
)


def serialize_entity_image(
    *,
    session: Session,
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    entity,
) -> EntityImageResponse:
    image = (
        session.get(MediaImage, entity.image_id)
        if entity.image_id is not None
        else None
    )

    if entity.image_id is not None and image is None:
        raise HTTPException(
            status_code=409,
            detail="Нарушена связь с изображением",
        )

    return EntityImageResponse(
        purpose=purpose,
        entity_id=entity_id,
        image_id=image.id if image else None,
        width=image.width if image else None,
        height=image.height if image else None,
        size_bytes=image.size_bytes if image else None,
        file_path=(
            f"/api/v1/media/images/{purpose}/{entity_id}/file"
            f"?image_id={image.id}"
            if image is not None
            else None
        ),
    )


@router.get(
    "/{purpose}/{entity_id}",
    response_model=EntityImageResponse,
)
def get_entity_image(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EntityImageResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_view_entity_image(
        session=session,
        auth=auth,
        purpose=purpose,
        entity=entity,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    return serialize_entity_image(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
        entity=entity,
    )


@router.patch(
    "/{purpose}/{entity_id}",
    response_model=EntityImageResponse,
)
def update_entity_image(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    payload: EntityImageUpdateRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EntityImageResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_manage_entity_image(
        auth=auth,
        purpose=purpose,
        entity=entity,
    )

    try:
        # Блокируем изменение этой сущности.
        #
        # UPDATE вместо SELECT FOR UPDATE:
        # работает и в PostgreSQL, и в SQLite.
        model = type(entity)

        session.execute(
            update(model)
            .where(model.id == entity.id)
            .values(image_id=model.image_id)
            .execution_options(synchronize_session=False)
        )

        session.refresh(entity)

        # Повторяем проверку на актуальных данных.
        ensure_can_manage_entity_image(
            auth=auth,
            purpose=purpose,
            entity=entity,
        )

        if entity.image_id != payload.expected_image_id:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Изображение уже изменено другим запросом. "
                    "Обновите данные и повторите действие."
                ),
            )

        if entity.image_id != payload.image_id:
            set_entity_image(
                session=session,
                entity=entity,
                purpose=purpose,
                image_id=payload.image_id,
                uploaded_by_user_id=auth.user.id,
            )

            if hasattr(entity, "updated_at"):
                entity.updated_at = utc_now_naive()

            session.add(entity)

        session.commit()
        session.refresh(entity)

    except Exception:
        session.rollback()
        raise

    return serialize_entity_image(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
        entity=entity,
    )


@router.get(
    "/{purpose}/{entity_id}/file",
    response_class=FileResponse,
)
def get_entity_image_file(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    image_id: uuid.UUID | None = None,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> FileResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_view_entity_image(
        session=session,
        auth=auth,
        purpose=purpose,
        entity=entity,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    if entity.image_id is None:
        raise HTTPException(
            status_code=404,
            detail="Изображение не добавлено",
        )

    # Если frontend запросил старую версию картинки,
    # не подменяем её молча новой.
    if (
        image_id is not None
        and image_id != entity.image_id
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение уже изменено",
        )

    image = session.get(
        MediaImage,
        entity.image_id,
    )

    if (
        image is None
        or image.purpose != purpose
        or not image.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение не найдено",
        )

    path = image_path(image.id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл изображения не найден",
        )

    return FileResponse(
        path=path,
        media_type="image/webp",
        headers={
            "Cache-Control": "private, no-store",
            "Vary": "Authorization",
            "X-Content-Type-Options": "nosniff",
            "Content-Disposition": "inline",
        },
    )