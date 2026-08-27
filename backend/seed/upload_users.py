# ./backend/seed/upload_users.py
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from sqlmodel import Session, select


BACKEND_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = Path(__file__).resolve().parent / "data" / "users.json"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.core.db import init_sqlite_db, sqlite_engine  # noqa: E402
from app.core.security import hash_password  # noqa: E402
from app.modules.users.enums import (  # noqa: E402
    DoctorPatientStatus,
    RelativePatientStatus,
    UserRole,
)
from app.modules.users.models import (  # noqa: E402
    DoctorPatientLink,
    DoctorProfile,
    MedAssistantProfile,
    PatientProfile,
    RelativePatientLink,
    RelativeProfile,
    Speciality,
    User,
    UserRoleLink,
)
from app.modules.users.utils import get_user_by_email  # noqa: E402


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def load_seed_data() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_or_create_speciality(
    *,
    session: Session,
    name: str,
    description: str | None,
) -> Speciality:
    speciality = session.exec(
        select(Speciality).where(Speciality.name == name)
    ).first()

    if speciality:
        if description is not None:
            speciality.description = description
            session.add(speciality)

        return speciality

    speciality = Speciality(
        name=name,
        description=description,
    )

    session.add(speciality)
    session.flush()

    return speciality


def ensure_role(
    *,
    session: Session,
    user: User,
    role: UserRole,
    is_primary: bool,
) -> UserRoleLink:
    role_link = session.exec(
        select(UserRoleLink).where(
            UserRoleLink.user_id == user.id,
            UserRoleLink.role == role,
        )
    ).first()

    if role_link:
        role_link.is_primary = is_primary
        session.add(role_link)
        return role_link

    role_link = UserRoleLink(
        user_id=user.id,
        role=role,
        is_primary=is_primary,
    )

    session.add(role_link)
    session.flush()

    return role_link


def create_or_update_user(
    *,
    session: Session,
    user_data: dict[str, Any],
    specialities: dict[str, Speciality],
) -> User:
    email = user_data["email"].strip().lower()
    user = get_user_by_email(session, email)

    if not user:
        user = User(
            email=email,
            hashed_password=hash_password(user_data["password"]),
        )

    user.first_name = user_data.get("first_name")
    user.last_name = user_data.get("last_name")
    user.middle_name = user_data.get("middle_name")
    user.is_active = True
    user.is_blocked = False
    user.deleted_at = None
    user.updated_at = utc_now()

    if user_data.get("email_verified"):
        user.email_verified_at = user.email_verified_at or utc_now()

    session.add(user)
    session.flush()

    role_items = user_data.get("roles", [])

    for role_item in role_items:
        ensure_role(
            session=session,
            user=user,
            role=UserRole(role_item["role"]),
            is_primary=bool(role_item.get("is_primary", False)),
        )

    doctor_data = user_data.get("doctor")

    if doctor_data is not None:
        speciality_name = doctor_data["speciality"]
        speciality = specialities[speciality_name]

        doctor_profile = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == user.id
            )
        ).first()

        if not doctor_profile:
            doctor_profile = DoctorProfile(
                user_id=user.id,
                speciality_id=speciality.id,
            )
        else:
            doctor_profile.speciality_id = speciality.id
            doctor_profile.updated_at = utc_now()

        session.add(doctor_profile)

    patient_data = user_data.get("patient")

    if patient_data is not None:
        patient_profile = session.exec(
            select(PatientProfile).where(
                PatientProfile.user_id == user.id
            )
        ).first()

        parsed_dob = (
            date.fromisoformat(patient_data["dob"])
            if patient_data.get("dob")
            else None
        )

        if not patient_profile:
            patient_profile = PatientProfile(
                user_id=user.id,
                record_id=patient_data["record_id"],
                fullname=patient_data.get("fullname"),
                dob=parsed_dob,
            )
        else:
            patient_profile.record_id = patient_data["record_id"]
            patient_profile.fullname = patient_data.get("fullname")
            patient_profile.dob = parsed_dob
            patient_profile.updated_at = utc_now()

        session.add(patient_profile)

    if user_data.get("relative") is not None:
        relative_profile = session.exec(
            select(RelativeProfile).where(
                RelativeProfile.user_id == user.id
            )
        ).first()

        if not relative_profile:
            session.add(RelativeProfile(user_id=user.id))

    roles = {
        UserRole(role_item["role"])
        for role_item in role_items
    }

    if UserRole.MED_ASSISTANT in roles:
        med_profile = session.exec(
            select(MedAssistantProfile).where(
                MedAssistantProfile.user_id == user.id
            )
        ).first()

        if not med_profile:
            session.add(MedAssistantProfile(user_id=user.id))

    session.flush()

    return user


