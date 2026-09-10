У меня такой проект:

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
backend/alembic/versions/b1e4c7d902af_content_library_visibility.py (40 lines)
backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py (141 lines)
backend/alembic/versions/d3f8a2c6e901_life_aspects.py (157 lines) (это последняя миграция)
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
backend/app/main.py (113 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/access.py (64 lines)
backend/app/modules/articles/models.py (126 lines)
backend/app/modules/articles/routers.py (918 lines)
backend/app/modules/articles/schemas.py (127 lines)
backend/app/modules/articles/tracking.py (91 lines)
backend/app/modules/articles/utils.py (186 lines)
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
backend/app/modules/consents/contact_routers.py (187 lines)
backend/app/modules/consents/contact_schemas.py (20 lines)
backend/app/modules/consents/contact_service.py (123 lines)
backend/app/modules/consents/enums.py (15 lines)
backend/app/modules/consents/models.py (83 lines)
backend/app/modules/consents/routers.py (252 lines)
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
backend/app/modules/notifications/ToDo.md (1 lines)
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
backend/app/modules/programs/routers.py (1848 lines)
backend/app/modules/programs/schemas.py (274 lines)
backend/app/modules/programs/utils.py (632 lines)
backend/app/modules/questionnaires/__init__.py (0 lines)
backend/app/modules/questionnaires/enums.py (17 lines)
backend/app/modules/questionnaires/json_q/audit.json (272 lines)
backend/app/modules/questionnaires/models.py (237 lines)
backend/app/modules/questionnaires/Readme.md (61 lines)
backend/app/modules/questionnaires/routers.py (1291 lines)
backend/app/modules/questionnaires/schemas.py (218 lines)
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
backend/app/modules/tags/life_aspect_catalog.py (227 lines)
backend/app/modules/tags/life_aspect_patient_routers.py (46 lines)
backend/app/modules/tags/life_aspect_routers.py (360 lines)
backend/app/modules/tags/life_aspect_schemas.py (131 lines)
backend/app/modules/tags/models.py (279 lines)
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
backend/seed/check_program_progress.py (140 lines)
backend/seed/create_superuser.py (153 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/repair_program_submission_stage.py (193 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database — копия.db (1254 lines)
backend/test_database.db (1408 lines)
```

*Files: 141*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (209 lines)
frontend/app/components/articles/Form.vue (241 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (523 lines)
frontend/app/components/articles/ReaderAction.vue (209 lines)
frontend/app/components/assignments/ContentPicker.vue (181 lines)
frontend/app/components/assignments/CreateDialog.vue (345 lines)
frontend/app/components/assignments/PatientList.vue (108 lines)
frontend/app/components/assignments/PickerItem.vue (130 lines)
frontend/app/components/auth/PasswordForm.vue (173 lines)
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (294 lines)
frontend/app/components/content/LibraryVisibility.vue (38 lines)
frontend/app/components/content/RichTextEditor.vue (469 lines)
frontend/app/components/content/RichTextRenderer.vue (136 lines)
frontend/app/components/content/TagSelector.vue (80 lines)
frontend/app/components/directories/Specialities.vue (471 lines)
frontend/app/components/directories/Tags.vue (311 lines)
frontend/app/components/invitations/LinkDialog.vue (257 lines)
frontend/app/components/invitations/PatientDialog.vue (435 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (88 lines)
frontend/app/components/layout/Footer.vue (53 lines)
frontend/app/components/layout/Logo.vue (86 lines)
frontend/app/components/layout/Navbar.vue (405 lines)
frontend/app/components/layout/PatientActions.vue (15 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/life-aspects/FormDialog.vue (165 lines)
frontend/app/components/life-aspects/Tag.vue (85 lines)
frontend/app/components/life-aspects/TagLinks.vue (392 lines)
frontend/app/components/notifications/BrowserPermission.vue (96 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patient/ContactDialog.vue (209 lines)
frontend/app/components/patient/Home.vue (179 lines)
frontend/app/components/patient/home/ContinueCard.vue (74 lines)
frontend/app/components/patient/home/Hero.vue (51 lines)
frontend/app/components/patient/home/LifeAspects.vue (69 lines)
frontend/app/components/patient/home/Recommendations.vue (265 lines)
frontend/app/components/patient/home/RotatingText.vue (119 lines)
frontend/app/components/patient/Journey.vue (79 lines)
frontend/app/components/patient/NextStep.vue (184 lines)
frontend/app/components/patient/ProgramCard.vue (233 lines)
frontend/app/components/patient/ProgramSteps.vue (96 lines)
frontend/app/components/patient/PurchaseDialog.vue (129 lines)
frontend/app/components/patient/Support.vue (186 lines)
frontend/app/components/patient/support/Actions.vue (48 lines)
frontend/app/components/patient/support/Fab.vue (24 lines)
frontend/app/components/patient/support/Hub.vue (105 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (111 lines)
frontend/app/components/patients/List.vue (257 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/patients/Tags.vue (105 lines)
frontend/app/components/programs/configurator/Editor.vue (738 lines)
frontend/app/components/programs/configurator/HomeSettings.vue (68 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (395 lines)
frontend/app/components/programs/configurator/LibraryEntry.vue (70 lines)
frontend/app/components/programs/configurator/ServiceSelect.vue (170 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/journey/Navbar.vue (383 lines)
frontend/app/components/programs/journey/Steps.vue (69 lines)
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/StaffOverview.vue (404 lines)
frontend/app/components/programs/viewer/Stage.vue (443 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (537 lines)
frontend/app/components/questionnaires/JsonImporter.vue (265 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/services/DeleteDialog.vue (95 lines)
frontend/app/components/services/FormDialog.vue (463 lines)
frontend/app/components/services/List.vue (181 lines)
frontend/app/components/services/VisibilityDialog.vue (98 lines)
frontend/app/components/tags/OverrideEditor.vue (231 lines)
frontend/app/components/test/PsychiatristCard.vue (84 lines)
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
*Files: 88*

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
frontend/app/pages/index.vue (25 lines)
frontend/app/pages/login.vue (241 lines)
frontend/app/pages/patients/[id]/index.vue (469 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (37 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (287 lines)
frontend/app/pages/programs/index.vue (285 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (497 lines)
frontend/app/pages/questionnaires/index.vue (209 lines)
frontend/app/pages/register/invitation.vue (379 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/services/index.vue (205 lines)
frontend/app/pages/settings/directories.vue (90 lines)
frontend/app/pages/settings/life-aspects.vue (382 lines)
frontend/app/pages/settings/profile.vue (265 lines)
frontend/app/pages/settings/security.vue (325 lines)
frontend/app/pages/settings/tags.vue (123 lines)
frontend/app/pages/users/index.vue (529 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 30*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (22 lines)
frontend/app/layouts/program.vue (40 lines)
```
*Files: 3*

### composables

```
frontend/app/composables/useAppNavigation.js (199 lines)
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useFooterAwarePosition.js (147 lines)
frontend/app/composables/useProgramContext.js (62 lines)
frontend/app/composables/useProgramJourney.js (97 lines)
frontend/app/composables/useProgramPrice.js (180 lines)
frontend/app/composables/useReadingProgress.js (203 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 10*

### stores

```
frontend/app/stores/articles.js (172 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/emc-app.js (61 lines)
frontend/app/stores/invitations.js (53 lines)
frontend/app/stores/life-aspects.js (158 lines)
frontend/app/stores/notifications.js (387 lines)
frontend/app/stores/patient-home.js (339 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/patient-support.js (29 lines)
frontend/app/stores/program-journey.js (137 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (206 lines)
frontend/app/stores/services.js (159 lines)
frontend/app/stores/tag-access.js (210 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 19*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/doctor-only.js (14 lines)
frontend/app/middleware/life-aspect-manager.js (20 lines)
frontend/app/middleware/program-manager.js (19 lines)
frontend/app/middleware/service-manager.js (19 lines)
frontend/app/middleware/user-manager.js (19 lines)
```
*Files: 6*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*



-------

ФАЙЛЫ, КОТОРЫЕ МОГУТ ПРИГОДИТЬСЯ:
"""Add life aspects and their tag links."""

from alembic import op
import sqlalchemy as sa


revision = "d3f8a2c6e901"
down_revision = "b1e4c7d902af"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "life_aspects",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "order_index",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
        sa.Column(
            "hidden_at",
            sa.DateTime(),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_life_aspects_name",
        "life_aspects",
        ["name"],
        unique=True,
    )
    op.create_index(
        "ix_life_aspects_order_index",
        "life_aspects",
        ["order_index"],
        unique=False,
    )
    op.create_index(
        "ix_life_aspects_is_hidden",
        "life_aspects",
        ["is_hidden"],
        unique=False,
    )

    op.create_table(
        "life_aspect_tag_links",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "life_aspect_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "tag_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["life_aspect_id"],
            ["life_aspects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "life_aspect_id",
            "tag_id",
            name="uq_life_aspect_tag",
        ),
    )

    op.create_index(
        "ix_life_aspect_tag_links_life_aspect_id",
        "life_aspect_tag_links",
        ["life_aspect_id"],
        unique=False,
    )
    op.create_index(
        "ix_life_aspect_tag_links_tag_id",
        "life_aspect_tag_links",
        ["tag_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_life_aspect_tag_links_tag_id",
        table_name="life_aspect_tag_links",
    )
    op.drop_index(
        "ix_life_aspect_tag_links_life_aspect_id",
        table_name="life_aspect_tag_links",
    )
    op.drop_table("life_aspect_tag_links")

    op.drop_index(
        "ix_life_aspects_is_hidden",
        table_name="life_aspects",
    )
    op.drop_index(
        "ix_life_aspects_order_index",
        table_name="life_aspects",
    )
    op.drop_index(
        "ix_life_aspects_name",
        table_name="life_aspects",
    )
    op.drop_table("life_aspects")

# backend\app\modules\tags\life_aspect_schemas.py

import uuid
from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)

from app.modules.tags.schemas import TagResponse


class LifeAspectCreateRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=50_000,
    )

    order_index: int = Field(
        default=0,
        ge=0,
        le=100_000,
    )

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value):
        if isinstance(value, str):
            return value.strip()

        return value


class LifeAspectUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=50_000,
    )

    order_index: int | None = Field(
        default=None,
        ge=0,
        le=100_000,
    )

    is_hidden: bool | None = None

    @field_validator("name", mode="before")
    @classmethod
    def normalize_name(cls, value):
        if isinstance(value, str):
            return value.strip()

        return value

    @model_validator(mode="after")
    def reject_null_required_fields(self):
        # Отсутствие поля означает "не изменять".
        # Явный null допустим только для description.
        for field_name in (
            "name",
            "order_index",
            "is_hidden",
        ):
            if (
                field_name in self.model_fields_set
                and getattr(self, field_name) is None
            ):
                raise ValueError(
                    f"Поле {field_name} не может быть null"
                )

        return self


class LifeAspectResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None

    order_index: int

    is_hidden: bool
    hidden_at: datetime | None

    created_at: datetime
    updated_at: datetime

    tags: list[TagResponse]

class LifeAspectProgramResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None

    is_paid: bool
    is_popular: bool
    is_start: bool
    home_priority: int

    is_recommended: bool

    # Можно ли открыть существующий пациентский
    # endpoint подробного просмотра программы.
    # Это НЕ разрешение на платные материалы.
    can_open_program: bool

    has_program_access: bool


class LifeAspectPatientResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    order_index: int

    programs: list[LifeAspectProgramResponse]

# backend\app\modules\tags\life_aspect_routers.py

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
from app.modules.tags.life_aspect_schemas import (
    LifeAspectCreateRequest,
    LifeAspectResponse,
    LifeAspectUpdateRequest,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.tags.schemas import TagResponse
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/life-aspects/manage",
    tags=["Life aspects: management"],
    dependencies=[
        Depends(
            require_roles(
                UserRole.SUPERUSER,
                UserRole.MED_ASSISTANT,
            )
        ),
    ],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_aspect(
    *,
    session: Session,
    aspect_id: uuid.UUID,
) -> LifeAspect:
    aspect = session.get(LifeAspect, aspect_id)

    if aspect is None:
        raise HTTPException(
            status_code=404,
            detail="Сфера жизни не найдена",
        )

    return aspect


def serialize_aspects(
    *,
    session: Session,
    aspects: list[LifeAspect],
) -> list[LifeAspectResponse]:
    if not aspects:
        return []

    tags_by_aspect: dict[
        uuid.UUID,
        list[TagResponse],
    ] = {
        aspect.id: []
        for aspect in aspects
    }

    # Загружаем связи всех выбранных сфер одним запросом.
    rows = session.exec(
        select(
            LifeAspectTagLink.life_aspect_id,
            Tag,
        )
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id.in_(
                list(tags_by_aspect)
            )
        )
        .order_by(Tag.name, Tag.id)
    ).all()

    for aspect_id, tag in rows:
        tags_by_aspect[aspect_id].append(
            TagResponse.model_validate(tag)
        )

    return [
        LifeAspectResponse(
            id=aspect.id,
            name=aspect.name,
            description=aspect.description,
            order_index=aspect.order_index,
            is_hidden=aspect.is_hidden,
            hidden_at=aspect.hidden_at,
            created_at=aspect.created_at,
            updated_at=aspect.updated_at,
            tags=tags_by_aspect[aspect.id],
        )
        for aspect in aspects
    ]


def serialize_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> LifeAspectResponse:
    return serialize_aspects(
        session=session,
        aspects=[aspect],
    )[0]


def save_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> None:
    session.add(aspect)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=409,
            detail=(
                "Не удалось сохранить сферу жизни: "
                "конфликт данных. Проверьте, нет ли "
                "сферы с таким же названием."
            ),
        ) from error

    session.refresh(aspect)


@router.get(
    "",
    response_model=list[LifeAspectResponse],
)
async def list_life_aspects(
    include_hidden: bool = Query(default=False),
    session: Session = Depends(get_session),
) -> list[LifeAspectResponse]:
    statement = select(LifeAspect)

    if not include_hidden:
        statement = statement.where(
            LifeAspect.is_hidden.is_(False)
        )

    aspects = session.exec(
        statement.order_by(
            LifeAspect.order_index,
            LifeAspect.name,
            LifeAspect.id,
        )
    ).all()

    return serialize_aspects(
        session=session,
        aspects=list(aspects),
    )


@router.post(
    "",
    response_model=LifeAspectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_life_aspect(
    payload: LifeAspectCreateRequest,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = LifeAspect(
        name=payload.name,
        description=payload.description,
        order_index=payload.order_index,
    )

    save_aspect(
        session=session,
        aspect=aspect,
    )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.patch(
    "/{aspect_id}",
    response_model=LifeAspectResponse,
)
async def update_life_aspect(
    aspect_id: uuid.UUID,
    payload: LifeAspectUpdateRequest,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    changes = payload.model_dump(exclude_unset=True)

    if not changes:
        return serialize_aspect(
            session=session,
            aspect=aspect,
        )

    now = utc_now()

    if "is_hidden" in changes:
        next_is_hidden = changes.pop("is_hidden")

        if next_is_hidden != aspect.is_hidden:
            aspect.is_hidden = next_is_hidden
            aspect.hidden_at = (
                now if next_is_hidden else None
            )

    for field_name, value in changes.items():
        setattr(aspect, field_name, value)

    aspect.updated_at = now

    save_aspect(
        session=session,
        aspect=aspect,
    )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.put(
    "/{aspect_id}/tags/{tag_id}",
    response_model=LifeAspectResponse,
)
async def add_life_aspect_tag(
    aspect_id: uuid.UUID,
    tag_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> LifeAspectResponse:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    tag = session.get(Tag, tag_id)

    if tag is None:
        raise HTTPException(
            status_code=404,
            detail="Тег не найден",
        )

    if tag.is_hidden:
        raise HTTPException(
            status_code=409,
            detail=(
                "Скрытый тег нельзя добавить. "
                "Сначала восстановите его в справочнике."
            ),
        )

    statement = select(LifeAspectTagLink).where(
        LifeAspectTagLink.life_aspect_id == aspect.id,
        LifeAspectTagLink.tag_id == tag.id,
    )

    existing = session.exec(statement).first()

    if existing is None:
        session.add(
            LifeAspectTagLink(
                life_aspect_id=aspect.id,
                tag_id=tag.id,
            )
        )

        aspect.updated_at = utc_now()
        session.add(aspect)

        try:
            session.commit()
        except IntegrityError:
            session.rollback()

            # Параллельное повторное добавление той же
            # связи считаем успешной идемпотентной операцией.
            existing = session.exec(statement).first()

            if existing is None:
                raise

        aspect = get_aspect(
            session=session,
            aspect_id=aspect_id,
        )

    return serialize_aspect(
        session=session,
        aspect=aspect,
    )


@router.delete(
    "/{aspect_id}/tags/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_life_aspect_tag(
    aspect_id: uuid.UUID,
    tag_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> None:
    aspect = get_aspect(
        session=session,
        aspect_id=aspect_id,
    )

    link = session.exec(
        select(LifeAspectTagLink).where(
            LifeAspectTagLink.life_aspect_id == aspect.id,
            LifeAspectTagLink.tag_id == tag_id,
        )
    ).first()

    if link is None:
        return

    session.delete(link)

    aspect.updated_at = utc_now()
    session.add(aspect)

    session.commit()

# ./backend/app/modules/tags/life_aspect_patient_routers.py
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import (
    AuthContext,
    require_roles,
)
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
)
from app.modules.tags.life_aspect_catalog import (
    build_patient_life_aspects,
)
from app.modules.tags.life_aspect_schemas import (
    LifeAspectPatientResponse,
)
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/life-aspects",
    tags=["Life aspects: patient"],
)


@router.get(
    "/patient",
    response_model=list[LifeAspectPatientResponse],
)
async def list_life_aspects_for_patient(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[LifeAspectPatientResponse]:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    return build_patient_life_aspects(
        session=session,
        patient=patient,
    )

# ./backend/app/modules/tags/life_aspect_catalog.py
import uuid

from sqlmodel import Session, select

from app.modules.content.utils import (
    get_patient_effective_tag_ids,
    tags_match,
)
from app.modules.programs.models import (
    PatientProgramAccess,
    Program,
    ProgramTagLink,
)
from app.modules.tags.life_aspect_schemas import (
    LifeAspectPatientResponse,
    LifeAspectProgramResponse,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.users.models import PatientProfile


def build_patient_life_aspects(
    *,
    session: Session,
    patient: PatientProfile,
) -> list[LifeAspectPatientResponse]:
    aspects = session.exec(
        select(LifeAspect)
        .where(
            LifeAspect.is_hidden.is_(False)
        )
        .order_by(
            LifeAspect.order_index,
            LifeAspect.name,
            LifeAspect.id,
        )
    ).all()

    if not aspects:
        return []

    aspect_ids = [aspect.id for aspect in aspects]

    # Для группировки используем только нескрытые теги.
    aspect_links = session.exec(
        select(LifeAspectTagLink)
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id.in_(aspect_ids),
            Tag.is_hidden.is_(False),
        )
    ).all()

    tags_by_aspect: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {
        aspect.id: set()
        for aspect in aspects
    }

    all_aspect_tag_ids: set[uuid.UUID] = set()

    for link in aspect_links:
        tags_by_aspect[link.life_aspect_id].add(
            link.tag_id
        )
        all_aspect_tag_ids.add(link.tag_id)

    if not all_aspect_tag_ids:
        return []

    # Подбираем программы по тегам сфер, а не пациента.
    # Для принадлежности сфере достаточно одного тега.
    programs = session.exec(
        select(Program)
        .join(
            ProgramTagLink,
            ProgramTagLink.program_id == Program.id,
        )
        .where(
            Program.is_hidden.is_(False),
            ProgramTagLink.tag_id.in_(
                list(all_aspect_tag_ids)
            ),
        )
        .distinct()
    ).all()

    if not programs:
        return []

    program_ids = [program.id for program in programs]

    # Для рекомендации нужны ВСЕ теги программы:
    # сохраняем текущее правило tags_match().
    program_links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id.in_(program_ids)
        )
    ).all()

    tags_by_program: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {
        program.id: set()
        for program in programs
    }

    programs_by_tag: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {}

    for link in program_links:
        tags_by_program[link.program_id].add(link.tag_id)

        if link.tag_id in all_aspect_tag_ids:
            programs_by_tag.setdefault(
                link.tag_id,
                set(),
            ).add(link.program_id)

    accesses = session.exec(
        select(PatientProgramAccess).where(
            PatientProgramAccess.patient_id == patient.id,
            PatientProgramAccess.program_id.in_(program_ids),
        )
    ).all()

    accessible_program_ids = {
        access.program_id
        for access in accesses
        if access.is_active
    }

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    cards_by_program: dict[
        uuid.UUID,
        LifeAspectProgramResponse,
    ] = {}

    for program in programs:
        program_tag_ids = tags_by_program[program.id]

        matches_patient = tags_match(
            patient_tag_ids=patient_tag_ids,
            content_tag_ids=program_tag_ids,
        )

        has_access = program.id in accessible_program_ids

        cards_by_program[program.id] = (
            LifeAspectProgramResponse(
                id=program.id,
                title=program.title,
                description=program.description,

                is_paid=program.service_id is not None,
                is_popular=program.is_popular,
                is_start=program.is_start,
                home_priority=program.home_priority,

                is_recommended=(
                    bool(program_tag_ids)
                    and matches_patient
                ),

                # can_open_program=(
                #     has_access or matches_patient
                # ),
                can_open_program=True,
                has_program_access=has_access,
            )
        )

    result: list[LifeAspectPatientResponse] = []

    for aspect in aspects:
        matching_program_ids: set[uuid.UUID] = set()

        for tag_id in tags_by_aspect[aspect.id]:
            matching_program_ids.update(
                programs_by_tag.get(tag_id, set())
            )

        if not matching_program_ids:
            continue

        cards = [
            cards_by_program[program_id]
            for program_id in matching_program_ids
        ]

        cards.sort(
            key=lambda card: (
                not card.is_recommended,
                -card.home_priority,
                card.title.casefold(),
                str(card.id),
            )
        )

        result.append(
            LifeAspectPatientResponse(
                id=aspect.id,
                name=aspect.name,
                description=aspect.description,
                order_index=aspect.order_index,
                programs=cards,
            )
        )

    return result

# ./backend/app/modules/articles/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
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

    is_library_hidden: bool = Field(
        default=False,
        sa_column=sa.Column(
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
            index=True,
        ),
    )

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
    is_library_hidden: bool = False


class ArticleUpdateRequest(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=300,
    )
    content: str | None = Field(default=None, min_length=1)

    tag_ids: list[uuid.UUID] | None = None
    pro_content: bool | None = None
    is_library_hidden: bool = False

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
    is_library_hidden: bool = False

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
    is_library_hidden: bool = False

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

# ./backend/app/modules/articles/access.py
import uuid

from fastapi import HTTPException
from sqlmodel import Session

from app.modules.articles.models import Article
from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import patient_has_active_assignment
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.utils import (
    ensure_patient_program_content_access,
)
from app.modules.users.models import PatientProfile


def ensure_article_access(
    *,
    session: Session,
    article: Article,
    patient: PatientProfile,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    if article.is_hidden:
        raise HTTPException(
            status_code=403,
            detail="Статья скрыта",
        )

    if program_stage_id is not None and program_id is None:
        raise HTTPException(
            status_code=422,
            detail="Для этапа необходимо указать программу",
        )

    if program_id is not None:
        ensure_patient_program_content_access(
            session=session,
            patient=patient,
            program_id=program_id,
            stage_id=program_stage_id,
            content_type=ProgramItemType.ARTICLE,
            content_id=article.id,
            pro_content=article.pro_content,
        )
        return

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if (
        article.pro_content
        and not patient.pro_enabled
        and not is_assigned
    ):
        raise HTTPException(
            status_code=403,
            detail="Требуется Pro-доступ или назначение врача",
        )

далее, некоторые файлы высылаю сокращенными:
# ./backend/app/modules/articles/routers.py

import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from sqlalchemy.orm import defer
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
    return [
        serialize_article_list_item(
            session=session,
            article=row[4],
            can_access=row[5],
        )
        for row in ranked_articles[offset:offset + limit]
    ]
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

import sqlalchemy as sa
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

    is_library_hidden: bool = Field(
        default=False,
        sa_column=sa.Column(
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
            index=True,
        ),
    )

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

class QuestionnaireLibraryVisibilityRequest(BaseModel):
    is_library_hidden: bool

class QuestionnaireCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    description: str | None = None

    tag_ids: list[uuid.UUID] = []
    pro_content: bool = True
    is_library_hidden: bool = False

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
    is_library_hidden: bool = False

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
    is_library_hidden: bool = False

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
    QuestionnaireLibraryVisibilityRequest,
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
        is_library_hidden=questionnaire.is_library_hidden,
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
@@router.patch(
    "/{questionnaire_id}/library-visibility",
    response_model=QuestionnaireResponse,
)
async def change_questionnaire_library_visibility(
    questionnaire_id: uuid.UUID,
    payload: QuestionnaireLibraryVisibilityRequest,
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
    # Рекомендация по эффективным тегам пациента.
    # Не является разрешением на доступ к материалам.
    is_recommended: bool = False

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
    QuestionnaireSubmission,
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
from app.modules.consents.contact_service import (
    ensure_assistant_contact_allowed,
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
    return response
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

// frontend\app\stores\life-aspects.js

export const useLifeAspectsStore = defineStore(
  'life-aspects',
  () => {
    const { $api } = useNuxtApp()

    const aspects = ref([])
    const tags = ref([])

    const loading = ref(false)
    const saving = ref(false)

    let stateVersion = 0

    const orderedAspects = computed(() =>
      [...aspects.value].sort(
        (left, right) =>
          left.order_index - right.order_index
          || left.name.localeCompare(right.name, 'ru')
          || left.id.localeCompare(right.id),
      ),
    )

    function replaceAspect(aspect) {
      const index = aspects.value.findIndex(
        item => item.id === aspect.id,
      )

      if (index === -1) {
        aspects.value.push(aspect)
      } else {
        aspects.value[index] = aspect
      }
    }

    async function load() {
      if (saving.value) {
        throw new Error('Дождитесь окончания сохранения')
      }

      const version = ++stateVersion
      loading.value = true

      try {
        const [aspectItems, tagItems] = await Promise.all([
          $api('/api/v1/life-aspects/manage', {
            query: { include_hidden: true },
          }),
          $api('/api/v1/tags', {
            query: { include_hidden: true },
          }),
        ])

        if (version !== stateVersion) return

        aspects.value = aspectItems
        tags.value = tagItems
      } catch (error) {
        if (version === stateVersion) throw error
      } finally {
        if (version === stateVersion) {
          loading.value = false
        }
      }
    }

    async function mutate(request, applyResult) {
      if (saving.value || loading.value) {
        throw new Error('Дождитесь окончания операции')
      }

      const version = stateVersion
      saving.value = true

      try {
        const result = await request()

        if (version === stateVersion) {
          applyResult(result)
        }

        return result
      } finally {
        if (version === stateVersion) {
          saving.value = false
        }
      }
    }

    async function saveAspect(payload, aspectId = null) {
      return mutate(
        () => $api(
          aspectId
            ? `/api/v1/life-aspects/manage/${aspectId}`
            : '/api/v1/life-aspects/manage',
          {
            method: aspectId ? 'PATCH' : 'POST',
            body: payload,
          },
        ),
        replaceAspect,
      )
    }

    async function addTag(aspectId, tagId) {
      return mutate(
        () => $api(
          `/api/v1/life-aspects/manage/${aspectId}/tags/${tagId}`,
          { method: 'PUT' },
        ),
        replaceAspect,
      )
    }

    async function removeTag(aspectId, tagId) {
      return mutate(
        () => $api(
          `/api/v1/life-aspects/manage/${aspectId}/tags/${tagId}`,
          { method: 'DELETE' },
        ),
        () => {
          const aspect = aspects.value.find(
            item => item.id === aspectId,
          )

          if (aspect) {
            aspect.tags = aspect.tags.filter(
              tag => tag.id !== tagId,
            )
          }
        },
      )
    }

    function clear() {
      stateVersion += 1
      aspects.value = []
      tags.value = []
      loading.value = false
      saving.value = false
    }

    return {
      aspects,
      orderedAspects,
      tags,
      loading,
      saving,

      load,
      saveAspect,
      addTag,
      removeTag,
      clear,
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
    async function setLibraryVisibility(
        questionnaireId,
        isLibraryHidden,
      ) {
        const { $api } = useNuxtApp()

        const response = await $api(
          `/api/v1/questionnaires/${questionnaireId}/library-visibility`,
          {
            method: 'PATCH',
            body: {
              is_library_hidden: isLibraryHidden,
            },
          },
        )

        const item = questionnaires.value.find(
          current => current.id === questionnaireId,
        )

        if (item) {
          item.is_library_hidden = response.is_library_hidden
        }

        if (currentQuestionnaire.value?.id === questionnaireId) {
          currentQuestionnaire.value.is_library_hidden =
            response.is_library_hidden
        }

        return response
      }

    return {
      questionnaires,
      currentQuestionnaire,
      loading,

      fetchQuestionnaires,
      fetchQuestionnaire,
      createQuestionnaire,
      setVisibility,
      setLibraryVisibility,

      fetchMyProgress,
      startQuestionnaire,
      fetchSubmission,
      saveAnswer,
      completeSubmission,
    }
  },
)

Надо добавить медиа. Я не знаю, в какую папку лучше добавить: в ./backend/app/media или в ./backend/media 
Картинки пока делаем для статей, опросников, программ и life aspects

Надо сделать отдельный компаненнт загрузки картинки для кажлого элемента. 