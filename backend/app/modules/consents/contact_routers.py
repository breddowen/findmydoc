# ./backend/app/modules/consents/contact_routers.py
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.security import AuthContext, require_roles
from app.core.transactions import lock_patient_for_write
from app.modules.consents.contact_schemas import (
    ContactRequestCreateRequest,
    ContactRequestResponse,
)
from app.modules.consents.contact_service import (
    ensure_assistant_contact_allowed,
)
from app.modules.content.utils import (
    get_patient_profile_by_user_id,
)
from app.modules.notifications.enums import NotificationType
from app.modules.notifications.models import Notification
from app.modules.notifications.transactional import (
    create_in_app_notification,
    publish_saved_notifications,
    snapshot_notifications,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import User, UserRoleLink


router = APIRouter(
    prefix="/api/v1/consents",
    tags=["Assistant contact"],
)


@router.post(
    "/contact-request",
    response_model=ContactRequestResponse,
)
async def request_assistant_contact(
    payload: ContactRequestCreateRequest,
    auth: AuthContext = Depends(
        require_roles(UserRole.PATIENT)
    ),
    session: Session = Depends(get_session),
) -> ContactRequestResponse:
    patient = get_patient_profile_by_user_id(
        session=session,
        user_id=auth.user.id,
    )

    snapshots = []

    try:
        lock_patient_for_write(
            session=session,
            patient_id=patient.id,
        )

        now = datetime.now(timezone.utc)
        action_url = f"/patients/{patient.id}"

        # Повторные клики в течение 15 минут
        # не создают новые уведомления.
        recent_notification = session.exec(
            select(Notification)
            .where(
                Notification.notification_type
                == NotificationType.CONTACT_REQUESTED,
                Notification.action_url == action_url,
                Notification.created_at
                >= now - timedelta(minutes=15),
            )
            .order_by(Notification.created_at.desc())
        ).first()

        ensure_assistant_contact_allowed(
            session=session,
            patient_id=patient.id,
            user_id=auth.user.id,
            source="callback_request",
            document_version=payload.document_version,
        )

        if recent_notification is not None:
            response = ContactRequestResponse(
                requested_at=recent_notification.created_at,
                already_requested=True,
                message=(
                    "Запрос уже передан ассистенту. "
                    "Повторно отправлять его не нужно."
                ),
            )

            session.commit()
            return response

        staff_links = session.exec(
            select(UserRoleLink).where(
                UserRoleLink.role.in_(
                    [
                        UserRole.SUPERUSER,
                        UserRole.MED_ASSISTANT,
                    ]
                )
            )
        ).all()

        recipient_ids = {
            link.user_id
            for link in staff_links
        }

        recipients = []

        for user_id in sorted(recipient_ids, key=str):
            user = session.get(User, user_id)

            if (
                user
                and user.deleted_at is None
                and user.is_active
                and not user.is_blocked
            ):
                recipients.append(user)

        if not recipients:
            raise HTTPException(
                status_code=503,
                detail=(
                    "Не удалось передать запрос ассистенту. "
                    "Попробуйте позже или свяжитесь с клиникой."
                ),
            )

        request_id = uuid.uuid4()
        notifications = []

        for recipient in recipients:
            notifications.append(
                create_in_app_notification(
                    session=session,
                    user_id=recipient.id,
                    title="Пациент просит связаться с ним",
                    message=(
                        "Получен запрос на звонок ассистента. "
                        "Откройте карточку пациента."
                    ),
                    notification_type=(
                        NotificationType.CONTACT_REQUESTED
                    ),
                    action_url=action_url,
                    payload={
                        "patient_id": str(patient.id),
                        "contact_request_id": str(request_id),
                    },
                )
            )

        snapshots = snapshot_notifications(
            session=session,
            notifications=notifications,
        )

        response = ContactRequestResponse(
            requested_at=now,
            already_requested=False,
            message=(
                "Запрос передан ассистенту. "
                "С Вами свяжутся в рабочее время клиники."
            ),
        )

        # Разрешение на контакт и уведомления
        # сохраняются одной транзакцией.
        session.commit()

    except Exception:
        session.rollback()
        raise

    # Ошибка WebSocket не отменяет сохранённый запрос.
    await publish_saved_notifications(snapshots)

    return response