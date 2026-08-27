# ./backend/app/modules/referrals/utils.py
import hashlib
import secrets

from app.modules.referrals.enums import ReferralSource


def hash_referral_token(token: str) -> str:
    return hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()


def generate_referral_token() -> str:
    return secrets.token_urlsafe(48)


def is_psychiatric_speciality(
    speciality_name: str,
) -> bool:
    """
    Простое и прозрачное правило MVP.

    Если название специальности содержит слово "психиатр",
    направление считается направлением существующего
    психиатрического потока.

    Позже это можно заменить отдельным полем специальности,
    не меняя модель Referral, потому что snapshot уже хранится.
    """
    normalized_name = speciality_name.strip().casefold()

    return "психиатр" in normalized_name


def determine_referral_source(
    speciality_name: str,
) -> ReferralSource:
    if is_psychiatric_speciality(speciality_name):
        return ReferralSource.PSYCHIATRY_EXISTING

    return ReferralSource.KVB_DOCTOR