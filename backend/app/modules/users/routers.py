# ./backend/app/modules/users/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, get_current_auth, require_roles
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    PatientProfile,
    User,
    UserRoleLink,
)
from app.modules.users.schemas import (
    AdminBlockRequest,
    AdminUserListItem,
    AdminUserPageResponse,
    UserResponse,
    UserUpdateRequest,
)
from app.modules.users.utils import (
    build_user_response,
    get_user_roles,
)


router = APIRouter(prefix="/api/v1/users", tags=["Users"])


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@router.get("/me", response_model=UserResponse)
async def get_me(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> UserResponse:
    return build_user_response(
        session=session,
        user=auth.user,
        active_role=auth.active_role,
    )


@router.patch("/me", response_model=UserResponse)
async def update_me(
    payload: UserUpdateRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> UserResponse:
    update_data = payload.model_dump(
        exclude_unset=True
    )

    dob_was_provided = "dob" in update_data
    dob = update_data.pop("dob", None)

    for field_name, value in update_data.items():
        setattr(auth.user, field_name, value)

    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == auth.user.id
        )
    ).first()

    if dob_was_provided:
        if not patient:
            raise HTTPException(
                status_code=(
                    status.HTTP_422_UNPROCESSABLE_ENTITY
                ),
                detail=(
                    "Дата рождения доступна "
                    "только для пациента"
                ),
            )

        patient.dob = dob

    name_fields = {
        "first_name",
        "last_name",
        "middle_name",
    }

    if patient and name_fields.intersection(
        update_data
    ):
        # PatientProfile.fullname пока остаётся
        # в модели, поэтому синхронизируем его
        # со структурированным ФИО пользователя.
        patient.fullname = (
            " ".join(
                part
                for part in [
                    auth.user.last_name,
                    auth.user.first_name,
                    auth.user.middle_name,
                ]
                if part
            )
            or None
        )
        patient.updated_at = utc_now()
        session.add(patient)

    auth.user.updated_at = utc_now()

    session.add(auth.user)
    session.commit()
    session.refresh(auth.user)

    return build_user_response(
        session=session,
        user=auth.user,
        active_role=auth.active_role,
    )


@router.get(
    "",
    response_model=AdminUserPageResponse,
    dependencies=[
        Depends(
            require_roles(
                UserRole.SUPERUSER,
                UserRole.MED_ASSISTANT,
            )
        )
    ],
)
async def list_users(
    search: str | None = Query(
        default=None,
        max_length=200,
    ),
    role: UserRole | None = Query(default=None),
    include_deleted: bool = False,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    session: Session = Depends(get_session),
) -> AdminUserPageResponse:
    filters = []

    if not include_deleted:
        filters.append(User.deleted_at.is_(None))

    if search:
        normalized_search = search.strip().lower()

        if normalized_search:
            filters.append(
                User.email.contains(normalized_search)
            )

    count_statement = select(
        func.count(func.distinct(User.id))
    ).select_from(User)

    users_statement = select(User)

    if role is not None:
        count_statement = count_statement.join(
            UserRoleLink,
            UserRoleLink.user_id == User.id,
        ).where(
            UserRoleLink.role == role,
        )

        users_statement = users_statement.join(
            UserRoleLink,
            UserRoleLink.user_id == User.id,
        ).where(
            UserRoleLink.role == role,
        )

    if filters:
        count_statement = count_statement.where(*filters)
        users_statement = users_statement.where(*filters)

    total_items = session.exec(
        count_statement
    ).one()

    total_pages = max(
        1,
        (total_items + page_size - 1) // page_size,
    )

    normalized_page = min(page, total_pages)

    users = session.exec(
        users_statement
        .distinct()
        .order_by(User.created_at.desc())
        .offset((normalized_page - 1) * page_size)
        .limit(page_size)
    ).all()

    items: list[AdminUserListItem] = []

    for user in users:
        roles = [
            role_link.role
            for role_link in get_user_roles(
                session,
                user.id,
            )
        ]

        full_name = " ".join(
            part
            for part in [
                user.last_name,
                user.first_name,
                user.middle_name,
            ]
            if part
        ) or user.email

        items.append(
            AdminUserListItem(
                id=user.id,
                email=user.email,
                full_name=full_name,
                roles=roles,
                is_active=user.is_active,
                is_blocked=user.is_blocked,
                is_email_verified=(
                    user.email_verified_at is not None
                ),
                deleted_at=user.deleted_at,
                created_at=user.created_at,
            )
        )

    return AdminUserPageResponse(
        items=items,
        page=normalized_page,
        page_size=page_size,
        total_items=total_items,
        total_pages=total_pages,
    )


@router.patch(
    "/{user_id}/block",
    response_model=AdminUserListItem,
)
async def block_or_unblock_user(
    user_id: uuid.UUID,
    payload: AdminBlockRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> AdminUserListItem:
    target_user = session.get(User, user_id)

    if not target_user or target_user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )

    if target_user.id == auth.user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Нельзя заблокировать собственный аккаунт",
        )

    target_roles = [
        role_link.role
        for role_link in get_user_roles(session, target_user.id)
    ]

    if (
        UserRole.SUPERUSER in target_roles
        and auth.active_role != UserRole.SUPERUSER
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ассистент не может блокировать суперпользователя",
        )

    target_user.is_blocked = payload.is_blocked
    target_user.auth_version += 1
    target_user.updated_at = utc_now()

    session.add(target_user)
    session.commit()
    session.refresh(target_user)

    full_name = " ".join(
        part
        for part in [
            target_user.last_name,
            target_user.first_name,
            target_user.middle_name,
        ]
        if part
    ) or target_user.email

    return AdminUserListItem(
        id=target_user.id,
        email=target_user.email,
        full_name=full_name,
        roles=target_roles,
        is_active=target_user.is_active,
        is_blocked=target_user.is_blocked,
        is_email_verified=target_user.email_verified_at is not None,
        deleted_at=target_user.deleted_at,
        created_at=target_user.created_at,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.SUPERUSER)
    ),
    session: Session = Depends(get_session),
) -> None:
    target_user = session.get(User, user_id)

    if not target_user or target_user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )

    if target_user.id == auth.user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Нельзя удалить собственный аккаунт",
        )

    target_user.deleted_at = utc_now()
    target_user.is_active = False
    target_user.auth_version += 1
    target_user.updated_at = utc_now()

    session.add(target_user)
    session.commit()