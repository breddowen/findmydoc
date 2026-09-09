# ./backend/app/modules/tags/life_aspect_patient_routers.py
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import (
    AuthContext,
    require_roles,
)
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
)
from app.modules.tags.life_aspect_catalog import (
    build_patient_life_aspects,
)
from app.modules.tags.life_aspect_schemas import (
    LifeAspectPatientResponse,
)
from app.modules.users.enums import UserRole


router = APIRouter(
    prefix="/api/v1/life-aspects",
    tags=["Life aspects: patient"],
)


@router.get(
    "/patient",
    response_model=list[LifeAspectPatientResponse],
)
async def list_life_aspects_for_patient(
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> list[LifeAspectPatientResponse]:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    return build_patient_life_aspects(
        session=session,
        patient=patient,
    )