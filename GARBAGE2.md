У меня такой проект:

# Project Structure

> Generated: 2026-08-31 20:47

---

## AI Backend

```
backend/alembic/env.py
backend/alembic/README
backend/alembic/script.py.mako
backend/alembic/versions/4a9d77a6cc23_initial_schema.py
backend/app/.env
backend/app/__init__.py
backend/app/core/__init__.py
backend/app/core/config.py
backend/app/core/db.py
backend/app/core/email.py
backend/app/core/security.py
backend/app/core/websockets/__init__.py
backend/app/core/websockets/manager.py
backend/app/main.py
backend/app/modules/__init__.py
backend/app/modules/articles/__init__.py
backend/app/modules/articles/models.py
backend/app/modules/articles/routers.py
backend/app/modules/articles/schemas.py
backend/app/modules/articles/utils.py
backend/app/modules/assignments/__init__.py
backend/app/modules/assignments/enums.py
backend/app/modules/assignments/models.py
backend/app/modules/assignments/routers.py
backend/app/modules/assignments/schemas.py
backend/app/modules/assignments/utils.py
backend/app/modules/auth/__init__.py
backend/app/modules/auth/models.py
backend/app/modules/auth/routers.py
backend/app/modules/auth/schemas.py
backend/app/modules/auth/utils.py
backend/app/modules/consents/__init__.py
backend/app/modules/consents/enums.py
backend/app/modules/consents/models.py
backend/app/modules/consents/routers.py
backend/app/modules/consents/schemas.py
backend/app/modules/consents/utils.py
backend/app/modules/content/__init__.py
backend/app/modules/content/utils.py
backend/app/modules/events/__init__.py
backend/app/modules/events/enums.py
backend/app/modules/events/models.py
backend/app/modules/events/routers.py
backend/app/modules/events/schemas.py
backend/app/modules/events/service.py
backend/app/modules/invitations/__init__.py
backend/app/modules/invitations/enums.py
backend/app/modules/invitations/models.py
backend/app/modules/invitations/routers.py
backend/app/modules/invitations/schemas.py
backend/app/modules/invitations/utils.py
backend/app/modules/notifications/__init__.py
backend/app/modules/notifications/enums.py
backend/app/modules/notifications/models.py
backend/app/modules/notifications/routers.py
backend/app/modules/notifications/schemas.py
backend/app/modules/notifications/service.py
backend/app/modules/patients/__init__.py
backend/app/modules/patients/enums.py
backend/app/modules/patients/routers.py
backend/app/modules/patients/schemas.py
backend/app/modules/patients/utils.py
backend/app/modules/programs/__init__.py
backend/app/modules/programs/enums.py
backend/app/modules/programs/models.py
backend/app/modules/programs/Readme.md
backend/app/modules/programs/routers.py
backend/app/modules/programs/schemas.py
backend/app/modules/programs/utils.py
backend/app/modules/questionnaires/__init__.py
backend/app/modules/questionnaires/enums.py
backend/app/modules/questionnaires/json_q/audit.json
backend/app/modules/questionnaires/models.py
backend/app/modules/questionnaires/Readme.md
backend/app/modules/questionnaires/routers.py
backend/app/modules/questionnaires/schemas.py
backend/app/modules/questionnaires/utils.py
backend/app/modules/referrals/__init__.py
backend/app/modules/referrals/enums.py
backend/app/modules/referrals/models.py
backend/app/modules/referrals/routers.py
backend/app/modules/referrals/schemas.py
backend/app/modules/referrals/utils.py
backend/app/modules/relationships/__init__.py
backend/app/modules/relationships/routers.py
backend/app/modules/relationships/schemas.py
backend/app/modules/specialities/__init__.py
backend/app/modules/specialities/routers.py
backend/app/modules/specialities/schemas.py
backend/app/modules/tags/__init__.py
backend/app/modules/tags/enums.py
backend/app/modules/tags/models.py
backend/app/modules/tags/routers.py
backend/app/modules/tags/schemas.py
backend/app/modules/tags/utils.py
backend/app/modules/users/__init__.py
backend/app/modules/users/enums.py
backend/app/modules/users/models.py
backend/app/modules/users/routers.py
backend/app/modules/users/schemas.py
backend/app/modules/users/utils.py
backend/requirements.txt
backend/seed/create_superuser.py
backend/seed/data/tags.json
backend/seed/data/users.json
backend/seed/Readme.md
backend/seed/upload_tags.py
backend/seed/upload_users.py
backend/test_database.db
```

*Files: 109*

---

## Frontend

### components

