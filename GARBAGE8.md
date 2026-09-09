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
backend/app/modules/programs/routers.py (1806 lines)
backend/app/modules/programs/schemas.py (271 lines)
backend/app/modules/programs/utils.py (576 lines)
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

*Files: 129*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (209 lines)
frontend/app/components/articles/Form.vue (241 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (486 lines)
frontend/app/components/articles/ReaderAction.vue (196 lines)
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
frontend/app/components/layout/Footer.vue (52 lines)
frontend/app/components/layout/Logo.vue (86 lines)
frontend/app/components/layout/Navbar.vue (338 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patient/Home.vue (148 lines)
frontend/app/components/patient/Journey.vue (79 lines)
frontend/app/components/patient/NextStep.vue (184 lines)
frontend/app/components/patient/ProgramCard.vue (258 lines)
frontend/app/components/patient/ProgramSteps.vue (96 lines)
frontend/app/components/patient/PurchaseDialog.vue (110 lines)
frontend/app/components/patient/Support.vue (186 lines)
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
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (389 lines)
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
*Files: 70*

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
frontend/app/pages/questionnaires/index.vue (209 lines)
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
frontend/app/stores/patient-home.js (225 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (206 lines)
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

---- 

Возможно, тебе пригодятся:

# ./backend/app/modules/tags/enums.py
from enum import Enum


class DoctorTagOverrideAction(str, Enum):
    ADD = "add"
    REMOVE = "remove"

# ./backend/app/modules/tags/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.users.models import (
    DoctorProfile,
    PatientProfile,
    Speciality,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Tag(SQLModel, table=True):
    __tablename__ = "tags"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    name: str = Field(
        unique=True,
        index=True,
        max_length=100,
    )
    description: Optional[str] = Field(default=None)

    # Системные теги нельзя удалить через обычный API.
    is_system: bool = Field(default=False, index=True)

    is_hidden: bool = Field(default=False, index=True)
    hidden_at: Optional[datetime] = Field(default=None)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    speciality_links: list["SpecialityTagLink"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    doctor_overrides: list["DoctorTagOverride"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )

    patient_overrides: list["PatientTagOverride"] = Relationship(
        back_populates="tag",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class SpecialityTagLink(SQLModel, table=True):
    __tablename__ = "speciality_tag_links"
    __table_args__ = (
        UniqueConstraint(
            "speciality_id",
            "tag_id",
            name="uq_speciality_tag",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    speciality_id: uuid.UUID = Field(
        foreign_key="specialities.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)

    speciality: Optional[Speciality] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[SpecialityTagLink.speciality_id]",
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="speciality_links",
        sa_relationship_kwargs={
            "foreign_keys": "[SpecialityTagLink.tag_id]",
        },
    )


class DoctorTagOverride(SQLModel, table=True):
    __tablename__ = "doctor_tag_overrides"
    __table_args__ = (
        UniqueConstraint(
            "doctor_id",
            "tag_id",
            name="uq_doctor_tag_override",
        ),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    doctor_id: uuid.UUID = Field(
        foreign_key="doctor_profiles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    action: DoctorTagOverrideAction = Field(index=True)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    doctor: Optional[DoctorProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorTagOverride.doctor_id]",
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="doctor_overrides",
        sa_relationship_kwargs={
            "foreign_keys": "[DoctorTagOverride.tag_id]",
        },
    )

class PatientTagOverride(SQLModel, table=True):
    __tablename__ = "patient_tag_overrides"
    __table_args__ = (
        UniqueConstraint(
            "patient_id",
            "tag_id",
            name="uq_patient_tag_override",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    patient_id: uuid.UUID = Field(
        foreign_key="patient_profiles.id",
        index=True,
    )
    tag_id: uuid.UUID = Field(
        foreign_key="tags.id",
        index=True,
    )

    # Используем тот же enum ADD/REMOVE,
    # что и для индивидуальных тегов врача.
    action: DoctorTagOverrideAction = Field(
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now,
    )
    updated_at: datetime = Field(
        default_factory=utc_now,
    )

    patient: Optional[PatientProfile] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientTagOverride.patient_id]"
            ),
        }
    )

    tag: Optional[Tag] = Relationship(
        back_populates="patient_overrides",
        sa_relationship_kwargs={
            "foreign_keys": (
                "[PatientTagOverride.tag_id]"
            ),
        },
    )

# ./backend/app/modules/tags/schemas.py
import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.modules.tags.enums import DoctorTagOverrideAction


class TagCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class TagUpdateRequest(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    description: str | None = None


class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None
    is_system: bool
    created_at: datetime
    updated_at: datetime


class SpecialityTagResponse(BaseModel):
    speciality_id: uuid.UUID
    speciality_name: str
    tags: list[TagResponse]


class DoctorTagOverrideRequest(BaseModel):
    tag_id: uuid.UUID
    action: DoctorTagOverrideAction


class DoctorTagOverrideResponse(BaseModel):
    id: uuid.UUID
    doctor_id: uuid.UUID
    tag: TagResponse
    action: DoctorTagOverrideAction
    created_at: datetime
    updated_at: datetime


class EffectiveTagResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    is_system: bool

    # default, custom, doctor, patient или system.
    sources: list[str]


class EffectiveTagsResponse(BaseModel):
    owner_type: Literal["doctor", "patient", "relative"]
    owner_id: uuid.UUID
    tags: list[EffectiveTagResponse]


class MessageResponse(BaseModel):
    message: str

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None

    is_system: bool
    is_hidden: bool
    hidden_at: datetime | None

    created_at: datetime
    updated_at: datetime


class TagVisibilityRequest(BaseModel):
    is_hidden: bool

class PatientTagOverrideRequest(BaseModel):
    tag_id: uuid.UUID
    action: DoctorTagOverrideAction


class PatientTagOverrideResponse(BaseModel):
    id: uuid.UUID
    patient_id: uuid.UUID
    tag: TagResponse
    action: DoctorTagOverrideAction
    created_at: datetime
    updated_at: datetime

далее, некоторые файлы будут урезаны, чтобы сэкономить место:

# ./backend/app/modules/tags/utils.py

import uuid
from dataclasses import dataclass, field

from sqlmodel import Session, select

from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.tags.models import (
    DoctorTagOverride,
    PatientTagOverride,
    SpecialityTagLink,
    Tag,
)
from app.modules.tags.schemas import (
    EffectiveTagResponse,
    EffectiveTagsResponse,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    RelativePatientStatus,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    RelativePatientLink,
    RelativeProfile,
)


@dataclass
class EffectiveTagData:
    tag: Tag
    sources: set[str] = field(default_factory=set)


def merge_tag_data(
    target: dict[uuid.UUID, EffectiveTagData],
    source: dict[uuid.UUID, EffectiveTagData],
    source_prefix: str | None = None,
) -> None:
    for tag_id, source_data in source.items():
        if tag_id not in target:
            target[tag_id] = EffectiveTagData(tag=source_data.tag)

        if source_prefix:
            target[tag_id].sources.add(source_prefix)
        else:
            target[tag_id].sources.update(source_data.sources)


def get_doctor_effective_tag_data(
    *,
    session: Session,
    doctor: DoctorProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    default_links = session.exec(
        select(SpecialityTagLink).where(
            SpecialityTagLink.speciality_id
            == doctor.speciality_id
        )
    ).all()

    for link in default_links:
        tag = session.get(Tag, link.tag_id)

        if not tag or tag.is_hidden:
            continue

        result[tag.id] = EffectiveTagData(
            tag=tag,
            sources={"default"},
        )

    overrides = session.exec(
        select(DoctorTagOverride).where(
            DoctorTagOverride.doctor_id == doctor.id
        )
    ).all()

    for override in overrides:
        tag = session.get(Tag, override.tag_id)

        if not tag or tag.is_hidden:
            continue

        if override.action == DoctorTagOverrideAction.REMOVE:
            result.pop(tag.id, None)
            continue

        if tag.id not in result:
            result[tag.id] = EffectiveTagData(tag=tag)

        # Кастомное добавление имеет приоритет над default.
        result[tag.id].sources = {"custom"}

    return result


def get_patient_effective_tag_data(
    *,
    session: Session,
    patient: PatientProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    active_links = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.patient_id == patient.id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).all()

    for link in active_links:
        doctor = session.get(
            DoctorProfile,
            link.doctor_id,
        )

        if not doctor:
            continue

        doctor_tags = get_doctor_effective_tag_data(
            session=session,
            doctor=doctor,
        )

        merge_tag_data(
            target=result,
            source=doctor_tags,
            source_prefix=f"doctor:{doctor.id}",
        )

    # Настройки пациента перекрывают результат
    # наследования от всех врачей.
    patient_overrides = session.exec(
        select(PatientTagOverride).where(
            PatientTagOverride.patient_id
            == patient.id
        )
    ).all()

    for override in patient_overrides:
        tag = session.get(Tag, override.tag_id)

        if not tag or tag.is_hidden:
            continue

        if (
            override.action
            == DoctorTagOverrideAction.REMOVE
        ):
            result.pop(tag.id, None)
            continue

        if tag.id not in result:
            result[tag.id] = EffectiveTagData(
                tag=tag
            )

        result[tag.id].sources = {
            "patient:custom",
        }

    return result


def get_relative_effective_tag_data(
    *,
    session: Session,
    relative: RelativeProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    active_links = session.exec(
        select(RelativePatientLink).where(
            RelativePatientLink.relative_id == relative.id,
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE,
        )
    ).all()

    for link in active_links:
        patient = session.get(
            PatientProfile,
            link.patient_id,
        )

        if not patient:
            continue

        patient_tags = get_patient_effective_tag_data(
            session=session,
            patient=patient,
        )

        merge_tag_data(
            target=result,
            source=patient_tags,
            source_prefix=f"patient:{patient.id}",
        )

    relative_tag = session.exec(
        select(Tag).where(
            Tag.name == "relative",
            Tag.is_system.is_(True),
        )
    ).first()

    if relative_tag and not relative_tag.is_hidden:
        result[relative_tag.id] = EffectiveTagData(
            tag=relative_tag,
            sources={"system"},
        )

    return result


def serialize_effective_tags(
    *,
    owner_type: str,
    owner_id: uuid.UUID,
    tag_data: dict[uuid.UUID, EffectiveTagData],
) -> EffectiveTagsResponse:
    sorted_items = sorted(
        tag_data.values(),
        key=lambda item: item.tag.name.lower(),
    )

    return EffectiveTagsResponse(
        owner_type=owner_type,
        owner_id=owner_id,
        tags=[
            EffectiveTagResponse(
                id=item.tag.id,
                name=item.tag.name,
                description=item.tag.description,
                is_system=item.tag.is_system,
                sources=sorted(item.sources),
            )
            for item in sorted_items
        ],
    )

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
    PatientTagOverride,
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
    PatientTagOverrideRequest,
    PatientTagOverrideResponse,
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
from app.modules.patients.utils import (
    ensure_patient_access,
)

def utc_now() -> datetime:
    FUNCTION BODY
    return datetime.now(timezone.utc)
def get_patient_for_tag_management(
    *,
    session: Session,
    auth: AuthContext,
    patient_id: uuid.UUID,
) -> PatientProfile:
    FUNCTION BODY
    return patient
def get_current_doctor_profile(
    *,
    session: Session,
    auth: AuthContext,
) -> DoctorProfile:
    FUNCTION BODY
    return doctor
def serialize_override(
    *,
    session: Session,
    override: DoctorTagOverride,
) -> DoctorTagOverrideResponse:
    FUNCTION BODY
    return DoctorTagOverrideResponse(
        id=override.id,
        doctor_id=override.doctor_id,
        tag=TagResponse.model_validate(tag),
        action=override.action,
        created_at=override.created_at,
        updated_at=override.updated_at,
    )
def serialize_patient_override(
    *,
    session: Session,
    override: PatientTagOverride,
) -> PatientTagOverrideResponse:
    FUNCTION BODY
    return PatientTagOverrideResponse(
        id=override.id,
        patient_id=override.patient_id,
        tag=TagResponse.model_validate(tag),
        action=override.action,
        created_at=override.created_at,
        updated_at=override.updated_at,
    )
@@router.get("", response_model=list[TagResponse])
async def list_tags(
    include_hidden: bool = Query(default=False),
    _: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[Tag]:
    FUNCTION BODY
    return list(
        session.exec(
            statement.order_by(Tag.name)
        ).all()
    )
@@router.post(
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
    FUNCTION BODY
    return tag
@@router.patch(
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
    FUNCTION BODY
    return tag
@@router.delete(
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
    FUNCTION BODY
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Тег используется {usage_name}. "
                    "Вместо удаления скройте его."
                ),
            )
@@router.patch(
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
    FUNCTION BODY
    return tag
@@router.get(
    "/specialities/{speciality_id}",
    response_model=SpecialityTagResponse,
)
async def get_speciality_tags(
    speciality_id: uuid.UUID,
    _: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> SpecialityTagResponse:
    FUNCTION BODY
    return SpecialityTagResponse(
        speciality_id=speciality.id,
        speciality_name=speciality.name,
        tags=[
            TagResponse.model_validate(tag)
            for tag in tags
        ],
    )
@@router.post(
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
    FUNCTION BODY
    return MessageResponse(
        message="Тег добавлен к специальности"
    )
@@router.delete(
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
    FUNCTION BODY
    return MessageResponse(
        message="Тег удалён из специальности"
    )
@@router.get(
    "/doctors/me/overrides",
    response_model=list[DoctorTagOverrideResponse],
)
async def list_my_doctor_tag_overrides(
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> list[DoctorTagOverrideResponse]:
    FUNCTION BODY
    return [
        serialize_override(
            session=session,
            override=override,
        )
        for override in overrides
    ]
@@router.put(
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
    FUNCTION BODY
    return serialize_override(
        session=session,
        override=override,
    )
@@router.delete(
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
    FUNCTION BODY
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Индивидуальная настройка тега не найдена",
        )
@@router.get(
    "/patients/{patient_id}/effective",
    response_model=EffectiveTagsResponse,
)
async def get_patient_effective_tags_for_staff(
    patient_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> EffectiveTagsResponse:
    FUNCTION BODY
    return serialize_effective_tags(
        owner_type="patient",
        owner_id=patient.id,
        tag_data=tag_data,
    )
@@router.get(
    "/patients/{patient_id}/overrides",
    response_model=list[PatientTagOverrideResponse],
)
async def list_patient_tag_overrides(
    patient_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> list[PatientTagOverrideResponse]:
    FUNCTION BODY
    return [
        serialize_patient_override(
            session=session,
            override=override,
        )
        for override in overrides
    ]
@@router.put(
    "/patients/{patient_id}/overrides",
    response_model=PatientTagOverrideResponse,
)
async def set_patient_tag_override(
    patient_id: uuid.UUID,
    payload: PatientTagOverrideRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> PatientTagOverrideResponse:
    FUNCTION BODY
    return serialize_patient_override(
        session=session,
        override=override,
    )
@@router.delete(
    "/patients/{patient_id}/overrides/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def reset_patient_tag_override(
    patient_id: uuid.UUID,
    tag_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.DOCTOR,
            UserRole.MED_ASSISTANT,
            UserRole.SUPERUSER,
        )
    ),
    session: Session = Depends(get_session),
) -> None:
    FUNCTION BODY
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=(
                "Индивидуальная настройка "
                "тега пациента не найдена"
            ),
        )
@@router.get(
    "/me/effective",
    response_model=EffectiveTagsResponse,
)
async def get_my_effective_tags(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EffectiveTagsResponse:
    FUNCTION BODY
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Для активной роли эффективные теги не предусмотрены",
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
<!-- ./frontend/app/pages/settings/tags.vue -->
<script setup>
definePageMeta({
  middleware: [
    'doctor-only',
  ],
})

const store = useTagAccessStore()
const errorMessage = ref('')
const message = ref('')

async function load() {
  errorMessage.value = ''

  try {
    await store.fetchDoctorState()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить теги врача'
  }
}

async function setOverride({ tag, action }) {
  errorMessage.value = ''
  message.value = ''

  try {
    await store.setDoctorOverride(
      tag.id,
      action,
    )

    message.value = 'Настройка тега сохранена'
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить тег'
  }
}

async function resetOverride(tag) {
  errorMessage.value = ''
  message.value = ''

  try {
    await store.resetDoctorOverride(tag.id)

    message.value = (
      'Восстановлено значение специальности'
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось сбросить настройку'
  }
}

onMounted(load)
</script>

<template>
  <div class="mx-auto max-w-4xl space-y-6">
    <header>
      <h1 class="text-2xl font-bold sm:text-3xl">
        Мои теги
      </h1>

      <p class="text-base-content/60 mt-1">
        Индивидуальная настройка тегов,
        унаследованных от специальности.
      </p>
    </header>

    <div class="alert alert-warning">
      <Icon
        name="lucide:triangle-alert"
        class="size-5"
      />

      <span>
        Изменение ваших тегов повлияет на фильтрацию
        контента у всех прикреплённых пациентов.
      </span>
    </div>

    <div
      v-if="message"
      class="alert alert-success"
    >
      <Icon
        name="lucide:circle-check"
        class="size-5"
      />
      <span>{{ message }}</span>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <section
      class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
    >
      <TagsOverrideEditor
        :tags="store.tags"
        :effective-tags="
          store.doctorEffectiveTags
        "
        :overrides="store.doctorOverrides"
        :loading="store.loadingDoctor"
        :saving="store.saving"
        default-label="Настройка специальности"
        @set="setOverride"
        @reset="resetOverride"
      />
    </section>
  </div>
</template>
<!-- frontend\app\pages\index.vue -->
<template>
  <div>Home</div>
</template>
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
<!-- ./frontend/app/components/layout/Navbar.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()
const ui = useUiStore()

const {
  isStaff,
  activeRoleName,
  navigationGroups,
} = useAppNavigation()

const mobileMenuOpen = ref(false)

function closeMobileMenu() {
  mobileMenuOpen.value = false
}

const invitationsStore = useInvitationsStore()

const patientInviteOpen = ref(false)
const invitationLinkOpen = ref(false)

const createdPatientInvitation = ref(null)
const invitationEmailSent = ref(false)
const invitationEmailError = ref('')

const { isClientReady } = useClientReady()

const isDoctor = computed(() =>
  isClientReady.value
  && auth.activeRole === 'doctor',
)

function handlePatientInvitationCreated(
  invitation,
) {
  createdPatientInvitation.value = invitation
  invitationEmailSent.value = false
  invitationEmailError.value = ''
  invitationLinkOpen.value = true
}

async function sendPatientInvitationEmail() {
  if (!createdPatientInvitation.value) return

  invitationEmailError.value = ''

  try {
    const response =
      await invitationsStore
        .sendPatientInvitation(
          createdPatientInvitation.value
            .invitation_id,
        )

    // При отправке создаётся новая ссылка,
    // поэтому обновляем и QR-код, и ID.
    createdPatientInvitation.value = response

    invitationEmailSent.value = Boolean(
      response.email_sent_at
      && !response.email_send_error,
    )

    invitationEmailError.value =
      response.email_send_error || ''
  } catch (error) {
    invitationEmailSent.value = false
    invitationEmailError.value =
      error?.data?.detail
      || 'Не удалось отправить приглашение'
  }
}

async function handlePatientAttached(response) {
  await navigateTo(
    `/patients/${response.patient_id}`,
  )
}
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
        class="mx-auto grid min-h-16 w-full max-w-7xl grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-2 px-3 py-1 sm:min-h-20 sm:px-4"
      >
      <div class="flex min-w-0 items-center">
        <button
          v-if="isStaff"
          type="button"
          class="btn btn-circle btn-ghost"
          :aria-label="
            ui.sidebarOpen
              ? 'Свернуть боковое меню'
              : 'Открыть боковое меню'
          "
          @click="ui.toggleSidebar"
        >
          <Icon
            :name="
              ui.sidebarOpen
                ? 'lucide:panel-left-close'
                : 'lucide:menu'
            "
            class="size-5"
          />
        </button>

        <button
          v-else
          type="button"
          class="btn btn-circle btn-ghost lg:hidden"
          aria-label="Открыть меню"
          @click="mobileMenuOpen = true"
        >
          <Icon
            name="lucide:menu"
            class="size-5"
          />
        </button>

        <LayoutLogo
          v-if="!isStaff"
          to="/dashboard"
          variant="navbar"
        />
      </div>

      <div
        v-if="!isStaff"
        class="hidden min-w-0 items-center justify-center px-2 lg:flex"
      >
        <UiMegaMenu
          :groups="navigationGroups"
          size-class="megamenu-sm"
        />
      </div>

      <div
        v-else
        class="flex min-w-0 items-center px-2"
      >
        <button
          v-if="isDoctor"
          type="button"
          class="btn btn-primary btn-sm"
          @click="patientInviteOpen = true"
        >
          <Icon
            name="lucide:user-plus"
            class="size-4"
          />

          <span class="hidden sm:inline">
            Пригласить пациента
          </span>
        </button>

        <span
          v-else
          class="text-base-content/60 truncate text-sm"
        >
          ...
        </span>
      </div>

      <div
        class="flex shrink-0 items-center justify-end gap-1"
      >
        <NotificationsCenter />

        <LayoutThemeToggle />

        <div class="dropdown dropdown-end">
          <button
            type="button"
            tabindex="0"
            class="btn btn-ghost gap-2 px-2"
          >
            <div class="avatar avatar-placeholder">
              <div
                class="bg-primary text-primary-content w-9 rounded-full"
              >
                <span class="text-sm">
                  {{ userStore.initials }}
                </span>
              </div>
            </div>

            <div
              class="hidden max-w-44 text-left sm:block"
            >
              <p class="truncate text-sm font-medium">
                {{ userStore.fullName }}
              </p>

              <p
                class="text-base-content/60 min-h-4 truncate text-xs"
              >
                {{ activeRoleName }}
              </p>
            </div>

            <Icon
              name="lucide:chevron-down"
              class="hidden size-4 sm:block"
            />
          </button>

          <ul
            tabindex="0"
            class="menu dropdown-content bg-base-100 border-base-300 z-50 mt-2 w-64 rounded-box border p-2 shadow-xl"
          >
            <li class="menu-title">
              <span class="truncate">
                {{ userStore.user?.email }}
              </span>
            </li>

            <li>
              <NuxtLink to="/settings/profile">
                <Icon
                  name="lucide:user-round"
                  class="size-4"
                />
                Личные данные
              </NuxtLink>
            </li>

            <li>
              <NuxtLink to="/settings/security">
                <Icon
                  name="lucide:key-round"
                  class="size-4"
                />
                Passkey и пароль
              </NuxtLink>
            </li>

            <li>
              <button
                type="button"
                class="text-error"
                @click="auth.logout"
              >
                <Icon
                  name="lucide:log-out"
                  class="size-4"
                />
                Выйти
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>

  <UiBottomSheet
    v-if="!isStaff"
    v-model="mobileMenuOpen"
    title="Меню"
  >
    <nav>
      <ul class="menu w-full gap-1 p-0 text-base">
        <template
          v-for="group in navigationGroups"
          :key="group.key"
        >
          <li class="menu-title mt-2 first:mt-0">
            <span>{{ group.label }}</span>
          </li>

          <li
            v-for="link in group.links"
            :key="link.to"
          >
            <NuxtLink
              :to="link.to"
              @click="closeMobileMenu"
            >
              <Icon
                :name="link.icon"
                class="size-5"
              />
              {{ link.label }}
            </NuxtLink>
          </li>
        </template>
      </ul>
    </nav>

    <template #footer>
      <button
        type="button"
        class="btn btn-error btn-outline w-full"
        @click="auth.logout"
      >
        <Icon
          name="lucide:log-out"
          class="size-4"
        />
        Выйти
      </button>
    </template>
  </UiBottomSheet>

  <InvitationsPatientDialog
    v-if="isDoctor"
    v-model="patientInviteOpen"
    @created="handlePatientInvitationCreated"
    @attached="handlePatientAttached"
  />

  <InvitationsLinkDialog
    v-if="isDoctor"
    v-model="invitationLinkOpen"
    :url="
      createdPatientInvitation
        ?.registration_url || ''
    "
    :email="
      createdPatientInvitation?.email || ''
    "
    title="Приглашение пациента"
    description="Покажите пациенту QR-код, скопируйте ссылку или отправьте её на email."
    can-send-email
    :sending-email="
      invitationsStore.sendingEmail
    "
    :email-sent="invitationEmailSent"
    :email-error="invitationEmailError"
    @send-email="sendPatientInvitationEmail"
  />
</template>
// ./frontend/app/composables/useAppNavigation.js
export function useAppNavigation() {
  const auth = useAuthStore()
  const { isClientReady } = useClientReady()

  const roleNames = {
    superuser: 'Суперпользователь',
    med_assistant: 'Медицинский ассистент',
    doctor: 'Врач',
    patient: 'Пациент',
    relative: 'Родственник',
  }

  const isStaff = computed(() =>
    isClientReady.value
    && [
      'doctor',
      'med_assistant',
      'superuser',
    ].includes(auth.activeRole),
  )

  const canManage = computed(() =>
    isClientReady.value
    && [
      'superuser',
      'med_assistant',
    ].includes(auth.activeRole),
  )

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

  const navigationGroups = computed(() => {
    if (!isClientReady.value) {
      return []
    }

    const mainLinks = [
      {
        to: '/dashboard',
        label: 'Главная',
        icon: 'lucide:layout-dashboard',
        description: 'Обзор и последние действия',
      },
    ]

    if (isStaff.value) {
      mainLinks.push({
        to: '/patients',
        label: 'Пациенты',
        icon: 'lucide:users',
        description: 'Список и карточки пациентов',
      })
    }

    if (canManage.value) {
      mainLinks.push({
        to: '/users',
        label: 'Пользователи',
        icon: 'lucide:user-cog',
        description: 'Аккаунты и приглашения',
      })
    }

    const contentLinks = [
      {
        to: '/content/articles',
        label: 'Статьи',
        icon: 'lucide:file-text',
        description: 'Материалы для пользователей',
      },
      {
        to: '/programs',
        label: 'Программы',
        icon: 'lucide:route',
        description: 'Программы сопровождения',
      },
    ]

    if (auth.activeRole === 'patient') {
      contentLinks.push({
        to: '/questionnaires',
        label: 'Опросники',
        icon: 'lucide:clipboard-list',
        description: 'Назначенные опросники',
      })
    }

    if (canManage.value) {
      contentLinks.push({
        to: '/content/questionnaires',
        label: 'Опросники',
        icon: 'lucide:clipboard-list',
        description: 'Редактор опросников',
      })
    }

    const groups = [
      {
        key: 'main',
        label: 'Работа',
        icon: 'lucide:briefcase',
        links: mainLinks,
      },
      {
        key: 'content',
        label: 'Контент',
        icon: 'lucide:files',
        links: contentLinks,
      },
    ]

    if (canManage.value) {
      groups.push({
        key: 'management',
        label: 'Управление',
        icon: 'lucide:settings-2',
        links: [
          {
            to: '/programs/new',
            label: 'Конфигуратор',
            icon: 'lucide:workflow',
            description: 'Создание программ',
            exact: true,
          },
          {
            to: '/services',
            label: 'Услуги',
            icon: 'lucide:badge-russian-ruble',
            description: 'Цены, скидки и коды услуг',
          },
          {
            to: '/settings/directories',
            label: 'Справочники',
            icon: 'lucide:library',
            description: 'Специальности и теги',
          },
        ],
      })
    }

    const settingsLinks = [
      {
        to: '/settings/profile',
        label: 'Личные данные',
        icon: 'lucide:user-round',
        description: 'ФИО и данные аккаунта',
      },
    ]

    if (auth.activeRole === 'doctor') {
      settingsLinks.push({
        to: '/settings/tags',
        label: 'Мои теги',
        icon: 'lucide:tags',
        description: 'Индивидуальные настройки тегов',
      })
    }

    settingsLinks.push({
      to: '/settings/security',
      label: 'Безопасность',
      icon: 'lucide:shield-check',
      description: 'Пароль и passkey',
    })

    groups.push({
      key: 'settings',
      label: 'Настройки',
      icon: 'lucide:settings',
      links: settingsLinks,
    })

    return groups
  })

  return {
    isStaff,
    canManage,
    activeRoleName,
    navigationGroups,
  }
}
Разумеется, тебе будут нажны еще файлы. Напиши, что надо прислать, потому что проект большой, как видишь

------
Смотри, сейчас главная страница пациента пустая (там написано home). надо сделать главную страницу. На ней я хочу в самом серху расположить главный посыл сервиса: 
Помогаем улучшить Вашу жизнь (думаю, пока сделаем так)
а под ним пусть будет меняться текст при помощи такого daisyui элемента:
<span class="text-rotate text-7xl leading-[2]">
  <span class="justify-items-center">
    <span>📐 DESIGN</span>
    <span>⌨️ DEVELOP</span>
    <span>🌎 DEPLOY</span>
    <span>🌱 SCALE</span>
    <span>🔧 MAINTAIN</span>
    <span>♻️ REPEAT</span>
  </span>
</span>
Пусть там будут типа:
Нормализуем питание
Улучшаем сон
Снижаем стресс
... придумай еще 2-3
И сделай это в виде отдельных компонентов: один компонент - перевертыш текстов, а другой - для главной фразы, в который импортируется перевертыш
я думаю, тут надо сделать Hero
<div
  class="hero min-h-screen"
  style="background-image: url(https://img.daisyui.com/images/stock/photo-1507358522600-9f71e620c44e.webp);"
>
  <div class="hero-overlay"></div>
  <div class="hero-content text-neutral-content text-center">
    <div class="max-w-md">
      <h1 class="mb-5 text-5xl font-bold">Hello there</h1>
      <p class="mb-5">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
учитывай, что нужно делать mobile friendly. и этот компонент не должен занимать весь видимый экран, чтобы пациент мог видеть, что ниже есть карточуки программ (это я напишу ниже)

Посыл такой: у нас холодный старт: врач непсихиатр регистрирует пациента в приложении, где будут комплексные программы с консультациями и без. Без консультаций - программы бесплатные. Платные программы содержат консультации врачей - по сути, пациент покупает комплекс консультаций (оплата только стоимости набора консультаций специалистов), но плюс там будут инструмекнты для самомтоятельной работы: статьи и опросники, которые пациент проходит.

Статьи могут быть и отдельные, и те, которые только входят в программы. Опросники аналогично.

---
Также, сейчас мне не очень нравится, что пациенту вообще непонятно, что за программа и что она улучшает. Надо сделать немного по-другому. Давай сделаем еще одну сущность: life aspect (или придумай, как лучше надзвать). Пусть он будет в модуле tags. Пусть будет так: я смогу делать еще и то, что мы улучшаем: Сон, питание, вредные привычки, снижаем боль, стрессоустойчивость... придумай еще. 
Суперпользователь или медицинский ассистент заходят в отдельный конструктор, там будет список тегов и поля того, что улучшаем. Пользователь сожет drag and drop теги в какой-то аспект. Один тег можно закидывать в разные аспекты. НапримеР, сон можно закинуть и в улучшаем сон и стрессоустойчивость, потому что работа со стрессоустойчивостью также предполагает улучшение сна.

И после этого весь контент ,который содержит теги, может быть разделен на несколько областей, где этот контент полезен.

И после мы на главной странице под Hero, мы разместим так:
если программа отфильтровалась тегами пациента (которые он унаследовал у врача, либо врач пациенту теги задал), то эти программы будут обображаться в самом верху отдельно - Рекомендуемые программы. Для компактности, давай сделаем карусель, где рекомендуемые программы будут слайдиться:
<div class="carousel carousel-center bg-neutral rounded-box max-w-md space-x-4 p-4">
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      alt="Tailwind CSS component"
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      class="rounded-box" />
  </div>
</div>
плюс, добавим кнопки:
<div class="carousel w-full">
  <div id="slide1" class="carousel-item relative w-full">
    <img
      alt="Tailwind CSS slide example"
      src="https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide4" class="btn btn-circle">❮</a>
      <a href="#slide2" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide2" class="carousel-item relative w-full">
    <img
      alt="Tailwind CSS slide example"
      src="https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide1" class="btn btn-circle">❮</a>
      <a href="#slide3" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide3" class="carousel-item relative w-full">
    <img
      alt="Tailwind CSS slide example"
      src="https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide2" class="btn btn-circle">❮</a>
      <a href="#slide4" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide4" class="carousel-item relative w-full">
    <img
      alt="Tailwind CSS slide example"
      src="https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide3" class="btn btn-circle">❮</a>
      <a href="#slide1" class="btn btn-circle">❯</a>
    </div>
  </div>
</div>

это на телефонах. На широких экранах давай сделаем пагинацию по 2-3 программы. Думаю, так будет удобно
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

Кроме того, если пациент проходит какую-то программу, пусть hero уже не будет и эта программа располагается в виде узкой карточки и там будет написано, насколько процентов выполнена и кнопка Продолжить программу. Посчему узкая, потому что пациент может выполнять сразу несколько программ и они не должны сильно сдвигать на главной странице интерфейс вниз

Далее, под рекомендованными программами надо уже добавить карточки со сферами жизни. Карточки давай сделаем подряд вниз (не в карусели). Пусть карточки будут в виде аккордеона
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" checked="checked" />
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">Click the "Sign Up" button in the top right corner and follow the registration process.</div>
</div>
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" />
  <div class="collapse-title font-semibold">I forgot my password. What should I do?</div>
  <div class="collapse-content text-sm">Click on "Forgot Password" on the login page and follow the instructions sent to your email.</div>
</div>
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" />
  <div class="collapse-title font-semibold">How do I update my profile information?</div>
  <div class="collapse-content text-sm">Go to "My Account" settings and select "Edit Profile" to make changes.</div>
</div>
и при раскрытии карточки сферы жизни, там будет список всех входящих в нее программ

На этих программах на главном экране, статьи и опросники в аккордеон сфер жизни не включай, чтобы не захламлять интерфейс.

теперь Navbar пациента:


сейчас там три точки
<span
          v-else
          class="text-base-content/60 truncate text-sm"
        >
          ...
        </span>

а надо сделать так:
На главной странице вместо одного бургера должны быть 3 кнопки. располагаю, как хочу, чтоы было:
ЛОГО, иконка типа greed icon, 