# ./backend/app/modules/questionnaires/utils.py
import uuid
from typing import Any

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.questionnaires.enums import QuestionType
from app.modules.questionnaires.models import (
    Question,
    Questionnaire,
    QuestionnaireTagLink,
)
from app.modules.questionnaires.schemas import (
    AnswerSubmitRequest,
)
from app.modules.tags.models import Tag


def get_questionnaire_tag_ids(
    *,
    session: Session,
    questionnaire_id: uuid.UUID,
) -> set[uuid.UUID]:
    links = session.exec(
        select(QuestionnaireTagLink).where(
            QuestionnaireTagLink.questionnaire_id
            == questionnaire_id
        )
    ).all()

    return {link.tag_id for link in links}


def get_questionnaire_tags(
    *,
    session: Session,
    questionnaire_id: uuid.UUID,
) -> list[Tag]:
    links = session.exec(
        select(QuestionnaireTagLink).where(
            QuestionnaireTagLink.questionnaire_id
            == questionnaire_id
        )
    ).all()

    tags: list[Tag] = []

    for link in links:
        tag = session.get(Tag, link.tag_id)

        if tag:
            tags.append(tag)

    return sorted(
        tags,
        key=lambda item: item.name.casefold(),
    )


def validate_questionnaire_answers(
    *,
    questionnaire: Questionnaire,
    answers: list[AnswerSubmitRequest],
) -> dict[uuid.UUID, Any]:
    answers_by_question = {
        answer.question_id: answer.value
        for answer in answers
    }

    question_ids = {
        question.id
        for question in questionnaire.questions
    }

    unknown_ids = set(answers_by_question) - question_ids

    if unknown_ids:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Передан ответ на неизвестный вопрос",
        )

    normalized_answers: dict[uuid.UUID, Any] = {}

    for question in questionnaire.questions:
        has_answer = question.id in answers_by_question

        if question.is_required and not has_answer:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=(
                    f"Не заполнен обязательный вопрос: "
                    f"{question.text}"
                ),
            )

        if not has_answer:
            continue

        value = answers_by_question[question.id]

        if question.question_type == QuestionType.TEXT:
            if not isinstance(value, str):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается текст: {question.text}",
                )

        elif question.question_type == QuestionType.NUMBER:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
            ):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается число: {question.text}",
                )

        elif question.question_type == QuestionType.BOOLEAN:
            if not isinstance(value, bool):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Ожидается логическое значение: "
                        f"{question.text}"
                    ),
                )

        elif question.question_type == QuestionType.SCALE:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
            ):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ожидается число шкалы: {question.text}",
                )

            if (
                value < question.scale_min
                or value > question.scale_max
            ):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Значение шкалы вне диапазона: "
                        f"{question.text}"
                    ),
                )

        elif (
            question.question_type
            == QuestionType.SINGLE_CHOICE
        ):
            option_ids = {
                str(option.id)
                for option in question.options
            }

            if str(value) not in option_ids:
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Неизвестный вариант ответа: "
                        f"{question.text}"
                    ),
                )

            value = str(value)

        elif (
            question.question_type
            == QuestionType.MULTIPLE_CHOICE
        ):
            if not isinstance(value, list):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Ожидается список вариантов: "
                        f"{question.text}"
                    ),
                )

            option_ids = {
                str(option.id)
                for option in question.options
            }
            selected_ids = [str(item) for item in value]

            if not set(selected_ids).issubset(option_ids):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        f"Передан неизвестный вариант: "
                        f"{question.text}"
                    ),
                )

            value = list(dict.fromkeys(selected_ids))

        normalized_answers[question.id] = value

    return normalized_answers

def normalize_question_answer(
    *,
    question: Question,
    value: Any,
) -> Any:
    if question.question_type == QuestionType.TEXT:
        if not isinstance(value, str):
            raise HTTPException(
                status_code=422,
                detail="Ожидается текстовый ответ",
            )

        return value

    if question.question_type == QuestionType.NUMBER:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise HTTPException(
                status_code=422,
                detail="Ожидается числовой ответ",
            )

        return value

    if question.question_type == QuestionType.BOOLEAN:
        if not isinstance(value, bool):
            raise HTTPException(
                status_code=422,
                detail="Ожидается значение Да или Нет",
            )

        return value

    if question.question_type == QuestionType.SCALE:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise HTTPException(
                status_code=422,
                detail="Ожидается значение шкалы",
            )

        if (
            value < question.scale_min
            or value > question.scale_max
        ):
            raise HTTPException(
                status_code=422,
                detail="Значение находится вне диапазона шкалы",
            )

        return value

    option_ids = {
        str(option.id)
        for option in question.options
    }

    if question.question_type == QuestionType.SINGLE_CHOICE:
        normalized_value = str(value)

        if normalized_value not in option_ids:
            raise HTTPException(
                status_code=422,
                detail="Неизвестный вариант ответа",
            )

        return normalized_value

    if question.question_type == QuestionType.MULTIPLE_CHOICE:
        if not isinstance(value, list):
            raise HTTPException(
                status_code=422,
                detail="Ожидается список вариантов",
            )

        normalized_values = list(
            dict.fromkeys(
                str(item)
                for item in value
            )
        )

        if not set(normalized_values).issubset(option_ids):
            raise HTTPException(
                status_code=422,
                detail="Передан неизвестный вариант ответа",
            )

        return normalized_values

    raise HTTPException(
        status_code=422,
        detail="Неизвестный тип вопроса",
    )
