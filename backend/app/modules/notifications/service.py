# ./backend/app/modules/notifications/service.py
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlmodel import Session

from app.core.email import send_console_email
from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
    NotificationType,
)
from app.modules.notifications.models import Notification
from app.modules.users.models import User


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_notification(
    notification: Notification,
) -> dict[str, Any]:
    return {
        "id": str(notification.id),
        "user_id": str(notification.user_id),
        "notification_type": (
            notification.notification_type.value
        ),
        "title": notification.title,
        "message": notification.message,
        "action_url": notification.action_url,
        "payload": notification.payload_json,
        "channels": notification.channels_json,
        "is_read": notification.is_read,
        "created_at": notification.created_at.isoformat(),
        "read_at": (
            notification.read_at.isoformat()
            if notification.read_at
            else None
        ),
    }


async def send_notification(
    *,
    session: Session,
    user_id: uuid.UUID,
    title: str,
    message: str,
    notification_type: NotificationType = (
        NotificationType.GENERAL
    ),
    channels: list[NotificationChannel] | None = None,
    action_url: str | None = None,
    payload: dict[str, Any] | None = None,
) -> Notification | None:
    """
    ЕДИНАЯ ТОЧКА ОТПРАВКИ УВЕДОМЛЕНИЙ.

    Пример:

        await send_notification(
            session=session,
            user_id=patient_user_id,
            title="Назначен опросник",
            message="Врач назначил вам новый опросник.",
            notification_type=(
                NotificationType.QUESTIONNAIRE_ASSIGNED
            ),
            channels=[
                NotificationChannel.IN_APP,
                NotificationChannel.BROWSER,
            ],
            action_url="/questionnaires",
        )

    IN_APP:
        уведомление сохраняется в базе и отображается
        в колокольчике.

    EMAIL:
        пока выводится в консоль backend.

    BROWSER:
        отправляется через WebSocket. Системное уведомление
        браузера появится, если пользователь дал разрешение
        и приложение открыто.
    """
    selected_channels = channels or [
        NotificationChannel.IN_APP,
    ]

    user = session.get(User, user_id)

    if not user or user.deleted_at is not None:
        return None

    notification: Notification | None = None

    if NotificationChannel.IN_APP in selected_channels:
        notification = Notification(
            user_id=user.id,
            notification_type=notification_type,
            title=title.strip(),
            message=message.strip(),
            action_url=action_url,
            payload_json=payload or {},
            channels_json=[
                channel.value
                for channel in selected_channels
            ],
        )

        session.add(notification)
        session.commit()
        session.refresh(notification)

    if NotificationChannel.EMAIL in selected_channels:
        send_console_email(
            recipient=user.email,
            subject=title,
            message=message,
        )

    websocket_payload = {
        "type": "notification",
        "notification": (
            serialize_notification(notification)
            if notification
            else {
                "id": str(uuid.uuid4()),
                "user_id": str(user.id),
                "notification_type": (
                    notification_type.value
                ),
                "title": title,
                "message": message,
                "action_url": action_url,
                "payload": payload or {},
                "channels": [
                    channel.value
                    for channel in selected_channels
                ],
                "is_read": False,
                "created_at": utc_now().isoformat(),
                "read_at": None,
            }
        ),
    }

    if (
        NotificationChannel.IN_APP in selected_channels
        or NotificationChannel.BROWSER
        in selected_channels
    ):
        await websocket_manager.send_to_user(
            user_id=user.id,
            message=websocket_payload,
        )

    return notification