# ./backend/alembic/versions/5b613f08c942_video_program_progress.py

"""Add video program items, progress and event types."""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "5b613f08c942"
down_revision = "49b2d70c8e16"
branch_labels = None
depends_on = None


def extend_postgres_enum(
    table_name: str,
    column_name: str,
    expected_label: str,
    new_labels: tuple[str, ...],
) -> None:
    bind = op.get_bind()

    if bind.dialect.name != "postgresql":
        return

    inspector = sa.inspect(bind)

    column = next(
        item
        for item in inspector.get_columns(table_name)
        if item["name"] == column_name
    )

    enum_type = column["type"]

    if (
        not isinstance(enum_type, postgresql.ENUM)
        or expected_label not in enum_type.enums
    ):
        raise RuntimeError(
            f"Неожиданный тип {table_name}.{column_name}. "
            "Проверьте существующую схему Enum."
        )

    preparer = bind.dialect.identifier_preparer
    schema = enum_type.schema or inspector.default_schema_name

    qualified_name = (
        f"{preparer.quote_schema(schema)}."
        f"{preparer.quote(enum_type.name)}"
    )

    for label in new_labels:
        safe_label = label.replace("'", "''")

        op.execute(
            sa.text(
                f"ALTER TYPE {qualified_name} "
                f"ADD VALUE IF NOT EXISTS '{safe_label}'"
            )
        )


def upgrade() -> None:
    extend_postgres_enum(
        "program_stage_items",
        "item_type",
        "ARTICLE",
        ("VIDEO",),
    )

    extend_postgres_enum(
        "events",
        "event_type",
        "ARTICLE_OPENED",
        (
            "VIDEO_OPENED",
            "VIDEO_STARTED",
            "VIDEO_COMPLETED",
        ),
    )

    with op.batch_alter_table("program_stage_items") as batch:
        batch.add_column(
            sa.Column(
                "video_id",
                sa.Uuid(),
                nullable=True,
            )
        )

        batch.create_foreign_key(
            "fk_program_stage_items_video",
            "videos",
            ["video_id"],
            ["id"],
            ondelete="RESTRICT",
        )

        batch.create_index(
            "ix_program_stage_items_video_id",
            ["video_id"],
        )

    op.create_table(
        "video_progress",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("video_id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("progress_percent", sa.Float(), nullable=False),
        sa.Column("max_progress_percent", sa.Float(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column(
            "completion_method",
            sa.String(length=16),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["video_id"],
            ["videos.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["patient_profiles.id"],
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint(
            "video_id",
            "patient_id",
            name="uq_video_patient_progress",
        ),
        sa.CheckConstraint(
            "progress_percent >= 0 AND progress_percent <= 100",
            name="ck_video_progress_percent",
        ),
        sa.CheckConstraint(
            "max_progress_percent >= progress_percent "
            "AND max_progress_percent <= 100",
            name="ck_video_progress_max_percent",
        ),
        sa.CheckConstraint(
            "completion_method IS NULL "
            "OR completion_method IN ('position', 'manual')",
            name="ck_video_progress_completion_method",
        ),
    )

    for name in ("video_id", "patient_id"):
        op.create_index(
            f"ix_video_progress_{name}",
            "video_progress",
            [name],
        )


def downgrade() -> None:
    bind = op.get_bind()

    checks = (
        "SELECT COUNT(*) FROM video_progress",
        "SELECT COUNT(*) FROM program_stage_items "
        "WHERE video_id IS NOT NULL",
        "SELECT COUNT(*) FROM events "
        "WHERE CAST(event_type AS TEXT) IN "
        "('VIDEO_OPENED', 'VIDEO_STARTED', 'VIDEO_COMPLETED')",
    )

    if any(
        bind.execute(sa.text(query)).scalar_one()
        for query in checks
    ):
        raise RuntimeError(
            "Откат остановлен: уже существуют видеошаги, "
            "прогресс или события. Сначала требуется "
            "отдельный план сохранения этих данных."
        )

    op.drop_table("video_progress")

    with op.batch_alter_table("program_stage_items") as batch:
        batch.drop_index(
            "ix_program_stage_items_video_id",
        )
        batch.drop_constraint(
            "fk_program_stage_items_video",
            type_="foreignkey",
        )
        batch.drop_column("video_id")

    # Добавленные значения PostgreSQL Enum оставляем.
    # Они не мешают прежнему коду при отсутствии строк
    # с этими значениями. Автоматически пересоздавать
    # общий тип Enum при откате небезопасно.