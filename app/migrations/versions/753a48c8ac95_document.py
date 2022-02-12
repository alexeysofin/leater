"""document

Revision ID: 753a48c8ac95
Revises: 7494d0b57b5b
Create Date: 2022-02-12 11:44:42.980764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '753a48c8ac95'
down_revision = '7494d0b57b5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('text', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('documents')
    # ### end Alembic commands ###