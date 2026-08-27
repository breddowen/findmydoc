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

router = APIRouter(
    prefix="/api/v1/questionnaires",
    tags=["Questionnaires"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_questionnaire(
    *,
    session: Session,
    questionnaire: Questionnaire,
) -> QuestionnaireResponse:
    tags = get_questionnaire_tags(
        session=session,
        questionnaire_id=questionnaire.id,
    )

    questions = sorted(
        questionnaire.questions,
        key=lambda item: item.order_index,
    )

    return QuestionnaireResponse(
        id=questionnaire.id,
        title=questionnaire.title,
        description=questionnaire.description,
        pro_content=questionnaire.pro_content,
        is_hidden=questionnaire.is_hidden,
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
    if len({
        item.order_index
        for item in payload.questions
    }) != len(payload.questions):
        raise HTTPException(
            status_code=422,
            detail="Порядок вопросов должен быть уникальным",
        )

    for tag_id in dict.fromkeys(payload.tag_ids):
        if not session.get(Tag, tag_id):
            raise HTTPException(
                status_code=404,
                detail=f"Тег {tag_id} не найден",
            )

    questionnaire = Questionnaire(
        title=payload.title.strip(),
        description=payload.description,
        pro_content=payload.pro_content,
        copied_from_id=copied_from_id,
        created_by_user_id=created_by_user_id,
    )

    session.add(questionnaire)
    session.flush()

    for tag_id in dict.fromkeys(payload.tag_ids):
        session.add(
            QuestionnaireTagLink(
                questionnaire_id=questionnaire.id,
                tag_id=tag_id,
            )
        )

    for question_data in payload.questions:
        question = Question(
            questionnaire_id=questionnaire.id,
            question_type=question_data.question_type,
            text=question_data.text,
            is_required=question_data.is_required,
            order_index=question_data.order_index,
            scale_min=question_data.scale_min,
            scale_max=question_data.scale_max,
            scale_min_label=question_data.scale_min_label,
            scale_max_label=question_data.scale_max_label,
        )

        session.add(question)
        session.flush()

        for option_data in question_data.options:
            session.add(
                QuestionOption(
                    question_id=question.id,
                    text=option_data.text,
                    order_index=option_data.order_index,
                )
            )

    return questionnaire


@router.get("", response_model=list[QuestionnaireListItem])
async def list_questionnaires(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[QuestionnaireListItem]:
    questionnaires = session.exec(
        select(Questionnaire).order_by(
            Questionnaire.created_at.desc()
        )
    ).all()

    patient = None

    if auth.active_role == UserRole.PATIENT:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

    result: list[QuestionnaireListItem] = []

    for questionnaire in questionnaires:
        tag_ids = get_questionnaire_tag_ids(
            session=session,
            questionnaire_id=questionnaire.id,
        )

        if patient and not patient_can_access_content(
            session=session,
            patient=patient,
            content_tag_ids=tag_ids,
            pro_content=questionnaire.pro_content,
            is_hidden=questionnaire.is_hidden,
        ):
            continue

        tags = get_questionnaire_tags(
            session=session,
            questionnaire_id=questionnaire.id,
        )

        result.append(
            QuestionnaireListItem(
                id=questionnaire.id,
                title=questionnaire.title,
                description=questionnaire.description,
                pro_content=questionnaire.pro_content,
                is_hidden=questionnaire.is_hidden,
                tags=[
                    QuestionnaireTagResponse(
                        id=tag.id,
                        name=tag.name,
                        description=tag.description,
                    )
                    for tag in tags
                ],
                questions_count=len(
                    questionnaire.questions
                ),
                created_at=questionnaire.created_at,
            )
        )

    return result


@router.get(
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
    questionnaire = session.get(
        Questionnaire,
        questionnaire_id,
    )

    if not questionnaire:
        raise HTTPException(
            status_code=404,
            detail="Опросник не найден",
        )

    if auth.active_role == UserRole.PATIENT:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        if program_id:
            from app.modules.programs.enums import (
                ProgramItemType,
            )
            from app.modules.programs.utils import (
                ensure_patient_program_content_access,
            )

            ensure_patient_program_content_access(
                session=session,
                patient=patient,
                program_id=program_id,
                stage_id=program_stage_id,
                content_type=(
                    ProgramItemType.QUESTIONNAIRE
                ),
                content_id=questionnaire.id,
                pro_content=(
                    questionnaire.pro_content
                ),
            )
        else:
            ensure_patient_content_access(
                session=session,
                patient=patient,
                content_tag_ids=(
                    get_questionnaire_tag_ids(
                        session=session,
                        questionnaire_id=(
                            questionnaire.id
                        ),
                    )
                ),
                pro_content=(
                    questionnaire.pro_content
                ),
                is_hidden=questionnaire.is_hidden,
            )

    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )

@router.post(
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
    questionnaire = create_questionnaire_from_payload(
        session=session,
        payload=payload,
        created_by_user_id=auth.user.id,
        copied_from_id=payload.copied_from_id,
    )

    session.commit()
    session.refresh(questionnaire)

    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )


@router.post(
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
    source = session.get(
        Questionnaire,
        questionnaire_id,
    )

    if not source:
        raise HTTPException(
            status_code=404,
            detail="Опросник не найден",
        )

    source_response = serialize_questionnaire(
        session=session,
        questionnaire=source,
    )

    payload_data = QuestionnaireCreateRequest(
        title=(
            payload.title.strip()
            if payload.title
            else f"{source.title} — копия"
        ),
        description=source.description,
        tag_ids=[
            tag.id
            for tag in source_response.tags
        ],
        pro_content=source.pro_content,
        questions=[
            {
                "question_type": question.question_type,
                "text": question.text,
                "is_required": question.is_required,
                "order_index": question.order_index,
                "scale_min": question.scale_min,
                "scale_max": question.scale_max,
                "scale_min_label": (
                    question.scale_min_label
                ),
                "scale_max_label": (
                    question.scale_max_label
                ),
                "options": [
                    {
                        "text": option.text,
                        "order_index": (
                            option.order_index
                        ),
                    }
                    for option in question.options
                ],
            }
            for question in source_response.questions
        ],
    )

    copy = create_questionnaire_from_payload(
        session=session,
        payload=payload_data,
        created_by_user_id=auth.user.id,
        copied_from_id=source.id,
    )

    session.commit()
    session.refresh(copy)

    return serialize_questionnaire(
        session=session,
        questionnaire=copy,
    )


@router.patch(
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
    questionnaire = session.get(
        Questionnaire,
        questionnaire_id,
    )

    if not questionnaire:
        raise HTTPException(
            status_code=404,
            detail="Опросник не найден",
        )

    questionnaire.is_hidden = payload.is_hidden
    questionnaire.hidden_at = (
        utc_now()
        if payload.is_hidden
        else None
    )

    session.add(questionnaire)
    session.commit()
    session.refresh(questionnaire)

    return serialize_questionnaire(
        session=session,
        questionnaire=questionnaire,
    )


@router.post(
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
    questionnaire = session.get(
        Questionnaire,
        questionnaire_id,
    )

    if not questionnaire:
        raise HTTPException(
            status_code=404,
            detail="Опросник не найден",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    # Скрытие имеет приоритет над всеми
    # способами доступа.
    if questionnaire.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Опросник скрыт",
        )

    if (program_id is None) != (
        program_stage_id is None
    ):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=(
                "program_id и program_stage_id "
                "должны передаваться вместе"
            ),
        )

    # Для контента программы проверяем доступ
    # только в контексте программы.
    #
    # Глобальные правила доступа здесь повторно
    # не применяются.
    if program_id is not None:
        from app.modules.programs.enums import (
            ProgramItemType,
        )
        from app.modules.programs.utils import (
            ensure_patient_program_content_access,
        )

        ensure_patient_program_content_access(
            session=session,
            patient=patient,
            program_id=program_id,
            stage_id=program_stage_id,
            content_type=(
                ProgramItemType.QUESTIONNAIRE
            ),
            content_id=questionnaire.id,
            pro_content=questionnaire.pro_content,
        )
    else:
        # Вне программы активное назначение даёт
        # доступ к опроснику без дополнительной
        # глобальной проверки контента.
        is_assigned = patient_has_active_assignment(
            session=session,
            patient_id=patient.id,
            assignment_type=(
                AssignmentType.QUESTIONNAIRE
            ),
            content_id=questionnaire.id,
        )

        if not is_assigned:
            ensure_patient_content_access(
                session=session,
                patient=patient,
                content_tag_ids=(
                    get_questionnaire_tag_ids(
                        session=session,
                        questionnaire_id=(
                            questionnaire.id
                        ),
                    )
                ),
                pro_content=questionnaire.pro_content,
                is_hidden=questionnaire.is_hidden,
            )

    # Повторный запуск одного и того же опросника
    # в том же контексте возвращает существующую
    # незавершённую попытку.
    existing_submission = session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient.id,
            QuestionnaireSubmission.questionnaire_id
            == questionnaire.id,
            QuestionnaireSubmission.program_id
            == program_id,
            QuestionnaireSubmission.program_stage_id
            == program_stage_id,
            QuestionnaireSubmission.status
            == QuestionnaireSubmissionStatus.IN_PROGRESS,
        )
        .order_by(
            QuestionnaireSubmission.started_at.desc()
        )
    ).first()

    if existing_submission:
        return SubmissionStartResponse(
            submission_id=existing_submission.id,
            questionnaire_id=(
                existing_submission.questionnaire_id
            ),
            status=existing_submission.status,
            started_at=existing_submission.started_at,
        )

    submission = QuestionnaireSubmission(
        questionnaire_id=questionnaire.id,
        patient_id=patient.id,
        program_id=program_id,
        program_stage_id=program_stage_id,
    )

    session.add(submission)
    session.flush()

    record_event(
        session=session,
        event_type=EventType.QUESTIONNAIRE_STARTED,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        program_id=program_id,
        subject_type="questionnaire",
        subject_id=questionnaire.id,
        metadata={
            "submission_id": str(submission.id),
            "program_stage_id": (
                str(program_stage_id)
                if program_stage_id
                else None
            ),
        },
    )

    # Если опросник был назначен пациенту,
    # назначение переходит в состояние in progress.
    #
    # Функция безопасно ничего не делает,
    # если активного назначения нет.
    mark_assignment_in_progress(
        session=session,
        patient_id=patient.id,
        assignment_type=(
            AssignmentType.QUESTIONNAIRE
        ),
        content_id=questionnaire.id,
    )

    session.commit()
    session.refresh(submission)

    return SubmissionStartResponse(
        submission_id=submission.id,
        questionnaire_id=questionnaire.id,
        status=submission.status,
        started_at=submission.started_at,
    )


@router.post(
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
    submission = session.get(
        QuestionnaireSubmission,
        submission_id,
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Попытка не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    

    if submission.patient_id != patient.id:
        raise HTTPException(
            status_code=403,
            detail=(
                "Это прохождение принадлежит "
                "другому пациенту"
            ),
        )

    if (
        submission.status
        == QuestionnaireSubmissionStatus.COMPLETED
    ):
        raise HTTPException(
            status_code=400,
            detail="Опросник уже заполнен",
        )

    questionnaire = session.get(
        Questionnaire,
        submission.questionnaire_id,
    )

    if not questionnaire:
        raise HTTPException(
            status_code=409,
            detail="Опросник больше не существует",
        )

    normalized_answers = (
        validate_questionnaire_answers(
            questionnaire=questionnaire,
            answers=payload.answers,
        )
    )

    for (
        question_id,
        value,
    ) in normalized_answers.items():
        existing_answer = session.exec(
            select(QuestionAnswer).where(
                QuestionAnswer.submission_id
                == submission.id,
                QuestionAnswer.question_id
                == question_id,
            )
        ).first()

        if existing_answer:
            existing_answer.value_json = value
            existing_answer.created_at = utc_now()

            session.add(existing_answer)
        else:
            session.add(
                QuestionAnswer(
                    submission_id=submission.id,
                    question_id=question_id,
                    value_json=value,
                )
            )

    submission.status = (
        QuestionnaireSubmissionStatus.COMPLETED
    )
    submission.completed_at = utc_now()

    session.add(submission)

    record_event(
        session=session,
        event_type=EventType.QUESTIONNAIRE_COMPLETED,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        program_id=submission.program_id,
        subject_type="questionnaire",
        subject_id=questionnaire.id,
        metadata={
            "submission_id": str(submission.id),
            "program_stage_id": (
                str(submission.program_stage_id)
                if submission.program_stage_id
                else None
            ),
        },
    )

    mark_assignment_completed(
        session=session,
        patient_id=patient.id,
        assignment_type=(
            AssignmentType.QUESTIONNAIRE
        ),
        content_id=questionnaire.id,
    )

    # Синхронизируем прогресс программ после
    # завершения опросника и назначения.
    #
    # program_in_progress и program_completed
    # создаются однократно благодаря
    # in_progress_event_at / completed_event_at.
    sync_patient_program_enrollments(
        session=session,
        patient_id=patient.id,
    )

    # Сохраняем одной транзакцией:
    # - ответы;
    # - завершение submission;
    # - событие questionnaire_completed;
    # - завершение assignment;
    # - состояние программы и её события.
    session.commit()
    session.refresh(submission)

    # После успешного commit уведомляем
    # активных врачей пациента.
    doctor_links = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.patient_id
            == patient.id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).all()

    for doctor_link in doctor_links:
        doctor = session.get(
            DoctorProfile,
            doctor_link.doctor_id,
        )

        if not doctor:
            continue

        await send_notification(
            session=session,
            user_id=doctor.user_id,
            title="Опросник завершён",
            message=(
                "Пациент завершил опросник "
                f"«{questionnaire.title}»."
            ),
            notification_type=(
                NotificationType.QUESTIONNAIRE_COMPLETED
            ),
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url=(
                f"/patients/{patient.id}"
                f"/questionnaires/{submission.id}"
            ),
            payload={
                "patient_id": str(patient.id),
                "questionnaire_id": str(
                    questionnaire.id
                ),
                "submission_id": str(
                    submission.id
                ),
            },
        )

    answers = session.exec(
        select(QuestionAnswer).where(
            QuestionAnswer.submission_id
            == submission.id
        )
    ).all()

    response_answers: list[AnswerResponse] = []

    for answer in answers:
        question = session.get(
            Question,
            answer.question_id,
        )

        if not question:
            continue

        response_answers.append(
            AnswerResponse(
                question_id=question.id,
                question_text=question.text,
                question_type=question.question_type,
                value=answer.value_json,
            )
        )

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

@router.put(
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
    submission = session.get(
        QuestionnaireSubmission,
        submission_id,
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Попытка прохождения не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    if submission.patient_id != patient.id:
        raise HTTPException(
            status_code=403,
            detail="Попытка принадлежит другому пациенту",
        )

    if (
        submission.status
        == QuestionnaireSubmissionStatus.COMPLETED
    ):
        raise HTTPException(
            status_code=400,
            detail="Завершённый опросник изменить нельзя",
        )

    question = session.get(
        Question,
        payload.question_id,
    )

    if (
        not question
        or question.questionnaire_id
        != submission.questionnaire_id
    ):
        raise HTTPException(
            status_code=404,
            detail="Вопрос не найден в этом опроснике",
        )

    normalized_value = normalize_question_answer(
        question=question,
        value=payload.value,
    )

    answer = session.exec(
        select(QuestionAnswer).where(
            QuestionAnswer.submission_id
            == submission.id,
            QuestionAnswer.question_id
            == question.id,
        )
    ).first()

    now = utc_now()

    if answer:
        answer.value_json = normalized_value
        answer.created_at = now
    else:
        answer = QuestionAnswer(
            submission_id=submission.id,
            question_id=question.id,
            value_json=normalized_value,
            created_at=now,
        )

    session.add(answer)
    session.commit()
    session.refresh(answer)

    return AnswerSaveResponse(
        submission_id=submission.id,
        question_id=question.id,
        value=answer.value_json,
        saved_at=answer.created_at,
    )

@router.get(
    "/submissions/mine/progress",
    response_model=list[SubmissionProgressItem],
)
async def get_my_questionnaire_progress(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[SubmissionProgressItem]:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    submissions = session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient.id
        )
        .order_by(
            QuestionnaireSubmission.started_at.desc()
        )
    ).all()

    result: list[SubmissionProgressItem] = []

    for submission in submissions:
        questionnaire = session.get(
            Questionnaire,
            submission.questionnaire_id,
        )

        if not questionnaire:
            continue

        answers_count = len(
            session.exec(
                select(QuestionAnswer).where(
                    QuestionAnswer.submission_id
                    == submission.id
                )
            ).all()
        )

        questions_count = len(
            questionnaire.questions
        )

        progress_percent = (
            round(
                answers_count / questions_count * 100,
                2,
            )
            if questions_count
            else 0
        )

        result.append(
            SubmissionProgressItem(
                submission_id=submission.id,
                questionnaire_id=questionnaire.id,
                questionnaire_title=questionnaire.title,
                status=submission.status,
                answered_questions=answers_count,
                questions_count=questions_count,
                progress_percent=progress_percent,
                started_at=submission.started_at,
                completed_at=submission.completed_at,
                program_id=submission.program_id,
                program_stage_id=submission.program_stage_id,
            )
        )

    return result

@router.get(
    "/submissions/{submission_id}",
    response_model=SubmissionResponse,
)
async def get_submission(
    submission_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> SubmissionResponse:
    submission = session.get(
        QuestionnaireSubmission,
        submission_id,
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Попытка не найдена",
        )

    if auth.active_role == UserRole.PATIENT:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        if submission.patient_id != patient.id:
            raise HTTPException(
                status_code=403,
                detail="Нет доступа к этой попытке",
            )

    elif auth.active_role == UserRole.DOCTOR:
        from app.modules.users.enums import DoctorPatientStatus
        from app.modules.users.models import (
            DoctorPatientLink,
            DoctorProfile,
        )

        doctor = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == auth.user.id
            )
        ).first()

        link = (
            session.exec(
                select(DoctorPatientLink).where(
                    DoctorPatientLink.doctor_id
                    == doctor.id,
                    DoctorPatientLink.patient_id
                    == submission.patient_id,
                    DoctorPatientLink.status
                    == DoctorPatientStatus.ACTIVE,
                )
            ).first()
            if doctor
            else None
        )

        if not link:
            raise HTTPException(
                status_code=403,
                detail="Врач не связан с этим пациентом",
            )

    elif auth.active_role not in {
        UserRole.SUPERUSER,
        UserRole.MED_ASSISTANT,
    }:
        raise HTTPException(
            status_code=403,
            detail="Нет доступа к результату",
        )

    questionnaire = session.get(
        Questionnaire,
        submission.questionnaire_id,
    )

    answers = session.exec(
        select(QuestionAnswer).where(
            QuestionAnswer.submission_id
            == submission.id
        )
    ).all()

    response_answers: list[AnswerResponse] = []

    for answer in answers:
        question = session.get(
            Question,
            answer.question_id,
        )

        if not question:
            continue

        response_answers.append(
            AnswerResponse(
                question_id=question.id,
                question_text=question.text,
                question_type=question.question_type,
                value=answer.value_json,
            )
        )

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