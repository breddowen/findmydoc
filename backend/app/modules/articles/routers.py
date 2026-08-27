# ./backend/app/modules/articles/routers.py
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
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


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@router.get(
    "",
    response_model=list[ArticleListItem],
)
async def list_articles(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[ArticleListItem]:
    articles = session.exec(
        select(Article).order_by(
            Article.created_at.desc()
        )
    ).all()

    if auth.active_role != UserRole.PATIENT:
        return [
            serialize_article_list_item(
                session=session,
                article=article,
            )
            for article in articles
        ]

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    result: list[ArticleListItem] = []

    for article in articles:
        # Скрытые статьи не показываются даже в случае
        # активного назначения.
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

        # Назначенная статья доступна независимо
        # от тегов пациента.
        if (
            not is_assigned
            and not patient_can_see_content(
                session=session,
                patient=patient,
                content_tag_ids=tag_ids,
                is_hidden=article.is_hidden,
            )
        ):
            continue

        # Назначение также даёт доступ к Pro-контенту
        # независимо от статуса Pro пациента.
        can_access = (
            is_assigned
            or not article.pro_content
            or patient.pro_enabled
        )

        result.append(
            serialize_article_list_item(
                session=session,
                article=article,
                can_access=can_access,
            )
        )

    return result


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

        # Скрытие имеет приоритет над назначением.
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

    return serialize_article(
        session=session,
        article=article,
    )


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


@router.post(
    "/{article_id}/read",
    response_model=ArticleReadResponse,
)
async def mark_article_as_read(
    article_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ArticleReadResponse:
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

    event = record_event(
        session=session,
        event_type=EventType.ARTICLE_READ,
        patient_id=patient.id,
        actor_user_id=auth.user.id,
        subject_type="article",
        subject_id=article.id,
    )

    session.commit()
    session.refresh(event)

    return ArticleReadResponse(
        message="Чтение статьи зарегистрировано",
        event_id=event.id,
    )

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

    was_completed = (
        progress.completed_at is not None
    )

    progress.progress_percent = (
        normalized_percent
    )

    progress.max_progress_percent = max(
        progress.max_progress_percent,
        normalized_percent,
    )

    progress.updated_at = now

    if (
        progress.max_progress_percent >= 100
        and progress.completed_at is None
    ):
        progress.completed_at = now

    session.add(progress)
    session.flush()

    # Событие создаётся только один раз
    # при первом достижении 100%.
    if (
        not was_completed
        and progress.completed_at is not None
    ):
        record_event(
            session=session,
            event_type=EventType.ARTICLE_READ,
            patient_id=patient.id,
            actor_user_id=auth.user.id,
            subject_type="article",
            subject_id=article.id,
            metadata={
                "progress_percent": 100,
            },
        )

    # При достижении 100% завершаем
    # активное назначение статьи.
    if progress.completed_at is not None:
        mark_assignment_completed(
            session=session,
            patient_id=patient.id,
            assignment_type=AssignmentType.ARTICLE,
            content_id=article.id,
        )

        # Синхронизируем программы пациента,
        # в которые входит эта статья.
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