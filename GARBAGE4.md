У меня такой проект:
# Project Structure

> Generated: 2026-09-04 21:36

---

## AI Backend

```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (29 lines)
backend/alembic/versions/4a9d77a6cc23_initial_schema.py (887 lines)
backend/alembic/versions/6eb4582e2464_add_new_field_to_users.py (33 lines)
backend/alembic/versions/7c21a6d4ef10_admin_invitations_and_hidden_directories.py (170 lines)
backend/alembic/versions/9f31b8c4d2e7_medical_services.py (454 lines)
backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py (141 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (58 lines)
backend/app/core/db.py (129 lines)
backend/app/core/email.py (150 lines)
backend/app/core/security.py (232 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (107 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/models.py (115 lines)
backend/app/modules/articles/routers.py (644 lines)
backend/app/modules/articles/schemas.py (89 lines)
backend/app/modules/articles/utils.py (177 lines)
backend/app/modules/assignments/__init__.py (0 lines)
backend/app/modules/assignments/enums.py (14 lines)
backend/app/modules/assignments/models.py (81 lines)
backend/app/modules/assignments/routers.py (302 lines)
backend/app/modules/assignments/schemas.py (56 lines)
backend/app/modules/assignments/utils.py (106 lines)
backend/app/modules/auth/__init__.py (0 lines)
backend/app/modules/auth/models.py (73 lines)
backend/app/modules/auth/routers.py (753 lines)
backend/app/modules/auth/schemas.py (97 lines)
backend/app/modules/auth/utils.py (148 lines)
backend/app/modules/consents/__init__.py (0 lines)
backend/app/modules/consents/enums.py (15 lines)
backend/app/modules/consents/models.py (83 lines)
backend/app/modules/consents/routers.py (277 lines)
backend/app/modules/consents/schemas.py (38 lines)
backend/app/modules/consents/utils.py (37 lines)
backend/app/modules/content/__init__.py (0 lines)
backend/app/modules/content/utils.py (167 lines)
backend/app/modules/events/__init__.py (0 lines)
backend/app/modules/events/enums.py (31 lines)
backend/app/modules/events/models.py (83 lines)
backend/app/modules/events/routers.py (69 lines)
backend/app/modules/events/schemas.py (32 lines)
backend/app/modules/events/service.py (54 lines)
backend/app/modules/invitations/__init__.py (0 lines)
backend/app/modules/invitations/admin_routers.py (422 lines)
backend/app/modules/invitations/admin_schemas.py (93 lines)
backend/app/modules/invitations/admin_utils.py (224 lines)
backend/app/modules/invitations/enums.py (17 lines)
backend/app/modules/invitations/models.py (127 lines)
backend/app/modules/invitations/routers.py (1277 lines)
backend/app/modules/invitations/schemas.py (152 lines)
backend/app/modules/invitations/utils.py (222 lines)
backend/app/modules/notifications/__init__.py (0 lines)
backend/app/modules/notifications/enums.py (30 lines)
backend/app/modules/notifications/models.py (64 lines)
backend/app/modules/notifications/routers.py (288 lines)
backend/app/modules/notifications/schemas.py (47 lines)
backend/app/modules/notifications/service.py (163 lines)
backend/app/modules/patients/__init__.py (0 lines)
backend/app/modules/patients/enums.py (7 lines)
backend/app/modules/patients/routers.py (511 lines)
backend/app/modules/patients/schemas.py (138 lines)
backend/app/modules/patients/utils.py (231 lines)
backend/app/modules/programs/__init__.py (0 lines)
backend/app/modules/programs/enums.py (22 lines)
backend/app/modules/programs/models.py (339 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1615 lines)
backend/app/modules/programs/schemas.py (257 lines)
backend/app/modules/programs/utils.py (576 lines)
backend/app/modules/questionnaires/__init__.py (0 lines)
backend/app/modules/questionnaires/enums.py (17 lines)
backend/app/modules/questionnaires/json_q/audit.json (272 lines)
backend/app/modules/questionnaires/models.py (226 lines)
backend/app/modules/questionnaires/Readme.md (61 lines)
backend/app/modules/questionnaires/routers.py (1240 lines)
backend/app/modules/questionnaires/schemas.py (213 lines)
backend/app/modules/questionnaires/utils.py (303 lines)
backend/app/modules/referrals/__init__.py (0 lines)
backend/app/modules/referrals/enums.py (19 lines)
backend/app/modules/referrals/models.py (114 lines)
backend/app/modules/referrals/routers.py (464 lines)
backend/app/modules/referrals/schemas.py (83 lines)
backend/app/modules/referrals/utils.py (42 lines)
backend/app/modules/relationships/__init__.py (0 lines)
backend/app/modules/relationships/routers.py (580 lines)
backend/app/modules/relationships/schemas.py (79 lines)
backend/app/modules/services/__init__.py (0 lines)
backend/app/modules/services/enums.py (8 lines)
backend/app/modules/services/models.py (131 lines)
backend/app/modules/services/routers.py (350 lines)
backend/app/modules/services/schemas.py (159 lines)
backend/app/modules/services/utils.py (118 lines)
backend/app/modules/specialities/__init__.py (0 lines)
backend/app/modules/specialities/routers.py (331 lines)
backend/app/modules/specialities/schemas.py (50 lines)
backend/app/modules/tags/__init__.py (0 lines)
backend/app/modules/tags/enums.py (7 lines)
backend/app/modules/tags/models.py (192 lines)
backend/app/modules/tags/routers.py (957 lines)
backend/app/modules/tags/schemas.py (104 lines)
backend/app/modules/tags/utils.py (246 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (334 lines)
backend/app/modules/users/routers.py (360 lines)
backend/app/modules/users/schemas.py (145 lines)
backend/app/modules/users/utils.py (126 lines)
backend/requirements.txt (47 lines)
backend/seed/create_superuser.py (153 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database.db (968 lines)
```

*Files: 122*

---

## Frontend

### components

