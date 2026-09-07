# ./backend/alembic/versions/b1e4c7d902af_content_library_visibility.py
"""Add independent content library visibility."""

from alembic import op
import sqlalchemy as sa


revision = "b1e4c7d902af"
down_revision = "95f734785945"
branch_labels = None
depends_on = None


def upgrade() -> None:
    for table_name in ("articles", "questionnaires"):
        op.add_column(
            table_name,
            sa.Column(
                "is_library_hidden",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )

        op.create_index(
            f"ix_{table_name}_is_library_hidden",
            table_name,
            ["is_library_hidden"],
            unique=False,
        )


def downgrade() -> None:
    for table_name in ("questionnaires", "articles"):
        with op.batch_alter_table(table_name) as batch_op:
            batch_op.drop_index(
                f"ix_{table_name}_is_library_hidden",
            )
            batch_op.drop_column("is_library_hidden")