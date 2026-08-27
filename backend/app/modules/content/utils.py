# ./backend/app/modules/content/utils.py
import uuid

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.tags.utils import (
    get_patient_effective_tag_data,
)
from app.modules.users.models import PatientProfile


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

def patient_can_see_content(
    *,
    session: Session,
    patient: PatientProfile,
    content_tag_ids: set[uuid.UUID],
    is_hidden: bool,
) -> bool:
    if is_hidden:
        return False

    # Контент без тегов считается общим.
    if not content_tag_ids:
        return True

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    return bool(
        patient_tag_ids.intersection(content_tag_ids)
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