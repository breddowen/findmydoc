"""article analytics events

Revision ID: 6042112705c7
Revises: c8d174f29a31
Create Date: 2026-09-04 22:37:41.095763
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6042112705c7"
down_revision: Union[
    str,
    Sequence[str],
    None,
] = "c8d174f29a31"
branch_labels: Union[
    str,
    Sequence[str],
    None,
] = None
depends_on: Union[
    str,
    Sequence[str],
    None,
] = None


def get_column_names(
    bind,
    table_name: str,
) -> set[str]:
    inspector = sa.inspect(bind)

    return {
        column["name"]
        for column in inspector.get_columns(
            table_name
        )
    }


def get_index_names(
    bind,
    table_name: str,
) -> set[str]:
    inspector = sa.inspect(bind)

    return {
        index["name"]
        for index in inspector.get_indexes(
            table_name
        )
        if index.get("name")
    }


def get_unique_constraint_names(
    bind,
    table_name: str,
) -> set[str]:
    inspector = sa.inspect(bind)

    return {
        constraint["name"]
        for constraint
        in inspector.get_unique_constraints(
            table_name
        )
        if constraint.get("name")
    }


def has_assignment_foreign_key(
    bind,
) -> bool:
    inspector = sa.inspect(bind)

    for foreign_key in inspector.get_foreign_keys(
        "events"
    ):
        if (
            foreign_key.get(
                "constrained_columns"
            )
            == ["assignment_id"]
            and foreign_key.get(
                "referred_table"
            )
            == "content_assignments"
        ):
            return True

    return False


def upgrade_postgresql(
    bind,
) -> None:
    # В исходной PostgreSQL-миграции Enum хранит
    # имена элементов Python Enum.
    op.execute(
        "ALTER TYPE eventtype "
        "ADD VALUE IF NOT EXISTS 'ARTICLE_OPENED'"
    )
    op.execute(
        "ALTER TYPE eventtype "
        "ADD VALUE IF NOT EXISTS 'ARTICLE_ASSIGNED'"
    )

    column_names = get_column_names(
        bind,
        "events",
    )

    if "interaction_id" not in column_names:
        op.add_column(
            "events",
            sa.Column(
                "interaction_id",
                sa.Uuid(),
                nullable=True,
            ),
        )

    if "source" not in column_names:
        op.add_column(
            "events",
            sa.Column(
                "source",
                sa.String(length=50),
                nullable=True,
            ),
        )

    if "assignment_id" not in column_names:
        op.add_column(
            "events",
            sa.Column(
                "assignment_id",
                sa.Uuid(),
                nullable=True,
            ),
        )

    if not has_assignment_foreign_key(bind):
        op.create_foreign_key(
            "fk_events_assignment_id",
            "events",
            "content_assignments",
            ["assignment_id"],
            ["id"],
        )

    unique_names = (
        get_unique_constraint_names(
            bind,
            "events",
        )
    )

    if (
        "uq_event_type_interaction"
        not in unique_names
    ):
        op.create_unique_constraint(
            "uq_event_type_interaction",
            "events",
            [
                "event_type",
                "interaction_id",
            ],
        )


def upgrade_sqlite(
    bind,
) -> None:
    """
    SQLite не поддерживает добавление внешнего ключа
    и UNIQUE-ограничения через обычный ALTER TABLE.

    batch_alter_table пересоздаёт таблицу, копирует данные
    и переименовывает новую таблицу обратно в events.
    """
    column_names = get_column_names(
        bind,
        "events",
    )
    unique_names = (
        get_unique_constraint_names(
            bind,
            "events",
        )
    )
    assignment_fk_exists = (
        has_assignment_foreign_key(bind)
    )

    with op.batch_alter_table(
        "events",
        recreate="always",
    ) as batch_op:
        if (
            "interaction_id"
            not in column_names
        ):
            batch_op.add_column(
                sa.Column(
                    "interaction_id",
                    sa.Uuid(),
                    nullable=True,
                )
            )

        if "source" not in column_names:
            batch_op.add_column(
                sa.Column(
                    "source",
                    sa.String(length=50),
                    nullable=True,
                )
            )

        if (
            "assignment_id"
            not in column_names
        ):
            batch_op.add_column(
                sa.Column(
                    "assignment_id",
                    sa.Uuid(),
                    nullable=True,
                )
            )

        if not assignment_fk_exists:
            batch_op.create_foreign_key(
                "fk_events_assignment_id",
                "content_assignments",
                ["assignment_id"],
                ["id"],
            )

        if (
            "uq_event_type_interaction"
            not in unique_names
        ):
            batch_op.create_unique_constraint(
                "uq_event_type_interaction",
                [
                    "event_type",
                    "interaction_id",
                ],
            )


def create_indexes_if_missing(
    bind,
) -> None:
    index_names = get_index_names(
        bind,
        "events",
    )

    if (
        "ix_events_interaction_id"
        not in index_names
    ):
        op.create_index(
            "ix_events_interaction_id",
            "events",
            ["interaction_id"],
            unique=False,
        )

    if "ix_events_source" not in index_names:
        op.create_index(
            "ix_events_source",
            "events",
            ["source"],
            unique=False,
        )

    if (
        "ix_events_assignment_id"
        not in index_names
    ):
        op.create_index(
            "ix_events_assignment_id",
            "events",
            ["assignment_id"],
            unique=False,
        )

    if (
        "ix_events_article_analytics"
        not in index_names
    ):
        op.create_index(
            "ix_events_article_analytics",
            "events",
            [
                "subject_type",
                "event_type",
                "subject_id",
                "occurred_at",
            ],
            unique=False,
        )


def upgrade() -> None:
    bind = op.get_bind()

    if bind.dialect.name == "sqlite":
        upgrade_sqlite(bind)
    elif bind.dialect.name == "postgresql":
        upgrade_postgresql(bind)
    else:
        raise RuntimeError(
            "Unsupported database dialect: "
            f"{bind.dialect.name}"
        )

    # После batch-операции нужен новый Inspector,
    # поэтому индексы создаются отдельным этапом.
    create_indexes_if_missing(bind)


def drop_index_if_exists(
    bind,
    index_name: str,
) -> None:
    index_names = get_index_names(
        bind,
        "events",
    )

    if index_name in index_names:
        op.drop_index(
            index_name,
            table_name="events",
        )


def downgrade_postgresql(
    bind,
) -> None:
    unique_names = (
        get_unique_constraint_names(
            bind,
            "events",
        )
    )

    if (
        "uq_event_type_interaction"
        in unique_names
    ):
        op.drop_constraint(
            "uq_event_type_interaction",
            "events",
            type_="unique",
        )

    if has_assignment_foreign_key(bind):
        op.drop_constraint(
            "fk_events_assignment_id",
            "events",
            type_="foreignkey",
        )

    column_names = get_column_names(
        bind,
        "events",
    )

    if "assignment_id" in column_names:
        op.drop_column(
            "events",
            "assignment_id",
        )

    if "source" in column_names:
        op.drop_column(
            "events",
            "source",
        )

    if "interaction_id" in column_names:
        op.drop_column(
            "events",
            "interaction_id",
        )

    # Значения ARTICLE_OPENED и ARTICLE_ASSIGNED
    # остаются в PostgreSQL Enum. Удаление отдельных
    # значений потребовало бы пересоздания всего типа.


def downgrade_sqlite(
    bind,
) -> None:
    column_names = get_column_names(
        bind,
        "events",
    )
    unique_names = (
        get_unique_constraint_names(
            bind,
            "events",
        )
    )

    assignment_fk_exists = (
        has_assignment_foreign_key(bind)
    )

    with op.batch_alter_table(
        "events",
        recreate="always",
    ) as batch_op:
        if (
            "uq_event_type_interaction"
            in unique_names
        ):
            batch_op.drop_constraint(
                "uq_event_type_interaction",
                type_="unique",
            )

        if assignment_fk_exists:
            batch_op.drop_constraint(
                "fk_events_assignment_id",
                type_="foreignkey",
            )

        if "assignment_id" in column_names:
            batch_op.drop_column(
                "assignment_id"
            )

        if "source" in column_names:
            batch_op.drop_column(
                "source"
            )

        if "interaction_id" in column_names:
            batch_op.drop_column(
                "interaction_id"
            )


def downgrade() -> None:
    bind = op.get_bind()

    # Индексы удаляем до пересоздания таблицы.
    drop_index_if_exists(
        bind,
        "ix_events_article_analytics",
    )
    drop_index_if_exists(
        bind,
        "ix_events_assignment_id",
    )
    drop_index_if_exists(
        bind,
        "ix_events_source",
    )
    drop_index_if_exists(
        bind,
        "ix_events_interaction_id",
    )

    if bind.dialect.name == "sqlite":
        downgrade_sqlite(bind)
    elif bind.dialect.name == "postgresql":
        downgrade_postgresql(bind)
    else:
        raise RuntimeError(
            "Unsupported database dialect: "
            f"{bind.dialect.name}"
        )