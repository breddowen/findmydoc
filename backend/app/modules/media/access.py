# backend\app\modules\media\access.py

import uuid

from fastapi import HTTPException
from sqlmodel import Session, select

from app.core.security import AuthContext
from app.modules.articles.models import Article
from app.modules.articles.utils import get_article_tag_ids
from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import (
    patient_has_active_assignment,
)
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
    patient_can_access_content,
    patient_can_see_content,
)
from app.modules.media.constants import ImagePurpose
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import (
    Program,
    ProgramStage,
    ProgramStageItem,
    ProgramTagLink,
)
from app.modules.questionnaires.models import Questionnaire
from app.modules.questionnaires.utils import (
    get_questionnaire_tag_ids,
)
from app.modules.tags.models import (
    LifeAspect,
    LifeAspectTagLink,
    Tag,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import (
    DoctorProfile,
    User,
)


MANAGER_ROLES = {
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
}

STAFF_ROLES = {
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
    UserRole.DOCTOR,
}


def not_found() -> None:
    raise HTTPException(
        status_code=404,
        detail="Изображение или сущность не найдены",
    )


def get_image_entity(
    *,
    session: Session,
    purpose: ImagePurpose,
    entity_id: uuid.UUID,
):
    if purpose == "doctor":
        user = session.get(User, entity_id)

        if user is None or user.deleted_at is not None:
            not_found()

        entity = session.exec(
            select(DoctorProfile).where(
                DoctorProfile.user_id == user.id
            )
        ).first()
    else:
        models = {
            "article": Article,
            "questionnaire": Questionnaire,
            "program": Program,
            "life_aspect": LifeAspect,
        }

        entity = session.get(
            models[purpose],
            entity_id,
        )

    if entity is None:
        not_found()

    return entity


def ensure_can_manage_entity_image(
    *,
    auth: AuthContext,
    purpose: ImagePurpose,
    entity,
) -> None:
    if auth.active_role in MANAGER_ROLES:
        return

    if auth.active_role == UserRole.DOCTOR:
        if (
            purpose == "doctor"
            and entity.user_id == auth.user.id
        ):
            return

        if (
            purpose == "article"
            and entity.created_by_user_id == auth.user.id
        ):
            return

    raise HTTPException(
        status_code=403,
        detail="Нет прав на изменение изображения",
    )


def ensure_program_card_context(
    *,
    session: Session,
    purpose: ImagePurpose,
    content_id: uuid.UUID,
    program_id: uuid.UUID,
    program_stage_id: uuid.UUID | None,
) -> None:
    program = session.get(Program, program_id)

    if program is None or program.is_hidden:
        not_found()

    statement = (
        select(ProgramStageItem.id)
        .join(
            ProgramStage,
            ProgramStage.id == ProgramStageItem.stage_id,
        )
        .where(
            ProgramStage.program_id == program.id,
        )
    )

    if purpose == "article":
        statement = statement.where(
            ProgramStageItem.item_type == ProgramItemType.ARTICLE,
            ProgramStageItem.article_id == content_id,
        )
    elif purpose == "questionnaire":
        statement = statement.where(
            ProgramStageItem.item_type
            == ProgramItemType.QUESTIONNAIRE,
            ProgramStageItem.questionnaire_id == content_id,
        )
    else:
        not_found()

    if program_stage_id is not None:
        statement = statement.where(
            ProgramStage.id == program_stage_id
        )

    if session.exec(statement.limit(1)).first() is None:
        not_found()

    # Здесь намеренно нет проверки покупки программы.
    # Проверяем обложку карточки, а не её Pro-материал.


def patient_can_see_article_card(
    *,
    session: Session,
    patient,
    article: Article,
) -> bool:
    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    # Назначение может показывать материал вне каталога.
    if is_assigned:
        return True

    if article.is_library_hidden:
        return False

    # Используем фактическую настройку вашего каталога,
    # не задавая её повторно и не меняя текущее значение.
    #
    # Импорт внутри функции исключает циклический импорт
    # при загрузке модулей приложения.
    from app.modules.articles.routers import (
        STRICT_PATIENT_ARTICLE_TAG_FILTER,
    )

    if not STRICT_PATIENT_ARTICLE_TAG_FILTER:
        return True

    return patient_can_see_content(
        session=session,
        patient=patient,
        content_tag_ids=get_article_tag_ids(
            session=session,
            article_id=article.id,
        ),
        is_hidden=False,
    )


def patient_can_see_questionnaire_card(
    *,
    session: Session,
    patient,
    questionnaire: Questionnaire,
) -> bool:
    if patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.QUESTIONNAIRE,
        content_id=questionnaire.id,
    ):
        return True

    if questionnaire.is_library_hidden:
        return False

    # Сохраняем текущее правило списка опросников:
    # он сейчас фильтрует карточки через
    # patient_can_access_content().
    #
    # В контексте программы обложка будет доступна
    # независимо от Pro через отдельную ветку выше.
    return patient_can_access_content(
        session=session,
        patient=patient,
        content_tag_ids=get_questionnaire_tag_ids(
            session=session,
            questionnaire_id=questionnaire.id,
        ),
        pro_content=questionnaire.pro_content,
        is_hidden=False,
    )


