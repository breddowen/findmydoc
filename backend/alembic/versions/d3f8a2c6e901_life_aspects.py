"""Add life aspects and their tag links."""

from alembic import op
import sqlalchemy as sa


revision = "d3f8a2c6e901"
down_revision = "b1e4c7d902af"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "life_aspects",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "order_index",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "is_hidden",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
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
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_life_aspects_name",
        "life_aspects",
        ["name"],
        unique=True,
    )
    op.create_index(
        "ix_life_aspects_order_index",
        "life_aspects",
        ["order_index"],
        unique=False,
    )
    op.create_index(
        "ix_life_aspects_is_hidden",
        "life_aspects",
        ["is_hidden"],
        unique=False,
    )

    op.create_table(
        "life_aspect_tag_links",
        sa.Column(
            "id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "life_aspect_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "tag_id",
            sa.Uuid(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["life_aspect_id"],
            ["life_aspects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "life_aspect_id",
            "tag_id",
            name="uq_life_aspect_tag",
        ),
    )

    op.create_index(
        "ix_life_aspect_tag_links_life_aspect_id",
        "life_aspect_tag_links",
        ["life_aspect_id"],
        unique=False,
    )
    op.create_index(
        "ix_life_aspect_tag_links_tag_id",
        "life_aspect_tag_links",
        ["tag_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_life_aspect_tag_links_tag_id",
        table_name="life_aspect_tag_links",
    )
    op.drop_index(
        "ix_life_aspect_tag_links_life_aspect_id",
        table_name="life_aspect_tag_links",
    )
    op.drop_table("life_aspect_tag_links")

    op.drop_index(
        "ix_life_aspects_is_hidden",
        table_name="life_aspects",
    )
    op.drop_index(
        "ix_life_aspects_order_index",
        table_name="life_aspects",
    )
    op.drop_index(
        "ix_life_aspects_name",
        table_name="life_aspects",
    )
    op.drop_table("life_aspects")