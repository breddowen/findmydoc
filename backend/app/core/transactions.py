# ./backend/app/core/transactions.py
import uuid

from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.exc import OperationalError
from sqlmodel import Session

from app.modules.users.models import PatientProfile


def lock_patient_for_write(
    *,
    session: Session,
    patient_id: uuid.UUID,
) -> None:
    """
    Вызывать до чтения изменяемого состояния пациента.

    PostgreSQL: блокировка строки до commit/rollback.
    SQLite: получение блокировки записи базы.

    Функция сама не выполняет commit.
    """
    statement = (
        update(PatientProfile)
        .where(PatientProfile.id == patient_id)
        .values(id=PatientProfile.id)
        .execution_options(synchronize_session=False)
    )

    try:
        session.execute(statement)
    except OperationalError as error:
        dialect = session.get_bind().dialect.name
        sqlite_code = getattr(
            error.orig,
            "sqlite_errorcode",
            None,
        )

        is_sqlite_busy = (
            dialect == "sqlite"
            and isinstance(sqlite_code, int)
            and (sqlite_code & 0xFF) in {5, 6}
        )

        if not is_sqlite_busy:
            raise

        session.rollback()

        raise HTTPException(
            status_code=503,
            detail=(
                "Данные сейчас обновляются. "
                "Повторите действие через несколько секунд."
            ),
            headers={"Retry-After": "1"},
        ) from error