def patient_can_see_life_aspect(
    *,
    session: Session,
    aspect: LifeAspect,
) -> bool:
    # Пациентский каталог сфер исключает пустые сферы.
    # Повторяем правило наличия хотя бы одной программы
    # через нескрытый тег.
    statement = (
        select(Program.id)
        .join(
            ProgramTagLink,
            ProgramTagLink.program_id == Program.id,
        )
        .join(
            LifeAspectTagLink,
            LifeAspectTagLink.tag_id == ProgramTagLink.tag_id,
        )
        .join(
            Tag,
            Tag.id == LifeAspectTagLink.tag_id,
        )
        .where(
            LifeAspectTagLink.life_aspect_id == aspect.id,
            Tag.is_hidden.is_(False),
            Program.is_hidden.is_(False),
        )
        .limit(1)
    )

    return session.exec(statement).first() is not None


def ensure_can_view_entity_image(
    *,
    session: Session,
    auth: AuthContext,
    purpose: ImagePurpose,
    entity,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    if program_stage_id is not None and program_id is None:
        raise HTTPException(
            status_code=422,
            detail="Для этапа необходимо указать программу",
        )

    if (
        program_id is not None
        and purpose not in {"article", "questionnaire"}
    ):
        raise HTTPException(
            status_code=422,
            detail=(
                "Контекст программы поддерживается "
                "только для статей и опросников"
            ),
        )

    if purpose == "doctor":
        if auth.active_role in MANAGER_ROLES:
            return

        if (
            auth.active_role == UserRole.DOCTOR
            and entity.user_id == auth.user.id
        ):
            return

        not_found()

    if purpose == "life_aspect":
        if auth.active_role in MANAGER_ROLES:
            return
    elif auth.active_role in STAFF_ROLES:
        return

    # Доступ родственников здесь пока не расширяем.
    # Для него потребуется отдельное правило просмотра.
    if auth.active_role != UserRole.PATIENT:
        not_found()

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    if entity.is_hidden:
        not_found()

    if purpose in {"article", "questionnaire"}:
        if program_id is not None:
            ensure_program_card_context(
                session=session,
                purpose=purpose,
                content_id=entity.id,
                program_id=program_id,
                program_stage_id=program_stage_id,
            )
            return

        if purpose == "article":
            allowed = patient_can_see_article_card(
                session=session,
                patient=patient,
                article=entity,
            )
        else:
            allowed = patient_can_see_questionnaire_card(
                session=session,
                patient=patient,
                questionnaire=entity,
            )

        if allowed:
            return

        not_found()

    if purpose == "program":
        # Ваш пациентский API показывает все
        # нескрытые программы независимо от тегов.
        return

    if purpose == "life_aspect":
        if patient_can_see_life_aspect(
            session=session,
            aspect=entity,
        ):
            return

        not_found()

    not_found()