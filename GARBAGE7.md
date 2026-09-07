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
