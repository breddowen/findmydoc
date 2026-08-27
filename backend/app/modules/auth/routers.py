# ./backend/app/modules/auth/routers.py
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from webauthn import (
    generate_authentication_options,
    generate_registration_options,
    options_to_json,
    verify_authentication_response,
    verify_registration_response,
)
from webauthn.helpers import (
    parse_authentication_credential_json,
    parse_registration_credential_json,
)
from webauthn.helpers.structs import (
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
    UserVerificationRequirement,
)

from app.core.config import settings
from app.core.db import get_session
from app.core.security import (
    AuthContext,
    create_access_token,
    create_role_selection_token,
    decode_jwt_token,
    ensure_user_can_authenticate,
    get_current_auth,
    hash_password,
    validate_password_strength,
    verify_password,
)
from app.modules.auth.models import (
    ActionTokenType,
    PasskeyCredential,
    WebAuthnChallenge,
    WebAuthnChallengeType,
)
from app.modules.auth.schemas import (
    EmailVerificationConfirmRequest,
    LoginResponse,
    MessageResponse,
    PasskeyAuthenticationOptionsResponse,
    PasskeyAuthenticationVerifyRequest,
    PasskeyRegistrationOptionsRequest,
    PasskeyRegistrationOptionsResponse,
    PasskeyRegistrationVerifyRequest,
    PasswordChangeRequest,
    PasswordLoginRequest,
    PasswordResetConfirmRequest,
    PasswordResetRequest,
    SelectRoleRequest,
    TokenResponse,
)
from app.modules.auth.utils import (
    base64url_to_bytes,
    bytes_to_base64url,
    credential_user_handle,
    get_valid_action_token,
    send_password_reset_email,
    send_verification_email,
)
from app.modules.users.enums import UserRole
from app.modules.users.models import User
from app.modules.users.schemas import RoleResponse
from app.modules.users.utils import (
    get_primary_role,
    get_user_by_email,
    get_user_roles,
    user_has_role,
)


router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def normalize_database_datetime(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)

    return value


def create_login_response(
    *,
    session: Session,
    user: User,
) -> LoginResponse:
    role_links = get_user_roles(session, user.id)

    if not role_links:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Пользователю не назначена ни одна роль",
        )

    if len(role_links) == 1:
        active_role = role_links[0].role

        return LoginResponse(
            status="authenticated",
            access_token=create_access_token(
                user=user,
                active_role=active_role,
            ),
            token_type="bearer",
            active_role=active_role,
        )

    return LoginResponse(
        status="role_selection_required",
        role_selection_token=create_role_selection_token(user=user),
        roles=[
            RoleResponse(
                role=role_link.role,
                is_primary=role_link.is_primary,
            )
            for role_link in role_links
        ],
    )


@router.post("/login", response_model=LoginResponse)
async def login(
    payload: PasswordLoginRequest,
    session: Session = Depends(get_session),
) -> LoginResponse:
    user = get_user_by_email(session, str(payload.email))

    if not user or not verify_password(
        payload.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
        )

    ensure_user_can_authenticate(user)

    return create_login_response(
        session=session,
        user=user,
    )


@router.post("/token", response_model=TokenResponse)
async def swagger_token_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
) -> TokenResponse:
    user = get_user_by_email(session, form_data.username)

    if not user or not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    ensure_user_can_authenticate(user)

    requested_role: UserRole | None = None

    if form_data.scopes:
        try:
            requested_role = UserRole(form_data.scopes[0])
        except ValueError as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Неизвестная роль в OAuth2 scope",
            ) from error

    active_role = requested_role or get_primary_role(
        session,
        user.id,
    )

    if not active_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Пользователю не назначена роль",
        )

    if not user_has_role(session, user.id, active_role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Запрошенная роль пользователю не назначена",
        )

    return TokenResponse(
        access_token=create_access_token(
            user=user,
            active_role=active_role,
        ),
        active_role=active_role,
    )


