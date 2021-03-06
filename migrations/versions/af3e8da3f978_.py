"""empty message

Revision ID: af3e8da3f978
Revises: 074e24d380a4
Create Date: 2019-11-16 21:22:04.120017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af3e8da3f978'
down_revision = '074e24d380a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keyword',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_keyword_word'), 'keyword', ['word'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_keyword_word'), table_name='keyword')
    op.drop_table('keyword')
    # ### end Alembic commands ###
