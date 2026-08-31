# ./backend/app/modules/tags/routers.py
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
    get_current_auth,
    require_roles,
)
from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.tags.models import (
    DoctorTagOverride,
    SpecialityTagLink,
    Tag,
)
from app.modules.tags.schemas import (
    DoctorTagOverrideRequest,
    DoctorTagOverrideResponse,
    EffectiveTagsResponse,
    MessageResponse,
    SpecialityTagResponse,
    TagCreateRequest,
    TagResponse,
    TagUpdateRequest,
    TagVisibilityRequest,
)
from app.modules.tags.utils import (
    get_doctor_effective_tag_data,
    get_patient_effective_tag_data,
    get_relative_effective_tag_data,
    serialize_effective_tags,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    DoctorProfile,
    PatientProfile,
    RelativeProfile,
    Speciality,
)

from app.modules.articles.models import ArticleTagLink
from app.modules.programs.models import ProgramTagLink
from app.modules.questionnaires.models import (
    QuestionnaireTagLink,
)


router = APIRouter(
    prefix="/api/v1/tags",
    tags=["Tags"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_current_doctor_profile(
    *,
    session: Session,
    auth: AuthContext,
) -> DoctorProfile:
    doctor = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == auth.user.id
        )
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль врача не найден",
        )

    return doctor


def serialize_override(
    *,
    session: Session,
    override: DoctorTagOverride,
) -> DoctorTagOverrideResponse:
    tag = session.get(Tag, override.tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Тег индивидуальной настройки не найден",
        )

    return DoctorTagOverrideResponse(
        id=override.id,
        doctor_id=override.doctor_id,
        tag=TagResponse.model_validate(tag),
        action=override.action,
        created_at=override.created_at,
        updated_at=override.updated_at,
    )


@router.get("", response_model=list[TagResponse])
async def list_tags(
    include_hidden: bool = Query(default=False),
    _: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[Tag]:
    statement = select(Tag)

    if not include_hidden:
        statement = statement.where(
            Tag.is_hidden.is_(False)
        )

    return list(
        session.exec(
            statement.order_by(Tag.name)
        ).all()
    )


@router.post(
    "",
    response_model=TagResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_tag(
    payload: TagCreateRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> Tag:
    normalized_name = payload.name.strip().lower()

    existing = session.exec(
        select(Tag).where(Tag.name == normalized_name)
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Тег с таким названием уже существует",
        )

    tag = Tag(
        name=normalized_name,
        description=payload.description,
        is_system=False,
    )

    session.add(tag)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Тег с таким названием уже существует",
        ) from error

    session.refresh(tag)

    return tag


@router.patch(
    "/{tag_id}",
    response_model=TagResponse,
)
async def update_tag(
    tag_id: uuid.UUID,
    payload: TagUpdateRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> Tag:
    tag = session.get(Tag, tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не найден",
        )

    update_data = payload.model_dump(exclude_unset=True)

    if "name" in update_data:
        if tag.is_system:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Название системного тега изменять нельзя",
            )

        update_data["name"] = update_data["name"].strip().lower()

    for field_name, value in update_data.items():
        setattr(tag, field_name, value)

    tag.updated_at = utc_now()

    session.add(tag)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Тег с таким названием уже существует",
        ) from error

    session.refresh(tag)

    return tag


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_tag(
    tag_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> None:
    tag = session.get(Tag, tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не найден",
        )

    if tag.is_system:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Системный тег нельзя удалить. "
                "При необходимости его можно скрыть."
            ),
        )

    usage_checks = [
        (
            SpecialityTagLink,
            SpecialityTagLink.tag_id,
            "специальностями",
        ),
        (
            DoctorTagOverride,
            DoctorTagOverride.tag_id,
            "настройками врачей",
        ),
        (
            ArticleTagLink,
            ArticleTagLink.tag_id,
            "статьями",
        ),
        (
            ProgramTagLink,
            ProgramTagLink.tag_id,
            "программами",
        ),
        (
            QuestionnaireTagLink,
            QuestionnaireTagLink.tag_id,
            "опросниками",
        ),
    ]

    for model, field, usage_name in usage_checks:
        usage = session.exec(
            select(model).where(field == tag.id)
        ).first()

        if usage:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Тег используется {usage_name}. "
                    "Вместо удаления скройте его."
                ),
            )

    session.delete(tag)
    session.commit()

