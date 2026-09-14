# ./backend/app/modules/programs/consultation_service.py

import hashlib
import json
import uuid

from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import update
from sqlmodel import Session, select

from app.modules.articles.models import Article
from app.modules.programs.consultation_schemas import (
    StageConsultationItemResponse,
    StageConsultationsResponse,
    StageConsultationsUpdateRequest,
)
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import (
    Program,
    ProgramStage,
    ProgramStageItem,
)
from app.modules.questionnaires.models import Questionnaire
from app.modules.users.models import Speciality


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def lock_program_for_structure_edit(
    *,
    session: Session,
    program_id: uuid.UUID,
) -> Program:
    # UPDATE берёт блокировку строки в PostgreSQL
    # и блокировку записи в SQLite.
    #
    # Значение здесь не меняем.
    result = session.execute(
        update(Program)
        .where(Program.id == program_id)
        .values(updated_at=Program.updated_at)
        .execution_options(synchronize_session=False)
    )

    if result.rowcount != 1:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    program = session.get(Program, program_id)
    session.refresh(program)

    return program


def get_stage_items(
    *,
    session: Session,
    stage_id: uuid.UUID,
) -> list[ProgramStageItem]:
    return list(
        session.exec(
            select(ProgramStageItem)
            .where(
                ProgramStageItem.stage_id == stage_id
            )
            .order_by(
                ProgramStageItem.order_index,
                ProgramStageItem.id,
            )
        ).all()
    )


def calculate_stage_revision(
    *,
    stage: ProgramStage,
    items: list[ProgramStageItem],
) -> str:
    # Версия зависит от реального состава и порядка
    # элементов, а не от времени открытия формы.
    data = {
        "stage_id": str(stage.id),
        "items": [
            {
                "id": str(item.id),
                "item_type": item.item_type.value,
                "order_index": item.order_index,
                "article_id": (
                    str(item.article_id)
                    if item.article_id
                    else None
                ),
                "questionnaire_id": (
                    str(item.questionnaire_id)
                    if item.questionnaire_id
                    else None
                ),
                "speciality_id": (
                    str(item.speciality_id)
                    if item.speciality_id
                    else None
                ),
                "consultation_title": item.consultation_title,
                "consultation_description": (
                    item.consultation_description
                ),
            }
            for item in items
        ],
    }

    encoded = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    return hashlib.sha256(encoded).hexdigest()


def serialize_stage_consultations(
    *,
    session: Session,
    stage: ProgramStage,
) -> StageConsultationsResponse:
    items = get_stage_items(
        session=session,
        stage_id=stage.id,
    )

    article_ids = {
        item.article_id
        for item in items
        if item.article_id is not None
    }

    questionnaire_ids = {
        item.questionnaire_id
        for item in items
        if item.questionnaire_id is not None
    }

    speciality_ids = {
        item.speciality_id
        for item in items
        if item.speciality_id is not None
    }

    articles = {}

    if article_ids:
        rows = session.exec(
            select(
                Article.id,
                Article.title,
                Article.is_hidden,
            ).where(
                Article.id.in_(article_ids)
            )
        ).all()

        articles = {
            row[0]: {
                "title": row[1],
                "is_hidden": row[2],
            }
            for row in rows
        }

    questionnaires = {}

    if questionnaire_ids:
        rows = session.exec(
            select(
                Questionnaire.id,
                Questionnaire.title,
                Questionnaire.is_hidden,
            ).where(
                Questionnaire.id.in_(questionnaire_ids)
            )
        ).all()

        questionnaires = {
            row[0]: {
                "title": row[1],
                "is_hidden": row[2],
            }
            for row in rows
        }

    specialities = {}

    if speciality_ids:
        specialities = {
            speciality.id: speciality
            for speciality in session.exec(
                select(Speciality).where(
                    Speciality.id.in_(speciality_ids)
                )
            ).all()
        }

    result = []

    for item in items:
        if item.item_type == ProgramItemType.ARTICLE:
            article = articles.get(item.article_id)

            result.append(
                StageConsultationItemResponse(
                    id=item.id,
                    item_type=item.item_type,
                    title=(
                        article["title"]
                        if article
                        else "Статья недоступна"
                    ),
                    is_hidden=(
                        article["is_hidden"]
                        if article
                        else True
                    ),
                )
            )

            continue

        if item.item_type == ProgramItemType.QUESTIONNAIRE:
            questionnaire = questionnaires.get(
                item.questionnaire_id
            )

            result.append(
                StageConsultationItemResponse(
                    id=item.id,
                    item_type=item.item_type,
                    title=(
                        questionnaire["title"]
                        if questionnaire
                        else "Опросник недоступен"
                    ),
                    is_hidden=(
                        questionnaire["is_hidden"]
                        if questionnaire
                        else True
                    ),
                )
            )

            continue

        speciality = specialities.get(item.speciality_id)

        result.append(
            StageConsultationItemResponse(
                id=item.id,
                item_type=item.item_type,
                title=(
                    item.consultation_title
                    or (
                        speciality.consultation_name
                        if speciality
                        else None
                    )
                    or (
                        f"Консультация: {speciality.name}"
                        if speciality
                        else "Консультация"
                    )
                ),
                speciality_id=item.speciality_id,
                speciality_name=(
                    speciality.name if speciality else None
                ),
                consultation_title=item.consultation_title,
                consultation_description=(
                    item.consultation_description
                ),
            )
        )

    return StageConsultationsResponse(
        id=stage.id,
        title=stage.title,
        revision=calculate_stage_revision(
            stage=stage,
            items=items,
        ),
        items=result,
    )


