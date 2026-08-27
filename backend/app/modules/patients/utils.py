# ./backend/app/modules/patients/utils.py
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlmodel import Session, select

from app.core.security import AuthContext
from app.modules.articles.models import ArticleProgress
from app.modules.consents.models import (
    ConsentRecord,
    ContactPreference,
)
from app.modules.events.models import Event
from app.modules.patients.enums import (
    PatientRegistrationStatus,
)
from app.modules.questionnaires.models import (
    QuestionAnswer,
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


def normalize_datetime(
    value: datetime | None,
) -> datetime | None:
    if value is None:
        return None

    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value


def build_user_fullname(
    *,
    user: User,
    patient: PatientProfile | None = None,
) -> str:
    if patient and patient.fullname:
        return patient.fullname

    return (
        " ".join(
            part
            for part in [
                user.last_name,
                user.first_name,
                user.middle_name,
            ]
            if part
        )
        or user.email
    )


def get_registration_status(
    user: User,
) -> PatientRegistrationStatus:
    if user.email_verified_at is not None:
        return PatientRegistrationStatus.REGISTERED

    return PatientRegistrationStatus.EMAIL_NOT_VERIFIED


def get_contact_preference(
    *,
    session: Session,
    patient_id: uuid.UUID,
) -> ContactPreference | None:
    return session.exec(
        select(ContactPreference).where(
            ContactPreference.patient_id == patient_id
        )
    ).first()


def get_last_patient_activity(
    *,
    session: Session,
    patient: PatientProfile,
    user: User,
) -> datetime:
    values: list[datetime] = [
        normalize_datetime(user.created_at),
    ]

    event_activity = session.exec(
        select(func.max(Event.occurred_at)).where(
            Event.patient_id == patient.id
        )
    ).one()

    article_activity = session.exec(
        select(
            func.max(ArticleProgress.updated_at)
        ).where(
            ArticleProgress.patient_id == patient.id
        )
    ).one()

    submission_started = session.exec(
        select(
            func.max(
                QuestionnaireSubmission.started_at
            )
        ).where(
            QuestionnaireSubmission.patient_id
            == patient.id
        )
    ).one()

    submission_completed = session.exec(
        select(
            func.max(
                QuestionnaireSubmission.completed_at
            )
        ).where(
            QuestionnaireSubmission.patient_id
            == patient.id
        )
    ).one()

    answer_activity = session.exec(
        select(func.max(QuestionAnswer.created_at))
        .join(
            QuestionnaireSubmission,
            QuestionnaireSubmission.id
            == QuestionAnswer.submission_id,
        )
        .where(
            QuestionnaireSubmission.patient_id
            == patient.id
        )
    ).one()

    consent_activity = session.exec(
        select(
            func.max(ConsentRecord.created_at)
        ).where(
            ConsentRecord.patient_id == patient.id
        )
    ).one()

    optional_values = [
        event_activity,
        article_activity,
        submission_started,
        submission_completed,
        answer_activity,
        consent_activity,
    ]

    for value in optional_values:
        normalized = normalize_datetime(value)

        if normalized:
            values.append(normalized)

    return max(values)


def get_current_doctor_profile(
    *,
    session: Session,
    auth: AuthContext,
) -> DoctorProfile:
    doctor = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == auth.user.id
        )
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль врача не найден",
        )

    return doctor


def ensure_patient_access(
    *,
    session: Session,
    auth: AuthContext,
    patient_id: uuid.UUID,
) -> None:
    if auth.active_role in {
        UserRole.SUPERUSER,
        UserRole.MED_ASSISTANT,
    }:
        return

    if auth.active_role != UserRole.DOCTOR:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Нет доступа к пациенту",
        )

    doctor = get_current_doctor_profile(
        session=session,
        auth=auth,
    )

    link = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.doctor_id == doctor.id,
            DoctorPatientLink.patient_id == patient_id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).first()

    if not link:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Врач не связан с этим пациентом",
        )