```
frontend/app/components/articles/Form.vue (233 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (291 lines)
frontend/app/components/assignments/ContentPicker.vue (181 lines)
frontend/app/components/assignments/CreateDialog.vue (345 lines)
frontend/app/components/assignments/PatientList.vue (108 lines)
frontend/app/components/assignments/PickerItem.vue (130 lines)
frontend/app/components/auth/PasswordForm.vue (173 lines)
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (295 lines)
frontend/app/components/content/RichTextEditor.vue (469 lines)
frontend/app/components/content/RichTextRenderer.vue (136 lines)
frontend/app/components/content/TagSelector.vue (80 lines)
frontend/app/components/directories/Specialities.vue (471 lines)
frontend/app/components/directories/Tags.vue (311 lines)
frontend/app/components/invitations/LinkDialog.vue (257 lines)
frontend/app/components/invitations/PatientDialog.vue (435 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (88 lines)
frontend/app/components/layout/Footer.vue (52 lines)
frontend/app/components/layout/Logo.vue (86 lines)
frontend/app/components/layout/Navbar.vue (338 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (111 lines)
frontend/app/components/patients/List.vue (257 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/patients/Tags.vue (105 lines)
frontend/app/components/programs/configurator/Editor.vue (633 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (272 lines)
frontend/app/components/programs/configurator/ServiceSelect.vue (170 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (384 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (529 lines)
frontend/app/components/questionnaires/JsonImporter.vue (264 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/services/DeleteDialog.vue (95 lines)
frontend/app/components/services/FormDialog.vue (463 lines)
frontend/app/components/services/List.vue (181 lines)
frontend/app/components/services/VisibilityDialog.vue (98 lines)
frontend/app/components/tags/OverrideEditor.vue (231 lines)
frontend/app/components/ui/BottomSheet.vue (203 lines)
frontend/app/components/ui/ContentSkeleton.vue (73 lines)
frontend/app/components/ui/MegaMenu.vue (205 lines)
frontend/app/components/ui/Modal.vue (150 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (99 lines)
frontend/app/components/users/InvitationList.vue (231 lines)
frontend/app/components/users/InviteDialog.vue (29 lines)
frontend/app/components/users/InviteForm.vue (367 lines)
frontend/app/components/users/List.vue (182 lines)
```
*Files: 58*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (43 lines)
frontend/app/pages/content/articles/index.vue (169 lines)
frontend/app/pages/content/articles/new.vue (49 lines)
frontend/app/pages/content/questionnaires/[id].vue (319 lines)
frontend/app/pages/content/questionnaires/index.vue (166 lines)
frontend/app/pages/content/questionnaires/new.vue (9 lines)
frontend/app/pages/dashboard.vue (168 lines)
frontend/app/pages/forgot-password.vue (102 lines)
frontend/app/pages/index.vue (3 lines)
frontend/app/pages/login.vue (238 lines)
frontend/app/pages/patients/[id]/index.vue (469 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (37 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (391 lines)
frontend/app/pages/programs/index.vue (285 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (375 lines)
frontend/app/pages/questionnaires/index.vue (151 lines)
frontend/app/pages/register/invitation.vue (321 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/services/index.vue (205 lines)
frontend/app/pages/settings/directories.vue (90 lines)
frontend/app/pages/settings/profile.vue (265 lines)
frontend/app/pages/settings/security.vue (325 lines)
frontend/app/pages/settings/tags.vue (123 lines)
frontend/app/pages/users/index.vue (529 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 29*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (22 lines)
```
*Files: 2*

### composables

```
frontend/app/composables/useAppNavigation.js (193 lines)
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useProgramPrice.js (180 lines)
frontend/app/composables/useReadingProgress.js (178 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 7*

### stores

```
frontend/app/stores/articles.js (106 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/invitations.js (53 lines)
frontend/app/stores/notifications.js (312 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (174 lines)
frontend/app/stores/services.js (159 lines)
frontend/app/stores/tag-access.js (210 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 14*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/doctor-only.js (14 lines)
frontend/app/middleware/program-manager.js (19 lines)
frontend/app/middleware/service-manager.js (19 lines)
frontend/app/middleware/user-manager.js (19 lines)
```
*Files: 5*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*

смотри, модуль events записывает разные события (пока этот функционал используется неполно):

# ./backend/app/modules/events/enums.py
from enum import Enum


class EventType(str, Enum):
    REFERRAL_CREATED = "referral_created"
    LINK_SENT = "link_sent"
    LINK_OPENED = "link_opened"

    REGISTRATION_COMPLETED = "registration_completed"
    CONSENT_GIVEN = "consent_given"

    QUESTIONNAIRE_STARTED = "questionnaire_started"
    QUESTIONNAIRE_COMPLETED = "questionnaire_completed"
    ARTICLE_READ = "article_read"

    CONTACT_REQUESTED = "contact_requested"
    ASSISTANT_CALL_ATTEMPTED = "assistant_call_attempted"
    ASSISTANT_CONTACTED = "assistant_contacted"

    APPOINTMENT_BOOKED = "appointment_booked"
    APPOINTMENT_ATTENDED = "appointment_attended"

    PACKAGE_OFFERED = "package_offered"
    PAYMENT_LINK_SENT = "payment_link_sent"
    PACKAGE_PURCHASED = "package_purchased"
    REFUND_CREATED = "refund_created"

    PROGRAM_STARTED = "program_started"
    PROGRAM_COMPLETED = "program_completed"
    PROGRAM_IN_PROGRESS = "program_in_progress"

# ./backend/app/modules/events/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, SQLModel

from app.modules.events.enums import EventType


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    event_type: EventType = Field(index=True)

    patient_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="patient_profiles.id",
        index=True,
    )

    actor_user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    referral_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="referrals.id",
        index=True,
    )

    doctor_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="doctor_profiles.id",
        index=True,
    )

    speciality_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="specialities.id",
        index=True,
    )

    product_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    program_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    subject_type: Optional[str] = Field(
        default=None,
        index=True,
        max_length=100,
    )

    subject_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    metadata_json: dict = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )

    occurred_at: datetime = Field(
        default_factory=utc_now,
        index=True,
    )
    created_at: datetime = Field(default_factory=utc_now)

# ./backend/app/modules/events/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from app.modules.events.enums import EventType


class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    event_type: EventType

    patient_id: uuid.UUID | None
    actor_user_id: uuid.UUID | None
    referral_id: uuid.UUID | None
    doctor_id: uuid.UUID | None
    speciality_id: uuid.UUID | None

    product_id: uuid.UUID | None
    program_id: uuid.UUID | None

    subject_type: str | None
    subject_id: uuid.UUID | None

    metadata_json: dict[str, Any]

    occurred_at: datetime
    created_at: datetime

# ./backend/app/modules/events/service.py
import uuid
from typing import Any

from sqlmodel import Session

from app.modules.events.enums import EventType
from app.modules.events.models import Event


def record_event(
    *,
    session: Session,
    event_type: EventType,
    patient_id: uuid.UUID | None = None,
    actor_user_id: uuid.UUID | None = None,
    referral_id: uuid.UUID | None = None,
    doctor_id: uuid.UUID | None = None,
    speciality_id: uuid.UUID | None = None,
    product_id: uuid.UUID | None = None,
    program_id: uuid.UUID | None = None,
    subject_type: str | None = None,
    subject_id: uuid.UUID | None = None,
    metadata: dict[str, Any] | None = None,
) -> Event:
    """
    ЕДИНАЯ ТОЧКА РЕГИСТРАЦИИ БИЗНЕС-СОБЫТИЙ.

    События создаются на backend после успешной проверки
    бизнес-операции. Frontend может сообщить о действии,
    но не должен самостоятельно считаться источником истины.

    Для отключения конкретного события достаточно убрать вызов
    record_event() из соответствующей бизнес-операции.

    Обычные просмотры страниц здесь не регистрируются.
    """
    event = Event(
        event_type=event_type,
        patient_id=patient_id,
        actor_user_id=actor_user_id,
        referral_id=referral_id,
        doctor_id=doctor_id,
        speciality_id=speciality_id,
        product_id=product_id,
        program_id=program_id,
        subject_type=subject_type,
        subject_id=subject_id,
        metadata_json=metadata or {},
    )

    session.add(event)

    return event

# ./backend/app/modules/events/routers.py
import uuid

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.events.models import Event
from app.modules.events.schemas import EventResponse
from app.modules.users.enums import UserRole
from app.modules.users.models import DoctorProfile


router = APIRouter(
    prefix="/api/v1/events",
    tags=["Events"],
)


@router.get("", response_model=list[EventResponse])
async def list_events(
    referral_id: uuid.UUID | None = None,
    patient_id: uuid.UUID | None = None,
    limit: int = 200,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> list[Event]:
    safe_limit = min(max(limit, 1), 500)

    statement = select(Event)

    if referral_id:
        statement = statement.where(
            Event.referral_id == referral_id
        )

    if patient_id:
        statement = statement.where(
            Event.patient_id == patient_id
        )

    if auth.active_role == UserRole.DOCTOR:
        doctor = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == auth.user.id
            )
        ).first()

        if not doctor:
            return []

        statement = statement.where(
            Event.doctor_id == doctor.id
        )

    return list(
        session.exec(
            statement
            .order_by(Event.occurred_at.desc())
            .limit(safe_limit)
        ).all()
    )

