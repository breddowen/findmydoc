# ./backend/app/modules/specialities/routers.py
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import require_roles
from app.modules.specialities.schemas import (
    SpecialityCreateRequest,
    SpecialityResponse,
    SpecialityUpdateRequest,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import DoctorProfile, Speciality


router = APIRouter(
    prefix="/api/v1/specialities",
    tags=["Specialities"],
)


@router.get("", response_model=list[SpecialityResponse])
async def list_specialities(
    session: Session = Depends(get_session),
) -> list[Speciality]:
    return list(
        session.exec(
            select(Speciality).order_by(Speciality.name)
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
    speciality = session.get(Speciality, speciality_id)

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
    dependencies=[
        Depends(
            require_roles(
                UserRole.SUPERUSER,
                UserRole.MED_ASSISTANT,
            )
        )
    ],
)
async def create_speciality(
    payload: SpecialityCreateRequest,
    session: Session = Depends(get_session),
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
            detail="Специальность с таким названием уже существует",
        )

    speciality = Speciality(
        name=normalized_name,
        description=payload.description,
        consultation_name=payload.consultation_name,
        consultation_description=(
            payload.consultation_description
        ),
    )

    session.add(speciality)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Специальность с таким названием уже существует",
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
    speciality = session.get(Speciality, speciality_id)

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    update_data = payload.model_dump(exclude_unset=True)

    if "name" in update_data:
        update_data["name"] = update_data["name"].strip()

    for field_name, value in update_data.items():
        setattr(speciality, field_name, value)

    session.add(speciality)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Специальность с таким названием уже существует",
        ) from error

    session.refresh(speciality)

    return speciality


@router.delete(
    "/{speciality_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_speciality(
    speciality_id: uuid.UUID,
    session: Session = Depends(get_session),
    _=Depends(require_roles(UserRole.SUPERUSER)),
) -> None:
    speciality = session.get(Speciality, speciality_id)

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    doctor = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.speciality_id == speciality_id
        )
    ).first()

    if doctor:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Нельзя удалить специальность, "
                "пока она назначена хотя бы одному врачу"
            ),
        )

    session.delete(speciality)
    session.commit()