@router.post("/select-role", response_model=TokenResponse)
async def select_role(
    payload: SelectRoleRequest,
    session: Session = Depends(get_session),
) -> TokenResponse:
    token_payload = decode_jwt_token(
        payload.role_selection_token,
        expected_type="role_selection",
    )

    try:
        user_id = uuid.UUID(token_payload["sub"])
        auth_version = int(token_payload["auth_version"])
    except (ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Некорректный токен выбора роли",
        ) from error

    user = ensure_user_can_authenticate(
        session.get(User, user_id)
    )

    if user.auth_version != auth_version:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Токен выбора роли больше не действителен",
        )

    if not user_has_role(session, user.id, payload.role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Эта роль не назначена пользователю",
        )

    return TokenResponse(
        access_token=create_access_token(
            user=user,
            active_role=payload.role,
        ),
        active_role=payload.role,
    )


@router.post("/change-password", response_model=MessageResponse)
async def change_password(
    payload: PasswordChangeRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> MessageResponse:
    if not verify_password(
        payload.current_password,
        auth.user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Текущий пароль указан неверно",
        )

    if payload.new_password != payload.new_password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Новые пароли не совпадают",
        )

    validate_password_strength(payload.new_password)

    auth.user.hashed_password = hash_password(payload.new_password)
    auth.user.auth_version += 1
    auth.user.updated_at = utc_now()

    session.add(auth.user)
    session.commit()

    return MessageResponse(
        message="Пароль изменён. Выполните вход повторно."
    )


@router.post(
    "/password-reset/request",
    response_model=MessageResponse,
)
async def request_password_reset(
    payload: PasswordResetRequest,
    session: Session = Depends(get_session),
) -> MessageResponse:
    user = get_user_by_email(session, str(payload.email))

    if (
        user
        and user.deleted_at is None
        and user.is_active
        and not user.is_blocked
    ):
        send_password_reset_email(
            session=session,
            user=user,
        )

    return MessageResponse(
        message=(
            "Если аккаунт с таким email существует, "
            "ссылка будет отправлена."
        )
    )


@router.post(
    "/password-reset/confirm",
    response_model=MessageResponse,
)
async def confirm_password_reset(
    payload: PasswordResetConfirmRequest,
    session: Session = Depends(get_session),
) -> MessageResponse:
    if payload.new_password != payload.new_password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Пароли не совпадают",
        )

    validate_password_strength(payload.new_password)

    action_token = get_valid_action_token(
        session=session,
        raw_token=payload.token,
        token_type=ActionTokenType.PASSWORD_RESET,
    )

    if not action_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ссылка недействительна или просрочена",
        )

    user = ensure_user_can_authenticate(
        session.get(User, action_token.user_id)
    )

    user.hashed_password = hash_password(payload.new_password)
    user.auth_version += 1
    user.updated_at = utc_now()

    action_token.consumed_at = utc_now()

    session.add(user)
    session.add(action_token)
    session.commit()

    return MessageResponse(
        message="Пароль восстановлен. Теперь можно войти."
    )


@router.post(
    "/email-verification/resend",
    response_model=MessageResponse,
)
async def resend_email_verification(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> MessageResponse:
    if auth.user.email_verified_at is not None:
        return MessageResponse(
            message="Email уже подтверждён"
        )

    send_verification_email(
        session=session,
        user=auth.user,
    )

    return MessageResponse(
        message="Ссылка подтверждения сформирована"
    )


@router.post(
    "/email-verification/confirm",
    response_model=MessageResponse,
)
async def confirm_email_verification(
    payload: EmailVerificationConfirmRequest,
    session: Session = Depends(get_session),
) -> MessageResponse:
    action_token = get_valid_action_token(
        session=session,
        raw_token=payload.token,
        token_type=ActionTokenType.EMAIL_VERIFICATION,
    )

    if not action_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ссылка недействительна или просрочена",
        )

    user = session.get(User, action_token.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )

    now = utc_now()

    user.email_verified_at = now
    user.updated_at = now
    action_token.consumed_at = now

    session.add(user)
    session.add(action_token)
    session.commit()

    return MessageResponse(message="Email подтверждён")


