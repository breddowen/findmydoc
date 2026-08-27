# ./backend/migrations/upgrade_programs_v2.py
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
from sqlmodel import SQLModel  # noqa: E402


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
            table_name="specialities",
            column_name="consultation_name",
            definition="VARCHAR(300)",
        )
        add_column_if_missing(
            connection=connection,
            table_name="specialities",
            column_name="consultation_description",
            definition="TEXT",
        )

        add_column_if_missing(
            connection=connection,
            table_name="programs",
            column_name="price_amount",
            definition="NUMERIC(12, 2)",
        )
        add_column_if_missing(
            connection=connection,
            table_name="programs",
            column_name="currency",
            definition="VARCHAR(20)",
        )

        add_column_if_missing(
            connection=connection,
            table_name="program_stage_items",
            column_name="speciality_id",
            definition="CHAR(32)",
        )
        add_column_if_missing(
            connection=connection,
            table_name="program_stage_items",
            column_name="consultation_title",
            definition="VARCHAR(300)",
        )
        add_column_if_missing(
            connection=connection,
            table_name="program_stage_items",
            column_name="consultation_description",
            definition="TEXT",
        )

    SQLModel.metadata.create_all(sqlite_engine)

    print()
    print("Program migration completed successfully.")


if __name__ == "__main__":
    migrate()