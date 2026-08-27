# ./backend/app/modules/patients/routers.py
import math
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, or_
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.articles.models import (
    Article,
    ArticleProgress,
)
from app.modules.events.models import Event
from app.modules.patients.schemas import (
    PatientArticleProgressItem,
    PatientDetailResponse,
    PatientDoctorItem,
    PatientEventItem,
    PatientListItem,
    PatientPageResponse,
    PatientProResponse,
    PatientProUpdateRequest,
    PatientQuestionnaireProgressItem,
)
from app.modules.patients.utils import (
    build_user_fullname,
    ensure_patient_access,
    get_contact_preference,
    get_current_doctor_profile,
    get_last_patient_activity,
    get_registration_status,
)
from app.modules.questionnaires.models import (
    QuestionAnswer,
    Questionnaire,
    QuestionnaireSubmission,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    UserRole,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    User,
)


router = APIRouter(
    prefix="/api/v1/patients",
    tags=["Patients"],
)


def serialize_patient_list_item(
    *,
    session: Session,
    patient: PatientProfile,
) -> PatientListItem:
    user = session.get(User, patient.user_id)

    if not user:
        raise HTTPException(
            status_code=409,
            detail="У пациента отсутствует пользователь",
        )

    preference = get_contact_preference(
        session=session,
        patient_id=patient.id,
    )

    doctors_count = session.exec(
        select(func.count())
        .select_from(DoctorPatientLink)
        .where(
            DoctorPatientLink.patient_id == patient.id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).one()

    return PatientListItem(
        patient_id=patient.id,
        user_id=user.id,
        record_id=patient.record_id,
        email=user.email,
        fullname=build_user_fullname(
            user=user,
            patient=patient,
        ),
        dob=patient.dob,
        gender=user.gender,
        registration_status=get_registration_status(
            user
        ),
        registered_at=user.created_at,
        last_activity_at=get_last_patient_activity(
            session=session,
            patient=patient,
            user=user,
        ),
        assistant_contact_allowed=bool(
            preference
            and preference.allow_assistant_contact
            and not preference.do_not_call
        ),
        do_not_call=bool(
            preference and preference.do_not_call
        ),
        pro_enabled=patient.pro_enabled,
        doctors_count=int(doctors_count),
    )


@router.get("", response_model=PatientPageResponse)
async def list_patients(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    search: str | None = Query(
        default=None,
        max_length=200,
    ),
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> PatientPageResponse:
    statement = (
        select(PatientProfile)
        .join(User, User.id == PatientProfile.user_id)
    )

    count_statement = (
        select(func.count())
        .select_from(PatientProfile)
        .join(User, User.id == PatientProfile.user_id)
    )

    if auth.active_role == UserRole.DOCTOR:
        doctor = get_current_doctor_profile(
            session=session,
            auth=auth,
        )

        statement = (
            statement
            .join(
                DoctorPatientLink,
                DoctorPatientLink.patient_id
                == PatientProfile.id,
            )
            .where(
                DoctorPatientLink.doctor_id
                == doctor.id,
                DoctorPatientLink.status
                == DoctorPatientStatus.ACTIVE,
            )
        )

        count_statement = (
            count_statement
            .join(
                DoctorPatientLink,
                DoctorPatientLink.patient_id
                == PatientProfile.id,
            )
            .where(
                DoctorPatientLink.doctor_id
                == doctor.id,
                DoctorPatientLink.status
                == DoctorPatientStatus.ACTIVE,
            )
        )

    normalized_search = (
        search.strip()
        if search
        else None
    )

    if normalized_search:
        search_filter = or_(
            User.email.contains(normalized_search),
            PatientProfile.record_id.contains(
                normalized_search
            ),
            PatientProfile.fullname.contains(
                normalized_search
            ),
            User.first_name.contains(
                normalized_search
            ),
            User.last_name.contains(
                normalized_search
            ),
        )

        statement = statement.where(search_filter)
        count_statement = count_statement.where(
            search_filter
        )

    total_items = int(
        session.exec(count_statement).one()
    )

    patients = session.exec(
        statement
        .order_by(User.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    ).all()

    total_pages = max(
        1,
        math.ceil(total_items / page_size),
    )

    return PatientPageResponse(
        items=[
            serialize_patient_list_item(
                session=session,
                patient=patient,
            )
            for patient in patients
        ],
        page=page,
        page_size=page_size,
        total_items=total_items,
        total_pages=total_pages,
    )


@router.get(
    "/{patient_id}",
    response_model=PatientDetailResponse,
)
async def get_patient_detail(
    patient_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> PatientDetailResponse:
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

    user = session.get(User, patient.user_id)

    if not user:
        raise HTTPException(
            status_code=409,
            detail="У пациента отсутствует пользователь",
        )

    summary = serialize_patient_list_item(
        session=session,
        patient=patient,
    )

    doctor_links = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.patient_id == patient.id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).all()

    doctors: list[PatientDoctorItem] = []

    for link in doctor_links:
        doctor = session.get(
            DoctorProfile,
            link.doctor_id,
        )

        if (
            not doctor
            or not doctor.user
            or not doctor.speciality
        ):
            continue

        doctors.append(
            PatientDoctorItem(
                doctor_id=doctor.id,
                user_id=doctor.user.id,
                fullname=build_user_fullname(
                    user=doctor.user
                ),
                email=doctor.user.email,
                speciality_id=doctor.speciality.id,
                speciality_name=doctor.speciality.name,
                linked_at=link.created_at,
            )
        )

    article_progress_rows = session.exec(
        select(ArticleProgress)
        .where(
            ArticleProgress.patient_id == patient.id
        )
        .order_by(ArticleProgress.updated_at.desc())
    ).all()

    articles: list[PatientArticleProgressItem] = []

    for progress in article_progress_rows:
        article = session.get(
            Article,
            progress.article_id,
        )

        if not article:
            continue

        articles.append(
            PatientArticleProgressItem(
                article_id=article.id,
                title=article.title,
                progress_percent=(
                    progress.progress_percent
                ),
                max_progress_percent=(
                    progress.max_progress_percent
                ),
                started_at=progress.started_at,
                updated_at=progress.updated_at,
                completed_at=progress.completed_at,
            )
        )

    submissions = session.exec(
        select(QuestionnaireSubmission)
        .where(
            QuestionnaireSubmission.patient_id
            == patient.id,
            QuestionnaireSubmission.program_id.is_(None),
        )
        .order_by(
            QuestionnaireSubmission.started_at.desc()
        )
    ).all()

    questionnaires: list[
        PatientQuestionnaireProgressItem
    ] = []

    for submission in submissions:
        questionnaire = session.get(
            Questionnaire,
            submission.questionnaire_id,
        )

        if not questionnaire:
            continue

        answered_questions = len(
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
                answered_questions
                / questions_count
                * 100,
                2,
            )
            if questions_count
            else 0
        )

        questionnaires.append(
            PatientQuestionnaireProgressItem(
                submission_id=submission.id,
                questionnaire_id=questionnaire.id,
                questionnaire_title=(
                    questionnaire.title
                ),
                status=submission.status,
                answered_questions=answered_questions,
                questions_count=questions_count,
                progress_percent=progress_percent,
                started_at=submission.started_at,
                completed_at=submission.completed_at,
            )
        )

    events = session.exec(
        select(Event)
        .where(Event.patient_id == patient.id)
        .order_by(Event.occurred_at.desc())
        .limit(30)
    ).all()

    return PatientDetailResponse(
        patient_id=summary.patient_id,
        user_id=summary.user_id,
        record_id=summary.record_id,
        email=summary.email,
        fullname=summary.fullname,
        dob=summary.dob,
        gender=summary.gender,
        registration_status=(
            summary.registration_status
        ),
        registered_at=summary.registered_at,
        last_activity_at=summary.last_activity_at,
        assistant_contact_allowed=(
            summary.assistant_contact_allowed
        ),
        do_not_call=summary.do_not_call,
        pro_enabled=summary.pro_enabled,
        doctors=doctors,
        articles=articles,
        questionnaires=questionnaires,
        recent_events=[
            PatientEventItem(
                id=event.id,
                event_type=event.event_type,
                subject_type=event.subject_type,
                subject_id=event.subject_id,
                metadata=event.metadata_json,
                occurred_at=event.occurred_at,
            )
            for event in events
        ],
    )


@router.patch(
    "/{patient_id}/pro",
    response_model=PatientProResponse,
)
async def update_patient_pro(
    patient_id: uuid.UUID,
    payload: PatientProUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> PatientProResponse:
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

    patient.pro_enabled = payload.pro_enabled

    session.add(patient)
    session.commit()
    session.refresh(patient)

    return PatientProResponse(
        patient_id=patient.id,
        pro_enabled=patient.pro_enabled,
    )