@router.patch(
    "/{tag_id}/visibility",
    response_model=TagResponse,
)
async def set_tag_visibility(
    tag_id: uuid.UUID,
    payload: TagVisibilityRequest,
    _: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> Tag:
    tag = session.get(Tag, tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не найден",
        )

    now = utc_now()

    tag.is_hidden = payload.is_hidden
    tag.hidden_at = now if payload.is_hidden else None
    tag.updated_at = now

    session.add(tag)
    session.commit()
    session.refresh(tag)

    return tag

@router.get(
    "/specialities/{speciality_id}",
    response_model=SpecialityTagResponse,
)
async def get_speciality_tags(
    speciality_id: uuid.UUID,
    _: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> SpecialityTagResponse:
    speciality = session.get(
        Speciality,
        speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    links = session.exec(
        select(SpecialityTagLink).where(
            SpecialityTagLink.speciality_id == speciality.id
        )
    ).all()

    tags: list[Tag] = []

    for link in links:
        tag = session.get(Tag, link.tag_id)

        if tag:
            tags.append(tag)

    tags.sort(key=lambda item: item.name.lower())

    return SpecialityTagResponse(
        speciality_id=speciality.id,
        speciality_name=speciality.name,
        tags=[
            TagResponse.model_validate(tag)
            for tag in tags
        ],
    )


@router.post(
    "/specialities/{speciality_id}/{tag_id}",
    response_model=MessageResponse,
)
async def add_tag_to_speciality(
    speciality_id: uuid.UUID,
    tag_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    speciality = session.get(
        Speciality,
        speciality_id,
    )
    tag = session.get(Tag, tag_id)

    if not speciality:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Специальность не найдена",
        )

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не найден",
        )

    existing = session.exec(
        select(SpecialityTagLink).where(
            SpecialityTagLink.speciality_id == speciality.id,
            SpecialityTagLink.tag_id == tag.id,
        )
    ).first()

    if existing:
        return MessageResponse(
            message="Тег уже назначен специальности"
        )

    if tag.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Скрытый тег нельзя назначить специальности",
        )

    session.add(
        SpecialityTagLink(
            speciality_id=speciality.id,
            tag_id=tag.id,
        )
    )
    session.commit()

    return MessageResponse(
        message="Тег добавлен к специальности"
    )


@router.delete(
    "/specialities/{speciality_id}/{tag_id}",
    response_model=MessageResponse,
)
async def remove_tag_from_speciality(
    speciality_id: uuid.UUID,
    tag_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    link = session.exec(
        select(SpecialityTagLink).where(
            SpecialityTagLink.speciality_id == speciality_id,
            SpecialityTagLink.tag_id == tag_id,
        )
    ).first()

    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не назначен этой специальности",
        )

    session.delete(link)
    session.commit()

    return MessageResponse(
        message="Тег удалён из специальности"
    )


@router.get(
    "/doctors/me/overrides",
    response_model=list[DoctorTagOverrideResponse],
)
async def list_my_doctor_tag_overrides(
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> list[DoctorTagOverrideResponse]:
    doctor = get_current_doctor_profile(
        session=session,
        auth=auth,
    )

    overrides = session.exec(
        select(DoctorTagOverride)
        .where(DoctorTagOverride.doctor_id == doctor.id)
        .order_by(DoctorTagOverride.created_at)
    ).all()

    return [
        serialize_override(
            session=session,
            override=override,
        )
        for override in overrides
    ]


@router.put(
    "/doctors/me/overrides",
    response_model=DoctorTagOverrideResponse,
)
async def set_my_doctor_tag_override(
    payload: DoctorTagOverrideRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> DoctorTagOverrideResponse:
    doctor = get_current_doctor_profile(
        session=session,
        auth=auth,
    )

    tag = session.get(Tag, payload.tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Тег не найден",
        )

    if tag.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Скрытый тег нельзя использовать",
        )

    if tag.is_system:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Системный тег нельзя изменять вручную",
        )

    override = session.exec(
        select(DoctorTagOverride).where(
            DoctorTagOverride.doctor_id == doctor.id,
            DoctorTagOverride.tag_id == tag.id,
        )
    ).first()

    now = utc_now()

    if override:
        override.action = payload.action
        override.updated_at = now
    else:
        override = DoctorTagOverride(
            doctor_id=doctor.id,
            tag_id=tag.id,
            action=payload.action,
        )

    session.add(override)
    session.commit()
    session.refresh(override)

    return serialize_override(
        session=session,
        override=override,
    )


@router.delete(
    "/doctors/me/overrides/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def reset_my_doctor_tag_override(
    tag_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> None:
    doctor = get_current_doctor_profile(
        session=session,
        auth=auth,
    )

    override = session.exec(
        select(DoctorTagOverride).where(
            DoctorTagOverride.doctor_id == doctor.id,
            DoctorTagOverride.tag_id == tag_id,
        )
    ).first()

    if not override:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Индивидуальная настройка тега не найдена",
        )

    session.delete(override)
    session.commit()


@router.get(
    "/me/effective",
    response_model=EffectiveTagsResponse,
)
async def get_my_effective_tags(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EffectiveTagsResponse:
    if auth.active_role == UserRole.DOCTOR:
        doctor = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == auth.user.id
            )
        ).first()

        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Профиль врача не найден",
            )

        data = get_doctor_effective_tag_data(
            session=session,
            doctor=doctor,
        )

        return serialize_effective_tags(
            owner_type="doctor",
            owner_id=doctor.id,
            tag_data=data,
        )

    if auth.active_role == UserRole.PATIENT:
        patient = session.exec(
            select(PatientProfile).where(
                PatientProfile.user_id == auth.user.id
            )
        ).first()

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Профиль пациента не найден",
            )

        data = get_patient_effective_tag_data(
            session=session,
            patient=patient,
        )

        return serialize_effective_tags(
            owner_type="patient",
            owner_id=patient.id,
            tag_data=data,
        )

    if auth.active_role == UserRole.RELATIVE:
        relative = session.exec(
            select(RelativeProfile).where(
                RelativeProfile.user_id == auth.user.id
            )
        ).first()

        if not relative:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Профиль родственника не найден",
            )

        data = get_relative_effective_tag_data(
            session=session,
            relative=relative,
        )

        return serialize_effective_tags(
            owner_type="relative",
            owner_id=relative.id,
            tag_data=data,
        )

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Для активной роли эффективные теги не предусмотрены",
    )