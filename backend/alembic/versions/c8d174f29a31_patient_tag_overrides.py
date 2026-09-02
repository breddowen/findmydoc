# ./backend/alembic/versions/c8d174f29a31_patient_tag_overrides.py
"""patient tag overrides

Revision ID: c8d174f29a31
Revises: 9f31b8c4d2e7
Create Date: 2026-09-03
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "c8d174f29a31"
down_revision: Union[
    str,
    Sequence[str],
    None,
] = "9f31b8c4d2e7"
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


def get_override_action_type(
    dialect_name: str,
):
    if dialect_name == "postgresql":
        # Тип уже создан первой миграцией
        # для doctor_tag_overrides.
        return postgresql.ENUM(
            "ADD",
            "REMOVE",
            name="doctortagoverrideaction",
            create_type=False,
        )

    return sa.Enum(
        "ADD",
        "REMOVE",
        name="doctortagoverrideaction",
        native_enum=False,
    )


def upgrade() -> None:
    bind = op.get_bind()

    op.create_table(
        "patient_tag_overrides",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "patient_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "tag_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "action",
            get_override_action_type(
                bind.dialect.name
            ),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["patient_profiles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "patient_id",
            "tag_id",
            name="uq_patient_tag_override",
        ),
    )

    op.create_index(
        "ix_patient_tag_overrides_patient_id",
        "patient_tag_overrides",
        ["patient_id"],
        unique=False,
    )
    op.create_index(
        "ix_patient_tag_overrides_tag_id",
        "patient_tag_overrides",
        ["tag_id"],
        unique=False,
    )
    op.create_index(
        "ix_patient_tag_overrides_action",
        "patient_tag_overrides",
        ["action"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_patient_tag_overrides_action",
        table_name="patient_tag_overrides",
    )
    op.drop_index(
        "ix_patient_tag_overrides_tag_id",
        table_name="patient_tag_overrides",
    )
    op.drop_index(
        "ix_patient_tag_overrides_patient_id",
        table_name="patient_tag_overrides",
    )
    op.drop_table("patient_tag_overrides")