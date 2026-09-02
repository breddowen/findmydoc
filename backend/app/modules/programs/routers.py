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

router = APIRouter(
    prefix="/api/v1/programs",
    tags=["Programs"],
)

def get_program_service(
    *,
    session: Session,
    program: Program,
) -> MedicalService | None:
    if program.service_id is None:
        return None

    service = session.get(
        MedicalService,
        program.service_id,
    )

    if not service:
        # Такая ситуация возможна только при нарушении
        # целостности базы или ручном изменении данных.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Связанная услуга программы не найдена",
        )

    return service


def serialize_program_service_for_patient(
    *,
    session: Session,
    program: Program,
) -> MedicalServicePatientResponse | None:
    service = get_program_service(
        session=session,
        program=program,
    )

    if not service:
        return None

    return MedicalServicePatientResponse.model_validate(
        service
    )


def serialize_program_service_for_staff(
    *,
    session: Session,
    program: Program,
) -> MedicalServiceStaffResponse | None:
    service = get_program_service(
        session=session,
        program=program,
    )

    if not service:
        return None

    return MedicalServiceStaffResponse.model_validate(
        service
    )


def validate_program_service_choice(
    *,
    session: Session,
    service_id: uuid.UUID | None,
    current_service_id: uuid.UUID | None = None,
) -> MedicalService | None:
    if service_id is None:
        return None

    service = session.get(
        MedicalService,
        service_id,
    )

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Услуга не найдена",
        )

    # Скрытая услуга остаётся рабочей для уже связанной
    # программы, но её нельзя назначить заново.
    if (
        service.is_hidden
        and service.id != current_service_id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Скрытую услугу нельзя назначить программе"
            ),
        )

    return service

