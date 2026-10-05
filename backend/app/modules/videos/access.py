# ./backend/app/modules/videos/access.py

import uuid

from fastapi import HTTPException
from sqlmodel import Session

from app.core.security import AuthContext
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
)
from app.modules.programs.enums import ProgramItemType
from app.modules.programs.models import Program
from app.modules.programs.utils import (
    ensure_patient_program_content_access,
    get_program_content_item,
)
from app.modules.users.enums import UserRole
from app.modules.videos.models import Video


STAFF_ROLES = {
    UserRole.SUPERUSER,
    UserRole.MED_ASSISTANT,
    UserRole.DOCTOR,
}


def validate_program_context(
    program_id: uuid.UUID | None,
    program_stage_id: uuid.UUID | None,
) -> None:
    if program_stage_id is not None and program_id is None:
        raise HTTPException(
            status_code=422,
            detail="Для этапа необходимо указать программу",
        )


def ensure_video_access(
    *,
    session: Session,
    auth: AuthContext,
    video: Video,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    validate_program_context(
        program_id,
        program_stage_id,
    )

    if auth.active_role in STAFF_ROLES:
        return

    if auth.active_role != UserRole.PATIENT:
        raise HTTPException(
            status_code=403,
            detail="Нет доступа к видео",
        )

    if video.is_hidden:
        raise HTTPException(
            status_code=404,
            detail="Видео не найдено",
        )

    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    if program_id is not None:
        ensure_patient_program_content_access(
            session=session,
            patient=patient,
            program_id=program_id,
            stage_id=program_stage_id,
            content_type=ProgramItemType.VIDEO,
            content_id=video.id,
            pro_content=video.pro_content,
        )
        return

    if video.pro_content and not patient.pro_enabled:
        raise HTTPException(
            status_code=403,
            detail="Требуется Pro-доступ",
        )


def ensure_video_poster_access(
    *,
    session: Session,
    auth: AuthContext,
    video: Video,
    program_id: uuid.UUID | None = None,
    program_stage_id: uuid.UUID | None = None,
) -> None:
    validate_program_context(
        program_id,
        program_stage_id,
    )

    if auth.active_role in STAFF_ROLES:
        return

    if (
        auth.active_role != UserRole.PATIENT
        or video.is_hidden
    ):
        raise HTTPException(
            status_code=404,
            detail="Обложка не найдена",
        )

    if program_id is not None:
        program = session.get(Program, program_id)

        if program is None or program.is_hidden:
            raise HTTPException(
                status_code=404,
                detail="Программа не найдена",
            )

        item = get_program_content_item(
            session=session,
            program_id=program.id,
            stage_id=program_stage_id,
            content_type=ProgramItemType.VIDEO,
            content_id=video.id,
        )

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="Видео не входит в эту программу",
            )

        # Обложка карточки — не сам Pro-материал.
        return

    if not video.is_library_hidden:
        return

    ensure_video_access(
        session=session,
        auth=auth,
        video=video,
    )