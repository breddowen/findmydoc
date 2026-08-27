# ./backend/migrations/upgrade_questionnaires_program_context.py
import sys
from pathlib import Path

from sqlalchemy import inspect, text


BACKEND_DIR = Path(__file__).resolve().parents[1]

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.core.db import (  # noqa: E402
    import_all_models,
    sqlite_engine,
)


def add_column_if_missing(
    *,
    connection,
    table_name: str,
    column_name: str,
    definition: str,
) -> None:
    columns = {
        column["name"]
        for column in inspect(connection).get_columns(
            table_name
        )
    }

    if column_name in columns:
        print(
            f"✓ {table_name}.{column_name} already exists"
        )
        return

    connection.execute(
        text(
            f"ALTER TABLE {table_name} "
            f"ADD COLUMN {column_name} {definition}"
        )
    )

    print(f"✓ Added {table_name}.{column_name}")


def migrate() -> None:
    import_all_models()

    with sqlite_engine.begin() as connection:
        add_column_if_missing(
            connection=connection,
            table_name="questionnaire_submissions",
            column_name="program_id",
            definition="CHAR(32)",
        )

        add_column_if_missing(
            connection=connection,
            table_name="questionnaire_submissions",
            column_name="program_stage_id",
            definition="CHAR(32)",
        )

    print()
    print("Questionnaire program context migrated.")


if __name__ == "__main__":
    migrate()