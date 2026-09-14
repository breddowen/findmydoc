# ./backend/app/modules/programs/consultation_routers.py

import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import require_roles
from app.modules.programs.consultation_schemas import (
    ProgramConsultationsResponse,
    StageConsultationsResponse,
    StageConsultationsUpdateRequest,
)
from app.modules.programs.consultation_service import (
    lock_program_for_structure_edit,
    serialize_stage_consultations,
    update_stage_consultations,
)
from app.modules.programs.models import Program, ProgramStage
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/programs/manage",
    tags=["Programs: consultations"],
    dependencies=[
        Depends(
            require_roles(
                UserRole.SUPERUSER,
                UserRole.MED_ASSISTANT,
            )
        ),
    ],
)


@router.get(
    "/{program_id}/consultations",
    response_model=ProgramConsultationsResponse,
)
def get_program_consultations(
    program_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> ProgramConsultationsResponse:
    program = session.get(Program, program_id)

    if program is None:
        raise HTTPException(
            status_code=404,
            detail="Программа не найдена",
        )

    stages = session.exec(
        select(ProgramStage)
        .where(
            ProgramStage.program_id == program.id
        )
        .order_by(
            ProgramStage.order_index,
            ProgramStage.id,
        )
    ).all()

    return ProgramConsultationsResponse(
        id=program.id,
        title=program.title,
        stages=[
            serialize_stage_consultations(
                session=session,
                stage=stage,
            )
            for stage in stages
        ],
    )


@router.put(
    "/{program_id}/stages/{stage_id}/consultations",
    response_model=StageConsultationsResponse,
)
def save_stage_consultations(
    program_id: uuid.UUID,
    stage_id: uuid.UUID,
    payload: StageConsultationsUpdateRequest,
    session: Session = Depends(get_session),
) -> StageConsultationsResponse:
    try:
        program = lock_program_for_structure_edit(
            session=session,
            program_id=program_id,
        )

        stage = session.get(ProgramStage, stage_id)

        if stage is None or stage.program_id != program.id:
            raise HTTPException(
                status_code=404,
                detail="Этап не найден",
            )

        response = update_stage_consultations(
            session=session,
            program=program,
            stage=stage,
            payload=payload,
        )

        session.commit()
        return response

    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=409,
            detail=(
                "Не удалось сохранить консультации "
                "из-за конфликта данных. Обновите этап."
            ),
        ) from error

    except Exception:
        session.rollback()
        raise