# ./backend/app/modules/articles/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Article(SQLModel, table=True):
    __tablename__ = "articles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str = Field(index=True, max_length=300)
    content: str

    pro_content: bool = Field(default=True, index=True)
    is_hidden: bool = Field(default=False, index=True)

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    tag_links: list["ArticleTagLink"] = Relationship(
        back_populates="article",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class ArticleTagLink(SQLModel, table=True):
    __tablename__ = "article_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "article_id",
            "tag_id",
            name="uq_article_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    article_id: uuid.UUID = Field(
        foreign_key="articles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    article: Optional[Article] = Relationship(
        back_populates="tag_links",
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleTagLink.article_id]",
        },
    )

    tag: Optional[Tag] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleTagLink.tag_id]",
        }
    )

class ArticleProgress(SQLModel, table=True):
    __tablename__ = "article_progress"
    __table_args__ = (
        UniqueConstraint(
            "article_id",
            "patient_id",
            name="uq_article_patient_progress",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    article_id: uuid.UUID = Field(
        foreign_key="articles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    # Текущая сохранённая позиция.
    progress_percent: float = Field(default=0.0)

    # Максимально достигнутый прогресс.
    max_progress_percent: float = Field(default=0.0)

    started_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)

    article: Optional[Article] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ArticleProgress.article_id]",
        }
    )

# ./backend/app/modules/articles/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class ArticleCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    content: str = Field(min_length=1)

    tag_ids: list[uuid.UUID] = []

    pro_content: bool = True


class ArticleUpdateRequest(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )
    content: str | None = Field(default=None, min_length=1)

    tag_ids: list[uuid.UUID] | None = None
    pro_content: bool | None = None


class ArticleVisibilityRequest(BaseModel):
    is_hidden: bool


class ArticleTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class ArticleResponse(BaseModel):
    id: uuid.UUID

    title: str
    content: str

    pro_content: bool
    is_hidden: bool

    tags: list[ArticleTagResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    hidden_at: datetime | None


class ArticleListItem(BaseModel):
    id: uuid.UUID
    title: str

    pro_content: bool
    is_hidden: bool
    can_access: bool = True

    tags: list[ArticleTagResponse]

    created_at: datetime
    updated_at: datetime

class ArticleReadResponse(BaseModel):
    message: str
    event_id: uuid.UUID

class ArticleProgressUpdateRequest(BaseModel):
    progress_percent: float = Field(
        ge=0,
        le=100,
    )


class ArticleProgressResponse(BaseModel):
    article_id: uuid.UUID
    patient_id: uuid.UUID

    progress_percent: float
    max_progress_percent: float

    started_at: datetime
    updated_at: datetime
    completed_at: datetime | None

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

# ./backend/app/modules/users/models.py
import uuid
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.users.enums import (
    DoctorPatientStatus,
    Gender,
    RelativePatientStatus,
    UserRole,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UserRoleLink(SQLModel, table=True):
    __tablename__ = "user_role_links"
    __table_args__ = (
        UniqueConstraint("user_id", "role", name="uq_user_role"),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)
    role: UserRole = Field(index=True)
    is_primary: bool = Field(default=False)

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional["User"] = Relationship(back_populates="role_links")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    email: str = Field(unique=True, index=True, max_length=320)
    hashed_password: Optional[str] = Field(default=None)

    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    middle_name: Optional[str] = Field(default=None, max_length=100)
    gender: Optional[Gender] = Field(default=None)

    is_active: bool = Field(default=True, index=True)
    is_blocked: bool = Field(default=False, index=True)
    email_verified_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None, index=True)

    # При смене пароля значение увеличивается, старые JWT становятся невалидными.
    auth_version: int = Field(default=1)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    role_links: list[UserRoleLink] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    doctor_profile: Optional["DoctorProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[DoctorProfile.user_id]",
        },
    )

    patient_profile: Optional["PatientProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[PatientProfile.user_id]",
        },
    )

    relative_profile: Optional["RelativeProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[RelativeProfile.user_id]",
        },
    )

    med_assistant_profile: Optional["MedAssistantProfile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "uselist": False,
            "foreign_keys": "[MedAssistantProfile.user_id]",
        },
    )


class Speciality(SQLModel, table=True):
    __tablename__ = "specialities"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True, max_length=200)
    description: Optional[str] = Field(default=None)

    consultation_name: Optional[str] = Field(
        default=None,
        max_length=300,
    )
    consultation_description: Optional[str] = Field(
        default=None,
    )

    is_hidden: bool = Field(default=False, index=True)
    hidden_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)

    doctors: list["DoctorProfile"] = Relationship(
        back_populates="speciality"
    )


class DoctorProfile(SQLModel, table=True):
    __tablename__ = "doctor_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )
    speciality_id: uuid.UUID = Field(
        foreign_key="specialities.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="doctor_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorProfile.user_id]",
        },
    )

    speciality: Optional[Speciality] = Relationship(back_populates="doctors")

    patient_links: list["DoctorPatientLink"] = Relationship(
        back_populates="doctor",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.doctor_id]",
        },
    )


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


class RelativeProfile(SQLModel, table=True):
    __tablename__ = "relative_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="relative_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativeProfile.user_id]",
        },
    )

    patient_links: list["RelativePatientLink"] = Relationship(
        back_populates="relative",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.relative_id]",
        },
    )


class MedAssistantProfile(SQLModel, table=True):
    __tablename__ = "med_assistant_profiles"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        unique=True,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    user: Optional[User] = Relationship(
        back_populates="med_assistant_profile",
        sa_relationship_kwargs={
            "foreign_keys": "[MedAssistantProfile.user_id]",
        },
    )


class DoctorPatientLink(SQLModel, table=True):
    __tablename__ = "doctor_patient_links"
    __table_args__ = (
        UniqueConstraint(
            "doctor_id",
            "patient_id",
            name="uq_doctor_patient",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doctor_id: uuid.UUID = Field(
        foreign_key="doctor_profiles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    status: DoctorPatientStatus = Field(
        default=DoctorPatientStatus.ACTIVE,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    detached_at: Optional[datetime] = Field(default=None)

    doctor: Optional[DoctorProfile] = Relationship(
        back_populates="patient_links",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.doctor_id]",
        },
    )

    patient: Optional[PatientProfile] = Relationship(
        back_populates="doctor_links",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorPatientLink.patient_id]",
        },
    )