@router.post(
    "/passkeys/registration/options",
    response_model=PasskeyRegistrationOptionsResponse,
)
async def passkey_registration_options(
    payload: PasskeyRegistrationOptionsRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> PasskeyRegistrationOptionsResponse:
    existing_passkeys = session.exec(
        select(PasskeyCredential).where(
            PasskeyCredential.user_id == auth.user.id
        )
    ).all()

    exclude_credentials = [
        PublicKeyCredentialDescriptor(
            id=base64url_to_bytes(passkey.credential_id)
        )
        for passkey in existing_passkeys
    ]

    options = generate_registration_options(
        rp_id=settings.WEBAUTHN_RP_ID,
        rp_name=settings.WEBAUTHN_RP_NAME,
        user_id=credential_user_handle(auth.user.id),
        user_name=auth.user.email,
        user_display_name=(
            " ".join(
                part
                for part in [
                    auth.user.first_name,
                    auth.user.last_name,
                ]
                if part
            )
            or auth.user.email
        ),
        exclude_credentials=exclude_credentials,
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,
            user_verification=UserVerificationRequirement.REQUIRED,
        ),
    )

    challenge = WebAuthnChallenge(
        challenge=bytes_to_base64url(options.challenge),
        challenge_type=WebAuthnChallengeType.REGISTRATION,
        user_id=auth.user.id,
        expires_at=utc_now()
        + timedelta(
            seconds=settings.WEBAUTHN_CHALLENGE_EXPIRE_SECONDS
        ),
    )

    session.add(challenge)
    session.commit()
    session.refresh(challenge)

    return PasskeyRegistrationOptionsResponse(
        challenge_id=challenge.id,
        options=json.loads(options_to_json(options)),
    )


