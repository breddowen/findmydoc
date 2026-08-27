# ./backend/app/modules/relationships/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.relationships.schemas import (
    DoctorPatientResponse,
    DoctorShortResponse,
    MessageResponse,
    PatientDoctorResponse,
    PatientRelativeResponse,
    PatientShortResponse,
    RelativePatientResponse,
    RelativeShortResponse,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    RelativePatientStatus,
    UserRole,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    RelativePatientLink,
    RelativeProfile,
    User,
)


router = APIRouter(
    prefix="/api/v1/relationships",
    tags=["Relationships"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def build_fullname(user: User) -> str:
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


def get_doctor_profile(
    *,
    session: Session,
    user_id: uuid.UUID,
) -> DoctorProfile:
    doctor = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == user_id
        )
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль врача не найден",
        )

    return doctor


def get_patient_profile(
    *,
    session: Session,
    user_id: uuid.UUID,
) -> PatientProfile:
    patient = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == user_id
        )
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль пациента не найден",
        )

    return patient


def get_relative_profile(
    *,
    session: Session,
    user_id: uuid.UUID,
) -> RelativeProfile:
    relative = session.exec(
        select(RelativeProfile).where(
            RelativeProfile.user_id == user_id
        )
    ).first()

    if not relative:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль родственника не найден",
        )

    return relative


def serialize_patient(
    *,
    session: Session,
    patient: PatientProfile,
) -> PatientShortResponse:
    user = session.get(User, patient.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У профиля пациента отсутствует пользователь",
        )

    return PatientShortResponse(
        id=patient.id,
        user_id=user.id,
        record_id=patient.record_id,
        email=user.email,
        fullname=patient.fullname or build_fullname(user),
        dob=patient.dob,
        gender=user.gender,
    )


def serialize_doctor(
    *,
    session: Session,
    doctor: DoctorProfile,
) -> DoctorShortResponse:
    user = session.get(User, doctor.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У профиля врача отсутствует пользователь",
        )

    if not doctor.speciality:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У врача отсутствует специальность",
        )

    return DoctorShortResponse(
        id=doctor.id,
        user_id=user.id,
        email=user.email,
        fullname=build_fullname(user),
        speciality_id=doctor.speciality.id,
        speciality_name=doctor.speciality.name,
    )


def serialize_relative(
    *,
    session: Session,
    relative: RelativeProfile,
) -> RelativeShortResponse:
    user = session.get(User, relative.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="У профиля родственника отсутствует пользователь",
        )

    return RelativeShortResponse(
        id=relative.id,
        user_id=user.id,
        email=user.email,
        fullname=build_fullname(user),
    )