class RelativePatientLink(SQLModel, table=True):
    __tablename__ = "relative_patient_links"
    __table_args__ = (
        UniqueConstraint(
            "relative_id",
            "patient_id",
            name="uq_relative_patient",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    relative_id: uuid.UUID = Field(
        foreign_key="relative_profiles.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    relationship_degree: Optional[str] = Field(default=None, max_length=100)
    status: RelativePatientStatus = Field(
        default=RelativePatientStatus.ACTIVE,
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    detached_at: Optional[datetime] = Field(default=None)

    relative: Optional[RelativeProfile] = Relationship(
        back_populates="patient_links",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.relative_id]",
        },
    )

    patient: Optional[PatientProfile] = Relationship(
        back_populates="relative_links",
        sa_relationship_kwargs={
            "foreign_keys": "[RelativePatientLink.patient_id]",
        },
    )

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
      title: 'MentalConnect',
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
          content:
            'MentalConnect — сервис сопровождения пациентов',
        },
        {
          name: 'theme-color',
          content: '#f4f0eb',
        },
      ],
      link: [
        {
          rel: 'icon',
          type: 'image/x-icon',
          href: '/favicon.ico',
        },
        {
          rel: 'icon',
          type: 'image/png',
          sizes: '32x32',
          href: '/favicon-32x32.png',
        },
        {
          rel: 'icon',
          type: 'image/png',
          sizes: '16x16',
          href: '/favicon-16x16.png',
        },
        {
          rel: 'apple-touch-icon',
          sizes: '180x180',
          href: '/apple-touch-icon.png',
        },
        {
          rel: 'manifest',
          href: '/site.webmanifest',
        },
      ],
    },
  },
})

<!-- ./frontend/app/components/articles/Reader.vue -->
<script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  },
})

const auth = useAuthStore()
const userStore = useUserStore()
const router = useRouter()
const config = useRuntimeConfig()
const { $api } = useNuxtApp()

const articleElement = ref(null)

const savedProgress = ref(0)
const saving = ref(false)
const completed = ref(false)

const {
  progress,
  restoreProgress,
} = useReadingProgress(articleElement)

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canEdit = computed(() => {
  if (
    [
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
  ) {
    return true
  }

  return (
    auth.activeRole === 'doctor'
    && props.article.created_by_user_id
      === userStore.user?.id
  )
})

let saveTimer = null
let lastSentProgress = 0

async function loadProgress() {
  if (!isPatient.value) return

  try {
    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
    )

    savedProgress.value =
      response.progress_percent || 0

    lastSentProgress = savedProgress.value

    completed.value = Boolean(
      response.completed_at,
    )

    await nextTick()

    window.setTimeout(() => {
      restoreProgress(savedProgress.value)
    }, 100)
  } catch {
    // Отсутствие прогресса не должно мешать чтению.
  }
}

async function saveProgress(value = progress.value) {
  if (!isPatient.value || saving.value) return

  saving.value = true

  try {
    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
      {
        method: 'PUT',
        body: {
          progress_percent: value,
        },
      },
    )

    lastSentProgress = value
    savedProgress.value = value
    completed.value = Boolean(
      response.completed_at,
    )
  } finally {
    saving.value = false
  }
}

function scheduleSave() {
  if (!isPatient.value) return

  window.clearTimeout(saveTimer)

  saveTimer = window.setTimeout(() => {
    saveProgress()
  }, 800)
}

function saveWithKeepalive() {
  if (
    !isPatient.value
    || progress.value === lastSentProgress
  ) {
    return
  }

  const token = localStorage.getItem(
    'mentalme_access_token',
  )

  if (!token) return

  fetch(
    `${config.public.apiBase}/api/v1/articles/${props.article.id}/progress`,
    {
      method: 'PUT',
      keepalive: true,
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        progress_percent: progress.value,
      }),
    },
  ).catch(() => {})
}

async function closeReader() {
  window.clearTimeout(saveTimer)

  if (isPatient.value) {
    await saveProgress()
  }

  if (window.history.length > 1) {
    router.back()
  } else {
    await navigateTo('/content/articles')
  }
}

watch(progress, (value) => {
  if (!isPatient.value) return

  if (
    Math.abs(value - lastSentProgress) >= 5
    || value >= 100
  ) {
    scheduleSave()
  }
})

onMounted(() => {
  loadProgress()

  window.addEventListener(
    'pagehide',
    saveWithKeepalive,
  )
})

onBeforeRouteLeave(() => {
  saveWithKeepalive()
})

onBeforeUnmount(() => {
  window.clearTimeout(saveTimer)

  window.removeEventListener(
    'pagehide',
    saveWithKeepalive,
  )
})
</script>

<template>
  <div>
    <progress
      class="progress progress-secondary fixed inset-x-0 top-0 z-[70] h-1 w-full rounded-none"
      :value="progress"
      max="100"
      aria-label="Прогресс чтения статьи"
    />

    <div
      class="fixed right-3 top-3 z-[60] flex items-center gap-2 sm:right-5 sm:top-4"
    >
      <NuxtLink
        v-if="canEdit"
        :to="`/content/articles/${article.id}/edit`"
        class="btn btn-sm btn-primary shadow-lg"
      >
        <Icon
          name="lucide:pencil"
          class="size-4"
        />

        <span class="hidden sm:inline">
          Редактировать
        </span>
      </NuxtLink>

      <button
        type="button"
        class="btn btn-circle btn-sm bg-base-100 shadow-lg"
        aria-label="Закрыть статью"
        @click="closeReader"
      >
        <Icon
          name="lucide:x"
          class="size-5"
        />
      </button>
    </div>

    <article
      ref="articleElement"
      class="bg-base-100 border-base-300 mx-auto max-w-4xl rounded-3xl border p-5 sm:p-8 lg:p-10"
    >
      <div class="mb-5 flex flex-wrap gap-2">
        <span
          v-if="article.pro_content"
          class="badge badge-secondary"
        >
          Pro
        </span>

        <span
          v-for="tag in article.tags"
          :key="tag.id"
          class="badge badge-outline"
        >
          {{ tag.name }}
        </span>
      </div>

      <h1
        class="mb-8 text-3xl font-bold leading-tight sm:text-4xl"
      >
        {{ article.title }}
      </h1>

      <ContentRichTextRenderer
        :content="article.content"
      />

      <div
        class="border-base-300 mt-10 border-t pt-6"
      >
        <div class="flex items-center justify-between gap-4">
          <span class="text-sm font-medium">
            Прочитано {{ progress }}%
          </span>

          <span
            v-if="completed && isPatient"
            class="badge badge-success gap-1"
          >
            <Icon
              name="lucide:check"
              class="size-3"
            />
            Завершено
          </span>
        </div>

        <progress
          class="progress progress-secondary mt-3 w-full"
          :value="progress"
          max="100"
        />
      </div>
    </article>
  </div>
</template>

// ./frontend/app/composables/useReadingProgress.js

