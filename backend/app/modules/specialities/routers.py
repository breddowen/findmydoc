# ./backend/app/modules/specialities/routers.py
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
from app.modules.invitations.models import Invitation
from app.modules.programs.models import ProgramStageItem
from app.modules.referrals.models import Referral
from app.modules.specialities.schemas import (
    SpecialityCreateRequest,
    SpecialityResponse,
    SpecialityUpdateRequest,
    SpecialityVisibilityRequest,
)
from app.modules.tags.models import SpecialityTagLink
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    DoctorProfile,
    Speciality,
)


router = APIRouter(
    prefix="/api/v1/specialities",
    tags=["Specialities"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def clean_optional_text(
    value: str | None,
) -> str | None:
    if value is None:
        return None

    normalized = value.strip()
    return normalized or None


@router.get("", response_model=list[SpecialityResponse])
async def list_specialities(
    include_hidden: bool = Query(default=False),
    session: Session = Depends(get_session),
) -> list[Speciality]:
    statement = select(Speciality)

    if not include_hidden:
        statement = statement.where(
            Speciality.is_hidden.is_(False)
        )

    return list(
        session.exec(
            statement.order_by(Speciality.name)
        ).all()
    )


@router.get(
    "/{speciality_id}",
    response_model=SpecialityResponse,
)
async def get_speciality(
    speciality_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> Speciality:
    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    return speciality


@router.post(
    "",
    response_model=SpecialityResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_speciality(
    payload: SpecialityCreateRequest,
    session: Session = Depends(get_session),
    _=Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
) -> Speciality:
    normalized_name = payload.name.strip()

    existing = session.exec(
        select(Speciality).where(
            Speciality.name == normalized_name
        )
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Специальность с таким названием "
                "уже существует"
            ),
        )

    speciality = Speciality(
        name=normalized_name,
        description=clean_optional_text(
            payload.description
        ),
        consultation_name=clean_optional_text(
            payload.consultation_name
        ),
        consultation_description=clean_optional_text(
            payload.consultation_description
        ),
        is_hidden=False,
    )

    session.add(speciality)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Специальность с таким названием "
                "уже существует"
            ),
        ) from error

    session.refresh(speciality)
    return speciality


@router.patch(
    "/{speciality_id}",
    response_model=SpecialityResponse,
)
async def update_speciality(
    speciality_id: uuid.UUID,
    payload: SpecialityUpdateRequest,
    session: Session = Depends(get_session),
    _=Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
) -> Speciality:
    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for field_name, value in update_data.items():
        if field_name == "name":
            value = value.strip()

            if not value:
                raise HTTPException(
                    status_code=(
                        status.HTTP_422_UNPROCESSABLE_ENTITY
                    ),
                    detail=(
                        "Название специальности "
                        "не может быть пустым"
                    ),
                )
        else:
            value = clean_optional_text(value)

        setattr(speciality, field_name, value)

    session.add(speciality)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Специальность с таким названием "
                "уже существует"
            ),
        ) from error

    session.refresh(speciality)
    return speciality


@router.patch(
    "/{speciality_id}/visibility",
    response_model=SpecialityResponse,
)
async def set_speciality_visibility(
    speciality_id: uuid.UUID,
    payload: SpecialityVisibilityRequest,
    session: Session = Depends(get_session),
    _=Depends(
        require_roles(UserRole.SUPERUSER)
    ),
) -> Speciality:
    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    speciality.is_hidden = payload.is_hidden
    speciality.hidden_at = (
        utc_now() if payload.is_hidden else None
    )

    session.add(speciality)
    session.commit()
    session.refresh(speciality)

    return speciality


@router.delete(
    "/{speciality_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_speciality(
    speciality_id: uuid.UUID,
    session: Session = Depends(get_session),
    _=Depends(
        require_roles(UserRole.SUPERUSER)
    ),
) -> None:
    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    usage_checks = [
        (
            DoctorProfile,
            DoctorProfile.speciality_id,
            "врачами",
        ),
        (
            ProgramStageItem,
            ProgramStageItem.speciality_id,
            "программами",
        ),
        (
            Invitation,
            Invitation.speciality_id,
            "приглашениями",
        ),
        (
            Referral,
            Referral.speciality_id,
            "направлениями",
        ),
        (
            SpecialityTagLink,
            SpecialityTagLink.speciality_id,
            "назначенными тегами",
        ),
    ]

    for model, field, usage_name in usage_checks:
        usage = session.exec(
            select(model).where(
                field == speciality.id
            )
        ).first()

        if usage:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Специальность используется "
                    f"{usage_name}. Вместо удаления "
                    "скройте её."
                ),
            )

    session.delete(speciality)
    session.commit()