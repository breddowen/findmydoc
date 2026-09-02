# backend\app\modules\services\routers.py

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
from app.core.security import (
    AuthContext,
    require_roles,
)
from app.modules.programs.models import Program
from app.modules.services.models import MedicalService
from app.modules.services.schemas import (
    MedicalServiceCreateRequest,
    MedicalServiceStaffResponse,
    MedicalServiceUpdateRequest,
    MedicalServiceVisibilityRequest,
)
from app.modules.services.utils import (
    clean_optional_text,
    validate_service_pricing,
)
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/services",
    tags=["Services"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def raise_pricing_validation_error(
    *,
    service: MedicalService,
) -> None:
    try:
        validate_service_pricing(
            price_amount=service.price_amount,
            currency=service.currency,
            discount_percent=service.discount_percent,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=(
                status.HTTP_422_UNPROCESSABLE_ENTITY
            ),
            detail=str(error),
        ) from error


@router.get(
    "",
    response_model=list[MedicalServiceStaffResponse],
)
async def list_services(
    include_hidden: bool = Query(default=False),
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> list[MedicalServiceStaffResponse]:
    statement = select(MedicalService)

    if not include_hidden:
        statement = statement.where(
            MedicalService.is_hidden.is_(False)
        )

    services = session.exec(
        statement.order_by(
            MedicalService.code,
            MedicalService.title,
        )
    ).all()

    return [
        MedicalServiceStaffResponse.model_validate(
            service
        )
        for service in services
    ]


@router.get(
    "/{service_id}",
    response_model=MedicalServiceStaffResponse,
)
async def get_service(
    service_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> MedicalServiceStaffResponse:
    service = session.get(
        MedicalService,
        service_id,
    )

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга не найдена",
        )

    return MedicalServiceStaffResponse.model_validate(
        service
    )


@router.post(
    "",
    response_model=MedicalServiceStaffResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_service(
    payload: MedicalServiceCreateRequest,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> MedicalServiceStaffResponse:
    existing = session.exec(
        select(MedicalService).where(
            MedicalService.code == payload.code
        )
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Услуга с таким кодом уже существует"
            ),
        )

    service = MedicalService(
        code=payload.code,
        title=payload.title,
        description=clean_optional_text(
            payload.description
        ),
        price_amount=payload.price_amount,
        currency=payload.currency,
        discount_percent=payload.discount_percent,
        is_hidden=False,
    )

    session.add(service)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Услуга с таким кодом уже существует"
            ),
        ) from error

    session.refresh(service)

    return MedicalServiceStaffResponse.model_validate(
        service
    )


@router.patch(
    "/{service_id}",
    response_model=MedicalServiceStaffResponse,
)
async def update_service(
    service_id: uuid.UUID,
    payload: MedicalServiceUpdateRequest,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> MedicalServiceStaffResponse:
    service = session.get(
        MedicalService,
        service_id,
    )

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга не найдена",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    # Эти поля обязательны в самой модели.
    # PATCH может не передавать их, но не может обнулить.
    for required_field in (
        "code",
        "title",
        "discount_percent",
    ):
        if (
            required_field in update_data
            and update_data[required_field] is None
        ):
            raise HTTPException(
                status_code=(
                    status.HTTP_422_UNPROCESSABLE_ENTITY
                ),
                detail=(
                    f"Поле {required_field} "
                    "не может быть null"
                ),
            )

    for field_name, value in update_data.items():
        if field_name == "description":
            value = clean_optional_text(value)

        setattr(service, field_name, value)

    # Для PATCH проверяем итоговое состояние модели,
    # а не только переданные поля.
    raise_pricing_validation_error(service=service)

    service.updated_at = utc_now()

    session.add(service)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Услуга с таким кодом уже существует "
                "или переданы несогласованные данные"
            ),
        ) from error

    session.refresh(service)

    return MedicalServiceStaffResponse.model_validate(
        service
    )


@router.patch(
    "/{service_id}/visibility",
    response_model=MedicalServiceStaffResponse,
)
async def set_service_visibility(
    service_id: uuid.UUID,
    payload: MedicalServiceVisibilityRequest,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> MedicalServiceStaffResponse:
    service = session.get(
        MedicalService,
        service_id,
    )

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга не найдена",
        )

    now = utc_now()

    service.is_hidden = payload.is_hidden
    service.hidden_at = (
        now if payload.is_hidden else None
    )
    service.updated_at = now

    session.add(service)
    session.commit()
    session.refresh(service)

    return MedicalServiceStaffResponse.model_validate(
        service
    )


@router.delete(
    "/{service_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_service(
    service_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> None:
    service = session.get(
        MedicalService,
        service_id,
    )

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга не найдена",
        )

    linked_program = session.exec(
        select(Program).where(
            Program.service_id == service.id
        )
    ).first()

    if linked_program:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Услуга используется программами. "
                "Вместо удаления скройте её."
            ),
        )

    session.delete(service)
    session.commit()