export function useReadingProgress(target) {
  const progress = ref(0)

  let animationFrame = null
  let resizeObserver = null

  function getMetrics() {
    const element = target.value

    if (!element) return null

    const rect = element.getBoundingClientRect()

    const elementTop =
      rect.top + window.scrollY

    const elementHeight =
      element.offsetHeight

    const maxPageScroll = Math.max(
      document.documentElement.scrollHeight
        - window.innerHeight,
      0,
    )

    const articleEndScroll =
      elementTop
      + elementHeight
      - window.innerHeight

    const endPosition = Math.min(
      articleEndScroll,
      maxPageScroll,
    )

    const readableHeight = Math.max(
      endPosition - elementTop,
      1,
    )

    return {
      elementTop,
      readableHeight,
      endPosition,
    }
  }

  function calculate() {
    const metrics = getMetrics()

    if (!metrics) return

    const {
      elementTop,
      readableHeight,
      endPosition,
    } = metrics

    const currentPosition =
      window.scrollY - elementTop

    // Важный момент: сначала проверяем начало.
    // Иначе при временно маленькой высоте страницы
    // endPosition может оказаться <= elementTop
    // и мы ошибочно получим 100%.
    if (currentPosition <= 0) {
      progress.value = 0
      return
    }

    if (window.scrollY >= endPosition - 2) {
      progress.value = 100
      return
    }

    progress.value = Math.round(
      Math.min(
        Math.max(
          currentPosition
            / readableHeight
            * 100,
          0,
        ),
        100,
      ),
    )
  }

  function scheduleCalculate() {
    if (animationFrame) return

    animationFrame =
      window.requestAnimationFrame(() => {
        calculate()
        animationFrame = null
      })
  }

  function restoreProgress(percent) {
    if (percent <= 0) return

    const metrics = getMetrics()

    if (!metrics) return

    const {
      elementTop,
      readableHeight,
    } = metrics

    window.scrollTo({
      top:
        elementTop
        + readableHeight
        * Math.min(percent, 100)
        / 100,
      behavior: 'instant',
    })

    // Синхронизируем progress после scrollTo.
    scheduleCalculate()
  }

  onMounted(() => {
    nextTick(() => {
      scheduleCalculate()

      if (target.value) {
        resizeObserver = new ResizeObserver(() => {
          scheduleCalculate()
        })

        resizeObserver.observe(target.value)
      }
    })

    window.addEventListener(
      'scroll',
      scheduleCalculate,
      {
        passive: true,
      },
    )

    window.addEventListener(
      'resize',
      scheduleCalculate,
    )
  })

  onBeforeUnmount(() => {
    window.removeEventListener(
      'scroll',
      scheduleCalculate,
    )

    window.removeEventListener(
      'resize',
      scheduleCalculate,
    )

    resizeObserver?.disconnect()

    if (animationFrame) {
      window.cancelAnimationFrame(
        animationFrame,
      )
    }
  })

  return {
    progress: readonly(progress),
    calculate,
    restoreProgress,
  }
}


я думаю реализовать счетчик прочитанных статей и опросников при помощи этого модуля, но без дополнительных моделей или полей у модуля articles. 

Допустим, статья прочитана на 100%, нужно записать этот в events. При этом, я бы хотел также сделать счетчик кликов по статьям, чтобы затем уже иметь возможность считать что-то типа CPA (Cost Per Action) при показе статей пациенту для более эффективного вовлечения пациентов. Но я не уверен, как лучше организовать этот таким образом, чтобы не раздувать базу данных на таких моментах и чтобы потом можно было быстро и без перегрузки сервера и базы данных получать эти самые счетчики. Я думал, просто сохранять по uuid статьи (если статья новая, то при клике на нее создавать новый event, а затем при посторных кликакх и прочтениях искать по типу event и по uuid статьи). Сохранять uuid читающего, я думаю, что не надо , чтобы не плодить много events с одними и теми же статьями

Если у тебя есть вопросы по функционалу, сначала напиши вопросы. Плюс, напиши, какие файлы тебе прислать, если нужны






















-------------------












1. Что именно считается «показом статьи»? вроде, у меня при чтении статьи (точнее зачитывания до конца там стоит, что тстьая прочитана и надопись 100%) - это надо считать, что прочитана и однократно, то есть, если пользователь в тот же момент оспять пролистнул вверх, а потом вниз, повторно данное событие, разукмеется, не считать

article_impression — карточка реально показана - если это не перегрузит приложение, то давай redis у меня пока нет и у меня mvp. я думал, считать именно открытие статьи и чтение до конца

article_opened — пациент открыл статью - да, это я хочу считать
article_read — статья прочитана - да
article_assigned — статья назначена пациенту - ну, можно на всякий случай, чтобы поптом можно было подтянуть статистику

2. Как считать повторные действия? каждый клик на карточку статьи, я думаю, потому что один пациент может открывать статью несколько раз, плюс у него может, например, быть дела и он не успевает прочитать и потом открывает заново и ,все-таки, дочитать, и т.д.
В рамках чего эта статья открывается, я думаю, не так ванжо... ну давай сделаем, чтобы в рамках программы/самостоятельно просто клик на статью, чтобы потом можно было анализировать эффективность программ

Например, пациент может открыть статью пять раз. В отчёте вы хотите видеть: 5 открытий
Потом другой пациент открыл 4 раза : получается в сумме 9 открытий

3. Что означает «статья прочитана»? - событие создаётся только при первом достижении 100 если в рамках текущего открытия статьи, то один раз. но если пациент открыл статью еще раз (кликнул на карточку статьи), то повторно защитываем
достаточно ли 90 или строго 100 - давай 90 сделаем

должно ли событие создаваться, если статья настолько короткая, что не требует прокрутки - хороший вопрос... в целом я такого не планирую, но давай не будем защитывать такие статьи, а то потом при рекомендациях у меня первыми только и будут, что короткие

можно ли сбрасывать завершение после редактирования статьи? - да, давай не будем сбрасывать. активные редактирования не планируются
Нужна ли версия статьи? - не надо. пока делаем так, как проще и не раздуваем код

4. Какие показатели вы хотите получать?
общее количество показов - а, если ты имеешь ввиду, показ карточки статьи, то я не думаю, что это хорошаая идея, потому что это усложнит код... не надо пока
общее количество открытий -да, сколько раз пациент кликнул на карточку статьи в списке статей
уникальные пациенты, открывшие статью -да, пока нет, наверное. Это требует также регистрировать uuid пользователей, что может перегрузить бекенд. пока не хочу
общее количество прочтений -ну да давай считать 90% и выше
уникальные пациенты, прочитавшие статью - пока не думаю
конверсия из показа в открытие - нет пока не надо
конверсия из открытия в прочтение- да, именно это и хочу. то есть, расчет на основании показов к прочитываниям
средний максимальный прогресс - ну... тут надо будет фиксировать промежуточные проценты, или учитывать сессию, и т.д. ... сложно... не надо 
статистика по дням, неделям и месяцам да, не обязательно пока
статистика по врачу не уверен, что это надо на этапе mvp
статистика по программе а это можно, конечно
статистика по назначению тут тоже не вижу препятствий для анализа
статистика по тегу ну... если это не раздует код
статистика по источнику показа типо программа/прямое открытие? да, можно
воронка конкретного пациента тут не уверен пока пока что, сосредоточимся на показе статей

