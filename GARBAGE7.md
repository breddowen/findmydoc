У меня такой проект:
# Project Structure

> Generated: 2026-09-07 19:40

---

## AI Backend

```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (29 lines)
backend/alembic/versions/4a9d77a6cc23_initial_schema.py (887 lines)
backend/alembic/versions/6042112705c7_article_analytics_events.py (487 lines)
backend/alembic/versions/6eb4582e2464_add_new_field_to_users.py (33 lines)
backend/alembic/versions/7c21a6d4ef10_admin_invitations_and_hidden_directories.py (170 lines)
backend/alembic/versions/95f734785945_program_home_fields.py (71 lines)
backend/alembic/versions/9f31b8c4d2e7_medical_services.py (454 lines)
backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py (141 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (58 lines)
backend/app/core/db.py (129 lines)
backend/app/core/email.py (150 lines)
backend/app/core/security.py (232 lines)
backend/app/core/transactions.py (60 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (107 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/access.py (64 lines)
backend/app/modules/articles/models.py (115 lines)
backend/app/modules/articles/routers.py (926 lines)
backend/app/modules/articles/schemas.py (124 lines)
backend/app/modules/articles/tracking.py (91 lines)
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
backend/app/modules/consents/routers.py (245 lines)
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
backend/app/modules/notifications/transactional.py (91 lines)
backend/app/modules/patients/__init__.py (0 lines)
backend/app/modules/patients/enums.py (7 lines)
backend/app/modules/patients/routers.py (511 lines)
backend/app/modules/patients/schemas.py (138 lines)
backend/app/modules/patients/utils.py (231 lines)
backend/app/modules/programs/__init__.py (0 lines)
backend/app/modules/programs/enums.py (22 lines)
backend/app/modules/programs/models.py (358 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1808 lines)
backend/app/modules/programs/schemas.py (271 lines)
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
backend/test_database.db (1154 lines)
```

*Files: 128*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (203 lines)
frontend/app/components/articles/Form.vue (233 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (472 lines)
frontend/app/components/assignments/ContentPicker.vue (181 lines)
frontend/app/components/assignments/CreateDialog.vue (345 lines)
frontend/app/components/assignments/PatientList.vue (108 lines)
frontend/app/components/assignments/PickerItem.vue (130 lines)
frontend/app/components/auth/PasswordForm.vue (173 lines)
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (294 lines)
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
frontend/app/components/patient/Home.vue (160 lines)
frontend/app/components/patient/Journey.vue (78 lines)
frontend/app/components/patient/NextStep.vue (183 lines)
frontend/app/components/patient/Support.vue (185 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (111 lines)
frontend/app/components/patients/List.vue (257 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/patients/Tags.vue (105 lines)
frontend/app/components/programs/configurator/Editor.vue (715 lines)
frontend/app/components/programs/configurator/HomeSettings.vue (68 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (272 lines)
frontend/app/components/programs/configurator/ServiceSelect.vue (170 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (389 lines)
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
*Files: 64*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (146 lines)
frontend/app/pages/content/articles/index.vue (186 lines)
frontend/app/pages/content/articles/new.vue (49 lines)
frontend/app/pages/content/questionnaires/[id].vue (319 lines)
frontend/app/pages/content/questionnaires/index.vue (166 lines)
frontend/app/pages/content/questionnaires/new.vue (9 lines)
frontend/app/pages/dashboard.vue (159 lines)
frontend/app/pages/forgot-password.vue (102 lines)
frontend/app/pages/index.vue (4 lines)
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
frontend/app/pages/register/invitation.vue (379 lines)
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
frontend/app/stores/articles.js (172 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/invitations.js (53 lines)
frontend/app/stores/notifications.js (312 lines)
frontend/app/stores/patient-home.js (198 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (174 lines)
frontend/app/stores/services.js (159 lines)
frontend/app/stores/tag-access.js (210 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 15*

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

------
Файлы, которые могут пригодиться сразу:
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
from typing import Literal

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

    # Возвращаются только администраторам и медассистентам.
    opened_count: int | None = None
    read_count: int | None = None
    read_rate: float | None = None

class ArticleReadResponse(BaseModel):
    message: str
    event_id: uuid.UUID

class ArticleProgressResponse(BaseModel):
    article_id: uuid.UUID
    patient_id: uuid.UUID

    progress_percent: float
    max_progress_percent: float

    started_at: datetime
    updated_at: datetime
    completed_at: datetime | None

ArticleOpenSource = Literal[
    "library",
    "program",
    "assignment",
    "direct",
]


class ArticleOpenRequest(BaseModel):
    interaction_id: uuid.UUID

    source: ArticleOpenSource = "direct"

    program_id: uuid.UUID | None = None
    program_stage_id: uuid.UUID | None = None
    assignment_id: uuid.UUID | None = None


class ArticleOpenResponse(BaseModel):
    event_id: uuid.UUID
    interaction_id: uuid.UUID


class ArticleProgressUpdateRequest(BaseModel):
    progress_percent: float = Field(
        ge=0,
        le=100,
        allow_inf_nan=False,
    )

    interaction_id: uuid.UUID | None = None
    is_trackable: bool = False

    program_id: uuid.UUID | None = None
    program_stage_id: uuid.UUID | None = None

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

# ./backend/app/modules/programs/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import UniqueConstraint
import sqlalchemy as sa

from app.modules.articles.models import Article
from app.modules.services.models import MedicalService
from app.modules.questionnaires.models import Questionnaire
from app.modules.tags.models import Tag
from app.modules.users.models import (
    PatientProfile,
    Speciality,
    User,
)
from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
)

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Program(SQLModel, table=True):
    __tablename__ = "programs"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    title: str = Field(
        index=True,
        max_length=300,
    )
    description: Optional[str] = Field(default=None)

    service_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="medical_services.id",
        index=True,
    )

    pro_content: bool = Field(
        default=False,
        index=True,
    )

    is_start: bool = Field(
        default=False,
        sa_column=sa.Column(
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )

    home_priority: int = Field(
        default=0,
        sa_column=sa.Column(
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
    )

    is_popular: bool = Field(
        default=False,
        index=True,
    )

    is_hidden: bool = Field(
        default=False,
        index=True,
    )

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    service: Optional[MedicalService] = Relationship(
        back_populates="programs",
        sa_relationship_kwargs={
            "foreign_keys": "[Program.service_id]",
        },
    )

    stages: list["ProgramStage"] = Relationship(
        back_populates="program",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "ProgramStage.order_index",
        },
    )

    tag_links: list["ProgramTagLink"] = Relationship(
        back_populates="program",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class ProgramStage(SQLModel, table=True):
    __tablename__ = "program_stages"
    __table_args__ = (
        UniqueConstraint(
            "program_id",
            "order_index",
            name="uq_program_stage_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    title: str = Field(max_length=300)
    description: Optional[str] = Field(default=None)
    doctor_description: Optional[str] = Field(default=None)

    day_from: int = Field(index=True)
    day_to: int = Field(index=True)
    order_index: int = Field(index=True)

    program: Optional[Program] = Relationship(
        back_populates="stages"
    )

    items: list["ProgramStageItem"] = Relationship(
        back_populates="stage",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "ProgramStageItem.order_index",
        },
    )


class ProgramStageItem(SQLModel, table=True):
    __tablename__ = "program_stage_items"
    __table_args__ = (
        UniqueConstraint(
            "stage_id",
            "order_index",
            name="uq_program_stage_item_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    stage_id: uuid.UUID = Field(
        foreign_key="program_stages.id",
        index=True,
    )

    item_type: ProgramItemType = Field(index=True)
    order_index: int = Field(index=True)

    article_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="articles.id",
        index=True,
    )
    questionnaire_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="questionnaires.id",
        index=True,
    )
    speciality_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="specialities.id",
        index=True,
    )

    consultation_title: Optional[str] = Field(
        default=None,
        max_length=300,
    )
    consultation_description: Optional[str] = Field(
        default=None,
    )

    stage: Optional[ProgramStage] = Relationship(
        back_populates="items"
    )

    article: Optional[Article] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramStageItem.article_id]",
        }
    )

    questionnaire: Optional[Questionnaire] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[ProgramStageItem.questionnaire_id]"
            ),
        }
    )

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramStageItem.speciality_id]",
        }
    )


class ProgramTagLink(SQLModel, table=True):
    __tablename__ = "program_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "program_id",
            "tag_id",
            name="uq_program_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    program: Optional[Program] = Relationship(
        back_populates="tag_links"
    )

    tag: Optional[Tag] = Relationship()


class PatientProgramAccess(SQLModel, table=True):
    __tablename__ = "patient_program_access"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "program_id",
            name="uq_patient_program_access",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    is_active: bool = Field(default=False, index=True)

    # Текущий активный запрос пациента на покупку.
    purchase_requested: bool = Field(
        default=False,
        index=True,
    )
    requested_at: Optional[datetime] = Field(default=None)

    activated_at: Optional[datetime] = Field(default=None)
    deactivated_at: Optional[datetime] = Field(default=None)

    updated_by_user_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProgramAccess.patient_id]",
        }
    )

    program: Optional[Program] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[PatientProgramAccess.program_id]",
        }
    )

    updated_by_user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientProgramAccess.updated_by_user_id]"
            ),
        }
    )


class ProgramEnrollment(SQLModel, table=True):
    __tablename__ = "program_enrollments"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "program_id",
            name="uq_patient_program_enrollment",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    program_id: uuid.UUID = Field(
        foreign_key="programs.id",
        index=True,
    )

    status: ProgramEnrollmentStatus = Field(
        default=ProgramEnrollmentStatus.ACTIVE,
        index=True,
    )

    started_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)
    cancelled_at: Optional[datetime] = Field(default=None)

    # Эти поля не позволяют создавать повторные события.
    in_progress_event_at: Optional[datetime] = Field(default=None)
    completed_event_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramEnrollment.patient_id]",
        }
    )

    program: Optional[Program] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[ProgramEnrollment.program_id]",
        }
    )

# ./backend/app/modules/programs/schemas.py
import uuid
from datetime import datetime

from pydantic import BaseModel, Field, model_validator

from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
    ProgramStageStatus,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)

from app.modules.services.schemas import (
    MedicalServicePatientResponse,
    MedicalServiceStaffResponse,
)

class ProgramStageItemCreateRequest(BaseModel):
    item_type: ProgramItemType
    order_index: int = Field(ge=0)

    article_id: uuid.UUID | None = None
    questionnaire_id: uuid.UUID | None = None
    speciality_id: uuid.UUID | None = None

    consultation_title: str | None = Field(
        default=None,
        max_length=300,
    )
    consultation_description: str | None = None

    @model_validator(mode="after")
    def validate_reference(self):
        if self.item_type == ProgramItemType.ARTICLE:
            if (
                not self.article_id
                or self.questionnaire_id
                or self.speciality_id
            ):
                raise ValueError(
                    "Для статьи требуется только article_id"
                )

        if self.item_type == ProgramItemType.QUESTIONNAIRE:
            if (
                not self.questionnaire_id
                or self.article_id
                or self.speciality_id
            ):
                raise ValueError(
                    "Для опросника требуется только "
                    "questionnaire_id"
                )

        if self.item_type == ProgramItemType.CONSULTATION:
            if (
                not self.speciality_id
                or self.article_id
                or self.questionnaire_id
            ):
                raise ValueError(
                    "Для консультации требуется только "
                    "speciality_id"
                )

        return self


class ProgramStageCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)

    description: str | None = None
    doctor_description: str | None = None

    day_from: int = Field(ge=0)
    day_to: int = Field(ge=0)
    order_index: int = Field(ge=0)

    items: list[ProgramStageItemCreateRequest] = []

    @model_validator(mode="after")
    def validate_period(self):
        if self.day_to < self.day_from:
            raise ValueError(
                "day_to не может быть меньше day_from"
            )

        return self


class ProgramCreateRequest(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=300,
    )
    description: str | None = None

    # NULL означает бесплатную программу
    # без связанной медицинской услуги.
    service_id: uuid.UUID | None = None

    is_start: bool = False

    home_priority: int = Field(
        default=0,
        ge=0,
        le=1000,
    )

    is_popular: bool = False

    tag_ids: list[uuid.UUID] = []
    stages: list[ProgramStageCreateRequest] = Field(
        min_length=1
    )

class ProgramUpdateRequest(ProgramCreateRequest):
    pass


class ProgramVisibilityRequest(BaseModel):
    is_hidden: bool


class ProgramAccessUpdateRequest(BaseModel):
    is_active: bool


class ProgramTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class ProgramStageItemResponse(BaseModel):
    id: uuid.UUID
    item_type: ProgramItemType
    order_index: int

    content_id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    speciality_id: uuid.UUID | None = None
    speciality_name: str | None = None

    can_access: bool = True
    is_completed: bool = False

    # Заполняется для опросника при просмотре
    # программы конкретного пациента.
    submission_id: uuid.UUID | None = None
    submission_status: (
        QuestionnaireSubmissionStatus | None
    ) = None


class ProgramStagePatientResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    day_from: int
    day_to: int
    order_index: int

    status: ProgramStageStatus
    progress_percent: float

    items: list[ProgramStageItemResponse]


class ProgramStageClinicalResponse(
    ProgramStagePatientResponse
):
    doctor_description: str | None


class ProgramEnrollmentResponse(BaseModel):
    id: uuid.UUID
    status: ProgramEnrollmentStatus

    started_at: datetime
    completed_at: datetime | None

    elapsed_days: int


class ProgramPatientResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    service: MedicalServicePatientResponse | None
    is_popular: bool

    is_start: bool = False
    home_priority: int = 0

    tags: list[ProgramTagResponse]

    has_program_access: bool
    purchase_requested: bool

    progress_percent: float
    enrollment: ProgramEnrollmentResponse | None

    stages: list[ProgramStagePatientResponse]


class ProgramClinicalResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    service: MedicalServiceStaffResponse | None
    is_popular: bool

    is_start: bool = False
    home_priority: int = 0

    is_hidden: bool

    tags: list[ProgramTagResponse]
    stages: list[ProgramStageClinicalResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    hidden_at: datetime | None


class ProgramStartResponse(BaseModel):
    enrollment_id: uuid.UUID
    program_id: uuid.UUID
    status: ProgramEnrollmentStatus
    started_at: datetime


class ProgramPurchaseRequestResponse(BaseModel):
    program_id: uuid.UUID
    requested_at: datetime
    message: str


class PatientProgramAccessItem(BaseModel):
    program_id: uuid.UUID
    title: str

    service: MedicalServiceStaffResponse | None
    is_popular: bool

    is_hidden: bool
    is_active: bool

    purchase_requested: bool
    requested_at: datetime | None
    activated_at: datetime | None

class PatientProgramClinicalResponse(
    ProgramPatientResponse
):
    service: MedicalServiceStaffResponse | None
    is_hidden: bool
    stages: list[ProgramStageClinicalResponse]

# ./backend/app/modules/programs/enums.py
from enum import Enum


class ProgramItemType(str, Enum):
    ARTICLE = "article"
    QUESTIONNAIRE = "questionnaire"
    CONSULTATION = "consultation"


class ProgramEnrollmentStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ProgramStageStatus(str, Enum):
    UPCOMING = "upcoming"
    AVAILABLE = "available"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"

# ./backend/app/modules/programs/utils.py
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlmodel import Session, select

from app.modules.articles.models import ArticleProgress
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.programs.enums import (
    ProgramEnrollmentStatus,
    ProgramItemType,
    ProgramStageStatus,
)
from app.modules.programs.models import (
    PatientProgramAccess,
    Program,
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
    ProgramTagLink,
)
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)
from app.modules.questionnaires.models import (
    QuestionnaireSubmission,
)
from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def normalize_datetime(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value

def get_program_questionnaire_submission(
    *,
    session: Session,
    patient_id: uuid.UUID,
    item: ProgramStageItem,
) -> QuestionnaireSubmission | None:
    if (
        item.item_type
        != ProgramItemType.QUESTIONNAIRE
    ):
        return None

    stage = session.get(
        ProgramStage,
        item.stage_id,
    )

    if not stage:
        return None

    # Сначала ищем завершённую попытку.
    completed_submission = session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient_id,
            QuestionnaireSubmission.questionnaire_id
            == item.questionnaire_id,
            QuestionnaireSubmission.program_id
            == stage.program_id,
            QuestionnaireSubmission.program_stage_id
            == stage.id,
            QuestionnaireSubmission.status
            == QuestionnaireSubmissionStatus.COMPLETED,
        )
        .order_by(
            QuestionnaireSubmission.completed_at.desc()
        )
    ).first()

    if completed_submission:
        return completed_submission

    # Если завершённой нет, возвращаем последнюю
    # незавершённую попытку.
    return session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient_id,
            QuestionnaireSubmission.questionnaire_id
            == item.questionnaire_id,
            QuestionnaireSubmission.program_id
            == stage.program_id,
            QuestionnaireSubmission.program_stage_id
            == stage.id,
        )
        .order_by(
            QuestionnaireSubmission.started_at.desc()
        )
    ).first()

def get_program_tag_ids(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id == program_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_program_tags(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id == program_id
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


def validate_program_periods(program_data) -> None:
    stages = sorted(
        program_data.stages,
        key=lambda item: item.day_from,
    )

    if len({
        stage.order_index
        for stage in stages
    }) != len(stages):
        raise HTTPException(
            status_code=422,
            detail="Порядок этапов должен быть уникальным",
        )

    previous = None

    for stage in stages:
        if previous and stage.day_from <= previous.day_to:
            raise HTTPException(
                status_code=422,
                detail="Периоды этапов не должны пересекаться",
            )

        if len({
            item.order_index
            for item in stage.items
        }) != len(stage.items):
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Порядок элементов этапа "
                    f"«{stage.title}» должен быть уникальным"
                ),
            )

        previous = stage


def get_patient_program_access(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> PatientProgramAccess | None:
    return session.exec(
        select(PatientProgramAccess).where(
            PatientProgramAccess.patient_id
            == patient_id,
            PatientProgramAccess.program_id
            == program_id,
        )
    ).first()


def patient_has_program_access(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> bool:
    access = get_patient_program_access(
        session=session,
        patient_id=patient_id,
        program_id=program_id,
    )

    return bool(access and access.is_active)


def get_program_enrollment(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> ProgramEnrollment | None:
    return session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.patient_id
            == patient_id,
            ProgramEnrollment.program_id
            == program_id,
        )
    ).first()


def is_program_item_completed(
    *,
    session: Session,
    patient_id: uuid.UUID,
    item: ProgramStageItem,
) -> bool:
    if item.item_type == ProgramItemType.CONSULTATION:
        return False

    if item.item_type == ProgramItemType.ARTICLE:
        progress = session.exec(
            select(ArticleProgress).where(
                ArticleProgress.patient_id
                == patient_id,
                ArticleProgress.article_id
                == item.article_id,
                ArticleProgress.completed_at.is_not(None),
            )
        ).first()

        return progress is not None

    submission = get_program_questionnaire_submission(
        session=session,
        patient_id=patient_id,
        item=item,
    )

    return bool(
        submission
        and submission.status
        == QuestionnaireSubmissionStatus.COMPLETED
    )


def get_stage_task_items(
    stage: ProgramStage,
) -> list[ProgramStageItem]:
    return [
        item
        for item in stage.items
        if item.item_type
        != ProgramItemType.CONSULTATION
    ]


def calculate_stage_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    stage: ProgramStage,
) -> tuple[int, int, float]:
    task_items = get_stage_task_items(stage)

    if not task_items:
        return 0, 0, 100.0

    completed_count = sum(
        1
        for item in task_items
        if is_program_item_completed(
            session=session,
            patient_id=patient_id,
            item=item,
        )
    )

    percentage = round(
        completed_count / len(task_items) * 100,
        2,
    )

    return (
        completed_count,
        len(task_items),
        percentage,
    )


def calculate_stage_status(
    *,
    session: Session,
    patient_id: uuid.UUID,
    stage: ProgramStage,
    elapsed_days: int | None,
) -> ProgramStageStatus:
    if elapsed_days is None:
        return ProgramStageStatus.UPCOMING

    completed, total, _ = calculate_stage_progress(
        session=session,
        patient_id=patient_id,
        stage=stage,
    )

    if total == 0 and elapsed_days >= stage.day_from:
        return ProgramStageStatus.COMPLETED

    if total > 0 and completed == total:
        return ProgramStageStatus.COMPLETED

    if elapsed_days < stage.day_from:
        return ProgramStageStatus.UPCOMING

    if elapsed_days > stage.day_to:
        return ProgramStageStatus.OVERDUE

    if completed > 0:
        return ProgramStageStatus.IN_PROGRESS

    return ProgramStageStatus.AVAILABLE


def calculate_program_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program: Program,
) -> tuple[int, int, float]:
    task_items = [
        item
        for stage in program.stages
        for item in stage.items
        if item.item_type
        != ProgramItemType.CONSULTATION
    ]

    if not task_items:
        return 0, 0, 100.0

    completed_count = sum(
        1
        for item in task_items
        if is_program_item_completed(
            session=session,
            patient_id=patient_id,
            item=item,
        )
    )

    return (
        completed_count,
        len(task_items),
        round(
            completed_count / len(task_items) * 100,
            2,
        ),
    )


def sync_program_enrollment(
    *,
    session: Session,
    enrollment: ProgramEnrollment,
) -> None:
    if (
        enrollment.status
        != ProgramEnrollmentStatus.ACTIVE
    ):
        return

    program = session.get(
        Program,
        enrollment.program_id,
    )

    if not program:
        return

    completed, total, _ = calculate_program_progress(
        session=session,
        patient_id=enrollment.patient_id,
        program=program,
    )

    now = utc_now()

    if (
        completed > 0
        and enrollment.in_progress_event_at is None
    ):
        enrollment.in_progress_event_at = now

        record_event(
            session=session,
            event_type=EventType.PROGRAM_IN_PROGRESS,
            patient_id=enrollment.patient_id,
            program_id=program.id,
            subject_type="program",
            subject_id=program.id,
        )

    if (
        total > 0
        and completed == total
        and enrollment.completed_event_at is None
    ):
        enrollment.status = (
            ProgramEnrollmentStatus.COMPLETED
        )
        enrollment.completed_at = now
        enrollment.completed_event_at = now

        record_event(
            session=session,
            event_type=EventType.PROGRAM_COMPLETED,
            patient_id=enrollment.patient_id,
            program_id=program.id,
            subject_type="program",
            subject_id=program.id,
        )

    enrollment.updated_at = now
    session.add(enrollment)


def sync_patient_program_enrollments(
    *,
    session: Session,
    patient_id: uuid.UUID,
) -> None:
    enrollments = session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.patient_id == patient_id,
            ProgramEnrollment.status
            == ProgramEnrollmentStatus.ACTIVE,
        )
    ).all()

    for enrollment in enrollments:
        sync_program_enrollment(
            session=session,
            enrollment=enrollment,
        )

def get_program_content_item(
    *,
    session: Session,
    program_id: uuid.UUID,
    content_type: ProgramItemType,
    content_id: uuid.UUID,
    stage_id: uuid.UUID | None = None,
) -> ProgramStageItem | None:
    statement = (
        select(ProgramStageItem)
        .join(
            ProgramStage,
            ProgramStage.id
            == ProgramStageItem.stage_id,
        )
        .where(
            ProgramStage.program_id == program_id,
            ProgramStageItem.item_type == content_type,
        )
    )

    if stage_id:
        statement = statement.where(
            ProgramStage.id == stage_id
        )

    if content_type == ProgramItemType.ARTICLE:
        statement = statement.where(
            ProgramStageItem.article_id == content_id
        )

    elif (
        content_type
        == ProgramItemType.QUESTIONNAIRE
    ):
        statement = statement.where(
            ProgramStageItem.questionnaire_id
            == content_id
        )

    return session.exec(statement).first()


def ensure_patient_program_content_access(
    *,
    session: Session,
    patient,
    program_id: uuid.UUID,
    content_type: ProgramItemType,
    content_id: uuid.UUID,
    pro_content: bool,
    stage_id: uuid.UUID | None = None,
) -> ProgramStageItem:
    from app.modules.content.utils import (
        patient_can_see_content,
    )

    program = session.get(Program, program_id)

    if not program or program.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    item = get_program_content_item(
        session=session,
        program_id=program.id,
        content_type=content_type,
        content_id=content_id,
        stage_id=stage_id,
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Контент не входит в эту программу",
        )

    has_access = patient_has_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    can_see_program = patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=get_program_tag_ids(
            session=session,
            program_id=program.id,
        ),
        is_hidden=program.is_hidden,
    )

    if not has_access and not can_see_program:
        raise HTTPException(
            status_code=403,
            detail="Программа недоступна пациенту",
        )

    # Глобальный Pro здесь намеренно не используется.
    if pro_content and not has_access:
        raise HTTPException(
            status_code=403,
            detail=(
                "Для этого материала необходима "
                "покупка программы"
            ),
        )

    return item

урезанный афйл роутов программ:
# ./backend/app/modules/programs/routers.py

import uuid
from datetime import datetime, timezone
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlmodel import Session, select
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    require_roles,
)
from app.modules.articles.models import Article
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
    patient_can_see_content,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.service import (
    send_notification,
)
from app.modules.programs.enums import (
    ProgramItemType,
    ProgramStageStatus,
)
from app.modules.programs.models import (
    PatientProgramAccess,
    Program,
    ProgramEnrollment,
    ProgramStage,
    ProgramStageItem,
    ProgramTagLink,
)
from app.modules.programs.schemas import (
    PatientProgramAccessItem,
    ProgramAccessUpdateRequest,
    ProgramClinicalResponse,
    ProgramCreateRequest,
    ProgramEnrollmentResponse,
    ProgramPatientResponse,
    ProgramPurchaseRequestResponse,
    ProgramStageClinicalResponse,
    ProgramStageItemResponse,
    ProgramStagePatientResponse,
    ProgramStartResponse,
    ProgramTagResponse,
    ProgramUpdateRequest,
    ProgramVisibilityRequest,
    PatientProgramClinicalResponse,
)
from app.modules.programs.utils import (
    calculate_program_progress,
    calculate_stage_progress,
    calculate_stage_status,
    get_patient_program_access,
    get_program_enrollment,
    get_program_questionnaire_submission,
    get_program_tag_ids,
    get_program_tags,
    is_program_item_completed,
    normalize_datetime,
    patient_has_program_access,
    validate_program_periods,
    sync_program_enrollment,
)
from app.modules.questionnaires.models import (
    Questionnaire,
)
from app.modules.tags.models import Tag
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    Speciality,
    UserRoleLink,
    PatientProfile,
    User,
)
from app.modules.services.models import MedicalService
from app.modules.services.schemas import (
    MedicalServicePatientResponse,
    MedicalServiceStaffResponse,
)
from app.core.transactions import lock_patient_for_write
from app.modules.notifications.transactional import (
    create_in_app_notification,
    publish_saved_notifications,
    snapshot_notifications,
)

def get_program_service(
    *,
    session: Session,
    program: Program,
) -> MedicalService | None:
    FUNCTION BODY
    return service
def serialize_program_service_for_patient(
    *,
    session: Session,
    program: Program,
) -> MedicalServicePatientResponse | None:
    FUNCTION BODY
    return MedicalServicePatientResponse.model_validate(
        service
    )
def serialize_program_service_for_staff(
    *,
    session: Session,
    program: Program,
) -> MedicalServiceStaffResponse | None:
    FUNCTION BODY
    return MedicalServiceStaffResponse.model_validate(
        service
    )
def validate_start_program(
    *,
    session: Session,
    payload: ProgramCreateRequest | ProgramUpdateRequest,
    is_start: bool,
) -> None:
    FUNCTION BODY
                raise HTTPException(
                    status_code=422,
                    detail=(
                        "В стартовую программу можно включать "
                        "только нескрытые бесплатные материалы"
                    ),
                )
def validate_program_service_choice(
    *,
    session: Session,
    service_id: uuid.UUID | None,
    current_service_id: uuid.UUID | None = None,
) -> MedicalService | None:
    FUNCTION BODY
    return service
def fill_program_structure(
    *,
    session: Session,
    program: Program,
    payload: ProgramCreateRequest | ProgramUpdateRequest,
) -> None:
    FUNCTION BODY
                    raise HTTPException(
                        status_code=404,
                        detail="Специальность не найдена",
                    )
def utc_now() -> datetime:
    FUNCTION BODY
    return datetime.now(timezone.utc)
def serialize_item(
    *,
    session: Session,
    item: ProgramStageItem,
) -> ProgramStageItemResponse:
    FUNCTION BODY
    return ProgramStageItemResponse(
        id=item.id,
        item_type=item.item_type,
        order_index=item.order_index,

        # Для консультации content_id соответствует
        # специальности.
        content_id=speciality.id,

        title=(
            item.consultation_title
            or speciality.consultation_name
            or f"Консультация: {speciality.name}"
        ),
        description=(
            item.consultation_description
            if item.consultation_description is not None
            else speciality.consultation_description
        ),

        pro_content=False,
        is_hidden=False,

        speciality_id=speciality.id,
        speciality_name=speciality.name,

        can_access=True,

        # Консультация не считается заданием.
        is_completed=False,

        submission_id=None,
        submission_status=None,
    )
def serialize_patient_stage_items(
    *,
    session: Session,
    stage: ProgramStage,
    patient: PatientProfile,
    has_program_access: bool,
) -> list[ProgramStageItemResponse]:
    FUNCTION BODY
    return result
