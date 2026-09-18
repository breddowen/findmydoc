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
backend/test_database.db (?)
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


СКОРЕЕ ВСЕГО ПОНАДОБЯТСЯ:

# ./backend/app/core/email.py

import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr

from app.core.config import settings


def build_action_url(
    *,
    action_path: str | None,
    token: str | None,
    action_url: str | None,
) -> str | None:
    if action_url:
        return action_url

    if not action_path:
        return None

    frontend_url = settings.FRONTEND_URL.rstrip("/")
    path = action_path if action_path.startswith("/") else f"/{action_path}"

    result = f"{frontend_url}{path}"

    if token:
        separator = "&" if "?" in result else "?"
        result = f"{result}{separator}token={token}"

    return result


def build_email_body(
    *,
    message: str,
    action_url: str | None,
) -> str:
    parts = [message.strip()]

    if action_url:
        parts.extend([
            "",
            action_url,
        ])

    parts.extend([
        "",
        "Если вы не выполняли это действие, проигнорируйте письмо.",
    ])

    return "\n".join(parts)


def send_console_email(
    *,
    recipient: str,
    subject: str,
    message: str,
    action_path: str | None = None,
    token: str | None = None,
    action_url: str | None = None,
) -> None:
    resolved_action_url = build_action_url(
        action_path=action_path,
        token=token,
        action_url=action_url,
    )

    body = build_email_body(
        message=message,
        action_url=resolved_action_url,
    )

    email_backend = settings.EMAIL_BACKEND.strip().lower()

    if email_backend == "console":
        print()
        print("=" * 80)
        print("EMAIL")
        print(f"Backend: {settings.EMAIL_BACKEND}")
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print()
        print(body)
        print("=" * 80)
        print()
        return

    if email_backend != "smtp":
        raise RuntimeError(
            f"Неизвестный EMAIL_BACKEND: {settings.EMAIL_BACKEND}"
        )

    # if settings.EMAIL_BACKEND.lower() != "smtp":
    #     raise RuntimeError(
    #         f"Неизвестный EMAIL_BACKEND: {settings.EMAIL_BACKEND}"
    #     )

    if not settings.SMTP_USERNAME:
        raise RuntimeError("SMTP_USERNAME не настроен")

    if not settings.SMTP_PASSWORD:
        raise RuntimeError("SMTP_PASSWORD не настроен")

    email = EmailMessage()
    email["From"] = formataddr(
        (
            settings.EMAIL_FROM_NAME,
            settings.EMAIL_FROM_ADDRESS,
        )
    )
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(body)

    ssl_context = ssl.create_default_context()

    if settings.SMTP_USE_SSL:
        with smtplib.SMTP_SSL(
            host=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            timeout=settings.SMTP_TIMEOUT_SECONDS,
            context=ssl_context,
        ) as smtp:
            smtp.login(
                settings.SMTP_USERNAME,
                settings.SMTP_PASSWORD,
            )
            smtp.send_message(email)

        return

    with smtplib.SMTP(
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        timeout=settings.SMTP_TIMEOUT_SECONDS,
    ) as smtp:
        smtp.ehlo()

        if settings.SMTP_USE_STARTTLS:
            smtp.starttls(context=ssl_context)
            smtp.ehlo()

        smtp.login(
            settings.SMTP_USERNAME,
            settings.SMTP_PASSWORD,
        )
        smtp.send_message(email)

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

# ./backend/app/modules/notifications/enums.py
from enum import Enum


class NotificationChannel(str, Enum):
    IN_APP = "in_app"
    EMAIL = "email"
    BROWSER = "browser"


class NotificationType(str, Enum):
    GENERAL = "general"

    PATIENT_REGISTERED = "patient_registered"

    ARTICLE_ASSIGNED = "article_assigned"
    QUESTIONNAIRE_ASSIGNED = "questionnaire_assigned"

    QUESTIONNAIRE_COMPLETED = (
        "questionnaire_completed"
    )

    CONTACT_REQUESTED = "contact_requested"

    PROGRAM_PURCHASE_REQUESTED = (
        "program_purchase_requested"
    )
    PROGRAM_ACCESS_GRANTED = (
        "program_access_granted"
    )

# ./backend/app/modules/notifications/models.py
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, Relationship, SQLModel

from app.modules.notifications.enums import (
    NotificationType,
)
from app.modules.users.models import User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    user_id: uuid.UUID = Field(
        foreign_key="users.id",
        index=True,
    )

    notification_type: NotificationType = Field(
        default=NotificationType.GENERAL,
        index=True,
    )

    title: str = Field(max_length=300)
    message: str

    action_url: Optional[str] = Field(
        default=None,
        max_length=1000,
    )

    payload_json: dict = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )

    channels_json: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON, nullable=False),
    )

    is_read: bool = Field(default=False, index=True)

    created_at: datetime = Field(
        default_factory=utc_now,
        index=True,
    )
    read_at: Optional[datetime] = Field(default=None)

    user: Optional[User] = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "[Notification.user_id]",
        }
    )