def fill_program_structure(
    *,
    session: Session,
    program: Program,
    payload: ProgramCreateRequest | ProgramUpdateRequest,
) -> None:
    validate_program_periods(payload)

    for tag_id in dict.fromkeys(payload.tag_ids):
        if not session.get(Tag, tag_id):
            raise HTTPException(
                status_code=404,
                detail=f"Тег {tag_id} не найден",
            )

        session.add(
            ProgramTagLink(
                program_id=program.id,
                tag_id=tag_id,
            )
        )

    for stage_data in sorted(
        payload.stages,
        key=lambda item: item.order_index,
    ):
        stage = ProgramStage(
            program_id=program.id,
            title=stage_data.title.strip(),
            description=stage_data.description,
            doctor_description=(
                stage_data.doctor_description
            ),
            day_from=stage_data.day_from,
            day_to=stage_data.day_to,
            order_index=stage_data.order_index,
        )

        session.add(stage)
        session.flush()

        for item_data in sorted(
            stage_data.items,
            key=lambda item: item.order_index,
        ):
            consultation_title = None
            consultation_description = None

            if item_data.item_type == ProgramItemType.ARTICLE:
                if not session.get(
                    Article,
                    item_data.article_id,
                ):
                    raise HTTPException(
                        status_code=404,
                        detail="Статья не найдена",
                    )

            elif (
                item_data.item_type
                == ProgramItemType.QUESTIONNAIRE
            ):
                if not session.get(
                    Questionnaire,
                    item_data.questionnaire_id,
                ):
                    raise HTTPException(
                        status_code=404,
                        detail="Опросник не найден",
                    )

            else:
                speciality = session.get(
                    Speciality,
                    item_data.speciality_id,
                )

                if not speciality:
                    raise HTTPException(
                        status_code=404,
                        detail="Специальность не найдена",
                    )

                consultation_title = (
                    item_data.consultation_title
                    or speciality.consultation_name
                    or f"Консультация: {speciality.name}"
                )

                consultation_description = (
                    item_data.consultation_description
                    if item_data.consultation_description
                    is not None
                    else speciality.consultation_description
                )

            session.add(
                ProgramStageItem(
                    stage_id=stage.id,
                    item_type=item_data.item_type,
                    order_index=item_data.order_index,
                    article_id=item_data.article_id,
                    questionnaire_id=(
                        item_data.questionnaire_id
                    ),
                    speciality_id=(
                        item_data.speciality_id
                    ),
                    consultation_title=consultation_title,
                    consultation_description=(
                        consultation_description
                    ),
                )
            )

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_item(
    *,
    session: Session,
    item: ProgramStageItem,
) -> ProgramStageItemResponse:
    if item.item_type == ProgramItemType.ARTICLE:
        article = session.get(
            Article,
            item.article_id,
        )

        if not article:
            raise HTTPException(
                status_code=409,
                detail="Статья этапа не найдена",
            )

        return ProgramStageItemResponse(
            id=item.id,
            item_type=item.item_type,
            order_index=item.order_index,
            content_id=article.id,
            title=article.title,
            description=None,
            pro_content=article.pro_content,
            is_hidden=article.is_hidden,
            speciality_id=None,
            speciality_name=None,
            can_access=True,
            is_completed=False,
            submission_id=None,
            submission_status=None,
        )

    if (
        item.item_type
        == ProgramItemType.QUESTIONNAIRE
    ):
        questionnaire = session.get(
            Questionnaire,
            item.questionnaire_id,
        )

        if not questionnaire:
            raise HTTPException(
                status_code=409,
                detail="Опросник этапа не найден",
            )

        return ProgramStageItemResponse(
            id=item.id,
            item_type=item.item_type,
            order_index=item.order_index,
            content_id=questionnaire.id,
            title=questionnaire.title,
            description=questionnaire.description,
            pro_content=questionnaire.pro_content,
            is_hidden=questionnaire.is_hidden,
            speciality_id=None,
            speciality_name=None,
            can_access=True,
            is_completed=False,
            submission_id=None,
            submission_status=None,
        )

    speciality = session.get(
        Speciality,
        item.speciality_id,
    )

    if not speciality:
        raise HTTPException(
            status_code=409,
            detail="Специальность консультации не найдена",
        )

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
    result: list[ProgramStageItemResponse] = []

    for item in sorted(
        stage.items,
        key=lambda current: current.order_index,
    ):
        serialized = serialize_item(
            session=session,
            item=item,
        )

        if serialized.is_hidden:
            continue

        if item.item_type == ProgramItemType.CONSULTATION:
            serialized.can_access = True
            serialized.is_completed = False

            result.append(serialized)
            continue

        serialized.can_access = (
            not serialized.pro_content
            or has_program_access
        )

        if (
            item.item_type
            == ProgramItemType.QUESTIONNAIRE
        ):
            submission = (
                get_program_questionnaire_submission(
                    session=session,
                    patient_id=patient.id,
                    item=item,
                )
            )

            serialized.submission_id = (
                submission.id
                if submission
                else None
            )
            serialized.submission_status = (
                submission.status
                if submission
                else None
            )
            serialized.is_completed = bool(
                submission
                and submission.status.value
                == "completed"
            )

        else:
            serialized.is_completed = (
                is_program_item_completed(
                    session=session,
                    patient_id=patient.id,
                    item=item,
                )
            )

        result.append(serialized)

    return result

