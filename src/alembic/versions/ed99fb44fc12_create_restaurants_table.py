"""create restaurants table

Revision ID: ed99fb44fc12
Revises:
Create Date: 2021-08-07 13:47:59.496254

"""
import sqlalchemy as sa
from alembic import op
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'ed99fb44fc12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'restaurants',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column('rating', sa.SmallInteger),
        sa.Column('name', sa.Text),
        sa.Column('site', sa.Text),
        sa.Column('email', sa.Text),
        sa.Column('phone', sa.Text),
        sa.Column('street', sa.Text),
        sa.Column('city', sa.Text),
        sa.Column('state', sa.Text),
        sa.Column('lat', sa.Float),
        sa.Column('lng', sa.Float),
    )


def downgrade():
    op.drop_table('restaurants')
