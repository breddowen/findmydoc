# ./backend/app/modules/articles/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from app.modules.events.models import Event

from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import (
    AuthContext,
    get_current_auth,
    require_roles,
)
from app.modules.articles.models import (
    Article,
    ArticleProgress,
)
from app.modules.articles.schemas import (
    ArticleCreateRequest,
    ArticleListItem,
    ArticleProgressResponse,
    ArticleProgressUpdateRequest,
    ArticleReadResponse,
    ArticleResponse,
    ArticleUpdateRequest,
    ArticleVisibilityRequest,
    ArticleOpenRequest,
    ArticleOpenResponse,
    ArticleProgressUpdateRequest,

)
from app.modules.articles.utils import (
    get_article_tag_ids,
    replace_article_tags,
    serialize_article,
    serialize_article_list_item,
)
from app.modules.content.utils import (
    ensure_patient_content_access,
    get_patient_profile_by_user_id,
    patient_can_access_content,
    patient_can_see_content,
)
from app.modules.events.enums import EventType
from app.modules.events.service import record_event
from app.modules.users.enums import UserRole

from app.modules.assignments.enums import AssignmentType
from app.modules.assignments.utils import (
    mark_assignment_completed,
    patient_has_active_assignment,
)
from app.modules.programs.utils import (
    sync_patient_program_enrollments,
)

router = APIRouter(
    prefix="/api/v1/articles",
    tags=["Articles"],
)

# ============================================================
# НАСТРОЙКА ФИЛЬТРАЦИИ СТАТЕЙ ДЛЯ ПАЦИЕНТОВ
#
# False:
#   пациент видит все нескрытые статьи;
#   подходящие по тегам статьи находятся выше.
#
# True:
#   пациент видит только статьи по своим тегам
#   либо статьи с активным назначением.
# ============================================================
STRICT_PATIENT_ARTICLE_TAG_FILTER = False

ARTICLE_COMPLETION_THRESHOLD = 90.0
MIN_TRACKABLE_SCROLL_DISTANCE = 240

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def get_article_event_counts(
    *,
    session: Session,
    before: datetime | None = None,
) -> dict[uuid.UUID, dict[str, int]]:
    statement = (
        select(
            Event.subject_id,
            Event.event_type,
            func.count(Event.id),
        )
        .where(
            Event.subject_type == "article",
            Event.subject_id.is_not(None),
            Event.event_type.in_(
                [
                    EventType.ARTICLE_OPENED,
                    EventType.ARTICLE_READ,
                ]
            ),
        )
    )

    if before is not None:
        statement = statement.where(
            Event.occurred_at < before
        )

    statement = statement.group_by(
        Event.subject_id,
        Event.event_type,
    )

    result: dict[uuid.UUID, dict[str, int]] = {}

    for subject_id, event_type, count in session.exec(
        statement
    ).all():
        if subject_id not in result:
            result[subject_id] = {
                "opened": 0,
                "read": 0,
            }

        if event_type == EventType.ARTICLE_OPENED:
            result[subject_id]["opened"] = count
        elif event_type == EventType.ARTICLE_READ:
            result[subject_id]["read"] = count

    return result


def calculate_article_score(
    *,
    opened_count: int,
    read_count: int,
) -> float:
    """
    Сглаженный рейтинг.

    Новая статья с одним открытием и одним прочтением
    не должна сразу обгонять статью с большой статистикой.
    """
    if opened_count <= 0:
        return 0.0

    # Сглаживание с условным предварительным значением 50%
    # и весом 10 открытий.
    return (
        read_count + 5
    ) / (
        opened_count + 10
    )


def ensure_patient_can_access_article(
    *,
    article: Article,
    patient,
    is_assigned: bool,
) -> None:
    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if (
        article.pro_content
        and not patient.pro_enabled
        and not is_assigned
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Требуется Pro-доступ",
        )
    
