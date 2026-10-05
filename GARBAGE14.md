Мой проект:

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
backend/alembic/versions/b1e4c7d902af_content_library_visibility.py (40 lines)
backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py (141 lines)
backend/alembic/versions/d3f8a2c6e901_life_aspects.py (157 lines)
backend/alembic/versions/e4b7c2a901f6_media_images.py (116 lines)
backend/alembic/versions/f7a2d9c103b8_entity_images.py (60 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (73 lines)
backend/app/core/db.py (131 lines)
backend/app/core/email.py (150 lines)
backend/app/core/security.py (232 lines)
backend/app/core/transactions.py (60 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (123 lines)
backend/app/modules/__init__.py (0 lines)
backend/app/modules/articles/__init__.py (0 lines)
backend/app/modules/articles/access.py (64 lines)
backend/app/modules/articles/models.py (132 lines)
backend/app/modules/articles/routers.py (886 lines)
backend/app/modules/articles/schemas.py (133 lines)
backend/app/modules/articles/tracking.py (91 lines)
backend/app/modules/articles/utils.py (188 lines)
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
backend/app/modules/media/__init__.py (0 lines)
backend/app/modules/media/access.py (389 lines)
backend/app/modules/media/constants.py (55 lines)
backend/app/modules/media/image_routers.py (267 lines)
backend/app/modules/media/models.py (68 lines)
backend/app/modules/media/processing.py (214 lines)
backend/app/modules/media/routers.py (265 lines)
backend/app/modules/media/schemas.py (47 lines)
backend/app/modules/media/service.py (158 lines)
backend/app/modules/media/storage.py (71 lines)
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
backend/app/modules/programs/consultation_routers.py (126 lines)
backend/app/modules/programs/consultation_schemas.py (118 lines)
backend/app/modules/programs/consultation_service.py (498 lines)
backend/app/modules/programs/enums.py (22 lines)
backend/app/modules/programs/models.py (364 lines)
backend/app/modules/programs/Readme.md (30 lines)
backend/app/modules/programs/routers.py (1875 lines)
backend/app/modules/programs/schemas.py (279 lines)
backend/app/modules/programs/utils.py (632 lines)
backend/app/modules/questionnaires/__init__.py (0 lines)
backend/app/modules/questionnaires/enums.py (17 lines)
backend/app/modules/questionnaires/json_q/audit.json (272 lines)
backend/app/modules/questionnaires/models.py (243 lines)
backend/app/modules/questionnaires/Readme.md (61 lines)
backend/app/modules/questionnaires/routers.py (1306 lines)
backend/app/modules/questionnaires/schemas.py (223 lines)
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
backend/app/modules/tags/life_aspect_catalog.py (229 lines)
backend/app/modules/tags/life_aspect_patient_routers.py (46 lines)
backend/app/modules/tags/life_aspect_routers.py (384 lines)
backend/app/modules/tags/life_aspect_schemas.py (140 lines)
backend/app/modules/tags/models.py (285 lines)
backend/app/modules/tags/routers.py (957 lines)
backend/app/modules/tags/schemas.py (104 lines)
backend/app/modules/tags/utils.py (246 lines)
backend/app/modules/test_styles/__init__.py (0 lines)
backend/app/modules/test_styles/Readme_delete.md (19 lines)
backend/app/modules/test_styles/routers.py (79 lines)
backend/app/modules/test_styles/schemas.py (34 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (340 lines)
backend/app/modules/users/routers.py (360 lines)
backend/app/modules/users/schemas.py (146 lines)
backend/app/modules/users/utils.py (127 lines)
backend/media/images/1d/1d721b7fd0654c9b9ba91eda1a9b7040.webp (360 lines)
backend/media/images/34/34ddc045ce7f4202958de36ecbd46c56.webp (61 lines)
backend/media/images/8c/8c2c5463ea814c5190f94e6963c0f762.webp (53 lines)
backend/media/images/93/9373e2599ff34916bcb1595b9ee2b281.webp (53 lines)
backend/media/images/93/93b92d16e612422ea666b826be259b2e.webp (354 lines)
backend/media/images/cb/cb4b533270a1433da4bb7d0bddd56e9e.webp (41 lines)
backend/media/images/d3/d35f720d0b6a4179ba97aaae61cbe00f.webp (61 lines)
backend/requirements.txt (48 lines)
backend/seed/check_program_progress.py (140 lines)
backend/seed/create_superuser.py (153 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/repair_program_submission_stage.py (193 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database — копия.db (1254 lines)
backend/test_database.db (1519 lines)
```

*Files: 167*

---

## Frontend

### components

```
frontend/app/components/articles/Card.vue (237 lines)
frontend/app/components/articles/FinishButton.vue (33 lines)
frontend/app/components/articles/Form.vue (256 lines)
frontend/app/components/articles/PatientOverview.vue (185 lines)
frontend/app/components/articles/Reader.vue (521 lines)
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
frontend/app/components/Info/Article.vue (62 lines)
frontend/app/components/invitations/LinkDialog.vue (257 lines)
frontend/app/components/invitations/PatientDialog.vue (435 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (88 lines)
frontend/app/components/layout/Footer.vue (53 lines)
frontend/app/components/layout/Logo.vue (86 lines)
frontend/app/components/layout/Navbar.vue (409 lines)
frontend/app/components/layout/PatientActions.vue (15 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/life-aspects/FormDialog.vue (187 lines)
frontend/app/components/life-aspects/Tag.vue (85 lines)
frontend/app/components/life-aspects/TagLinks.vue (392 lines)
frontend/app/components/media/Cropper.client.vue (206 lines)
frontend/app/components/media/EntityEditor.vue (264 lines)
frontend/app/components/media/Field.vue (336 lines)
frontend/app/components/media/Image.vue (156 lines)
frontend/app/components/notifications/BrowserPermission.vue (96 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patient/ContactDialog.vue (209 lines)
frontend/app/components/patient/Home.vue (179 lines)
frontend/app/components/patient/home/ContinueCard.vue (74 lines)
frontend/app/components/patient/home/Hero.vue (51 lines)
frontend/app/components/patient/home/LifeAspects.vue (107 lines)
frontend/app/components/patient/home/Recommendations.vue (265 lines)
frontend/app/components/patient/home/RotatingText.vue (119 lines)
frontend/app/components/patient/Journey.vue (79 lines)
frontend/app/components/patient/NextStep.vue (184 lines)
frontend/app/components/patient/ProgramCard.vue (277 lines)
frontend/app/components/patient/Programs.vue (191 lines)
frontend/app/components/patient/ProgramSteps.vue (96 lines)
frontend/app/components/patient/PurchaseDialog.vue (129 lines)
frontend/app/components/patient/Support.vue (186 lines)
frontend/app/components/patient/support/Actions.vue (48 lines)
frontend/app/components/patient/support/ConsultationButton.vue (27 lines)
frontend/app/components/patient/support/Fab.vue (24 lines)
frontend/app/components/patient/support/Hub.vue (105 lines)
frontend/app/components/patients/ContactStatus.vue (66 lines)
frontend/app/components/patients/Item.vue (111 lines)
frontend/app/components/patients/List.vue (257 lines)
frontend/app/components/patients/ProAccess.vue (107 lines)
frontend/app/components/patients/Tags.vue (105 lines)
frontend/app/components/programs/configurator/Editor.vue (784 lines)
frontend/app/components/programs/configurator/HomeSettings.vue (68 lines)
frontend/app/components/programs/configurator/Item.vue (143 lines)
frontend/app/components/programs/configurator/Library.vue (395 lines)
frontend/app/components/programs/configurator/LibraryEntry.vue (70 lines)
frontend/app/components/programs/configurator/ServiceSelect.vue (170 lines)
frontend/app/components/programs/configurator/Stage.vue (251 lines)
frontend/app/components/programs/consultations/ConsultationsDialog.vue (446 lines)
frontend/app/components/programs/consultations/Items.vue (250 lines)
frontend/app/components/programs/journey/Navbar.vue (383 lines)
frontend/app/components/programs/journey/Steps.vue (69 lines)
frontend/app/components/programs/PatientAccess.vue (240 lines)
frontend/app/components/programs/PatientOverview.vue (154 lines)
frontend/app/components/programs/PatientProgress.vue (208 lines)
frontend/app/components/programs/StaffOverview.vue (404 lines)
frontend/app/components/programs/viewer/Stage.vue (452 lines)
frontend/app/components/programs/VisibilityDialog.vue (128 lines)
frontend/app/components/questionnaires/Editor.vue (570 lines)
frontend/app/components/questionnaires/JsonImporter.vue (265 lines)
frontend/app/components/questionnaires/QuestionField.vue (157 lines)
frontend/app/components/questionnaires/QuestionItem.vue (314 lines)
frontend/app/components/services/DeleteDialog.vue (95 lines)
frontend/app/components/services/FormDialog.vue (463 lines)
frontend/app/components/services/List.vue (181 lines)
frontend/app/components/services/VisibilityDialog.vue (98 lines)
frontend/app/components/tags/OverrideEditor.vue (231 lines)
frontend/app/components/test/PsychiatristCard.vue (84 lines)
frontend/app/components/test-styles/Editor.vue (534 lines)
frontend/app/components/test-styles/NavbarActions.vue (61 lines)
frontend/app/components/test-styles/Preview.vue (115 lines)
frontend/app/components/test-styles/SendButton.vue (161 lines)
frontend/app/components/test-styles/ThemeFields.vue (97 lines)
frontend/app/components/ui/BottomSheet.vue (222 lines)
frontend/app/components/ui/ContentSkeleton.vue (73 lines)
frontend/app/components/ui/MegaMenu.vue (205 lines)
frontend/app/components/ui/Modal.vue (157 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (105 lines)
frontend/app/components/users/InvitationList.vue (231 lines)
frontend/app/components/users/InviteDialog.vue (29 lines)
frontend/app/components/users/InviteForm.vue (367 lines)
frontend/app/components/users/List.vue (202 lines)
frontend/app/components/users/PhotoDialog.vue (49 lines)
```
*Files: 104*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue (85 lines)
frontend/app/pages/content/articles/[id]/index.vue (146 lines)
frontend/app/pages/content/articles/index.vue (186 lines)
frontend/app/pages/content/articles/new.vue (49 lines)
frontend/app/pages/content/questionnaires/[id].vue (375 lines)
frontend/app/pages/content/questionnaires/index.vue (166 lines)
frontend/app/pages/content/questionnaires/new.vue (9 lines)
frontend/app/pages/dashboard.vue (159 lines)
frontend/app/pages/forgot-password.vue (102 lines)
frontend/app/pages/index.vue (25 lines)
frontend/app/pages/info/doctor/about.vue (16 lines)
frontend/app/pages/info/doctor/conversation.vue (16 lines)
frontend/app/pages/info/patient.vue (12 lines)
frontend/app/pages/login.vue (241 lines)
frontend/app/pages/patients/[id]/index.vue (469 lines)
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue (184 lines)
frontend/app/pages/patients/index.vue (37 lines)
frontend/app/pages/programs/[id]/edit.vue (16 lines)
frontend/app/pages/programs/[id]/index.vue (287 lines)
frontend/app/pages/programs/index.vue (348 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (497 lines)
frontend/app/pages/questionnaires/index.vue (235 lines)
frontend/app/pages/register/invitation.vue (379 lines)
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/services/index.vue (205 lines)
frontend/app/pages/settings/directories.vue (90 lines)
frontend/app/pages/settings/life-aspects.vue (382 lines)
frontend/app/pages/settings/profile.vue (284 lines)
frontend/app/pages/settings/security.vue (325 lines)
frontend/app/pages/settings/tags.vue (123 lines)
frontend/app/pages/settings/test-styles.vue (14 lines)
frontend/app/pages/users/index.vue (543 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 34*

### utils

```
frontend/app/utils/media.js (98 lines)
frontend/app/utils/test-styles.js (390 lines)
```
*Files: 2*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (22 lines)
frontend/app/layouts/program.vue (40 lines)
```
*Files: 3*

### composables

```
frontend/app/composables/useAppNavigation.js (247 lines)
frontend/app/composables/useBodyScrollLock.js (48 lines)
frontend/app/composables/useBreakpoint.js (30 lines)
frontend/app/composables/useClientReady.js (12 lines)
frontend/app/composables/useFooterAwarePosition.js (147 lines)
frontend/app/composables/useMediaApi.js (73 lines)
frontend/app/composables/usePatientProgramGroups.js (94 lines)
frontend/app/composables/usePrivateImage.js (96 lines)
frontend/app/composables/useProgramContext.js (62 lines)
frontend/app/composables/useProgramJourney.js (97 lines)
frontend/app/composables/useProgramPrice.js (180 lines)
frontend/app/composables/useReadingProgress.js (203 lines)
frontend/app/composables/useWebAuthn.js (172 lines)
```
*Files: 13*

### stores

```
frontend/app/stores/articles.js (172 lines)
frontend/app/stores/assignments.js (99 lines)
frontend/app/stores/auth.js (205 lines)
frontend/app/stores/directories.js (208 lines)
frontend/app/stores/emc-app.js (61 lines)
frontend/app/stores/info.js (44 lines)
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
frontend/app/stores/test-styles.js (221 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 21*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/doctor-only.js (14 lines)
frontend/app/middleware/life-aspect-manager.js (20 lines)
frontend/app/middleware/program-manager.js (19 lines)
frontend/app/middleware/service-manager.js (19 lines)
frontend/app/middleware/test-styles.js (17 lines)
frontend/app/middleware/user-manager.js (19 lines)
```
*Files: 7*

### plugins

```
frontend/app/plugins/api.js (63 lines)
frontend/app/plugins/test-styles.client.js (41 lines)
```
*Files: 2*


я хочу сделать возможность загрузки видео. Смотри, я хочу так:
1. Пусть можно будет загружать 2 вида видео об одном и том же: адатпированное для шрокоэкранных устройств (наверное, 16:9) и для мобильных телефонов. На фронтенде там отдельно будет Добавить видео в sidebar у superuser и medical assistant. Допустим, я нажал на Добавить видео. И там будут поля drag-and-drop и вручную переключатель с выбором формата (желательно, сделать его минималичтичным - в один ряд там будут диагонали, я мышью буду активировать тот, который соответствует формату видео). Если я уже добавил видео для телефонов, то автоматически воторое виде будет определяться как для широких, но я могу потом постфакутм перключить его и тогда ,у другого видео также переключится на противоположный формат
2. Если я загрузил только одно видео, то его проигрвыать на любом устройстве;
3. Редактировать видео можно: удалять и заменять на другое, менять заголовок, менять формат
4. Как и со статьями и опросниками, видео можно сделать Pro (пусть будет по умолчанию), а также скрывать из отдельного доступа - вкладки Видео и тогда видео можно будет посмотреть только внутри программ
5. Добавление Видео в какую-то программу должно быть таким же, как и статьи и опросники - я могу перетаскивать его и вставлять в любом месте.
6. Также опционно можно добавлять картинку с обложкой. Если картинку не добавил, пусть обложка будет первым кадром видео (если это не сильно нагрузит сервер)

я пока не уверен только, потянет ли мой сервис... нет опята работы с видео. я не понимаю, какая нагрузка ложится при просмотре пользователями видео и как вообще этот процесс происходит... Я не хочу использовать какой-то внешний сервис типа Youtube, чтобы полностью контролировать котнет

Посоветуй формат видео, которое оптимальнее всего будет в браузере

В отличии от картинок с редактором при загрузке и автоконверсией в webp, с видео я не хочу грузить сервер необоснованной работой. Пусть просто, если видео не соответствует требованиям, возникало предукпрежение о том, что оно не подходит по формату

Ролики планируются короткие по 5-10 минут максимум типа как на tiktok

-----------------
Файлы, которые тебе могут пригдоиться:

# ./backend/app/core/config.py
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


APP_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = APP_DIR / ".env"


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test_database.db"

    SECRET_KEY: str = "your-super-secret-key-change-in-production-123456789"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    ROLE_SELECTION_TOKEN_EXPIRE_MINUTES: int = 5
    ACTION_TOKEN_EXPIRE_MINUTES: int = 60
    INVITATION_EXPIRE_HOURS: int = 72

    FRONTEND_URL: str = "http://localhost:3000"

    WEBAUTHN_RP_ID: str = "localhost"
    WEBAUTHN_RP_NAME: str = "MentalMe"
    WEBAUTHN_ORIGIN: str = "http://localhost:3000"
    WEBAUTHN_CHALLENGE_EXPIRE_SECONDS: int = 300   


    # EMAIL
    EMAIL_BACKEND:  str = "console"

    SMTP_HOST: str = "smtp.beget.com"
    SMTP_PORT: int = 465
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_USE_SSL: bool = True
    SMTP_USE_STARTTLS: bool = False
    SMTP_TIMEOUT_SECONDS: int = 15

    EMAIL_FROM_ADDRESS: str = "noreply@findmydoc.ru"
    EMAIL_FROM_NAME: str = "FindMyDoc"

    # Локально: backend/media.
    # В Docker переопределяем абсолютным путём.
    MEDIA_ROOT: Path = APP_DIR.parent / "media"

    MEDIA_IMAGE_MAX_BYTES: int = 10 * 1024 * 1024

    # Ограничение исходника до декодирования пикселей.
    MEDIA_IMAGE_MAX_PIXELS: int = 24_000_000

    MEDIA_WEBP_QUALITY: int = 85

    # Несохранённая загрузка доступна для привязки
    # и предпросмотра в течение суток.
    MEDIA_UPLOAD_TTL_HOURS: int = 24

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )




@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

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

    from app.modules.media import models as media_models  # noqa: F401


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


# backend\app\modules\media\access.py

import uuid

from fastapi import HTTPException
from sqlmodel import Session, select

from app.core.security import AuthContext
from app.modules.articles.models import Article
from app.modules.articles.utils import get_article_tag_ids
from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import (
    patient_has_active_assignment,
)
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
    patient_can_access_content,
    patient_can_see_content,
)
from app.modules.media.constants import ImagePurpose
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import (
    Program,
    ProgramStage,
    ProgramStageItem,
    ProgramTagLink,
)
from app.modules.questionnaires.models import Questionnaire
from app.modules.questionnaires.utils import (
    get_questionnaire_tag_ids,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    DoctorProfile,
    User,
)


MANAGER_ROLES = {
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
}

STAFF_ROLES = {
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
    UserRole.DOCTOR,
}


def not_found() -> None:
    raise HTTPException(
        status_code=404,
        detail="Изображение или сущность не найдены",
    )


def get_image_entity(
    *,
    session: Session,
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
):
    if purpose == "doctor":
        user = session.get(User, entity_id)

        if user is None or user.deleted_at is not None:
            not_found()

        entity = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == user.id
            )
        ).first()
    else:
        models = {
            "article": Article,
            "questionnaire": Questionnaire,
            "program": Program,
            "life_aspect": LifeAspect,
        }

        entity = session.get(
            models[purpose],
            entity_id,
        )

    if entity is None:
        not_found()

    return entity


def ensure_can_manage_entity_image(
    *,
    auth: AuthContext,
    purpose: ImagePurpose,
    entity,
) -> None:
    if auth.active_role in MANAGER_ROLES:
        return

    if auth.active_role == UserRole.DOCTOR:
        if (
            purpose == "doctor"
            and entity.user_id == auth.user.id
        ):
            return

        if (
            purpose == "article"
            and entity.created_by_user_id == auth.user.id
        ):
            return

    raise HTTPException(
        status_code=403,
        detail="Нет прав на изменение изображения",
    )


def ensure_program_card_context(
    *,
    session: Session,
    purpose: ImagePurpose,
    content_id: uuid.UUID,
    program_id: uuid.UUID,
    program_stage_id: uuid.UUID | None,
) -> None:
    program = session.get(Program, program_id)

    if program is None or program.is_hidden:
        not_found()

    statement = (
        select(ProgramStageItem.id)
        .join(
            ProgramStage,
            ProgramStage.id == ProgramStageItem.stage_id,
        )
        .where(
            ProgramStage.program_id == program.id,
        )
    )

    if purpose == "article":
        statement = statement.where(
            ProgramStageItem.item_type == ProgramItemType.ARTICLE,
            ProgramStageItem.article_id == content_id,
        )
    elif purpose == "questionnaire":
        statement = statement.where(
            ProgramStageItem.item_type
            == ProgramItemType.QUESTIONNAIRE,
            ProgramStageItem.questionnaire_id == content_id,
        )
    else:
        not_found()

    if program_stage_id is not None:
        statement = statement.where(
            ProgramStage.id == program_stage_id
        )

    if session.exec(statement.limit(1)).first() is None:
        not_found()

    # Здесь намеренно нет проверки покупки программы.
    # Проверяем обложку карточки, а не её Pro-материал.


def patient_can_see_article_card(
    *,
    session: Session,
    patient,
    article: Article,
) -> bool:
    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    # Назначение может показывать материал вне каталога.
    if is_assigned:
        return True

    if article.is_library_hidden:
        return False

    # Используем фактическую настройку вашего каталога,
    # не задавая её повторно и не меняя текущее значение.
    #
    # Импорт внутри функции исключает циклический импорт
    # при загрузке модулей приложения.
    from app.modules.articles.routers import (
        STRICT_PATIENT_ARTICLE_TAG_FILTER,
    )

    if not STRICT_PATIENT_ARTICLE_TAG_FILTER:
        return True

    return patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=get_article_tag_ids(
            session=session,
            article_id=article.id,
        ),
        is_hidden=False,
    )


def patient_can_see_questionnaire_card(
    *,
    session: Session,
    patient,
    questionnaire: Questionnaire,
) -> bool:
    if patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.QUESTIONNAIRE,
        content_id=questionnaire.id,
    ):
        return True

    if questionnaire.is_library_hidden:
        return False

    # Сохраняем текущее правило списка опросников:
    # он сейчас фильтрует карточки через
    # patient_can_access_content().
    #
    # В контексте программы обложка будет доступна
    # независимо от Pro через отдельную ветку выше.
    return patient_can_access_content(
        session=session,
        patient=patient,
        content_tag_ids=get_questionnaire_tag_ids(
            session=session,
            questionnaire_id=questionnaire.id,
        ),
        pro_content=questionnaire.pro_content,
        is_hidden=False,
    )


def patient_can_see_life_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> bool:
    # Пациентский каталог сфер исключает пустые сферы.
    # Повторяем правило наличия хотя бы одной программы
    # через нескрытый тег.
    statement = (
        select(Program.id)
        .join(
            ProgramTagLink,
            ProgramTagLink.program_id == Program.id,
        )
        .join(
            LifeAspectTagLink,
            LifeAspectTagLink.tag_id == ProgramTagLink.tag_id,
        )
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id == aspect.id,
            Tag.is_hidden.is_(False),
            Program.is_hidden.is_(False),
        )
        .limit(1)
    )

    return session.exec(statement).first() is not None


def ensure_can_view_entity_image(
    *,
    session: Session,
    auth: AuthContext,
    purpose: ImagePurpose,
    entity,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    if program_stage_id is not None and program_id is None:
        raise HTTPException(
            status_code=422,
            detail="Для этапа необходимо указать программу",
        )

    if (
        program_id is not None
        and purpose not in {"article", "questionnaire"}
    ):
        raise HTTPException(
            status_code=422,
            detail=(
                "Контекст программы поддерживается "
                "только для статей и опросников"
            ),
        )

    if purpose == "doctor":
        if auth.active_role in MANAGER_ROLES:
            return

        if (
            auth.active_role == UserRole.DOCTOR
            and entity.user_id == auth.user.id
        ):
            return

        not_found()

    if purpose == "life_aspect":
        if auth.active_role in MANAGER_ROLES:
            return
    elif auth.active_role in STAFF_ROLES:
        return

    # Доступ родственников здесь пока не расширяем.
    # Для него потребуется отдельное правило просмотра.
    if auth.active_role != UserRole.PATIENT:
        not_found()

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    if entity.is_hidden:
        not_found()

    if purpose in {"article", "questionnaire"}:
        if program_id is not None:
            ensure_program_card_context(
                session=session,
                purpose=purpose,
                content_id=entity.id,
                program_id=program_id,
                program_stage_id=program_stage_id,
            )
            return

        if purpose == "article":
            allowed = patient_can_see_article_card(
                session=session,
                patient=patient,
                article=entity,
            )
        else:
            allowed = patient_can_see_questionnaire_card(
                session=session,
                patient=patient,
                questionnaire=entity,
            )

        if allowed:
            return

        not_found()

    if purpose == "program":
        # Ваш пациентский API показывает все
        # нескрытые программы независимо от тегов.
        return

    if purpose == "life_aspect":
        if patient_can_see_life_aspect(
            session=session,
            aspect=entity,
        ):
            return

        not_found()

    not_found()

# backend\app\modules\media\constants.py

from dataclasses import dataclass
from typing import Literal


ImagePurpose = Literal[
    "doctor",
    "article",
    "questionnaire",
    "program",
    "life_aspect",
]


@dataclass(frozen=True)
class ImagePreset:
    ratio_width: int
    ratio_height: int
    max_width: int
    max_height: int


IMAGE_PRESETS: dict[str, ImagePreset] = {
    "doctor": ImagePreset(
        ratio_width=1,
        ratio_height=1,
        max_width=512,
        max_height=512,
    ),
    "article": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "questionnaire": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "program": ImagePreset(
        ratio_width=16,
        ratio_height=9,
        max_width=1600,
        max_height=900,
    ),
    "life_aspect": ImagePreset(
        ratio_width=3,
        ratio_height=1,
        max_width=1800,
        max_height=600,
    ),
}

# backend\app\modules\media\image_routers.py

import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import update
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import AuthContext, get_current_auth
from app.modules.media.access import (
    ensure_can_manage_entity_image,
    ensure_can_view_entity_image,
    get_image_entity,
)
from app.modules.media.constants import ImagePurpose
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.schemas import (
    EntityImageResponse,
    EntityImageUpdateRequest,
)
from app.modules.media.service import set_entity_image
from app.modules.media.storage import image_path


router = APIRouter(
    prefix="/api/v1/media/images",
    tags=["Media: entity images"],
)


def serialize_entity_image(
    *,
    session: Session,
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    entity,
) -> EntityImageResponse:
    image = (
        session.get(MediaImage, entity.image_id)
        if entity.image_id is not None
        else None
    )

    if entity.image_id is not None and image is None:
        raise HTTPException(
            status_code=409,
            detail="Нарушена связь с изображением",
        )

    return EntityImageResponse(
        purpose=purpose,
        entity_id=entity_id,
        image_id=image.id if image else None,
        width=image.width if image else None,
        height=image.height if image else None,
        size_bytes=image.size_bytes if image else None,
        file_path=(
            f"/api/v1/media/images/{purpose}/{entity_id}/file"
            f"?image_id={image.id}"
            if image is not None
            else None
        ),
    )


@router.get(
    "/{purpose}/{entity_id}",
    response_model=EntityImageResponse,
)
def get_entity_image(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EntityImageResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_view_entity_image(
        session=session,
        auth=auth,
        purpose=purpose,
        entity=entity,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    return serialize_entity_image(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
        entity=entity,
    )


@router.patch(
    "/{purpose}/{entity_id}",
    response_model=EntityImageResponse,
)
def update_entity_image(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    payload: EntityImageUpdateRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> EntityImageResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_manage_entity_image(
        auth=auth,
        purpose=purpose,
        entity=entity,
    )

    try:
        # Блокируем изменение этой сущности.
        #
        # UPDATE вместо SELECT FOR UPDATE:
        # работает и в PostgreSQL, и в SQLite.
        model = type(entity)

        session.execute(
            update(model)
            .where(model.id == entity.id)
            .values(image_id=model.image_id)
            .execution_options(synchronize_session=False)
        )

        session.refresh(entity)

        # Повторяем проверку на актуальных данных.
        ensure_can_manage_entity_image(
            auth=auth,
            purpose=purpose,
            entity=entity,
        )

        if entity.image_id != payload.expected_image_id:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Изображение уже изменено другим запросом. "
                    "Обновите данные и повторите действие."
                ),
            )

        if entity.image_id != payload.image_id:
            set_entity_image(
                session=session,
                entity=entity,
                purpose=purpose,
                image_id=payload.image_id,
                uploaded_by_user_id=auth.user.id,
            )

            if hasattr(entity, "updated_at"):
                entity.updated_at = utc_now_naive()

            session.add(entity)

        session.commit()
        session.refresh(entity)

    except Exception:
        session.rollback()
        raise

    return serialize_entity_image(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
        entity=entity,
    )


@router.get(
    "/{purpose}/{entity_id}/file",
    response_class=FileResponse,
)
def get_entity_image_file(
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
    image_id: uuid.UUID | None = None,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> FileResponse:
    entity = get_image_entity(
        session=session,
        purpose=purpose,
        entity_id=entity_id,
    )

    ensure_can_view_entity_image(
        session=session,
        auth=auth,
        purpose=purpose,
        entity=entity,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    if entity.image_id is None:
        raise HTTPException(
            status_code=404,
            detail="Изображение не добавлено",
        )

    # Если frontend запросил старую версию картинки,
    # не подменяем её молча новой.
    if (
        image_id is not None
        and image_id != entity.image_id
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение уже изменено",
        )

    image = session.get(
        MediaImage,
        entity.image_id,
    )

    if (
        image is None
        or image.purpose != purpose
        or not image.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение не найдено",
        )

    path = image_path(image.id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл изображения не найден",
        )

    return FileResponse(
        path=path,
        media_type="image/webp",
        headers={
            "Cache-Control": "private, no-store",
            "Vary": "Authorization",
            "X-Content-Type-Options": "nosniff",
            "Content-Disposition": "inline",
        },
    )

# backend\app\modules\media\models.py

import uuid
from datetime import datetime, timezone

from sqlalchemy import CheckConstraint
from sqlmodel import Field, SQLModel


def utc_now_naive() -> datetime:
    # В этой таблице храним UTC без timezone,
    # одинаково для SQLite и PostgreSQL.
    return datetime.now(timezone.utc).replace(
        tzinfo=None,
    )


class MediaImage(SQLModel, table=True):
    __tablename__ = "media_images"

    __table_args__ = (
        CheckConstraint(
            "width > 0 AND height > 0",
            name="ck_media_images_dimensions",
        ),
        CheckConstraint(
            "size_bytes > 0",
            name="ck_media_images_size",
        ),
        CheckConstraint(
            "purpose IN ("
            "'doctor', "
            "'article', "
            "'questionnaire', "
            "'program', "
            "'life_aspect'"
            ")",
            name="ck_media_images_purpose",
        ),
    )

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
    )

    # Строка, а не PostgreSQL ENUM:
    # проще расширять и поддерживать SQLite.
    purpose: str = Field(max_length=32)

    uploaded_by_user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    width: int
    height: int
    size_bytes: int

    is_attached: bool = Field(
        default=False,
        index=True,
    )

    created_at: datetime = Field(
        default_factory=utc_now_naive,
        index=True,
    )

# backend\app\modules\media\processing.py

import io
from dataclasses import dataclass

from PIL import (
    Image,
    ImageOps,
    UnidentifiedImageError,
)

from app.core.config import settings
from app.modules.media.constants import ImagePreset


ALLOWED_IMAGE_FORMATS = {
    "JPEG",
    "PNG",
    "WEBP",
}


class ImageProcessingError(ValueError):
    pass


@dataclass(frozen=True)
class CropRectangle:
    left: int
    top: int
    width: int
    height: int


@dataclass(frozen=True)
class ProcessedImage:
    data: bytes
    width: int
    height: int


def validate_source(image: Image.Image) -> None:
    if image.format not in ALLOWED_IMAGE_FORMATS:
        raise ImageProcessingError(
            "Поддерживаются только JPEG, PNG и WebP"
        )

    width, height = image.size

    if width <= 0 or height <= 0:
        raise ImageProcessingError(
            "Некорректный размер изображения"
        )

    if width * height > settings.MEDIA_IMAGE_MAX_PIXELS:
        raise ImageProcessingError(
            "Слишком большое разрешение изображения"
        )

    if getattr(image, "n_frames", 1) != 1:
        raise ImageProcessingError(
            "Анимированные изображения не поддерживаются"
        )


def validate_crop(
    *,
    image: Image.Image,
    crop: CropRectangle,
    preset: ImagePreset,
) -> None:
    if (
        crop.left < 0
        or crop.top < 0
        or crop.width <= 0
        or crop.height <= 0
    ):
        raise ImageProcessingError(
            "Некорректная область обрезки"
        )

    if (
        crop.left + crop.width > image.width
        or crop.top + crop.height > image.height
    ):
        raise ImageProcessingError(
            "Область обрезки выходит за границы изображения"
        )

    # Допускаем округление координат кроппера
    # примерно на один пиксель.
    difference = abs(
        crop.width * preset.ratio_height
        - crop.height * preset.ratio_width
    )

    tolerance = max(
        preset.ratio_width,
        preset.ratio_height,
    )

    if difference > tolerance:
        raise ImageProcessingError(
            "Область обрезки имеет неверные пропорции"
        )


def process_image(
    *,
    source: bytes,
    crop: CropRectangle,
    preset: ImagePreset,
) -> ProcessedImage:
    if not source:
        raise ImageProcessingError(
            "Загружен пустой файл"
        )

    if len(source) > settings.MEDIA_IMAGE_MAX_BYTES:
        raise ImageProcessingError(
            "Файл превышает допустимый размер"
        )

    try:
        # Сначала проверяем формат и структуру.
        with Image.open(io.BytesIO(source)) as probe:
            validate_source(probe)
            probe.verify()

        # После verify файл требуется открыть заново.
        with Image.open(io.BytesIO(source)) as original:
            validate_source(original)
            original.load()

            oriented = ImageOps.exif_transpose(original)

            try:
                validate_crop(
                    image=oriented,
                    crop=crop,
                    preset=preset,
                )

                cropped = oriented.crop(
                    (
                        crop.left,
                        crop.top,
                        crop.left + crop.width,
                        crop.top + crop.height,
                    )
                )

                try:
                    has_alpha = (
                        "A" in cropped.getbands()
                        or "transparency" in cropped.info
                    )

                    converted = cropped.convert(
                        "RGBA" if has_alpha else "RGB"
                    )

                    try:
                        # thumbnail уменьшает большие изображения,
                        # но не увеличивает маленькие.
                        converted.thumbnail(
                            (
                                preset.max_width,
                                preset.max_height,
                            ),
                            Image.Resampling.LANCZOS,
                        )

                        # Не переносим EXIF, комментарии
                        # и прочие метаданные исходника.
                        converted.info.clear()

                        output = io.BytesIO()

                        converted.save(
                            output,
                            format="WEBP",
                            quality=settings.MEDIA_WEBP_QUALITY,
                            method=4,
                            exif=b"",
                        )

                        return ProcessedImage(
                            data=output.getvalue(),
                            width=converted.width,
                            height=converted.height,
                        )
                    finally:
                        converted.close()
                finally:
                    cropped.close()
            finally:
                if oriented is not original:
                    oriented.close()

    except ImageProcessingError:
        raise
    except (
        UnidentifiedImageError,
        Image.DecompressionBombError,
        OSError,
        ValueError,
        SyntaxError,
        EOFError,
    ) as error:
        raise ImageProcessingError(
            "Не удалось прочитать изображение. "
            "Файл повреждён или имеет неподдерживаемый формат."
        ) from error

# backend\app\modules\media\routers.py

import logging
import uuid
from datetime import timedelta

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from sqlmodel import Session

from app.core.config import settings
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    get_current_auth,
    require_roles,
)
from app.modules.media.constants import (
    IMAGE_PRESETS,
    ImagePurpose,
)
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.processing import (
    CropRectangle,
    ImageProcessingError,
    process_image,
)
from app.modules.media.schemas import (
    MediaImageUploadResponse,
)
from app.modules.media.storage import (
    image_path,
    write_image,
)
from app.modules.users.enums import UserRole


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/media",
    tags=["Media"],
)


def ensure_upload_permission(
    *,
    auth: AuthContext,
    purpose: ImagePurpose,
) -> None:
    if auth.active_role in {
        UserRole.SUPERUSER,
        UserRole.MED_ASSISTANT,
    }:
        return

    if (
        auth.active_role == UserRole.DOCTOR
        and purpose in {"doctor", "article"}
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Нет прав на загрузку этого изображения",
    )


def get_owned_temporary_image(
    *,
    session: Session,
    image_id: uuid.UUID,
    auth: AuthContext,
) -> MediaImage:
    image = session.get(MediaImage, image_id)

    # Возвращаем одинаковый ответ для чужого,
    # отсутствующего и уже привязанного изображения.
    if (
        image is None
        or image.uploaded_by_user_id != auth.user.id
        or image.is_attached
    ):
        raise HTTPException(
            status_code=404,
            detail="Изображение не найдено",
        )

    ensure_upload_permission(
        auth=auth,
        purpose=image.purpose,
    )

    expires_at = image.created_at + timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    if expires_at <= utc_now_naive():
        raise HTTPException(
            status_code=410,
            detail=(
                "Срок временной загрузки истёк. "
                "Загрузите изображение повторно."
            ),
        )

    return image


@router.post(
    "/uploads",
    response_model=MediaImageUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_image(
    purpose: ImagePurpose = Form(...),
    crop_left: int = Form(..., ge=0),
    crop_top: int = Form(..., ge=0),
    crop_width: int = Form(..., gt=0),
    crop_height: int = Form(..., gt=0),
    file: UploadFile = File(...),
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> MediaImageUploadResponse:
    ensure_upload_permission(
        auth=auth,
        purpose=purpose,
    )

    try:
        # Читаем не больше лимита плюс один байт.
        source = file.file.read(
            settings.MEDIA_IMAGE_MAX_BYTES + 1
        )
    finally:
        file.file.close()

    if len(source) > settings.MEDIA_IMAGE_MAX_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_CONTENT_TOO_LARGE,
            detail="Размер изображения превышает 10 МБ",
        )

    try:
        processed = process_image(
            source=source,
            crop=CropRectangle(
                left=crop_left,
                top=crop_top,
                width=crop_width,
                height=crop_height,
            ),
            preset=IMAGE_PRESETS[purpose],
        )
    except ImageProcessingError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error

    image = MediaImage(
        purpose=purpose,
        uploaded_by_user_id=auth.user.id,
        width=processed.width,
        height=processed.height,
        size_bytes=len(processed.data),
    )

    try:
        write_image(
            image_id=image.id,
            data=processed.data,
        )
    except OSError as error:
        logger.exception(
            "Cannot write media image %s",
            image.id,
        )

        raise HTTPException(
            status_code=503,
            detail="Хранилище изображений временно недоступно",
        ) from error

    try:
        session.add(image)
        session.commit()
    except Exception:
        session.rollback()

        # Не удаляем файл немедленно:
        # при потере соединения во время commit
        # результат транзакции может быть неопределённым.
        #
        # Файлы без записи в БД заберёт безопасная
        # фоновая очистка с периодом ожидания.
        logger.exception(
            "Cannot save media metadata for %s",
            image.id,
        )
        raise

    return MediaImageUploadResponse(
        id=image.id,
        purpose=image.purpose,
        width=image.width,
        height=image.height,
        size_bytes=image.size_bytes,
        created_at=image.created_at,
        preview_path=(
            f"/api/v1/media/uploads/{image.id}/preview"
        ),
    )


@router.get(
    "/uploads/{image_id}/preview",
    response_class=FileResponse,
)
def preview_uploaded_image(
    image_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> FileResponse:
    image = get_owned_temporary_image(
        session=session,
        image_id=image_id,
        auth=auth,
    )

    path = image_path(image.id)

    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Файл изображения не найден",
        )

    return FileResponse(
        path=path,
        media_type="image/webp",
        headers={
            "Cache-Control": "private, no-store",
            "Vary": "Authorization",
            "X-Content-Type-Options": "nosniff",
            "Content-Disposition": "inline",
        },
    )

# backend\app\modules\media\schemas.py

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.media.constants import ImagePurpose


class MediaImageUploadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    purpose: ImagePurpose

    width: int
    height: int
    size_bytes: int

    created_at: datetime

    # Только закрытый API, не путь на диске.
    preview_path: str

class EntityImageUpdateRequest(BaseModel):
    # Обязательное поле. null означает удалить обложку.
    image_id: uuid.UUID | None

    # Изображение, которое пользователь видел,
    # когда открыл редактор.
    #
    # Защищает от незаметной перезаписи изменения,
    # сделанного другим сотрудником.
    expected_image_id: uuid.UUID | None


class EntityImageResponse(BaseModel):
    purpose: ImagePurpose
    entity_id: uuid.UUID

    image_id: uuid.UUID | None
    width: int | None
    height: int | None
    size_bytes: int | None

    file_path: str | None

# backend\app\modules\media\service.py

import uuid
from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy import update
from sqlmodel import Session

from app.core.config import settings
from app.modules.media.constants import ImagePurpose
from app.modules.media.models import (
    MediaImage,
    utc_now_naive,
)
from app.modules.media.storage import image_path
from app.modules.questionnaires.models import Questionnaire


def ensure_image_file_exists(image_id: uuid.UUID) -> None:
    if not image_path(image_id).is_file():
        raise HTTPException(
            status_code=409,
            detail=(
                "Файл изображения отсутствует. "
                "Загрузите изображение повторно."
            ),
        )


def set_entity_image(
    *,
    session: Session,
    entity,
    purpose: ImagePurpose,
    image_id: uuid.UUID | None,
    uploaded_by_user_id: uuid.UUID,
) -> None:
    current_image_id = entity.image_id

    # Сохранение формы без изменения изображения.
    if image_id == current_image_id:
        return

    # Только отвязываем. Сам файл здесь не удаляем.
    if image_id is None:
        entity.image_id = None
        session.add(entity)
        return

    ensure_image_file_exists(image_id)

    oldest_allowed = utc_now_naive() - timedelta(
        hours=settings.MEDIA_UPLOAD_TTL_HOURS,
    )

    # Атомарно забираем временную загрузку.
    #
    # Если два запроса одновременно пытаются использовать
    # один upload, успешно завершится только один.
    result = session.execute(
        update(MediaImage)
        .where(
            MediaImage.id == image_id,
            MediaImage.purpose == purpose,
            MediaImage.uploaded_by_user_id == uploaded_by_user_id,
            MediaImage.is_attached.is_(False),
            MediaImage.created_at > oldest_allowed,
        )
        .values(is_attached=True)
        .execution_options(synchronize_session=False)
    )

    if result.rowcount != 1:
        raise HTTPException(
            status_code=409,
            detail=(
                "Изображение нельзя использовать: "
                "оно принадлежит другому пользователю, "
                "имеет другое назначение, уже использовано "
                "или срок загрузки истёк. "
                "Загрузите изображение повторно."
            ),
        )

    entity.image_id = image_id
    session.add(entity)


def set_questionnaire_creation_image(
    *,
    session: Session,
    questionnaire: Questionnaire,
    requested_image_id: uuid.UUID | None,
    image_was_provided: bool,
    copied_from_id: uuid.UUID | None,
    uploaded_by_user_id: uuid.UUID,
) -> None:
    source = None

    if copied_from_id is not None:
        source = session.get(
            Questionnaire,
            copied_from_id,
        )

        if source is None:
            raise HTTPException(
                status_code=404,
                detail="Исходный опросник не найден",
            )

    # Старый клиент при копировании может не отправлять
    # image_id. В этом случае наследуем обложку.
    if not image_was_provided:
        requested_image_id = (
            source.image_id if source is not None else None
        )

    # Явный null означает копирование без обложки.
    if requested_image_id is None:
        return

    # Разрешаем совместное использование изображения
    # только через явно указанный исходный опросник.
    if (
        source is not None
        and source.image_id == requested_image_id
    ):
        image = session.get(
            MediaImage,
            requested_image_id,
        )

        if (
            image is None
            or image.purpose != "questionnaire"
            or not image.is_attached
        ):
            raise HTTPException(
                status_code=409,
                detail="Обложка исходного опросника недоступна",
            )

        ensure_image_file_exists(image.id)

        questionnaire.image_id = image.id
        session.add(questionnaire)
        return

    # Пользователь выбрал новую обложку вместо исходной.
    set_entity_image(
        session=session,
        entity=questionnaire,
        purpose="questionnaire",
        image_id=requested_image_id,
        uploaded_by_user_id=uploaded_by_user_id,
    )

# backend\app\modules\media\storage.py

import os
import uuid
from pathlib import Path
from tempfile import NamedTemporaryFile

from app.core.config import settings


def media_root() -> Path:
    configured = Path(settings.MEDIA_ROOT).expanduser()

    if not configured.is_absolute():
        # Такой же принцип, как у относительного
        # пути SQLite: относительно backend.
        backend_dir = Path(__file__).resolve().parents[3]
        configured = backend_dir / configured

    return configured.resolve()


def image_path(image_id: uuid.UUID) -> Path:
    identifier = image_id.hex

    return (
        media_root()
        / "images"
        / identifier[:2]
        / f"{identifier}.webp"
    )


def write_image(
    *,
    image_id: uuid.UUID,
    data: bytes,
) -> Path:
    destination = image_path(image_id)
    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary_path: Path | None = None

    try:
        # Временный файл создаём на той же файловой
        # системе, чтобы os.replace был атомарным.
        with NamedTemporaryFile(
            mode="wb",
            prefix=".upload-",
            suffix=".tmp",
            dir=destination.parent,
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)

            temporary.write(data)
            temporary.flush()
            os.fsync(temporary.fileno())

        os.replace(
            temporary_path,
            destination,
        )

        return destination
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

----
для начала ,задай мне дополнительные вопросы и попроси прислать необходимые файлы кроме тех, которые я тебе отправил












































------------------
Где сейчас работает или будет работать проект? на vps. пока параметры такие: Ubuntu 26.04, 2 Ядра, 2 ГБ оперативки, 30 ГБ NVMe, 1 Гбит/сек, но позже буду переносить на vps компании. технические характеристики сервера там будут не меньше, чем эти

Как запускается приложение? Есть ли Docker, Nginx или другой reverse proxy? запуск идет через docker-compose, github actions

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

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server_tokens off;

client_max_body_size 10m;

server {
    listen 80;
    listen [::]:80;

    server_name
        findmydoc.ru
        www.findmydoc.ru
        staging.findmydoc.ru;

    location ^~ /.well-known/acme-challenge/ {
        root /var/www/certbot;
        default_type text/plain;
        try_files $uri =404;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/findmydoc.ru/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;

    resolver 127.0.0.11 valid=30s ipv6=off;

    location ^~ /api/_nuxt_icon/ {
        set $frontend_upstream frontend-prod;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /api/v1/media/uploads {
        client_max_body_size 12m;

        set $backend_upstream backend-prod;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_read_timeout 120s;
        proxy_send_timeout 120s;
    }

    location /api/ {
        set $backend_upstream backend-prod;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }

    location = /docs {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /openapi.json {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /health/ {
        set $backend_upstream backend-prod;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
    }

    location / {
        set $frontend_upstream frontend-prod;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name www.findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/findmydoc.ru/privkey.pem;

    return 301 https://findmydoc.ru$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name staging.findmydoc.ru;

    ssl_certificate
        /etc/letsencrypt/live/staging.findmydoc.ru/fullchain.pem;
    ssl_certificate_key
        /etc/letsencrypt/live/staging.findmydoc.ru/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    add_header X-Robots-Tag "noindex, nofollow, noarchive" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    resolver 127.0.0.11 valid=30s ipv6=off;

    location ^~ /api/_nuxt_icon/ {
        set $frontend_upstream frontend-staging;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /api/v1/media/uploads {
        client_max_body_size 12m;

        set $backend_upstream backend-staging;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_read_timeout 120s;
        proxy_send_timeout 120s;
    }

    location /api/ {
        set $backend_upstream backend-staging;

        proxy_pass http://$backend_upstream:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;

        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }

    location = /docs {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /openapi.json {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /health/ {
        set $backend_upstream backend-staging;
        proxy_pass http://$backend_upstream:8000;
        proxy_set_header Host $host;
    }

    location / {
        set $frontend_upstream frontend-staging;

        proxy_pass http://$frontend_upstream:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For
            $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}

services:
  postgres:
    image: postgres:17-bookworm
    restart: unless-stopped
    shm_size: 256mb
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      TZ: UTC
      PGTZ: UTC
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - type: bind
        source: ./postgres/init/01-enable-pgcrypto.sql
        target: /docker-entrypoint-initdb.d/01-enable-pgcrypto.sql
        read_only: true
        bind:
          create_host_path: false
    healthcheck:
      test:
        [
          "CMD-SHELL",
          "pg_isready -U \"$${POSTGRES_USER}\" -d \"$${POSTGRES_DB}\""
        ]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 20s
    networks:
      - internal
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  migrate:
    image: ${BACKEND_IMAGE}
    profiles:
      - tools
    restart: "no"
    env_file:
      - ${BACKEND_ENV_FILE}
    environment:
      DATABASE_URL: postgresql+psycopg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
    command:
      - alembic
      - upgrade
      - head
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - internal

  backend:
    image: ${BACKEND_IMAGE}
    restart: unless-stopped
    env_file:
      - ${BACKEND_ENV_FILE}
    environment:
      DATABASE_URL: postgresql+psycopg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
      MEDIA_ROOT: /var/lib/findmydoc/media
    volumes:
      - type: bind
        source: ${MEDIA_HOST_PATH:?MEDIA_HOST_PATH must be set}
        target: /var/lib/findmydoc/media
        bind:
          create_host_path: false
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health/ready', timeout=5)"
        ]
      interval: 15s
      timeout: 7s
      retries: 10
      start_period: 30s
    networks:
      internal:
      proxy:
        aliases:
          - ${BACKEND_NETWORK_ALIAS}
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  frontend:
    image: ${FRONTEND_IMAGE}
    restart: unless-stopped
    env_file:
      - ${FRONTEND_ENV_FILE}
    healthcheck:
      test:
        [
          "CMD",
          "node",
          "-e",
          "fetch('http://127.0.0.1:3000').then(r => { if (!r.ok) process.exit(1) }).catch(() => process.exit(1))"
        ]
      interval: 15s
      timeout: 7s
      retries: 10
      start_period: 30s
    networks:
      proxy:
        aliases:
          - ${FRONTEND_NETWORK_ALIAS}
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  nginx:
    image: nginx:1.28-alpine
    profiles:
      - edge
    restart: unless-stopped
    command:
      - /bin/sh
      - -c
      - |
        while true; do
          sleep 6h
          nginx -s reload || true
        done &
        exec nginx -g 'daemon off;'
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
      - letsencrypt:/etc/letsencrypt:ro
      - certbot_www:/var/www/certbot:ro
    networks:
      - proxy
    logging:
      driver: json-file
      options:
        max-size: 10m
        max-file: "5"

  certbot:
    image: certbot/certbot:latest
    profiles:
      - edge
    restart: unless-stopped
    entrypoint:
      - /bin/sh
    command:
      - -c
      - |
        trap exit TERM
        while true; do
          certbot renew \
            --webroot \
            --webroot-path=/var/www/certbot \
            --quiet
          sleep 12h &
          wait $${!}
        done
    volumes:
      - letsencrypt:/etc/letsencrypt
      - certbot_www:/var/www/certbot
    networks:
      - proxy

volumes:
  postgres_data:

  letsencrypt:
    name: findmydoc_letsencrypt
    external: true

  certbot_www:
    name: findmydoc_certbot_www
    external: true

networks:
  internal:
    internal: true

  proxy:
    name: findmydoc_proxy
    external: true

Фронтенд и API доступны на одном домене или на разных? - на одном

Сколько примерно планируется: ну, самих видео максимум штук 20, обновлять будем редко. Пользователей... ну не очень много думаю, ОЧЕНЬ максимум 5-10 человек... там размерянный процесс работы будет по шагам. Программа включает в себя шаги, например, программа по снижению веса делится на n этапов, каждый этап содержит шаги - шагом может быть статья/опросник, а теперь еще и видео. 

Можно ли установить на сервер ffprobe и ffmpeg? Они нужны не обязательно для перекодирования: ну, если нужно, то конечно можно

Правильно понимаю: одна карточка видео — один заголовок, общие настройки доступа и максимум два видеофайла? Да, все верно. Форматы - ок
Нужны ли квадратные ролики и другие пропорции? - нет... только два вида

Важное различие: переключатель выбирает назначение файла, а не изменяет сам ролик. Если горизонтальный файл отметить как мобильный, он останется горизонтальным. - да, все верно. При несовпадении пропорций ничего делать не надо, пусть сохраняется

Подойдёт ли такое поведение редактора? - да, все верно

Как выбирать вариант на фронтенде: по ширине области просмотра, а не по определению модели устройства? Я бы предложил именно это. При повороте телефона или изменении размера окна уже начавшееся видео лучше не переключать автоматически, чтобы не прерывать просмотр. Подходит? - да, все подходит

Где ты будешь готовить видео: телефон, монтажная программа, экспорт из другого сервиса? Готов ли перед загрузкой экспортировать по заданному пресету? в специальной программе буду делать, поэтому буду готовить по пресету

длительность до 10 минут - ок
разрешение до 1920×1080 или 1080×1920 - ок
частоту до 30 кадров в секунду - ок

Pro для видео должен работать полностью так же, как для статей? В частности: если у пациента есть доступ к программе, но нет общего Pro-доступа, он сможет посмотреть Pro-видео внутри этой программы? - также, как и со статьями - не сможет, пока не открыт доступ к Pro контенту.. 

«Скрыть из отдельного доступа» означает:
только убрать карточку из вкладки «Видео» - да
или также запретить самостоятельное открытие по прямой ссылке, разрешив просмотр исключительно в доступной пользователю программе? - тут не очень понял... У меня url картинок можно защитить, чтобы их нельзя было открыть по прымому url... Можешь также сделать?

Нужны ли видео:
теги и фильтрация по ним, как у существующего контента - а, ну да... забыл написать
индивидуальные назначения пациенту - хм... да давай пока не будем делать
отдельный флаг полного скрытия, помимо скрытия из библиотеки? - да, надо

Как видео должно засчитываться в прогрессе программы? - хм, хороший вопрос... я об этом не подумал... 
кнопка «Завершить» - да, ок
автоматически после просмотра - да, если это не сильно грузит сервер... Если есть возможность запоминать вообще % просмотра, было бы очень круто... У меня есть функционал Events, может его задействовать?

Нужно ли запоминать позицию и продолжать с неё на другом устройстве? Можно ли свободно перематывать? - не заморачивайся пока над этим

При замене видеофайла уже накопленный прогресс пациентов сохраняется или сбрасывается? А при удалении видео, включённого в программы, нужно запретить удаление и показать список программ? - да, пусть сохраняется. Если видео включено в программу, пусть покажет предупреждение, что оно включено в n программ... но удалить можно... при этом с прогрессом пользователей поступайц как проще... если проще сбросить, сбрасывай

Управление доступно только SUPERUSER и MED_ASSISTANT — верно? Должен ли врач иметь возможность просматривать видео и добавлять существующее видео в программу, если у него есть права на её редактирование? - пока права на редактирование есть только у суперпользхователя и ассистента. у врача пока не делал.

Обложка общая для обоих вариантов или отдельная для каждого? Я бы начал с одной общей обложки для карточки. - одну пока давай

Если обложка не загружена, допустимо извлекать первый кадр один раз после загрузки, а не при каждом открытии? Первый кадр может быть чёрным — можно вместо него брать кадр примерно с первой секунды. Как предпочитаешь? - да, давай с первыой секунды. Разумеется, кадр брать только при первой загрузке

Во вкладке «Видео» нужен обычный каталог с карточками и отдельным проигрывателем или вертикальная лента с автопроигрыванием? Я пока понимаю сравнение с TikTok только как описание роликов, не интерфейса. - да, разумеется, это просто привел как пример. Никаких лент не делаем - просто проигрыватель, когда нажимаю на видео

Оговорка о контроле контента: собственное хранение позволяет управлять доступом и не зависеть от YouTube. Но полностью запретить копирование доступного пользователю видео нельзя — как минимум остаётся запись экрана. - не вопрос



ОБЩИЕ ПРАВИЛА ФРОНТЕНДА:

В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api.

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
















































-----------------------
Важное уточнение: Pro сейчас работает не так, как прозвучало в ответе - делаем как с остальным контентом, то есть, вариант А