```
frontend/app/components/articles/Form.vue
frontend/app/components/articles/PatientOverview.vue
frontend/app/components/articles/Reader.vue
frontend/app/components/assignments/ContentPicker.vue
frontend/app/components/assignments/CreateDialog.vue
frontend/app/components/assignments/PatientList.vue
frontend/app/components/assignments/PickerItem.vue
frontend/app/components/auth/RoleSelector.vue
frontend/app/components/consents/AssistantContact.vue
frontend/app/components/content/RichTextEditor.vue
frontend/app/components/content/RichTextRenderer.vue
frontend/app/components/content/TagSelector.vue
frontend/app/components/invitations/LinkDialog.vue
frontend/app/components/layout/EmailVerificationBanner.vue
frontend/app/components/layout/Footer.vue
frontend/app/components/layout/Navbar.vue
frontend/app/components/layout/ThemeToggle.vue
frontend/app/components/notifications/Center.vue
frontend/app/components/patients/ContactStatus.vue
frontend/app/components/patients/Item.vue
frontend/app/components/patients/List.vue
frontend/app/components/patients/ProAccess.vue
frontend/app/components/programs/configurator/Editor.vue
frontend/app/components/programs/configurator/Item.vue
frontend/app/components/programs/configurator/Library.vue
frontend/app/components/programs/configurator/Stage.vue
frontend/app/components/programs/PatientAccess.vue
frontend/app/components/programs/PatientOverview.vue
frontend/app/components/programs/PatientProgress.vue
frontend/app/components/programs/viewer/Stage.vue
frontend/app/components/programs/VisibilityDialog.vue
frontend/app/components/questionnaires/Editor.vue
frontend/app/components/questionnaires/JsonImporter.vue
frontend/app/components/questionnaires/QuestionField.vue
frontend/app/components/questionnaires/QuestionItem.vue
frontend/app/components/ui/BottomSheet.vue
frontend/app/components/ui/ContentSkeleton.vue
frontend/app/components/ui/Modal.vue
frontend/app/components/ui/Pagination.vue
frontend/app/components/ui/ResponsiveDialog.vue
```
*Files: 40*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue
frontend/app/pages/content/articles/[id]/index.vue
frontend/app/pages/content/articles/index.vue
frontend/app/pages/content/articles/new.vue
frontend/app/pages/content/questionnaires/[id].vue
frontend/app/pages/content/questionnaires/index.vue
frontend/app/pages/content/questionnaires/new.vue
frontend/app/pages/dashboard.vue
frontend/app/pages/forgot-password.vue
frontend/app/pages/index.vue
frontend/app/pages/login.vue
frontend/app/pages/patients/[id]/index.vue
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue
frontend/app/pages/patients/index.vue
frontend/app/pages/programs/[id]/edit.vue
frontend/app/pages/programs/[id]/index.vue
frontend/app/pages/programs/index.vue
frontend/app/pages/programs/new.vue
frontend/app/pages/questionnaires/[id].vue
frontend/app/pages/questionnaires/index.vue
frontend/app/pages/reset-password.vue
frontend/app/pages/settings/security.vue
frontend/app/pages/verify-email.vue
```
*Files: 23*

### layouts

```
frontend/app/layouts/auth.vue
frontend/app/layouts/default.vue
```
*Files: 2*

### composables

```
frontend/app/composables/useBodyScrollLock.js
frontend/app/composables/useBreakpoint.js
frontend/app/composables/useClientReady.js
frontend/app/composables/useProgramPrice.js
frontend/app/composables/useReadingProgress.js
frontend/app/composables/useWebAuthn.js
```
*Files: 6*

### stores

```
frontend/app/stores/articles.js
frontend/app/stores/assignments.js
frontend/app/stores/auth.js
frontend/app/stores/notifications.js
frontend/app/stores/patients.js
frontend/app/stores/programs.js
frontend/app/stores/questionnaires.js
frontend/app/stores/ui.js
frontend/app/stores/user.js
```
*Files: 9*

### middleware

```
frontend/app/middleware/auth.global.js
frontend/app/middleware/program-manager.js
```
*Files: 2*

### plugins

```
frontend/app/plugins/api.js
```
*Files: 1*

---

## Deploy

```
deploy/backend.Dockerfile
deploy/docker-compose.yml
deploy/env/backend.env.example
deploy/env/compose.env.example
deploy/env/frontend.env.example
deploy/frontend.Dockerfile
deploy/nginx/default.conf
deploy/postgres/init/01-enable-pgcrypto.sql
deploy/scripts/backup.sh
deploy/scripts/deploy.sh
deploy/scripts/init-letsencrypt.sh
```

*Files: 11*


# ./backend/app/core/security.py
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.utils import user_has_role


password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/token",
)


@dataclass
class AuthContext:
    user: User
    active_role: UserRole
    token_payload: dict[str, Any]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str | None,
) -> bool:
    if not hashed_password:
        return False

    return password_hash.verify(plain_password, hashed_password)


def validate_password_strength(password: str) -> None:
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароль должен содержать не менее 8 символов",
        )

    if len(password) > 128:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароль должен содержать не более 128 символов",
        )


def create_jwt_token(
    *,
    subject: uuid.UUID,
    token_type: str,
    expires_delta: timedelta,
    extra_claims: dict[str, Any] | None = None,
) -> str:
    now = utc_now()

    payload: dict[str, Any] = {
        "sub": str(subject),
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
        "jti": str(uuid.uuid4()),
    }

    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def create_access_token(
    *,
    user: User,
    active_role: UserRole,
) -> str:
    return create_jwt_token(
        subject=user.id,
        token_type="access",
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        extra_claims={
            "role": active_role.value,
            "auth_version": user.auth_version,
        },
    )


def create_role_selection_token(*, user: User) -> str:
    return create_jwt_token(
        subject=user.id,
        token_type="role_selection",
        expires_delta=timedelta(
            minutes=settings.ROLE_SELECTION_TOKEN_EXPIRE_MINUTES
        ),
        extra_claims={
            "auth_version": user.auth_version,
        },
    )


def decode_jwt_token(
    token: str,
    *,
    expected_type: str | None = None,
) -> dict[str, Any]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Недействительный или просроченный токен",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except InvalidTokenError as error:
        raise credentials_exception from error

    if expected_type and payload.get("type") != expected_type:
        raise credentials_exception

    if not payload.get("sub"):
        raise credentials_exception

    return payload


def ensure_user_can_authenticate(user: User | None) -> User:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учётные данные",
        )

    if user.deleted_at is not None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Аккаунт деактивирован",
        )

    if user.is_blocked:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Аккаунт заблокирован",
        )

    return user


async def get_current_auth(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> AuthContext:
    payload = decode_jwt_token(
        token,
        expected_type="access",
    )

    try:
        user_id = uuid.UUID(payload["sub"])
        active_role = UserRole(payload["role"])
        token_auth_version = int(payload["auth_version"])
    except (ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Некорректное содержимое токена",
            headers={"WWW-Authenticate": "Bearer"},
        ) from error

    user = ensure_user_can_authenticate(
        session.get(User, user_id)
    )

    if user.auth_version != token_auth_version:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Сессия больше не действительна",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user_has_role(session, user.id, active_role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Роль больше не доступна",
        )

    return AuthContext(
        user=user,
        active_role=active_role,
        token_payload=payload,
    )


def require_roles(*allowed_roles: UserRole):
    async def dependency(
        auth: AuthContext = Depends(get_current_auth),
    ) -> AuthContext:
        if auth.active_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав",
            )

        return auth

    return dependency

# ./backend/app/modules/users/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, get_current_auth, require_roles
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.schemas import (
    AdminBlockRequest,
    AdminUserListItem,
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
    update_data = payload.model_dump(exclude_unset=True)

    for field_name, value in update_data.items():
        setattr(auth.user, field_name, value)

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
    response_model=list[AdminUserListItem],
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
    search: str | None = Query(default=None, max_length=200),
    include_deleted: bool = False,
    session: Session = Depends(get_session),
) -> list[AdminUserListItem]:
    statement = select(User)

    if not include_deleted:
        statement = statement.where(User.deleted_at.is_(None))

    if search:
        normalized_search = search.strip().lower()
        statement = statement.where(
            User.email.contains(normalized_search)
        )

    users = session.exec(
        statement.order_by(User.created_at.desc())
    ).all()

    response: list[AdminUserListItem] = []

    for user in users:
        roles = [
            role_link.role
            for role_link in get_user_roles(session, user.id)
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

        response.append(
            AdminUserListItem(
                id=user.id,
                email=user.email,
                full_name=full_name,
                roles=roles,
                is_active=user.is_active,
                is_blocked=user.is_blocked,
                is_email_verified=user.email_verified_at is not None,
                deleted_at=user.deleted_at,
                created_at=user.created_at,
            )
        )

    return response


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


# ./backend/app/modules/users/utils.py
import uuid

from sqlmodel import Session, select

from app.modules.users.enums import UserRole
from app.modules.users.models import User, UserRoleLink
from app.modules.users.schemas import (
    DoctorProfileResponse,
    PatientProfileResponse,
    RelativeProfileResponse,
    RoleResponse,
    SpecialityResponse,
    UserResponse,
)


def normalize_email(email: str) -> str:
    return email.strip().lower()


def get_user_by_email(session: Session, email: str) -> User | None:
    normalized_email = normalize_email(email)

    return session.exec(
        select(User).where(User.email == normalized_email)
    ).first()


def get_user_by_id(session: Session, user_id: uuid.UUID) -> User | None:
    return session.get(User, user_id)


def get_user_roles(session: Session, user_id: uuid.UUID) -> list[UserRoleLink]:
    return list(
        session.exec(
            select(UserRoleLink)
            .where(UserRoleLink.user_id == user_id)
            .order_by(UserRoleLink.is_primary.desc(), UserRoleLink.created_at)
        ).all()
    )


def user_has_role(
    session: Session,
    user_id: uuid.UUID,
    role: UserRole,
) -> bool:
    role_link = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.user_id == user_id,
            UserRoleLink.role == role,
        )
    ).first()

    return role_link is not None


def get_primary_role(
    session: Session,
    user_id: uuid.UUID,
) -> UserRole | None:
    links = get_user_roles(session, user_id)

    if not links:
        return None

    primary = next((link for link in links if link.is_primary), None)

    return primary.role if primary else links[0].role


def build_user_response(
    *,
    session: Session,
    user: User,
    active_role: UserRole | None = None,
) -> UserResponse:
    role_links = get_user_roles(session, user.id)

    doctor_profile = None
    if user.doctor_profile and user.doctor_profile.speciality:
        doctor_profile = DoctorProfileResponse(
            id=user.doctor_profile.id,
            speciality=SpecialityResponse.model_validate(
                user.doctor_profile.speciality
            ),
        )

    patient_profile = None
    if user.patient_profile:
        patient_profile = PatientProfileResponse.model_validate(
            user.patient_profile
        )

    relative_profile = None
    if user.relative_profile:
        relative_profile = RelativeProfileResponse.model_validate(
            user.relative_profile
        )

    return UserResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        gender=user.gender,
        is_active=user.is_active,
        is_blocked=user.is_blocked,
        is_email_verified=user.email_verified_at is not None,
        deleted_at=user.deleted_at,
        roles=[
            RoleResponse(
                role=role_link.role,
                is_primary=role_link.is_primary,
            )
            for role_link in role_links
        ],
        active_role=active_role,
        doctor_profile=doctor_profile,
        patient_profile=patient_profile,
        relative_profile=relative_profile,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )

# ./backend/app/modules/users/enums.py
from enum import Enum


class UserRole(str, Enum):
    SUPERUSER = "superuser"
    PATIENT = "patient"
    DOCTOR = "doctor"
    RELATIVE = "relative"
    MED_ASSISTANT = "med_assistant"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class DoctorPatientStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    REJECTED = "rejected"
    DETACHED = "detached"


class RelativePatientStatus(str, Enum):
    ACTIVE = "active"
    DETACHED = "detached"


// ./frontend/app/stores/user.js
export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const loading = ref(false)

  const fullName = computed(() => {
    if (!user.value) return ''

    const parts = [
      user.value.last_name,
      user.value.first_name,
      user.value.middle_name,
    ].filter(Boolean)

    return parts.join(' ') || user.value.email
  })

  const initials = computed(() => {
    if (!user.value) return '?'

    const firstName = user.value.first_name || ''
    const lastName = user.value.last_name || ''

    const value = `${firstName[0] || ''}${lastName[0] || ''}`

    return value.toUpperCase() || '?'
  })

  const isEmailVerified = computed(
    () => Boolean(user.value?.is_email_verified),
  )

  async function fetchMe() {
    const { $api } = useNuxtApp()

    loading.value = true

    try {
      user.value = await $api('/api/v1/users/me')
      return user.value
    } finally {
      loading.value = false
    }
  }

  async function resendVerificationEmail() {
    const { $api } = useNuxtApp()

    return await $api(
      '/api/v1/auth/email-verification/resend',
      {
        method: 'POST',
      },
    )
  }

  function clear() {
    user.value = null
  }

  return {
    user,
    loading,
    fullName,
    initials,
    isEmailVerified,
    fetchMe,
    resendVerificationEmail,
    clear,
  }
})

// ./frontend/app/stores/auth.js
export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref(null)
  const activeRole = ref(null)

  const roleSelectionToken = ref(null)
  const availableRoles = ref([])

  const loading = ref(false)
  const initialized = ref(false)

  const isAuthenticated = computed(
    () => Boolean(accessToken.value),
  )

  const needsRoleSelection = computed(
    () =>
      Boolean(roleSelectionToken.value)
      && availableRoles.value.length > 0,
  )

  function persistAuth() {
    if (!import.meta.client) return

    if (accessToken.value) {
      localStorage.setItem(
        'mentalme_access_token',
        accessToken.value,
      )
    } else {
      localStorage.removeItem('mentalme_access_token')
    }

    if (activeRole.value) {
      localStorage.setItem(
        'mentalme_active_role',
        activeRole.value,
      )
    } else {
      localStorage.removeItem('mentalme_active_role')
    }
  }

  function initFromStorage() {
    if (!import.meta.client || initialized.value) return

    accessToken.value = localStorage.getItem(
      'mentalme_access_token',
    )

    activeRole.value = localStorage.getItem(
      'mentalme_active_role',
    )

    initialized.value = true
  }

  function clearRoleSelection() {
    roleSelectionToken.value = null
    availableRoles.value = []
  }

  function processLoginResponse(response) {
    if (response.status === 'authenticated') {
      accessToken.value = response.access_token
      activeRole.value = response.active_role

      clearRoleSelection()
      persistAuth()

      return {
        authenticated: true,
        needsRoleSelection: false,
      }
    }

    roleSelectionToken.value =
      response.role_selection_token

    availableRoles.value = response.roles || []

    return {
      authenticated: false,
      needsRoleSelection: true,
    }
  }

  async function login(email, password) {
    const { $api } = useNuxtApp()

    loading.value = true

    try {
      const response = await $api('/api/v1/auth/login', {
        method: 'POST',
        body: {
          email,
          password,
        },
      })

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  async function selectRole(role) {
    const { $api } = useNuxtApp()

    if (!roleSelectionToken.value) {
      throw new Error('Отсутствует токен выбора роли')
    }

    loading.value = true

    try {
      const response = await $api(
        '/api/v1/auth/select-role',
        {
          method: 'POST',
          body: {
            role_selection_token:
              roleSelectionToken.value,
            role,
          },
        },
      )

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  async function loginWithPasskey() {
    const { $api } = useNuxtApp()
    const { authenticateWithPasskey } = useWebAuthn()

    loading.value = true

    try {
      const optionsResponse = await $api(
        '/api/v1/auth/passkeys/authentication/options',
        {
          method: 'POST',
        },
      )

      const credential = await authenticateWithPasskey(
        optionsResponse.options,
      )

      const response = await $api(
        '/api/v1/auth/passkeys/authentication/verify',
        {
          method: 'POST',
          body: {
            challenge_id: optionsResponse.challenge_id,
            credential,
          },
        },
      )

      return processLoginResponse(response)
    } finally {
      loading.value = false
    }
  }

  function logout() {
    accessToken.value = null
    activeRole.value = null

    clearRoleSelection()
    persistAuth()

    const notificationsStore = useNotificationsStore()
    notificationsStore.disconnect()

    const userStore = useUserStore()
    userStore.clear()

    return navigateTo('/login')
  }

  return {
    accessToken,
    activeRole,
    roleSelectionToken,
    availableRoles,
    loading,
    initialized,

    isAuthenticated,
    needsRoleSelection,

    initFromStorage,
    login,
    loginWithPasskey,
    selectRole,
    logout,
    clearRoleSelection,
  }
})

<!-- ./frontend/app/components/invitations/LinkDialog.vue -->
<script setup>
import QRCode from 'qrcode'

const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  url: {
    type: String,
    default: '',
  },
  title: {
    type: String,
    default: 'Приглашение',
  },
  description: {
    type: String,
    default:
      'Отсканируйте QR-код или скопируйте ссылку.',
  },
})

const qrCodeDataUrl = ref('')
const generatingQr = ref(false)
const copied = ref(false)

async function generateQrCode() {
  if (!props.url) {
    qrCodeDataUrl.value = ''
    return
  }

  generatingQr.value = true

  try {
    qrCodeDataUrl.value = await QRCode.toDataURL(
      props.url,
      {
        width: 320,
        margin: 2,
        errorCorrectionLevel: 'M',
        color: {
          dark: '#111827',
          light: '#ffffff',
        },
      },
    )
  } finally {
    generatingQr.value = false
  }
}

async function copyLink() {
  if (!props.url) return

  try {
    await navigator.clipboard.writeText(props.url)
    copied.value = true

    window.setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch {
    copied.value = false
  }
}

watch(
  () => [model.value, props.url],
  ([opened]) => {
    if (opened) {
      generateQrCode()
    }
  },
  {
    immediate: true,
  },
)
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    :title="title"
    max-width-class="max-w-md"
  >
    <div class="flex flex-col items-center gap-5">
      <p class="text-base-content/70 text-center text-sm">
        {{ description }}
      </p>

      <div
        class="bg-white flex size-72 max-w-full items-center justify-center rounded-2xl p-3 shadow-sm"
      >
        <span
          v-if="generatingQr"
          class="loading loading-spinner loading-lg text-primary"
        />

        <img
          v-else-if="qrCodeDataUrl"
          :src="qrCodeDataUrl"
          alt="QR-код приглашения"
          class="h-full w-full object-contain"
        >

        <div
          v-else
          class="text-error flex flex-col items-center gap-2 text-center"
        >
          <Icon
            name="lucide:triangle-alert"
            class="size-8"
          />
          <span class="text-sm">
            Ссылка не сформирована
          </span>
        </div>
      </div>

      <div class="join w-full">
        <input
          :value="url"
          type="text"
          readonly
          class="input input-bordered join-item min-w-0 flex-1"
          aria-label="Ссылка приглашения"
          @focus="$event.target.select()"
        >

        <button
          type="button"
          class="btn btn-primary join-item"
          :disabled="!url"
          @click="copyLink"
        >
          <Icon
            :name="copied ? 'lucide:check' : 'lucide:copy'"
            class="size-4"
          />

          <span class="hidden sm:inline">
            {{ copied ? 'Скопировано' : 'Копировать' }}
          </span>
        </button>
      </div>
    </div>

    <template #footer>
      <button
        type="button"
        class="btn btn-primary w-full"
        @click="model = false"
      >
        Готово
      </button>
    </template>
  </UiResponsiveDialog>
</template>

<!-- ./frontend/app/components/ui/BottomSheet.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true,
  },
  showCloseButton: {
    type: Boolean,
    default: true,
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

const translateY = ref(0)
const dragging = ref(false)

let pointerStartY = 0

useBodyScrollLock(opened)

const sheetStyle = computed(() => ({
  transform: translateY.value
    ? `translateY(${translateY.value}px)`
    : undefined,
  transition: dragging.value
    ? 'none'
    : 'transform 180ms ease',
}))

function close() {
  model.value = false
  translateY.value = 0
  dragging.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handlePointerDown(event) {
  dragging.value = true
  pointerStartY = event.clientY

  event.currentTarget.setPointerCapture?.(
    event.pointerId,
  )
}

function handlePointerMove(event) {
  if (!dragging.value) return

  translateY.value = Math.max(
    0,
    event.clientY - pointerStartY,
  )
}

function handlePointerUp() {
  if (!dragging.value) return

  dragging.value = false

  if (translateY.value > 100) {
    close()
    return
  }

  translateY.value = 0
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
    translateY.value = 0
    emit('opened')
  }
})

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'keydown',
    handleKeydown,
  )
})
</script>

<template>
  <Teleport to="body">
    <Transition name="ui-sheet">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-end bg-black/50 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 safe-area-bottom flex max-h-[92dvh] w-full flex-col overflow-hidden rounded-t-3xl shadow-2xl"
          :style="sheetStyle"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <div
            class="flex shrink-0 touch-none justify-center py-3"
            @pointerdown="handlePointerDown"
            @pointermove="handlePointerMove"
            @pointerup="handlePointerUp"
            @pointercancel="handlePointerUp"
          >
            <div
              class="bg-base-300 h-1.5 w-12 rounded-full"
            />
          </div>

          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-4 pb-4"
          >
            <slot name="header">
              <h2 class="min-w-0 flex-1 text-lg font-semibold">
                {{ title }}
              </h2>
            </slot>

            <button
              v-if="showCloseButton"
              type="button"
              class="btn btn-circle btn-ghost btn-sm shrink-0"
              aria-label="Закрыть"
              @click="close"
            >
              <Icon
                name="lucide:x"
                class="size-5"
              />
            </button>
          </header>

          <div class="min-h-0 flex-1 overflow-y-auto px-4 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-4 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-sheet-enter-active,
.ui-sheet-leave-active {
  transition: opacity 220ms ease;
}

.ui-sheet-enter-active section,
.ui-sheet-leave-active section {
  transition: transform 220ms ease;
}

.ui-sheet-enter-from,
.ui-sheet-leave-to {
  opacity: 0;
}

.ui-sheet-enter-from section,
.ui-sheet-leave-to section {
  transform: translateY(100%);
}
</style>

<!-- ./frontend/app/components/ui/Modal.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  title: {
    type: String,
    default: '',
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true,
  },
  showCloseButton: {
    type: Boolean,
    default: true,
  },
  maxWidthClass: {
    type: String,
    default: 'max-w-lg',
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

useBodyScrollLock(opened)

function close() {
  model.value = false
  emit('close')
}

function handleBackdrop() {
  if (props.closeOnBackdrop) {
    close()
  }
}

function handleKeydown(event) {
  if (event.key === 'Escape' && model.value) {
    close()
  }
}

watch(model, (value) => {
  if (value) {
    emit('opened')
  }
})

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener(
    'keydown',
    handleKeydown,
  )
})
</script>

<template>
  <Teleport to="body">
    <Transition name="ui-modal">
      <div
        v-if="model"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-[2px]"
        role="presentation"
        @mousedown.self="handleBackdrop"
      >
        <section
          class="bg-base-100 relative flex max-h-[calc(100dvh-2rem)] w-full flex-col overflow-hidden rounded-2xl shadow-2xl"
          :class="maxWidthClass"
          role="dialog"
          aria-modal="true"
          :aria-label="title || 'Диалоговое окно'"
        >
          <header
            v-if="title || showCloseButton || $slots.header"
            class="border-base-300 flex shrink-0 items-center gap-3 border-b px-5 py-4"
          >
            <slot name="header">
              <h2 class="min-w-0 flex-1 text-lg font-semibold">
                {{ title }}
              </h2>
            </slot>

            <button
              v-if="showCloseButton"
              type="button"
              class="btn btn-circle btn-ghost btn-sm shrink-0"
              aria-label="Закрыть"
              @click="close"
            >
              <Icon
                name="lucide:x"
                class="size-5"
              />
            </button>
          </header>

          <div class="min-h-0 flex-1 overflow-y-auto px-5 py-5">
            <slot />
          </div>

          <footer
            v-if="$slots.footer"
            class="border-base-300 shrink-0 border-t px-5 py-4"
          >
            <slot name="footer" />
          </footer>
        </section>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.ui-modal-enter-active,
.ui-modal-leave-active {
  transition: opacity 180ms ease;
}

.ui-modal-enter-active section,
.ui-modal-leave-active section {
  transition:
    transform 180ms ease,
    opacity 180ms ease;
}

.ui-modal-enter-from,
.ui-modal-leave-to {
  opacity: 0;
}

.ui-modal-enter-from section,
.ui-modal-leave-to section {
  opacity: 0;
  transform: scale(0.96) translateY(0.5rem);
}
</style>

сейчас суперпользователь может только просматривать других пользователей...
А мне надо, чтобы суперпользователь мог создавать других суперпользователей по ссылке/qr коду, либо мог сразу указать почту, на которую пользователь, который будет рагистрироваться видеть OTP (One-Time Password) и вводить его при переходе по ссылке (думаю, так будет проще)

компонент otp лучше взять из daisyui:

otp	Component	For the container label
otp-joined	Modifier	Connects the character boxes together
otp-xs	Size	Extra small size
otp-sm	Size	Small size
otp-md	Size	Medium size [Default]
otp-lg	Size	Large size
otp-xl	Size	Extra large size
otp-neutral	Color	neutral color
otp-primary	Color	primary color
otp-secondary	Color	secondary color
otp-accent	Color	accent color
otp-success	Color	success color
otp-info	Color	info color
otp-warning	Color	warning color
otp-error	Color	error color


<label class="otp">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="6" pattern="[0-9]{6}" required />
</label>

<label class="otp otp-neutral">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-primary">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-secondary">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-accent">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-info">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-success">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-warning">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

<label class="otp otp-error">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <input type="text" autocomplete="one-time-code" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" required />
</label>

Пусть суперпользователь может добавлять любого пользователя:
на широких дисплеях открывается Modal, а на мобильных устройствах - bottomsheet 
в ней я могу выбирать роль пользователя, которого хочу зарегать и там формировать ссылку: для врача/медицинского ассистента/родственника/другоого суперпользователя надо вводить email. При добавлении пациента обязательный параметр - record_id ну и email. пусть если пациента создает суперпользователь или медицинский ассистент, у него пока не будет никаких тегов (когда врач приглашает пациента, пациент наследует теги от врача). 

Медицинский ассистент может добавлять всех, кроме суперпользователей

Плюс, надо сделать для пользователей возможность изменения пароля из аккаунта. Пусть атм просто будут 3 поля: ввод старого пароля, ввод нового пароля и подтверждение пароля.

Если тебе нужны какие-то файлы, попроси прислать.

Желательно этот момент делать без изменений в базе данных, чтобы не делать миграции. Но если вообще без этого никак, давай переделаем.

В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api. как ты видел выше

// ./frontend/app/middleware/auth.global.js
export default defineNuxtRouteMiddleware((to) => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  const publicPaths = [
    '/login',
    '/forgot-password',
    '/reset-password',
    '/verify-email',
    '/register',
  ]

  const isPublicPath = publicPaths.some((path) =>
    to.path.startsWith(path),
  )

  if (isPublicPath) {
    if (
      auth.isAuthenticated
      && to.path === '/login'
    ) {
      return navigateTo('/dashboard')
    }

    return
  }

  if (!auth.isAuthenticated) {
    return navigateTo(
      `/login?redirect=${encodeURIComponent(to.fullPath)}`,
    )
  }
})

для этого middleware, не надо на страницах делать  definePageMeta({ 
  middleware: ['default'],
}), потому что он и так подгрузится. А для остальных middleware это надо указывать

// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  modules: [
    '@pinia/nuxt',
    '@nuxt/icon',
  ],
  icon: {
    serverBundle: {
      collections: [
        'lucide',
      ],
    },

    clientBundle: {
      scan: true,
      sizeLimitKb: 512,
    },
  },
  vite: {
    plugins: [tailwindcss() as any],
  },
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBase:
        process.env.NUXT_PUBLIC_API_BASE
        || 'http://localhost:8000',
      siteUrl:
        process.env.NUXT_PUBLIC_SITE_URL
        || 'http://localhost:3000',
    },
  },
  app: {
    head: {
      title: 'MentalMe',
      meta: [
        {
          charset: 'utf-8',
        },
        {
          name: 'viewport',
          content:
            'width=device-width, initial-scale=1, viewport-fit=cover',
        },
        {
          name: 'description',
          content: 'MentalMe — сервис сопровождения пациентов',
        },
        {
          name: 'theme-color',
          content: '#ffffff',
        },
      ],
    },
  },
})

в коде надо, чтобы был такой порядок:
<script setup></script>
<template></template>
<style></style> - если нужно

не забывай оборачивать код, чтобы я мог его легко скопировать


Для начала задай мне вопросы по изменениям и функционалу, если они есть



























----------------


Сценарий регистрации: блин, давай лучше откажемся от OTP... слишком сложно. Пусть будет qr код, кнопка для копирования ссылки, как у врача, когда он приглашает пациента и кнопка отправить ссылку на почту. При регистрации ,пусть пользователь вводит новый пароль при переходе по ссылке... Думаю, так будет проще и прозрачнее

Обязательность email - да, для всех... точно. просто, для пациента еще и record_id

OTP и ссылка - все, OTP НЕ ДЕЛАЕМ. регистрация по ссылке стандартная как приглашение пациента

Ссылка должна стать недействительной:

после завершения регистрации; - да
после истечения срока;- да
после отмены приглашения;- да
после выпуска нового приглашения для того же email и роли? - да

Что делать, если пользователь с таким email уже существует?
Да, давай запретим пока уже зареганым пользователям отправку ссылки для простоты


Данные при регистрации - ну, тут главное, чтобы регистрация происходила быстро. а пользователь потом сможет сам указать в настройках. Забыл... для врача еще очень важно добавлять специальность из тех, которые есть в базе. Блин, у меня до сих пор нет функционала для добавления специальностей и тегв вручную (делал через seed).... Давай их тоже добавим. Файлы tags и specialities вышлю

родственнику нужно сразу выбирать пациента или связь создаётся позднее? - да, пусть позднее
для пациента record_id отображается в форме, но недоступен для редактирования? - ДА!
email должен быть зафиксирован приглашением и недоступен для изменения? пока так сделаем

Права доступа:
делай пока только для Superuser и Med assistant. у Doctor то, что есть меня пока устраивает

Медицинский ассистент действительно может приглашать других медицинских ассистентов? - не, пусть только superuser
Может ли медицинский ассистент приглашать врачей и родственников без дополнительных ограничений? - да
Нужно ли сохранить текущий сценарий приглашения пациента врачом без изменений? - да. его не трогай
Может ли суперпользователь отменять и повторно отправлять любые приглашения? - ну, давай сделаем
Медицинский ассистент может управлять только собственными приглашениями или всеми, кроме приглашений суперпользователей? - только собственными

4. Пациент и record_id
формат record_id: произвольная строка, UUID или число; - формально, в базе так record_id: str = Field(unique=True, index=True, max_length=100), но record_id это примерно такое: A000000 - ZZ999999 То есть, одна или 2 буквы в верхнем регистре и 6 цифр. Но давай мы сделаем так ,чтобы на бекенде просто все переводилось в верзний регистр, а на фронтенде сделаем, чтобы нельзя было забить не по правилам. Думаю, так буде тпроше и без раздувания кода.

должен ли он быть уникальным глобально; - да, обязательно!

что делать, если такой record_id уже занят - тогда запрещать регистрацию по нему. пациент уже есть в системе.

# ./backend/app/modules/users/models.py
...

class PatientProfile(SQLModel, table=True):
    __tablename__ = "patient_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    record_id: str = Field(unique=True, index=True, max_length=100)
    fullname: Optional[str] = Field(default=None, max_length=300)
    dob: Optional[date] = Field(default=None)

    pro_enabled: bool = Field(default=False)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="patient_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProfile.user_id]",
        },
    )

    doctor_links: list["DoctorPatientLink"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.patient_id]",
        },
    )

    relative_links: list["RelativePatientLink"] = Relationship(
        back_populates="patient",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.patient_id]",
        },
    )


5. Интерфейс управления пользователями: 
Нужно ли на этой же странице показывать:

активные приглашения; - ну, желательно
истёкшие приглашения; - желательно
статус отправки письма;  - желательно
кнопку повторной отправки; - желательно
кнопку отмены; не знаю.. ну, можно ,если не раздует код
кем и когда создано приглашение? желательно, конечно


6. Изменение пароля 
Какое поведение нужно? - Не завершать никакие сессии — не рекомендую.
текущие требования остаются: от 8 до 128 символов? - да, давай
нужно ли запрещать новый пароль, совпадающий со старым? - нет, пусть вводит старый ,если хочет
что делать с пользователем, созданным только через passkey и не имеющим пароля: таких пока нет

7. Нужна ли миграция тут как решишь на основании файлов

















---------------
Важный момент со ссылкой - да, давай так сделаем

Оставить как сейчас. Это безопаснее, поскольку приглашение могли передать через QR-код. - давай так сдеалем
A: оставить текущую безопасную реализацию и после смены пароля выйти из аккаунта; - если уже сделано, не надо переделывать

3. Управление тегами и специальностями - суперпользователь может делать вообще все, медицинский ассистент - согласен с твоим вариантом

специальность нельзя удалить, если к ней привязаны врачи, программы или приглашения; - да, давай так сделаем (и для суперпользователя). можно скрыть
тег нельзя удалить, если он используется в контенте, программах, специальностях или настройках врачей; - да, давай пуст ьможно будет сркрыть
4. Где разместить справочники как ты предлагаешь

