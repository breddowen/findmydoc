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
backend/test_database.db (?)
```

*Files: 141*

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
frontend/app/components/layout/Navbar.vue (405 lines)
frontend/app/components/layout/PatientActions.vue (29 lines)
frontend/app/components/layout/Sidebar.vue (178 lines)
frontend/app/components/layout/ThemeToggle.vue (28 lines)
frontend/app/components/life-aspects/FormDialog.vue (165 lines)
frontend/app/components/life-aspects/Tag.vue (85 lines)
frontend/app/components/life-aspects/TagLinks.vue (392 lines)
frontend/app/components/notifications/BrowserPermission.vue (96 lines)
frontend/app/components/notifications/Center.vue (181 lines)
frontend/app/components/patient/ContactDialog.vue (208 lines)
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
frontend/app/components/programs/viewer/Stage.vue (411 lines)
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
*Files: 81*

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
frontend/app/pages/programs/[id]/index.vue (404 lines)
frontend/app/pages/programs/index.vue (285 lines)
frontend/app/pages/programs/new.vue (12 lines)
frontend/app/pages/questionnaires/[id].vue (375 lines)
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
```
*Files: 2*

### composables

```
frontend/app/composables/useAppNavigation.js (199 lines)
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
frontend/app/stores/life-aspects.js (158 lines)
frontend/app/stores/notifications.js (387 lines)
frontend/app/stores/patient-home.js (339 lines)
frontend/app/stores/patients.js (105 lines)
frontend/app/stores/programs.js (237 lines)
frontend/app/stores/questionnaires.js (206 lines)
frontend/app/stores/services.js (159 lines)
frontend/app/stores/tag-access.js (210 lines)
frontend/app/stores/ui.js (203 lines)
frontend/app/stores/user.js (111 lines)
frontend/app/stores/users.js (266 lines)
```
*Files: 16*

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


Файлы, которые могут пригодиться (некоторые урезаны, потому что очень длинные):\
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
    FUNCTION BODY
    return datetime.now(timezone.utc)
def normalize_datetime(value: datetime) -> datetime:
    FUNCTION BODY
    return value
def get_program_questionnaire_submission(
    *,
    session: Session,
    patient_id: uuid.UUID,
    item: ProgramStageItem,
) -> QuestionnaireSubmission | None:
    FUNCTION BODY
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
    FUNCTION BODY
    return {link.tag_id for link in links}
def get_program_tags(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> list[Tag]:
    FUNCTION BODY
    return sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )
def validate_program_periods(program_data) -> None:
    FUNCTION BODY
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Порядок элементов этапа "
                    f"«{stage.title}» должен быть уникальным"
                ),
            )
def get_patient_program_access(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> PatientProgramAccess | None:
    FUNCTION BODY
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
    FUNCTION BODY
    return bool(access and access.is_active)
def get_program_enrollment(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program_id: uuid.UUID,
) -> ProgramEnrollment | None:
    FUNCTION BODY
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
    FUNCTION BODY
    return bool(
        submission
        and submission.status
        == QuestionnaireSubmissionStatus.COMPLETED
    )
def get_stage_task_items(
    stage: ProgramStage,
) -> list[ProgramStageItem]:
    FUNCTION BODY
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
    FUNCTION BODY
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
    FUNCTION BODY
    return ProgramStageStatus.AVAILABLE
def calculate_program_progress(
    *,
    session: Session,
    patient_id: uuid.UUID,
    program: Program,
) -> tuple[int, int, float]:
    FUNCTION BODY
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
    FUNCTION BODY
        return
def sync_patient_program_enrollments(
    *,
    session: Session,
    patient_id: uuid.UUID,
) -> None:
    FUNCTION BODY
def get_program_content_item(
    *,
    session: Session,
    program_id: uuid.UUID,
    content_type: ProgramItemType,
    content_id: uuid.UUID,
    stage_id: uuid.UUID | None = None,
) -> ProgramStageItem | None:
    FUNCTION BODY
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
    FUNCTION BODY
    return item

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

<!-- ./frontend/app/layouts/default.vue -->
<script setup>
</script>

<template>
  <LayoutSidebar>
    <div
      class="bg-base-200 flex min-h-dvh min-w-0 flex-col"
    >
      <LayoutEmailVerificationBanner />
      <LayoutNavbar />

      <main
        class="mx-auto w-full max-w-7xl flex-1 px-4 py-6 sm:py-8"
      >
        <slot />
      </main>

      <LayoutFooter />
    </div>
  </LayoutSidebar>
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

<!-- ./frontend/app/pages/programs/[id]/index.vue -->
<script setup>
const route = useRoute()
const auth = useAuthStore()
const store = useProgramsStore()

const selectedStageIndex = ref(0)

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
  getPurchaseActionLabel,
} = useProgramPrice()

const purchaseActionLabel = computed(() =>
  getPurchaseActionLabel(program.value),
)

const loading = ref(true)
const starting = ref(false)
const purchaseDialogOpen = ref(false)

const message = ref('')
const errorMessage = ref('')

const program = computed(
  () => store.currentProgram,
)

const isPatient = computed(
  () => auth.activeRole === 'patient',
)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

const selectedStage = computed(
  () => program.value?.stages[
    selectedStageIndex.value
  ],
)

