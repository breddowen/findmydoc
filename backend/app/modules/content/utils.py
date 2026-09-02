# ./backend/app/modules/content/utils.py


# Важное выражение для будущей смены логики

# CONTENT_TAG_MATCH_MODE: TagMatchMode = "all"
# Для возврата к OR достаточно изменить его на:
# CONTENT_TAG_MATCH_MODE: TagMatchMode = "any"
# Наследование тегов уже реализовано правильно и динамически, поэтому tags/utils.py не меняем.

import uuid
from typing import Literal

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.tags.utils import (
    get_patient_effective_tag_data,
)
from app.modules.users.models import PatientProfile


TagMatchMode = Literal["all", "any"]


# ВАЖНО: основная стратегия фильтрации контента.
#
# "all" — AND: пациент должен иметь все теги контента.
#         Дополнительные теги пациента не мешают.
#
# "any" — OR: достаточно хотя бы одного общего тега.
#
# Для кастомной логики измените функцию tags_match().
CONTENT_TAG_MATCH_MODE: TagMatchMode = "all"


def get_patient_profile_by_user_id(
    *,
    session: Session,
    user_id: uuid.UUID,
) -> PatientProfile:
    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == user_id
        )
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль пациента не найден",
        )

    return patient


def get_patient_effective_tag_ids(
    *,
    session: Session,
    patient: PatientProfile,
) -> set[uuid.UUID]:
    tag_data = get_patient_effective_tag_data(
        session=session,
        patient=patient,
    )

    return set(tag_data.keys())


def tags_match(
    *,
    patient_tag_ids: set[uuid.UUID],
    content_tag_ids: set[uuid.UUID],
    mode: TagMatchMode = CONTENT_TAG_MATCH_MODE,
) -> bool:
    """
    Централизованное правило сопоставления тегов.

    Контент без тегов является общим независимо
    от выбранного режима.
    """
    if not content_tag_ids:
        return True

    if mode == "all":
        # Нестрогий AND:
        # все теги контента должны быть у пациента,
        # но у пациента могут быть дополнительные теги.
        return content_tag_ids.issubset(
            patient_tag_ids
        )

    if mode == "any":
        # OR: достаточно одного совпавшего тега.
        return bool(
            patient_tag_ids.intersection(
                content_tag_ids
            )
        )

    raise ValueError(
        f"Неизвестный режим фильтрации тегов: {mode}"
    )


def patient_can_see_content(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    is_hidden: bool,
) -> bool:
    if is_hidden:
        return False

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    return tags_match(
        patient_tag_ids=patient_tag_ids,
        content_tag_ids=content_tag_ids,
    )


def patient_can_access_content(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    pro_content: bool,
    is_hidden: bool,
) -> bool:
    if not patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=content_tag_ids,
        is_hidden=is_hidden,
    ):
        return False

    if pro_content and not patient.pro_enabled:
        return False

    return True


def ensure_patient_content_access(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    pro_content: bool,
    is_hidden: bool,
) -> None:
    if not patient_can_access_content(
        session=session,
        patient=patient,
        content_tag_ids=content_tag_ids,
        pro_content=pro_content,
        is_hidden=is_hidden,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Контент недоступен пациенту",
        )