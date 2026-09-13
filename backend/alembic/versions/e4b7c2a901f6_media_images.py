"""Add private media image storage metadata."""

from alembic import op
import sqlalchemy as sa


revision = "e4b7c2a901f6"
down_revision = "d3f8a2c6e901"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "media_images",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "purpose",
            sa.String(length=32),
            nullable=False,
        ),
        sa.Column(
            "uploaded_by_user_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "width",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "height",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "size_bytes",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "is_attached",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "width > 0 AND height > 0",
            name="ck_media_images_dimensions",
        ),
        sa.CheckConstraint(
            "size_bytes > 0",
            name="ck_media_images_size",
        ),
        sa.CheckConstraint(
            "purpose IN ("
            "'doctor', "
            "'article', "
            "'questionnaire', "
            "'program', "
            "'life_aspect'"
            ")",
            name="ck_media_images_purpose",
        ),
        sa.ForeignKeyConstraint(
            ["uploaded_by_user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_media_images_uploaded_by_user_id",
        "media_images",
        ["uploaded_by_user_id"],
    )

    op.create_index(
        "ix_media_images_is_attached",
        "media_images",
        ["is_attached"],
    )

    op.create_index(
        "ix_media_images_created_at",
        "media_images",
        ["created_at"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_media_images_created_at",
        table_name="media_images",
    )

    op.drop_index(
        "ix_media_images_is_attached",
        table_name="media_images",
    )

    op.drop_index(
        "ix_media_images_uploaded_by_user_id",
        table_name="media_images",
    )

    op.drop_table("media_images")