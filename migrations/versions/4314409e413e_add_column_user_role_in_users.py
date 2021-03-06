"""add column user_role in users

Revision ID: 4314409e413e
Revises: 4b6d94602b1c
Create Date: 2021-12-15 15:19:48.489040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4314409e413e'
down_revision = '4b6d94602b1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_role', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_role')
    # ### end Alembic commands ###