def serialize_patient_program(
    *,
    session: Session,
    program: Program,
    patient: PatientProfile,
) -> ProgramPatientResponse:
    FUNCTION BODY
    return ProgramPatientResponse(
        id=program.id,
        title=program.title,
        description=program.description,

        service=serialize_program_service_for_patient(
            session=session,
            program=program,
        ),
        is_popular=program.is_popular,
        is_start=program.is_start,
        home_priority=program.home_priority,

        tags=[
            ProgramTagResponse(
                id=tag.id,
                name=tag.name,
                description=tag.description,
            )
            for tag in tags
        ],

        has_program_access=has_program_access,
        purchase_requested=bool(
            access
            and access.purchase_requested
            and not access.is_active
        ),

        progress_percent=program_progress,
        enrollment=enrollment_response,
        stages=stages,
    )
def serialize_clinical_program(
    *,
    session: Session,
    program: Program,
) -> ProgramClinicalResponse:
    FUNCTION BODY
    return ProgramClinicalResponse(
        id=program.id,
        title=program.title,
        description=program.description,

        service=serialize_program_service_for_staff(
            session=session,
            program=program,
        ),
        is_popular=program.is_popular,
        is_start=program.is_start,
        home_priority=program.home_priority,

        is_hidden=program.is_hidden,

        tags=[
            ProgramTagResponse(
                id=tag.id,
                name=tag.name,
                description=tag.description,
            )
            for tag in tags
        ],

        stages=stages,

        created_by_user_id=program.created_by_user_id,
        created_at=program.created_at,
        updated_at=program.updated_at,
        hidden_at=program.hidden_at,
    )