async function loadProgram() {
  loading.value = true
  errorMessage.value = ''

  try {
    if (isPatient.value) {
      await store.fetchProgramForPatient(
        route.params.id,
      )

      // Если вернулись из опросника программы,
      // открываем тот же этап.
      const requestedStageId =
        typeof route.query.stage === 'string'
          ? route.query.stage
          : null

      if (requestedStageId) {
        const requestedIndex =
          program.value.stages.findIndex(
            (stage) =>
              stage.id === requestedStageId,
          )

        if (requestedIndex >= 0) {
          selectedStageIndex.value =
            requestedIndex

          return
        }
      }

      // Если конкретный этап не был передан,
      // выбираем текущий активный этап.
      const preferredIndex =
        program.value.stages.findIndex(
          (stage) =>
            [
              'available',
              'in_progress',
              'overdue',
            ].includes(stage.status),
        )

      selectedStageIndex.value =
        preferredIndex >= 0
          ? preferredIndex
          : 0
    } else {
      await store.fetchProgramForStaff(
        route.params.id,
      )
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программу'
  } finally {
    loading.value = false
  }
}

async function startProgram() {
  starting.value = true
  errorMessage.value = ''
  if (starting.value || !program.value) return

  try {
    await store.startProgram(program.value.id)
    message.value = 'Программа начата'

    await loadProgram()
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось начать программу'
  } finally {
    starting.value = false
  }
}

async function requestPurchase() {
  if (!program.value) return

  errorMessage.value = ''

  if (program.value.purchase_requested) {
    message.value =
      'Запрос уже отправлен медицинскому ассистенту.'
    return
  }

  purchaseDialogOpen.value = true
}

function handlePurchaseRequested({ programId, response }) {
  if (program.value?.id !== programId) return

  program.value.purchase_requested = true
  message.value = response.message
}

onMounted(loadProgram)
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="3"
  />

  <div
    v-else-if="errorMessage && !program"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="program"
    class="space-y-6"
  >
    <header
      class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
    >
      <div
        class="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between"
      >
        <div class="min-w-0 flex-1">
          <div
                class="flex flex-wrap items-center gap-2"
                >
                <span class="text-primary text-2xl font-bold">
                    {{ formatFinalPrice(program) }}
                </span>

                <span
                    v-if="hasDiscount(program)"
                    class="text-base-content/40 line-through"
                >
                    {{ formatOriginalPrice(program) }}
                </span>

                <span
                    v-if="hasDiscount(program)"
                    class="badge badge-error font-bold"
                >
                    −{{ program.service?.discount_percent }}%
                </span>

                <span
                    v-if="program.is_popular"
                    class="badge badge-warning gap-1"
                >
                    <Icon
                    name="lucide:flame"
                    class="size-3"
                    />

                    Популярное
                </span>

                <span
                    v-if="program.has_program_access"
                    class="badge badge-success"
                >
                    Полный доступ
                </span>
                </div>

          <h1
            class="mt-3 text-3xl font-bold sm:text-4xl"
          >
            {{ program.title }}
          </h1>

          <p
            v-if="program.description"
            class="text-base-content/70 mt-3 max-w-3xl"
          >
            {{ program.description }}
          </p>

          <p
            v-if="isPatient && program.service"
            class="border-primary/20 bg-primary/5 mt-4 rounded-2xl border p-4 text-sm"
          >
            Начать можно бесплатно. Материалы без отметки Pro доступны
            без покупки. Консультации и Pro-материалы относятся
            к программе сопровождения со специалистами.
          </p>

          <div
            v-if="program.service"
            class="border-base-300 mt-5 rounded-2xl border p-4"
          >
            <div class="flex flex-wrap items-center gap-2">
              <span
                v-if="program.service.code"
                class="badge badge-neutral font-mono"
              >
                {{ program.service.code }}
              </span>

              <span class="font-medium">
                {{ program.service.title }}
              </span>
            </div>

            <p
              v-if="program.service.description"
              class="text-base-content/60 mt-2 text-sm"
            >
              {{ program.service.description }}
            </p>
          </div>

          <div class="mt-4 flex flex-wrap gap-1">
            <span
              v-for="tag in program.tags"
              :key="tag.id"
              class="badge badge-outline"
            >
              {{ tag.name }}
            </span>
          </div>
        </div>

        <div class="flex flex-col gap-2 sm:flex-row">
          <NuxtLink
            v-if="canManage"
            :to="`/programs/${program.id}/edit`"
            class="btn btn-outline"
          >
            <Icon
              name="lucide:pencil"
              class="size-4"
            />
            Редактировать
          </NuxtLink>

          <button
            v-if="
              isPatient
              && !program.enrollment
            "
            type="button"
            class="btn btn-primary"
            :disabled="starting"
            @click="startProgram"
          >
            <span
              v-if="starting"
              class="loading loading-spinner loading-sm"
            />

            Начать программу
          </button>
        </div>
      </div>

      <div
        v-if="isPatient && program.enrollment"
        class="mt-6"
      >
        <div class="mb-2 flex justify-between text-sm">
          <span>
            Общий прогресс
          </span>

          <strong>
            {{ program.progress_percent }}%
          </strong>
        </div>

        <progress
          class="progress progress-primary w-full"
          :value="program.progress_percent"
          max="100"
        />

        <p class="text-base-content/50 mt-2 text-xs">
          День программы:
          {{ program.enrollment.elapsed_days }}
        </p>
      </div>
    </header>

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

    <div class="overflow-x-auto pb-2">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(stage, index) in program.stages"
          :key="stage.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedStageIndex === index,
          }"
          @click="selectedStageIndex = index"
        >
          <Icon
            :name="
              stage.status === 'completed'
                ? 'lucide:circle-check'
                : stage.status === 'overdue'
                  ? 'lucide:triangle-alert'
                  : 'lucide:circle'
            "
            class="size-4"
          />

          Этап {{ index + 1 }}
        </button>
      </div>
    </div>

    <ProgramsViewerStage
        v-if="selectedStage"
        :stage="selectedStage"
        :program-id="program.id"
        :is-patient="isPatient"
        :purchase-label="purchaseActionLabel"
        :purchase-requested="Boolean(program.purchase_requested)"
        @purchase="requestPurchase"
      />
      <PatientPurchaseDialog
        v-if="isPatient"
        v-model="purchaseDialogOpen"
        :program="program"
        @requested="handlePurchaseRequested"
      />
  </div>
</template>