# ./backend/app/modules/notifications/schemas.py
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel

from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)


class NotificationResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID

    notification_type: NotificationType

    title: str
    message: str
    action_url: str | None

    payload: dict[str, Any]
    channels: list[NotificationChannel]

    is_read: bool
    created_at: datetime
    read_at: datetime | None


class NotificationPageResponse(BaseModel):
    items: list[NotificationResponse]

    page: int
    page_size: int
    total_items: int
    total_pages: int
    unread_count: int


class UnreadCountResponse(BaseModel):
    unread_count: int


class MarkAllReadResponse(BaseModel):
    updated_count: int

# ./backend/app/modules/notifications/routers.py
import asyncio
import math
import uuid
from datetime import datetime, timezone

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    WebSocket,
    WebSocketDisconnect,
)
from sqlalchemy import func
from sqlmodel import Session, select

from app.core.db import get_session, sqlite_engine
from app.core.security import (
    AuthContext,
    decode_jwt_token,
    ensure_user_can_authenticate,
    get_current_auth,
)
from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
)
from app.modules.notifications.models import Notification
from app.modules.notifications.schemas import (
    MarkAllReadResponse,
    NotificationPageResponse,
    NotificationResponse,
    UnreadCountResponse,
)
from app.modules.users.models import User


router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_response(
    notification: Notification,
) -> NotificationResponse:
    return NotificationResponse(
        id=notification.id,
        user_id=notification.user_id,
        notification_type=notification.notification_type,
        title=notification.title,
        message=notification.message,
        action_url=notification.action_url,
        payload=notification.payload_json,
        channels=[
            NotificationChannel(channel)
            for channel in notification.channels_json
        ],
        is_read=notification.is_read,
        created_at=notification.created_at,
        read_at=notification.read_at,
    )


