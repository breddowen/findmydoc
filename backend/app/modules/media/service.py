# backend\app\modules\media\service.py

import uuid
from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy import update
from sqlmodel import Session

from app.core.config import settings
from app.modules.media.constants import ImagePurpose
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.storage import image_path
from app.modules.questionnaires.models import Questionnaire


def ensure_image_file_exists(image_id: uuid.UUID) -> None:
    if not image_path(image_id).is_file():
        raise HTTPException(
            status_code=409,
            detail=(
                "Файл изображения отсутствует. "
                "Загрузите изображение повторно."
            ),
        )


def set_entity_image(
    *,
    session: Session,
    entity,
    purpose: ImagePurpose,
    image_id: uuid.UUID | None,
    uploaded_by_user_id: uuid.UUID,
) -> None:
    current_image_id = entity.image_id

    # Сохранение формы без изменения изображения.
    if image_id == current_image_id:
        return

    # Только отвязываем. Сам файл здесь не удаляем.
    if image_id is None:
        entity.image_id = None
        session.add(entity)
        return

    ensure_image_file_exists(image_id)

    oldest_allowed = utc_now_naive() - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    # Атомарно забираем временную загрузку.
    #
    # Если два запроса одновременно пытаются использовать
    # один upload, успешно завершится только один.
    result = session.execute(
        update(MediaImage)
        .where(
            MediaImage.id == image_id,
            MediaImage.purpose == purpose,
            MediaImage.uploaded_by_user_id == uploaded_by_user_id,
            MediaImage.is_attached.is_(False),
            MediaImage.created_at > oldest_allowed,
        )
        .values(is_attached=True)
        .execution_options(synchronize_session=False)
    )

    if result.rowcount != 1:
        raise HTTPException(
            status_code=409,
            detail=(
                "Изображение нельзя использовать: "
                "оно принадлежит другому пользователю, "
                "имеет другое назначение, уже использовано "
                "или срок загрузки истёк. "
                "Загрузите изображение повторно."
            ),
        )

    entity.image_id = image_id
    session.add(entity)


def set_questionnaire_creation_image(
    *,
    session: Session,
    questionnaire: Questionnaire,
    requested_image_id: uuid.UUID | None,
    image_was_provided: bool,
    copied_from_id: uuid.UUID | None,
    uploaded_by_user_id: uuid.UUID,
) -> None:
    source = None

    if copied_from_id is not None:
        source = session.get(
            Questionnaire,
            copied_from_id,
        )

        if source is None:
            raise HTTPException(
                status_code=404,
                detail="Исходный опросник не найден",
            )

    # Старый клиент при копировании может не отправлять
    # image_id. В этом случае наследуем обложку.
    if not image_was_provided:
        requested_image_id = (
            source.image_id if source is not None else None
        )

    # Явный null означает копирование без обложки.
    if requested_image_id is None:
        return

    # Разрешаем совместное использование изображения
    # только через явно указанный исходный опросник.
    if (
        source is not None
        and source.image_id == requested_image_id
    ):
        image = session.get(
            MediaImage,
            requested_image_id,
        )

        if (
            image is None
            or image.purpose != "questionnaire"
            or not image.is_attached
        ):
            raise HTTPException(
                status_code=409,
                detail="Обложка исходного опросника недоступна",
            )

        ensure_image_file_exists(image.id)

        questionnaire.image_id = image.id
        session.add(questionnaire)
        return

    # Пользователь выбрал новую обложку вместо исходной.
    set_entity_image(
        session=session,
        entity=questionnaire,
        purpose="questionnaire",
        image_id=requested_image_id,
        uploaded_by_user_id=uploaded_by_user_id,
    )