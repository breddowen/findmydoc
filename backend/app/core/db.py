# ./backend/app/core/db.py
import os
from collections.abc import Generator
from pathlib import Path

from sqlalchemy.engine import make_url
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


BACKEND_DIR = Path(__file__).resolve().parents[2]


def resolve_database_url(database_url: str) -> str:
    if not database_url.startswith("sqlite"):
        return database_url

    url = make_url(database_url)
    database = url.database

    if not database or database == ":memory:":
        return database_url

    database_path = Path(database)

    if not database_path.is_absolute():
        database_path = (BACKEND_DIR / database_path).resolve()

    return f"sqlite:///{database_path.as_posix()}"


DATABASE_URL = resolve_database_url(settings.DATABASE_URL)

connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine_kwargs = {
    "echo": False,
    "connect_args": connect_args,
    "pool_pre_ping": True,
}

if not DATABASE_URL.startswith("sqlite"):
    engine_kwargs.update({
        "pool_size": 10,
        "max_overflow": 20,
        "pool_timeout": 30,
        "pool_recycle": 1800,
    })

sqlite_engine = create_engine(
    DATABASE_URL,
    **engine_kwargs,
)


def get_db_path() -> str | None:
    if not DATABASE_URL.startswith("sqlite"):
        return None

    url = make_url(DATABASE_URL)

    if not url.database or url.database == ":memory:":
        return None

    return str(Path(url.database).resolve())


def import_all_models() -> None:
    # Базовые модели.
    from app.modules.users import models as user_models  # noqa: F401
    from app.modules.auth import models as auth_models  # noqa: F401
    from app.modules.invitations import models as invitation_models  # noqa: F401
    from app.modules.tags import models as tag_models  # noqa: F401

    # Контент сначала импортируется от простого к составному.
    from app.modules.articles import models as article_models  # noqa: F401
    from app.modules.questionnaires import models as questionnaire_models  # noqa: F401
    from app.modules.services import models as service_models  # noqa: F401
    from app.modules.programs import models as program_models  # noqa: F401

    # Клинический и аналитический маршрут.
    from app.modules.referrals import models as referral_models  # noqa: F401
    from app.modules.events import models as event_models  # noqa: F401
    from app.modules.consents import models as consent_models  # noqa: F401

    from app.modules.notifications import models as notification_models  # noqa: F401
    from app.modules.assignments import models as assignment_models  # noqa: F401


def init_sqlite_db() -> None:
    """
    Инициализация базы данных.

    Если SQLite-файл существует, создаются только недостающие таблицы.
    Если файл отсутствует, он будет создан автоматически.
    """
    import_all_models()

    db_path = get_db_path()

    if db_path is None:
        SQLModel.metadata.create_all(sqlite_engine)
        print("✓ Database tables synchronized")
        return

    parent_directory = os.path.dirname(db_path)

    if parent_directory:
        os.makedirs(parent_directory, exist_ok=True)

    if os.path.exists(db_path):
        print(f"📁 Database file already exists: {db_path}")
        print("   Checking for missing tables...")
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Tables synchronized")
    else:
        print(f"📁 Creating new database: {db_path}")
        SQLModel.metadata.create_all(sqlite_engine)
        print("   ✓ Database created")


def get_session() -> Generator[Session, None, None]:
    with Session(sqlite_engine) as session:
        yield session