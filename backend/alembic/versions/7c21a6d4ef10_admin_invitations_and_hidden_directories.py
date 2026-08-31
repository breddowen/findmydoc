"""admin invitations and hidden directories

Revision ID: 7c21a6d4ef10
Revises: 4a9d77a6cc23
Create Date: 2026-08-31
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7c21a6d4ef10"
down_revision: Union[str, Sequence[str], None] = "4a9d77a6cc23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()

    if bind.dialect.name == "postgresql":
        op.execute(
            "ALTER TYPE invitationtype "
            "ADD VALUE IF NOT EXISTS 'MED_ASSISTANT'"
        )
        op.execute(
            "ALTER TYPE invitationtype "
            "ADD VALUE IF NOT EXISTS 'SUPERUSER'"
        )

    op.add_column(
        "invitations",
        sa.Column(
            "email_sent_at",
            sa.DateTime(),
            nullable=True,
        ),
    )
    op.add_column(
        "invitations",
        sa.Column(
            "email_send_error",
            sa.String(length=1000),
            nullable=True,
        ),
    )

    op.add_column(
        "tags",
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )
    op.add_column(
        "tags",
        sa.Column(
            "hidden_at",
            sa.DateTime(),
            nullable=True,
        ),
    )
    op.create_index(
        "ix_tags_is_hidden",
        "tags",
        ["is_hidden"],
        unique=False,
    )

    op.add_column(
        "specialities",
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )
    op.add_column(
        "specialities",
        sa.Column(
            "hidden_at",
            sa.DateTime(),
            nullable=True,
        ),
    )
    op.create_index(
        "ix_specialities_is_hidden",
        "specialities",
        ["is_hidden"],
        unique=False,
    )

    if bind.dialect.name == "sqlite":
        with op.batch_alter_table("tags") as batch_op:
            batch_op.alter_column(
                "is_hidden",
                existing_type=sa.Boolean(),
                existing_nullable=False,
                server_default=None,
            )

        with op.batch_alter_table(
            "specialities"
        ) as batch_op:
            batch_op.alter_column(
                "is_hidden",
                existing_type=sa.Boolean(),
                existing_nullable=False,
                server_default=None,
            )
    else:
        op.alter_column(
            "tags",
            "is_hidden",
            existing_type=sa.Boolean(),
            existing_nullable=False,
            server_default=None,
        )
        op.alter_column(
            "specialities",
            "is_hidden",
            existing_type=sa.Boolean(),
            existing_nullable=False,
            server_default=None,
        )


def downgrade() -> None:
    op.drop_index(
        "ix_specialities_is_hidden",
        table_name="specialities",
    )
    op.drop_column(
        "specialities",
        "hidden_at",
    )
    op.drop_column(
        "specialities",
        "is_hidden",
    )

    op.drop_index(
        "ix_tags_is_hidden",
        table_name="tags",
    )
    op.drop_column(
        "tags",
        "hidden_at",
    )
    op.drop_column(
        "tags",
        "is_hidden",
    )

    op.drop_column(
        "invitations",
        "email_send_error",
    )
    op.drop_column(
        "invitations",
        "email_sent_at",
    )

    # Значения PostgreSQL ENUM намеренно не удаляются.
    # Удаление значений enum требует пересоздания типа.