У меня такой проект:
# Project Structure

> Generated: 2026-09-01 00:26

---

## AI Backend

```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (29 lines)
backend/alembic/versions/4a9d77a6cc23_initial_schema.py (887 lines)
backend/alembic/versions/6eb4582e2464_add_new_field_to_users.py (33 lines)
backend/alembic/versions/7c21a6d4ef10_admin_invitations_and_hidden_directories.py (170 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (58 lines)
backend/app/core/db.py (128 lines)
backend/app/core/email.py (150 lines)
backend/app/core/security.py (232 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (105 lines)
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
backend/app/modules/content/utils.py (108 lines)
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
backend/app/modules/invitations/routers.py (1041 lines)
backend/app/modules/invitations/schemas.py (143 lines)
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
backend/app/modules/programs/enums.py (27 lines)
backend/app/modules/programs/models.py (332 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1509 lines)
backend/app/modules/programs/schemas.py (296 lines)
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
backend/app/modules/specialities/__init__.py (0 lines)
backend/app/modules/specialities/routers.py (331 lines)
backend/app/modules/specialities/schemas.py (50 lines)
backend/app/modules/tags/__init__.py (0 lines)
backend/app/modules/tags/enums.py (7 lines)
backend/app/modules/tags/models.py (127 lines)
backend/app/modules/tags/routers.py (698 lines)
backend/app/modules/tags/schemas.py (91 lines)
backend/app/modules/tags/utils.py (214 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (334 lines)
backend/app/modules/users/routers.py (304 lines)
backend/app/modules/users/schemas.py (97 lines)
backend/app/modules/users/utils.py (126 lines)
backend/requirements.txt (47 lines)
backend/seed/create_superuser.py (153 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database.db (875 lines)
```