5. Что вы понимаете под CPA? смотри, я планирую считать что-то, что определяет соотношение открытий статьи к прочитыванию и на основении этого сторить рекомендации.
Планируется так: у пациента есть теги, на основании которых фильтруется контент, например: тревога, артериальная гипертензия, ибс... ему долны  рекомендоваться статьи по артериальной гипертензии/ибс и тревоге (пока сделано только это) но статьи потом надо, чтобы сортировались по индексу (ну, или по количеству дочитываний, я пока не решил... надо тестировать)

Также нужен идентификатор источника: ну, давай сделаем

6. Нужно ли связывать показ, открытие и прочтение одного пациента? а можно ли как-то сделать без сильного раздувания кода и нагрузки на сервер? если да, то конечно, давай сделаем так. Приватность не играет роли, потому что планируется деплой в контуре клиники

7. Какой ожидается объём? - хороший вопрос. Статей планируется ... ну, будем думать, что около 100. Пациентов ... ну пока у меня mvp... пока будем думать, что дай бог 100, но я думаю, если проект пойдет, то 1-2 тыс. открытий статей в сутки да, не очень много пока. обновлений прогресса в сутки ну ,сложно сказать... ожидаемый рост за год да как тебе сказать... хотелось бы, конечно большого роста... но это проект в частной клинике без внешней регистрации (пока). максимальный срок хранения событий пока механизм удаления не проработан, поэтому я и не хъочу раздувать базу, плюс пока не делаю redis.

8. Насколько быстро должны обновляться счётчики? задержка некритична. точность  тоже не обязатлеьно должна быть сильной

9. Кто будет видеть аналитику?: давай сделаем, чтобы SUPERUSER и медицинский ассистент видели статистику по всем пациентам, а каждый врач только по своим пациентам но это, если ты решишь, что регистрация событий по укникальным пациентам целесообразна к моим нуждам. Если регаистрировать будем просто счетчиками, то давай сделаем, чтобы SUPERUSER и медицинский ассистент могли видеть активность у карточек статей, а все остальные - нет, но сортировка у пациентов учитвала этот показатель

10. Как считать опросники? - пока делаем только для статей








-------------

































1. Что именно считается «показом статьи»? вроде, у меня при чтении статьи (точнее зачитывания до конца там стоит, что тстьая прочитана и надопись 100%) - это надо считать, что прочитана и однократно, то есть, если пользователь в тот же момент оспять пролистнул вверх, а потом вниз, повторно данное событие, разукмеется, не считать

article_impression — карточка реально показана - если это не перегрузит приложение, то давай redis у меня пока нет и у меня mvp. я думал, считать именно открытие статьи и чтение до конца

article_opened — пациент открыл статью - да, это я хочу считать
article_read — статья прочитана - да
article_assigned — статья назначена пациенту - ну, можно на всякий случай, чтобы поптом можно было подтянуть статистику

2. Как считать повторные действия? каждый клик на карточку статьи, я думаю, потому что один пациент может открывать статью несколько раз, плюс у него может, например, быть дела и он не успевает прочитать и потом открывает заново и ,все-таки, дочитать, и т.д.
В рамках чего эта статья открывается, я думаю, не так ванжо... ну давай сделаем, чтобы в рамках программы/самостоятельно просто клик на статью, чтобы потом можно было анализировать эффективность программ

Например, пациент может открыть статью пять раз. В отчёте вы хотите видеть: 5 открытий
Потом другой пациент открыл 4 раза : получается в сумме 9 открытий

3. Что означает «статья прочитана»? - событие создаётся только при первом достижении 100 если в рамках текущего открытия статьи, то один раз. но если пациент открыл статью еще раз (кликнул на карточку статьи), то повторно защитываем
достаточно ли 90 или строго 100 - давай 90 сделаем

должно ли событие создаваться, если статья настолько короткая, что не требует прокрутки - хороший вопрос... в целом я такого не планирую, но давай не будем защитывать такие статьи, а то потом при рекомендациях у меня первыми только и будут, что короткие

можно ли сбрасывать завершение после редактирования статьи? - да, давай не будем сбрасывать. активные редактирования не планируются
Нужна ли версия статьи? - не надо. пока делаем так, как проще и не раздуваем код

4. Какие показатели вы хотите получать?
общее количество показов - а, если ты имеешь ввиду, показ карточки статьи, то я не думаю, что это хорошаая идея, потому что это усложнит код... не надо пока
общее количество открытий -да, сколько раз пациент кликнул на карточку статьи в списке статей
уникальные пациенты, открывшие статью -да, пока нет, наверное. Это требует также регистрировать uuid пользователей, что может перегрузить бекенд. пока не хочу
общее количество прочтений -ну да давай считать 90% и выше
уникальные пациенты, прочитавшие статью - пока не думаю
конверсия из показа в открытие - нет пока не надо
конверсия из открытия в прочтение- да, именно это и хочу. то есть, расчет на основании показов к прочитываниям
средний максимальный прогресс - ну... тут надо будет фиксировать промежуточные проценты, или учитывать сессию, и т.д. ... сложно... не надо 
статистика по дням, неделям и месяцам да, не обязательно пока
статистика по врачу не уверен, что это надо на этапе mvp
статистика по программе а это можно, конечно
статистика по назначению тут тоже не вижу препятствий для анализа
статистика по тегу ну... если это не раздует код
статистика по источнику показа типо программа/прямое открытие? да, можно
воронка конкретного пациента тут не уверен пока пока что, сосредоточимся на показе статей

5. Что вы понимаете под CPA? смотри, я планирую считать что-то, что определяет соотношение открытий статьи к прочитыванию и на основении этого сторить рекомендации.
Планируется так: у пациента есть теги, на основании которых фильтруется контент, например: тревога, артериальная гипертензия, ибс... ему долны  рекомендоваться статьи по артериальной гипертензии/ибс и тревоге (пока сделано только это) но статьи потом надо, чтобы сортировались по индексу (ну, или по количеству дочитываний, я пока не решил... надо тестировать)

Также нужен идентификатор источника: ну, давай сделаем

6. Нужно ли связывать показ, открытие и прочтение одного пациента? а можно ли как-то сделать без сильного раздувания кода и нагрузки на сервер? если да, то конечно, давай сделаем так. Приватность не играет роли, потому что планируется деплой в контуре клиники

7. Какой ожидается объём? - хороший вопрос. Статей планируется ... ну, будем думать, что около 100. Пациентов ... ну пока у меня mvp... пока будем думать, что дай бог 100, но я думаю, если проект пойдет, то 1-2 тыс. открытий статей в сутки да, не очень много пока. обновлений прогресса в сутки ну ,сложно сказать... ожидаемый рост за год да как тебе сказать... хотелось бы, конечно большого роста... но это проект в частной клинике без внешней регистрации (пока). максимальный срок хранения событий пока механизм удаления не проработан, поэтому я и не хъочу раздувать базу, плюс пока не делаю redis.

8. Насколько быстро должны обновляться счётчики? задержка некритична. точность  тоже не обязатлеьно должна быть сильной

