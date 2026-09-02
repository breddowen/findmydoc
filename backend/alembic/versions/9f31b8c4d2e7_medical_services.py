"""medical services

Revision ID: 9f31b8c4d2e7
Revises: 6eb4582e2464
Create Date: 2026-09-02
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql


revision: str = "9f31b8c4d2e7"
down_revision: Union[
    str,
    Sequence[str],
    None,
] = "6eb4582e2464"
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


SERVICE_CURRENCY_VALUES = (
    "RUB",
    "UNIT",
)


def get_service_currency_type(
    dialect_name: str,
):
    if dialect_name == "postgresql":
        return postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="servicecurrency",
            create_type=False,
        )

    return sa.Enum(
        *SERVICE_CURRENCY_VALUES,
        name="servicecurrency",
        native_enum=False,
    )


def get_program_currency_type(
    dialect_name: str,
):
    if dialect_name == "postgresql":
        return postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="programcurrency",
            create_type=False,
        )

    return sa.Enum(
        *SERVICE_CURRENCY_VALUES,
        name="programcurrency",
        native_enum=False,
    )


def upgrade() -> None:
    bind = op.get_bind()
    dialect_name = bind.dialect.name

    if dialect_name == "postgresql":
        # Enum создаётся отдельно, чтобы create_table
        # не пытался создать его повторно.
        postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="servicecurrency",
        ).create(
            bind,
            checkfirst=True,
        )

    op.create_table(
        "medical_services",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "code",
            sqlmodel.sql.sqltypes.AutoString(
                length=50
            ),
            nullable=False,
        ),
        sa.Column(
            "title",
            sqlmodel.sql.sqltypes.AutoString(
                length=300
            ),
            nullable=False,
        ),
        sa.Column(
            "description",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column(
            "price_amount",
            sa.Numeric(
                precision=12,
                scale=2,
            ),
            nullable=True,
        ),
        sa.Column(
            "currency",
            get_service_currency_type(
                dialect_name
            ),
            nullable=True,
        ),
        sa.Column(
            "discount_percent",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column(
            "hidden_at",
            sa.DateTime(),
            nullable=True,
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
        sa.CheckConstraint(
            (
                "price_amount IS NULL "
                "OR price_amount >= 0"
            ),
            name=(
                "ck_medical_service_"
                "price_non_negative"
            ),
        ),
        sa.CheckConstraint(
            (
                "discount_percent >= 0 "
                "AND discount_percent <= 100"
            ),
            name=(
                "ck_medical_service_"
                "discount_range"
            ),
        ),
        sa.CheckConstraint(
            (
                "("
                "price_amount IS NULL "
                "AND currency IS NULL "
                "AND discount_percent = 0"
                ") OR ("
                "price_amount IS NOT NULL "
                "AND currency IS NOT NULL"
                ")"
            ),
            name=(
                "ck_medical_service_"
                "pricing_consistency"
            ),
        ),
        sa.CheckConstraint(
            (
                "price_amount IS NULL "
                "OR price_amount > 0 "
                "OR discount_percent = 0"
            ),
            name=(
                "ck_medical_service_"
                "free_discount"
            ),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "code",
            name="uq_medical_service_code",
        ),
    )

    op.create_index(
        "ix_medical_services_code",
        "medical_services",
        ["code"],
        unique=False,
    )
    op.create_index(
        "ix_medical_services_title",
        "medical_services",
        ["title"],
        unique=False,
    )
    op.create_index(
        "ix_medical_services_is_hidden",
        "medical_services",
        ["is_hidden"],
        unique=False,
    )

    if dialect_name == "sqlite":
        # SQLite изменяет внешние ключи через
        # пересоздание таблицы в batch-режиме.
        with op.batch_alter_table(
            "programs"
        ) as batch_op:
            batch_op.add_column(
                sa.Column(
                    "service_id",
                    sa.Uuid(),
                    nullable=True,
                )
            )
            batch_op.create_foreign_key(
                (
                    "fk_programs_service_id_"
                    "medical_services"
                ),
                "medical_services",
                ["service_id"],
                ["id"],
            )
            batch_op.create_index(
                "ix_programs_service_id",
                ["service_id"],
                unique=False,
            )

            batch_op.drop_column(
                "discount_percent"
            )
            batch_op.drop_column("currency")
            batch_op.drop_column("price_amount")
    else:
        op.add_column(
            "programs",
            sa.Column(
                "service_id",
                sa.Uuid(),
                nullable=True,
            ),
        )
        op.create_foreign_key(
            (
                "fk_programs_service_id_"
                "medical_services"
            ),
            "programs",
            "medical_services",
            ["service_id"],
            ["id"],
        )
        op.create_index(
            "ix_programs_service_id",
            "programs",
            ["service_id"],
            unique=False,
        )

        op.drop_column(
            "programs",
            "discount_percent",
        )
        op.drop_column(
            "programs",
            "currency",
        )
        op.drop_column(
            "programs",
            "price_amount",
        )

    if dialect_name == "postgresql":
        # Старый enum больше не используется программами.
        postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="programcurrency",
        ).drop(
            bind,
            checkfirst=True,
        )


def downgrade() -> None:
    bind = op.get_bind()
    dialect_name = bind.dialect.name

    if dialect_name == "postgresql":
        postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="programcurrency",
        ).create(
            bind,
            checkfirst=True,
        )

    program_currency_type = (
        get_program_currency_type(dialect_name)
    )

    if dialect_name == "sqlite":
        with op.batch_alter_table(
            "programs"
        ) as batch_op:
            batch_op.add_column(
                sa.Column(
                    "price_amount",
                    sa.Numeric(
                        precision=12,
                        scale=2,
                    ),
                    nullable=True,
                )
            )
            batch_op.add_column(
                sa.Column(
                    "currency",
                    program_currency_type,
                    nullable=True,
                )
            )
            batch_op.add_column(
                sa.Column(
                    "discount_percent",
                    sa.Integer(),
                    nullable=False,
                    server_default=sa.text("0"),
                )
            )

            batch_op.drop_index(
                "ix_programs_service_id"
            )
            batch_op.drop_constraint(
                (
                    "fk_programs_service_id_"
                    "medical_services"
                ),
                type_="foreignkey",
            )
            batch_op.drop_column("service_id")

        with op.batch_alter_table(
            "programs"
        ) as batch_op:
            batch_op.alter_column(
                "discount_percent",
                existing_type=sa.Integer(),
                existing_nullable=False,
                server_default=None,
            )
    else:
        op.add_column(
            "programs",
            sa.Column(
                "price_amount",
                sa.Numeric(
                    precision=12,
                    scale=2,
                ),
                nullable=True,
            ),
        )
        op.add_column(
            "programs",
            sa.Column(
                "currency",
                program_currency_type,
                nullable=True,
            ),
        )
        op.add_column(
            "programs",
            sa.Column(
                "discount_percent",
                sa.Integer(),
                nullable=False,
                server_default=sa.text("0"),
            ),
        )
        op.alter_column(
            "programs",
            "discount_percent",
            existing_type=sa.Integer(),
            existing_nullable=False,
            server_default=None,
        )

        op.drop_index(
            "ix_programs_service_id",
            table_name="programs",
        )
        op.drop_constraint(
            (
                "fk_programs_service_id_"
                "medical_services"
            ),
            "programs",
            type_="foreignkey",
        )
        op.drop_column(
            "programs",
            "service_id",
        )

    op.drop_index(
        "ix_medical_services_is_hidden",
        table_name="medical_services",
    )
    op.drop_index(
        "ix_medical_services_title",
        table_name="medical_services",
    )
    op.drop_index(
        "ix_medical_services_code",
        table_name="medical_services",
    )
    op.drop_table("medical_services")

    if dialect_name == "postgresql":
        postgresql.ENUM(
            *SERVICE_CURRENCY_VALUES,
            name="servicecurrency",
        ).drop(
            bind,
            checkfirst=True,
        )