import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from sqlmodel import Session, select


BACKEND_DIR = Path(__file__).resolve().parents[1]

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))


from app.core.db import sqlite_engine  # noqa: E402
from app.core.security import hash_password  # noqa: E402
from app.modules.users.enums import UserRole  # noqa: E402
from app.modules.users.models import (  # noqa: E402
    User,
    UserRoleLink,
)
from app.modules.users.utils import get_user_by_email  # noqa: E402


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if value is None or not value:
        raise RuntimeError(
            f"Required environment variable is missing: {name}"
        )

    return value


def parse_bool(value: str | None) -> bool:
    if value is None:
        return False

    return value.strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


def create_or_update_superuser() -> None:
    email = get_required_env(
        "BOOTSTRAP_SUPERUSER_EMAIL"
    ).strip().lower()

    password = get_required_env(
        "BOOTSTRAP_SUPERUSER_PASSWORD"
    )

    first_name = os.getenv(
        "BOOTSTRAP_SUPERUSER_FIRST_NAME",
        "Главный",
    ).strip()

    last_name = os.getenv(
        "BOOTSTRAP_SUPERUSER_LAST_NAME",
        "Администратор",
    ).strip()

    reset_password = parse_bool(
        os.getenv("BOOTSTRAP_SUPERUSER_RESET_PASSWORD")
    )

    if "@" not in email:
        raise RuntimeError("Invalid superuser email")

    if len(password) < 12:
        raise RuntimeError(
            "Superuser password must contain at least 12 characters"
        )

    if len(password) > 128:
        raise RuntimeError(
            "Superuser password must not exceed 128 characters"
        )

    with Session(sqlite_engine) as session:
        user = get_user_by_email(session, email)
        created = user is None

        if user is None:
            user = User(
                email=email,
                hashed_password=hash_password(password),
            )
        elif reset_password:
            user.hashed_password = hash_password(password)
            user.auth_version += 1

        user.first_name = first_name or None
        user.last_name = last_name or None
        user.is_active = True
        user.is_blocked = False
        user.deleted_at = None
        user.email_verified_at = (
            user.email_verified_at or utc_now()
        )
        user.updated_at = utc_now()

        session.add(user)
        session.flush()

        role_links = session.exec(
            select(UserRoleLink).where(
                UserRoleLink.user_id == user.id
            )
        ).all()

        superuser_role_link: UserRoleLink | None = None

        for role_link in role_links:
            if role_link.role == UserRole.SUPERUSER:
                superuser_role_link = role_link
            else:
                role_link.is_primary = False
                session.add(role_link)

        if superuser_role_link is None:
            superuser_role_link = UserRoleLink(
                user_id=user.id,
                role=UserRole.SUPERUSER,
                is_primary=True,
            )
        else:
            superuser_role_link.is_primary = True

        session.add(superuser_role_link)
        session.commit()

    if created:
        print(f"Superuser created: {email}")
    else:
        print(f"Superuser synchronized: {email}")

        if reset_password:
            print("Existing superuser password was changed.")
        else:
            print("Existing superuser password was not changed.")


if __name__ == "__main__":
    create_or_update_superuser()