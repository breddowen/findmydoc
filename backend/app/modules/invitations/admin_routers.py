# ./backend/app/modules/invitations/admin_routers.py
import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy import func
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.email import send_console_email
from app.core.security import AuthContext, require_roles
from app.modules.invitations.admin_schemas import (
    AdminInvitationCreateRequest,
    AdminInvitationCreatedResponse,
    AdminInvitationCreator,
    AdminInvitationEmailResponse,
    AdminInvitationListItem,
    AdminInvitationPageResponse,
)
from app.modules.invitations.admin_utils import (
    ensure_admin_can_invite_role,
    ensure_admin_can_manage_invitation,
    ensure_email_is_available,
    invitation_creator_name,
    role_to_invitation_type,
    update_expired_invitation,
    validate_admin_doctor_speciality,
    validate_admin_patient_record_id,
)
from app.modules.invitations.enums import (
    InvitationStatus,
    InvitationType,
)
from app.modules.invitations.models import Invitation
from app.modules.invitations.utils import (
    build_registration_url,
    create_invitation,
    utc_now,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import Speciality, User


router = APIRouter(
    prefix="/api/v1/invitations/admin",
    tags=["Administrative invitations"],
)


def build_created_response(
    *,
    invitation: Invitation,
    raw_token: str,
) -> AdminInvitationCreatedResponse:
    return AdminInvitationCreatedResponse(
        status="invitation_created",
        invitation_id=invitation.id,
        invitation_type=invitation.invitation_type,
        email=invitation.email,
        expires_at=invitation.expires_at,
        registration_url=build_registration_url(raw_token),
        email_sent_at=invitation.email_sent_at,
        email_send_error=invitation.email_send_error,
    )


def clone_invitation(
    *,
    session: Session,
    source: Invitation,
    created_by_user_id: uuid.UUID,
) -> tuple[Invitation, str]:
    return create_invitation(
        session=session,
        invitation_type=source.invitation_type,
        created_by_user_id=created_by_user_id,
        email=source.email,
        record_id=source.record_id,
        first_name=source.first_name,
        last_name=source.last_name,
        middle_name=source.middle_name,
        fullname=source.fullname,
        gender=source.gender,
        dob=source.dob,
        speciality_id=source.speciality_id,
        doctor_profile_id=source.doctor_profile_id,
        patient_profile_id=source.patient_profile_id,
        relationship_degree=source.relationship_degree,
        send_email=False,
    )


@router.post(
    "",
    response_model=AdminInvitationCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_admin_invitation(
    payload: AdminInvitationCreateRequest,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> AdminInvitationCreatedResponse:
    ensure_admin_can_invite_role(
        auth=auth,
        role=payload.role,
    )

    normalized_email = ensure_email_is_available(
        session=session,
        email=str(payload.email),
    )

    invitation_type = role_to_invitation_type(payload.role)

    record_id = None
    speciality_id = None

    if payload.role == UserRole.PATIENT:
        record_id = validate_admin_patient_record_id(
            session=session,
            record_id=payload.record_id,
        )

    elif payload.record_id is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="record_id доступен только для пациента",
        )

    if payload.role == UserRole.DOCTOR:
        speciality = validate_admin_doctor_speciality(
            session=session,
            speciality_id=payload.speciality_id,
        )
        speciality_id = speciality.id

    elif payload.speciality_id is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Специальность доступна только для врача",
        )

    invitation, raw_token = create_invitation(
        session=session,
        invitation_type=invitation_type,
        created_by_user_id=auth.user.id,
        email=normalized_email,
        record_id=record_id,
        speciality_id=speciality_id,
        send_email=False,
    )

    return build_created_response(
        invitation=invitation,
        raw_token=raw_token,
    )


@router.get(
    "",
    response_model=AdminInvitationPageResponse,
)
async def list_managed_invitations(
    invitation_type: InvitationType | None = Query(
        default=None,
    ),
    invitation_status: InvitationStatus | None = Query(
        default=None,
        alias="status",
    ),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> AdminInvitationPageResponse:
    filters = []

    if auth.active_role == UserRole.MED_ASSISTANT:
        filters.extend([
            Invitation.created_by_user_id == auth.user.id,
            Invitation.invitation_type.in_(
                [
                    InvitationType.PATIENT,
                    InvitationType.DOCTOR,
                    InvitationType.RELATIVE,
                ]
            ),
        ])

    if invitation_type is not None:
        filters.append(
            Invitation.invitation_type
            == invitation_type
        )

    if invitation_status is not None:
        filters.append(
            Invitation.status == invitation_status
        )

    count_statement = select(
        func.count(Invitation.id)
    )

    invitations_statement = select(Invitation)

    if filters:
        count_statement = count_statement.where(*filters)
        invitations_statement = (
            invitations_statement.where(*filters)
        )

    total_items = session.exec(
        count_statement
    ).one()

    total_pages = max(
        1,
        (total_items + page_size - 1) // page_size,
    )

    normalized_page = min(page, total_pages)

    invitations = session.exec(
        invitations_statement
        .order_by(Invitation.created_at.desc())
        .offset((normalized_page - 1) * page_size)
        .limit(page_size)
    ).all()

    now = utc_now()
    items: list[AdminInvitationListItem] = []

    for invitation in invitations:
        update_expired_invitation(
            session=session,
            invitation=invitation,
            now=now,
        )

        creator = session.get(
            User,
            invitation.created_by_user_id,
        )

        if not creator:
            continue

        speciality_name = None

        if invitation.speciality_id:
            speciality = session.get(
                Speciality,
                invitation.speciality_id,
            )

            speciality_name = (
                speciality.name if speciality else None
            )

        items.append(
            AdminInvitationListItem(
                id=invitation.id,
                invitation_type=invitation.invitation_type,
                status=invitation.status,
                email=invitation.email,
                record_id=invitation.record_id,
                speciality_id=invitation.speciality_id,
                speciality_name=speciality_name,
                creator=AdminInvitationCreator(
                    id=creator.id,
                    email=creator.email,
                    full_name=invitation_creator_name(
                        creator
                    ),
                ),
                created_at=invitation.created_at,
                expires_at=invitation.expires_at,
                accepted_at=invitation.accepted_at,
                revoked_at=invitation.revoked_at,
                email_sent_at=invitation.email_sent_at,
                email_send_error=(
                    invitation.email_send_error
                ),
                can_revoke=(
                    invitation.status
                    == InvitationStatus.PENDING
                ),
                can_resend=(
                    invitation.status
                    != InvitationStatus.ACCEPTED
                ),
            )
        )

    session.commit()

    return AdminInvitationPageResponse(
        items=items,
        page=normalized_page,
        page_size=page_size,
        total_items=total_items,
        total_pages=total_pages,
    )


@router.post(
    "/{invitation_id}/send",
    response_model=AdminInvitationEmailResponse,
)
async def send_admin_invitation_email(
    invitation_id: uuid.UUID,
    auth: AuthContext = Depends(
        require_roles(
            UserRole.SUPERUSER,
            UserRole.MED_ASSISTANT,
        )
    ),
    session: Session = Depends(get_session),
) -> AdminInvitationEmailResponse:
    source = session.get(
        Invitation,
        invitation_id,
    )

    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Приглашение не найдено",
        )

    ensure_admin_can_manage_invitation(
        auth=auth,
        invitation=source,
    )

    ensure_email_is_available(
        session=session,
        email=source.email,
    )

    if source.invitation_type == InvitationType.PATIENT:
        validate_admin_patient_record_id(
            session=session,
            record_id=source.record_id,
        )

    if source.invitation_type == InvitationType.DOCTOR:
        validate_admin_doctor_speciality(
            session=session,
            speciality_id=source.speciality_id,
        )

    invitation, raw_token = clone_invitation(
        session=session,
        source=source,
        created_by_user_id=auth.user.id,
    )

    registration_url = build_registration_url(raw_token)

    try:
        send_console_email(
            recipient=invitation.email,
            subject="Приглашение в MentalMe",
            message=(
                "Для регистрации в MentalMe перейдите "
                "по ссылке:"
            ),
            action_url=registration_url,
        )
    except Exception as error:
        invitation.email_sent_at = None
        invitation.email_send_error = str(error)[:1000]

        session.add(invitation)
        session.commit()

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                "Приглашение создано, но отправить письмо "
                "не удалось"
            ),
        ) from error

    invitation.email_sent_at = utc_now()
    invitation.email_send_error = None

    session.add(invitation)
    session.commit()
    session.refresh(invitation)

    return AdminInvitationEmailResponse(
        status="invitation_created",
        invitation_id=invitation.id,
        invitation_type=invitation.invitation_type,
        email=invitation.email,
        expires_at=invitation.expires_at,
        registration_url=registration_url,
        email_sent_at=invitation.email_sent_at,
        email_send_error=None,
    )