<!-- ./frontend/app/components/programs/viewer/Stage.vue -->
<script setup>
const props = defineProps({
  stage: {
    type: Object,
    required: true,
  },
  programId: {
    type: String,
    required: true,
  },
  patientId: {
    type: String,
    default: null,
  },
  isPatient: {
    type: Boolean,
    default: false,
  },
  purchaseLabel: {
    type: String,
    default: 'Купить программу',
  },
  purchaseRequested: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits([
  'purchase',
])

const statusMeta = {
  upcoming: {
    title: 'Ещё не открыт',
    class: 'badge-neutral',
    icon: 'lucide:clock',
  },
  available: {
    title: 'Доступен',
    class: 'badge-info',
    icon: 'lucide:play',
  },
  in_progress: {
    title: 'В процессе',
    class: 'badge-warning',
    icon: 'lucide:loader-circle',
  },
  completed: {
    title: 'Выполнен',
    class: 'badge-success',
    icon: 'lucide:circle-check',
  },
  overdue: {
    title: 'Есть невыполненные задания',
    class: 'badge-error',
    icon: 'lucide:triangle-alert',
  },
}

function getItemLink(item) {
  if (item.item_type === 'article') {
    return {
      path: `/content/articles/${item.content_id}`,
      query: {
        source: 'program',
        program_id: props.programId,
        program_stage_id: props.stage.id,

        // Пока сохраняем прежние параметры для
        // совместимости с существующим возвратом.
        program: props.programId,
        stage: props.stage.id,
      },
    }
  }

  if (
    item.item_type === 'questionnaire'
    && props.isPatient
  ) {
    return {
      path: `/questionnaires/${item.content_id}`,
      query: {
        program: props.programId,
        stage: props.stage.id,
      },
    }
  }

  if (
    item.item_type === 'questionnaire'
    && props.patientId
    && item.submission_id
  ) {
    return (
      `/patients/${props.patientId}`
      + `/questionnaires/${item.submission_id}`
    )
  }

  return null
}
function canOpenItem(item) {
  if (item.item_type === 'consultation') {
    return false
  }

  if (props.isPatient) {
    return item.can_access
  }

  if (item.item_type === 'article') {
    return true
  }

  return Boolean(
    props.patientId
    && item.submission_id
  )
}

function getActionText(item) {
  if (props.isPatient) {
    return item.is_completed
      ? 'Открыть снова'
      : 'Выполнить'
  }

  if (item.item_type === 'article') {
    return 'Открыть статью'
  }

  if (item.submission_id) {
    return item.is_completed
      ? 'Посмотреть результат'
      : 'Посмотреть ответы'
  }

  return ''
}
</script>

<template>
  <section
    class="bg-base-100 border-base-300 rounded-3xl border p-5 sm:p-7"
  >
    <div
      class="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between"
    >
      <div>
        <p class="text-primary text-sm font-medium">
          День {{ stage.day_from }}–{{ stage.day_to }}
        </p>

        <h2 class="mt-1 text-2xl font-bold">
          {{ stage.title }}
        </h2>

        <p
          v-if="stage.description"
          class="text-base-content/70 mt-3"
        >
          {{ stage.description }}
        </p>
      </div>

      <span
        class="badge gap-1"
        :class="
          statusMeta[stage.status]?.class
        "
      >
        <Icon
          :name="
            statusMeta[stage.status]?.icon
            || 'lucide:circle'
          "
          class="size-3"
        />

        {{
          statusMeta[stage.status]?.title
          || stage.status
        }}
      </span>
    </div>

    <div
      v-if="isPatient"
      class="mt-5"
    >
      <div class="mb-2 flex justify-between text-sm">
        <span>Выполнение этапа</span>
        <strong>{{ stage.progress_percent }}%</strong>
      </div>

      <progress
        class="progress progress-primary w-full"
        :value="stage.progress_percent"
        max="100"
      />
    </div>

    <div
      v-if="!isPatient && stage.doctor_description"
      class="border-info/30 bg-info/10 mt-5 rounded-2xl border p-4"
    >
      <div class="flex gap-3">
        <Icon
          name="lucide:stethoscope"
          class="text-info size-5 shrink-0"
        />

        <div>
          <p class="font-semibold">
            Инструкция для врача
          </p>

          <p class="mt-1 text-sm">
            {{ stage.doctor_description }}
          </p>
        </div>
      </div>
    </div>

    <div class="relative mt-8 space-y-4">
      <div
        class="bg-base-300 absolute bottom-5 left-5 top-5 w-0.5"
      />

      <article
        v-for="(item, index) in stage.items"
        :key="item.id"
        class="relative flex gap-4"
      >
        <div
          class="z-10 flex size-10 shrink-0 items-center justify-center rounded-full border-4 border-base-100"
          :class="{
            'bg-success text-success-content':
              item.is_completed,
            'bg-primary text-primary-content':
              !item.is_completed
              && item.can_access
              && item.item_type !== 'consultation',
            'bg-base-300':
              !item.can_access,
            'bg-accent text-accent-content':
              item.item_type === 'consultation',
          }"
        >
          <Icon
            v-if="item.is_completed"
            name="lucide:check"
            class="size-4"
          />

          <Icon
            v-else-if="item.item_type === 'article'"
            name="lucide:file-text"
            class="size-4"
          />

          <Icon
            v-else-if="
              item.item_type === 'questionnaire'
            "
            name="lucide:clipboard-list"
            class="size-4"
          />

          <Icon
            v-else
            name="lucide:stethoscope"
            class="size-4"
          />
        </div>

        <div
          class="border-base-300 min-w-0 flex-1 rounded-2xl border p-4"
          :class="{
            'border-success/40 bg-success/5':
              item.is_completed,
            'border-accent/40 bg-accent/5':
              item.item_type === 'consultation',
          }"
        >
          <div
            class="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between"
          >
            <div>
              <p class="text-base-content/50 text-xs">
                Шаг {{ index + 1 }}
              </p>

              <h3 class="mt-1 font-semibold">
                {{ item.title }}
              </h3>

              <p
                v-if="item.description"
                class="text-base-content/60 mt-2 text-sm"
              >
                {{ item.description }}
              </p>
            </div>

            <span
              v-if="item.pro_content"
              class="badge badge-secondary shrink-0"
            >
              Pro
            </span>
          </div>

          <div
                v-if="
                    item.item_type !== 'consultation'
                "
                class="mt-4"
                >
                <!-- Пациент -->
                <template v-if="isPatient">
                  <NuxtLink
                    v-if="item.can_access"
                    :to="getItemLink(item)"
                    class="btn btn-primary btn-sm"
                  >
                    {{ getActionText(item) }}
                  </NuxtLink>

                  <template v-else-if="item.pro_content">
                    <p class="text-base-content/60 mb-2 text-xs">
                      Этот материал доступен в программе сопровождения.
                    </p>

                    <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      :disabled="purchaseRequested"
                      @click="emit('purchase')"
                    >
                      <Icon
                        :name="
                          purchaseRequested
                            ? 'lucide:check'
                            : 'lucide:shopping-cart'
                        "
                        class="size-4"
                      />

                      {{
                        purchaseRequested
                          ? 'Запрос отправлен'
                          : purchaseLabel
                      }}
                    </button>
                  </template>

                  <p v-else class="text-base-content/60 text-sm">
                    Материал пока недоступен.
                  </p>
                </template>

                <!-- Врач, ассистент или суперпользователь -->
                <template v-else>
                    <NuxtLink
                    v-if="canOpenItem(item)"
                    :to="getItemLink(item)"
                    class="btn btn-outline btn-sm"
                    >
                    <Icon
                        :name="
                        item.item_type === 'article'
                            ? 'lucide:external-link'
                            : 'lucide:clipboard-check'
                        "
                        class="size-4"
                    />

                    {{ getActionText(item) }}
                    </NuxtLink>

                    <span
                    v-else-if="
                        item.item_type === 'questionnaire'
                    "
                    class="badge badge-ghost"
                    >
                    Пациент не начинал
                    </span>
                </template>
                </div>

          <div
            v-else
            class="mt-4 flex items-center gap-2 text-sm"
          >
            <Icon
              name="lucide:calendar-clock"
              class="text-accent size-4"
            />

            Консультация входит в план программы. Дату и время согласует ассистент клиники.
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<!-- ./frontend/app/components/programs/PatientAccess.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const {
  formatFinalPrice,
  formatOriginalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const confirmOpen = ref(false)
const selectedProgram = ref(null)

const errorMessage = ref('')

function requestToggle(program) {
  selectedProgram.value = program
  confirmOpen.value = true
}

async function confirmToggle() {
  if (!selectedProgram.value) return

  try {
    await store.setPatientProgramAccess(
      props.patientId,
      selectedProgram.value.program_id,
      !selectedProgram.value.is_active,
    )

    confirmOpen.value = false
    selectedProgram.value = null
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось изменить доступ'
  }
}

const sortedPrograms = computed(() =>
  [...store.patientAccessPrograms].sort(
    (first, second) => {
      if (
        first.purchase_requested
        !== second.purchase_requested
      ) {
        return first.purchase_requested
          ? -1
          : 1
      }

      return first.title.localeCompare(
        second.title,
        'ru',
      )
    },
  ),
)

onMounted(async () => {
  try {
    await store.fetchPatientProgramAccess(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section
    class="bg-base-100 border-base-300 rounded-2xl border p-5 sm:p-6"
  >
    <div>
      <h2 class="text-xl font-bold">
        Доступ к программам
      </h2>

      <p class="text-base-content/60 mt-1 text-sm">
        Включение открывает Pro-контент только внутри
        выбранной программы.
      </p>
    </div>

    <div
      v-if="errorMessage"
      class="alert alert-error mt-4"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="list"
      :count="3"
    />

    <div
      v-else
      class="mt-5 space-y-3"
    >
      <div
        v-for="program in sortedPrograms"
        :key="program.program_id"
        class="border-base-300 flex flex-col gap-4 rounded-2xl border p-4 sm:flex-row sm:items-center"
        :class="{
          'border-warning bg-warning/5 ring-warning/10 ring-4':
            program.purchase_requested,
        }"
      >
        <div class="min-w-0 flex-1">
          <div class="flex flex-wrap items-center gap-2">
            <p class="font-medium">
              {{ program.title }}
            </p>

            <span
              v-if="program.purchase_requested"
              class="badge badge-warning badge-sm gap-1"
            >
              <Icon
                name="lucide:shopping-cart"
                class="size-3"
              />
              Пациент запросил доступ
            </span>

            <span
              v-if="program.is_hidden"
              class="badge badge-ghost badge-sm"
            >
              Скрыта
            </span>
          </div>

          <div
            class="text-base-content/60 mt-2 flex flex-wrap items-center gap-2 text-sm"
          >
            <span
              v-if="program.service?.code"
              class="font-mono"
            >
              {{ program.service.code }}
            </span>

            <strong>
              {{ formatFinalPrice(program) }}
            </strong>

            <span
              v-if="hasDiscount(program)"
              class="text-base-content/40 line-through"
            >
              {{ formatOriginalPrice(program) }}
            </span>
          </div>
        </div>

        <label
          class="flex cursor-pointer items-center gap-3"
        >
          <span class="text-sm">
            {{
              program.is_active
                ? 'Доступ открыт'
                : 'Нет доступа'
            }}
          </span>

          <input
            type="checkbox"
            class="toggle toggle-success"
            :checked="program.is_active"
            @change.prevent="requestToggle(program)"
          >
        </label>
      </div>
    </div>
  </section>

  <UiResponsiveDialog
    v-model="confirmOpen"
    :title="
      selectedProgram?.is_active
        ? 'Отключить доступ'
        : 'Открыть доступ'
    "
    max-width-class="max-w-md"
  >
    <p>
      {{
        selectedProgram?.is_active
          ? 'Пациент потеряет доступ к Pro-контенту внутри программы.'
          : 'Пациент получит доступ ко всему Pro-контенту внутри программы.'
      }}
    </p>

    <p class="mt-3 font-semibold">
      {{ selectedProgram?.title }}
    </p>

    <template #footer>
      <div class="flex justify-end gap-2">
        <button
          type="button"
          class="btn"
          @click="confirmOpen = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn"
          :class="
            selectedProgram?.is_active
              ? 'btn-error'
              : 'btn-success'
          "
          @click="confirmToggle"
        >
          Подтвердить
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>

<!-- ./frontend/app/components/programs/PatientProgress.vue -->
<script setup>
const props = defineProps({
  patientId: {
    type: String,
    required: true,
  },
})

const store = useProgramsStore()

const loading = ref(true)
const errorMessage = ref('')

const selectedProgramIndex = ref(0)
const selectedStageIndexes = reactive({})

const selectedProgram = computed(
  () =>
    store.patientProgressPrograms[
      selectedProgramIndex.value
    ],
)

function getSelectedStage(program) {
  const index =
    selectedStageIndexes[program.id] || 0

  return program.stages[index]
}

function statusName(program) {
  if (!program.enrollment) {
    if (program.purchase_requested) {
      return 'Запрошена пациентом'
    }

    return 'Доступ открыт, не начата'
  }

  if (
    program.enrollment.status === 'completed'
  ) {
    return 'Завершена'
  }

  return 'В процессе'
}

onMounted(async () => {
  try {
    await store.fetchPatientProgramProgress(
      props.patientId,
    )
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы пациента'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <UiContentSkeleton
    v-if="loading"
    variant="card"
    :count="2"
  />

  <div
    v-else-if="errorMessage"
    class="alert alert-error"
  >
    {{ errorMessage }}
  </div>

  <div
    v-else-if="store.patientProgressPrograms.length"
    class="space-y-5"
  >
    <div class="overflow-x-auto pb-1">
      <div
        role="tablist"
        class="tabs tabs-box flex-nowrap"
      >
        <button
          v-for="(program, index) in store.patientProgressPrograms"
          :key="program.id"
          type="button"
          role="tab"
          class="tab min-w-max gap-2"
          :class="{
            'tab-active':
              selectedProgramIndex === index,
          }"
          @click="selectedProgramIndex = index"
        >
          <Icon
            name="lucide:route"
            class="size-4"
          />
          {{ program.title }}
        </button>
      </div>
    </div>

    <template v-if="selectedProgram">
      <header
        class="bg-base-100 border-base-300 rounded-2xl border p-5"
      >
        <div
          class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between"
        >
          <div>
            <h2 class="text-xl font-bold">
              {{ selectedProgram.title }}
            </h2>

            <p class="text-base-content/60 text-sm">
              {{ statusName(selectedProgram) }}
            </p>
          </div>

          <span
            class="badge"
            :class="{
              'badge-warning':
                selectedProgram.purchase_requested,
              'badge-success':
                selectedProgram.enrollment?.status
                  === 'completed',
              'badge-primary':
                selectedProgram.enrollment?.status
                  === 'active',
            }"
          >
            {{ selectedProgram.progress_percent }}%
          </span>
        </div>

        <progress
          class="progress progress-primary mt-4 w-full"
          :value="selectedProgram.progress_percent"
          max="100"
        />
      </header>

      <div class="overflow-x-auto pb-1">
        <div class="join">
          <button
            v-for="(stage, index) in selectedProgram.stages"
            :key="stage.id"
            type="button"
            class="btn join-item btn-sm"
            :class="{
              'btn-primary':
                (selectedStageIndexes[
                  selectedProgram.id
                ] || 0) === index,
            }"
            @click="
              selectedStageIndexes[
                selectedProgram.id
              ] = index
            "
          >
            <Icon
              :name="
                stage.status === 'completed'
                  ? 'lucide:circle-check'
                  : stage.status === 'overdue'
                    ? 'lucide:triangle-alert'
                    : 'lucide:circle'
              "
              class="size-4"
            />

            Этап {{ index + 1 }}
          </button>
        </div>
      </div>

      <ProgramsViewerStage
        v-if="getSelectedStage(selectedProgram)"
        :stage="getSelectedStage(selectedProgram)"
        :program-id="selectedProgram.id"
        :patient-id="patientId"
        :is-patient="false"
        />
    </template>
  </div>

  <div
    v-else
    class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
  >
    <Icon
      name="lucide:route-off"
      class="text-base-content/30 mx-auto size-12"
    />

    <p class="mt-4 font-medium">
      Пациент пока не начал и не приобретал программы
    </p>
  </div>
</template>

<!-- ./frontend/app/components/programs/VisibilityDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

const props = defineProps({
  program: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits([
  'hidden',
])

const store = useProgramsStore()

const hiding = ref(false)
const errorMessage = ref('')

async function hideProgram() {
  if (!props.program) return

  hiding.value = true
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      props.program.id,
      true,
    )

    emit('hidden', response)
    model.value = false
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось скрыть программу'
  } finally {
    hiding.value = false
  }
}
</script>

<template>
  <UiResponsiveDialog
    v-model="model"
    title="Скрыть программу"
    max-width-class="max-w-md"
  >
    <div class="space-y-4">
      <div
        class="bg-warning/10 border-warning/30 rounded-2xl border p-4"
      >
        <div class="flex gap-3">
          <Icon
            name="lucide:eye-off"
            class="text-warning mt-0.5 size-5 shrink-0"
          />

          <div>
            <p class="font-semibold">
              Программа исчезнет из каталога пациентов
            </p>

            <p class="text-base-content/70 mt-1 text-sm">
              Существующие данные прохождения сохранятся.
              Программу можно будет снова показать.
            </p>
          </div>
        </div>
      </div>

      <p>
        Вы действительно хотите скрыть программу:
      </p>

      <p class="font-semibold">
        {{ program?.title }}
      </p>

      <div
        v-if="errorMessage"
        class="alert alert-error"
      >
        {{ errorMessage }}
      </div>
    </div>

    <template #footer>
      <div
        class="flex flex-col-reverse gap-2 sm:flex-row sm:justify-end"
      >
        <button
          type="button"
          class="btn"
          :disabled="hiding"
          @click="model = false"
        >
          Отмена
        </button>

        <button
          type="button"
          class="btn btn-warning"
          :disabled="hiding"
          @click="hideProgram"
        >
          <span
            v-if="hiding"
            class="loading loading-spinner loading-sm"
          />

          <Icon
            v-else
            name="lucide:eye-off"
            class="size-4"
          />

          Скрыть
        </button>
      </div>
    </template>
  </UiResponsiveDialog>
</template>

// ./frontend/app/stores/patient-home.js
export const usePatientHomeStore = defineStore(
  'patient-home',
  () => {
    const { $api } = useNuxtApp()

    const programs = ref([])
    const lifeAspects = ref([])
    const loading = ref(false)
    const errorMessage = ref('')

    let loadVersion = 0

    function priorityOf(program) {
      return Number(program.home_priority) || 0
    }

    function comparePrograms(left, right) {
      const priorityDifference =
        priorityOf(right) - priorityOf(left)

      if (priorityDifference) {
        return priorityDifference
      }

      const titleDifference = String(left.title || '').localeCompare(
        String(right.title || ''),
        'ru',
        { sensitivity: 'base' },
      )

      return titleDifference
        || String(left.id).localeCompare(String(right.id))
    }

    const orderedPrograms = computed(() =>
      [...programs.value].sort(comparePrograms),
    )

    function homeGroup(program) {
        if (!program.service) {
          return program.is_start ? 0 : 1
        }

        return program.has_program_access ? 2 : 3
      }

      const homePrograms = computed(() =>
        programs.value
          .filter(
            program =>
              program.enrollment?.status !== 'completed',
          )
          .sort(
            (left, right) =>
              homeGroup(left) - homeGroup(right)
              || comparePrograms(left, right),
          ),
      )

    const activePrograms = computed(() =>
      orderedPrograms.value.filter(
        program =>
          program.enrollment?.status === 'active',
      ),
    )

    function hasCompletedTask(program) {
      return (program.stages || []).some(
        stage => (stage.items || []).some(
          item =>
            [
              'article',
              'questionnaire',
            ].includes(item.item_type)
            && item.is_completed === true,
        ),
      )
    }

    // Пациент начал программу и выполнил
    // хотя бы одно задание.
    const inProgressPrograms = computed(() =>
      activePrograms.value.filter(hasCompletedTask),
    )

    // Остальные программы для обычного списка.
    // Уже показанные в блоке продолжения не дублируем.
    const remainingHomePrograms = computed(() => {
      const inProgressIds = new Set(
        inProgressPrograms.value.map(
          program => program.id,
        ),
      )

      return homePrograms.value.filter(
        program => !inProgressIds.has(program.id),
      )
    })

    const recommendedPrograms = computed(() =>
      remainingHomePrograms.value.filter(
        program => program.is_recommended === true,
      ),
    )

    const otherHomePrograms = computed(() =>
      remainingHomePrograms.value.filter(
        program => program.is_recommended !== true,
      ),
    )

    const completedPrograms = computed(() =>
      orderedPrograms.value.filter(
        program =>
          program.enrollment?.status === 'completed',
      ),
    )

    const hasCompletedStart = computed(() =>
      completedPrograms.value.some(
        program => program.is_start,
      ),
    )

    const primaryProgram = computed(() => {
      const activeWithAccess =
        activePrograms.value.find(
          program => program.has_program_access,
        )

      if (activeWithAccess) {
        return activeWithAccess
      }

      if (activePrograms.value.length) {
        return activePrograms.value[0]
      }

      const purchasedNotStarted =
        orderedPrograms.value.find(
          program =>
            program.has_program_access
            && !program.enrollment,
        )

      if (purchasedNotStarted) {
        return purchasedNotStarted
      }

      if (hasCompletedStart.value) {
        return null
      }

      return orderedPrograms.value.find(
        program =>
          program.is_start
          && !program.service
          && !program.enrollment,
      ) || null
    })

    const otherActivePrograms = computed(() =>
      activePrograms.value.filter(
        program =>
          program.id !== primaryProgram.value?.id,
      ),
    )

    const pendingRequests = computed(() =>
      orderedPrograms.value.filter(
        program => program.purchase_requested,
      ),
    )

    const supportPrograms = computed(() =>
      orderedPrograms.value
        .filter(
          program =>
            Boolean(program.service)
            && !program.is_start
            && !program.has_program_access
            && !program.purchase_requested,
        )
        .slice(0, 2),
    )

    async function load() {
      const currentVersion = ++loadVersion

      loading.value = true
      errorMessage.value = ''
      programs.value = []
      lifeAspects.value = []

      try {
        const [
          programResponse,
          aspectResponse,
        ] = await Promise.all([
          $api('/api/v1/programs/patient'),
          $api('/api/v1/life-aspects/patient'),
        ])

        if (currentVersion !== loadVersion) return

        programs.value = programResponse
        lifeAspects.value = aspectResponse
      } catch (error) {
        if (currentVersion !== loadVersion) return

        errorMessage.value =
          typeof error?.data?.detail === 'string'
            ? error.data.detail
            : 'Не удалось загрузить программы и сферы жизни'
      } finally {
        if (currentVersion === loadVersion) {
          loading.value = false
        }
      }
    }

    async function startProgram(programId) {
      return await $api(
        `/api/v1/programs/patient/${programId}/start`,
        {
          method: 'POST',
        },
      )
    }

    async function requestPurchase(programId) {
      const response = await $api(
        `/api/v1/programs/patient/${programId}/request-purchase`,
        {
          method: 'POST',
        },
      )

      const program = programs.value.find(
        item => item.id === programId,
      )

      if (program) {
        program.purchase_requested = true
      }

      return response
    }

    const homeLifeAspects = computed(() => {
      const programsById = new Map(
        programs.value.map(program => [
          program.id,
          program,
        ]),
      )

      const inProgressIds = new Set(
        inProgressPrograms.value.map(
          program => program.id,
        ),
      )

      return lifeAspects.value
        .map(aspect => ({
          ...aspect,

          // Используем полные пациентские данные программы:
          // доступ к материалам, прогресс, участие и услугу.
          programs: aspect.programs
            .map(program => programsById.get(program.id))
            .filter(program =>
              program
              && !inProgressIds.has(program.id),
            )
            .sort(
              (left, right) =>
                Number(Boolean(right.is_recommended))
                  - Number(Boolean(left.is_recommended))
                || comparePrograms(left, right),
            ),
        }))
        .filter(aspect => aspect.programs.length > 0)
    })

    const unclassifiedPrograms = computed(() => {
      const classifiedIds = new Set(
        lifeAspects.value.flatMap(
          aspect => aspect.programs.map(
            program => program.id,
          ),
        ),
      )

      return remainingHomePrograms.value.filter(
        program =>
          !classifiedIds.has(program.id)
          && !program.is_recommended,
      )
    })

    function clear() {
      loadVersion += 1
      programs.value = []
      lifeAspects.value = []
      loading.value = false
      errorMessage.value = ''
    }

    return {
      programs,
      loading,
      errorMessage,

      primaryProgram,
      otherActivePrograms,
      completedPrograms,
      hasCompletedStart,
      pendingRequests,
      supportPrograms,
      homePrograms,

      inProgressPrograms,
      remainingHomePrograms,
      recommendedPrograms,
      otherHomePrograms,

      load,
      startProgram,
      requestPurchase,
      clear,

      lifeAspects,
      homeLifeAspects,
      unclassifiedPrograms,
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

----
СПЕЦИФИКА ФРОНТЕНДА

В nuxt4 компоненты, и т.д. располагаются внутри ./app/, например: ./fronted/app/components/
аналогично с composables, layouts, middleware, pages, plugins, stores, assets

если, например, компонент: ./frontend/app/components/User/Data.vue, то при импорте в другие компоненты он будет выглядеть так: UserData.vue
если компонент в такой директории: ./frontend/app/components/User/UserData.vue, то в других компонентах он все равно будет вяглядеть так: UserData.vue. Лучше не дублируй у названия компонента название родительской директории.
Постарайся разделять компоненты, чтобы код был максимально читаемым
у каждого файла в самой первой строке в комментариях пиши его полный путь

в pinia store нужно чтобы файлы были .js (а не .ts), написаны на composition api. как ты видел выше

переиспользуемые компоненты:

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
<!-- ./frontend/app/components/ui/ResponsiveDialog.vue -->
<script setup>
const model = defineModel({
  type: Boolean,
  default: false,
})

defineProps({
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

const { isClientReady } = useClientReady()

const { matches: isDesktop } = useBreakpoint(
  '(min-width: 768px)',
)
</script>

<template>
  <!--
    Modal и BottomSheet появляются только после
    завершения hydration. Это предотвращает отличие
    серверного DOM от клиентского.
  -->
  <template v-if="isClientReady">
    <UiModal
      v-if="isDesktop"
      v-model="model"
      :title="title"
      :close-on-backdrop="closeOnBackdrop"
      :show-close-button="showCloseButton"
      :max-width-class="maxWidthClass"
      @close="emit('close')"
      @opened="emit('opened')"
    >
      <template
        v-if="$slots.header"
        #header
      >
        <slot name="header" />
      </template>

      <slot />

      <template
        v-if="$slots.footer"
        #footer
      >
        <slot name="footer" />
      </template>
    </UiModal>

    <UiBottomSheet
      v-else
      v-model="model"
      :title="title"
      :close-on-backdrop="closeOnBackdrop"
      :show-close-button="showCloseButton"
      @close="emit('close')"
      @opened="emit('opened')"
    >
      <template
        v-if="$slots.header"
        #header
      >
        <slot name="header" />
      </template>

      <slot />

      <template
        v-if="$slots.footer"
        #footer
      >
        <slot name="footer" />
      </template>
    </UiBottomSheet>
  </template>
</template>
<!-- ./frontend/app/components/layout/PatientActions.vue -->
<script setup>
const emit = defineEmits(['menu'])

const contactOpen = ref(false)
</script>

<template>
  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm shrink-0"
    aria-label="Открыть меню"
    @click="emit('menu')"
  >
    <Icon name="lucide:menu" class="size-5" />
  </button>

  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm text-primary bg-primary/10 shrink-0"
    aria-label="Заказать звонок ассистента"
    title="Связаться с ассистентом"
    @click="contactOpen = true"
  >
    <Icon name="lucide:phone" class="size-4" />
  </button>

  <PatientContactDialog v-model="contactOpen" />
</template>
<!-- ./frontend/app/components/articles/ReaderAction.vue -->
<script setup>
const props = defineProps({
  target: {
    type: Object,
    default: null,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['close'])

const atBoundary = ref(true)
const scrolling = ref(false)

const showClose = computed(() =>
  atBoundary.value && !scrolling.value,
)

let frame = null
let scrollTimer = null
let resizeObserver = null
let mounted = false

const EDGE_DISTANCE = 48

function getBounds() {
  const element = props.target

  if (!element) return null

  const rect = element.getBoundingClientRect()
  const scrollY = window.scrollY
  const viewportHeight = window.innerHeight

  const maxScroll = Math.max(
    document.documentElement.scrollHeight - viewportHeight,
    0,
  )

  const articleTop = rect.top + scrollY
  const articleBottom = rect.bottom + scrollY

  const start = Math.min(
    maxScroll,
    Math.max(0, articleTop - 16),
  )

  const end = Math.min(
    maxScroll,
    Math.max(start, articleBottom - viewportHeight),
  )

  return {
    start,
    end,
    shortArticle: rect.height <= viewportHeight,
  }
}

function updateBoundary() {
  const bounds = getBounds()

  if (!bounds) {
    atBoundary.value = true
    return
  }

  atBoundary.value =
    bounds.shortArticle
    || window.scrollY <= bounds.start + EDGE_DISTANCE
    || window.scrollY >= bounds.end - EDGE_DISTANCE
}

function scheduleUpdate() {
  if (frame !== null) return

  frame = window.requestAnimationFrame(() => {
    frame = null
    updateBoundary()
  })
}

function handleScroll() {
  scrolling.value = true

  window.clearTimeout(scrollTimer)
  scheduleUpdate()

  scrollTimer = window.setTimeout(() => {
    scrolling.value = false
    updateBoundary()
  }, 180)
}

function scrollToStart() {
  const bounds = getBounds()

  if (!bounds) return

  const reduceMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)',
  ).matches

  window.scrollTo({
    top: bounds.start,
    behavior: reduceMotion ? 'instant' : 'smooth',
  })
}

function handleClick() {
  if (props.disabled) return

  if (showClose.value) {
    emit('close')
  } else {
    scrollToStart()
  }
}

function observeTarget() {
  resizeObserver?.disconnect()

  if (!mounted || !props.target) return

  resizeObserver = new ResizeObserver(scheduleUpdate)
  resizeObserver.observe(props.target)
  resizeObserver.observe(document.documentElement)

  scheduleUpdate()
}

watch(
  () => props.target,
  observeTarget,
  { flush: 'post' },
)

onMounted(() => {
  mounted = true
  observeTarget()
  updateBoundary()

  window.addEventListener('scroll', handleScroll, {
    passive: true,
  })
  window.addEventListener('resize', scheduleUpdate)
})

onBeforeUnmount(() => {
  mounted = false

  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', scheduleUpdate)

  window.clearTimeout(scrollTimer)
  resizeObserver?.disconnect()

  if (frame !== null) {
    window.cancelAnimationFrame(frame)
  }
})
</script>

<template>
  <div
    class="fixed z-[60]"
    style="
      right: calc(1rem + env(safe-area-inset-right, 0px));
      bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
    "
  >
    <button
      type="button"
      class="btn btn-circle btn-lg border-base-300 bg-base-200 text-base-content hover:bg-base-300 shadow-lg"
      :disabled="disabled"
      :aria-label="showClose ? 'Закрыть статью' : 'В начало статьи'"
      :title="showClose ? 'Закрыть статью' : 'В начало статьи'"
      @click="handleClick"
    >
      <span
        v-if="disabled"
        class="loading loading-spinner loading-sm"
      />

      <Icon
        v-else
        :name="showClose ? 'lucide:x' : 'lucide:arrow-up'"
        class="size-6"
      />
    </button>
  </div>
</template>
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
<!-- ./frontend/app/components/layout/Footer.vue -->
<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer
    class="bg-neutral text-neutral-content mt-auto px-4 py-4"
  >
    <div
      class="mx-auto flex w-full max-w-7xl flex-col items-center justify-between gap-4 sm:flex-row"
    >
      <LayoutLogo
        to="/dashboard"
        variant="footer"
      />

      <div
        class="flex flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center text-xs sm:justify-end sm:text-right"
      >
        <span>
          Разработка — Максим Титков
        </span>

        <span
          class="hidden opacity-40 sm:inline"
          aria-hidden="true"
        >
          •
        </span>

        <a
          href="mailto:mtitkov@emcmos.ru"
          class="link whitespace-nowrap opacity-80 transition-opacity hover:opacity-100"
        >
          mtitkov@emcmos.ru
        </a>

        <span
          class="hidden opacity-40 sm:inline"
          aria-hidden="true"
        >
          •
        </span>

        <span class="whitespace-nowrap opacity-70">
          © {{ currentYear }}. Все права защищены.
        </span>
      </div>
    </div>
  </footer>
</template>
<!-- ./frontend/app/components/layout/PatientActions.vue -->
<script setup>
const emit = defineEmits(['menu'])

const contactOpen = ref(false)
</script>

<template>
  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm shrink-0"
    aria-label="Открыть меню"
    @click="emit('menu')"
  >
    <Icon name="lucide:menu" class="size-5" />
  </button>

  <button
    type="button"
    class="btn btn-circle btn-ghost btn-sm text-primary bg-primary/10 shrink-0"
    aria-label="Заказать звонок ассистента"
    title="Связаться с ассистентом"
    @click="contactOpen = true"
  >
    <Icon name="lucide:phone" class="size-4" />
  </button>

  <PatientContactDialog v-model="contactOpen" />
</template>
<!-- ./frontend/app/pages/programs/index.vue -->
<script setup>
const auth = useAuthStore()
const store = useProgramsStore()

const {
  formatOriginalPrice,
  formatFinalPrice,
  hasDiscount,
} = useProgramPrice()

const loading = ref(true)
const errorMessage = ref('')

const visibilityDialogOpen = ref(false)
const selectedProgram = ref(null)

const canManage = computed(() =>
  [
    'superuser',
    'med_assistant',
  ].includes(auth.activeRole),
)

function openHideDialog(program) {
  selectedProgram.value = program
  visibilityDialogOpen.value = true
}

async function showProgram(program) {
  errorMessage.value = ''

  try {
    const response = await store.setVisibility(
      program.id,
      false,
    )

    Object.assign(program, response)
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось показать программу'
  }
}

function handleHidden(response) {
  const item = store.programs.find(
    (program) => program.id === response.id,
  )

  if (item) {
    Object.assign(item, response)
  }
}

onMounted(async () => {
  try {
    if (auth.activeRole === 'patient') {
      await store.fetchProgramsForPatient()
    } else {
      await store.fetchProgramsForStaff()
    }
  } catch (error) {
    errorMessage.value =
      error?.data?.detail
      || 'Не удалось загрузить программы'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-6">
    <header
      class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <div>
        <h1 class="text-2xl font-bold sm:text-3xl">
          Программы
        </h1>

        <p class="text-base-content/60 mt-1">
          Пошаговые программы работы с материалами.
        </p>
      </div>

      <NuxtLink
        v-if="canManage"
        to="/programs/new"
        class="btn btn-primary"
      >
        <Icon
          name="lucide:plus"
          class="size-4"
        />
        Новая программа
      </NuxtLink>
    </header>

    <div
      v-if="errorMessage"
      class="alert alert-error"
    >
      {{ errorMessage }}
    </div>

    <UiContentSkeleton
      v-if="loading"
      variant="card"
      :count="3"
    />

    <div
      v-else-if="store.programs.length"
      class="grid gap-5 md:grid-cols-2 xl:grid-cols-3"
    >
      <div
        v-for="program in store.programs"
        :key="program.id"
        :class="[
          program.is_popular
            ? 'aura aura-rainbow'
            : '',
          'h-full',
        ]"
      >
        <article
          class="card bg-base-100 border-base-300 relative h-full overflow-hidden border"
          :class="{
            'opacity-60': program.is_hidden,
          }"
        >
          <div
            v-if="program.is_popular"
            class="bg-warning text-warning-content absolute right-0 top-0 rounded-bl-2xl px-4 py-2 text-xs font-bold shadow"
          >
            <Icon
              name="lucide:flame"
              class="mr-1 inline size-4"
            />
            Популярное
          </div>

          <div class="card-body">
            <div class="flex flex-wrap gap-2 pr-24">
              <span
                v-if="hasDiscount(program)"
                class="badge badge-error gap-1 font-bold"
              >
                <Icon
                  name="lucide:badge-percent"
                  class="size-3"
                />
                −{{ program.service?.discount_percent }}%
              </span>

              <span
                v-if="program.has_program_access"
                class="badge badge-success"
              >
                Полный доступ
              </span>

              <span
                v-if="program.purchase_requested"
                class="badge badge-warning"
              >
                Запрос отправлен
              </span>

              <span
                v-if="program.is_hidden"
                class="badge badge-ghost"
              >
                Скрыта
              </span>
            </div>

            <h2 class="card-title mt-2">
              {{ program.title }}
            </h2>

            <p
              class="text-base-content/60 line-clamp-3 text-sm"
            >
              {{ program.description }}
            </p>

            <div class="mt-2 flex items-end gap-2">
              <span class="text-primary text-xl font-bold">
                {{ formatFinalPrice(program) }}
              </span>

              <span
                v-if="hasDiscount(program)"
                class="text-base-content/40 text-sm line-through"
              >
                {{ formatOriginalPrice(program) }}
              </span>
            </div>

            <div class="mt-2 flex flex-wrap gap-1">
              <span
                v-for="tag in program.tags"
                :key="tag.id"
                class="badge badge-outline badge-sm"
              >
                {{ tag.name }}
              </span>
            </div>

            <div class="card-actions mt-auto pt-5">
              <NuxtLink
                :to="`/programs/${program.id}`"
                class="btn btn-primary btn-sm"
              >
                Открыть
              </NuxtLink>

              <NuxtLink
                v-if="canManage"
                :to="`/programs/${program.id}/edit`"
                class="btn btn-outline btn-sm"
              >
                <Icon
                  name="lucide:pencil"
                  class="size-4"
                />
                Изменить
              </NuxtLink>

              <button
                v-if="canManage && !program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="openHideDialog(program)"
              >
                <Icon
                  name="lucide:eye-off"
                  class="size-4"
                />
                Скрыть
              </button>

              <button
                v-if="canManage && program.is_hidden"
                type="button"
                class="btn btn-ghost btn-sm"
                @click="showProgram(program)"
              >
                <Icon
                  name="lucide:eye"
                  class="size-4"
                />
                Показать
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>

    <div
      v-else
      class="bg-base-100 border-base-300 rounded-2xl border border-dashed p-10 text-center"
    >
      <Icon
        name="lucide:route"
        class="text-base-content/30 mx-auto size-12"
      />

      <p class="mt-4 font-medium">
        Программ пока нет
      </p>
    </div>
  </div>

  <ProgramsVisibilityDialog
    v-model="visibilityDialogOpen"
    :program="selectedProgram"
    @hidden="handleHidden"
  />
</template>


Смотри, надо немного переделать. 
1. Для интерфейса прохождения программы надо сделать отдельный layout: пусть там будет измененный navbar. Лого убрать. В левом крайнем углу пусть будет бургер. Далее пусть будет текущий этап. Давай сдалем красиво в виде карточек, которые накладываются одна на другую. Только не увеличивай высоту navbar:
<div class="stack stack-end size-28">
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">A</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">B</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">C</div>
  </div>
</div>

Если в данном этапе выполнены все элементы: прочитаны статьи и заполнены опросники, то давай этап будет отмечаться как выполненный - пусть он будет более бесцветный и на нем будет стоять зеленая галочка, чтобы было понятно, что он выполнеен (или предложи, как лучше показать, что этап выполнен и надо переходить на другой). Правее будет кнопка > нажав на которую, карточка Этапа 2 будет перекрывать Этап 1. Давай  прогресс текущего этапа сделаем под Navbar в виде узкой полоски, как это сделано для статей, который этот:
<progress
      class="progress progress-secondary fixed inset-x-0 top-0 z-[70] h-1 w-full rounded-none"
      :value="progress"
      max="100"
      aria-label="Прогресс чтения статьи"
    />
Если можешь, сделай, чтобы он заполнялся градиентом от более светлого к более насыщенному.

Теперь надо изменить ту часть, которая описывает всю программу и заголовок программы, она занимает очень много места в самом верху страницы и отвлекает от этапов. Надо убрать стоимость, когда мы находимся внутри программы, то есть тут: <!-- ./frontend/app/pages/programs/[id]/index.vue -->
Сделать так, чтобы фон был такой же, как фон страницы (сейчас этСтоимость, заголовок, описание рпограммы, тег и прогресс визуально в виде карточки и он вообще не отличается от этапов - такие же карточки - ниже, это сбивает с толку). Пусть заголовок и описание будут не карточкой, а просто на странице. Плюс, на мобильных устройствах давай описание сделаем только первую строку с моногточием и кнопку для раскрытия, потому что сейчас оно занимает очень много места. Тегм программы уберем, потому что они тоже занимают очень много места. Общий прогресс давай оставим, но сделаем его в виде steps, где будут этапы 
<div class="overflow-x-auto">
  <ul class="steps">
    <li class="step">start</li>
    <li class="step step-secondary">2</li>
    <li class="step step-secondary">3</li>
    <li class="step step-secondary">4</li>
    <li class="step">5</li>
    <li class="step step-accent">6</li>
    <li class="step step-accent">7</li>
    <li class="step">8</li>
    <li class="step step-error">9</li>
    <li class="step step-error">10</li>
    <li class="step">11</li>
    <li class="step">12</li>
    <li class="step step-warning">13</li>
    <li class="step step-warning">14</li>
    <li class="step">15</li>
    <li class="step step-neutral">16</li>
    <li class="step step-neutral">17</li>
    <li class="step step-neutral">18</li>
    <li class="step step-neutral">19</li>
    <li class="step step-neutral">20</li>
    <li class="step step-neutral">21</li>
    <li class="step step-neutral">22</li>
    <li class="step step-neutral">23</li>
    <li class="step step-neutral">end</li>
  </ul>
</div>
То есть, нам надо, чтобы максимально пользователь понимал, что он двигается по шагам. Подумай еще ,может еще можно как-то сделать.

Пока что, плохо сделан канал для связи. У нас есть 3 варианта связи: заявка ассистенту на звонок, приобрести программу и записаться к врачу.

Смотри, надо, чтобы внутри программы был отдельный footer вместо текущего. Пусть там будет просто 3 кнопки:
Связаться с ассистентом, затем записаться к врачу и затем индивидуальные программы

При нажатии на Связаться с ассистентом, будет то же самое, что и тут:
<button
    type="button"
    class="btn btn-circle btn-ghost btn-sm text-primary bg-primary/10 shrink-0"
    aria-label="Заказать звонок ассистента"
    title="Связаться с ассистентом"
    @click="contactOpen = true"
  >
    <Icon name="lucide:phone" class="size-4" />
  </button>

При нажатии на кнопку записаться к врачу, будет также вылезать либо Bottomsheet, либо Modal в зависимости от устройства, в котором будет 2 карточки разных врачей: психиатра и специалиста по аддикциям - это тестовые карточки их напишем пока вручную для демонтарции. позже мы будем это приложение интегрировать в личный кабинет, откуда данные будут подтягиваться (сделай тестовый компонент карточек в ./frontend/app/components/test/PsychiatristCard.vue ну, тестовый store // ./frontend/app/stores/emc-app.js с данными врачей), в виде фото - давай сделаем плейсхолдер - не принципиально какой, главное, чтобы было видно карточки врачей. Под ФИО пусть будет написанна площадка приема: EMC (это название медицинского центра и адрес Щепкина 35) а под адресом Ближайшие дни. Если можешь, сделай, чтобвы отображались завтра и послезавтра (если расчитать дату сложно, то не заморачивайся, напиши словами затра, послезавтра). 
Кнопка приобрести программу должна вести сюда: <!-- ./frontend/app/pages/programs/index.vue -->  

Далее, вне программы (вне layoput программы, о котором я написал выше), надо сделать fab копонент основного цвета с иконкой сообщения. он должен быть как и у статьи и правом нижем углу у пациентов на всех страницах, кроме layout программы (который мы делаем). При нажатии на него муть также вылезает Modal или Bottomsheet, где будут те же кнопки: заявка ассистенту на звонок, приобрести программу и записаться к врачу

Ты понял - нужно сделать понятный способ связи.
----
Для начала, задай мне уточняющий вопросы и пришли список файлов, которые еще надо прислать, если какие-то нужны
Подумай, может ты знаешь еще какие-то варианты для моей задачи
































-----------------
1. Где использовать новый layout?
Да, именно на странице программы. Но если программа еще не начата, сейчас кнопка Начать программу ничего не делает. Давай ее уберем с каротчки программы и перенесем в navbar, если программа еще не начата. И при нажатии появляется то, что я описал
Пусть статьи и опросники тоже будут на этом layout, чтобы не сбивать пользователя

2. Что оставить в Navbar? - хороший воапрос. 
Что делать с текущими элементами справа — уведомлениями, переключателем темы и профилем? На мобильном я бы перенёс тему и профиль в меню, чтобы название этапа не оказалось зажато. - да, дававй так и сделаем
Сам бургер должен открывать обычное меню приложения или меню программы? Предлагаю обычное меню с заметным пунктом «Выйти из программы», ведущим на главную пациента. - отлично!

3. Как определять завершение этапа и разрешать переходы?
Этап выполнен, когда прочитаны все его статьи и завершены все опросники. - да, ок
Консультации не учитываются — как и в текущей модели. - разумеется
Выполненная карточка получает спокойный фон, зелёную галочку и подпись «Выполнен». - ок
Автоматически на следующий этап не переключаем: показываем явную кнопку «Следующий этап». - да, давай так
Просматривать другие этапы можно, но доступ к заданиям по-прежнему определяется backend. - ок. у меня пока демо, все этапы доступны сразу. потом закрою этот момент

Недоступные Pro-материалы должны мешать завершению этапа? - хорошая идея... да, давай так сделаем. но доступ к другим пусть будет. это,как бы, ознакомление с платной программой

Этап без заданий, только с консультацией, считать выполненным или просто показывать без прогресса? - таких не будет. любой этап содержит хотя бы одну статью либо опросник

И правильно ли я понимаю, что существующие ограничения по дням программы менять не нужно? - пока у меня MVP для демонтсрации руководству, оставляем их доступными

4. Footer внутри программы:
закреплён снизу экрана, чтобы связь всегда была доступна - нет, давай в конце страницы, чтобы не уменьшать и так небольшое поле
Уточни третье название: Индивидуальные программы - давай так сделаем

5. FAB вне программы
Ты написал «на всех страницах пациента». Включаем ли сюда чтение статьи и заполнение опросника? - хех... спасибо, что заметил... не, на этих не надо, конечно. Также, не надо на странице логина

И заодно, сделай ArticlesReaderAction яркого цвета, пожалуйста, сейчас вообще на него не обращают внимания

Также: после появления FAB убираем телефон из обычного Navbar, чтобы не дублировать вход в одно и то же действие? - да не знаю... ну давай уберем, все равно там вообще непонятно, что эта кнопка делает

6. Демонстрационная запись к врачу
Предлагаю пока показывать сообщение «Демонстрационный режим: запись пока недоступна», без отправки реальной заявки и без имитации успешной записи. Либо карточки могут быть просто информационными. - ну, давай так... как решишь

У стопки этапов показывать короткую подпись «Этап 2 из 5». Название этапа — одной строкой с многоточием. Это понятнее, чем только декоративные карточки. - отлично, давай

Общие steps сделать интерактивными: галочка — выполнен, выделенный контур — сейчас открыт, нейтральное состояние — остальные. Не опираться только на цвет. - не очень понял, но давай попробуем
Под Navbar показывать только прогресс выбранного этапа. Узкая градиентная полоска, привязанная к нижнему краю Navbar, будет учитывать его фактическую высоту. - да, отлично. желаельно как можно уже, но чтобы было заметно
Убрать дублирующий прогресс из карточки этапа в пациентском режиме. При этом сохранить его там, где компонент используется сотрудниками. - ок
В конце списка заданий показывать явный результат: «Все задания этапа выполнены» и кнопку перехода. Если выполнена только бесплатная часть — отдельную честную подпись вместо ощущения, что пользователь что-то пропустил. - ок
Сохранять выбранный этап в query-параметре stage. Тогда обновление страницы и возврат из материала не сбросят навигацию. - ок
Не открывать диалоги друг поверх друга. При выборе «Связаться с ассистентом» в общем окне связи сначала закрывать окно выбора, затем открывать существующий диалог заявки. - да
Описание программы на мобильном — одна строка и кнопка «Подробнее» / «Свернуть»; на десктопе — полностью. - супер!



