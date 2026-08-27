# ./backend/app/modules/tags/utils.py
import uuid
from dataclasses import dataclass, field

from sqlmodel import Session, select

from app.modules.tags.enums import DoctorTagOverrideAction
from app.modules.tags.models import (
    DoctorTagOverride,
    SpecialityTagLink,
    Tag,
)
from app.modules.tags.schemas import (
    EffectiveTagResponse,
    EffectiveTagsResponse,
)
from app.modules.users.enums import (
    DoctorPatientStatus,
    RelativePatientStatus,
)
from app.modules.users.models import (
    DoctorPatientLink,
    DoctorProfile,
    PatientProfile,
    RelativePatientLink,
    RelativeProfile,
)


@dataclass
class EffectiveTagData:
    tag: Tag
    sources: set[str] = field(default_factory=set)


def merge_tag_data(
    target: dict[uuid.UUID, EffectiveTagData],
    source: dict[uuid.UUID, EffectiveTagData],
    source_prefix: str | None = None,
) -> None:
    for tag_id, source_data in source.items():
        if tag_id not in target:
            target[tag_id] = EffectiveTagData(tag=source_data.tag)

        if source_prefix:
            target[tag_id].sources.add(source_prefix)
        else:
            target[tag_id].sources.update(source_data.sources)


def get_doctor_effective_tag_data(
    *,
    session: Session,
    doctor: DoctorProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    default_links = session.exec(
        select(SpecialityTagLink).where(
            SpecialityTagLink.speciality_id
            == doctor.speciality_id
        )
    ).all()

    for link in default_links:
        tag = session.get(Tag, link.tag_id)

        if not tag:
            continue

        result[tag.id] = EffectiveTagData(
            tag=tag,
            sources={"default"},
        )

    overrides = session.exec(
        select(DoctorTagOverride).where(
            DoctorTagOverride.doctor_id == doctor.id
        )
    ).all()

    for override in overrides:
        tag = session.get(Tag, override.tag_id)

        if not tag:
            continue

        if override.action == DoctorTagOverrideAction.REMOVE:
            result.pop(tag.id, None)
            continue

        if tag.id not in result:
            result[tag.id] = EffectiveTagData(tag=tag)

        # Кастомное добавление имеет приоритет над default.
        result[tag.id].sources = {"custom"}

    return result


def get_patient_effective_tag_data(
    *,
    session: Session,
    patient: PatientProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    active_links = session.exec(
        select(DoctorPatientLink).where(
            DoctorPatientLink.patient_id == patient.id,
            DoctorPatientLink.status
            == DoctorPatientStatus.ACTIVE,
        )
    ).all()

    for link in active_links:
        doctor = session.get(
            DoctorProfile,
            link.doctor_id,
        )

        if not doctor:
            continue

        doctor_tags = get_doctor_effective_tag_data(
            session=session,
            doctor=doctor,
        )

        merge_tag_data(
            target=result,
            source=doctor_tags,
            source_prefix=f"doctor:{doctor.id}",
        )

    return result


def get_relative_effective_tag_data(
    *,
    session: Session,
    relative: RelativeProfile,
) -> dict[uuid.UUID, EffectiveTagData]:
    result: dict[uuid.UUID, EffectiveTagData] = {}

    active_links = session.exec(
        select(RelativePatientLink).where(
            RelativePatientLink.relative_id == relative.id,
            RelativePatientLink.status
            == RelativePatientStatus.ACTIVE,
        )
    ).all()

    for link in active_links:
        patient = session.get(
            PatientProfile,
            link.patient_id,
        )

        if not patient:
            continue

        patient_tags = get_patient_effective_tag_data(
            session=session,
            patient=patient,
        )

        merge_tag_data(
            target=result,
            source=patient_tags,
            source_prefix=f"patient:{patient.id}",
        )

    relative_tag = session.exec(
        select(Tag).where(
            Tag.name == "relative",
            Tag.is_system.is_(True),
        )
    ).first()

    if relative_tag:
        result[relative_tag.id] = EffectiveTagData(
            tag=relative_tag,
            sources={"system"},
        )

    return result


def serialize_effective_tags(
    *,
    owner_type: str,
    owner_id: uuid.UUID,
    tag_data: dict[uuid.UUID, EffectiveTagData],
) -> EffectiveTagsResponse:
    sorted_items = sorted(
        tag_data.values(),
        key=lambda item: item.tag.name.lower(),
    )

    return EffectiveTagsResponse(
        owner_type=owner_type,
        owner_id=owner_id,
        tags=[
            EffectiveTagResponse(
                id=item.tag.id,
                name=item.tag.name,
                description=item.tag.description,
                is_system=item.tag.is_system,
                sources=sorted(item.sources),
            )
            for item in sorted_items
        ],
    )