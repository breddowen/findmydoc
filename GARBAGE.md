У меня такой проект:

# Project Structure

> Generated: 2026-08-27 22:59

---

## AI Backend

```
backend/alembic/env.py (60 lines)
backend/alembic/README (1 lines)
backend/alembic/script.py.mako (28 lines)
backend/alembic/versions/0d94f719ce10_initial_migration.py (102 lines)
backend/app/.env (14 lines)
backend/app/__init__.py (0 lines)
backend/app/core/__init__.py (0 lines)
backend/app/core/config.py (41 lines)
backend/app/core/db.py (115 lines)
backend/app/core/email.py (27 lines)
backend/app/core/security.py (232 lines)
backend/app/core/websockets/__init__.py (0 lines)
backend/app/core/websockets/manager.py (72 lines)
backend/app/main.py (84 lines)
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
backend/app/modules/invitations/enums.py (15 lines)
backend/app/modules/invitations/models.py (121 lines)
backend/app/modules/invitations/routers.py (957 lines)
backend/app/modules/invitations/schemas.py (143 lines)
backend/app/modules/invitations/utils.py (215 lines)
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
backend/app/modules/referrals/routers.py (463 lines)
backend/app/modules/referrals/schemas.py (83 lines)
backend/app/modules/referrals/utils.py (42 lines)
backend/app/modules/relationships/__init__.py (0 lines)
backend/app/modules/relationships/routers.py (580 lines)
backend/app/modules/relationships/schemas.py (79 lines)
backend/app/modules/specialities/__init__.py (0 lines)
backend/app/modules/specialities/routers.py (191 lines)
backend/app/modules/specialities/schemas.py (44 lines)
backend/app/modules/tags/__init__.py (0 lines)
backend/app/modules/tags/enums.py (7 lines)
backend/app/modules/tags/models.py (124 lines)
backend/app/modules/tags/routers.py (610 lines)
backend/app/modules/tags/schemas.py (73 lines)
backend/app/modules/tags/utils.py (214 lines)
backend/app/modules/users/__init__.py (0 lines)
backend/app/modules/users/enums.py (29 lines)
backend/app/modules/users/models.py (331 lines)
backend/app/modules/users/routers.py (239 lines)
backend/app/modules/users/schemas.py (89 lines)
backend/app/modules/users/utils.py (126 lines)
backend/requirements.txt (39 lines)
backend/seed/data/tags.json (52 lines)
backend/seed/data/users.json (149 lines)
backend/seed/Readme.md (1 lines)
backend/seed/upload_tags.py (123 lines)
backend/seed/upload_users.py (381 lines)
backend/test_database.db (1255 lines)
```

*Files: 108*

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
frontend/app/components/auth/RoleSelector.vue (132 lines)
frontend/app/components/consents/AssistantContact.vue (295 lines)
frontend/app/components/content/RichTextEditor.vue (469 lines)
frontend/app/components/content/RichTextRenderer.vue (136 lines)
frontend/app/components/content/TagSelector.vue (80 lines)
frontend/app/components/invitations/LinkDialog.vue (162 lines)
frontend/app/components/layout/EmailVerificationBanner.vue (87 lines)
frontend/app/components/layout/Footer.vue (48 lines)
frontend/app/components/layout/Navbar.vue (384 lines)
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
frontend/app/components/ui/Modal.vue (150 lines)
frontend/app/components/ui/Pagination.vue (69 lines)
frontend/app/components/ui/ResponsiveDialog.vue (90 lines)
```
*Files: 40*

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
frontend/app/pages/reset-password.vue (122 lines)
frontend/app/pages/settings/security.vue (323 lines)
frontend/app/pages/verify-email.vue (81 lines)
```
*Files: 23*

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
frontend/app/stores/notifications.js (312 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (174 lines)
frontend/app/stores/ui.js (62 lines)
frontend/app/stores/user.js (71 lines)
```
*Files: 9*

### middleware

```
frontend/app/middleware/auth.global.js (39 lines)
frontend/app/middleware/program-manager.js (19 lines)
```
*Files: 2*

### plugins

```
frontend/app/plugins/api.js (63 lines)
```
*Files: 1*

----------

надо подготовыить все для деплоя.

1. Развертывание через docker-compose. пусть там будут сервися бекенда, фронтенда, базы данных postgres, nginx и что ты еще посоветуешь? Деплоить планирую на beget. там есть почтовый сервер (я так понял, STMP)

почта пока такая - в виде заглушки:
# ./backend/app/core/email.py
from app.core.config import settings


def send_console_email(
    *,
    recipient: str,
    subject: str,
    message: str,
    action_path: str | None = None,
    token: str | None = None,
) -> None:
    print()
    print("=" * 80)
    print("📧 EMAIL STUB")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print()
    print(message)

    if action_path and token:
        frontend_url = settings.FRONTEND_URL.rstrip("/")
        print()
        print(f"Link: {frontend_url}{action_path}?token={token}")

    print("=" * 80)
    print()

# ./backend/app/.env
DATABASE_URL=sqlite:///./test_database.db
SECRET_KEY=your-super-secret-key-change-in-production-123456789
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
ROLE_SELECTION_TOKEN_EXPIRE_MINUTES=5
ACTION_TOKEN_EXPIRE_MINUTES=60
INVITATION_EXPIRE_HOURS=72
FRONTEND_URL=http://localhost:3000

WEBAUTHN_RP_ID=localhost
WEBAUTHN_RP_NAME=MentalMe
WEBAUTHN_ORIGIN=http://localhost:3000
WEBAUTHN_CHALLENGE_EXPIRE_SECONDS=300

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

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

# ./frontend/.env
NUXT_PUBLIC_API_BASE=http://localhost:8000
NUXT_PUBLIC_SITE_URL=http://localhost:3000

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
      title: 'MentalMe',
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
          content: 'MentalMe — сервис сопровождения пациентов',
        },
        {
          name: 'theme-color',
          content: '#ffffff',
        },
      ],
    },
  },
})

На локальной машине запускаю не через docker-compose, база данных - sqlite, а на сервере надо, чтобы была postgres. 

2. CI/CD через github actions
3. При деплое, на github registry должны заливаться контейнеры с фронтендом и бекендом, а затем из них уже будут разворачиваться сервисы в docker-compose.

Сделай отдельный каталог: ./deploy/, где будут docker-compose.yml, отдельные Dockerfiles для бекенда и фронтенда (лучше именно в этой директории, чтобы не засорять директории frontend и beckend)

версия npm 12.0.2
Python 3.10.7

Postgres надо под pgcrypto с шифрованием

Если тебе нужны какие-то файлы, попроси прислать

Надо будет описать детально, что и как делать, особенно, как действовать на github и на vds