"""doc-url

Revision ID: bede968e75b0
Revises: 753a48c8ac95
Create Date: 2022-02-12 12:29:41.968563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bede968e75b0'
down_revision = '753a48c8ac95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('url', sa.String(), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('documents', 'url')
    # ### end Alembic commands ###
