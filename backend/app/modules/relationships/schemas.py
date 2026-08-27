# ./backend/app/modules/relationships/schemas.py
import uuid
from datetime import date, datetime

from pydantic import BaseModel, EmailStr

from app.modules.users.enums import (
    DoctorPatientStatus,
    Gender,
    RelativePatientStatus,
)


class PatientShortResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    record_id: str
    email: EmailStr
    fullname: str | None
    dob: date | None
    gender: Gender | None


class DoctorPatientResponse(BaseModel):
    link_id: uuid.UUID
    status: DoctorPatientStatus
    created_at: datetime
    detached_at: datetime | None

    patient: PatientShortResponse


class DoctorShortResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    email: EmailStr
    fullname: str
    speciality_id: uuid.UUID
    speciality_name: str


class PatientDoctorResponse(BaseModel):
    link_id: uuid.UUID
    status: DoctorPatientStatus
    created_at: datetime
    detached_at: datetime | None

    doctor: DoctorShortResponse


class RelativeShortResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    email: EmailStr
    fullname: str


class PatientRelativeResponse(BaseModel):
    link_id: uuid.UUID
    relationship_degree: str | None
    status: RelativePatientStatus
    created_at: datetime
    detached_at: datetime | None

    relative: RelativeShortResponse


class RelativePatientResponse(BaseModel):
    link_id: uuid.UUID
    relationship_degree: str | None
    status: RelativePatientStatus
    created_at: datetime
    detached_at: datetime | None

    patient: PatientShortResponse


class MessageResponse(BaseModel):
    message: str