@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    articles = session.exec(
        select(Article).order_by(
            Article.created_at.desc()
        )
    ).all()

    now = datetime.now(timezone.utc)

    ranking_cutoff = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    # Актуальные счётчики для суперпользователя
    # и медицинского ассистента.
    live_event_counts = get_article_event_counts(
        session=session,
    )

    # Стабильные в течение дня счётчики,
    # используемые только для ранжирования
    # списка пациента.
    ranking_event_counts = get_article_event_counts(
        session=session,
        before=ranking_cutoff,
    )

    event_counts = get_article_event_counts(
        session=session,
        before=ranking_cutoff,
    )

    if auth.active_role != UserRole.PATIENT:
        result: list[ArticleListItem] = []

        can_see_analytics = auth.active_role in {
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        }

        for article in articles:
            item = serialize_article_list_item(
                session=session,
                article=article,
            )

            if can_see_analytics:
                counts = live_event_counts.get(
                    article.id,
                    {
                        "opened": 0,
                        "read": 0,
                    },
                )

                opened_count = counts["opened"]
                read_count = counts["read"]

                item.opened_count = opened_count
                item.read_count = read_count
                item.read_rate = round(
                    (
                        read_count
                        / opened_count
                        * 100
                    )
                    if opened_count > 0
                    else 0,
                    2,
                )

            result.append(item)

        return result[offset:offset + limit]

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    ranked_articles: list[
        tuple[
            bool,
            bool,
            float,
            datetime,
            ArticleListItem,
        ]
    ] = []

    for article in articles:
        if article.is_hidden:
            continue

        tag_ids = get_article_tag_ids(
            session=session,
            article_id=article.id,
        )

        is_assigned = patient_has_active_assignment(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        matches_patient_tags = (
            patient_can_see_content(
                session=session,
                patient=patient,
                content_tag_ids=tag_ids,
                is_hidden=False,
            )
        )

        # ====================================================
        # МЕСТО СТРОГОЙ ФИЛЬТРАЦИИ СТАТЕЙ ПО ТЕГАМ
        # ====================================================
        if (
            STRICT_PATIENT_ARTICLE_TAG_FILTER
            and not is_assigned
            and not matches_patient_tags
        ):
            continue

        # Теги больше не запрещают чтение.
        # Они используются только для ранжирования.
        can_access = (
            is_assigned
            or not article.pro_content
            or patient.pro_enabled
        )

        counts = ranking_event_counts.get(
            article.id,
            {
                "opened": 0,
                "read": 0,
            },
        )

        score = calculate_article_score(
            opened_count=counts["opened"],
            read_count=counts["read"],
        )

        item = serialize_article_list_item(
            session=session,
            article=article,
            can_access=can_access,
        )

        ranked_articles.append(
            (
                is_assigned,
                matches_patient_tags,
                score,
                article.created_at,
                item,
            )
        )

    ranked_articles.sort(
        key=lambda row: (
            row[0],  # Назначенные.
            row[1],  # Подходящие по тегам.
            row[2],  # Эффективность статьи.
            row[3],  # Более новые.
        ),
        reverse=True,
    )

    items = [
        row[4]
        for row in ranked_articles
    ]

    return items[offset:offset + limit]

@router.get(
    "/{article_id}",
    response_model=ArticleResponse,
)
async def get_article(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    if auth.active_role == UserRole.PATIENT:
        patient = get_patient_profile_by_user_id(
            session=session,
            user_id=auth.user.id,
        )

        is_assigned = patient_has_active_assignment(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        ensure_patient_can_access_article(
            article=article,
            patient=patient,
            is_assigned=is_assigned,
        )

    return serialize_article(
        session=session,
        article=article,
    )

# @router.get(
#     "/{article_id}",
#     response_model=ArticleResponse,
# )
# async def get_article(
#     article_id: uuid.UUID,
#     auth: AuthContext = Depends(get_current_auth),
#     session: Session = Depends(get_session),
# ) -> ArticleResponse:
#     article = session.get(Article, article_id)

#     if not article:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Статья не найдена",
#         )

#     if auth.active_role == UserRole.PATIENT:
#         patient = get_patient_profile_by_user_id(
#             session=session,
#             user_id=auth.user.id,
#         )

#         is_assigned = patient_has_active_assignment(
#             session=session,
#             patient_id=patient.id,
#             assignment_type=AssignmentType.ARTICLE,
#             content_id=article.id,
#         )

#         # Скрытие имеет приоритет над назначением.
#         if article.is_hidden:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Статья скрыта",
#             )

#         if not is_assigned:
#             ensure_patient_content_access(
#                 session=session,
#                 patient=patient,
#                 content_tag_ids=get_article_tag_ids(
#                     session=session,
#                     article_id=article.id,
#                 ),
#                 pro_content=article.pro_content,
#                 is_hidden=article.is_hidden,
#             )

#     return serialize_article(
#         session=session,
#         article=article,
#     )


@router.post(
    "",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_article(
    payload: ArticleCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = Article(
        title=payload.title.strip(),
        content=payload.content,
        pro_content=payload.pro_content,
        created_by_user_id=auth.user.id,
    )

    session.add(article)
    session.flush()

    replace_article_tags(
        session=session,
        article=article,
        tag_ids=payload.tag_ids,
    )

    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


@router.patch(
    "/{article_id}",
    response_model=ArticleResponse,
)
async def update_article(
    article_id: uuid.UUID,
    payload: ArticleUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if (
        auth.active_role == UserRole.DOCTOR
        and article.created_by_user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Врач может редактировать только "
                "созданные им статьи"
            ),
        )

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )
    tag_ids = update_data.pop("tag_ids", None)

    if "title" in update_data:
        update_data["title"] = (
            update_data["title"].strip()
        )

    for field_name, value in update_data.items():
        setattr(article, field_name, value)

    if tag_ids is not None:
        replace_article_tags(
            session=session,
            article=article,
            tag_ids=tag_ids,
        )

    article.updated_at = utc_now()

    session.add(article)
    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


@router.patch(
    "/{article_id}/visibility",
    response_model=ArticleResponse,
)
async def change_article_visibility(
    article_id: uuid.UUID,
    payload: ArticleVisibilityRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
            UserRole.DOCTOR,
        )
    ),
    session: Session = Depends(get_session),
) -> ArticleResponse:
    article = session.get(Article, article_id)

    if (
        auth.active_role == UserRole.DOCTOR
        and article.created_by_user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Врач может редактировать только "
                "созданные им статьи"
            ),
        )

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    article.is_hidden = payload.is_hidden
    article.hidden_at = (
        utc_now()
        if payload.is_hidden
        else None
    )
    article.updated_at = utc_now()

    session.add(article)
    session.commit()
    session.refresh(article)

    return serialize_article(
        session=session,
        article=article,
    )


# @router.post(
#     "/{article_id}/read",
#     response_model=ArticleReadResponse,
# )
# async def mark_article_as_read(
#     article_id: uuid.UUID,
#     auth: AuthContext = Depends(
#         require_roles(UserRole.PATIENT)
#     ),
#     session: Session = Depends(get_session),
# ) -> ArticleReadResponse:
#     article = session.get(Article, article_id)

#     if not article:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Статья не найдена",
#         )

#     patient = get_patient_profile_by_user_id(
#         session=session,
#         user_id=auth.user.id,
#     )

#     ensure_patient_content_access(
#         session=session,
#         patient=patient,
#         content_tag_ids=get_article_tag_ids(
#             session=session,
#             article_id=article.id,
#         ),
#         pro_content=article.pro_content,
#         is_hidden=article.is_hidden,
#     )

#     event = record_event(
#         session=session,
#         event_type=EventType.ARTICLE_READ,
#         patient_id=patient.id,
#         actor_user_id=auth.user.id,
#         subject_type="article",
#         subject_id=article.id,
#     )

#     session.commit()
#     session.refresh(event)

#     return ArticleReadResponse(
#         message="Чтение статьи зарегистрировано",
#         event_id=event.id,
#     )

@router.get(
    "/{article_id}/progress",
    response_model=ArticleProgressResponse,
)
async def get_article_progress(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleProgressResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if not is_assigned:
        ensure_patient_content_access(
            session=session,
            patient=patient,
            content_tag_ids=get_article_tag_ids(
                session=session,
                article_id=article.id,
            ),
            pro_content=article.pro_content,
            is_hidden=article.is_hidden,
        )

    progress = session.exec(
        select(ArticleProgress).where(
            ArticleProgress.article_id == article.id,
            ArticleProgress.patient_id == patient.id,
        )
    ).first()

    if not progress:
        now = utc_now()

        return ArticleProgressResponse(
            article_id=article.id,
            patient_id=patient.id,
            progress_percent=0,
            max_progress_percent=0,
            started_at=now,
            updated_at=now,
            completed_at=None,
        )

    return ArticleProgressResponse(
        article_id=progress.article_id,
        patient_id=progress.patient_id,
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


@router.put(
    "/{article_id}/progress",
    response_model=ArticleProgressResponse,
)
async def save_article_progress(
    article_id: uuid.UUID,
    payload: ArticleProgressUpdateRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleProgressResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    if article.is_hidden:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Статья скрыта",
        )

    if not is_assigned:
        ensure_patient_content_access(
            session=session,
            patient=patient,
            content_tag_ids=get_article_tag_ids(
                session=session,
                article_id=article.id,
            ),
            pro_content=article.pro_content,
            is_hidden=article.is_hidden,
        )

    progress = session.exec(
        select(ArticleProgress).where(
            ArticleProgress.article_id == article.id,
            ArticleProgress.patient_id == patient.id,
        )
    ).first()

    now = utc_now()

    normalized_percent = round(
        min(
            max(payload.progress_percent, 0),
            100,
        ),
        2,
    )

    if not progress:
        progress = ArticleProgress(
            article_id=article.id,
            patient_id=patient.id,
        )

    progress.progress_percent = normalized_percent

    progress.max_progress_percent = max(
        progress.max_progress_percent,
        normalized_percent,
    )

    progress.updated_at = now

    # Статья считается прочитанной при достижении
    # порога завершения (например, 90%).
    if (
        progress.max_progress_percent
        >= ARTICLE_COMPLETION_THRESHOLD
        and progress.completed_at is None
    ):
        progress.completed_at = now

    session.add(progress)
    session.flush()

    # ARTICLE_READ создаётся отдельно для каждого
    # trackable-открытия статьи при достижении порога.
    should_register_read = (
        normalized_percent
        >= ARTICLE_COMPLETION_THRESHOLD
        and payload.is_trackable
        and payload.interaction_id is not None
    )

    if should_register_read:
        opening_event = session.exec(
            select(Event).where(
                Event.event_type
                == EventType.ARTICLE_OPENED,
                Event.interaction_id
                == payload.interaction_id,
                Event.patient_id
                == patient.id,
                Event.subject_type
                == "article",
                Event.subject_id
                == article.id,
            )
        ).first()

        if opening_event:
            existing_read_event = session.exec(
                select(Event).where(
                    Event.event_type
                    == EventType.ARTICLE_READ,
                    Event.interaction_id
                    == payload.interaction_id,
                )
            ).first()

            if not existing_read_event:
                record_event(
                    session=session,
                    event_type=EventType.ARTICLE_READ,
                    patient_id=patient.id,
                    actor_user_id=auth.user.id,
                    program_id=opening_event.program_id,
                    assignment_id=opening_event.assignment_id,
                    interaction_id=payload.interaction_id,
                    source=opening_event.source,
                    subject_type="article",
                    subject_id=article.id,
                    metadata={
                        "progress_percent": (
                            normalized_percent
                        ),
                    },
                )

    # completed_at — пожизненное состояние пациента.
    # При первом достижении порога завершаем активное
    # назначение и синхронизируем программы.
    if progress.completed_at is not None:
        mark_assignment_completed(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        sync_patient_program_enrollments(
            session=session,
            patient_id=patient.id,
        )

    session.commit()
    session.refresh(progress)

    return ArticleProgressResponse(
        article_id=progress.article_id,
        patient_id=progress.patient_id,
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

@router.post(
    "/{article_id}/open",
    response_model=ArticleOpenResponse,
)
async def register_article_open(
    article_id: uuid.UUID,
    payload: ArticleOpenRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleOpenResponse:
    article = session.get(Article, article_id)

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Статья не найдена",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    is_assigned = patient_has_active_assignment(
        session=session,
        patient_id=patient.id,
        assignment_type=AssignmentType.ARTICLE,
        content_id=article.id,
    )

    ensure_patient_can_access_article(
        article=article,
        patient=patient,
        is_assigned=is_assigned,
    )

    existing_event = session.exec(
        select(Event).where(
            Event.event_type
            == EventType.ARTICLE_OPENED,
            Event.interaction_id
            == payload.interaction_id,
        )
    ).first()

    if existing_event:
        if (
            existing_event.patient_id != patient.id
            or existing_event.subject_id != article.id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Идентификатор открытия уже "
                    "используется"
                ),
            )

        return ArticleOpenResponse(
            event_id=existing_event.id,
            interaction_id=payload.interaction_id,
        )

    event = record_event(
        session=session,
        event_type=EventType.ARTICLE_OPENED,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        program_id=payload.program_id,
        assignment_id=payload.assignment_id,
        interaction_id=payload.interaction_id,
        source=payload.source,
        subject_type="article",
        subject_id=article.id,
    )

    session.commit()
    session.refresh(event)

    return ArticleOpenResponse(
        event_id=event.id,
        interaction_id=payload.interaction_id,
    )