def update_stage_consultations(
    *,
    session: Session,
    program: Program,
    stage: ProgramStage,
    payload: StageConsultationsUpdateRequest,
) -> StageConsultationsResponse:
    current_items = get_stage_items(
        session=session,
        stage_id=stage.id,
    )

    current_revision = calculate_stage_revision(
        stage=stage,
        items=current_items,
    )

    if current_revision != payload.expected_revision:
        raise HTTPException(
            status_code=409,
            detail=(
                "Этап уже изменён другим запросом. "
                "Обновите данные и повторите изменения."
            ),
        )

    current_by_id = {
        item.id: item
        for item in current_items
    }

    provided_ids = [
        item.id
        for item in payload.items
        if item.id is not None
    ]

    if len(provided_ids) != len(set(provided_ids)):
        raise HTTPException(
            status_code=422,
            detail="Элементы этапа не должны повторяться",
        )

    for requested in payload.items:
        if requested.id is None:
            continue

        existing = current_by_id.get(requested.id)

        if existing is None:
            raise HTTPException(
                status_code=422,
                detail="Элемент не принадлежит этому этапу",
            )

        if existing.item_type != requested.item_type:
            raise HTTPException(
                status_code=422,
                detail="Нельзя изменять тип существующего элемента",
            )

    current_protected_ids = [
        item.id
        for item in current_items
        if item.item_type != ProgramItemType.CONSULTATION
    ]

    requested_protected_ids = [
        item.id
        for item in payload.items
        if item.item_type != ProgramItemType.CONSULTATION
    ]

    if current_protected_ids != requested_protected_ids:
        raise HTTPException(
            status_code=422,
            detail=(
                "Статьи и опросники должны остаться "
                "в прежнем составе и взаимном порядке"
            ),
        )

    speciality_ids = {
        item.speciality_id
        for item in payload.items
        if item.item_type == ProgramItemType.CONSULTATION
    }

    specialities = {}

    if speciality_ids:
        specialities = {
            speciality.id: speciality
            for speciality in session.exec(
                select(Speciality).where(
                    Speciality.id.in_(speciality_ids)
                )
            ).all()
        }

    for requested in payload.items:
        if requested.item_type != ProgramItemType.CONSULTATION:
            continue

        speciality = specialities.get(
            requested.speciality_id
        )

        if speciality is None:
            raise HTTPException(
                status_code=422,
                detail="Специальность не найдена",
            )

        existing = (
            current_by_id.get(requested.id)
            if requested.id is not None
            else None
        )

        unchanged_speciality = (
            existing is not None
            and existing.speciality_id == requested.speciality_id
        )

        if speciality.is_hidden and not unchanged_speciality:
            raise HTTPException(
                status_code=422,
                detail=(
                    "Нельзя добавить консультацию "
                    "со скрытой специальностью"
                ),
            )

    # Освобождаем окончательные индексы.
    # Это нужно из-за uq_program_stage_item_order.
    temporary_start = max(
        [item.order_index for item in current_items] + [0]
    ) + len(payload.items) + 1

    if temporary_start + len(current_items) > 2_147_483_647:
        raise HTTPException(
            status_code=409,
            detail="Некорректные индексы порядка элементов",
        )

    for index, item in enumerate(current_items):
        item.order_index = temporary_start + index
        session.add(item)

    session.flush()

    retained_ids = set(provided_ids)

    for item in current_items:
        if (
            item.item_type == ProgramItemType.CONSULTATION
            and item.id not in retained_ids
        ):
            session.delete(item)

    session.flush()

    for index, requested in enumerate(payload.items):
        if requested.id is None:
            item = ProgramStageItem(
                stage_id=stage.id,
                item_type=ProgramItemType.CONSULTATION,
                order_index=index,
                speciality_id=requested.speciality_id,
                consultation_title=requested.consultation_title,
                consultation_description=(
                    requested.consultation_description
                ),
            )
        else:
            item = current_by_id[requested.id]
            item.order_index = index

            if item.item_type == ProgramItemType.CONSULTATION:
                item.speciality_id = requested.speciality_id
                item.consultation_title = (
                    requested.consultation_title
                )
                item.consultation_description = (
                    requested.consultation_description
                )

        session.add(item)

    program.updated_at = utc_now()
    session.add(program)

    session.flush()

    return serialize_stage_consultations(
        session=session,
        stage=stage,
    )