# ./backend/alembic/versions/0c92e3a7b641_media_video_files.py

"""Create storage metadata for uploaded video files."""

from alembic import op
import sqlalchemy as sa


revision = "0c92e3a7b641"
down_revision = "f7a2d9c103b8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "media_video_files",
        sa.Column(
            "id",
            sa.Uuid(),
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
            "rotation_degrees",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "duration_seconds",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "fps",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "size_bytes",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.Column(
            "has_audio",
            sa.Boolean(),
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
        sa.PrimaryKeyConstraint(
            "id",
            name="pk_media_video_files",
        ),
        sa.ForeignKeyConstraint(
            ["uploaded_by_user_id"],
            ["users.id"],
            name="fk_media_video_files_uploaded_by_users",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "width > 0 AND height > 0",
            name="ck_media_video_files_dimensions",
        ),
        sa.CheckConstraint(
            "size_bytes > 0",
            name="ck_media_video_files_size",
        ),
        sa.CheckConstraint(
            "duration_seconds > 0",
            name="ck_media_video_files_duration",
        ),
        sa.CheckConstraint(
            "fps > 0",
            name="ck_media_video_files_fps",
        ),
        sa.CheckConstraint(
            "rotation_degrees IN (0, 90, 180, 270)",
            name="ck_media_video_files_rotation",
        ),
    )

    for column_name in (
        "uploaded_by_user_id",
        "is_attached",
        "created_at",
    ):
        op.create_index(
            f"ix_media_video_files_{column_name}",
            "media_video_files",
            [column_name],
            unique=False,
        )


def downgrade() -> None:
    for column_name in (
        "created_at",
        "is_attached",
        "uploaded_by_user_id",
    ):
        op.drop_index(
            f"ix_media_video_files_{column_name}",
            table_name="media_video_files",
        )

    op.drop_table("media_video_files")