@router.post(
    "/passkeys/registration/verify",
    response_model=MessageResponse,
)
async def verify_passkey_registration(
    payload: PasskeyRegistrationVerifyRequest,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> MessageResponse:
    challenge = session.get(
        WebAuthnChallenge,
        payload.challenge_id,
    )

    if (
        not challenge
        or challenge.challenge_type
        != WebAuthnChallengeType.REGISTRATION
        or challenge.user_id != auth.user.id
        or challenge.consumed_at is not None
        or normalize_database_datetime(challenge.expires_at) <= utc_now()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="WebAuthn challenge недействителен или просрочен",
        )

    try:
        credential = parse_registration_credential_json(
            json.dumps(payload.credential)
        )

        verification = verify_registration_response(
            credential=credential,
            expected_challenge=base64url_to_bytes(
                challenge.challenge
            ),
            expected_rp_id=settings.WEBAUTHN_RP_ID,
            expected_origin=settings.WEBAUTHN_ORIGIN,
            require_user_verification=True,
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Не удалось проверить passkey: {error}",
        ) from error

    credential_id = bytes_to_base64url(
        verification.credential_id
    )

    duplicate = session.exec(
        select(PasskeyCredential).where(
            PasskeyCredential.credential_id == credential_id
        )
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Этот passkey уже зарегистрирован",
        )

    transports: list[str] = []

    response = payload.credential.get("response", {})
    raw_transports = response.get("transports", [])

    if isinstance(raw_transports, list):
        transports = [str(item) for item in raw_transports]

    passkey = PasskeyCredential(
        user_id=auth.user.id,
        credential_id=credential_id,
        public_key=verification.credential_public_key,
        sign_count=verification.sign_count,
        name=payload.name.strip(),
        transports_json=json.dumps(transports),
    )

    challenge.consumed_at = utc_now()

    session.add(passkey)
    session.add(challenge)
    session.commit()

    return MessageResponse(message="Passkey добавлен")


@router.post(
    "/passkeys/authentication/options",
    response_model=PasskeyAuthenticationOptionsResponse,
)
async def passkey_authentication_options(
    session: Session = Depends(get_session),
) -> PasskeyAuthenticationOptionsResponse:
    options = generate_authentication_options(
        rp_id=settings.WEBAUTHN_RP_ID,
        user_verification=UserVerificationRequirement.REQUIRED,
    )

    challenge = WebAuthnChallenge(
        challenge=bytes_to_base64url(options.challenge),
        challenge_type=WebAuthnChallengeType.AUTHENTICATION,
        expires_at=utc_now()
        + timedelta(
            seconds=settings.WEBAUTHN_CHALLENGE_EXPIRE_SECONDS
        ),
    )

    session.add(challenge)
    session.commit()
    session.refresh(challenge)

    return PasskeyAuthenticationOptionsResponse(
        challenge_id=challenge.id,
        options=json.loads(options_to_json(options)),
    )


@router.post(
    "/passkeys/authentication/verify",
    response_model=LoginResponse,
)
async def verify_passkey_authentication(
    payload: PasskeyAuthenticationVerifyRequest,
    session: Session = Depends(get_session),
) -> LoginResponse:
    challenge = session.get(
        WebAuthnChallenge,
        payload.challenge_id,
    )

    if (
        not challenge
        or challenge.challenge_type
        != WebAuthnChallengeType.AUTHENTICATION
        or challenge.consumed_at is not None
        or normalize_database_datetime(challenge.expires_at) <= utc_now()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="WebAuthn challenge недействителен или просрочен",
        )

    raw_credential_id = payload.credential.get("rawId")

    if not raw_credential_id:
        raw_credential_id = payload.credential.get("id")

    if not isinstance(raw_credential_id, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credential ID отсутствует",
        )

    passkey = session.exec(
        select(PasskeyCredential).where(
            PasskeyCredential.credential_id == raw_credential_id
        )
    ).first()

    if not passkey:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Passkey не зарегистрирован",
        )

    user = ensure_user_can_authenticate(
        session.get(User, passkey.user_id)
    )

    try:
        credential = parse_authentication_credential_json(
            json.dumps(payload.credential)
        )

        verification = verify_authentication_response(
            credential=credential,
            expected_challenge=base64url_to_bytes(
                challenge.challenge
            ),
            expected_rp_id=settings.WEBAUTHN_RP_ID,
            expected_origin=settings.WEBAUTHN_ORIGIN,
            credential_public_key=passkey.public_key,
            credential_current_sign_count=passkey.sign_count,
            require_user_verification=True,
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Не удалось проверить passkey: {error}",
        ) from error

    now = utc_now()

    passkey.sign_count = verification.new_sign_count
    passkey.last_used_at = now
    challenge.consumed_at = now

    session.add(passkey)
    session.add(challenge)
    session.commit()

    return create_login_response(
        session=session,
        user=user,
    )


@router.get("/passkeys")
async def list_passkeys(
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    passkeys = session.exec(
        select(PasskeyCredential)
        .where(PasskeyCredential.user_id == auth.user.id)
        .order_by(PasskeyCredential.created_at.desc())
    ).all()

    return [
        {
            "id": str(passkey.id),
            "name": passkey.name,
            "created_at": passkey.created_at.isoformat(),
            "last_used_at": (
                passkey.last_used_at.isoformat()
                if passkey.last_used_at
                else None
            ),
        }
        for passkey in passkeys
    ]


@router.delete(
    "/passkeys/{passkey_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_passkey(
    passkey_id: uuid.UUID,
    auth: AuthContext = Depends(get_current_auth),
    session: Session = Depends(get_session),
) -> None:
    passkey = session.get(PasskeyCredential, passkey_id)

    if not passkey or passkey.user_id != auth.user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passkey не найден",
        )

    session.delete(passkey)
    session.commit()