9. Кто будет видеть аналитику?: давай сделаем, чтобы SUPERUSER и медицинский ассистент видели статистику по всем пациентам, а каждый врач только по своим пациентам но это, если ты решишь, что регистрация событий по укникальным пациентам целесообразна к моим нуждам. Если регаистрировать будем просто счетчиками, то давай сделаем, чтобы SUPERUSER и медицинский ассистент могли видеть активность у карточек статей, а все остальные - нет, но сортировка у пациентов учитвала этот показатель

10. Как считать опросники? - пока делаем только для статей

# ./backend/app/core/db.py
import os
from collections.abc import Generator
from pathlib import Path

from sqlalchemy.engine import make_url
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


BACKEND_DIR = Path(__file__).resolve().parents[2]


def resolve_database_url(database_url: str) -> str:
    if not database_url.startswith("sqlite"):
        return database_url

    url = make_url(database_url)
    database = url.database

    if not database or database == ":memory:":
        return database_url

    database_path = Path(database)

    if not database_path.is_absolute():
        database_path = (BACKEND_DIR / database_path).resolve()

    return f"sqlite:///{database_path.as_posix()}"


DATABASE_URL = resolve_database_url(settings.DATABASE_URL)

connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine_kwargs = {
    "echo": False,
    "connect_args": connect_args,
    "pool_pre_ping": True,
}

if not DATABASE_URL.startswith("sqlite"):
    engine_kwargs.update({
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 1800,
    })

sqlite_engine = create_engine(
    DATABASE_URL,
    **engine_kwargs,
)


def get_db_path() -> str | None:
    if not DATABASE_URL.startswith("sqlite"):
        return None

    url = make_url(DATABASE_URL)

    if not url.database or url.database == ":memory:":
        return None

    return str(Path(url.database).resolve())


def import_all_models() -> None:
    # Базовые модели.
    from app.modules.users import models as user_models  # noqa: F401
    from app.modules.auth import models as auth_models  # noqa: F401
    from app.modules.invitations import models as invitation_models  # noqa: F401
    from app.modules.tags import models as tag_models  # noqa: F401

    # Контент сначала импортируется от простого к составному.
    from app.modules.articles import models as article_models  # noqa: F401
    from app.modules.questionnaires import models as questionnaire_models  # noqa: F401
    from app.modules.services import models as service_models  # noqa: F401
    from app.modules.programs import models as program_models  # noqa: F401

    # Клинический и аналитический маршрут.
    from app.modules.referrals import models as referral_models  # noqa: F401
    from app.modules.events import models as event_models  # noqa: F401
    from app.modules.consents import models as consent_models  # noqa: F401

    from app.modules.notifications import models as notification_models  # noqa: F401
    from app.modules.assignments import models as assignment_models  # noqa: F401


def init_sqlite_db() -> None:
    """
    Инициализация базы данных.

    Если SQLite-файл существует, создаются только недостающие таблицы.
    Если файл отсутствует, он будет создан автоматически.
    """
    import_all_models()

    db_path = get_db_path()

    if db_path is None:
        SQLModel.metadata.create_all(sqlite_engine)
        print("✓ Database tables synchronized")
        return

    parent_directory = os.path.dirname(db_path)

    if parent_directory:
        os.makedirs(parent_directory, exist_ok=True)

    if os.path.exists(db_path):
        print(f"📁 Database file already exists: {db_path}")
        print("   Checking for missing tables...")
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Tables synchronized")
    else:
        print(f"📁 Creating new database: {db_path}")
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Database created")


def get_session() -> Generator[Session, None, None]:
    with Session(sqlite_engine) as session:
        yield session

