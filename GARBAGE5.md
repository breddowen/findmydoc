У меня такой проект:

## Backend

```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (29 lines)
backend/alembic/versions/4a9d77a6cc23_initial_schema.py (887 lines)
backend/alembic/versions/6042112705c7_article_analytics_events.py (487 lines)
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
backend/app/modules/articles/routers.py (1032 lines)
backend/app/modules/articles/schemas.py (128 lines)
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
backend/app/modules/events/enums.py (34 lines)
backend/app/modules/events/models.py (116 lines)
backend/app/modules/events/routers.py (69 lines)
backend/app/modules/events/schemas.py (32 lines)
backend/app/modules/events/service.py (60 lines)
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
backend/test_database.db (?)
```

*Files: 123*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (203 lines)
frontend/app/components/articles/Form.vue (233 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (321 lines)
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
*Files: 59*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (103 lines)
frontend/app/pages/content/articles/index.vue (186 lines)
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
frontend/app/composables/useReadingProgress.js (203 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 7*

### stores

```
frontend/app/stores/articles.js (159 lines)
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




--------------------
--------------------



# ./backend/app/modules/events/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, JSON, UniqueConstraint
from sqlmodel import Field, SQLModel

from app.modules.events.enums import EventType


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Event(SQLModel, table=True):
    __tablename__ = "events"
    __table_args__ = (
        UniqueConstraint(
            "event_type",
            "interaction_id",
            name="uq_event_type_interaction",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

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

    assignment_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="content_assignments.id",
        index=True,
    )

    # Один UUID на одно открытие страницы статьи.
    # ARTICLE_OPENED и ARTICLE_READ получают одинаковый UUID.
    interaction_id: Optional[uuid.UUID] = Field(
        default=None,
        index=True,
    )

    # library, program, assignment, direct.
    source: Optional[str] = Field(
        default=None,
        max_length=50,
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

    created_at: datetime = Field(
        default_factory=utc_now,
    )

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
    assignment_id: uuid.UUID | None = None,
    interaction_id: uuid.UUID | None = None,
    source: str | None = None,
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
        assignment_id=assignment_id,
        interaction_id=interaction_id,
        source=source,
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

# ./backend/app/modules/articles/utils.py
import uuid

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.articles.models import (
    Article,
    ArticleTagLink,
)
from app.modules.articles.schemas import (
    ArticleListItem,
    ArticleResponse,
    ArticleTagResponse,
)
from app.modules.tags.models import Tag


def get_article_tag_ids(
    *,
    session: Session,
    article_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_article_tags(
    *,
    session: Session,
    article_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article_id
        )
    ).all()

    tags: list[Tag] = []

    for link in links:
        tag = session.get(Tag, link.tag_id)

        if tag:
            tags.append(tag)

    return sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )


def validate_tag_ids(
    *,
    session: Session,
    tag_ids: list[uuid.UUID],
) -> list[Tag]:
    unique_tag_ids = list(dict.fromkeys(tag_ids))
    tags: list[Tag] = []

    for tag_id in unique_tag_ids:
        tag = session.get(Tag, tag_id)

        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Тег {tag_id} не найден",
            )

        tags.append(tag)

    return tags


def replace_article_tags(
    *,
    session: Session,
    article: Article,
    tag_ids: list[uuid.UUID],
) -> None:
    unique_tag_ids = list(
        dict.fromkeys(tag_ids)
    )

    validate_tag_ids(
        session=session,
        tag_ids=unique_tag_ids,
    )

    old_links = session.exec(
        select(ArticleTagLink).where(
            ArticleTagLink.article_id == article.id
        )
    ).all()

    old_by_tag_id = {
        link.tag_id: link
        for link in old_links
    }

    old_tag_ids = set(old_by_tag_id)
    new_tag_ids = set(unique_tag_ids)

    # Удаляем только те связи, которых
    # больше нет в payload.
    for tag_id in old_tag_ids - new_tag_ids:
        session.delete(
            old_by_tag_id[tag_id]
        )

    # Добавляем только действительно новые.
    for tag_id in new_tag_ids - old_tag_ids:
        session.add(
            ArticleTagLink(
                article_id=article.id,
                tag_id=tag_id,
            )
        )


def serialize_article(
    *,
    session: Session,
    article: Article,
) -> ArticleResponse:
    tags = get_article_tags(
        session=session,
        article_id=article.id,
    )

    return ArticleResponse(
        id=article.id,
        title=article.title,
        content=article.content,
        pro_content=article.pro_content,
        is_hidden=article.is_hidden,
        tags=[
            ArticleTagResponse(
                id=tag.id,
                name=tag.name,
                description=tag.description,
            )
            for tag in tags
        ],
        created_by_user_id=article.created_by_user_id,
        created_at=article.created_at,
        updated_at=article.updated_at,
        hidden_at=article.hidden_at,
    )


def serialize_article_list_item(
    *,
    session: Session,
    article: Article,
    can_access: bool = True,
) -> ArticleListItem:
    full_response = serialize_article(
        session=session,
        article=article,
    )

    return ArticleListItem(
        id=full_response.id,
        title=full_response.title,
        pro_content=full_response.pro_content,
        is_hidden=full_response.is_hidden,
        can_access=can_access,
        tags=full_response.tags,
        created_at=full_response.created_at,
        updated_at=full_response.updated_at,
    )

# ./backend/app/modules/articles/routers.py
тут очень больше 1000 строк кода, высылаю фрагменты
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from app.modules.events.models import Event

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
    ArticleOpenRequest,
    ArticleOpenResponse,
    ArticleProgressUpdateRequest,

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
# ============================================================
# НАСТРОЙКА ФИЛЬТРАЦИИ СТАТЕЙ ДЛЯ ПАЦИЕНТОВ
#
# False:
#   пациент видит все нескрытые статьи;
#   подходящие по тегам статьи находятся выше.
#
# True:
#   пациент видит только статьи по своим тегам
#   либо статьи с активным назначением.
# ============================================================
STRICT_PATIENT_ARTICLE_TAG_FILTER = False

ARTICLE_COMPLETION_THRESHOLD = 90.0
MIN_TRACKABLE_SCROLL_DISTANCE = 240

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def get_article_event_counts(
    *,
    session: Session,
    before: datetime | None = None,
) -> dict[uuid.UUID, dict[str, int]]:
    statement = (
        select(
            Event.subject_id,
            Event.event_type,
            func.count(Event.id),
        )
        .where(
            Event.subject_type == "article",
            Event.subject_id.is_not(None),
            Event.event_type.in_(
                [
                    EventType.ARTICLE_OPENED,
                    EventType.ARTICLE_READ,
                ]
            ),
        )
    )

    if before is not None:
        statement = statement.where(
            Event.occurred_at < before
        )

    statement = statement.group_by(
        Event.subject_id,
        Event.event_type,
    )

    result: dict[uuid.UUID, dict[str, int]] = {}

    for subject_id, event_type, count in session.exec(
        statement
    ).all():
        if subject_id not in result:
            result[subject_id] = {
                "opened": 0,
                "read": 0,
            }

        if event_type == EventType.ARTICLE_OPENED:
            result[subject_id]["opened"] = count
        elif event_type == EventType.ARTICLE_READ:
            result[subject_id]["read"] = count

    return result


def calculate_article_score(
    *,
    opened_count: int,
    read_count: int,
) -> float:
    """
    Сглаженный рейтинг.

    Новая статья с одним открытием и одним прочтением
    не должна сразу обгонять статью с большой статистикой.
    """
    if opened_count <= 0:
        return 0.0

    # Сглаживание с условным предварительным значением 50%
    # и весом 10 открытий.
    return (
        read_count + 5
    ) / (
        opened_count + 10
    )


def ensure_patient_can_access_article(
    *,
    article: Article,
    patient,
    is_assigned: bool,
) -> None:
    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if (
        article.pro_content
        and not patient.pro_enabled
        and not is_assigned
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Требуется Pro-доступ",
        )
    
@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    articles = session.exec(
        select(Article).order_by(
            Article.created_at.desc()
        )
    ).all()

    now = datetime.now(timezone.utc)

    ranking_cutoff = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    # Актуальные счётчики для суперпользователя
    # и медицинского ассистента.
    live_event_counts = get_article_event_counts(
        session=session,
    )

    # Стабильные в течение дня счётчики,
    # используемые только для ранжирования
    # списка пациента.
    ranking_event_counts = get_article_event_counts(
        session=session,
        before=ranking_cutoff,
    )

    event_counts = get_article_event_counts(
        session=session,
        before=ranking_cutoff,
    )

    if auth.active_role != UserRole.PATIENT:
        result: list[ArticleListItem] = []

        can_see_analytics = auth.active_role in {
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        }

        for article in articles:
            item = serialize_article_list_item(
                session=session,
                article=article,
            )

            if can_see_analytics:
                counts = live_event_counts.get(
                    article.id,
                    {
                        "opened": 0,
                        "read": 0,
                    },
                )

                opened_count = counts["opened"]
                read_count = counts["read"]

                item.opened_count = opened_count
                item.read_count = read_count
                item.read_rate = round(
                    (
                        read_count
                        / opened_count
                        * 100
                    )
                    if opened_count > 0
                    else 0,
                    2,
                )

            result.append(item)

        return result[offset:offset + limit]

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    ranked_articles: list[
        tuple[
            bool,
            bool,
            float,
            datetime,
            ArticleListItem,
        ]
    ] = []

    for article in articles:
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

        matches_patient_tags = (
            patient_can_see_content(
                session=session,
                patient=patient,
                content_tag_ids=tag_ids,
                is_hidden=False,
            )
        )

        # ====================================================
        # МЕСТО СТРОГОЙ ФИЛЬТРАЦИИ СТАТЕЙ ПО ТЕГАМ
        # ====================================================
        if (
            STRICT_PATIENT_ARTICLE_TAG_FILTER
            and not is_assigned
            and not matches_patient_tags
        ):
            continue

        # Теги больше не запрещают чтение.
        # Они используются только для ранжирования.
        can_access = (
            is_assigned
            or not article.pro_content
            or patient.pro_enabled
        )

        counts = ranking_event_counts.get(
            article.id,
            {
                "opened": 0,
                "read": 0,
            },
        )

        score = calculate_article_score(
            opened_count=counts["opened"],
            read_count=counts["read"],
        )

        item = serialize_article_list_item(
            session=session,
            article=article,
            can_access=can_access,
        )

        ranked_articles.append(
            (
                is_assigned,
                matches_patient_tags,
                score,
                article.created_at,
                item,
            )
        )

    ranked_articles.sort(
        key=lambda row: (
            row[0],  # Назначенные.
            row[1],  # Подходящие по тегам.
            row[2],  # Эффективность статьи.
            row[3],  # Более новые.
        ),
        reverse=True,
    )

    items = [
        row[4]
        for row in ranked_articles
    ]

    return items[offset:offset + limit]
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

    progress.progress_percent = normalized_percent

    progress.max_progress_percent = max(
        progress.max_progress_percent,
        normalized_percent,
    )

    progress.updated_at = now

    # Статья считается прочитанной при достижении
    # порога завершения (например, 90%).
    if (
        progress.max_progress_percent
        >= ARTICLE_COMPLETION_THRESHOLD
        and progress.completed_at is None
    ):
        progress.completed_at = now

    session.add(progress)
    session.flush()

    # ARTICLE_READ создаётся отдельно для каждого
    # trackable-открытия статьи при достижении порога.
    should_register_read = (
        normalized_percent
        >= ARTICLE_COMPLETION_THRESHOLD
        and payload.is_trackable
        and payload.interaction_id is not None
    )

    if should_register_read:
        opening_event = session.exec(
            select(Event).where(
                Event.event_type
                == EventType.ARTICLE_OPENED,
                Event.interaction_id
                == payload.interaction_id,
                Event.patient_id
                == patient.id,
                Event.subject_type
                == "article",
                Event.subject_id
                == article.id,
            )
        ).first()

        if opening_event:
            existing_read_event = session.exec(
                select(Event).where(
                    Event.event_type
                    == EventType.ARTICLE_READ,
                    Event.interaction_id
                    == payload.interaction_id,
                )
            ).first()

            if not existing_read_event:
                record_event(
                    session=session,
                    event_type=EventType.ARTICLE_READ,
                    patient_id=patient.id,
                    actor_user_id=auth.user.id,
                    program_id=opening_event.program_id,
                    assignment_id=opening_event.assignment_id,
                    interaction_id=payload.interaction_id,
                    source=opening_event.source,
                    subject_type="article",
                    subject_id=article.id,
                    metadata={
                        "progress_percent": (
                            normalized_percent
                        ),
                    },
                )

    # completed_at — пожизненное состояние пациента.
    # При первом достижении порога завершаем активное
    # назначение и синхронизируем программы.
    if progress.completed_at is not None:
        mark_assignment_completed(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

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

@router.post(
    "/{article_id}/open",
    response_model=ArticleOpenResponse,
)
async def register_article_open(
    article_id: uuid.UUID,
    payload: ArticleOpenRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleOpenResponse:
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

    ensure_patient_can_access_article(
        article=article,
        patient=patient,
        is_assigned=is_assigned,
    )

    existing_event = session.exec(
        select(Event).where(
            Event.event_type
            == EventType.ARTICLE_OPENED,
            Event.interaction_id
            == payload.interaction_id,
        )
    ).first()

    if existing_event:
        if (
            existing_event.patient_id != patient.id
            or existing_event.subject_id != article.id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Идентификатор открытия уже "
                    "используется"
                ),
            )

        return ArticleOpenResponse(
            event_id=existing_event.id,
            interaction_id=payload.interaction_id,
        )

    event = record_event(
        session=session,
        event_type=EventType.ARTICLE_OPENED,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        program_id=payload.program_id,
        assignment_id=payload.assignment_id,
        interaction_id=payload.interaction_id,
        source=payload.source,
        subject_type="article",
        subject_id=article.id,
    )

    session.commit()
    session.refresh(event)

    return ArticleOpenResponse(
        event_id=event.id,
        interaction_id=payload.interaction_id,
    )

Фронтенд:
// frontend\package.json
{
  "name": "frontend",
  "type": "module",
  "private": true,
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "nuxt prepare"
  },
  "dependencies": {
    "@nuxt/icon": "^2.5.0",
    "@pinia/nuxt": "^1.0.2",
    "@tailwindcss/vite": "^4.3.3",
    "@tiptap/extension-link": "^3.30.3",
    "@tiptap/extension-placeholder": "^3.30.3",
    "@tiptap/extension-underline": "^3.30.3",
    "@tiptap/starter-kit": "^3.30.3",
    "@tiptap/vue-3": "^3.30.3",
    "daisyui": "^5.7.21",
    "dompurify": "^3.4.14",
    "nuxt": "^4.5.2",
    "pinia": "^4.0.3",
    "qrcode": "^1.5.4",
    "tailwindcss": "^4.3.3",
    "vue": "^3.5.41",
    "vue-draggable-plus": "^0.6.1",
    "vue-router": "^5.2.0"
  },
  "devDependencies": {
    "@iconify-json/lucide": "^1.2.125"
  }
}
<!-- frontend\app\pages\index.vue -->
<template>
  <div>Home</div>
</template>

<!-- ./frontend/app/pages/content/articles/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useArticlesStore()

const errorMessage = ref('')
const loadMoreElement = ref(null)

let observer = null

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

const canViewAnalytics = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

async function toggleVisibility(article) {
  errorMessage.value = ''

  try {
    await store.setVisibility(
      article.id,
      !article.is_hidden,
    )

    await store.fetchArticles({
      reset: true,
      limit: 5,
    })
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить видимость'
  }
}

async function loadInitialArticles() {
  await store.fetchArticles({
    reset: true,
    limit: 5,
  })
}

async function loadMoreArticles() {
  if (
    store.loading
    || !store.hasMore
  ) {
    return
  }

  await store.fetchArticles({
    limit: 10,
  })
}

onMounted(async () => {
  await loadInitialArticles()

  observer = new IntersectionObserver(
    entries => {
      if (entries[0]?.isIntersecting) {
        loadMoreArticles()
      }
    },
    {
      rootMargin: '300px',
    },
  )

  if (loadMoreElement.value) {
    observer.observe(
      loadMoreElement.value,
    )
  }
})

onBeforeUnmount(() => {
  observer?.disconnect()
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Статьи
        </h1>

        <p class="text-base-content/60 mt-1">
          Материалы для пациентов.
        </p>
      </div>
      <ClientOnly>
        <NuxtLink
          v-if="canManage"
          to="/content/articles/new"
          class="btn btn-primary"
        >
          <Icon
            name="lucide:plus"
            class="size-4"
          />
          Новая статья
        </NuxtLink>
      </ClientOnly>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <!-- Полноэкранный loader только при первой загрузке. -->
    <div
      v-if="store.loading && !store.articles.length"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <div
      v-else-if="store.articles.length"
      class="grid items-start gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <ArticlesCard
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
        :can-manage="canManage"
        :show-analytics="canViewAnalytics"
        @toggle-visibility="toggleVisibility"
      />
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:file-text"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Статей пока нет
      </p>
    </div>

    <!-- Sentinel для автоматической подгрузки. -->
    <div
      v-if="store.hasMore"
      ref="loadMoreElement"
      class="flex justify-center py-8"
    >
      <span
        v-if="store.loading"
        class="loading loading-spinner text-primary"
      />

      <button
        v-else
        type="button"
        class="btn btn-ghost btn-sm"
        @click="loadMoreArticles"
      >
        Загрузить ещё
      </button>
    </div>
  </div>
</template>

<!-- frontend\app\components\articles\Card.vue -->
 <script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  },

  canManage: {
    type: Boolean,
    default: false,
  },

  showAnalytics: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'toggle-visibility',
])

const openedCount = computed(
  () => props.article.opened_count ?? 0,
)

const readCount = computed(
  () => props.article.read_count ?? 0,
)

const readRate = computed(() => {
  const value = Number(
    props.article.read_rate ?? 0,
  )

  return new Intl.NumberFormat(
    'ru-RU',
    {
      minimumFractionDigits: 0,
      maximumFractionDigits: 1,
    },
  ).format(value)
})

const articleRoute = computed(() => ({
  path: `/content/articles/${props.article.id}`,
  query: {
    source: 'library',
  },
}))

function toggleVisibility() {
  emit(
    'toggle-visibility',
    props.article,
  )
}
</script>

<template>
  <article
    class="card bg-base-100 border-base-300 overflow-hidden border"
    :class="{
      'opacity-60': article.is_hidden,
    }"
  >
    <div class="card-body">
      <div class="flex flex-wrap gap-2">
        <span
          v-if="article.pro_content"
          class="badge badge-secondary"
        >
          Pro
        </span>

        <span
          v-if="article.is_hidden"
          class="badge badge-warning"
        >
          Скрыта
        </span>
      </div>

      <h2 class="card-title">
        {{ article.title }}
      </h2>

      <div
        v-if="article.tags?.length"
        class="flex flex-wrap gap-1"
      >
        <span
          v-for="tag in article.tags"
          :key="tag.id"
          class="badge badge-outline badge-sm"
        >
          {{ tag.name }}
        </span>
      </div>

      <div
        v-if="showAnalytics"
        class="text-base-content/60 flex items-center gap-3 text-xs"
        >
        <div
            class="tooltip tooltip-bottom"
            data-tip="Открытия"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:mouse-pointer-click"
                class="text-primary size-3.5"
            />
            <span class="font-medium">
                {{ openedCount }}
            </span>
            </span>
        </div>

        <div
            class="tooltip tooltip-bottom"
            data-tip="Прочтения"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:book-open-check"
                class="text-success size-3.5"
            />
            <span class="font-medium">
                {{ readCount }}
            </span>
            </span>
        </div>

        <div
            class="tooltip tooltip-bottom"
            data-tip="Дочитали"
        >
            <span class="flex cursor-help items-center gap-1">
            <Icon
                name="lucide:percent"
                class="text-secondary size-3.5"
            />
            <span class="font-medium">
                {{ readRate }}%
            </span>
            </span>
        </div>
        </div>

      <div class="card-actions mt-auto pt-4">
        <NuxtLink
          :to="articleRoute"
          class="btn btn-sm"
        >
          <Icon
            name="lucide:book-open"
            class="size-4"
          />

          Открыть
        </NuxtLink>
        <ClientOnly>
             <NuxtLink
                v-if="canManage"
                :to="`/content/articles/${article.id}/edit`"
                class="btn btn-sm btn-outline"
                >
                <Icon
                    name="lucide:pencil"
                    class="size-4"
                />

                Редактировать
                </NuxtLink>
        </ClientOnly>

        <button
          v-if="canManage"
          type="button"
          class="btn btn-sm btn-ghost"
          @click="toggleVisibility"
        >
          <Icon
            :name="
              article.is_hidden
                ? 'lucide:eye'
                : 'lucide:eye-off'
            "
            class="size-4"
          />

          {{
            article.is_hidden
              ? 'Показать'
              : 'Скрыть'
          }}
        </button>
      </div>
    </div>
  </article>
</template>

<!-- ./frontend/app/components/articles/PatientOverview.vue -->
<script setup>
const store = useArticlesStore()

const articles = ref([])
const loading = ref(true)
const errorMessage = ref('')

function canReadArticle(article) {
  return article.can_access !== false
}

function articleAuraClass(article) {
  if (!article.pro_content) {
    return ''
  }

  return canReadArticle(article)
    ? 'aura aura-rainbow'
    : 'aura aura-silver'
}

onMounted(async () => {
  try {
    const response = await store.fetchArticles()

    articles.value = response.slice(0, 6)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить статьи'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="space-y-4">
    <div
      class="flex items-center justify-between gap-4"
    >
      <div>
        <h2 class="text-xl font-bold sm:text-2xl">
          Рекомендуемые статьи
        </h2>

        <p class="text-base-content/60 text-sm">
          Материалы подобраны по вашим тегам.
        </p>
      </div>

      <NuxtLink
        to="/content/articles"
        class="btn btn-ghost btn-sm"
      >
        Все статьи
      </NuxtLink>
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <div
      v-else-if="articles.length"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="article in articles"
        :key="article.id"
        :class="[
          articleAuraClass(article),
          'h-full',
        ]"
      >
        <!-- Доступная статья -->
        <NuxtLink
          v-if="canReadArticle(article)"
          :to="`/content/articles/${article.id}`"
          class="card bg-base-100 border-base-300 hover:border-primary h-full border transition"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                v-if="article.pro_content"
                class="badge badge-secondary badge-sm"
              >
                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-primary btn-sm"
              >
                Читать
              </span>
            </div>
          </div>
        </NuxtLink>

        <!-- Заблокированная Pro-статья -->
        <div
          v-else
          class="card bg-base-100 h-full"
        >
          <div class="card-body">
            <div class="flex flex-wrap gap-1">
              <span
                class="badge badge-secondary badge-sm gap-1"
              >
                <Icon
                  name="lucide:sparkles"
                  class="size-3"
                />

                Pro
              </span>

              <span
                v-for="tag in article.tags.slice(0, 3)"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <h3 class="card-title">
              {{ article.title }}
            </h3>

            <p
              class="text-base-content/60 text-sm"
            >
              Статья доступна пользователям Pro.
            </p>

            <div class="card-actions mt-auto">
              <span
                class="btn btn-disabled btn-sm gap-1"
              >
                <Icon
                  name="lucide:lock"
                  class="size-4"
                />

                Только Pro
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p
      v-else
      class="text-base-content/50"
    >
      Подходящих статей пока нет.
    </p>
  </section>
</template>

<!-- ./frontend/app/components/articles/Reader.vue -->
<script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true,
  },
  interactionId: {
    type: String,
    default: null,
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
  isTrackable,
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

    if (!completed.value) {
      window.setTimeout(() => {
        restoreProgress(savedProgress.value)
      }, 100)
    }
  } catch {
    // Отсутствие прогресса не должно мешать чтению.
  }
}

async function saveProgress(
  value = progress.value,
) {
  if (!isPatient.value || saving.value) return

  saving.value = true

  try {
    const body = {
      progress_percent: value,
    }

    if (props.interactionId) {
      body.interaction_id =
        props.interactionId

      body.is_trackable =
        isTrackable.value
    }

    const response = await $api(
      `/api/v1/articles/${props.article.id}/progress`,
      {
        method: 'PUT',
        body,
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

  const body = {
    progress_percent: progress.value,
  }

  if (props.interactionId) {
    body.interaction_id =
      props.interactionId

    body.is_trackable =
      isTrackable.value
  }

  fetch(
    `${config.public.apiBase}/api/v1/articles/${props.article.id}/progress`,
    {
      method: 'PUT',
      keepalive: true,
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
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
    || value >= 90
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

<!-- ./frontend/app/pages/programs/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useProgramsStore()

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const errorMessage = ref('')

const visibilityDialogOpen = ref(false)
const selectedProgram = ref(null)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

function openHideDialog(program) {
  selectedProgram.value = program
  visibilityDialogOpen.value = true
}

async function showProgram(program) {
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      program.id,
      false,
    )

    Object.assign(program, response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось показать программу'
  }
}

function handleHidden(response) {
  const item = store.programs.find(
    (program) => program.id === response.id,
  )

  if (item) {
    Object.assign(item, response)
  }
}

onMounted(async () => {
  try {
    if (auth.activeRole === 'patient') {
      await store.fetchProgramsForPatient()
    } else {
      await store.fetchProgramsForStaff()
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Программы
        </h1>

        <p class="text-base-content/60 mt-1">
          Пошаговые программы работы с материалами.
        </p>
      </div>

      <NuxtLink
        v-if="canManage"
        to="/programs/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая программа
      </NuxtLink>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="store.programs.length"
      class="grid gap-5 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="program in store.programs"
        :key="program.id"
        :class="[
          program.is_popular
            ? 'aura aura-rainbow'
            : '',
          'h-full',
        ]"
      >
        <article
          class="card bg-base-100 border-base-300 relative h-full overflow-hidden border"
          :class="{
            'opacity-60': program.is_hidden,
          }"
        >
          <div
            v-if="program.is_popular"
            class="bg-warning text-warning-content absolute right-0 top-0 rounded-bl-2xl px-4 py-2 text-xs font-bold shadow"
          >
            <Icon
              name="lucide:flame"
              class="mr-1 inline size-4"
            />
            Популярное
          </div>

          <div class="card-body">
            <div class="flex flex-wrap gap-2 pr-24">
              <span
                v-if="hasDiscount(program)"
                class="badge badge-error gap-1 font-bold"
              >
                <Icon
                  name="lucide:badge-percent"
                  class="size-3"
                />
                −{{ program.service?.discount_percent }}%
              </span>

              <span
                v-if="program.has_program_access"
                class="badge badge-success"
              >
                Полный доступ
              </span>

              <span
                v-if="program.purchase_requested"
                class="badge badge-warning"
              >
                Запрос отправлен
              </span>

              <span
                v-if="program.is_hidden"
                class="badge badge-ghost"
              >
                Скрыта
              </span>
            </div>

            <h2 class="card-title mt-2">
              {{ program.title }}
            </h2>

            <p
              class="text-base-content/60 line-clamp-3 text-sm"
            >
              {{ program.description }}
            </p>

            <div class="mt-2 flex items-end gap-2">
              <span class="text-primary text-xl font-bold">
                {{ formatFinalPrice(program) }}
              </span>

              <span
                v-if="hasDiscount(program)"
                class="text-base-content/40 text-sm line-through"
              >
                {{ formatOriginalPrice(program) }}
              </span>
            </div>

            <div class="mt-2 flex flex-wrap gap-1">
              <span
                v-for="tag in program.tags"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <div class="card-actions mt-auto pt-5">
              <NuxtLink
                :to="`/programs/${program.id}`"
                class="btn btn-primary btn-sm"
              >
                Открыть
              </NuxtLink>

              <NuxtLink
                v-if="canManage"
                :to="`/programs/${program.id}/edit`"
                class="btn btn-outline btn-sm"
              >
                <Icon
                  name="lucide:pencil"
                  class="size-4"
                />
                Изменить
              </NuxtLink>

              <button
                v-if="canManage && !program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="openHideDialog(program)"
              >
                <Icon
                  name="lucide:eye-off"
                  class="size-4"
                />
                Скрыть
              </button>

              <button
                v-if="canManage && program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="showProgram(program)"
              >
                <Icon
                  name="lucide:eye"
                  class="size-4"
                />
                Показать
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:route"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Программ пока нет
      </p>
    </div>
  </div>

  <ProgramsVisibilityDialog
    v-model="visibilityDialogOpen"
    :program="selectedProgram"
    @hidden="handleHidden"
  />
</template>

<!-- ./frontend/app/pages/questionnaires/index.vue -->
<script setup>
const store = useQuestionnairesStore()

const questionnaires = ref([])
const progressItems = ref([])

const loading = ref(true)
const page = ref(1)
const pageSize = 10

const paginatedItems = computed(() => {
  const start = (page.value - 1) * pageSize

  return questionnaires.value.slice(
    start,
    start + pageSize,
  )
})

function getProgress(questionnaireId) {
  return progressItems.value.find(
    (item) =>
      item.questionnaire_id === questionnaireId,
  )
}

async function load() {
  loading.value = true

  try {
    const [items, progress] = await Promise.all([
      store.fetchQuestionnaires(),
      store.fetchMyProgress(),
    ])

    questionnaires.value = items
    progressItems.value = progress
  } finally {
    loading.value = false
  }
}

onMounted(load)
</script>

<template>
  <div class="space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Опросники
      </h1>

      <p class="text-base-content/60 mt-1">
        Начатые опросники сохраняются автоматически.
      </p>
    </header>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <article
        v-for="questionnaire in paginatedItems"
        :key="questionnaire.id"
        class="card bg-base-100 border-base-300 border"
      >
        <div class="card-body">
          <div class="flex flex-wrap gap-2">
            <span
              v-if="questionnaire.pro_content"
              class="badge badge-secondary"
            >
              Pro
            </span>

            <span
              v-if="
                getProgress(questionnaire.id)?.status
                === 'completed'
              "
              class="badge badge-success"
            >
              Пройден
            </span>

            <span
              v-else-if="getProgress(questionnaire.id)"
              class="badge badge-warning"
            >
              Не завершён
            </span>
          </div>

          <h2 class="card-title">
            {{ questionnaire.title }}
          </h2>

          <p class="text-base-content/60 line-clamp-3 text-sm">
            {{ questionnaire.description }}
          </p>

          <div
            v-if="getProgress(questionnaire.id)"
            class="mt-3"
          >
            <progress
              class="progress progress-primary w-full"
              :value="
                getProgress(questionnaire.id).progress_percent
              "
              max="100"
            />

            <p class="mt-1 text-xs">
              {{
                getProgress(questionnaire.id).progress_percent
              }}%
            </p>
          </div>

          <div class="card-actions mt-4">
            <NuxtLink
              :to="`/questionnaires/${questionnaire.id}`"
              class="btn btn-primary btn-sm"
            >
              {{
                getProgress(questionnaire.id)?.status
                === 'in_progress'
                  ? 'Продолжить'
                  : 'Начать'
              }}
            </NuxtLink>
          </div>
        </div>
      </article>
    </div>

    <UiPagination
      v-model="page"
      :total-items="questionnaires.length"
      :page-size="pageSize"
    />
  </div>
</template>

// ./frontend/app/stores/articles.js
export const useArticlesStore = defineStore(
  'articles',
  () => {
    const articles = ref([])
    const currentArticle = ref(null)
    const loading = ref(false)

    const hasMore = ref(true)

    async function fetchArticles({
      reset = false,
      limit = 5,
    } = {}) {
      const { $api } = useNuxtApp()

      if (loading.value) return articles.value

      if (reset) {
        articles.value = []
        hasMore.value = true
      }

      if (!hasMore.value) {
        return articles.value
      }

      loading.value = true

      try {
        const page = await $api(
          '/api/v1/articles',
          {
            query: {
              offset: articles.value.length,
              limit,
            },
          },
        )

        const existingIds = new Set(
          articles.value.map(
            article => article.id,
          ),
        )

        const newItems = page.filter(
          article => !existingIds.has(article.id),
        )

        articles.value.push(...newItems)

        hasMore.value = page.length === limit

        return articles.value
      } finally {
        loading.value = false
      }
    }

    async function fetchArticle(articleId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentArticle.value = await $api(
          `/api/v1/articles/${articleId}`,
        )

        return currentArticle.value
      } finally {
        loading.value = false
      }
    }

    async function createArticle(payload) {
      const { $api } = useNuxtApp()

      return await $api('/api/v1/articles', {
        method: 'POST',
        body: payload,
      })
    }

    async function updateArticle(
      articleId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}`,
        {
          method: 'PATCH',
          body: payload,
        },
      )
    }

    async function setVisibility(
      articleId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function markAsRead(articleId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/read`,
        {
          method: 'POST',
        },
      )
    }

    async function registerOpen(
      articleId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/articles/${articleId}/open`,
        {
          method: 'POST',
          body: payload,
        },
      )
    }

    return {
      articles,
      currentArticle,
      loading,

      hasMore,
      fetchArticles,
      fetchArticle,
      registerOpen,
      createArticle,
      updateArticle,
      setVisibility,
      markAsRead,
    }
  },
)
// ./frontend/app/stores/programs.js
export const useProgramsStore = defineStore(
  'programs',
  () => {
    const programs = ref([])
    const currentProgram = ref(null)

    const patientAccessPrograms = ref([])

    const loading = ref(false)
    const saving = ref(false)

    const patientProgressPrograms = ref([])

    async function fetchProgramsForStaff() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/manage',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramsForPatient() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        programs.value = await $api(
          '/api/v1/programs/patient',
        )

        return programs.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForStaff(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/manage/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function fetchProgramForPatient(programId) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentProgram.value = await $api(
          `/api/v1/programs/patient/${programId}`,
        )

        return currentProgram.value
      } finally {
        loading.value = false
      }
    }

    async function createProgram(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          '/api/v1/programs/manage',
          {
            method: 'POST',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function updateProgram(
      programId,
      payload,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        return await $api(
          `/api/v1/programs/manage/${programId}`,
          {
            method: 'PUT',
            body: payload,
          },
        )
      } finally {
        saving.value = false
      }
    }

    async function setVisibility(
      programId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/manage/${programId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function startProgram(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/start`,
        {
          method: 'POST',
        },
      )
    }

    async function requestPurchase(programId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/programs/patient/${programId}/request-purchase`,
        {
          method: 'POST',
        },
      )
    }

    async function fetchPatientProgramAccess(
      patientId,
    ) {
      const { $api } = useNuxtApp()

      patientAccessPrograms.value = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access`,
      )

      return patientAccessPrograms.value
    }

    async function setPatientProgramAccess(
      patientId,
      programId,
      isActive,
    ) {
      const { $api } = useNuxtApp()

      const response = await $api(
        `/api/v1/programs/manage/patient/${patientId}/access/${programId}`,
        {
          method: 'PATCH',
          body: {
            is_active: isActive,
          },
        },
      )

      const item = patientAccessPrograms.value.find(
        (program) =>
          program.program_id === programId,
      )

      if (item) {
        Object.assign(item, response)
      }

      return response
    }

    async function fetchPatientProgramProgress(
        patientId,
        ) {
        const { $api } = useNuxtApp()

        patientProgressPrograms.value = await $api(
            `/api/v1/programs/manage/patient/${patientId}/progress`,
        )

        return patientProgressPrograms.value
        }

    return {
      programs,
      currentProgram,
      patientAccessPrograms,

      loading,
      saving,

      fetchProgramsForStaff,
      fetchProgramsForPatient,
      fetchProgramForStaff,
      fetchProgramForPatient,

      createProgram,
      updateProgram,
      setVisibility,

      startProgram,
      requestPurchase,

      fetchPatientProgramAccess,
      setPatientProgramAccess,

      patientProgressPrograms,
      fetchPatientProgramProgress,
    }
  },
)
// ./frontend/app/stores/questionnaires.js
export const useQuestionnairesStore = defineStore(
  'questionnaires',
  () => {
    const questionnaires = ref([])
    const currentQuestionnaire = ref(null)
    const loading = ref(false)

    async function fetchQuestionnaires() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        questionnaires.value = await $api(
          '/api/v1/questionnaires',
        )

        return questionnaires.value
      } finally {
        loading.value = false
      }
    }

    async function fetchQuestionnaire(
      id,
      {
        programId = null,
        programStageId = null,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentQuestionnaire.value = await $api(
          `/api/v1/questionnaires/${id}`,
          {
            query: {
              program_id: programId || undefined,
              program_stage_id:
                programStageId || undefined,
            },
          },
        )

        return currentQuestionnaire.value
      } finally {
        loading.value = false
      }
    }

    async function createQuestionnaire(payload) {
      const { $api } = useNuxtApp()

      return await $api(
        '/api/v1/questionnaires',
        {
          method: 'POST',
          body: payload,
        },
      )
    }

    async function setVisibility(
      questionnaireId,
      isHidden,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/${questionnaireId}/visibility`,
        {
          method: 'PATCH',
          body: {
            is_hidden: isHidden,
          },
        },
      )
    }

    async function fetchMyProgress() {
      const { $api } = useNuxtApp()

      return await $api(
        '/api/v1/questionnaires/submissions/mine/progress',
      )
    }

    async function startQuestionnaire(
      questionnaireId,
      {
        programId = null,
        programStageId = null,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/${questionnaireId}/start`,
        {
          method: 'POST',
          query: {
            program_id: programId || undefined,
            program_stage_id:
              programStageId || undefined,
          },
        },
      )
    }

    async function fetchSubmission(submissionId) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}`,
      )
    }

    async function saveAnswer(
      submissionId,
      questionId,
      value,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}/answer`,
        {
          method: 'PUT',
          body: {
            question_id: questionId,
            value,
          },
        },
      )
    }

    async function completeSubmission(
      submissionId,
      answers,
    ) {
      const { $api } = useNuxtApp()

      return await $api(
        `/api/v1/questionnaires/submissions/${submissionId}/complete`,
        {
          method: 'POST',
          body: {
            answers,
          },
        },
      )
    }

    return {
      questionnaires,
      currentQuestionnaire,
      loading,

      fetchQuestionnaires,
      fetchQuestionnaire,
      createQuestionnaire,
      setVisibility,

      fetchMyProgress,
      startQuestionnaire,
      fetchSubmission,
      saveAnswer,
      completeSubmission,
    }
  },
)
// ./frontend/app/plugins/api.js
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()

  const api = $fetch.create({
    baseURL: config.public.apiBase,

    onRequest({ options }) {
      if (!import.meta.client) return

      const accessToken = localStorage.getItem(
        'mentalme_access_token',
      )

      if (!accessToken) return

      const headers = new Headers(options.headers || {})
      headers.set(
        'Authorization',
        `Bearer ${accessToken}`,
      )

      options.headers = headers
    },

    async onResponseError({ response }) {
      if (!import.meta.client) return

      if (response.status !== 401) return

      const hadAccessToken = Boolean(
        localStorage.getItem('mentalme_access_token'),
      )

      if (!hadAccessToken) return

      localStorage.removeItem('mentalme_access_token')
      localStorage.removeItem('mentalme_active_role')

      const publicPaths = [
        '/login',
        '/forgot-password',
        '/reset-password',
        '/verify-email',
        '/register',
      ]

      const isPublicPath = publicPaths.some((path) =>
        window.location.pathname.startsWith(path),
      )

      if (!isPublicPath) {
        window.location.href = '/login?sessionExpired=1'
      }
    },
  })

  return {
    provide: {
      api,
    },
  }
})

// ./frontend/app/composables/useReadingProgress.js

const MIN_TRACKABLE_SCROLL_DISTANCE = 240

export function useReadingProgress(target) {
  const progress = ref(0)
  const isTrackable = ref(false)

  let animationFrame = null
  let resizeObserver = null

  function getMetrics() {
    const element = target.value

    if (!element) {
      isTrackable.value = false
      return null
    }

    const rect =
      element.getBoundingClientRect()

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

    // Сначала рассчитываем конечную позицию.
    const endPosition = Math.min(
      articleEndScroll,
      maxPageScroll,
    )

    // И только после этого доступную для чтения
    // дистанцию прокрутки.
    const rawReadableHeight =
      endPosition - elementTop

    isTrackable.value =
      rawReadableHeight
      >= MIN_TRACKABLE_SCROLL_DISTANCE

    const readableHeight = Math.max(
      rawReadableHeight,
      1,
    )

    return {
      elementTop,
      readableHeight,
      rawReadableHeight,
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

    // До начала статьи прогресс равен нулю.
    if (currentPosition <= 0) {
      progress.value = 0
      return
    }

    // Для слишком короткой статьи допускаем
    // визуальное отображение прогресса, но
    // isTrackable останется false, поэтому
    // ARTICLE_READ зарегистрирован не будет.
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
    if (animationFrame !== null) return

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

    scheduleCalculate()
  }

  onMounted(() => {
    nextTick(() => {
      scheduleCalculate()

      if (target.value) {
        resizeObserver =
          new ResizeObserver(() => {
            scheduleCalculate()
          })

        resizeObserver.observe(
          target.value,
        )
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
    resizeObserver = null

    if (animationFrame !== null) {
      window.cancelAnimationFrame(
        animationFrame,
      )

      animationFrame = null
    }
  })

  return {
    progress: readonly(progress),
    isTrackable: readonly(isTrackable),
    calculate,
    restoreProgress,
  }
}
// ./frontend/app/middleware/program-manager.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (
    ![
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
  ) {
    return navigateTo('/programs')
  }
})

// ./frontend/app/middleware/service-manager.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (
    ![
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
  ) {
    return navigateTo('/dashboard')
  }
})
// ./frontend/app/middleware/user-manager.js
export default defineNuxtRouteMiddleware(() => {
  if (import.meta.server) return

  const auth = useAuthStore()

  if (!auth.initialized) {
    auth.initFromStorage()
  }

  if (
    ![
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole)
  ) {
    return navigateTo('/dashboard')
  }
})


если нужны еще какие-то файлы, попроси прислать
----

Смотри, это MVP проекта для многопрофильной клиники. 
обстоятельства такие: где-то 2 года назад старое рукооводство отделения решило сделать проект: там в элетронную историю болезни внедрили алгоритм, который выявляет пациентов с высокир риском дистресса: он включается периодически, примерно раз в 3 месяца и помечает пациентов как "Высокй риск дистресса". Весь бюджет проекта потратили на этот функционал и... все. 
Проблема в том, что больше ничего не происходит: соматические врачи не понимают, что и как делать с пациентами, обратившимися к ним на прием. Допутсим, врач терапевт видит, что пациенту нужна помощь психиатра, но пациент никогда не обращался ранее к психиатру и либо не понимает, зачем ему тратить деньги и время на окнсультацию психиатра, либо боится из-за стигматизации. 
Я решил взять на себя роль кризис-менеджера и сдвинуть дело, чтобы окупить огромные затраты, которые руководство считает необоснованными. Для этого я сделал приложение, которое:
1. Врач Не психиатр может формировать ссылку на регистрацию в приложении (либо в виде qr кода, либо отправить пациенту на почту). Тахим образом, я планирую сделать хоть какую-то теплую передачу пациента в приложение
2. Пациент заходит и на главной странице он должен видеть сразу то, что его замотивирует... Вот, как раз, это сейчас надо сделать, потмоу что до галвной страницы я пока не дошел. Я думаю, там надо как-то расположить самые четко подобранные материалы как раз под пациента. Пока что, идея в том, что у специальности есть набор тегов. При регистрации врача, эти теги передаются ему, но врач также может себе эти теги кастомихировать. При регистрации пациента, теги от врача передаются пациенту. Плюс, сам врач может конкретного пациента кастомизировать. Плюс, если врач другой специальности также привязывается к пациенту, его теги также передаются пациенту. контент фильтруется по тегам.
3. кроме того, в статьях я наладил сбор информации по прочтению и количествам открытий статьи

Надо сделать самую галвную страницу пациента так, чтобы пациент с максимальной вероятностью начал вовлекаться в работу с приложением. Иныцми словами, это что-то типа воронки продаж... 

На следующей неделе у меня демонстрация приложения для стейкхолдеров. Планируется демонстрация в основном, что видит пациент, когда регистрируется в приложении. Разумееется, руоводство будет смотреть, насколько эффективно потенциальные пациенты будут вовелекаться в процесс работы и как траектория в приложении будет выводить пациентов на запись к психиатру (сейчас планируется покупка программ). Программа - это комплект консультация - пока психитров, плюс материалы в виде опросников и статей. Часть материалов будет бесплатной, чтобы пациент вовлекался в работу, а часть - платной, но только те матеиалы, которые требуют ведения специалиста. Как раз, это пациент и покупает - индивидуальное ведение специалистов - пакет конслуьтаций. Программы также фильтруются по тегам, чтобы показывать пациентам наиболее релевантные из них. Я думаю, что для каждой категории также сделать 2-3 программы, чтобы был выбор. Допутсим, пациент начал работу и хочет уже начать работать со специалистом. Он нажимает на конпку, ассистент и суперпользователь получают уведомление, что пациент хочет приобрести программу, далее ассистент связывается по телефону с пациентом и пациент совершает покупку в клинике (не приложении), после покупки ассистент дает пациенту доступ.

Необходима МИНИМАЛЬНАЯ КОГНИТИВНАЯ НАГРУЗКА . Например, сейчас после того, как ссылка отправлена пациенту, пациент после ввода пароля перенаправляется на страницу логина... так нельзя ... надо, чтобы пациент сразу же был залогинен. В идеале, вообще надо, чтобы пациент логинился бесшовно, без ввода каких-то данных и сразу виде материалы, которые могут его как-то зацепить. Доступ можно восстановить и потом... я не знаю, как это можно реализовать, может ты что-то посоветуешь

Плюс, помжет ты посоветуешь что-то по внедерению элементов геймификации и других, чтобьы задействоать дофамин...


Для начала, задай мне дополнитлеьные вопросы и попроси прислать необзходимые файлы, если таковые нужны. Некоторые файлы, конечно, довольно болшие, но что делать, пришлю.




























============================













1. Пациент и первый шаг:
1. Какого пациента берём для основного сценария демонстрации?
Ну, договорились, что это пациент с алкогольной зависимостью. Допустим, пациент обратился к врачу-терапевту (по выгрузке, к терапевту наибольшее число оюращений которые алгоритм определил как высокий риск, алкоголь также относится к риску). 

какая специальность у направляющего врача - пока терапевт
с какой жалобой пришёл пациент - предположим, избыточный вес, тошноту, вздутие живота, и типа того - диспепсические жалобы
что врач говорит перед отправкой приглашения - а вот это очень важный вопрос... посоветуй, что лучше сказать... я пока думаю, что врач говорит типа: "Сморите, Иван Иванович, ваша проблема требует комплексного наблюдения, в том числе и специалиста по зависимостям. Я рекомендую Вам воспользоваться нашей платформой, которая показывает вам конкретные шаги для решения Вашей проблемы"... пока думаю так, но ты посоветуй, как лучше сказать. я вообще хочу добавить это на сайт - спич для врача, но пока давай сосредоточися на текущей задаче.
какие теги получает пациент - ну, сделаем алкоголь, гастрит, панкреатит, высокие трансаминазы, например. А контент будет не конкретно наркологический, чтобы не отпугнуть, а допустим, по постепенному изменению образа жизни. А программа будет типа SMART recovery, но для индивидуального ведения - просто изменение образа жизни: налахивание сна, питания, снижение веса, спорт, и в том числе отмена алкоголя... можно туда динамику анализов засунуть, например

2. Что пациент знает о направлении?
Врач прямо предлагает консультацию психиатра? - это индивидуально, врачи иногда боятся напрямую говорить слово психиатр - иногда психотерапевт, иногда специалист по аддикциям
Говорит о влиянии стресса на самочувствие? - разуемеется, у нас в клинике концепция 360 градусов, то есть , мы во главу угла ставим образ жизни и комплексную работу с пациентом.
Просто предлагает полезные материалы? - вот, не нзаю я, какие принципы заложить в спич для врачей - может ты посоветуешь . это еще одна задача, потому что моя работа также будет включать индивидуальные встречи с врачами и мне им надо будет помимо регистрации в приложении, также давать инструкции, что и как делать с пациентом. Ты же понимаешь, это дело довольно деликатное.
Объясняет отметку «высокий риск дистресса»? - я не знаю... ну, можно, наверное, но не всем, а то некоторые испугаются, скажут - Вы тут всех метите как больных...

И отдельно: приложение уже получает эту отметку из медицинской системы или пока работает независимо от неё? Смотри... пока что, отдельно. демонстрировать вообще буду приложение на моей собвтенной vds, но мы будем интегрировать это в личный кабинет пациента. думаю, через iframe, или как там это делают... Нужно будет максимально бесшовное взаимодействие. Может ты по этой части что-то посоветуешь. Личный кабине тпациента- это приложение для мобильных устройств, где пациент видит консультации, записи и т.д. Это не электронная карта. Просто, для интеграции требуется работа с it департаментом, а это уже отдельная история...

3. Какое одно действие вы хотите получить в первые несколько минут?
прочитать короткий материал - я думаю, лучше сделать это самым первым, потому что это наиболее понятно.
ответить на несколько вопросов - тут не знаю, 
попробовать небольшую практику - навероне, это не самое главное, хотя я думаю, что практика - это программа с траекторией выполнения.
познакомиться с программой - ну, или это самое первое - небольшая бесплатная программа с конкретной траекторией - пациент читает статьи, заполняет опросники и понимает, что означает для него, например, измеенние образа жизни и какую роль там играет психиатр. Например, "Как наладить сон?", а опросник "Вы убрали все гаджеты за час до сна? да/нет; Вы выключили свет? да/нет, и т.д." Потом пациент если он все равное не может уснуть, понимает из дальнейших статей, что возможно требуетсяф медикаментозная коррекция... ну, ты понял.
попросить ассистента связаться - тут думаю это уже после того, как пациент поймет смысл для консультаций психиатра

4. Какие материалы реально будут готовы к демонстрации?
нескольких бесплатных статей: например: "Польза полноценного сна; Как наладить сон?; Почему сон нарушается; Не всё сразу: как начинать изменения небольшими шагами (именется ввиду, пробему с алкоголем); Триггеры: как замечать ситуации высокого риска"
опросников: 
Мой план профилактики рецидива: Этот опрос поможет собрать ваш личный план на случай, если тяга усилится или станет сложнее сохранять изменения.
Моя ситуация по модели ABC: Этот опрос поможет разобрать одну недавнюю ситуацию, в которой вы испытали сильную эмоцию, тягу или вернулись к привычному зависимому...
Моя мотивация и цели: Этот опрос поможет зафиксировать вашу точку старта и понять, какие изменения сейчас важны для вас. Здесь нет правильных или неправильных ответов —...
одной–трёх программ для выбранного сценария: давай так: бесплатная программа без пакета консультаций и платного контента: "Life Balance FREE", платная, но недорогая с минимальным пакетом: "Life Balance Lite" - допустим, 5 шагов, 5 консультаций психиатра, 1875 у.е. (каждая консультация психиатра стоит 275 у.е.) Ну, и самая дорогая: "Life Balance Personal" - 10 шагов, 11 консультаций - стартовая консультация короткая по 175 у.е., остальные по 375 у.е. суммарно 3925 у.е.
Есть ли возможность сначала обсудить выбор с ассистентом, не выбирая конкретную программу? - да, разумеется! Более того, мне тут директор по развитию сказал, что цену надо вообще убрать, чтобы не пугать пациентов... я думаю, что по описанию пациент будет понимать примерную стоимость, а ассистент уже будет озвучивать цуену программы


5. Как сейчас устроено приглашение?
Это персональная одноразовая ссылка или общая ссылка врача? - персональная ссылка для пациента, которую формирует врач. для формирования ссылки врач вводит record_id - уникальный номер пациента в медицинской карте и email пациента. Если record_id уже есть в системе, то врачу предлагается присоединиться к курации пациента

Пациент заранее указан в системе? - нет, до регистрации пациента, его нет в системе, но ассистент может регистрировать пациента заранее в некоторых случаях, потому что фактически - это пациенты нашенй клиники и они есть в электронной карте
Email или телефон уже известны? - технически - да. То есть, телоефон нам в приложении вообще не нужен, потому что пациента находят в ЭМК по номеру карты
Какие поля пациент заполняет, кроме пароля? - никаких: почту и номер карты за пациента заполняет врач. 
Есть ли срок действия ссылки? - да, несколько дней
QR-код пациент сканирует на приёме или получает на бумаге? - предполагается, врач на своем телефоне или компьютере показывает qr код пациенту, а пациент уже с телефона сканирует
кроме того, сделан функционал passkey - пока пользователи могут добавлять passkey устройства уже после регистрации в настройках





