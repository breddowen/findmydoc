# ./backend/app/modules/tags/life_aspect_catalog.py
import uuid

from sqlmodel import Session, select

from app.modules.content.utils import (
    get_patient_effective_tag_ids,
    tags_match,
)
from app.modules.programs.models import (
    PatientProgramAccess,
    Program,
    ProgramTagLink,
)
from app.modules.tags.life_aspect_schemas import (
    LifeAspectPatientResponse,
    LifeAspectProgramResponse,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.users.models import PatientProfile


def build_patient_life_aspects(
    *,
    session: Session,
    patient: PatientProfile,
) -> list[LifeAspectPatientResponse]:
    aspects = session.exec(
        select(LifeAspect)
        .where(
            LifeAspect.is_hidden.is_(False)
        )
        .order_by(
            LifeAspect.order_index,
            LifeAspect.name,
            LifeAspect.id,
        )
    ).all()

    if not aspects:
        return []

    aspect_ids = [aspect.id for aspect in aspects]

    # Для группировки используем только нескрытые теги.
    aspect_links = session.exec(
        select(LifeAspectTagLink)
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id.in_(aspect_ids),
            Tag.is_hidden.is_(False),
        )
    ).all()

    tags_by_aspect: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {
        aspect.id: set()
        for aspect in aspects
    }

    all_aspect_tag_ids: set[uuid.UUID] = set()

    for link in aspect_links:
        tags_by_aspect[link.life_aspect_id].add(
            link.tag_id
        )
        all_aspect_tag_ids.add(link.tag_id)

    if not all_aspect_tag_ids:
        return []

    # Подбираем программы по тегам сфер, а не пациента.
    # Для принадлежности сфере достаточно одного тега.
    programs = session.exec(
        select(Program)
        .join(
            ProgramTagLink,
            ProgramTagLink.program_id == Program.id,
        )
        .where(
            Program.is_hidden.is_(False),
            ProgramTagLink.tag_id.in_(
                list(all_aspect_tag_ids)
            ),
        )
        .distinct()
    ).all()

    if not programs:
        return []

    program_ids = [program.id for program in programs]

    # Для рекомендации нужны ВСЕ теги программы:
    # сохраняем текущее правило tags_match().
    program_links = session.exec(
        select(ProgramTagLink).where(
            ProgramTagLink.program_id.in_(program_ids)
        )
    ).all()

    tags_by_program: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {
        program.id: set()
        for program in programs
    }

    programs_by_tag: dict[
        uuid.UUID,
        set[uuid.UUID],
    ] = {}

    for link in program_links:
        tags_by_program[link.program_id].add(link.tag_id)

        if link.tag_id in all_aspect_tag_ids:
            programs_by_tag.setdefault(
                link.tag_id,
                set(),
            ).add(link.program_id)

    accesses = session.exec(
        select(PatientProgramAccess).where(
            PatientProgramAccess.patient_id == patient.id,
            PatientProgramAccess.program_id.in_(program_ids),
        )
    ).all()

    accessible_program_ids = {
        access.program_id
        for access in accesses
        if access.is_active
    }

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    cards_by_program: dict[
        uuid.UUID,
        LifeAspectProgramResponse,
    ] = {}

    for program in programs:
        program_tag_ids = tags_by_program[program.id]

        matches_patient = tags_match(
            patient_tag_ids=patient_tag_ids,
            content_tag_ids=program_tag_ids,
        )

        has_access = program.id in accessible_program_ids

        cards_by_program[program.id] = (
            LifeAspectProgramResponse(
                id=program.id,
                title=program.title,
                description=program.description,

                is_paid=program.service_id is not None,
                is_popular=program.is_popular,
                is_start=program.is_start,
                home_priority=program.home_priority,

                is_recommended=(
                    bool(program_tag_ids)
                    and matches_patient
                ),

                # can_open_program=(
                #     has_access or matches_patient
                # ),
                can_open_program=True,
                has_program_access=has_access,
            )
        )

    result: list[LifeAspectPatientResponse] = []

    for aspect in aspects:
        matching_program_ids: set[uuid.UUID] = set()

        for tag_id in tags_by_aspect[aspect.id]:
            matching_program_ids.update(
                programs_by_tag.get(tag_id, set())
            )

        if not matching_program_ids:
            continue

        cards = [
            cards_by_program[program_id]
            for program_id in matching_program_ids
        ]

        cards.sort(
            key=lambda card: (
                not card.is_recommended,
                -card.home_priority,
                card.title.casefold(),
                str(card.id),
            )
        )

        result.append(
            LifeAspectPatientResponse(
                id=aspect.id,
                name=aspect.name,
                description=aspect.description,
                order_index=aspect.order_index,
                programs=cards,
            )
        )

    return result