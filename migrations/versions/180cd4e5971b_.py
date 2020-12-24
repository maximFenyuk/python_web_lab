"""empty message

Revision ID: 180cd4e5971b
Revises: 3fc5ef796dc0
Create Date: 2019-12-01 22:30:26.491239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '180cd4e5971b'
down_revision = '3fc5ef796dc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###