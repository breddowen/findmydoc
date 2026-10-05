# ./backend/app/modules/videos/catalog_routers.py

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.modules.content.utils import (
    get_patient_effective_tag_ids,
    get_patient_profile_by_user_id,
    tags_match,
)
from app.modules.users.enums import UserRole
from app.modules.videos.models import Video
from app.modules.videos.schemas import VideoCatalogItem
from app.modules.videos.service import serialize_video


router = APIRouter(
    prefix="/api/v1/videos",
    tags=["Videos: patient catalog"],
)

# Как в текущем каталоге статей:
# показываем все материалы, подходящие по тегам — выше.
STRICT_PATIENT_VIDEO_TAG_FILTER = False


@router.get(
    "",
    response_model=list[VideoCatalogItem],
)
def list_videos_for_patient(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[VideoCatalogItem]:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    patient_tag_ids = get_patient_effective_tag_ids(
        session=session,
        patient=patient,
    )

    videos = session.exec(
        select(Video)
        .where(
            Video.is_hidden.is_(False),
            Video.is_library_hidden.is_(False),
        )
        .order_by(
            Video.created_at.desc(),
            Video.id.asc(),
        )
    ).all()

    ranked = []

    for video in videos:
        serialized = serialize_video(
            session=session,
            video=video,
        )

        matches = tags_match(
            patient_tag_ids=patient_tag_ids,
            content_tag_ids={
                tag.id
                for tag in serialized.tags
            },
        )

        if STRICT_PATIENT_VIDEO_TAG_FILTER and not matches:
            continue

        item = VideoCatalogItem(
            **serialized.model_dump(),
            can_access=(
                not video.pro_content
                or patient.pro_enabled
            ),
        )

        ranked.append((matches, item))

    # Стабильная сортировка сохраняет исходный порядок
    # по дате и id внутри каждой группы.
    ranked.sort(
        key=lambda row: row[0],
        reverse=True,
    )

    return [
        item
        for _, item in ranked[offset:offset + limit]
    ]