@router.get("", response_model=NotificationPageResponse)
async def list_notifications(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> NotificationPageResponse:
    total_items = int(
        session.exec(
            select(func.count())
            .select_from(Notification)
            .where(
                Notification.user_id == auth.user.id
            )
        ).one()
    )

    unread_count = int(
        session.exec(
            select(func.count())
            .select_from(Notification)
            .where(
                Notification.user_id == auth.user.id,
                Notification.is_read.is_(False),
            )
        ).one()
    )

    notifications = session.exec(
        select(Notification)
        .where(Notification.user_id == auth.user.id)
        .order_by(Notification.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    ).all()

    return NotificationPageResponse(
        items=[
            serialize_response(item)
            for item in notifications
        ],
        page=page,
        page_size=page_size,
        total_items=total_items,
        total_pages=max(
            1,
            math.ceil(total_items / page_size),
        ),
        unread_count=unread_count,
    )


@router.get(
    "/unread-count",
    response_model=UnreadCountResponse,
)
async def get_unread_count(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> UnreadCountResponse:
    count = session.exec(
        select(func.count())
        .select_from(Notification)
        .where(
            Notification.user_id == auth.user.id,
            Notification.is_read.is_(False),
        )
    ).one()

    return UnreadCountResponse(
        unread_count=int(count)
    )


@router.patch(
    "/read-all",
    response_model=MarkAllReadResponse,
)
async def mark_all_notifications_as_read(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> MarkAllReadResponse:
    notifications = session.exec(
        select(Notification).where(
            Notification.user_id == auth.user.id,
            Notification.is_read.is_(False),
        )
    ).all()

    now = utc_now()

    for notification in notifications:
        notification.is_read = True
        notification.read_at = now
        session.add(notification)

    session.commit()

    return MarkAllReadResponse(
        updated_count=len(notifications)
    )


@router.patch(
    "/{notification_id}/read",
    response_model=NotificationResponse,
)
async def mark_notification_as_read(
    notification_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> NotificationResponse:
    notification = session.get(
        Notification,
        notification_id,
    )

    if (
        not notification
        or notification.user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=404,
            detail="Уведомление не найдено",
        )

    if not notification.is_read:
        notification.is_read = True
        notification.read_at = utc_now()

        session.add(notification)
        session.commit()
        session.refresh(notification)

    return serialize_response(notification)


@router.websocket("/ws")
async def notifications_websocket(
    websocket: WebSocket,
) -> None:
    await websocket.accept()

    user_id: uuid.UUID | None = None

    try:
        authentication_message = await asyncio.wait_for(
            websocket.receive_json(),
            timeout=10,
        )

        if authentication_message.get("type") != "authenticate":
            await websocket.close(code=1008)
            return

        token = authentication_message.get("token")

        if not isinstance(token, str):
            await websocket.close(code=1008)
            return

        payload = decode_jwt_token(
            token,
            expected_type="access",
        )

        user_id = uuid.UUID(payload["sub"])
        token_auth_version = int(
            payload["auth_version"]
        )

        with Session(sqlite_engine) as session:
            user = ensure_user_can_authenticate(
                session.get(User, user_id)
            )

            if user.auth_version != token_auth_version:
                await websocket.close(code=1008)
                return

        await websocket_manager.connect(
            user_id=user_id,
            websocket=websocket,
        )

        await websocket.send_json({
            "type": "authenticated",
        })

        while True:
            message = await websocket.receive_json()

            if message.get("type") == "ping":
                await websocket.send_json({
                    "type": "pong",
                })

    except (
        WebSocketDisconnect,
        asyncio.TimeoutError,
        ValueError,
        KeyError,
    ):
        pass
    except Exception:
        try:
            await websocket.close(code=1011)
        except Exception:
            pass
    finally:
        if user_id:
            websocket_manager.disconnect(
                user_id=user_id,
                websocket=websocket,
            )

# ./backend/app/modules/notifications/service.py
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlmodel import Session

from app.core.email import send_console_email
from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.models import Notification
from app.modules.users.models import User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_notification(
    notification: Notification,
) -> dict[str, Any]:
    return {
        "id": str(notification.id),
        "user_id": str(notification.user_id),
        "notification_type": (
            notification.notification_type.value
        ),
        "title": notification.title,
        "message": notification.message,
        "action_url": notification.action_url,
        "payload": notification.payload_json,
        "channels": notification.channels_json,
        "is_read": notification.is_read,
        "created_at": notification.created_at.isoformat(),
        "read_at": (
            notification.read_at.isoformat()
            if notification.read_at
            else None
        ),
    }


async def send_notification(
    *,
    session: Session,
    user_id: uuid.UUID,
    title: str,
    message: str,
    notification_type: NotificationType = (
        NotificationType.GENERAL
    ),
    channels: list[NotificationChannel] | None = None,
    action_url: str | None = None,
    payload: dict[str, Any] | None = None,
) -> Notification | None:
    """
    ЕДИНАЯ ТОЧКА ОТПРАВКИ УВЕДОМЛЕНИЙ.

    Пример:

        await send_notification(
            session=session,
            user_id=patient_user_id,
            title="Назначен опросник",
            message="Врач назначил вам новый опросник.",
            notification_type=(
                NotificationType.QUESTIONNAIRE_ASSIGNED
            ),
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url="/questionnaires",
        )

    IN_APP:
        уведомление сохраняется в базе и отображается
        в колокольчике.

    EMAIL:
        пока выводится в консоль backend.

    BROWSER:
        отправляется через WebSocket. Системное уведомление
        браузера появится, если пользователь дал разрешение
        и приложение открыто.
    """
    selected_channels = channels or [
        NotificationChannel.IN_APP,
    ]

    user = session.get(User, user_id)

    if not user or user.deleted_at is not None:
        return None

    notification: Notification | None = None

    if NotificationChannel.IN_APP in selected_channels:
        notification = Notification(
            user_id=user.id,
            notification_type=notification_type,
            title=title.strip(),
            message=message.strip(),
            action_url=action_url,
            payload_json=payload or {},
            channels_json=[
                channel.value
                for channel in selected_channels
            ],
        )

        session.add(notification)
        session.commit()
        session.refresh(notification)

    if NotificationChannel.EMAIL in selected_channels:
        send_console_email(
            recipient=user.email,
            subject=title,
            message=message,
        )

    websocket_payload = {
        "type": "notification",
        "notification": (
            serialize_notification(notification)
            if notification
            else {
                "id": str(uuid.uuid4()),
                "user_id": str(user.id),
                "notification_type": (
                    notification_type.value
                ),
                "title": title,
                "message": message,
                "action_url": action_url,
                "payload": payload or {},
                "channels": [
                    channel.value
                    for channel in selected_channels
                ],
                "is_read": False,
                "created_at": utc_now().isoformat(),
                "read_at": None,
            }
        ),
    }

    if (
        NotificationChannel.IN_APP in selected_channels
        or NotificationChannel.BROWSER
        in selected_channels
    ):
        await websocket_manager.send_to_user(
            user_id=user.id,
            message=websocket_payload,
        )

    return notification

# ./backend/app/modules/notifications/transactional.py
import logging
import uuid
from typing import Any

from sqlmodel import Session

from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.models import Notification
from app.modules.notifications.service import serialize_notification


logger = logging.getLogger(__name__)


def create_in_app_notification(
    *,
    session: Session,
    user_id: uuid.UUID,
    title: str,
    message: str,
    notification_type: NotificationType,
    action_url: str | None = None,
    payload: dict[str, Any] | None = None,
) -> Notification:
    """
    Только добавляет уведомление в текущую транзакцию.
    Не делает commit и не выполняет сетевую отправку.
    """
    notification = Notification(
        user_id=user_id,
        notification_type=notification_type,
        title=title.strip(),
        message=message.strip(),
        action_url=action_url,
        payload_json=payload or {},
        channels_json=[
            NotificationChannel.IN_APP.value,
            NotificationChannel.BROWSER.value,
        ],
    )

    session.add(notification)

    return notification


def snapshot_notifications(
    *,
    session: Session,
    notifications: list[Notification],
) -> list[dict[str, Any]]:
    """
    Подготовить данные до commit, пока ошибки сериализации
    ещё могут откатить всю операцию.
    """
    session.flush()

    return [
        serialize_notification(notification)
        for notification in notifications
    ]


async def publish_saved_notifications(
    snapshots: list[dict[str, Any]],
) -> None:
    """
    Вызывать только после успешного commit.

    Сбой WebSocket не отменяет уже сохранённую заявку
    и не превращает успешную операцию в ошибку API.
    """
    for snapshot in snapshots:
        try:
            await websocket_manager.send_to_user(
                user_id=uuid.UUID(snapshot["user_id"]),
                message={
                    "type": "notification",
                    "notification": snapshot,
                },
            )
        except Exception:
            logger.exception(
                "WebSocket delivery failed for notification %s",
                snapshot["id"],
            )

frontend\app\assets\css\main.css
@import "tailwindcss";

@plugin "daisyui" {
  themes: false;
}

@plugin "daisyui/theme" {
  name: "light";
  default: true;
  prefersdark: false;
  color-scheme: light;

  --color-base-100: #fffdfb;
  --color-base-200: #f4f0eb;
  --color-base-300: #e5ddd3;
  --color-base-content: #261d1b;

  --color-primary: #963532;
  --color-primary-content: #ffffff;

  --color-secondary: #c7aa80;
  --color-secondary-content: #2b211c;

  --color-accent: #b77d58;
  --color-accent-content: #ffffff;

  --color-neutral: #493b37;
  --color-neutral-content: #ffffff;

  --color-info: #4e7488;
  --color-info-content: #ffffff;

  --color-success: #54765e;
  --color-success-content: #ffffff;

  --color-warning: #b47b2f;
  --color-warning-content: #ffffff;

  --color-error: #a23c38;
  --color-error-content: #ffffff;

  --radius-selector: 0.375rem;
  --radius-field: 0.375rem;
  --radius-box: 0.75rem;

  --size-selector: 0.25rem;
  --size-field: 0.25rem;

  --border: 1px;
  --depth: 1;
  --noise: 0;
}

@plugin "daisyui/theme" {
  name: "dark";
  default: false;
  prefersdark: true;
  color-scheme: dark;

  --color-base-100: #241e1c;
  --color-base-200: #191514;
  --color-base-300: #382f2c;
  --color-base-content: #f4ede5;

  --color-primary: #d7837d;
  --color-primary-content: #281513;

  --color-secondary: #c9aa7d;
  --color-secondary-content: #241b16;

  --color-accent: #c99069;
  --color-accent-content: #271812;

  --color-neutral: #423735;
  --color-neutral-content: #f7f0e8;

  --color-info: #76a4bc;
  --color-info-content: #10232d;

  --color-success: #82ad8d;
  --color-success-content: #102218;

  --color-warning: #d7a45a;
  --color-warning-content: #2b1d09;

  --color-error: #e47e78;
  --color-error-content: #2c1110;

  --radius-selector: 0.375rem;
  --radius-field: 0.375rem;
  --radius-box: 0.75rem;

  --size-selector: 0.25rem;
  --size-field: 0.25rem;

  --border: 1px;
  --depth: 1;
  --noise: 0;
}

html {
  min-height: 100%;
  background-color: var(--color-base-200);
}

body {
  min-height: 100dvh;
  margin: 0;
  color: var(--color-base-content);
  background-color: var(--color-base-200);
  overscroll-behavior-y: none;
}

#__nuxt {
  min-height: 100dvh;
}

::selection {
  color: var(--color-primary-content);
  background-color: var(--color-primary);
}

button,
a,
input,
select,
textarea {
  -webkit-tap-highlight-color: transparent;
}

.safe-area-bottom {
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}

.safe-area-top {
  padding-top: env(safe-area-inset-top);
}

для широких дисплеев у меня такой компонент модального окна:

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
  persistent: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'close',
  'opened',
])

const opened = computed(() => model.value)

useBodyScrollLock(opened)

function close() {
  if (props.persistent) return

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
              :disabled="persistent"
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

для мобильных устройств:
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
  persistent: {
    type: Boolean,
    default: false,
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
  if (props.persistent) return

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
  if (props.persistent) return

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

watch(
  () => props.persistent,
  (value) => {
    if (!value) return

    dragging.value = false
    translateY.value = 0
  },
)

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
              :disabled="persistent"
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

<!-- ./frontend/app/components/layout/Navbar.vue -->
<script setup>
const auth = useAuthStore()
const userStore = useUserStore()
const ui = useUiStore()
const notifications = useNotificationsStore()

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

const isPatient = computed(() =>
  isClientReady.value
  && auth.activeRole === 'patient',
)

onMounted(() => {
  notifications.connect()

  void notifications.fetchUnreadCount().catch(() => {
    // Ошибка фоновой загрузки не блокирует навигацию.
  })
})

onBeforeUnmount(() => {
  notifications.disconnect()
})
</script>

<template>
  <header
    class="bg-base-100 border-base-300 sticky top-0 z-30 border-b"
  >
    <div
      class="mx-auto grid min-h-16 w-full max-w-7xl items-center gap-2 px-3 py-1 sm:min-h-20 sm:px-4"
      :class="
        isPatient
          ? 'grid-cols-[minmax(0,1fr)_auto]'
          : 'grid-cols-[auto_minmax(0,1fr)_auto]'
      "
    >
      <div class="flex min-w-0 items-center gap-1">
        <template v-if="isPatient">
          <div class="patient-navbar-brand">
            <LayoutLogo
              to="/dashboard"
              variant="navbar"
            />
          </div>

          <LayoutPatientActions
            @menu="mobileMenuOpen = true"
          />
        </template>

        <template v-else>
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
        </template>
      </div>

      <div
        v-if="!isStaff && !isPatient"
        class="hidden min-w-0 items-center justify-center px-2 lg:flex"
      >
        <UiMegaMenu
          :groups="navigationGroups"
          size-class="megamenu-sm"
        />
      </div>

      <div
        v-else-if="isStaff"
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

            <li v-if="isStaff">
              <NotificationsBrowserPermission />
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
<style scoped>
.patient-navbar-brand {
  width: clamp(3rem, 16vw, 5rem);
  min-width: 0;
  flex-shrink: 1;
}

.patient-navbar-brand :deep(a) {
  max-width: 100%;
  min-width: 0;
}

.patient-navbar-brand :deep(svg),
.patient-navbar-brand :deep(img) {
  max-width: 100%;
  height: auto;
}

@media (min-width: 640px) {
  .patient-navbar-brand {
    width: auto;
    max-width: 10rem;
  }
}
</style>

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
          {
            to: '/settings/life-aspects',
            label: 'Сферы жизни',
            icon: 'lucide:heart-pulse',
            description: 'Направления, описания и связанные теги',
          },
        ],
      })
    }

    if (auth.activeRole === 'doctor') {
      groups.push({
        key: 'information',
        label: 'Информация',
        icon: 'lucide:info',
        links: [
          {
            to: '/info/doctor/conversation',
            label: 'Как рассказать пациенту',
            icon: 'lucide:message-circle',
            description: 'Пример объяснения на приёме',
          },
          {
            to: '/info/doctor/about',
            label: 'О приложении для врача',
            icon: 'lucide:book-open',
            description: 'Поддержка пациента между визитами',
          },
        ],
      })
    }

    if (auth.activeRole === 'patient') {
      groups.push({
        key: 'information',
        label: 'Информация',
        icon: 'lucide:info',
        links: [
          {
            to: '/info/patient',
            label: 'Как помогает приложение',
            icon: 'lucide:book-open',
            description: 'Возможности приложения',
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

<script setup>
const route = useRoute()

onMounted(() => {
  void navigateTo(
    {
      path: '/dashboard',
      query: route.query,
      hash: route.hash,
    },
    {
      replace: true,
    },
  )
})
</script>

<template>
  <p
    class="text-base-content/60 py-6 text-center text-sm"
    role="status"
  >
    Открываем главную…
  </p>
</template>

// ./frontend/app/stores/emc-app.js
export const useEmcAppStore = defineStore(
  'emc-app',
  () => {
    const doctors = ref([
      {
        id: 'demo-psychiatrist',
        fullName: 'Мовина Лариса Георгиевна',
        speciality: 'Психиатр',
        initials: 'ЛГ',
        clinic: 'EMC',
        address: 'Щепкина, 35',
        isDemo: true,
      },
      {
        id: 'demo-addiction-specialist',
        fullName: 'Титков Максим Сергеевич',
        speciality: 'Специалист по аддикциям',
        initials: 'МТ',
        clinic: 'EMC',
        address: 'Щепкина, 35',
        isDemo: true,
      },
    ])

    const nearestDays = ref([])

    function refreshDemoDays() {
      const formatter = new Intl.DateTimeFormat(
        'ru-RU',
        {
          day: 'numeric',
          month: 'long',
        },
      )

      const today = new Date()

      nearestDays.value = [1, 2].map(offset => {
        const date = new Date(
          today.getFullYear(),
          today.getMonth(),
          today.getDate() + offset,
          12,
        )

        return {
          id: `demo-day-${offset}`,
          label: offset === 1 ? 'Завтра' : 'Послезавтра',
          dateLabel: formatter.format(date),
        }
      })
    }

    return {
      doctors,
      nearestDays,
      refreshDemoDays,
    }
  },
)

// ./frontend/app/stores/notifications.js
export const useNotificationsStore = defineStore(
  'notifications',
  () => {
    const items = ref([])
    const unreadCount = ref(0)

    const page = ref(1)
    const totalItems = ref(0)
    const totalPages = ref(1)

    const loading = ref(false)
    const connected = ref(false)

    let socket = null
    let reconnectTimer = null
    let pingTimer = null
    let manuallyDisconnected = false
    let assignmentRefreshTimer = null

    let notificationRefreshTimer = null
    let notificationSessionVersion = 0

    const seenNotificationIds = new Set()

    async function fetchNotifications(requestedPage = 1) {
    const { $api } = useNuxtApp()
    const version = notificationSessionVersion

    loading.value = true

    try {
      const response = await $api(
        '/api/v1/notifications',
        {
          query: {
            page: requestedPage,
            page_size: 10,
          },
        },
      )

      if (version !== notificationSessionVersion) {
        return response
      }

      items.value = response.items
      unreadCount.value = response.unread_count
      page.value = response.page
      totalItems.value = response.total_items
      totalPages.value = response.total_pages

      return response
    } finally {
      if (version === notificationSessionVersion) {
        loading.value = false
      }
    }
  }

  async function fetchUnreadCount() {
    const { $api } = useNuxtApp()
    const version = notificationSessionVersion

    const response = await $api(
      '/api/v1/notifications/unread-count',
    )

    if (version === notificationSessionVersion) {
      unreadCount.value = response.unread_count
    }
  }

  function scheduleNotificationsRefresh() {
    window.clearTimeout(notificationRefreshTimer)

    notificationRefreshTimer = window.setTimeout(() => {
      void fetchNotifications(page.value).catch(() => {
        // Уведомление уже сохранено на backend.
        // Не ломаем интерфейс при временной ошибке сети.
      })
    }, 200)
  }
  async function markAsRead(notification) {
        if (notification.is_read) return
  
        const { $api } = useNuxtApp()
  
        const response = await $api(
          `/api/v1/notifications/${notification.id}/read`,
          {
            method: 'PATCH',
          },
        )
  
        const item = items.value.find(
          (current) => current.id === notification.id,
        )
  
        if (item) {
          item.is_read = true
          item.read_at = response.read_at
        }
  
        unreadCount.value = Math.max(
          unreadCount.value - 1,
          0,
        )
      }

    async function markAllAsRead() {
      const { $api } = useNuxtApp()

      await $api(
        '/api/v1/notifications/read-all',
        {
          method: 'PATCH',
        },
      )

      for (const item of items.value) {
        item.is_read = true
      }

      unreadCount.value = 0
    }

    function showBrowserNotification(notification) {
      if (!import.meta.client) return

      if (
        !notification.channels?.includes('browser')
        || !('Notification' in window)
        || Notification.permission !== 'granted'
      ) {
        return
      }

      try {
        const browserNotification = new Notification(
          notification.title,
          {
            body: notification.message,
            tag: notification.id,
            icon: '/favicon.ico',
          },
        )

        browserNotification.onclick = () => {
          window.focus()

          const actionUrl = notification.action_url

          if (
            typeof actionUrl === 'string'
            && actionUrl.startsWith('/')
            && !actionUrl.startsWith('//')
          ) {
            void navigateTo(actionUrl)
          }

          browserNotification.close()
        }
      } catch {
        // Некоторые мобильные браузеры не поддерживают
        // создание Notification без Service Worker.
        // Колокольчик при этом должен продолжать работать.
      }
    }

    function handleSocketMessage(event) {
      let data

      try {
        data = JSON.parse(event.data)
      } catch {
        return
      }

      if (data.type === 'authenticated') {
        connected.value = true
        scheduleNotificationsRefresh()
        return
      }

      if (
        data.type !== 'notification'
        || !data.notification?.id
      ) {
        return
      }

      const notification = data.notification

      if (seenNotificationIds.has(notification.id)) {
        return
      }

      seenNotificationIds.add(notification.id)

      if (seenNotificationIds.size > 1000) {
        const oldestId = seenNotificationIds.values().next().value
        seenNotificationIds.delete(oldestId)
      }

      if (
        [
          'article_assigned',
          'questionnaire_assigned',
        ].includes(notification.notification_type)
      ) {
        scheduleAssignmentsRefresh()
      }

      if (notification.channels?.includes('in_app')) {
        // Счётчики берём с backend, не увеличиваем вслепую:
        // уведомление могло уже попасть в HTTP-ответ.
        scheduleNotificationsRefresh()
      }

      showBrowserNotification(notification)
    }

    function connect() {
      if (!import.meta.client) return

      const token = localStorage.getItem(
        'mentalme_access_token',
      )

      if (!token || socket) return

      manuallyDisconnected = false
      window.clearTimeout(reconnectTimer)

      const config = useRuntimeConfig()

      const websocketUrl = new URL(
        config.public.apiBase,
        window.location.origin,
      )

      websocketUrl.protocol =
        websocketUrl.protocol === 'https:' ? 'wss:' : 'ws:'

      websocketUrl.pathname =
        websocketUrl.pathname.replace(/\/$/, '')
        + '/api/v1/notifications/ws'

      websocketUrl.search = ''
      websocketUrl.hash = ''

      const currentSocket = new WebSocket(
        websocketUrl.toString(),
      )

      socket = currentSocket

      currentSocket.addEventListener('open', () => {
        if (socket !== currentSocket) return

        currentSocket.send(
          JSON.stringify({
            type: 'authenticate',
            token,
          }),
        )

        window.clearInterval(pingTimer)

        pingTimer = window.setInterval(() => {
          if (
            socket === currentSocket
            && currentSocket.readyState === WebSocket.OPEN
          ) {
            currentSocket.send(
              JSON.stringify({ type: 'ping' }),
            )
          }
        }, 30000)
      })

      currentSocket.addEventListener('message', (event) => {
        if (socket === currentSocket) {
          handleSocketMessage(event)
        }
      })

      currentSocket.addEventListener('close', () => {
        if (socket !== currentSocket) return

        connected.value = false
        socket = null

        window.clearInterval(pingTimer)

        if (!manuallyDisconnected) {
          reconnectTimer = window.setTimeout(connect, 3000)
        }
      })
    }

    function disconnect() {
      if (!import.meta.client) return

      manuallyDisconnected = true
      notificationSessionVersion += 1

      window.clearTimeout(reconnectTimer)
      window.clearInterval(pingTimer)
      window.clearTimeout(assignmentRefreshTimer)
      window.clearTimeout(notificationRefreshTimer)

      const previousSocket = socket
      socket = null

      previousSocket?.close()

      connected.value = false
      loading.value = false

      items.value = []
      unreadCount.value = 0
      page.value = 1
      totalItems.value = 0
      totalPages.value = 1

      seenNotificationIds.clear()
    }

    async function requestBrowserPermission() {
      if (
        !import.meta.client
        || !window.isSecureContext
        || !('Notification' in window)
      ) {
        return 'unsupported'
      }

      return await Notification.requestPermission()
    }

    function scheduleAssignmentsRefresh() {
        const auth = useAuthStore()

        if (auth.activeRole !== 'patient') {
            return
        }

        window.clearTimeout(assignmentRefreshTimer)

        assignmentRefreshTimer = window.setTimeout(
            async () => {
            try {
                const assignmentsStore =
                useAssignmentsStore()

                await assignmentsStore.fetchMyAssignments()
            } catch {
                // Ошибка фонового обновления не должна
                // прерывать обработку уведомлений.
            }
            },
            150,
        )
        }

    return {
      items,
      unreadCount,
      page,
      totalItems,
      totalPages,
      loading,
      connected,

      fetchNotifications,
      fetchUnreadCount,
      markAsRead,
      markAllAsRead,

      connect,
      disconnect,
      requestBrowserPermission,
    }
  },
)

// ./frontend/app/stores/ui.js
export const useUiStore = defineStore('ui', () => {
  const theme = ref('light')
  const initialized = ref(false)

  const sidebarInitialized = ref(false)
  const isDesktopViewport = ref(false)

  // Сохраняем только предпочтение для компьютера.
  const desktopSidebarOpen = ref(false)

  // Мобильное состояние всегда временное.
  const mobileSidebarOpen = ref(false)

  let desktopMediaQuery = null

  const isDark = computed(
    () => theme.value === 'dark',
  )

  const sidebarOpen = computed({
    get() {
      return isDesktopViewport.value
        ? desktopSidebarOpen.value
        : mobileSidebarOpen.value
    },

    set(value) {
      setSidebarOpen(value)
    },
  })

  function applyTheme() {
    if (!import.meta.client) return

    document.documentElement.setAttribute(
      'data-theme',
      theme.value,
    )

    const themeColor = theme.value === 'dark'
      ? '#191514'
      : '#f4f0eb'

    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute('content', themeColor)
  }

  function initTheme() {
    if (!import.meta.client || initialized.value) {
      return
    }

    const storedTheme = localStorage.getItem(
      'mentalme_theme',
    )

    if (
      storedTheme === 'light'
      || storedTheme === 'dark'
    ) {
      theme.value = storedTheme
    } else {
      const prefersDark = window.matchMedia(
        '(prefers-color-scheme: dark)',
      ).matches

      theme.value = prefersDark
        ? 'dark'
        : 'light'
    }

    applyTheme()
    initialized.value = true
  }

  function setTheme(value) {
    if (
      value !== 'light'
      && value !== 'dark'
    ) {
      return
    }

    theme.value = value

    if (import.meta.client) {
      localStorage.setItem(
        'mentalme_theme',
        value,
      )
    }

    applyTheme()
  }

  function toggleTheme() {
    setTheme(
      isDark.value ? 'light' : 'dark',
    )
  }

  function persistDesktopSidebar() {
    if (!import.meta.client) return

    localStorage.setItem(
      'mentalme_sidebar_open',
      desktopSidebarOpen.value
        ? '1'
        : '0',
    )
  }

  function handleViewportChange(event) {
    isDesktopViewport.value = event.matches

    // Мобильное меню никогда не открывается
    // автоматически при изменении ширины окна.
    mobileSidebarOpen.value = false
  }

  function initSidebar() {
    if (
      !import.meta.client
      || sidebarInitialized.value
    ) {
      return
    }

    desktopMediaQuery = window.matchMedia(
      '(min-width: 1024px)',
    )

    isDesktopViewport.value =
      desktopMediaQuery.matches

    desktopSidebarOpen.value =
      localStorage.getItem(
        'mentalme_sidebar_open',
      ) === '1'

    // На телефоне sidebar после перезагрузки закрыт,
    // независимо от desktop-предпочтения.
    mobileSidebarOpen.value = false

    desktopMediaQuery.addEventListener(
      'change',
      handleViewportChange,
    )

    sidebarInitialized.value = true
  }

  function setSidebarOpen(value) {
    const normalized = Boolean(value)

    if (isDesktopViewport.value) {
      desktopSidebarOpen.value = normalized
      persistDesktopSidebar()
      return
    }

    mobileSidebarOpen.value = normalized
  }

  function openSidebar() {
    setSidebarOpen(true)
  }

  function closeSidebar() {
    setSidebarOpen(false)
  }

  function closeMobileSidebar() {
    mobileSidebarOpen.value = false
  }

  function toggleSidebar() {
    setSidebarOpen(!sidebarOpen.value)
  }

  return {
    theme,
    initialized,
    isDark,

    sidebarInitialized,
    isDesktopViewport,
    sidebarOpen,

    initTheme,
    setTheme,
    toggleTheme,

    initSidebar,
    setSidebarOpen,
    openSidebar,
    closeSidebar,
    closeMobileSidebar,
    toggleSidebar,
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

ОБЩИЕ ПРАВИЛА ФРОНТЕНДА:

В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api. как ты видел выше
----

Ситуация следующая: я врач- психиатр. работаю в коммерческом многопрофильном центре с vip пациентами. Предыдущая заведующая создавала проект, на который было потрачено очень много денег. Проект вообще провалился и заведующую уволили. я взялся за то, чтобы переделать проект с нуля. Поскольку я уменю программировать, я сделал заново веб-приложение. 

Была большая встреча с руководством. на ней присутствовали it-дирекция и дирекция по маркетингу. они одобрили проект в запуск.

Планируется несколько этапов запуска.

Сейчас отдел маркетинга будет смотреть на дизайн и подгонять его под дизайн сайта медицинского центра

Затем будет интеграция в сайт медицинского центра, а в перспективе - в мобильное приложение клиники.

Ну, ты пойми.. они меня знают как психиатра, а кто-то из руководства вообще видит впервые. Я немного переживаю и хочу оправдать ожидания. Мне надо, чтобы у них вообще не было никаких сомнений в том, что со мной можно разговааривать на их языке.

Я хочу насть с отдела маркетинга и стилей. Давай сделаем для суперпользователя отдельную страницу и для этой страницы вкладку в боковой панели/bottomsheet в зависимости от устройства. В ней мы сделаем следующее: пусть там будет полная настройка стилей для кастомизации из frontend\app\assets\css\main.css

Я бы хотел, чтобы отдел маркетинга зашёл туда, увидел интерфейс, где он может менять люой из компонентов из frontend\app\assets\css\main.css, он мог менять, затем нажать на Сохранить. Результат кастомизации сохранялся в localstorage, чтобы только он видел эти изменения на всех страницах сайта, независимо от перехагрузки страницы. Плюс, когда сотрудник изменил хоть что-то в этих настройках, в navbar была кнопка: Сбросить стили, чтобы стили были сброшены до тех, которые были изначально и Вернуть стили - тогда возвращаются стили, которые сотрудник сделал последние. И еще была кнопка: Отправить разработчику и в этом случае, мне на почту maxim-titkov@yandex.ru отправлялись стили (тут не суть важно, но делательно, чтобы я мог их копировать и вставить в main.css для скорости) и я потом смог обновить сайт в соответвтвии с требованиями маркетинга.

И предложи, что еще можно такого красивого сделать, чтобы им понравилось.

Для начала, задай уточняющие вопросы и при необходимости, попроси прислать недостающие файлы.

В базу данных забивать стили не надо. Я этот функционал все равно выпилю после полноценного запуска сайта, это временная мера, направленная в том числе, на мой авторитет.