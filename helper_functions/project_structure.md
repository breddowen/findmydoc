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