@router.get(
    "/doctors/me/patients",
    response_model=list[DoctorPatientResponse],
)
async def list_my_patients(
    include_detached: bool = False,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> list[DoctorPatientResponse]:
    doctor = get_doctor_profile(
        session=session,
        user_id=auth.user.id,
    )

    statement = select(DoctorPatientLink).where(
        DoctorPatientLink.doctor_id == doctor.id
    )

    if not include_detached:
        statement = statement.where(
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE
        )

    links = session.exec(
        statement.order_by(
            DoctorPatientLink.created_at.desc()
        )
    ).all()

    response: list[DoctorPatientResponse] = []

    for link in links:
        patient = session.get(
            PatientProfile,
            link.patient_id,
        )

        if not patient:
            continue

        response.append(
            DoctorPatientResponse(
                link_id=link.id,
                status=link.status,
                created_at=link.created_at,
                detached_at=link.detached_at,
                patient=serialize_patient(
                    session=session,
                    patient=patient,
                ),
            )
        )

    return response


@router.delete(
    "/doctors/me/patients/{patient_id}",
    response_model=MessageResponse,
)
async def detach_patient_from_doctor(
    patient_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    doctor = get_doctor_profile(
        session=session,
        user_id=auth.user.id,
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Активная связь с пациентом не найдена",
        )

    now = utc_now()

    link.status = DoctorPatientStatus.DETACHED
    link.detached_at = now
    link.updated_at = now

    session.add(link)
    session.commit()

    return MessageResponse(
        message="Пациент отвязан от врача"
    )


@router.get(
    "/patients/me/doctors",
    response_model=list[PatientDoctorResponse],
)
async def list_my_doctors(
    include_detached: bool = False,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[PatientDoctorResponse]:
    patient = get_patient_profile(
        session=session,
        user_id=auth.user.id,
    )

    statement = select(DoctorPatientLink).where(
        DoctorPatientLink.patient_id == patient.id
    )

    if not include_detached:
        statement = statement.where(
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE
        )

    links = session.exec(
        statement.order_by(
            DoctorPatientLink.created_at.desc()
        )
    ).all()

    response: list[PatientDoctorResponse] = []

    for link in links:
        doctor = session.get(
            DoctorProfile,
            link.doctor_id,
        )

        if not doctor:
            continue

        response.append(
            PatientDoctorResponse(
                link_id=link.id,
                status=link.status,
                created_at=link.created_at,
                detached_at=link.detached_at,
                doctor=serialize_doctor(
                    session=session,
                    doctor=doctor,
                ),
            )
        )

    return response


@router.get(
    "/patients/me/relatives",
    response_model=list[PatientRelativeResponse],
)
async def list_my_relatives(
    include_detached: bool = False,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[PatientRelativeResponse]:
    patient = get_patient_profile(
        session=session,
        user_id=auth.user.id,
    )

    statement = select(RelativePatientLink).where(
        RelativePatientLink.patient_id == patient.id
    )

    if not include_detached:
        statement = statement.where(
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE
        )

    links = session.exec(
        statement.order_by(
            RelativePatientLink.created_at.desc()
        )
    ).all()

    response: list[PatientRelativeResponse] = []

    for link in links:
        relative = session.get(
            RelativeProfile,
            link.relative_id,
        )

        if not relative:
            continue

        response.append(
            PatientRelativeResponse(
                link_id=link.id,
                relationship_degree=link.relationship_degree,
                status=link.status,
                created_at=link.created_at,
                detached_at=link.detached_at,
                relative=serialize_relative(
                    session=session,
                    relative=relative,
                ),
            )
        )

    return response


@router.delete(
    "/patients/me/relatives/{relative_id}",
    response_model=MessageResponse,
)
async def detach_my_relative(
    relative_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    patient = get_patient_profile(
        session=session,
        user_id=auth.user.id,
    )

    link = session.exec(
        select(RelativePatientLink).where(
            RelativePatientLink.patient_id == patient.id,
            RelativePatientLink.relative_id == relative_id,
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE,
        )
    ).first()

    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Активная связь с родственником не найдена",
        )

    now = utc_now()

    link.status = RelativePatientStatus.DETACHED
    link.detached_at = now
    link.updated_at = now

    session.add(link)
    session.commit()

    return MessageResponse(
        message="Родственник отвязан от пациента"
    )


@router.get(
    "/relatives/me/patients",
    response_model=list[RelativePatientResponse],
)
async def list_related_patients(
    include_detached: bool = False,
    auth: AuthContext = Depends(
        require_roles(UserRole.RELATIVE)
    ),
    session: Session = Depends(get_session),
) -> list[RelativePatientResponse]:
    relative = get_relative_profile(
        session=session,
        user_id=auth.user.id,
    )

    statement = select(RelativePatientLink).where(
        RelativePatientLink.relative_id == relative.id
    )

    if not include_detached:
        statement = statement.where(
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE
        )

    links = session.exec(
        statement.order_by(
            RelativePatientLink.created_at.desc()
        )
    ).all()

    response: list[RelativePatientResponse] = []

    for link in links:
        patient = session.get(
            PatientProfile,
            link.patient_id,
        )

        if not patient:
            continue

        response.append(
            RelativePatientResponse(
                link_id=link.id,
                relationship_degree=link.relationship_degree,
                status=link.status,
                created_at=link.created_at,
                detached_at=link.detached_at,
                patient=serialize_patient(
                    session=session,
                    patient=patient,
                ),
            )
        )

    return response


@router.delete(
    "/doctors/me/patients/{patient_id}/relatives/{relative_id}",
    response_model=MessageResponse,
)
async def detach_patient_relative_by_doctor(
    patient_id: uuid.UUID,
    relative_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.DOCTOR)
    ),
    session: Session = Depends(get_session),
) -> MessageResponse:
    doctor = get_doctor_profile(
        session=session,
        user_id=auth.user.id,
    )

    doctor_patient_link = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.doctor_id == doctor.id,
            DoctorPatientLink.patient_id == patient_id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).first()

    if not doctor_patient_link:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Врач не связан с этим пациентом",
        )

    relative_link = session.exec(
        select(RelativePatientLink).where(
            RelativePatientLink.patient_id == patient_id,
            RelativePatientLink.relative_id == relative_id,
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE,
        )
    ).first()

    if not relative_link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Активная связь с родственником не найдена",
        )

    now = utc_now()

    relative_link.status = RelativePatientStatus.DETACHED
    relative_link.detached_at = now
    relative_link.updated_at = now

    session.add(relative_link)
    session.commit()

    return MessageResponse(
        message="Родственник отвязан от пациента"
    )