файл с миграциями огромный. тебе не хватит только отдельных полей?
op.create_table('events',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_type', postgresql.ENUM('REFERRAL_CREATED', 'LINK_SENT', 'LINK_OPENED', 'REGISTRATION_COMPLETED', 'CONSENT_GIVEN', 'QUESTIONNAIRE_STARTED', 'QUESTIONNAIRE_COMPLETED', 'ARTICLE_READ', 'CONTACT_REQUESTED', 'ASSISTANT_CALL_ATTEMPTED', 'ASSISTANT_CONTACTED', 'APPOINTMENT_BOOKED', 'APPOINTMENT_ATTENDED', 'PACKAGE_OFFERED', 'PAYMENT_LINK_SENT', 'PACKAGE_PURCHASED', 'REFUND_CREATED', 'PROGRAM_STARTED', 'PROGRAM_COMPLETED', 'PROGRAM_IN_PROGRESS', name='eventtype', create_type=False), nullable=False),
op.create_index(op.f('ix_events_actor_user_id'), 'events', ['actor_user_id'], unique=False)
op.create_index(op.f('ix_events_actor_user_id'), 'events', ['actor_user_id'], unique=False)
    op.create_index(op.f('ix_events_doctor_id'), 'events', ['doctor_id'], unique=False)
    op.create_index(op.f('ix_events_event_type'), 'events', ['event_type'], unique=False)
    op.create_index(op.f('ix_events_occurred_at'), 'events', ['occurred_at'], unique=False)
    op.create_index(op.f('ix_events_patient_id'), 'events', ['patient_id'], unique=False)
    op.create_index(op.f('ix_events_product_id'), 'events', ['product_id'], unique=False)
    op.create_index(op.f('ix_events_program_id'), 'events', ['program_id'], unique=False)
    op.create_index(op.f('ix_events_referral_id'), 'events', ['referral_id'], unique=False)
    op.create_index(op.f('ix_events_speciality_id'), 'events', ['speciality_id'], unique=False)
    op.create_index(op.f('ix_events_subject_id'), 'events', ['subject_id'], unique=False)
    op.create_index(op.f('ix_events_subject_type'), 'events', ['subject_type'], unique=False)





```plaintext
# ./backend/app/modules/articles/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import (
    AuthContext,
    get_current_auth,
    require_roles,
)
from app.modules.articles.models import (
    Article,
    ArticleProgress,
)
from app.modules.articles.schemas import (
    ArticleCreateRequest,
    ArticleListItem,
    ArticleProgressResponse,
    ArticleProgressUpdateRequest,
    ArticleReadResponse,
    ArticleResponse,
    ArticleUpdateRequest,
    ArticleVisibilityRequest,
)
from app.modules.articles.utils import (
    get_article_tag_ids,
    replace_article_tags,
    serialize_article,
    serialize_article_list_item,
)
from app.modules.content.utils import (
    ensure_patient_content_access,
    get_patient_profile_by_user_id,
    patient_can_access_content,
    patient_can_see_content,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.users.enums import UserRole

from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import (
    mark_assignment_completed,
    patient_has_active_assignment,
)
from app.modules.programs.utils import (
    sync_patient_program_enrollments,
)

router = APIRouter(
    prefix="/api/v1/articles",
    tags=["Articles"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    articles = session.exec(
        select(Article).order_by(
            Article.created_at.desc()
        )
    ).all()

    if auth.active_role != UserRole.PATIENT:
        return [
            serialize_article_list_item(
                session=session,
                article=article,
            )
            for article in articles
        ]

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    result: list[ArticleListItem] = []

    for article in articles:
        # Скрытые статьи не показываются даже в случае
        # активного назначения.
        if article.is_hidden:
            continue

        tag_ids = get_article_tag_ids(
            session=session,
            article_id=article.id,
        )

        is_assigned = patient_has_active_assignment(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        # Назначенная статья доступна независимо
        # от тегов пациента.
        if (
            not is_assigned
            and not patient_can_see_content(
                session=session,
                patient=patient,
                content_tag_ids=tag_ids,
                is_hidden=article.is_hidden,
            )
        ):
            continue

        # Назначение также даёт доступ к Pro-контенту
        # независимо от статуса Pro пациента.
        can_access = (
            is_assigned
            or not article.pro_content
            or patient.pro_enabled
        )

        result.append(
            serialize_article_list_item(
                session=session,
                article=article,
                can_access=can_access,
            )
        )

    return result


@router.get(
    "/{article_id}",
    response_model=ArticleResponse,
)
async def get_article(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    if auth.active_role == UserRole.PATIENT:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        is_assigned = patient_has_active_assignment(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        # Скрытие имеет приоритет над назначением.
        if article.is_hidden:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Статья скрыта",
            )

        if not is_assigned:
            ensure_patient_content_access(
                session=session,
                patient=patient,
                content_tag_ids=get_article_tag_ids(
                    session=session,
                    article_id=article.id,
                ),
                pro_content=article.pro_content,
                is_hidden=article.is_hidden,
            )

    return serialize_article(
        session=session,
        article=article,
    )


@router.post(
    "",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_article(
    payload: ArticleCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = Article(
        title=payload.title.strip(),
        content=payload.content,
        pro_content=payload.pro_content,
        created_by_user_id=auth.user.id,
    )

    session.add(article)
    session.flush()

    replace_article_tags(
        session=session,
        article=article,
        tag_ids=payload.tag_ids,
    )

    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


@router.patch(
    "/{article_id}",
    response_model=ArticleResponse,
)
async def update_article(
    article_id: uuid.UUID,
    payload: ArticleUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if (
        auth.active_role == UserRole.DOCTOR
        and article.created_by_user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Врач может редактировать только "
                "созданные им статьи"
            ),
        )

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )
    tag_ids = update_data.pop("tag_ids", None)

    if "title" in update_data:
        update_data["title"] = (
            update_data["title"].strip()
        )

    for field_name, value in update_data.items():
        setattr(article, field_name, value)

    if tag_ids is not None:
        replace_article_tags(
            session=session,
            article=article,
            tag_ids=tag_ids,
        )

    article.updated_at = utc_now()

    session.add(article)
    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


@router.patch(
    "/{article_id}/visibility",
    response_model=ArticleResponse,
)
async def change_article_visibility(
    article_id: uuid.UUID,
    payload: ArticleVisibilityRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if (
        auth.active_role == UserRole.DOCTOR
        and article.created_by_user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Врач может редактировать только "
                "созданные им статьи"
            ),
        )

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    article.is_hidden = payload.is_hidden
    article.hidden_at = (
        utc_now()
        if payload.is_hidden
        else None
    )
    article.updated_at = utc_now()

    session.add(article)
    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


@router.post(
    "/{article_id}/read",
    response_model=ArticleReadResponse,
)
async def mark_article_as_read(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleReadResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    ensure_patient_content_access(
        session=session,
        patient=patient,
        content_tag_ids=get_article_tag_ids(
            session=session,
            article_id=article.id,
        ),
        pro_content=article.pro_content,
        is_hidden=article.is_hidden,
    )

    event = record_event(
        session=session,
        event_type=EventType.ARTICLE_READ,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        subject_type="article",
        subject_id=article.id,
    )

    session.commit()
    session.refresh(event)

    return ArticleReadResponse(
        message="Чтение статьи зарегистрировано",
        event_id=event.id,
    )

@router.get(
    "/{article_id}/progress",
    response_model=ArticleProgressResponse,
)
async def get_article_progress(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleProgressResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if not is_assigned:
        ensure_patient_content_access(
            session=session,
            patient=patient,
            content_tag_ids=get_article_tag_ids(
                session=session,
                article_id=article.id,
            ),
            pro_content=article.pro_content,
            is_hidden=article.is_hidden,
        )

    progress = session.exec(
        select(ArticleProgress).where(
            ArticleProgress.article_id == article.id,
            ArticleProgress.patient_id == patient.id,
        )
    ).first()

    if not progress:
        now = utc_now()

        return ArticleProgressResponse(
            article_id=article.id,
            patient_id=patient.id,
            progress_percent=0,
            max_progress_percent=0,
            started_at=now,
            updated_at=now,
            completed_at=None,
        )

    return ArticleProgressResponse(
        article_id=progress.article_id,
        patient_id=progress.patient_id,
        progress_percent=(
            progress.progress_percent
        ),
        max_progress_percent=(
            progress.max_progress_percent
        ),
        started_at=progress.started_at,
        updated_at=progress.updated_at,
        completed_at=progress.completed_at,
    )


@router.put(
    "/{article_id}/progress",
    response_model=ArticleProgressResponse,
)
async def save_article_progress(
    article_id: uuid.UUID,
    payload: ArticleProgressUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleProgressResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if not is_assigned:
        ensure_patient_content_access(
            session=session,
            patient=patient,
            content_tag_ids=get_article_tag_ids(
                session=session,
                article_id=article.id,
            ),
            pro_content=article.pro_content,
            is_hidden=article.is_hidden,
        )

    progress = session.exec(
        select(ArticleProgress).where(
            ArticleProgress.article_id == article.id,
            ArticleProgress.patient_id == patient.id,
        )
    ).first()

    now = utc_now()

    normalized_percent = round(
        min(
            max(payload.progress_percent, 0),
            100,
        ),
        2,
    )

    if not progress:
        progress = ArticleProgress(
            article_id=article.id,
            patient_id=patient.id,
        )

    was_completed = (
        progress.completed_at is not None
    )

    progress.progress_percent = (
        normalized_percent
    )

    progress.max_progress_percent = max(
        progress.max_progress_percent,
        normalized_percent,
    )

    progress.updated_at = now

    if (
        progress.max_progress_percent >= 100
        and progress.completed_at is None
    ):
        progress.completed_at = now

    session.add(progress)
    session.flush()

    # Событие создаётся только один раз
    # при первом достижении 100%.
    if (
        not was_completed
        and progress.completed_at is not None
    ):
        record_event(
            session=session,
            event_type=EventType.ARTICLE_READ,
            patient_id=patient.id,
            actor_user_id=auth.user.id,
            subject_type="article",
            subject_id=article.id,
            metadata={
                "progress_percent": 100,
            },
        )

    # При достижении 100% завершаем
    # активное назначение статьи.
    if progress.completed_at is not None:
        mark_assignment_completed(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        # Синхронизируем программы пациента,
        # в которые входит эта статья.
        sync_patient_program_enrollments(
            session=session,
            patient_id=patient.id,
        )

    session.commit()
    session.refresh(progress)

    return ArticleProgressResponse(
        article_id=progress.article_id,
        patient_id=progress.patient_id,
        progress_percent=(
            progress.progress_percent
        ),
        max_progress_percent=(
            progress.max_progress_percent
        ),
        started_at=progress.started_at,
        updated_at=progress.updated_at,
        completed_at=progress.completed_at,
    )
```