def serialize_patient_program(
    *,
    session: Session,
    program: Program,
    patient: PatientProfile,
) -> ProgramPatientResponse:
    tags = get_program_tags(
        session=session,
        program_id=program.id,
    )

    access = get_patient_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    has_program_access = bool(
        access and access.is_active
    )

    enrollment = get_program_enrollment(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    elapsed_days: int | None = None
    enrollment_response = None

    if enrollment:
        started_at = normalize_datetime(
            enrollment.started_at
        )

        elapsed_days = max(
            (
                utc_now().date()
                - started_at.date()
            ).days,
            0,
        )

        enrollment_response = ProgramEnrollmentResponse(
            id=enrollment.id,
            status=enrollment.status,
            started_at=enrollment.started_at,
            completed_at=enrollment.completed_at,
            elapsed_days=elapsed_days,
        )

    _, _, program_progress = calculate_program_progress(
        session=session,
        patient_id=patient.id,
        program=program,
    )

    stages: list[ProgramStagePatientResponse] = []

    for stage in sorted(
        program.stages,
        key=lambda current: current.order_index,
    ):
        _, _, stage_progress = calculate_stage_progress(
            session=session,
            patient_id=patient.id,
            stage=stage,
        )

        stage_status = calculate_stage_status(
            session=session,
            patient_id=patient.id,
            stage=stage,
            elapsed_days=elapsed_days,
        )

        stages.append(
            ProgramStagePatientResponse(
                id=stage.id,
                title=stage.title,
                description=stage.description,
                day_from=stage.day_from,
                day_to=stage.day_to,
                order_index=stage.order_index,
                status=stage_status,
                progress_percent=stage_progress,
                items=serialize_patient_stage_items(
                    session=session,
                    stage=stage,
                    patient=patient,
                    has_program_access=(
                        has_program_access
                    ),
                ),
            )
        )

    return ProgramPatientResponse(
        id=program.id,
        title=program.title,
        description=program.description,

        service=serialize_program_service_for_patient(
            session=session,
            program=program,
        ),
        is_popular=program.is_popular,

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
    tags = get_program_tags(
        session=session,
        program_id=program.id,
    )

    stages: list[ProgramStageClinicalResponse] = []

    for stage in sorted(
        program.stages,
        key=lambda current: current.order_index,
    ):
        stages.append(
            ProgramStageClinicalResponse(
                id=stage.id,
                title=stage.title,
                description=stage.description,
                doctor_description=(
                    stage.doctor_description
                ),
                day_from=stage.day_from,
                day_to=stage.day_to,
                order_index=stage.order_index,

                # У клинического шаблона нет конкретного
                # пациента, поэтому это нейтральные значения.
                status=ProgramStageStatus.AVAILABLE,
                progress_percent=0,

                items=[
                    serialize_item(
                        session=session,
                        item=item,
                    )
                    for item in sorted(
                        stage.items,
                        key=lambda current: (
                            current.order_index
                        ),
                    )
                ],
            )
        )

    return ProgramClinicalResponse(
        id=program.id,
        title=program.title,
        description=program.description,

        service=serialize_program_service_for_staff(
            session=session,
            program=program,
        ),
        is_popular=program.is_popular,

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


@router.post(
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
    try:
        validate_program_service_choice(
            session=session,
            service_id=payload.service_id,
        )
        program = Program(
            title=payload.title.strip(),
            description=payload.description,
            is_popular=payload.is_popular,
            pro_content=False,
            created_by_user_id=auth.user.id,
        )

        session.add(program)
        session.flush()

        # Эта функция уже создаёт:
        # - теги;
        # - этапы;
        # - статьи;
        # - опросники;
        # - консультации.
        fill_program_structure(
            session=session,
            program=program,
            payload=payload,
        )

        session.commit()
        session.refresh(program)

        return serialize_clinical_program(
            session=session,
            program=program,
        )

    except Exception:
        session.rollback()
        raise

@router.get(
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
    programs = session.exec(
        select(Program).order_by(
            Program.created_at.desc()
        )
    ).all()

    return [
        serialize_clinical_program(
            session=session,
            program=program,
        )
        for program in programs
    ]


@router.get(
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
    program = session.get(Program, program_id)

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    return serialize_clinical_program(
        session=session,
        program=program,
    )


@router.get(
    "/patient",
    response_model=list[ProgramPatientResponse],
)
async def list_programs_for_patient(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[ProgramPatientResponse]:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    programs = session.exec(
        select(Program)
        .where(Program.is_hidden.is_(False))
        .order_by(Program.created_at.desc())
    ).all()

    result: list[ProgramPatientResponse] = []

    for program in programs:
        has_access = patient_has_program_access(
            session=session,
            patient_id=patient.id,
            program_id=program.id,
        )

        can_see_by_tags = patient_can_see_content(
            session=session,
            patient=patient,
            content_tag_ids=get_program_tag_ids(
                session=session,
                program_id=program.id,
            ),
            is_hidden=program.is_hidden,
        )

        if not has_access and not can_see_by_tags:
            continue

        result.append(
            serialize_patient_program(
                session=session,
                program=program,
                patient=patient,
            )
        )

    return result


@router.get(
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
    program = session.get(Program, program_id)

    if not program or program.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    has_access = patient_has_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    can_see_by_tags = patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=get_program_tag_ids(
            session=session,
            program_id=program.id,
        ),
        is_hidden=program.is_hidden,
    )

    if not has_access and not can_see_by_tags:
        raise HTTPException(
            status_code=403,
            detail="Программа недоступна пациенту",
        )

    return serialize_patient_program(
        session=session,
        program=program,
        patient=patient,
    )


@router.patch(
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
    program = session.get(Program, program_id)

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    program.is_hidden = payload.is_hidden
    program.hidden_at = (
        utc_now()
        if payload.is_hidden
        else None
    )
    program.updated_at = utc_now()

    session.add(program)
    session.commit()
    session.refresh(program)

    return serialize_clinical_program(
        session=session,
        program=program,
    )

@router.put(
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
    program = session.get(Program, program_id)

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    validate_program_service_choice(
        session=session,
        service_id=payload.service_id,
        current_service_id=program.service_id,
    )

    old_tag_links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id == program.id
        )
    ).all()

    old_stages = session.exec(
        select(ProgramStage).where(
            ProgramStage.program_id == program.id
        )
    ).all()

    for link in old_tag_links:
        session.delete(link)

    for stage in old_stages:
        session.delete(stage)

    session.flush()

    program.title = payload.title.strip()
    program.description = payload.description
    program.service_id = payload.service_id
    program.pro_content = False
    program.updated_at = utc_now()
    program.is_popular = payload.is_popular

    session.add(program)
    session.flush()

    fill_program_structure(
        session=session,
        program=program,
        payload=payload,
    )

    session.commit()
    session.refresh(program)

    return serialize_clinical_program(
        session=session,
        program=program,
    )

@router.post(
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
    program = session.get(Program, program_id)

    if not program or program.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    has_program_access = patient_has_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    if (
        not has_program_access
        and not patient_can_see_content(
            session=session,
            patient=patient,
            content_tag_ids=get_program_tag_ids(
                session=session,
                program_id=program.id,
            ),
            is_hidden=program.is_hidden,
        )
    ):
        raise HTTPException(
            status_code=403,
            detail="Программа недоступна пациенту",
        )

    enrollment = get_program_enrollment(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    if not enrollment:
        enrollment = ProgramEnrollment(
            patient_id=patient.id,
            program_id=program.id,
        )

        session.add(enrollment)
        session.flush()

        record_event(
            session=session,
            event_type=EventType.PROGRAM_STARTED,
            patient_id=patient.id,
            actor_user_id=auth.user.id,
            program_id=program.id,
            subject_type="program",
            subject_id=program.id,
        )

        session.commit()
        session.refresh(enrollment)

    return ProgramStartResponse(
        enrollment_id=enrollment.id,
        program_id=program.id,
        status=enrollment.status,
        started_at=enrollment.started_at,
    )


@router.post(
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
    program = session.get(
        Program,
        program_id,
    )

    if not program or program.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    access = get_patient_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    now = utc_now()

    if not access:
        access = PatientProgramAccess(
            patient_id=patient.id,
            program_id=program.id,
            purchase_requested=True,
            requested_at=now,
        )

    elif access.is_active:
        raise HTTPException(
            status_code=400,
            detail="Программа уже приобретена",
        )

    elif access.purchase_requested:
        return ProgramPurchaseRequestResponse(
            program_id=program.id,
            requested_at=access.requested_at,
            message=(
                "Запрос уже отправлен. "
                "Медицинский ассистент "
                "свяжется с вами."
            ),
        )

    else:
        access.purchase_requested = True
        access.requested_at = now
        access.updated_at = now

    session.add(access)
    session.commit()
    session.refresh(access)

    staff_role_links = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.role.in_(
                [
                    UserRole.SUPERUSER,
                    UserRole.MED_ASSISTANT,
                ]
            )
        )
    ).all()

    notified_user_ids: set[uuid.UUID] = set()

    for role_link in staff_role_links:
        if (
            role_link.user_id
            in notified_user_ids
        ):
            continue

        notified_user_ids.add(
            role_link.user_id
        )

        await send_notification(
            session=session,
            user_id=role_link.user_id,
            title=(
                "Запрос на покупку программы"
            ),
            message=(
                "Пациент запросил доступ "
                "к программе "
                f"«{program.title}»."
            ),
            notification_type=(
                NotificationType
                .PROGRAM_PURCHASE_REQUESTED
            ),
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url=(
                f"/patients/{patient.id}"
            ),
            payload={
                "patient_id": str(
                    patient.id
                ),
                "program_id": str(
                    program.id
                ),
            },
        )

    return ProgramPurchaseRequestResponse(
        program_id=program.id,
        requested_at=access.requested_at,
        message=(
            "Запрос отправлен. "
            "Медицинский ассистент "
            "свяжется с вами."
        ),
    )

@router.get(
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
    patient = session.get(PatientProfile, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Пациент не найден",
        )

    programs = session.exec(
        select(Program).order_by(Program.title)
    ).all()

    result: list[PatientProgramAccessItem] = []

    for program in programs:
        access = get_patient_program_access(
            session=session,
            patient_id=patient.id,
            program_id=program.id,
        )

        result.append(
            PatientProgramAccessItem(
                program_id=program.id,
                title=program.title,

                service=serialize_program_service_for_staff(
                    session=session,
                    program=program,
                ),
                is_popular=program.is_popular,

                purchase_requested=bool(
                    access
                    and access.purchase_requested
                ),

                is_hidden=program.is_hidden,
                is_active=bool(
                    access and access.is_active
                ),
                requested_at=(
                    access.requested_at
                    if access
                    else None
                ),
                activated_at=(
                    access.activated_at
                    if access
                    else None
                ),
            )
        )

    return result


@router.patch(
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
    patient = session.get(
        PatientProfile,
        patient_id,
    )

    program = session.get(
        Program,
        program_id,
    )

    if not patient or not program:
        raise HTTPException(
            status_code=404,
            detail=(
                "Пациент или программа не найдены"
            ),
        )

    access = get_patient_program_access(
        session=session,
        patient_id=patient.id,
        program_id=program.id,
    )

    now = utc_now()

    if not access:
        access = PatientProgramAccess(
            patient_id=patient.id,
            program_id=program.id,
        )

    access.is_active = payload.is_active

    # Решение по запросу принято.
    access.purchase_requested = False

    access.updated_by_user_id = auth.user.id
    access.updated_at = now

    if payload.is_active:
        access.activated_at = now
        access.deactivated_at = None
    else:
        access.deactivated_at = now

    session.add(access)
    session.commit()
    session.refresh(access)

    patient_user = session.get(
        User,
        patient.user_id,
    )

    if patient_user:
        await send_notification(
            session=session,
            user_id=patient_user.id,
            title=(
                "Программа доступна"
                if payload.is_active
                else (
                    "Доступ к программе отключён"
                )
            ),
            message=(
                "Вам открыт полный доступ "
                "к программе "
                f"«{program.title}»."
                if payload.is_active
                else (
                    "Полный доступ к программе "
                    f"«{program.title}» отключён."
                )
            ),
            notification_type=(
                NotificationType.PROGRAM_ACCESS_GRANTED
                if payload.is_active
                else NotificationType.GENERAL
            ),
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url=(
                f"/programs/{program.id}"
            ),
        )

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
    patient_response = serialize_patient_program(
        session=session,
        program=program,
        patient=patient,
    )

    clinical_stages: list[
        ProgramStageClinicalResponse
    ] = []

    patient_stages_by_id = {
        stage.id: stage
        for stage in patient_response.stages
    }

    for stage in sorted(
        program.stages,
        key=lambda current: current.order_index,
    ):
        patient_stage = patient_stages_by_id[stage.id]

        clinical_stages.append(
            ProgramStageClinicalResponse(
                id=patient_stage.id,
                title=patient_stage.title,
                description=patient_stage.description,
                doctor_description=(
                    stage.doctor_description
                ),
                day_from=patient_stage.day_from,
                day_to=patient_stage.day_to,
                order_index=patient_stage.order_index,
                status=patient_stage.status,
                progress_percent=(
                    patient_stage.progress_percent
                ),
                items=patient_stage.items,
            )
        )

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

@router.get(
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
    from app.modules.patients.utils import (
        ensure_patient_access,
    )

    ensure_patient_access(
        session=session,
        auth=auth,
        patient_id=patient_id,
    )

    patient = session.get(
        PatientProfile,
        patient_id,
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Пациент не найден",
        )

    enrollments = session.exec(
        select(ProgramEnrollment).where(
            ProgramEnrollment.patient_id
            == patient.id
        )
    ).all()

    accesses = session.exec(
        select(PatientProgramAccess).where(
            PatientProgramAccess.patient_id
            == patient.id
        )
    ).all()

    program_ids = {
        enrollment.program_id
        for enrollment in enrollments
    }

    program_ids.update(
        access.program_id
        for access in accesses
        if (
            access.is_active
            or access.purchase_requested
        )
    )

    programs: list[Program] = []

    for program_id in program_ids:
        program = session.get(Program, program_id)

        if program:
            programs.append(program)

    programs.sort(
        key=lambda item: item.title.casefold()
    )

    return [
        serialize_patient_clinical_program(
            session=session,
            program=program,
            patient=patient,
        )
        for program in programs
    ]