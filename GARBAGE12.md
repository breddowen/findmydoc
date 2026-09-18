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
backend/app/main.py (119 lines)
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

*Files: 163*

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
frontend/app/components/layout/Navbar.vue (405 lines)
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
*Files: 99*

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
frontend/app/pages/users/index.vue (543 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 33*

### utils

```
frontend/app/utils/media.js (98 lines)
```
*Files: 1*

### layouts

```
frontend/app/layouts/auth.vue (28 lines)
frontend/app/layouts/default.vue (22 lines)
frontend/app/layouts/program.vue (40 lines)
```
*Files: 3*

### composables

```
frontend/app/composables/useAppNavigation.js (237 lines)
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
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 20*

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

-------------
deploy\docker-compose.yml

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


.github\workflows\deploy.yml
name: Build and deploy

on:
  push:
    branches:
      - main
      - develop

  workflow_dispatch:

permissions:
  contents: read
  packages: write

concurrency:
  group: findmydoc-vds-deployment
  cancel-in-progress: false

jobs:
  build:
    name: Build and publish images
    runs-on: ubuntu-24.04

    outputs:
      image_prefix: ${{ steps.names.outputs.image_prefix }}
      image_tag: ${{ steps.names.outputs.image_tag }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v5

      - name: Prepare image names
        id: names
        shell: bash
        run: |
          REPOSITORY="$(echo '${{ github.repository }}' | tr '[:upper:]' '[:lower:]')"

          echo "image_prefix=ghcr.io/${REPOSITORY}" >> "$GITHUB_OUTPUT"
          echo "image_tag=${GITHUB_SHA}" >> "$GITHUB_OUTPUT"

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push backend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/backend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-backend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-backend:${{ github.ref_name }}
          cache-from: type=gha,scope=backend
          cache-to: type=gha,mode=max,scope=backend

      - name: Build and push frontend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/frontend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ github.ref_name }}
          cache-from: type=gha,scope=frontend
          cache-to: type=gha,mode=max,scope=frontend

  deploy:
    name: Deploy
    needs:
      - build

    runs-on: ubuntu-24.04

    environment:
      name: ${{ github.ref_name == 'main' && 'production' || 'staging' }}

    steps:
    - name: Checkout repository
      uses: actions/checkout@v5

    - name: Determine target environment
      id: target
      shell: bash
      run: |
        set -euo pipefail

        if [[ "${GITHUB_REF_NAME}" == "main" ]]; then
          echo "name=production" >> "$GITHUB_OUTPUT"
        elif [[ "${GITHUB_REF_NAME}" == "develop" ]]; then
          echo "name=staging" >> "$GITHUB_OUTPUT"
        else
          echo "Unsupported deployment branch: ${GITHUB_REF_NAME}" >&2
          exit 1
        fi

    - name: Validate deployment target
      shell: bash
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
        VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
        VPS_USER: ${{ secrets.VPS_USER }}
      run: |
        set -euo pipefail

        if [[ -z "${VPS_HOST}" ]]; then
          echo "VPS_HOST is empty"
          exit 1
        fi

        if [[ "${VPS_HOST}" == *"@"* ]]; then
          echo "VPS_HOST must contain only an IP address or hostname"
          echo "Do not include deploy@ or root@"
          exit 1
        fi

        if [[ ! "${VPS_PORT}" =~ ^[0-9]+$ ]]; then
          echo "VPS_PORT must be numeric"
          exit 1
        fi

        if [[ "${VPS_USER}" != "deploy" ]]; then
          echo "VPS_USER must be deploy"
          exit 1
        fi

        echo "Deployment target is correct"

    - name: Configure SSH
      shell: bash
      env:
        SSH_PRIVATE_KEY: ${{ secrets.VPS_SSH_PRIVATE_KEY }}
        VPS_KNOWN_HOSTS: ${{ secrets.VPS_KNOWN_HOSTS }}
      run: |
        set -euo pipefail

        mkdir -p ~/.ssh
        chmod 700 ~/.ssh

        printf '%s\n' "$SSH_PRIVATE_KEY" \
          | sed 's/\r$//' \
          > ~/.ssh/id_ed25519
        chmod 600 ~/.ssh/id_ed25519

        printf '%s\n' "$VPS_KNOWN_HOSTS" \
          | sed 's/\r$//' \
          > ~/.ssh/known_hosts
        chmod 600 ~/.ssh/known_hosts

        ssh-keygen -y -f ~/.ssh/id_ed25519 > /tmp/deploy-key.pub

        echo "Private key fingerprint:"
        ssh-keygen -lf /tmp/deploy-key.pub

    - name: Test SSH connection
      shell: bash
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
        VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
        VPS_USER: ${{ secrets.VPS_USER }}
      run: |
        set -euo pipefail

        ssh \
          -i ~/.ssh/id_ed25519 \
          -o IdentitiesOnly=yes \
          -o BatchMode=yes \
          -o PasswordAuthentication=no \
          -o StrictHostKeyChecking=yes \
          -p "${VPS_PORT}" \
          "${VPS_USER}@${VPS_HOST}" \
          'echo "SSH connection successful"; id'

    - name: Upload deployment configuration
      shell: bash
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
        VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
        VPS_USER: ${{ secrets.VPS_USER }}
      run: |
        set -euo pipefail

        rsync \
          --archive \
          --compress \
          --delete \
          -e "ssh \
            -i ~/.ssh/id_ed25519 \
            -o IdentitiesOnly=yes \
            -o BatchMode=yes \
            -o PasswordAuthentication=no \
            -o StrictHostKeyChecking=yes \
            -p ${VPS_PORT}" \
          deploy/ \
          "${VPS_USER}@${VPS_HOST}:/opt/findmydoc/deploy/"

    - name: Run deployment
      shell: bash
      env:
        VPS_HOST: ${{ secrets.VPS_HOST }}
        VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
        VPS_USER: ${{ secrets.VPS_USER }}
        TARGET: ${{ steps.target.outputs.name }}
        IMAGE_PREFIX: ${{ needs.build.outputs.image_prefix }}
        IMAGE_TAG: ${{ needs.build.outputs.image_tag }}
      run: |
        set -euo pipefail

        ssh \
          -i ~/.ssh/id_ed25519 \
          -o IdentitiesOnly=yes \
          -o BatchMode=yes \
          -o PasswordAuthentication=no \
          -o StrictHostKeyChecking=yes \
          -p "${VPS_PORT}" \
          "${VPS_USER}@${VPS_HOST}" \
          "chmod +x /opt/findmydoc/deploy/scripts/*.sh && \
          /opt/findmydoc/deploy/scripts/deploy.sh \
          '${TARGET}' \
          '${IMAGE_PREFIX}' \
          '${IMAGE_TAG}'"

deploy\backend.Dockerfile
FROM python:3.10-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN groupadd --gid 10001 app \
    && useradd \
        --uid 10001 \
        --gid app \
        --create-home \
        --shell /usr/sbin/nologin \
        app

COPY backend/requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip \
    && python -m pip install \
        --requirement /app/requirements.txt

COPY backend/ /app/

RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--proxy-headers", "--forwarded-allow-ips=*"]

deploy\frontend.Dockerfile
FROM node:24.15.0-bookworm-slim AS builder

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm ci --include=dev

COPY frontend/ ./

ENV NODE_ENV=production

RUN npm run build


FROM node:24.15.0-bookworm-slim AS runtime

ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=3000 \
    NITRO_HOST=0.0.0.0 \
    NITRO_PORT=3000

WORKDIR /app

COPY --from=builder --chown=node:node /app/.output ./.output

USER node

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]

deploy\nginx\default.conf
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

deploy\scripts\backup.sh
#!/usr/bin/env bash

set -Eeuo pipefail

TARGET="${1:-production}"

case "$TARGET" in
  production)
    PROJECT="findmydoc-prod"
    ENV_FILE="/opt/findmydoc/production/compose.env"
    ;;
  staging)
    PROJECT="findmydoc-staging"
    ENV_FILE="/opt/findmydoc/staging/compose.env"
    ;;
  *)
    echo "Unknown environment: $TARGET" >&2
    exit 1
    ;;
esac

DEPLOY_DIR="/opt/findmydoc/deploy"
BACKUP_DIR="/opt/findmydoc/backups/${TARGET}"

mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

TIMESTAMP="$(date -u +'%Y-%m-%d_%H-%M-%S')"
BACKUP_FILE="${BACKUP_DIR}/database_${TIMESTAMP}.sql.gz"

cd "$DEPLOY_DIR"

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  exec -T postgres \
  sh -c 'pg_dump \
    --username="$POSTGRES_USER" \
    --dbname="$POSTGRES_DB" \
    --no-owner \
    --no-privileges' \
  | gzip -9 > "$BACKUP_FILE"

chmod 600 "$BACKUP_FILE"

find "$BACKUP_DIR" \
  -type f \
  -name "database_*.sql.gz" \
  -mtime +14 \
  -delete

echo "Backup created: $BACKUP_FILE"

deploy\scripts\deploy.sh
#!/usr/bin/env bash

set -Eeuo pipefail

TARGET="${1:?Environment is required}"
IMAGE_PREFIX="${2:?Image prefix is required}"
IMAGE_TAG="${3:?Image tag is required}"

case "$TARGET" in
  production)
    PROJECT="findmydoc-prod"
    ENV_DIR="/opt/findmydoc/production"
    ;;
  staging)
    PROJECT="findmydoc-staging"
    ENV_DIR="/opt/findmydoc/staging"
    ;;
  *)
    echo "Unknown environment: $TARGET" >&2
    exit 1
    ;;
esac

DEPLOY_DIR="/opt/findmydoc/deploy"
ENV_FILE="${ENV_DIR}/compose.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Environment file does not exist: $ENV_FILE" >&2
  exit 1
fi

exec 9>/tmp/findmydoc-deploy.lock
flock -x 9

set_env_value() {
  local key="$1"
  local value="$2"
  local file="$3"

  if grep -q "^${key}=" "$file"; then
    sed -i "s|^${key}=.*|${key}=${value}|" "$file"
  else
    printf '%s=%s\n' "$key" "$value" >> "$file"
  fi
}

BACKEND_IMAGE="${IMAGE_PREFIX}-backend:${IMAGE_TAG}"
FRONTEND_IMAGE="${IMAGE_PREFIX}-frontend:${IMAGE_TAG}"

set_env_value \
  "BACKEND_IMAGE" \
  "$BACKEND_IMAGE" \
  "$ENV_FILE"

set_env_value \
  "FRONTEND_IMAGE" \
  "$FRONTEND_IMAGE" \
  "$ENV_FILE"

cd "$DEPLOY_DIR"

echo "Pulling images..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  pull postgres backend frontend migrate

echo "Starting PostgreSQL..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  up -d --wait postgres

if docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  ps --status running postgres \
  | grep -q postgres
then
  echo "Creating database backup..."

  if ! "$DEPLOY_DIR/scripts/backup.sh" "$TARGET"; then
    echo "Backup failed; deployment stopped." >&2
    exit 1
  fi
fi

echo "Running database migrations..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  run --rm migrate

echo "Starting application services..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  up -d --wait backend frontend

if [[ "$TARGET" == "production" ]]; then
  if docker run --rm \
    -v findmydoc_letsencrypt:/etc/letsencrypt:ro \
    alpine:3.22 \
    test -f \
    /etc/letsencrypt/live/findmydoc.ru/fullchain.pem
  then
    echo "Starting Nginx and Certbot..."

    docker compose \
      --project-name "$PROJECT" \
      --env-file "$ENV_FILE" \
      --profile edge \
      up -d nginx certbot
  else
    echo "TLS certificates are not initialized yet."
    echo "Run init-letsencrypt.sh after the first deployment."
  fi
fi

echo "Current services:"

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  ps

docker image prune -f

echo "Deployment completed: $TARGET"

deploy\scripts\init-letsencrypt.sh
#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT="findmydoc-prod"
DEPLOY_DIR="/opt/findmydoc/deploy"
ENV_FILE="/opt/findmydoc/production/compose.env"

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <letsencrypt-email>" >&2
  exit 1
fi

LETSENCRYPT_EMAIL="$1"

cd "$DEPLOY_DIR"

if docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt:ro \
  alpine:3.22 \
  test -f /etc/letsencrypt/live/findmydoc.ru/fullchain.pem
then
  echo "Certificates are already initialized."
  exit 0
fi

docker network inspect findmydoc_proxy >/dev/null 2>&1 \
  || docker network create findmydoc_proxy

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  create nginx certbot

echo "Creating certificate directories..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine:3.22 \
  mkdir -p \
  /etc/letsencrypt/live/findmydoc.ru \
  /etc/letsencrypt/live/staging.findmydoc.ru

echo "Creating temporary certificate for findmydoc.ru..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine/openssl \
  req \
  -x509 \
  -nodes \
  -newkey rsa:2048 \
  -days 1 \
  -keyout /etc/letsencrypt/live/findmydoc.ru/privkey.pem \
  -out /etc/letsencrypt/live/findmydoc.ru/fullchain.pem \
  -subj /CN=findmydoc.ru

echo "Creating temporary certificate for staging.findmydoc.ru..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine/openssl \
  req \
  -x509 \
  -nodes \
  -newkey rsa:2048 \
  -days 1 \
  -keyout /etc/letsencrypt/live/staging.findmydoc.ru/privkey.pem \
  -out /etc/letsencrypt/live/staging.findmydoc.ru/fullchain.pem \
  -subj /CN=staging.findmydoc.ru

echo "Starting Nginx with temporary certificates..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  up -d nginx

sleep 5

echo "Removing temporary certificates..."

docker run --rm \
  -v findmydoc_letsencrypt:/etc/letsencrypt \
  alpine:3.22 \
  rm -rf \
  /etc/letsencrypt/live/findmydoc.ru \
  /etc/letsencrypt/archive/findmydoc.ru \
  /etc/letsencrypt/renewal/findmydoc.ru.conf \
  /etc/letsencrypt/live/staging.findmydoc.ru \
  /etc/letsencrypt/archive/staging.findmydoc.ru \
  /etc/letsencrypt/renewal/staging.findmydoc.ru.conf

echo "Requesting production certificate..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  run --rm \
  --entrypoint certbot \
  certbot \
  certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  --email "$LETSENCRYPT_EMAIL" \
  --agree-tos \
  --no-eff-email \
  --cert-name findmydoc.ru \
  -d findmydoc.ru \
  -d www.findmydoc.ru

echo "Requesting staging certificate..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  run --rm \
  --entrypoint certbot \
  certbot \
  certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  --email "$LETSENCRYPT_EMAIL" \
  --agree-tos \
  --no-eff-email \
  --cert-name staging.findmydoc.ru \
  -d staging.findmydoc.ru

echo "Restarting Nginx and starting renewal service..."

docker compose \
  --project-name "$PROJECT" \
  --env-file "$ENV_FILE" \
  --profile edge \
  up -d --force-recreate nginx certbot

echo "Lets Encrypt initialization completed."

backend\requirements.txt
alembic==1.19.1
alembic-postgresql-enum==1.10.0
annotated-doc==0.0.5
annotated-types==0.8.0
anyio==4.14.2
argon2-cffi==25.1.0
argon2-cffi-bindings==26.1.0
cbor2==6.1.4
cffi==2.1.1
click==8.4.2
colorama==0.4.6
cryptography==50.0.0
dnspython==2.8.0
email-validator==2.3.0
exceptiongroup==1.3.1
fastapi==0.141.1
greenlet==3.5.5
h11==0.16.0
httptools==0.8.0
idna==3.19
Mako==1.4.1
MarkupSafe==3.0.3
pillow==12.3.0
psycopg==3.3.4
psycopg-binary==3.3.4
pwdlib==0.3.1
pyasn1==0.6.4
pyasn1_modules==0.4.2
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.15.0
pydantic_core==2.46.4
PyJWT==2.13.0
pyOpenSSL==26.4.0
python-dotenv==1.2.3
python-multipart==0.0.32
PyYAML==6.0.3
SQLAlchemy==2.0.52
sqlmodel==0.0.39
starlette==1.6.0
tomli==2.4.1
typing-inspection==0.4.4
typing_extensions==4.16.0
tzdata==2026.3
uvicorn==0.52.4
watchfiles==1.2.0
webauthn==3.0.0
websockets==16.1.1

# ./backend/app/main.py
from sqlalchemy import text
from sqlmodel import Session

from app.core.db import init_sqlite_db, sqlite_engine

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.db import init_sqlite_db
from app.modules.auth.routers import router as auth_router
from app.modules.consents.routers import router as consents_router
from app.modules.consents.contact_routers import router as assistant_contact_router
from app.modules.events.routers import router as events_router
from app.modules.invitations.routers import router as invitations_router
from app.modules.referrals.routers import router as referrals_router
from app.modules.relationships.routers import router as relationships_router
from app.modules.specialities.routers import router as specialities_router
from app.modules.tags.routers import router as tags_router
from app.modules.tags.life_aspect_routers import router as life_aspects_manage_router
from app.modules.tags.life_aspect_patient_routers import router as life_aspects_patient_router
from app.modules.users.routers import router as users_router
from app.modules.articles.routers import router as articles_router
from app.modules.services.routers import router as services_router
from app.modules.programs.routers import router as programs_router
from app.modules.programs.consultation_routers import router as program_consultations_router
from app.modules.questionnaires.routers import router as questionnaires_router
from app.modules.patients.routers import router as patients_router
from app.modules.assignments.routers import router as assignments_router
from app.modules.notifications.routers import router as notifications_router
from app.modules.invitations.admin_routers import router as admin_invitations_router
from app.modules.media.routers import router as media_router
from app.modules.media.image_routers import router as entity_images_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.DATABASE_URL.startswith("sqlite"):
        init_sqlite_db()

    yield


app = FastAPI(
    title="MentalMe API",
    description=(
        "Backend для клинического маршрута MentalMe."
    ),
    version="0.5.0",
    lifespan=lifespan,
    swagger_ui_parameters={
        "persistAuthorization": True,
        "displayRequestDuration": True,
        "filter": True,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(patients_router)
app.include_router(specialities_router)
app.include_router(invitations_router)
app.include_router(admin_invitations_router)
app.include_router(tags_router)
app.include_router(life_aspects_manage_router)
app.include_router(life_aspects_patient_router)
app.include_router(relationships_router)

app.include_router(referrals_router)
app.include_router(consents_router)
app.include_router(assistant_contact_router)
app.include_router(events_router)

app.include_router(articles_router)
app.include_router(questionnaires_router)
app.include_router(services_router)
app.include_router(programs_router)
app.include_router(program_consultations_router)

app.include_router(assignments_router)
app.include_router(notifications_router)

app.include_router(media_router)
app.include_router(entity_images_router)

@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "name": "MentalMe API",
        "status": "ok",
        "docs": "/docs",
    }


@app.get("/health/live", tags=["System"])
async def liveness_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/health/ready", tags=["System"])
async def readiness_check() -> dict[str, str]:
    with Session(sqlite_engine) as session:
        session.exec(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }

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

----
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
    "@tiptap/core": "3.31.3",
    "@tiptap/extension-link": "3.31.3",
    "@tiptap/extension-placeholder": "3.31.3",
    "@tiptap/extension-underline": "3.31.3",
    "@tiptap/pm": "3.31.3",
    "@tiptap/starter-kit": "3.31.3",
    "@tiptap/vue-3": "3.31.3",
    "daisyui": "^5.7.21",
    "dompurify": "^3.4.14",
    "nuxt": "^4.5.2",
    "pinia": "^4.0.3",
    "qrcode": "^1.5.4",
    "tailwindcss": "^4.3.3",
    "vue": "^3.5.41",
    "vue-advanced-cropper": "^2.8.9",
    "vue-draggable-plus": "^0.6.1",
    "vue-router": "^5.2.0"
  },
  "devDependencies": {
    "@iconify-json/lucide": "^1.2.125"
  },
  "allowScripts": {
    "esbuild@0.28.2": true
  }
}



----------------------------------
Надо написать документацию по проекту для it департамента.

Локально работает sqlite, на vds работает postgres. шифрование пока не сделано, но планируется pgcrypto при необходимости, но надо будет определиться с тем данными, которые в итоге останутся.

Пока что, CI/CD через Github actions, но при необходимости, лучше развернуть gitea

Смотри... это медицинский проект внутри многопрофильной клиники. он сделан для маршрутизации пациентов от одного рпофильного специалиста к другому через выдачу пациенту контента в простой и читаемой форме. 
Я делаю проект своими силами, но уже встал вопрос в интеграцию в клинику. Сегодня на собрании обсуждалось, что врач будет нажимать на кнопку с медицинской информационной системе клиники - ОМИС и пациент будет получать pushup уведомление в мобильном приложении клиники, нажав на котоорое он переходит на мой сервис, который будет интегрирован в мобильное приложение верчех webview. Но сейчас в клинике старое мобильное приложение для пациентов, на новое сделают в началое февраля 2027 года, поэтому, пока новое мобильное приложение не готово, мы сделаем поддомен на emcmos.ru и врач при нажатии на кнопку в ОМИС, пациент будет получать magnet link Для доступа в личный кабинет приложения.

Тут мы соовммещаем 3 сервиса: моё приложение, ОМИС для врача и поддомен на домене клиники. Соответственно, будет активная работа с it департаментом.

Надо описать, как сейчас происходит развертнывание, технические детали работы приложения и другие ньюансы.


Для начала, задай мне вопросы, которые необходимы. Потом надо будет сделать документацию в том виде, в котором обычно такую работу делают, чтобы специалистам было понятно текщуее состояние проекта и задачи

Также, по фронтенду опиши про компоненты, отделно, что стили находятся в одном месте - assets и поэтому переделать стиль приложения под фирменный стиль нкомпании не составит труда, 

Они люди занятые - это топ руководители, поэтому по структуре надо, чтобы в самом начале были описаны самые важные разделы, а ниже - отдельные технические делати. По бекенду, надо описать принцип приложение - модульная структура, подходящая для дальнейшего масштабирования, можешь перечислить модули, доступ к api на этапе демонатрционной версии открыт и он находится на https://findmydoc.ru/docs для основного и https://staging.findmydoc.ru/docs для тестового. Опиши этапновть разработки, ветки на github main и develop, чтобы они понимал, что развертнывание и поддержка также тут учтены. Про бекапы, почтовый клиент можно, но не обязательно, потому что мы планируем интеграцию в мобильное приложение






















----------------------------------

1. Как назвать проект в документе? давай назовем mentalconnect. findmydoc - это просто мой домен, он был нужен, чтобы сделать https

2. Каков фактический статус системы? пока что, была только демонатрция для руководства. Планируется запуск пилота с участием сотрудников с 28 сентября (сейчас 15 сентября, просто я ухожу в отпуск до 28-го, потому мы соберем собрание отделения, распределим роли, кто и какой контект разрабатывает)

Уже есть реальные пациенты и реальные медицинские данные? - пока нет

Какие основные сценарии уже работают полностью, а какие пока только представлены в интерфейсе? работает интерфейс добавления контента, регистрация пациента по ссылке врача, добавление passkey (но рукоодвству passkey не понравился, попросили исключить его ). 

3. Как сформулировать границы назначения сервиса? Ты все правильно понял. В приложении не предполагается наличие медицинских заключений, диагнозов, назначений лечения

4. Как должен выглядеть первый сценарий интеграции с ОМИС?
врач понимает, что пациента надо направить ,например к психитру. Он в карте пациента нажимает кнопку, там выбирает теги пациента, например депрессия, тревога и при нажатии на кнопку (придумай название), пациент получает в личном кабинете pushup уведомление, нажав на которое, он переходит в личный кабинет (пока нет нового приложения, это будет поддомен emcmos.ru)

5. Что вы называете «magnet link»? - да, разумеется magic link 

кто отправляет ссылку: ОМИС, ваше приложение или другой сервис клиники - ну, я думаю, что ОМИС
каким каналом: SMS, email, мобильное приложение - напиши варианты, пусть it решает. в идеале хотелось бы, чтобы это было pushup или смс
должна ли ссылка сразу авторизовать пациента - да, в идеале бесшовно с минимальной когнитивной нагрузкой и задержкой
механизм уже реализован или его ещё предстоит разработать - ну, пока предстоит. и для этого нужная работа со мной и it департаментом. от меня ,видимо, требуется, пока описать, как все работает, чтобы it-шники решили, что с их стороны нужно сделать

Можно ли передавать вашему сервису идентификатор пациента и назначенной программы, а впоследствии возвращать в ОМИС статусы прохождения? yfdthyjt vj;yj

7. Как будет определяться пациент? в моем приложении есть обязательный параметр record_id - это номер карты пациента в ОМИС

# ./backend/app/modules/users/models.py
.....
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

Отдельно: нужно ли поддерживать детей и законных представителей? пока не заморачивайся.
relative - родственники - пока тоже не думай об этом. я ввел эту роль предварительно

РОЛИ:
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

8. Что согласовано по мобильному приложению?
Начало февраля 2027 года — подтверждённый срок или ориентир?  - ну, это ориентир, конечно всякое бывает... но руководитель it департамента говорил уверено

Предполагается ли, что пациент, уже авторизованный в приложении клиники, будет открывать ваш сервис в WebView без повторного входа? надо ,чтобы было так

Есть ли у мобильной команды требования к авторизации, push-уведомлениям и переходам на конкретную программу? - я не знаю... можно вынечти отдельный раздел с вопросами, которые нужны мне для интеграции

9. Где предполагается размещать сервис после интеграции?
Я хотел на внутреннем сервере клиники, но мне на встрече сказали, что это делается на сервере согласованного клиникой провайдера. Мой vds также как и согласованный провайдер - в России

10. Какой поддомен планируется использовать? - не знаю пока... мы пока не решили... пока что, пусть рабочее название будет mentalconnect

Важно уточнить: речь только о подключении доменного имени к текущему VDS или также о переносе приложения в инфраструктуру клиники? - нет, предполагается развертывание на согласованный vds клиники. Сейчас тестовый проект работает на моем личном vds

11. Какие данные действительно нужны сервису? Пишу только те, которые нужны
идентификатор пациента ОМИС;
сведения о враче;
ответы на анкеты - там внеутри приложения опросники
направления, программы и история прохождения;

12. Кто будет отвечать за систему после запуска?
разработка и поддержка - я
серверы, домен и сертификаты - it департамент
интеграцию с ОМИС и мобильным приложением- it департамент
информационную безопасность - это отдельная история. с ними пока встреч не было. им будем делать отдельную документацию
поддержку пользователей и обработку инцидентов - я не знаю... либо it департамент на себя это возьмет, либо я . зависит от того, на каком укровне проблема. Администрирование сервера - это их работа. Работа приложения - моя

Кто принимает решения со стороны клиники и кто будет техническим контактным лицом? смотри... Я врач психитар, который в рамках проекта цифровой психиатрии разработал самостоятельно приложение. Медицинское руководство в лице директора по развитию и заведующего отделения психиатрии поддержало проект. Встреча была со стейкхолдером - операционным директором клиники и руководством it департамента. Я пообещал it департаменту, что пришлю им всю техническую документацию по проекту, чтобы нам разобраться с задачами

13. Какие требования и сроки уже обозначены? - пока никаких, но как можно быстрее. Мне надо, чтобы все запустилось очень быстро. К сожалению, все испортил мой отпуск из-за которого я улетаю до 28 сентября... но потом я всецело буду включен в работу и ъхочется сделать уже к середине октября интеграцию

Есть ли внутренние требования ИБ, обязательное согласование обработки медицинских данных или ограничения на использование GitHub и внешнего хостинга? - я обэтом ничего не знаю... можно вынести в раздел вопросов

14. Подтвердите фактическую конфигурацию VDS.
пока развернуто на beget, скромном сервере: Ubuntu 26.04, CPU 3-3.3 GHz 2 ядра, операц Память 2 гб, NVMe 30 ГБ, Канал 1 Гбит/сек.
Основная и тестовая среды размещены на одном сервере? - да

По конфигурации предполагаются отдельные Compose-проекты и базы PostgreSQL, общая внешняя Docker-сеть и общий Nginx. Так ли это настроено сейчас? Разделены ли каталоги медиафайлов основной и тестовой сред? - я не понял, о чем ты... вроде, все конфиги тебе прислал

15. Как сейчас устроены доступы и хранение кода?
Репозиторий GitHub и образы GHCR конечно все приватное, секреты на гитхабе. Я тебе отправлю все инструкции по развертыванию, которые я себе подготовил для переноса

Gitea рассматривается как пожелание или как требование клиники? При переносе потребуется определить не только размещение Git, но и исполнители CI/CD и реестр Docker-образов. - смотри, это как опция, чтоб мы можэем делать все приватно

16. Какие способы входа уже используются? - все ,что в коде. пока основной способ - jwt
Где frontend хранит токен: вроде, в localstorage. куки не делал

Какие роли доступны и кто может видеть данные конкретного пациента? суперпользователь и медицинский ассистент видят всех, а врач только привязанных к нему пациентов

17. Что уже сделано по безопасности и журналированию? пока ничего. делал в сжатые сроки... планирую все подготовыить, но мне необходимо понимать требования

18. Как реально запускаются резервные копии? тоже пока руки н дошли

19. Как проверяются изменения перед основной средой? смотри в документе внизу

20. Насколько централизовано оформление? у меня брендуков нет. этим будет заниматься отдел маркетинга. Я должен указать, что есть отдельная точка для задания стилей (я специально это сделал в отдельном файле, чтобы было как конструктор)