@@router.post(
    "/manage",
    response_model=ProgramClinicalResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_program(
    payload: ProgramCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> ProgramClinicalResponse:
    FUNCTION BODY
        raise
@@router.get(
    "/manage",
    response_model=list[ProgramClinicalResponse],
)
async def list_programs_for_staff(
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> list[ProgramClinicalResponse]:
    FUNCTION BODY
    return [
        serialize_clinical_program(
            session=session,
            program=program,
        )
        for program in programs
    ]
@@router.get(
    "/manage/{program_id}",
    response_model=ProgramClinicalResponse,
)
async def get_program_for_staff(
    program_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ProgramClinicalResponse:
    FUNCTION BODY
    return serialize_clinical_program(
        session=session,
        program=program,
    )
@@router.get(
    "/patient",
    response_model=list[ProgramPatientResponse],
)
async def list_programs_for_patient(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[ProgramPatientResponse]:
    FUNCTION BODY
    return result
@@router.get(
    "/patient/{program_id}",
    response_model=ProgramPatientResponse,
)
async def get_program_for_patient(
    program_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ProgramPatientResponse:
    FUNCTION BODY
    return serialize_patient_program(
        session=session,
        program=program,
        patient=patient,
    )
@@router.patch(
    "/manage/{program_id}/visibility",
    response_model=ProgramClinicalResponse,
)
async def change_program_visibility(
    program_id: uuid.UUID,
    payload: ProgramVisibilityRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> ProgramClinicalResponse:
    FUNCTION BODY
    return serialize_clinical_program(
        session=session,
        program=program,
        is_start=program.is_start,
        home_priority=program.home_priority,
    )
@@router.put(
    "/manage/{program_id}",
    response_model=ProgramClinicalResponse,
)
async def update_program(
    program_id: uuid.UUID,
    payload: ProgramUpdateRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> ProgramClinicalResponse:
    FUNCTION BODY
    return serialize_clinical_program(
        session=session,
        program=program,
    )
@@router.post(
    "/patient/{program_id}/start",
    response_model=ProgramStartResponse,
)
async def start_program(
    program_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ProgramStartResponse:
    FUNCTION BODY
    return ProgramStartResponse(
        enrollment_id=enrollment.id,
        program_id=program.id,
        status=enrollment.status,
        started_at=enrollment.started_at,
    )
@@router.post(
    "/patient/{program_id}/request-purchase",
    response_model=ProgramPurchaseRequestResponse,
)
async def request_program_purchase(
    program_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ProgramPurchaseRequestResponse:
    FUNCTION BODY
    return response
@@router.get(
    "/manage/patient/{patient_id}/access",
    response_model=list[PatientProgramAccessItem],
)
async def list_patient_program_access(
    patient_id: uuid.UUID,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> list[PatientProgramAccessItem]:
    FUNCTION BODY
    return result
@@router.patch(
    "/manage/patient/{patient_id}/access/{program_id}",
    response_model=PatientProgramAccessItem,
)
async def update_patient_program_access(
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
    payload: ProgramAccessUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> PatientProgramAccessItem:
    FUNCTION BODY
    return PatientProgramAccessItem(
        program_id=program.id,
        title=program.title,

        service=serialize_program_service_for_staff(
            session=session,
            program=program,
        ),
        is_popular=program.is_popular,

        purchase_requested=bool(
            access.purchase_requested
        ),

        is_hidden=program.is_hidden,
        is_active=access.is_active,
        requested_at=access.requested_at,
        activated_at=access.activated_at,
    )
def serialize_patient_clinical_program(
    *,
    session: Session,
    program: Program,
    patient: PatientProfile,
) -> PatientProgramClinicalResponse:
    FUNCTION BODY
    return PatientProgramClinicalResponse(
        id=patient_response.id,
        title=patient_response.title,
        description=patient_response.description,

        # Этот ответ предназначен для сотрудников,
        # поэтому содержит технический код услуги.
        service=serialize_program_service_for_staff(
            session=session,
            program=program,
        ),
        is_popular=patient_response.is_popular,
        is_start=patient_response.is_start,
        home_priority=patient_response.home_priority,

        tags=patient_response.tags,

        has_program_access=(
            patient_response.has_program_access
        ),
        purchase_requested=(
            patient_response.purchase_requested
        ),

        progress_percent=(
            patient_response.progress_percent
        ),
        enrollment=patient_response.enrollment,

        is_hidden=program.is_hidden,
        stages=clinical_stages,
    )
@@router.get(
    "/manage/patient/{patient_id}/progress",
    response_model=list[PatientProgramClinicalResponse],
)
async def list_patient_program_progress(
    patient_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> list[PatientProgramClinicalResponse]:
    FUNCTION BODY
    return [
        serialize_patient_clinical_program(
            session=session,
            program=program,
            patient=patient,
        )
        for program in programs
    ]

урезанные роуты статей
# ./backend/app/modules/articles/routers.py

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
from app.modules.articles.access import ensure_article_access
from app.core.transactions import lock_patient_for_write
from app.modules.articles.tracking import (
    record_article_interaction_event,
)

def utc_now() -> datetime:
    FUNCTION BODY
    return datetime.now(timezone.utc)
def get_article_event_counts(
    *,
    session: Session,
    before: datetime | None = None,
) -> dict[uuid.UUID, dict[str, int]]:
    FUNCTION BODY
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
    FUNCTION BODY
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
    FUNCTION BODY
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Требуется Pro-доступ",
        )
@@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    FUNCTION BODY
    return items[offset:offset + limit]
@@router.get(
    "/{article_id}",
    response_model=ArticleResponse,
)
async def get_article(
    article_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    FUNCTION BODY
    return serialize_article(
        session=session,
        article=article,
    )
@@router.post(
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
    FUNCTION BODY
    return serialize_article(
        session=session,
        article=article,
    )
@@router.patch(
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
    FUNCTION BODY
    return serialize_article(
        session=session,
        article=article,
    )
@@router.patch(
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
    FUNCTION BODY
    return serialize_article(
        session=session,
        article=article,
    )
@@router.get(
    "/{article_id}/progress",
    response_model=ArticleProgressResponse,
)
async def get_article_progress(
    article_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleProgressResponse:
    FUNCTION BODY
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
@@router.put(
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
    FUNCTION BODY
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
@@router.post(
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
    FUNCTION BODY
    return ArticleOpenResponse(
        event_id=event.id,
        interaction_id=event.interaction_id,
    )

# ./backend/app/modules/questionnaires/enums.py
from enum import Enum


class QuestionType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"

    SCALE = "scale"
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"


class QuestionnaireSubmissionStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

# ./backend/app/modules/questionnaires/models.py
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import Column, JSON, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
    QuestionType,
)
from app.modules.tags.models import Tag


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Questionnaire(SQLModel, table=True):
    __tablename__ = "questionnaires"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str = Field(index=True, max_length=300)
    description: Optional[str] = Field(default=None)

    pro_content: bool = Field(default=True, index=True)
    is_hidden: bool = Field(default=False, index=True)

    copied_from_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="questionnaires.id",
        index=True,
    )

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

    questions: list["Question"] = Relationship(
        back_populates="questionnaire",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "Question.order_index",
        },
    )

    tag_links: list["QuestionnaireTagLink"] = Relationship(
        back_populates="questionnaire",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class Question(SQLModel, table=True):
    __tablename__ = "questions"
    __table_args__ = (
        UniqueConstraint(
            "questionnaire_id",
            "order_index",
            name="uq_questionnaire_question_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )

    question_type: QuestionType = Field(index=True)
    text: str
    is_required: bool = Field(default=True)

    order_index: int = Field(index=True)

    scale_min: Optional[int] = Field(default=None)
    scale_max: Optional[int] = Field(default=None)
    scale_min_label: Optional[str] = Field(default=None)
    scale_max_label: Optional[str] = Field(default=None)

    questionnaire: Optional[Questionnaire] = Relationship(
        back_populates="questions"
    )

    options: list["QuestionOption"] = Relationship(
        back_populates="question",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "order_by": "QuestionOption.order_index",
        },
    )


class QuestionOption(SQLModel, table=True):
    __tablename__ = "question_options"
    __table_args__ = (
        UniqueConstraint(
            "question_id",
            "order_index",
            name="uq_question_option_order",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    question_id: uuid.UUID = Field(
        foreign_key="questions.id",
        index=True,
    )

    text: str
    order_index: int = Field(index=True)

    question: Optional[Question] = Relationship(
        back_populates="options"
    )


class QuestionnaireTagLink(SQLModel, table=True):
    __tablename__ = "questionnaire_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "questionnaire_id",
            "tag_id",
            name="uq_questionnaire_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    questionnaire: Optional[Questionnaire] = Relationship(
        back_populates="tag_links"
    )

    tag: Optional[Tag] = Relationship()


class QuestionnaireSubmission(SQLModel, table=True):
    __tablename__ = "questionnaire_submissions"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    questionnaire_id: uuid.UUID = Field(
        foreign_key="questionnaires.id",
        index=True,
    )
    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )

    # Если опросник запущен внутри программы.
    program_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="programs.id",
        index=True,
    )
    program_stage_id: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="program_stages.id",
        index=True,
    )

    status: QuestionnaireSubmissionStatus = Field(
        default=QuestionnaireSubmissionStatus.IN_PROGRESS,
        index=True,
    )

    started_at: datetime = Field(default_factory=utc_now)
    completed_at: Optional[datetime] = Field(default=None)

    answers: list["QuestionAnswer"] = Relationship(
        back_populates="submission",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class QuestionAnswer(SQLModel, table=True):
    __tablename__ = "question_answers"
    __table_args__ = (
        UniqueConstraint(
            "submission_id",
            "question_id",
            name="uq_submission_question_answer",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    submission_id: uuid.UUID = Field(
        foreign_key="questionnaire_submissions.id",
        index=True,
    )
    question_id: uuid.UUID = Field(
        foreign_key="questions.id",
        index=True,
    )

    value_json: Any = Field(
        sa_column=Column(JSON, nullable=False)
    )

    created_at: datetime = Field(default_factory=utc_now)

    submission: Optional[QuestionnaireSubmission] = Relationship(
        back_populates="answers"
    )

# ./backend/app/modules/questionnaires/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, model_validator

from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
    QuestionType,
)


class QuestionOptionCreateRequest(BaseModel):
    text: str = Field(min_length=1)
    order_index: int = Field(ge=0)


class QuestionCreateRequest(BaseModel):
    question_type: QuestionType
    text: str = Field(min_length=1)
    is_required: bool = True
    order_index: int = Field(ge=0)

    scale_min: int | None = None
    scale_max: int | None = None
    scale_min_label: str | None = None
    scale_max_label: str | None = None

    options: list[QuestionOptionCreateRequest] = []

    @model_validator(mode="after")
    def validate_question(self):
        choice_types = {
            QuestionType.SINGLE_CHOICE,
            QuestionType.MULTIPLE_CHOICE,
        }

        if (
            self.question_type in choice_types
            and len(self.options) < 2
        ):
            raise ValueError(
                "В вопросе с вариантами ответа "
                "должно быть не менее двух вариантов"
            )

        if self.question_type == QuestionType.SCALE:
            if (
                self.scale_min is None
                or self.scale_max is None
            ):
                raise ValueError(
                    "Для шкалы нужны scale_min и scale_max"
                )

            if self.scale_max <= self.scale_min:
                raise ValueError(
                    "scale_max должен быть больше scale_min"
                )

        return self


class QuestionnaireCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    description: str | None = None

    tag_ids: list[uuid.UUID] = []
    pro_content: bool = True

    copied_from_id: uuid.UUID | None = None

    questions: list[QuestionCreateRequest] = Field(
        min_length=1
    )


class QuestionnaireCopyRequest(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )


class QuestionnaireVisibilityRequest(BaseModel):
    is_hidden: bool


class QuestionOptionResponse(BaseModel):
    id: uuid.UUID
    text: str
    order_index: int


class QuestionResponse(BaseModel):
    id: uuid.UUID
    question_type: QuestionType
    text: str
    is_required: bool
    order_index: int

    scale_min: int | None
    scale_max: int | None
    scale_min_label: str | None
    scale_max_label: str | None

    options: list[QuestionOptionResponse]


class QuestionnaireTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None


class QuestionnaireResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    copied_from_id: uuid.UUID | None

    tags: list[QuestionnaireTagResponse]
    questions: list[QuestionResponse]

    created_by_user_id: uuid.UUID
    created_at: datetime
    hidden_at: datetime | None


class QuestionnaireListItem(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    pro_content: bool
    is_hidden: bool

    tags: list[QuestionnaireTagResponse]

    questions_count: int
    created_at: datetime


class SubmissionStartResponse(BaseModel):
    submission_id: uuid.UUID
    questionnaire_id: uuid.UUID
    status: QuestionnaireSubmissionStatus
    started_at: datetime


class AnswerSubmitRequest(BaseModel):
    question_id: uuid.UUID
    value: Any


class SubmissionCompleteRequest(BaseModel):
    answers: list[AnswerSubmitRequest]


class AnswerResponse(BaseModel):
    question_id: uuid.UUID
    question_text: str
    question_type: QuestionType
    value: Any


class SubmissionResponse(BaseModel):
    id: uuid.UUID
    questionnaire_id: uuid.UUID
    patient_id: uuid.UUID

    program_id: uuid.UUID | None
    program_stage_id: uuid.UUID | None

    status: QuestionnaireSubmissionStatus
    started_at: datetime
    completed_at: datetime | None

    answers: list[AnswerResponse]

class AnswerSaveRequest(BaseModel):
    question_id: uuid.UUID
    value: Any


class AnswerSaveResponse(BaseModel):
    submission_id: uuid.UUID
    question_id: uuid.UUID
    value: Any
    saved_at: datetime


class SubmissionProgressItem(BaseModel):
    submission_id: uuid.UUID
    questionnaire_id: uuid.UUID
    questionnaire_title: str

    program_id: uuid.UUID | None
    program_stage_id: uuid.UUID | None

    status: QuestionnaireSubmissionStatus
    answered_questions: int
    questions_count: int
    progress_percent: float

    started_at: datetime
    completed_at: datetime | None
# ./backend/app/modules/questionnaires/utils.py
import uuid
from typing import Any

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.questionnaires.enums import QuestionType
from app.modules.questionnaires.models import (
    Question,
    Questionnaire,
    QuestionnaireTagLink,
)
from app.modules.questionnaires.schemas import (
    AnswerSubmitRequest,
)
from app.modules.tags.models import Tag


def get_questionnaire_tag_ids(
    *,
    session: Session,
    questionnaire_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(QuestionnaireTagLink).where(
            QuestionnaireTagLink.questionnaire_id
            == questionnaire_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_questionnaire_tags(
    *,
    session: Session,
    questionnaire_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(QuestionnaireTagLink).where(
            QuestionnaireTagLink.questionnaire_id
            == questionnaire_id
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


def validate_questionnaire_answers(
    *,
    questionnaire: Questionnaire,
    answers: list[AnswerSubmitRequest],
) -> dict[uuid.UUID, Any]:
    answers_by_question = {
        answer.question_id: answer.value
        for answer in answers
    }

    question_ids = {
        question.id
        for question in questionnaire.questions
    }

    unknown_ids = set(answers_by_question) - question_ids

    if unknown_ids:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Передан ответ на неизвестный вопрос",
        )

    normalized_answers: dict[uuid.UUID, Any] = {}

    for question in questionnaire.questions:
        has_answer = question.id in answers_by_question

        if question.is_required and not has_answer:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=(
                    f"Не заполнен обязательный вопрос: "
                    f"{question.text}"
                ),
            )

        if not has_answer:
            continue

        value = answers_by_question[question.id]

        if question.question_type == QuestionType.TEXT:
            if not isinstance(value, str):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается текст: {question.text}",
                )

        elif question.question_type == QuestionType.NUMBER:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
            ):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается число: {question.text}",
                )

        elif question.question_type == QuestionType.BOOLEAN:
            if not isinstance(value, bool):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Ожидается логическое значение: "
                        f"{question.text}"
                    ),
                )

        elif question.question_type == QuestionType.SCALE:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
            ):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается число шкалы: {question.text}",
                )

            if (
                value < question.scale_min
                or value > question.scale_max
            ):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Значение шкалы вне диапазона: "
                        f"{question.text}"
                    ),
                )

        elif (
            question.question_type
            == QuestionType.SINGLE_CHOICE
        ):
            option_ids = {
                str(option.id)
                for option in question.options
            }

            if str(value) not in option_ids:
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Неизвестный вариант ответа: "
                        f"{question.text}"
                    ),
                )

            value = str(value)

        elif (
            question.question_type
            == QuestionType.MULTIPLE_CHOICE
        ):
            if not isinstance(value, list):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Ожидается список вариантов: "
                        f"{question.text}"
                    ),
                )

            option_ids = {
                str(option.id)
                for option in question.options
            }
            selected_ids = [str(item) for item in value]

            if not set(selected_ids).issubset(option_ids):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Передан неизвестный вариант: "
                        f"{question.text}"
                    ),
                )

            value = list(dict.fromkeys(selected_ids))

        normalized_answers[question.id] = value

    return normalized_answers

def normalize_question_answer(
    *,
    question: Question,
    value: Any,
) -> Any:
    if question.question_type == QuestionType.TEXT:
        if not isinstance(value, str):
            raise HTTPException(
                status_code=422,
                detail="Ожидается текстовый ответ",
            )

        return value

    if question.question_type == QuestionType.NUMBER:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise HTTPException(
                status_code=422,
                detail="Ожидается числовой ответ",
            )

        return value

    if question.question_type == QuestionType.BOOLEAN:
        if not isinstance(value, bool):
            raise HTTPException(
                status_code=422,
                detail="Ожидается значение Да или Нет",
            )

        return value

    if question.question_type == QuestionType.SCALE:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise HTTPException(
                status_code=422,
                detail="Ожидается значение шкалы",
            )

        if (
            value < question.scale_min
            or value > question.scale_max
        ):
            raise HTTPException(
                status_code=422,
                detail="Значение находится вне диапазона шкалы",
            )

        return value

    option_ids = {
        str(option.id)
        for option in question.options
    }

    if question.question_type == QuestionType.SINGLE_CHOICE:
        normalized_value = str(value)

        if normalized_value not in option_ids:
            raise HTTPException(
                status_code=422,
                detail="Неизвестный вариант ответа",
            )

        return normalized_value

    if question.question_type == QuestionType.MULTIPLE_CHOICE:
        if not isinstance(value, list):
            raise HTTPException(
                status_code=422,
                detail="Ожидается список вариантов",
            )

        normalized_values = list(
            dict.fromkeys(
                str(item)
                for item in value
            )
        )

        if not set(normalized_values).issubset(option_ids):
            raise HTTPException(
                status_code=422,
                detail="Передан неизвестный вариант ответа",
            )

        return normalized_values

    raise HTTPException(
        status_code=422,
        detail="Неизвестный тип вопроса",
    )

урезанные роуты опросников:
# ./backend/app/modules/questionnaires/routers.py

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
from app.modules.content.utils import (
    ensure_patient_content_access,
    get_patient_profile_by_user_id,
    patient_can_access_content,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.questionnaires.enums import (
    QuestionnaireSubmissionStatus,
)
from app.modules.questionnaires.models import (
    Question,
    QuestionAnswer,
    Questionnaire,
    QuestionnaireSubmission,
    QuestionnaireTagLink,
    QuestionOption,
)
from app.modules.questionnaires.schemas import (
    AnswerResponse,
    AnswerSaveRequest,
    AnswerSaveResponse,
    QuestionOptionResponse,
    QuestionnaireCopyRequest,
    QuestionnaireCreateRequest,
    QuestionnaireListItem,
    QuestionnaireResponse,
    QuestionnaireTagResponse,
    QuestionnaireVisibilityRequest,
    QuestionResponse,
    SubmissionCompleteRequest,
    SubmissionProgressItem,
    SubmissionResponse,
    SubmissionStartResponse,
)
from app.modules.questionnaires.utils import (
    get_questionnaire_tag_ids,
    get_questionnaire_tags,
    normalize_question_answer,
    validate_questionnaire_answers,
)
from app.modules.tags.models import Tag
from app.modules.users.enums import UserRole
from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import (
    mark_assignment_completed,
    mark_assignment_in_progress,
    patient_has_active_assignment,
)
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.service import (
    send_notification,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    UserRole,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
)
from app.modules.programs.utils import (
    sync_patient_program_enrollments,
)

def utc_now() -> datetime:
    FUNCTION BODY
    return datetime.now(timezone.utc)
def serialize_questionnaire(
    *,
    session: Session,
    questionnaire: Questionnaire,
) -> QuestionnaireResponse:
    FUNCTION BODY
    return QuestionnaireResponse(
        id=questionnaire.id,
        title=questionnaire.title,
        description=questionnaire.description,
        pro_content=questionnaire.pro_content,
        is_hidden=questionnaire.is_hidden,
        copied_from_id=questionnaire.copied_from_id,
        tags=[
            QuestionnaireTagResponse(
                id=tag.id,
                name=tag.name,
                description=tag.description,
            )
            for tag in tags
        ],
        questions=[
            QuestionResponse(
                id=question.id,
                question_type=question.question_type,
                text=question.text,
                is_required=question.is_required,
                order_index=question.order_index,
                scale_min=question.scale_min,
                scale_max=question.scale_max,
                scale_min_label=question.scale_min_label,
                scale_max_label=question.scale_max_label,
                options=[
                    QuestionOptionResponse(
                        id=option.id,
                        text=option.text,
                        order_index=option.order_index,
                    )
                    for option in sorted(
                        question.options,
                        key=lambda item: item.order_index,
                    )
                ],
            )
            for question in questions
        ],
        created_by_user_id=questionnaire.created_by_user_id,
        created_at=questionnaire.created_at,
        hidden_at=questionnaire.hidden_at,
    )
def create_questionnaire_from_payload(
    *,
    session: Session,
    payload: QuestionnaireCreateRequest,
    created_by_user_id: uuid.UUID,
    copied_from_id: uuid.UUID | None = None,
) -> Questionnaire:
    FUNCTION BODY
    return questionnaire
@@router.get("", response_model=list[QuestionnaireListItem])
async def list_questionnaires(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[QuestionnaireListItem]:
    FUNCTION BODY
    return result
@@router.get(
    "/{questionnaire_id}",
    response_model=QuestionnaireResponse,
)
async def get_questionnaire(
    questionnaire_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> QuestionnaireResponse:
    FUNCTION BODY
    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )
@@router.post(
    "",
    response_model=QuestionnaireResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_questionnaire(
    payload: QuestionnaireCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> QuestionnaireResponse:
    FUNCTION BODY
    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )
@@router.post(
    "/{questionnaire_id}/copy",
    response_model=QuestionnaireResponse,
    status_code=status.HTTP_201_CREATED,
)
async def copy_questionnaire(
    questionnaire_id: uuid.UUID,
    payload: QuestionnaireCopyRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> QuestionnaireResponse:
    FUNCTION BODY
    return serialize_questionnaire(
        session=session,
        questionnaire=copy,
    )
@@router.patch(
    "/{questionnaire_id}/visibility",
    response_model=QuestionnaireResponse,
)
async def change_questionnaire_visibility(
    questionnaire_id: uuid.UUID,
    payload: QuestionnaireVisibilityRequest,
    _: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> QuestionnaireResponse:
    FUNCTION BODY
    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )
@@router.post(
    "/{questionnaire_id}/start",
    response_model=SubmissionStartResponse,
)
async def start_questionnaire(
    questionnaire_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> SubmissionStartResponse:
    FUNCTION BODY
    return SubmissionStartResponse(
        submission_id=submission.id,
        questionnaire_id=questionnaire.id,
        status=submission.status,
        started_at=submission.started_at,
    )
@@router.post(
    "/submissions/{submission_id}/complete",
    response_model=SubmissionResponse,
)
async def complete_questionnaire(
    submission_id: uuid.UUID,
    payload: SubmissionCompleteRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> SubmissionResponse:
    FUNCTION BODY
    return SubmissionResponse(
        id=submission.id,
        questionnaire_id=(
            submission.questionnaire_id
        ),
        patient_id=submission.patient_id,
        status=submission.status,
        started_at=submission.started_at,
        completed_at=submission.completed_at,
        answers=response_answers,
        program_id=submission.program_id,
        program_stage_id=submission.program_stage_id,
    )
@@router.put(
    "/submissions/{submission_id}/answer",
    response_model=AnswerSaveResponse,
)
async def save_submission_answer(
    submission_id: uuid.UUID,
    payload: AnswerSaveRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> AnswerSaveResponse:
    FUNCTION BODY
    return AnswerSaveResponse(
        submission_id=submission.id,
        question_id=question.id,
        value=answer.value_json,
        saved_at=answer.created_at,
    )
@@router.get(
    "/submissions/mine/progress",
    response_model=list[SubmissionProgressItem],
)
async def get_my_questionnaire_progress(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[SubmissionProgressItem]:
    FUNCTION BODY
    return result
@@router.get(
    "/submissions/{submission_id}",
    response_model=SubmissionResponse,
)
async def get_submission(
    submission_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> SubmissionResponse:
    FUNCTION BODY
    return SubmissionResponse(
        id=submission.id,
        questionnaire_id=submission.questionnaire_id,
        patient_id=submission.patient_id,
        status=submission.status,
        started_at=submission.started_at,
        completed_at=submission.completed_at,
        answers=response_answers,
        program_id=submission.program_id,
        program_stage_id=submission.program_stage_id,
    )

"""program_home_fields

Revision ID: 95f734785945
Revises: 6042112705c7
Create Date: 2026-09-07 00:43:00.920877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '95f734785945'
down_revision: Union[str, Sequence[str], None] = '6042112705c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_events_article_analytics'))

    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.alter_column('invitation_type',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.Enum('DOCTOR', 'PATIENT', 'RELATIVE', 'MED_ASSISTANT', 'SUPERUSER', name='invitationtype'),
               existing_nullable=False)

    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "is_start",
                sa.Boolean(),
                server_default=sa.false(),
                nullable=False,
            )
        )
        batch_op.add_column(
            sa.Column(
                "home_priority",
                sa.Integer(),
                server_default=sa.text("0"),
                nullable=False,
            )
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.drop_column('home_priority')
        batch_op.drop_column('is_start')

    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.alter_column('invitation_type',
               existing_type=sa.Enum('DOCTOR', 'PATIENT', 'RELATIVE', 'MED_ASSISTANT', 'SUPERUSER', name='invitationtype'),
               type_=sa.VARCHAR(length=8),
               existing_nullable=False)

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_events_article_analytics'), ['subject_type', 'event_type', 'subject_id', 'occurred_at'], unique=False)

    # ### end Alembic commands ###
локально у меня база mysql, на сервере - Postgres

Фронтенд:
<!-- ./frontend/app/pages/dashboard.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()

const { isClientReady } = useClientReady()

const roleNames = {
  superuser: 'Суперпользователь',
  med_assistant: 'Медицинский ассистент',
  doctor: 'Врач',
  patient: 'Пациент',
  relative: 'Родственник',
}

const staffRoles = [
  'doctor',
  'med_assistant',
  'superuser',
]

const activeRoleName = computed(() => {
  if (!isClientReady.value) {
    return ''
  }

  return (
    roleNames[auth.activeRole]
    || auth.activeRole
    || ''
  )
})

const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient'
)

const isStaff = computed(() =>
  isClientReady.value
  && staffRoles.includes(auth.activeRole)
)

onMounted(async () => {
  if (!userStore.user) {
    await userStore.fetchMe()
  }
})
</script>

<template>
  <div class="space-y-6">
    <PatientHome v-if="isPatient" />

    <!-- Приветствие -->
    <section
      v-if="!isPatient"
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-8"
    >
      <p
        class="text-base-content/60 min-h-5 text-sm"
      >
        <span v-if="isClientReady">
          {{ activeRoleName }}
        </span>
      </p>

      <h1
        class="mt-1 text-xl font-bold sm:text-2xl"
      >
        Здравствуйте,
        {{ userStore.user?.first_name || 'пользователь' }}
      </h1>
    </section>

    <!-- Dashboard сотрудников -->
    <section
      v-if="isStaff"
      class="space-y-4"
    >
      <div
        class="flex items-center justify-between gap-4"
      >
        <h2 class="text-xl font-bold sm:text-2xl">
          Пациенты
        </h2>

        <NuxtLink
          to="/patients"
          class="btn btn-ghost btn-sm"
        >
          Открыть весь список
        </NuxtLink>
      </div>

      <PatientsList
        compact
        :page-size="10"
      />
    </section>

    <!-- Общие настройки -->
    <section
      v-if="!isPatient"
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <NuxtLink
        to="/settings/security"
        class="card bg-base-100 border-base-300 hover:border-primary border transition"
      >
        <div class="card-body">
          <div
            class="bg-primary/10 text-primary flex size-12 items-center justify-center rounded-2xl"
          >
            <Icon
              name="lucide:shield-check"
              class="size-6"
            />
          </div>

          <h2 class="card-title mt-2">
            Безопасность
          </h2>

          <p class="text-base-content/60 text-sm">
            Добавьте passkey или измените пароль.
          </p>
        </div>
      </NuxtLink>

      <div
        class="card bg-base-100 border-base-300 border"
      >
        <div class="card-body">
          <div
            class="bg-secondary/10 text-secondary flex size-12 items-center justify-center rounded-2xl"
          >
            <Icon
              name="lucide:tags"
              class="size-6"
            />
          </div>

          <h2 class="card-title mt-2">
            Активная роль
          </h2>

          <p
            class="text-base-content/60 min-h-5 text-sm"
          >
            <span v-if="isClientReady">
              {{ activeRoleName }}
            </span>
          </p>
        </div>
      </div>
    </section>
  </div>
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

<!-- ./frontend/app/pages/content/articles/new.vue -->
<script setup>
const store = useArticlesStore()

const saving = ref(false)
const errorMessage = ref('')

async function save(payload) {
  saving.value = true
  errorMessage.value = ''

  try {
    const article = await store.createArticle(payload)

    await navigateTo(
      `/content/articles/${article.id}`,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось создать статью'
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-5xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Новая статья
      </h1>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <ArticlesForm
      :saving="saving"
      @submit="save"
      @cancel="navigateTo('/content/articles')"
    />
  </div>
</template>

<!-- ./frontend/app/components/articles/Form.vue -->
<script setup>
const props = defineProps({
  initialValue: {
    type: Object,
    default: null,
  },
  saving: {
    type: Boolean,
    default: false,
  },
  submitLabel: {
    type: String,
    default: 'Сохранить статью',
  },
})

const emit = defineEmits([
  'submit',
  'cancel',
])

const { $api } = useNuxtApp()

const tags = ref([])
const loadingTags = ref(false)

const previewOpen = ref(false)
const errorMessage = ref('')

const form = reactive({
  title: '',
  content: '',
  tag_ids: [],
  pro_content: true,
})

function applyInitialValue(value) {
  if (!value) return

  form.title = value.title || ''
  form.content = value.content || ''
  form.tag_ids = (value.tags || []).map(
    (tag) => tag.id,
  )
  form.pro_content = Boolean(value.pro_content)
}

async function loadTags() {
  loadingTags.value = true

  try {
    tags.value = await $api('/api/v1/tags')
  } finally {
    loadingTags.value = false
  }
}

function submit() {
  errorMessage.value = ''

  if (!form.title.trim()) {
    errorMessage.value = 'Введите название статьи'
    return
  }

  if (!form.content.trim() || form.content === '<p></p>') {
    errorMessage.value = 'Введите текст статьи'
    return
  }

  emit('submit', {
    title: form.title.trim(),
    content: form.content,
    tag_ids: form.tag_ids,
    pro_content: form.pro_content,
  })
}

watch(
  () => props.initialValue,
  applyInitialValue,
  {
    immediate: true,
  },
)

onMounted(loadTags)
</script>

<template>
  <form
    class="space-y-6"
    @submit.prevent="submit"
  >
    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <section
      class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-6"
    >
      <div class="space-y-5">
        <label class="form-control block">
          <span class="label">
            <span class="label-text font-medium">
              Название статьи
            </span>
          </span>

          <input
            v-model="form.title"
            type="text"
            maxlength="300"
            required
            class="input input-bordered w-full"
            placeholder="Введите название"
          >
        </label>

        <div>
          <div class="mb-2 flex items-center justify-between">
            <span class="font-medium">
              Текст статьи
            </span>

            <button
              type="button"
              class="btn btn-ghost btn-sm"
              :disabled="!form.content"
              @click="previewOpen = true"
            >
              <Icon
                name="lucide:eye"
                class="size-4"
              />
              Предпросмотр
            </button>
          </div>

          <ContentRichTextEditor
            v-model="form.content"
            placeholder="Введите текст статьи..."
          />
        </div>

        <div>
          <p class="mb-3 font-medium">
            Теги
          </p>

          <ContentTagSelector
            v-model="form.tag_ids"
            :tags="tags"
            :loading="loadingTags"
          />
        </div>

        <label
          class="border-base-300 flex cursor-pointer items-start justify-between gap-4 rounded-2xl border p-4"
        >
          <span>
            <span class="block font-medium">
              Профессиональный контент
            </span>

            <span
              class="text-base-content/60 mt-1 block text-sm"
            >
              Доступен пациенту только после включения
              доступа Pro.
            </span>
          </span>

          <input
            v-model="form.pro_content"
            type="checkbox"
            class="toggle toggle-primary shrink-0"
          >
        </label>
      </div>
    </section>

    <div
      class="flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
    >
      <button
        type="button"
        class="btn"
        :disabled="saving"
        @click="emit('cancel')"
      >
        Отмена
      </button>

      <button
        type="submit"
        class="btn btn-primary"
        :disabled="saving"
      >
        <span
          v-if="saving"
          class="loading loading-spinner loading-sm"
        />

        {{ submitLabel }}
      </button>
    </div>
  </form>

  <UiResponsiveDialog
    v-model="previewOpen"
    title="Предпросмотр статьи"
    max-width-class="max-w-3xl"
  >
    <article>
      <h1 class="mb-6 text-2xl font-bold sm:text-3xl">
        {{ form.title || 'Без названия' }}
      </h1>

      <ContentRichTextRenderer
        :content="form.content"
      />
    </article>
  </UiResponsiveDialog>
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
<!-- ./frontend/app/pages/questionnaires/[id].vue -->
<script setup>
const route = useRoute()
const store = useQuestionnairesStore()

const questionnaire = ref(null)
const submissionId = ref(null)

const answers = reactive({})
const savingQuestions = reactive({})

const loading = ref(true)
const completing = ref(false)
const completed = ref(false)

const errorMessage = ref('')

const saveTimers = new Map()

const answeredCount = computed(() =>
  questionnaire.value?.questions.filter(
    (question) =>
      answers[question.id] !== undefined
      && answers[question.id] !== null
      && answers[question.id] !== '',
  ).length || 0
)

const progress = computed(() => {
  const total =
    questionnaire.value?.questions.length || 0

  return total
    ? Math.round(answeredCount.value / total * 100)
    : 0
})

async function initialize() {
  loading.value = true

  try {
    questionnaire.value =
      await store.fetchQuestionnaire(
        route.params.id,
      )

    const allProgress =
      await store.fetchMyProgress()

    const existing = allProgress.find(
      (item) =>
        item.questionnaire_id === route.params.id
        && item.status === 'in_progress',
    )

    if (existing) {
      submissionId.value = existing.submission_id

      const submission =
        await store.fetchSubmission(
          existing.submission_id,
        )

      for (const answer of submission.answers) {
        answers[answer.question_id] = answer.value
      }
    } else {
      const submission =
        await store.startQuestionnaire(
          route.params.id,
        )

      submissionId.value = submission.submission_id
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось открыть опросник'
  } finally {
    loading.value = false
  }
}

function scheduleAnswerSave(question) {
  const oldTimer = saveTimers.get(question.id)

  if (oldTimer) {
    window.clearTimeout(oldTimer)
  }

  const timer = window.setTimeout(async () => {
    savingQuestions[question.id] = true

    try {
      await store.saveAnswer(
        submissionId.value,
        question.id,
        answers[question.id],
      )
    } catch (error) {
      errorMessage.value =
        error?.data?.detail
        || 'Не удалось сохранить ответ'
    } finally {
      savingQuestions[question.id] = false
      saveTimers.delete(question.id)
    }
  }, 500)

  saveTimers.set(question.id, timer)
}

async function complete() {
  errorMessage.value = ''

  const missingRequired =
    questionnaire.value.questions.find(
      (question) =>
        question.is_required
        && (
          answers[question.id] === undefined
          || answers[question.id] === null
          || answers[question.id] === ''
        ),
    )

  if (missingRequired) {
    errorMessage.value =
      `Ответьте на обязательный вопрос: ${missingRequired.text}`

    document
      .getElementById(
        `question-${missingRequired.id}`,
      )
      ?.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      })

    return
  }

  completing.value = true

  try {
    const payload = questionnaire.value.questions
      .filter(
        (question) =>
          answers[question.id] !== undefined,
      )
      .map((question) => ({
        question_id: question.id,
        value: answers[question.id],
      }))

    await store.completeSubmission(
      submissionId.value,
      payload,
    )

    completed.value = true
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось завершить опросник'
  } finally {
    completing.value = false
  }
}

onMounted(initialize)

onBeforeUnmount(() => {
  for (const timer of saveTimers.values()) {
    window.clearTimeout(timer)
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="3"
  />

  <div
    v-else-if="errorMessage && !questionnaire"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="completed"
    class="bg-base-100 border-base-300 mx-auto max-w-2xl rounded-3xl border p-8 text-center"
  >
    <Icon
      name="lucide:circle-check-big"
      class="text-success mx-auto size-16"
    />

    <h1 class="mt-5 text-2xl font-bold">
      Опросник заполнен
    </h1>

    <NuxtLink
      to="/questionnaires"
      class="btn btn-primary mt-6"
    >
      Вернуться к опросникам
    </NuxtLink>
  </div>

  <div
    v-else-if="questionnaire"
    class="mx-auto max-w-3xl space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <h1 class="text-2xl font-bold sm:text-3xl">
        {{ questionnaire.title }}
      </h1>

      <p
        v-if="questionnaire.description"
        class="text-base-content/60 mt-2"
      >
        {{ questionnaire.description }}
      </p>

      <div class="mt-5">
        <div class="mb-2 flex justify-between text-sm">
          <span>
            Заполнено {{ answeredCount }} из
            {{ questionnaire.questions.length }}
          </span>

          <strong>{{ progress }}%</strong>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="progress"
          max="100"
        />
      </div>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <section class="space-y-4">
      <article
        v-for="(question, index) in questionnaire.questions"
        :id="`question-${question.id}`"
        :key="question.id"
        class="bg-base-100 border-base-300 rounded-2xl border p-4 sm:p-6"
      >
        <div class="mb-5 flex items-start gap-3">
          <div
            class="bg-primary text-primary-content flex size-8 shrink-0 items-center justify-center rounded-full text-sm font-bold"
          >
            {{ index + 1 }}
          </div>

          <div class="min-w-0 flex-1">
            <h2 class="font-semibold sm:text-lg">
              {{ question.text }}
            </h2>

            <span
              v-if="question.is_required"
              class="text-error text-xs"
            >
              Обязательный вопрос
            </span>
          </div>

          <span
            v-if="savingQuestions[question.id]"
            class="loading loading-spinner loading-xs"
          />
        </div>

        <QuestionnairesQuestionField
          v-model="answers[question.id]"
          :question="question"
          @update:model-value="
            scheduleAnswerSave(question)
          "
        />
      </article>
    </section>

    <div
      class="bg-base-100 border-base-300 sticky bottom-3 rounded-2xl border p-3 shadow-xl"
    >
      <button
        type="button"
        class="btn btn-primary w-full"
        :disabled="completing"
        @click="complete"
      >
        <span
          v-if="completing"
          class="loading loading-spinner loading-sm"
        />

        Завершить опросник
      </button>
    </div>
  </div>
</template>

<!-- ./frontend/app/pages/content/questionnaires/new.vue -->
<script setup>
</script>

<template>
  <div class="mx-auto max-w-5xl">
    <QuestionnairesEditor />
  </div>
</template>

<!-- ./frontend/app/components/questionnaires/Editor.vue -->
<script setup>
const route = useRoute()
const { $api } = useNuxtApp()
const store = useQuestionnairesStore()

const saving = ref(false)
const loading = ref(false)
const loadingTags = ref(false)

const tags = ref([])

const importOpen = ref(false)
const errorMessage = ref('')

const form = reactive(createEmptyForm())

function createEmptyQuestion() {
  return {
    client_id: crypto.randomUUID(),
    question_type: 'text',
    text: '',
    is_required: true,
    order_index: 0,

    scale_min: null,
    scale_max: null,
    scale_min_label: null,
    scale_max_label: null,

    options: [],
  }
}

function createEmptyForm() {
  return {
    title: '',
    description: '',
    pro_content: true,
    tag_ids: [],
    copied_from_id: null,
    questions: [
      createEmptyQuestion(),
    ],
  }
}

function applyForm(data) {
  form.title = data.title || ''
  form.description = data.description || ''
  form.pro_content = data.pro_content !== false
  form.tag_ids = data.tag_ids || []
  form.copied_from_id =
    data.copied_from_id || null

  form.questions = (data.questions || []).map(
    (question, questionIndex) => ({
      client_id:
        question.client_id
        || crypto.randomUUID(),

      question_type: question.question_type,
      text: question.text || '',
      is_required:
        question.is_required !== false,
      order_index: questionIndex,

      scale_min: question.scale_min ?? null,
      scale_max: question.scale_max ?? null,
      scale_min_label:
        question.scale_min_label ?? null,
      scale_max_label:
        question.scale_max_label ?? null,

      options: (question.options || []).map(
        (option, optionIndex) => ({
          client_id:
            option.client_id
            || crypto.randomUUID(),
          text: option.text || '',
          order_index: optionIndex,
        }),
      ),
    }),
  )

  if (!form.questions.length) {
    form.questions = [
      createEmptyQuestion(),
    ]
  }
}

async function loadTags() {
  loadingTags.value = true

  try {
    tags.value = await $api('/api/v1/tags')
  } finally {
    loadingTags.value = false
  }
}

async function loadCopySource() {
  const sourceId = route.query.copy

  if (typeof sourceId !== 'string') return

  loading.value = true

  try {
    const source =
      await store.fetchQuestionnaire(sourceId)

    applyForm({
      title: `${source.title} — копия`,
      description: source.description,
      pro_content: source.pro_content,
      tag_ids: source.tags.map((tag) => tag.id),
      copied_from_id: source.id,
      questions: source.questions,
    })
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить исходный опросник'
  } finally {
    loading.value = false
  }
}

function addQuestion() {
  const question = createEmptyQuestion()
  question.order_index = form.questions.length

  form.questions.push(question)
}

function removeQuestion(index) {
  if (form.questions.length === 1) {
    errorMessage.value =
      'Опросник должен содержать хотя бы один вопрос'
    return
  }

  form.questions.splice(index, 1)
  reindexQuestions()
}

function moveQuestion(index, direction) {
  const targetIndex = index + direction

  if (
    targetIndex < 0
    || targetIndex >= form.questions.length
  ) {
    return
  }

  const temporary = form.questions[index]
  form.questions[index] = form.questions[targetIndex]
  form.questions[targetIndex] = temporary

  reindexQuestions()
}

function reindexQuestions() {
  form.questions.forEach((question, index) => {
    question.order_index = index

    question.options.forEach((option, optionIndex) => {
      option.order_index = optionIndex
    })
  })
}

function validateForm() {
  if (!form.title.trim()) {
    return 'Введите название опросника'
  }

  if (!form.questions.length) {
    return 'Добавьте хотя бы один вопрос'
  }

  for (
    let index = 0;
    index < form.questions.length;
    index += 1
  ) {
    const question = form.questions[index]

    if (!question.text.trim()) {
      return `Введите текст вопроса №${index + 1}`
    }

    if (
      [
        'single_choice',
        'multiple_choice',
      ].includes(question.question_type)
    ) {
      if (question.options.length < 2) {
        return (
          `У вопроса №${index + 1} должно быть `
          + 'не менее двух вариантов'
        )
      }

      if (
        question.options.some(
          (option) => !option.text.trim(),
        )
      ) {
        return (
          `Заполните варианты ответа `
          + `в вопросе №${index + 1}`
        )
      }
    }

    if (
      question.question_type === 'scale'
      && question.scale_max <= question.scale_min
    ) {
      return (
        `В вопросе №${index + 1} максимум `
        + 'должен быть больше минимума'
      )
    }
  }

  return null
}

function buildPayload() {
  reindexQuestions()

  return {
    title: form.title.trim(),
    description:
      form.description.trim() || null,
    pro_content: form.pro_content,
    tag_ids: form.tag_ids,
    copied_from_id: form.copied_from_id,

    questions: form.questions.map(
      (question, questionIndex) => ({
        question_type: question.question_type,
        text: question.text.trim(),
        is_required: question.is_required,
        order_index: questionIndex,

        scale_min:
          question.question_type === 'scale'
            ? question.scale_min
            : null,

        scale_max:
          question.question_type === 'scale'
            ? question.scale_max
            : null,

        scale_min_label:
          question.question_type === 'scale'
            ? question.scale_min_label || null
            : null,

        scale_max_label:
          question.question_type === 'scale'
            ? question.scale_max_label || null
            : null,

        options: [
          'single_choice',
          'multiple_choice',
        ].includes(question.question_type)
          ? question.options.map(
              (option, optionIndex) => ({
                text: option.text.trim(),
                order_index: optionIndex,
              }),
            )
          : [],
      }),
    ),
  }
}

async function save() {
  errorMessage.value = validateForm() || ''

  if (errorMessage.value) return

  saving.value = true

  try {
    const questionnaire =
      await store.createQuestionnaire(
        buildPayload(),
      )

    await navigateTo('/content/questionnaires')
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось создать опросник'
  } finally {
    saving.value = false
  }
}

function handleImport(data) {
  applyForm(data)
  errorMessage.value = ''
}

function downloadJson() {
  const payload = buildPayload()

  const blob = new Blob(
    [
      JSON.stringify(payload, null, 2),
    ],
    {
      type: 'application/json',
    },
  )

  const url = URL.createObjectURL(blob)
  const anchor = document.createElement('a')

  anchor.href = url
  anchor.download = 'questionnaire.json'
  anchor.click()

  URL.revokeObjectURL(url)
}

onMounted(async () => {
  await Promise.all([
    loadTags(),
    loadCopySource(),
  ])
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Новый опросник
        </h1>

        <p class="text-base-content/60 mt-1">
          После сохранения опросник нельзя редактировать.
        </p>
      </div>

      <div class="flex flex-col gap-2 sm:flex-row">
        <button
          type="button"
          class="btn btn-outline"
          @click="downloadJson"
        >
          <Icon
            name="lucide:download"
            class="size-4"
          />
          Скачать JSON
        </button>

        <button
          type="button"
          class="btn btn-outline"
          @click="importOpen = true"
        >
          <Icon
            name="lucide:upload"
            class="size-4"
          />
          Загрузить JSON
        </button>
      </div>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      <Icon
        name="lucide:circle-alert"
        class="size-5"
      />
      <span>{{ errorMessage }}</span>
    </div>

    <div
      v-if="loading"
      class="flex justify-center py-16"
    >
      <span
        class="loading loading-spinner loading-lg text-primary"
      />
    </div>

    <template v-else>
      <section
        class="bg-base-100 border-base-300 space-y-5 rounded-2xl border p-4 sm:p-6"
      >
        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Название
          </span>

          <input
            v-model="form.title"
            type="text"
            maxlength="300"
            class="input input-bordered w-full"
          >
        </label>

        <label class="form-control block">
          <span class="label-text mb-2 font-medium">
            Описание
          </span>

          <textarea
            v-model="form.description"
            class="textarea textarea-bordered min-h-28 w-full"
          />
        </label>

        <div>
          <p class="mb-3 font-medium">
            Теги
          </p>

          <ContentTagSelector
            v-model="form.tag_ids"
            :tags="tags"
            :loading="loadingTags"
          />
        </div>

        <label
          class="border-base-300 flex cursor-pointer items-center justify-between gap-4 rounded-2xl border p-4"
        >
          <span>
            <span class="block font-medium">
              Профессиональный контент
            </span>

            <span
              class="text-base-content/60 text-sm"
            >
              Требует доступа Pro.
            </span>
          </span>

          <input
            v-model="form.pro_content"
            type="checkbox"
            class="toggle toggle-primary"
          >
        </label>
      </section>

      <section class="space-y-4">
        <QuestionnairesQuestionItem
          v-for="(question, index) in form.questions"
          :key="question.client_id"
          v-model="form.questions[index]"
          :index="index"
          :total="form.questions.length"
          @remove="removeQuestion(index)"
          @move-up="moveQuestion(index, -1)"
          @move-down="moveQuestion(index, 1)"
        />

        <button
          type="button"
          class="btn btn-outline w-full"
          @click="addQuestion"
        >
          <Icon
            name="lucide:plus"
            class="size-5"
          />
          Добавить вопрос
        </button>
      </section>

      <div
        class="flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
      >
        <NuxtLink
          to="/content/questionnaires"
          class="btn"
        >
          Отмена
        </NuxtLink>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="saving"
          @click="save"
        >
          <span
            v-if="saving"
            class="loading loading-spinner loading-sm"
          />

          Создать опросник
        </button>
      </div>
    </template>
  </div>

  <QuestionnairesJsonImporter
    v-model="importOpen"
    @import="handleImport"
  />
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

    async function fetchArticle(
      articleId,
      {
        programId = null,
        programStageId = null,
      } = {},
    ) {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        currentArticle.value = await $api(
          `/api/v1/articles/${articleId}`,
          {
            query: {
              program_id: programId || undefined,
              program_stage_id:
                programStageId || undefined,
            },
          },
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

// ./frontend/app/stores/tag-access.js
export const useTagAccessStore = defineStore(
  'tag-access',
  () => {
    const tags = ref([])

    const doctorEffectiveTags = ref([])
    const doctorOverrides = ref([])

    const patientEffectiveTags = ref([])
    const patientOverrides = ref([])

    const loadingDoctor = ref(false)
    const loadingPatient = ref(false)
    const saving = ref(false)

    async function fetchTags() {
      const { $api } = useNuxtApp()

      tags.value = await $api(
        '/api/v1/tags',
      )

      return tags.value
    }

    async function fetchDoctorState() {
      const { $api } = useNuxtApp()

      loadingDoctor.value = true

      try {
        const [
          catalog,
          effective,
          overrides,
        ] = await Promise.all([
          $api('/api/v1/tags'),
          $api('/api/v1/tags/me/effective'),
          $api(
            '/api/v1/tags/doctors/me/overrides',
          ),
        ])

        tags.value = catalog
        doctorEffectiveTags.value =
          effective.tags || []
        doctorOverrides.value = overrides

        return {
          effective: effective.tags || [],
          overrides,
        }
      } finally {
        loadingDoctor.value = false
      }
    }

    async function setDoctorOverride(
      tagId,
      action,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          '/api/v1/tags/doctors/me/overrides',
          {
            method: 'PUT',
            body: {
              tag_id: tagId,
              action,
            },
          },
        )

        await fetchDoctorState()
      } finally {
        saving.value = false
      }
    }

    async function resetDoctorOverride(tagId) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/doctors/me/overrides/${tagId}`,
          {
            method: 'DELETE',
          },
        )

        await fetchDoctorState()
      } finally {
        saving.value = false
      }
    }

    async function fetchPatientState(patientId) {
      const { $api } = useNuxtApp()

      loadingPatient.value = true

      try {
        const [
          catalog,
          effective,
          overrides,
        ] = await Promise.all([
          $api('/api/v1/tags'),
          $api(
            `/api/v1/tags/patients/${patientId}/effective`,
          ),
          $api(
            `/api/v1/tags/patients/${patientId}/overrides`,
          ),
        ])

        tags.value = catalog
        patientEffectiveTags.value =
          effective.tags || []
        patientOverrides.value = overrides

        return {
          effective: effective.tags || [],
          overrides,
        }
      } finally {
        loadingPatient.value = false
      }
    }

    async function setPatientOverride(
      patientId,
      tagId,
      action,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/patients/${patientId}/overrides`,
          {
            method: 'PUT',
            body: {
              tag_id: tagId,
              action,
            },
          },
        )

        await fetchPatientState(patientId)
      } finally {
        saving.value = false
      }
    }

    async function resetPatientOverride(
      patientId,
      tagId,
    ) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        await $api(
          `/api/v1/tags/patients/${patientId}/overrides/${tagId}`,
          {
            method: 'DELETE',
          },
        )

        await fetchPatientState(patientId)
      } finally {
        saving.value = false
      }
    }

    return {
      tags,

      doctorEffectiveTags,
      doctorOverrides,

      patientEffectiveTags,
      patientOverrides,

      loadingDoctor,
      loadingPatient,
      saving,

      fetchTags,
      fetchDoctorState,
      setDoctorOverride,
      resetDoctorOverride,

      fetchPatientState,
      setPatientOverride,
      resetPatientOverride,
    }
  },
)

// ./frontend/app/stores/user.js
export const useUserStore = defineStore(
  'user',
  () => {
    const user = ref(null)
    const loading = ref(false)
    const saving = ref(false)

    const fullName = computed(() => {
      if (!user.value) return ''

      return (
        [
          user.value.last_name,
          user.value.first_name,
          user.value.middle_name,
        ]
          .filter(Boolean)
          .join(' ')
        || user.value.email
        || ''
      )
    })

    const initials = computed(() => {
      if (!user.value) return '?'

      const first = (
        user.value.first_name
        || user.value.email
        || '?'
      ).charAt(0)

      const last = (
        user.value.last_name || ''
      ).charAt(0)

      return `${first}${last}`.toUpperCase()
    })

    const isEmailVerified = computed(() =>
      Boolean(user.value?.is_email_verified),
    )

    async function fetchMe() {
      const { $api } = useNuxtApp()

      loading.value = true

      try {
        user.value = await $api(
          '/api/v1/users/me',
        )

        return user.value
      } finally {
        loading.value = false
      }
    }

    async function updateProfile(payload) {
      const { $api } = useNuxtApp()

      saving.value = true

      try {
        user.value = await $api(
          '/api/v1/users/me',
          {
            method: 'PATCH',
            body: payload,
          },
        )

        return user.value
      } finally {
        saving.value = false
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
      saving,

      fullName,
      initials,
      isEmailVerified,

      fetchMe,
      updateProfile,
      resendVerificationEmail,
      clear,
    }
  },
)

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
<!-- ./frontend/app/components/ui/Pagination.vue -->
<script setup>
const model = defineModel({
  type: Number,
  default: 1,
})

const props = defineProps({
  totalItems: {
    type: Number,
    default: 0,
  },
  pageSize: {
    type: Number,
    default: 10,
  },
})

const totalPages = computed(() =>
  Math.max(
    1,
    Math.ceil(props.totalItems / props.pageSize),
  ),
)

watch(totalPages, (value) => {
  if (model.value > value) {
    model.value = value
  }
})
</script>

<template>
  <nav
    v-if="totalPages > 1"
    class="flex items-center justify-center gap-2"
    aria-label="Пагинация"
  >
    <button
      type="button"
      class="btn btn-square btn-sm"
      :disabled="model <= 1"
      aria-label="Предыдущая страница"
      @click="model -= 1"
    >
      <Icon
        name="lucide:chevron-left"
        class="size-4"
      />
    </button>

    <span class="px-3 text-sm">
      {{ model }} из {{ totalPages }}
    </span>

    <button
      type="button"
      class="btn btn-square btn-sm"
      :disabled="model >= totalPages"
      aria-label="Следующая страница"
      @click="model += 1"
    >
      <Icon
        name="lucide:chevron-right"
        class="size-4"
      />
    </button>
  </nav>
</template>
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
<!-- ./frontend/app/components/patient/Home.vue -->
<script setup>
const store = usePatientHomeStore()

onMounted(() => {
  store.load()
})

onBeforeUnmount(() => {
  store.clear()
})
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-7">
    <UiContentSkeleton
      v-if="store.loading"
      variant="card"
      :count="2"
    />

    <section
      v-else-if="store.errorMessage"
      class="border-base-300 bg-base-100 rounded-3xl border p-6"
    >
      <p role="alert">
        {{ store.errorMessage }}
      </p>

      <button
        type="button"
        class="btn btn-primary mt-4"
        @click="store.load"
      >
        Попробовать ещё раз
      </button>
    </section>

    <template v-else>
      <PatientNextStep
        v-if="store.primaryProgram"
        :key="store.primaryProgram.id"
        :program="store.primaryProgram"
      />

      <section
        v-else
        class="border-base-300 bg-base-100 rounded-3xl border p-5 sm:p-8"
      >
        <h1 class="text-2xl font-bold">
          {{
            store.hasCompletedStart
              ? 'Первый маршрут пройден'
              : 'Здравствуйте'
          }}
        </h1>

        <p class="text-base-content/70 mt-3">
          {{
            store.hasCompletedStart
              ? 'Можно вернуться к материалам или обсудить дальнейшую поддержку со специалистом.'
              : 'Здесь можно познакомиться с материалами клиники и доступными программами.'
          }}
        </p>

        <NuxtLink
          to="/programs"
          class="btn btn-primary mt-5"
        >
          {{
            store.hasCompletedStart
              ? 'Посмотреть дальнейшие варианты'
              : 'Посмотреть программы'
          }}
        </NuxtLink>
      </section>

      <PatientJourney
        v-if="store.primaryProgram?.is_start"
        :program="store.primaryProgram"
      />

      <AssignmentsPatientList />

      <details
        v-if="store.otherActivePrograms.length"
        class="border-base-300 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer font-medium">
          Другие начатые программы
        </summary>

        <div class="mt-4 space-y-3">
          <NuxtLink
            v-for="program in store.otherActivePrograms"
            :key="program.id"
            :to="`/programs/${program.id}`"
            class="border-base-300 block rounded-xl border p-4"
          >
            <span class="font-medium">
              {{ program.title }}
            </span>

            <span class="text-base-content/60 mt-1 block text-sm">
              Продолжить программу
            </span>
          </NuxtLink>
        </div>
      </details>

      <PatientSupport />

      <details
        v-if="store.completedPrograms.length"
        class="border-base-300 rounded-2xl border p-4"
      >
        <summary class="cursor-pointer font-medium">
          Пройденные материалы программ
        </summary>

        <div class="mt-4 space-y-3">
          <NuxtLink
            v-for="program in store.completedPrograms"
            :key="program.id"
            :to="`/programs/${program.id}`"
            class="link link-primary block"
          >
            {{ program.title }}
          </NuxtLink>
        </div>
      </details>

      <nav
        class="text-base-content/70 flex flex-wrap gap-x-5 gap-y-3 text-sm"
        aria-label="Материалы и программы"
      >
        <NuxtLink
          to="/content/articles"
          class="link"
        >
          Все статьи
        </NuxtLink>

        <NuxtLink
          to="/questionnaires"
          class="link"
        >
          Опросники
        </NuxtLink>

        <NuxtLink
          to="/programs"
          class="link"
        >
          Все программы
        </NuxtLink>
      </nav>
    </template>
  </div>
</template>
<!-- ./frontend/app/components/patient/Journey.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const items = computed(() =>
  (props.program.stages || [])
    .flatMap(stage =>
      (stage.items || []).map(item => ({
        ...item,
        stageId: stage.id,
      })),
    )
    .filter(
      item =>
        item.item_type !== 'consultation'
        && !item.is_hidden,
    ),
)

const previewItems = computed(() =>
  items.value.slice(0, 3),
)
</script>

<template>
  <section
    v-if="previewItems.length"
    class="space-y-3"
  >
    <h2 class="text-lg font-semibold">
      Что входит в маршрут
    </h2>

    <ol class="space-y-3">
      <li
        v-for="(item, index) in previewItems"
        :key="item.id"
        class="flex items-start gap-3"
      >
        <span
          class="flex size-7 shrink-0 items-center justify-center rounded-full text-xs font-semibold"
          :class="
            item.is_completed
              ? 'bg-success/15 text-success'
              : 'bg-base-200 text-base-content/70'
          "
        >
          <Icon
            v-if="item.is_completed"
            name="lucide:check"
            class="size-4"
          />

          <template v-else>
            {{ index + 1 }}
          </template>
        </span>

        <span class="pt-0.5 text-sm">
          {{ item.title }}
        </span>
      </li>
    </ol>

    <NuxtLink
      v-if="items.length > previewItems.length"
      :to="`/programs/${program.id}`"
      class="link link-primary text-sm"
    >
      Посмотреть весь маршрут
    </NuxtLink>
  </section>
</template>
<!-- ./frontend/app/components/patient/NextStep.vue -->
<script setup>
const props = defineProps({
  program: {
    type: Object,
    required: true,
  },
})

const store = usePatientHomeStore()

const opening = ref(false)
const errorMessage = ref('')

const nextStep = computed(() => {
  const stages = props.program.stages || []

  for (const stage of stages) {
    if (
      props.program.enrollment
      && stage.status === 'upcoming'
    ) {
      continue
    }

    const item = (stage.items || []).find(
      current =>
        current.item_type !== 'consultation'
        && !current.is_hidden
        && current.can_access
        && !current.is_completed,
    )

    if (item) {
      return { stage, item }
    }
  }

  return null
})

const progressValue = computed(() => {
  const value = Number(props.program.progress_percent)

  return Number.isFinite(value)
    ? Math.min(Math.max(value, 0), 100)
    : 0
})

const actionText = computed(() => {
  if (!props.program.enrollment) {
    return props.program.is_start
      ? 'Начать с первого шага'
      : 'Открыть мой план'
  }

  return nextStep.value
    ? 'Продолжить'
    : 'Посмотреть план'
})

async function openProgram() {
  if (opening.value) return

  opening.value = true
  errorMessage.value = ''

  try {
    if (!props.program.enrollment) {
      await store.startProgram(props.program.id)
    }

    await navigateTo({
      path: `/programs/${props.program.id}`,
      query: nextStep.value
        ? { stage: nextStep.value.stage.id }
        : {},
    })
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось открыть программу'
  } finally {
    opening.value = false
  }
}
</script>

<template>
  <section
    class="border-primary/20 bg-base-100 rounded-3xl border p-5 shadow-sm sm:p-8"
  >
    <p class="text-primary text-sm font-medium">
      {{
        program.enrollment
          ? 'Ваш следующий шаг'
          : program.is_start
            ? 'Начните с небольшого шага'
            : 'Ваша программа доступна'
      }}
    </p>

    <h1 class="mt-3 text-2xl font-bold sm:text-3xl">
      {{ program.title }}
    </h1>

    <p
      v-if="program.description"
      class="text-base-content/70 mt-3 max-w-2xl"
    >
      {{ program.description }}
    </p>

    <div
      v-if="nextStep"
      class="bg-base-200 mt-6 rounded-2xl p-4"
    >
      <p class="text-base-content/60 text-xs">
        {{
          nextStep.item.item_type === 'article'
            ? 'Материал для чтения'
            : 'Вопросы для размышления'
        }}
      </p>

      <h2 class="mt-1 font-semibold">
        {{ nextStep.item.title }}
      </h2>
    </div>

    <div
      v-if="program.enrollment"
      class="mt-5"
    >
      <div class="mb-2 flex justify-between gap-3 text-xs">
        <span>Прогресс по материалам</span>
        <span>{{ progressValue }}%</span>
      </div>

      <progress
        class="progress progress-primary w-full"
        :value="progressValue"
        max="100"
      />
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-5"
      role="alert"
    >
      {{ errorMessage }}
    </div>

    <button
      type="button"
      class="btn btn-primary mt-6 w-full sm:w-auto"
      :disabled="opening"
      @click="openProgram"
    >
      <span
        v-if="opening"
        class="loading loading-spinner loading-sm"
      />

      {{ actionText }}

      <Icon
        v-if="!opening"
        name="lucide:arrow-right"
        class="size-4"
      />
    </button>

    <p
      v-if="program.is_start"
      class="text-base-content/60 mt-3 text-sm"
    >
      Бесплатно. Можно остановиться и продолжить позже.
    </p>
  </section>
</template>
<!-- ./frontend/app/components/patient/Support.vue -->
<script setup>
const store = usePatientHomeStore()

const selectedProgram = ref(null)
const dialogOpen = ref(false)
const requesting = ref(false)
const errorMessage = ref('')

function openDialog(program) {
  selectedProgram.value = program
  errorMessage.value = ''
  dialogOpen.value = true
}

async function sendRequest() {
  if (!selectedProgram.value || requesting.value) return

  requesting.value = true
  errorMessage.value = ''

  try {
    await store.requestPurchase(
      selectedProgram.value.id,
    )

    dialogOpen.value = false
    selectedProgram.value = null
  } catch (error) {
    errorMessage.value =
      typeof error?.data?.detail === 'string'
        ? error.data.detail
        : 'Не удалось отправить запрос. Попробуйте ещё раз.'
  } finally {
    requesting.value = false
  }
}
</script>

<template>
  <section
    v-if="
      store.supportPrograms.length
      || store.pendingRequests.length
    "
    class="border-base-300 bg-base-100 rounded-3xl border p-5 sm:p-6"
  >
    <h2 class="text-xl font-semibold">
      Поддержка специалиста
    </h2>

    <p class="text-base-content/70 mt-2 text-sm">
      Можно обсудить программу сопровождения с ассистентом
      клиники. Он объяснит состав, стоимость и порядок записи.
    </p>

    <div
      v-if="store.pendingRequests.length"
      class="mt-5 space-y-3"
      aria-live="polite"
    >
      <div
        v-for="program in store.pendingRequests"
        :key="program.id"
        class="bg-success/10 rounded-2xl p-4"
      >
        <p class="font-medium">
          Запрос отправлен
        </p>

        <p class="mt-1 text-sm">
          {{ program.title }}
        </p>

        <p class="text-base-content/70 mt-2 text-sm">
          Ассистент обычно связывается в течение 1–2 дней
          по телефону, указанному в клинике.
        </p>
      </div>
    </div>

    <div class="mt-5 space-y-4">
      <article
        v-for="program in store.supportPrograms"
        :key="program.id"
        class="border-base-300 rounded-2xl border p-4"
      >
        <p class="text-base-content/60 text-xs">
          Платная программа сопровождения
        </p>

        <h3 class="mt-1 font-semibold">
          {{ program.title }}
        </h3>

        <p
          v-if="program.description"
          class="text-base-content/70 mt-2 text-sm"
        >
          {{ program.description }}
        </p>

        <div class="mt-4 flex flex-wrap gap-2">
          <NuxtLink
            :to="`/programs/${program.id}`"
            class="btn btn-outline btn-sm"
          >
            Состав и стоимость
          </NuxtLink>

          <button
            type="button"
            class="btn btn-ghost btn-sm"
            @click="openDialog(program)"
          >
            Обсудить с ассистентом
          </button>
        </div>
      </article>
    </div>

    <p class="text-base-content/60 mt-4 text-xs">
      Запрос не обязывает покупать программу.
      Это не канал срочной медицинской помощи.
    </p>
  </section>

  <UiResponsiveDialog
    v-model="dialogOpen"
    title="Обсудить программу"
    max-width-class="max-w-md"
  >
    <div class="space-y-4">
      <p class="font-medium">
        {{ selectedProgram?.title }}
      </p>

      <p class="text-base-content/70 text-sm">
        Отправим ассистенту запрос на обсуждение этой программы.
        Он обычно связывается в течение 1–2 дней по телефону,
        указанному в клинике.
      </p>

      <p class="text-base-content/70 text-sm">
        Состав и стоимость согласуются до покупки.
        Оплата в приложении не производится.
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
        role="alert"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
        <button
          type="button"
          class="btn btn-ghost"
          :disabled="requesting"
          @click="dialogOpen = false"
        >
          Пока не нужно
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="requesting"
          @click="sendRequest"
        >
          <span
            v-if="requesting"
            class="loading loading-spinner loading-sm"
          />

          Прошу связаться со мной
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>

В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api. как ты видел выше


---

Надо сделать несколько мелких вещей:
1. Добавить статьям и опросникам поле для того, чтобы скрывать их из общего списка статей и опросников, чтобы их было видно только внутри программ, потому что не все статьи и опросники подходят для общего отображения. Придется делать миграции, но что делать

2. В конфигураторе программ сейчас неудобно организована библиотека: статьи и опросники без пагинации, никак не организованы... Сделай окно бибилиотеки шире. Пусть будет возможность фильтровать контет по тегам . Допустим, при пагинации будет 5 статей/опросников, под ними пусть располагаются теги. Я нажимаю на теги и нерелевантные элементы исчезают, а тег с бледного цвета становится цветным, то есть, активным. 

3. Также, мне не нравится, что у пациента на главной странице показывается только одна стартовая программа. Надо показывать все, чтобы можно было скроллить. оставь значение Приоритета на главной, пусть если у какой-то программы приоритет выше, она была в саом верху, но если нет, то ... не знаю... пусть как-то располагаются. пусть платные программы также располагаются в списке, у них стоимость будет по запросу, но рамка платных программ пусть будет золотой. то есть, они должны отличаться от бесплатных визуально. Главное, чтобы плантые программы располагались не в самом верху, чтоыб первичный пациент не попадал сразу на них. 

4. Сделай карточки программ компактнее и удобнее, особенно для мобильных телефонов. Сейчас одна стартовая программа занимает почти всю страницу на мобильном устройстве. Например, шаги убери под раскрывающийся список.

5. На странице чтения статьи справа в нижмнем углу сделай кнопку назад типо такой: 
<div class="fab">
  <button class="btn btn-lg btn-circle btn-primary">F</button>
</div>
только цвет не сильно яркий и написано Х, чтобы закрыть статью и обратно в список статей/опросников, когда я в самом верху или в самом низу, а пока скроллю или нахожусь не в самом верху или в самом низу, кнопка вверх - то есть, в начало статьи. Эту кнопку сделай в виде отдельного элемента

ЕСЛИ ТЕБЕ НУЖНЫ ЕЩЕ КАКИЕ-ТО ФАЙЛЫ, попроси прислать! ЕСЛИ ЕСТЬ ВОПРОСЫ, задавай



























---------------------
«Только внутри программ» — это скрытие из каталога или строгое ограничение доступа? - скрытие из каталога, ну и чтобы бекенд их просто не отдавал, чтобы не нагружать сервис. блокировать api к такой статье не надо. короче, как ты предложил
Нужно ли менять новый флаг у уже созданных опросников? как ты преложил
Куда закрывать статью, открытую из программы? - да, как ты предложил




























------------------------\

Описание переписки с нейронкой для планирования сервиса
Теперь сценарий достаточно понятен. Для MVP я рекомендую не «витрину программ», а короткий маршрут с одним очевидным следующим шагом. Программы и обращение к специалисту должны быть доступны сразу, но не конкурировать на первом экране с шестью статьями, настройками и согласиями.

Ниже — предлагаемая траектория, важные замечания по присланному коду и первое изменение, которое уже можно внедрить: вход сразу после регистрации.

1. Какую траекторию делаем
Приглашение терапевта → короткий полезный материал → небольшой бесплатный маршрут → объяснение роли специалиста → запрос на связь.

При этом пациенту не нужно сначала «заслужить» консультацию прочтением материалов. Ссылка «Обсудить со специалистом» доступна с самого начала — просто это второстепенное действие, а не главное.

Что говорит терапевт
В вашем варианте хороша идея комплексного наблюдения. Но слова «ваша проблема требует» и «конкретные шаги для решения проблемы» звучат одновременно директивно и немного неопределённо.

Я бы предложил такую основу:

«Иван Иванович, мы продолжим разбираться с причинами ваших жалоб. При этом сон, питание и употребление алкоголя тоже могут влиять на самочувствие. Можно предложить вам короткий материал нашей клиники о том, с чего начать изменения без попытки поменять всё сразу?

Здесь можно бесплатно познакомиться с рекомендациями. А если захотите обсудить ситуацию лично, ассистент поможет записаться к специалисту. Открытие материалов ни к чему вас не обязывает».

Если необходимость помощи по поводу алкоголя уже обсуждалась:

«В вашей ситуации я также рекомендую консультацию психиатра-нарколога. Он поможет оценить, как алкоголь влияет на состояние, и подобрать безопасный план изменений. Начать можно с одной консультации — покупать большую программу заранее не обязательно».

Использовать нужно реальную специальность и квалификацию врача. «Специалист по зависимостям» допустим как понятное пояснение, но не как способ скрыть, к кому записывается пациент.

Снижаем стигму объяснением, а не неожиданной подменой «образа жизни» психиатрической помощью.

Отметку алгоритма необязательно выносить в начало разговора. Если она обсуждается, важно объяснять: это сигнал обратить внимание, а не установленный диагноз.

Важная граница для выбранного сценария
Бесплатная программа про изменения образа жизни подходит как образовательный маршрут, но не как самостоятельная программа отмены алкоголя при зависимости.

В материалах об изменении употребления нужен короткий, заметный блок:

«При регулярном употреблении алкоголя резкая отмена может быть опасной. Если при сокращении появляются дрожь, потливость, сердцебиение или выраженная тревога, обратитесь за медицинской помощью, не дожидаясь звонка ассистента. При судорогах, спутанности сознания или галлюцинациях — звоните 112 или 103».

Полный кризисный модуль можно отложить. Эту базовую границу безопасности — нет. Аналогично, цепочка «соблюдал гигиену сна → не помогло → нужны лекарства» слишком упрощена: следующий шаг — оценка причин нарушения сна врачом, а не автоматический вывод о медикаментах.

2. Главная пациента: конкретная структура
Первый экран
Не показываем сверху роль, номер карты, технические теги и настройки безопасности.

Пример текста:

Изменения начинаются с небольшого шага

Необязательно менять всё сразу. Начните с короткого материала о том, как выбрать посильный первый шаг.

Не всё сразу: с чего начать изменения

Бесплатный материал · около 3 минут

[Читать первый материал]

Обсудить помощь специалиста

Время чтения должно соответствовать реальному тексту. Если сна среди жалоб нет, не стоит начинать с утверждения «давайте восстановим ваш сон» — это будет ложная персонализация.

Надпись «Рекомендовано вашим врачом» используем только для материала, который врач действительно назначил. Совпадение тегов ещё не означает личную рекомендацию.

Ниже — один бесплатный маршрут
Ваш первый маршрут

Три небольших шага, чтобы разобраться в ситуации и понять, какая поддержка вам подходит.

С чего начать изменения.
Что сейчас важно именно вам.
Как может помочь специалист.
Бесплатно. Проходите в удобном темпе.

На главной это краткий обзор, а не ещё одна большая панель с несколькими равнозначными кнопками.

Предлагаю сделать первый материал первым элементом бесплатной программы. Пациент нажимает «Читать первый материал», приложение начинает бесплатный маршрут и открывает статью. Не заставляем его сначала изучать страницу программы и отдельно нажимать «Начать программу».

С технической стороны переход должен учитывать успешный ответ на запуск программы; если запуск не удался, нельзя молча отображать её как начатую.

Далее — понятное предложение поддержки
Необязательно разбираться в этом одному

Специалист поможет оценить влияние алкоголя на самочувствие, обсудить сон и подобрать безопасный план изменений.

Можно начать с одной консультации или обсудить программу сопровождения.

[Обсудить варианты помощи]

Ассистент обычно связывается в течение 1–2 дней. Обращение не обязывает покупать программу. Это не канал срочной помощи.

Уточните перед публикацией, календарные это дни или рабочие.

При повторном входе
Вот что я имел в виду под «возвращением пациента»:

Состояние	Главное действие
Ещё ничего не начал	Читать первый материал
Начал маршрут	Продолжить текущий шаг
Завершил бесплатный маршрут	Выбрать дальнейший шаг: материалы или помощь специалиста
Отправил запрос	Увидеть подтверждение запроса и продолжить бесплатные материалы
Получил доступ к сопровождению	Продолжить свою программу
На первом месте всегда один актуальный шаг, а не весь каталог.

Показывать состояние «Запрос отправлен» уже позволяет ваш purchase_requested. Это не большой новый модуль, а полезное применение имеющихся данных.

3. Содержание бесплатного маршрута
Я бы оставил название Life Balance как бренд, а пациенту показывал понятный подзаголовок:

Life Balance — первые шаги

Шаг	Содержание	Задача
С чего начать	«Не всё сразу: как начинать изменения небольшими шагами»	Уменьшить ощущение чрезмерной сложности
Что важно для меня	Короткая версия «Моя мотивация и цели»	Связать маршрут с собственной целью пациента
Какая поддержка подходит	Новая статья «Как проходит первая консультация специалиста по зависимостям»	Снять конкретные вопросы и опасения
«Моя ситуация по модели ABC» и «Мой план профилактики рецидива» я бы не ставил на первый экран. Они полезны, но требуют больше вовлечённости, а слово «рецидив» предполагает контекст, которого у впервые обратившегося пациента может ещё не быть.

В статье о консультации нужно ответить на практические вопросы:

о чём врач будет спрашивать;
нужно ли заранее готовиться;
обязательно ли назначают лекарства;
как согласовывается план помощи;
что входит в консультацию, а что оплачивается отдельно;
кто имеет доступ к информации.
Последний пункт — по реальным правилам клиники, без обещаний абсолютной анонимности.

Бесплатный маршрут должен приносить самостоятельную пользу. Не следует специально делать его недостаточным, чтобы пациент пришёл к выводу, что без покупки он не справится.

4. Программы и цена
Я бы не предлагал пациенту на первом экране выбирать между FREE, Lite и Personal. Это выбор между внутренними названиями продукта, смысл которых пока неясен.

Лучше:

Самостоятельный старт — бесплатные материалы.
Первая консультация — разобраться в ситуации с врачом.
Индивидуальное сопровождение — согласованный план консультаций и работы между ними.
Lite и Personal можно оставить внутри страницы сопровождения или для обсуждения с ассистентом.

Убрать цену с первого экрана — разумно. Полностью скрывать её ради того, чтобы пациент сначала оставил заявку, я бы не рекомендовал. Если цена фиксированная, дайте возможность посмотреть её до обращения. Если состав индивидуальный, честно напишите, от чего зависит стоимость и что она согласуется до оплаты.

Количество консультаций лучше объяснять содержанием и задачами сопровождения, а не делать большую упаковку вариантом «по умолчанию».

давай сделаем бесплатную программу по этому сценарию. она должна включать в себя 3 шага. Каждый шаг должен содержать по 2-3-4 статьи и 1 опросник, либо опросник в начале и опросник в конце шага. 

Опросники делай в виде json:
образец:
{
  "title": "AUDIT — тест для выявления расстройств, связанных с употреблением алкоголя",
  "description": "Alcohol Use Disorders Identification Test (AUDIT), разработанный Всемирной организацией здравоохранения. Опросник состоит из 10 вопросов об употреблении алкоголя.",
  "pro_content": false,
  "tag_ids": [],
  "questions": [
    {
      "question_type": "single_choice",
      "text": "Как часто вы употребляете алкогольные напитки?",
      "is_required": true,
      "order_index": 0,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Раз в месяц или реже",
          "order_index": 1
        },
        {
          "text": "2–4 раза в месяц",
          "order_index": 2
        },
        {
          "text": "2–3 раза в неделю",
          "order_index": 3
        },
        {
          "text": "4 раза в неделю или чаще",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Сколько стандартных порций алкоголя вы обычно выпиваете в день, когда употребляете алкоголь?",
      "is_required": true,
      "order_index": 1,
      "options": [
        {
          "text": "1–2",
          "order_index": 0
        },
        {
          "text": "3–4",
          "order_index": 1
        },
        {
          "text": "5–6",
          "order_index": 2
        },
        {
          "text": "7–9",
          "order_index": 3
        },
        {
          "text": "10 или больше",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто вы выпиваете 6 или более стандартных порций алкоголя за один раз?",
      "is_required": true,
      "order_index": 2,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто за последний год вы обнаруживали, что не можете прекратить употребление алкоголя после того, как начали пить?",
      "is_required": true,
      "order_index": 3,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто за последний год из-за употребления алкоголя вы не могли выполнить то, что обычно от вас ожидалось?",
      "is_required": true,
      "order_index": 4,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто за последний год вам требовалось выпить утром, чтобы прийти в себя после употребления большого количества алкоголя накануне?",
      "is_required": true,
      "order_index": 5,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто за последний год после употребления алкоголя вы испытывали чувство вины или угрызения совести?",
      "is_required": true,
      "order_index": 6,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Как часто за последний год из-за употребления алкоголя вы не могли вспомнить, что происходило накануне вечером?",
      "is_required": true,
      "order_index": 7,
      "options": [
        {
          "text": "Никогда",
          "order_index": 0
        },
        {
          "text": "Реже одного раза в месяц",
          "order_index": 1
        },
        {
          "text": "Ежемесячно",
          "order_index": 2
        },
        {
          "text": "Еженедельно",
          "order_index": 3
        },
        {
          "text": "Ежедневно или почти ежедневно",
          "order_index": 4
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Получали ли вы или кто-либо другой травму в результате вашего употребления алкоголя?",
      "is_required": true,
      "order_index": 8,
      "options": [
        {
          "text": "Нет",
          "order_index": 0
        },
        {
          "text": "Да, но не за последний год",
          "order_index": 1
        },
        {
          "text": "Да, за последний год",
          "order_index": 2
        }
      ]
    },
    {
      "question_type": "single_choice",
      "text": "Выражал ли родственник, друг, врач или другой медицинский работник обеспокоенность вашим употреблением алкоголя или советовал вам сократить его?",
      "is_required": true,
      "order_index": 9,
      "options": [
        {
          "text": "Нет",
          "order_index": 0
        },
        {
          "text": "Да, но не за последний год",
          "order_index": 1
        },
        {
          "text": "Да, за последний год",
          "order_index": 2
        }
      ]
    }
  ]
}
<!-- ./frontend/app/components/questionnaires/JsonImporter.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const emit = defineEmits([
  'import',
])

const jsonText = ref('')
const errorMessage = ref('')

const supportedTypes = new Set([
  'text',
  'number',
  'boolean',
  'scale',
  'single_choice',
  'multiple_choice',
])

function normalizeQuestionnaire(source) {
  const data = source.questionnaire || source

  if (!data || typeof data !== 'object') {
    throw new Error('JSON должен содержать объект')
  }

  if (
    typeof data.title !== 'string'
    || !data.title.trim()
  ) {
    throw new Error('Поле title обязательно')
  }

  if (!Array.isArray(data.questions)) {
    throw new Error(
      'Поле questions должно быть массивом',
    )
  }

  if (data.questions.length === 0) {
    throw new Error(
      'Опросник должен содержать вопросы',
    )
  }

  const questions = data.questions.map(
    (question, questionIndex) => {
      const questionType = String(
        question.question_type
        || question.type
        || '',
      ).toLowerCase()

      if (!supportedTypes.has(questionType)) {
        throw new Error(
          `Неизвестный тип вопроса №${questionIndex + 1}: ${questionType}`,
        )
      }

      const options = Array.isArray(question.options)
        ? question.options.map(
            (option, optionIndex) => ({
              client_id: crypto.randomUUID(),
              text:
                typeof option === 'string'
                  ? option
                  : String(option.text || ''),
              order_index: optionIndex,
            }),
          )
        : []

      return {
        client_id: crypto.randomUUID(),
        question_type: questionType,
        text: String(question.text || ''),
        is_required:
          question.is_required !== false,
        order_index: questionIndex,
        is_library_hidden: data.is_library_hidden === true,

        scale_min:
          questionType === 'scale'
            ? Number(question.scale_min ?? 0)
            : null,

        scale_max:
          questionType === 'scale'
            ? Number(question.scale_max ?? 10)
            : null,

        scale_min_label:
          question.scale_min_label ?? null,

        scale_max_label:
          question.scale_max_label ?? null,

        options,
      }
    },
  )

  return {
    title: data.title.trim(),
    description: data.description || '',
    pro_content: data.pro_content !== false,
    tag_ids: Array.isArray(data.tag_ids)
      ? data.tag_ids
      : [],
    copied_from_id: data.copied_from_id || null,
    questions,
  }
}

function importJson() {
  errorMessage.value = ''

  try {
    const parsed = JSON.parse(jsonText.value)
    const normalized = normalizeQuestionnaire(parsed)

    emit('import', normalized)
    model.value = false
    jsonText.value = ''
  } catch (error) {
    errorMessage.value =
      error?.message
      || 'Не удалось прочитать JSON'
  }
}

async function handleFile(event) {
  errorMessage.value = ''

  const file = event.target.files?.[0]

  if (!file) return

  if (
    !file.name.toLowerCase().endsWith('.json')
    && file.type !== 'application/json'
  ) {
    errorMessage.value =
      'Выберите файл в формате JSON'
    return
  }

  try {
    jsonText.value = await file.text()
  } catch {
    errorMessage.value =
      'Не удалось прочитать файл'
  } finally {
    event.target.value = ''
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Импорт опросника из JSON"
    max-width-class="max-w-3xl"
  >
    <div class="space-y-5">
      <div
        class="border-primary/30 bg-primary/5 rounded-2xl border p-4"
      >
        <div class="flex items-start gap-3">
          <Icon
            name="lucide:info"
            class="text-primary mt-0.5 size-5 shrink-0"
          />

          <div class="text-sm">
            <p class="font-medium">
              Можно загрузить JSON-файл или вставить JSON
              вручную.
            </p>

            <p class="text-base-content/60 mt-1">
              После импорта опросник можно проверить
              и отредактировать перед сохранением.
            </p>
          </div>
        </div>
      </div>

      <label class="form-control block">
        <span class="label">
          <span class="label-text font-medium">
            JSON-файл
          </span>
        </span>

        <input
          type="file"
          accept=".json,application/json"
          class="file-input file-input-bordered w-full"
          @change="handleFile"
        >
      </label>

      <div class="divider">
        ИЛИ
      </div>

      <label class="form-control block">
        <span class="label">
          <span class="label-text font-medium">
            JSON
          </span>
        </span>

        <textarea
          v-model="jsonText"
          class="textarea textarea-bordered min-h-72 w-full font-mono text-sm"
          placeholder="{ ... }"
        />
      </label>

      <div
        v-if="errorMessage"
        class="alert alert-error"
      >
        <Icon
          name="lucide:circle-alert"
          class="size-5"
        />
        <span>{{ errorMessage }}</span>
      </div>
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-primary"
          :disabled="!jsonText.trim()"
          @click="importJson"
        >
          <Icon
            name="lucide:upload"
            class="size-4"
          />
          Импортировать
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>

также, для кадого этапа надо сделать короткое описание, которое пациент видит - он должен понимать смысл, какие конкретно пробемы реашет этот шаг

сама программа тоже должна включать короткое описание, чего пациент добьется балгодаря нее

также, каждый этап включает Инструкция для врача - хотя, работа это самостоятельноая и не предполагает консультации специалитса, пусть у врача будут короткие инструкции, вдруг пациент спросит его по какому-то шагу. Надо описать, что конкретно делает данный шаг, какие туда входят инструменты и что решает: работа с мотивацией/ улучшение контроля, и т.д.

каждый этап включает шаги. Собственно, шаг - это либо статья либо опросник. Надо сохранить преемственность каждой статьи у каждого шага и сделать так, чтобы сложность увеличивалась

Смотри, у меня приложение настроено на то, чтобы замотивировать пациента на консультацию психиатра. Тут сценарий тавкой: пациент обратился к гастроэнтерологу и специалист решил, что пациент выпивает алкоголь больше обычного. Но просграмма должна включать лишь элементы решения проблемы алкоголя, чтобы не спугнуть пациента от консультации - надо сделать решение пролемы с алкоголем в составе комплекса по измеению образа жизни, а не как самоцель, чтобы пацуиент сам пришел к выводу, что ему нужна консультация психиатра

Если надо, сначала задай необходимые вопросы, приведи заголовки статей и варианты опросников.