*Files: 114*

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
frontend/app/components/invitations/LinkDialog.vue (239 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (87 lines)
frontend/app/components/layout/Footer.vue (48 lines)
frontend/app/components/layout/Navbar.vue (365 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (107 lines)
frontend/app/components/patients/List.vue (242 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/programs/configurator/Editor.vue (694 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (272 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/PatientAccess.vue (231 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/viewer/Stage.vue (380 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (529 lines)
frontend/app/components/questionnaires/JsonImporter.vue (264 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/ui/BottomSheet.vue (203 lines)
frontend/app/components/ui/ContentSkeleton.vue (73 lines)
frontend/app/components/ui/MegaMenu.vue (205 lines)
frontend/app/components/ui/Modal.vue (150 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (90 lines)
frontend/app/components/users/InvitationList.vue (231 lines)
frontend/app/components/users/InviteDialog.vue (29 lines)
frontend/app/components/users/InviteForm.vue (367 lines)
frontend/app/components/users/List.vue (182 lines)
```
*Files: 48*

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
frontend/app/pages/patients/[id]/index.vue (465 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (30 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (359 lines)
frontend/app/pages/programs/index.vue (284 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (375 lines)
frontend/app/pages/questionnaires/index.vue (151 lines)
frontend/app/pages/register/invitation.vue (321 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/settings/directories.vue (90 lines)
frontend/app/pages/settings/security.vue (325 lines)
frontend/app/pages/users/index.vue (529 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 26*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (18 lines)
```
*Files: 2*

### composables

```
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useProgramPrice.js (67 lines)
frontend/app/composables/useReadingProgress.js (178 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 6*

### stores

```
frontend/app/stores/articles.js (106 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/notifications.js (312 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (174 lines)
frontend/app/stores/ui.js (62 lines)
frontend/app/stores/user.js (71 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 11*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/program-manager.js (19 lines)
frontend/app/middleware/user-manager.js (19 lines)
```
*Files: 3*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*
-------------------

# ./backend/app/modules/programs/models.py
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import Column, Numeric, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.modules.articles.models import Article
from app.modules.programs.enums import (
    ProgramCurrency,
    ProgramEnrollmentStatus,
    ProgramItemType,
)
from app.modules.questionnaires.models import Questionnaire
from app.modules.tags.models import Tag
from app.modules.users.models import (
    PatientProfile,
    Speciality,
    User,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Program(SQLModel, table=True):
    __tablename__ = "programs"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str = Field(index=True, max_length=300)
    description: Optional[str] = Field(default=None)

    pro_content: bool = Field(default=False, index=True)

    price_amount: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(
            Numeric(12, 2),
            nullable=True,
        ),
    )
    currency: Optional[ProgramCurrency] = Field(
        default=None,
    )

    discount_percent: int = Field(
        default=0,
        ge=0,
        le=100,
    )
    is_popular: bool = Field(
        default=False,
        index=True,
    )

    is_hidden: bool = Field(default=False, index=True)

    created_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    hidden_at: Optional[datetime] = Field(default=None)

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

в общем, надо немного переделать...

Сейчас я в самой программе устанавливаю стоимость, вид валюты, скидку, и т.д.

Надо сделать промежуточный слой наверное, назовем её Service (услуга)

В нее мы перенесем: price_amount, currency, discount_percent, и добавим код услуги (как называть реши сам)

Идея такая: у нас медицинский центр. В нем утверждаются коды услуг, например услуга PRG568 стоит 1000 условных единиц, услуга PRG569 стоит 2580 условных единиц, а услуга PRG560 - всего 200 условных единиц (или рублей, не важно). Мы можем согласовывать скидку под конкретную услугу, а не программу.
Услуг - ограниченное количество, а программ может быть несколько. Например, под услугу PRG568 я сделаю программы с психиатром и психотерапевтом (закину в них консультации, статьи, опросники), а под PRG569 сделаю компленксную мультидисциплинарную программу с несколькими специальностями... 

То есть, я сначала создаю услугу, а потом при создании программы эту услугу указываю в программе и уже на странице с программами цена, скидка и тд будут подтягиваться из услуги, а этапы, консулдьтации специалистов - из Программы.

Давай, наверное, сделаем отдельный модуль services.

Напиши, какие файлы тебе нужны и задай дополнитлеьные вопросы.

Начнем делать с бекенда, затем сделаем на фронтенде































-----------------
Предварительная связь: все - да. Плюс, давай сделаем так, что если у программы нет услуги, то она будет бесплатной

1. Обязательность услуги если программа не содержит услугу, то она будет отображаться как бесплатная
2. Бесплатные услуги да, отлично ты придумал. Но тогда надо решить, можно ли привязывать программу к услуге с NULL-ценой. - в этом случае пусть пишется ,чт оцена по запросу
3. Код услуги - отлично!
4. Наименование услуги - да, пусть будет даже поле описания помимо title как ты предложил
5. Скидка - да, давай так сделаем. зачем хранить то, что можно вычислить
6. Изменение цены: Если администратор изменит стоимость услуги, должна ли новая цена автоматически появиться во всех связанных программах? - да! разумеется. Не заморачивайся со снимком цены
7. Архивирование и удаление: давай если услуга связана с программой, мы ее будем скрывать и остальное как ты предложил
8. Права доступа: просматривать полный каталог услуг; сможет суперпользователь и мед ассистент. создавать услуги, редактировать цену и скидку, скрывать и восстанавливать услуги, может суперпользователь. выбирать услугу при создании программы может также мед ассистент
Пациент также не видит код услуги (он ему просто незачем). Остальные код услуги видят, чтобы его выставить в другой CRM
9. Валюта ну, давай перенесем
10. Что делать с существующими программами: не заморачивайся. я еще не создавал
11. is_popular пусть относится к Прорамме, а не к услуге
12. Выдача программ через API ну, давай сделаем вложенной



















---------------
1. Поведение бесплатной программы: да, бесплатная программа доступна без покупки. Но если внутри нее есть Pro контент (статьи или опросники, они остаются недоступны, пока ассистент не даст пациенту доступ"). по сути, платная или бесплатная программа - условное понятие - оно нужно для того, чтобы пациент увилед цену и нажал на купить. Тогда ассистент увидит, что пациент хочет приобрести программу и после этого ассистент свяжется с пациентом и пациент произведет оплату (не на данном сервисе), и после этого ассистент откроет доступ к Pro контенту. Как бы, так... Вообще, в 90% случаев, программы будут платными: там будут бесплатные материалы для ознакомления и остальные платные, которые откроются после того, как ассистент откроет доступ. И программа - это не только статьи и опросники, но и консультации, которые входят пакетом. В программе консультации - только обозначаются, чтобы пациент понимал, из чего строится стоимость программы. Но, например, программы в рамках чекапов - будут бесплатные программы, которые пациент делает, чтобы вовлечь его в работу с сервисом
2. 