def get_doctor_profile(
    session: Session,
    user: User,
) -> DoctorProfile:
    profile = session.exec(
        select(DoctorProfile).where(
            DoctorProfile.user_id == user.id
        )
    ).first()

    if not profile:
        raise RuntimeError(
            f"У пользователя {user.email} отсутствует профиль врача"
        )

    return profile


def get_patient_profile(
    session: Session,
    user: User,
) -> PatientProfile:
    profile = session.exec(
        select(PatientProfile).where(
            PatientProfile.user_id == user.id
        )
    ).first()

    if not profile:
        raise RuntimeError(
            f"У пользователя {user.email} отсутствует профиль пациента"
        )

    return profile


def get_relative_profile(
    session: Session,
    user: User,
) -> RelativeProfile:
    profile = session.exec(
        select(RelativeProfile).where(
            RelativeProfile.user_id == user.id
        )
    ).first()

    if not profile:
        raise RuntimeError(
            f"У пользователя {user.email} отсутствует профиль родственника"
        )

    return profile


def upload_seed() -> None:
    init_sqlite_db()
    data = load_seed_data()

    with Session(sqlite_engine) as session:
        specialities: dict[str, Speciality] = {}

        for speciality_data in data["specialities"]:
            speciality = get_or_create_speciality(
                session=session,
                name=speciality_data["name"],
                description=speciality_data.get("description"),
            )
            specialities[speciality.name] = speciality

        session.flush()

        users_by_key: dict[str, User] = {}

        for user_data in data["users"]:
            user = create_or_update_user(
                session=session,
                user_data=user_data,
                specialities=specialities,
            )

            users_by_key[user_data["key"]] = user
            print(f"✓ User synchronized: {user.email}")

        session.flush()

        for link_data in data.get("doctor_patient_links", []):
            doctor_user = users_by_key[link_data["doctor"]]
            patient_user = users_by_key[link_data["patient"]]

            doctor = get_doctor_profile(session, doctor_user)
            patient = get_patient_profile(session, patient_user)

            link = session.exec(
                select(DoctorPatientLink).where(
                    DoctorPatientLink.doctor_id == doctor.id,
                    DoctorPatientLink.patient_id == patient.id,
                )
            ).first()

            if not link:
                link = DoctorPatientLink(
                    doctor_id=doctor.id,
                    patient_id=patient.id,
                    status=DoctorPatientStatus.ACTIVE,
                )
            else:
                link.status = DoctorPatientStatus.ACTIVE
                link.detached_at = None
                link.updated_at = utc_now()

            session.add(link)

        for link_data in data.get("relative_patient_links", []):
            relative_user = users_by_key[link_data["relative"]]
            patient_user = users_by_key[link_data["patient"]]

            relative = get_relative_profile(session, relative_user)
            patient = get_patient_profile(session, patient_user)

            link = session.exec(
                select(RelativePatientLink).where(
                    RelativePatientLink.relative_id == relative.id,
                    RelativePatientLink.patient_id == patient.id,
                )
            ).first()

            if not link:
                link = RelativePatientLink(
                    relative_id=relative.id,
                    patient_id=patient.id,
                    relationship_degree=link_data.get(
                        "relationship_degree"
                    ),
                    status=RelativePatientStatus.ACTIVE,
                )
            else:
                link.relationship_degree = link_data.get(
                    "relationship_degree"
                )
                link.status = RelativePatientStatus.ACTIVE
                link.detached_at = None
                link.updated_at = utc_now()

            session.add(link)

        session.commit()

    print()
    print("Seed completed successfully.")
    print("Password for all users: secret")


if __name__ == "__main__":
    upload_seed()