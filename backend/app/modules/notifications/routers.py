# ./backend/app/modules/notifications/routers.py
import asyncio
import math
import uuid
from datetime import datetime, timezone

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    WebSocket,
    WebSocketDisconnect,
)
from sqlalchemy import func
from sqlmodel import Session, select

from app.core.db import get_session, sqlite_engine
from app.core.security import (
    AuthContext,
    decode_jwt_token,
    ensure_user_can_authenticate,
    get_current_auth,
)
from app.core.websockets.manager import websocket_manager
from app.modules.notifications.enums import (
    NotificationChannel,
)
from app.modules.notifications.models import Notification
from app.modules.notifications.schemas import (
    MarkAllReadResponse,
    NotificationPageResponse,
    NotificationResponse,
    UnreadCountResponse,
)
from app.modules.users.models import User


router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_response(
    notification: Notification,
) -> NotificationResponse:
    return NotificationResponse(
        id=notification.id,
        user_id=notification.user_id,
        notification_type=notification.notification_type,
        title=notification.title,
        message=notification.message,
        action_url=notification.action_url,
        payload=notification.payload_json,
        channels=[
            NotificationChannel(channel)
            for channel in notification.channels_json
        ],
        is_read=notification.is_read,
        created_at=notification.created_at,
        read_at=notification.read_at,
    )


@router.get("", response_model=NotificationPageResponse)
async def list_notifications(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> NotificationPageResponse:
    total_items = int(
        session.exec(
            select(func.count())
            .select_from(Notification)
            .where(
                Notification.user_id == auth.user.id
            )
        ).one()
    )

    unread_count = int(
        session.exec(
            select(func.count())
            .select_from(Notification)
            .where(
                Notification.user_id == auth.user.id,
                Notification.is_read.is_(False),
            )
        ).one()
    )

    notifications = session.exec(
        select(Notification)
        .where(Notification.user_id == auth.user.id)
        .order_by(Notification.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    ).all()

    return NotificationPageResponse(
        items=[
            serialize_response(item)
            for item in notifications
        ],
        page=page,
        page_size=page_size,
        total_items=total_items,
        total_pages=max(
            1,
            math.ceil(total_items / page_size),
        ),
        unread_count=unread_count,
    )


@router.get(
    "/unread-count",
    response_model=UnreadCountResponse,
)
async def get_unread_count(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> UnreadCountResponse:
    count = session.exec(
        select(func.count())
        .select_from(Notification)
        .where(
            Notification.user_id == auth.user.id,
            Notification.is_read.is_(False),
        )
    ).one()

    return UnreadCountResponse(
        unread_count=int(count)
    )


@router.patch(
    "/read-all",
    response_model=MarkAllReadResponse,
)
async def mark_all_notifications_as_read(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> MarkAllReadResponse:
    notifications = session.exec(
        select(Notification).where(
            Notification.user_id == auth.user.id,
            Notification.is_read.is_(False),
        )
    ).all()

    now = utc_now()

    for notification in notifications:
        notification.is_read = True
        notification.read_at = now
        session.add(notification)

    session.commit()

    return MarkAllReadResponse(
        updated_count=len(notifications)
    )


@router.patch(
    "/{notification_id}/read",
    response_model=NotificationResponse,
)
async def mark_notification_as_read(
    notification_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> NotificationResponse:
    notification = session.get(
        Notification,
        notification_id,
    )

    if (
        not notification
        or notification.user_id != auth.user.id
    ):
        raise HTTPException(
            status_code=404,
            detail="Уведомление не найдено",
        )

    if not notification.is_read:
        notification.is_read = True
        notification.read_at = utc_now()

        session.add(notification)
        session.commit()
        session.refresh(notification)

    return serialize_response(notification)


@router.websocket("/ws")
async def notifications_websocket(
    websocket: WebSocket,
) -> None:
    await websocket.accept()

    user_id: uuid.UUID | None = None

    try:
        authentication_message = await asyncio.wait_for(
            websocket.receive_json(),
            timeout=10,
        )

        if authentication_message.get("type") != "authenticate":
            await websocket.close(code=1008)
            return

        token = authentication_message.get("token")

        if not isinstance(token, str):
            await websocket.close(code=1008)
            return

        payload = decode_jwt_token(
            token,
            expected_type="access",
        )

        user_id = uuid.UUID(payload["sub"])
        token_auth_version = int(
            payload["auth_version"]
        )

        with Session(sqlite_engine) as session:
            user = ensure_user_can_authenticate(
                session.get(User, user_id)
            )

            if user.auth_version != token_auth_version:
                await websocket.close(code=1008)
                return

        await websocket_manager.connect(
            user_id=user_id,
            websocket=websocket,
        )

        await websocket.send_json({
            "type": "authenticated",
        })

        while True:
            message = await websocket.receive_json()

            if message.get("type") == "ping":
                await websocket.send_json({
                    "type": "pong",
                })

    except (
        WebSocketDisconnect,
        asyncio.TimeoutError,
        ValueError,
        KeyError,
    ):
        pass
    except Exception:
        try:
            await websocket.close(code=1011)
        except Exception:
            pass
    finally:
        if user_id:
            websocket_manager.disconnect(
                user_id=user_id,
                websocket=websocket,
            )