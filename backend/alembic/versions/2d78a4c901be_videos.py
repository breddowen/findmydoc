# ./backend/alembic/versions/2d78a4c901be_videos.py

"""Create video materials and tag links."""

from alembic import op
import sqlalchemy as sa


revision = "2d78a4c901be"
down_revision = "0c92e3a7b641"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "videos",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "title",
            sa.String(length=300),
            nullable=False,
        ),
        sa.Column(
            "pro_content",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column(
            "is_library_hidden",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column(
            "wide_file_id",
            sa.Uuid(),
            nullable=True,
        ),
        sa.Column(
            "mobile_file_id",
            sa.Uuid(),
            nullable=True,
        ),
        sa.Column(
            "created_by_user_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "version",
            sa.Integer(),
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
        sa.Column(
            "hidden_at",
            sa.DateTime(),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name="pk_videos",
        ),
        sa.ForeignKeyConstraint(
            ["wide_file_id"],
            ["media_video_files.id"],
            name="fk_videos_wide_file",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["mobile_file_id"],
            ["media_video_files.id"],
            name="fk_videos_mobile_file",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_user_id"],
            ["users.id"],
            name="fk_videos_created_by_users",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "wide_file_id IS NOT NULL "
            "OR mobile_file_id IS NOT NULL",
            name="ck_videos_has_file",
        ),
        sa.CheckConstraint(
            "wide_file_id IS NULL "
            "OR mobile_file_id IS NULL "
            "OR wide_file_id <> mobile_file_id",
            name="ck_videos_different_files",
        ),
        sa.CheckConstraint(
            "version > 0",
            name="ck_videos_version",
        ),
    )

    for column_name in (
        "title",
        "pro_content",
        "is_hidden",
        "is_library_hidden",
        "wide_file_id",
        "mobile_file_id",
        "created_by_user_id",
        "created_at",
    ):
        op.create_index(
            f"ix_videos_{column_name}",
            "videos",
            [column_name],
        )

    op.create_table(
        "video_tag_links",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "video_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "tag_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name="pk_video_tag_links",
        ),
        sa.ForeignKeyConstraint(
            ["video_id"],
            ["videos.id"],
            name="fk_video_tag_links_video",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
            name="fk_video_tag_links_tag",
            ondelete="RESTRICT",
        ),
        sa.UniqueConstraint(
            "video_id",
            "tag_id",
            name="uq_video_tag",
        ),
    )

    for column_name in ("video_id", "tag_id"):
        op.create_index(
            f"ix_video_tag_links_{column_name}",
            "video_tag_links",
            [column_name],
        )


def downgrade() -> None:
    op.drop_table("video_tag_links")
    op.drop_table("videos")