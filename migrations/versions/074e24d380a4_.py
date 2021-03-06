"""empty message

Revision ID: 074e24d380a4
Revises: 7bce24136b0d
Create Date: 2019-11-16 19:01:18.162027

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '074e24d380a4'
down_revision = '7bce24136b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('website',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_website_url'), 'website', ['url'], unique=True)
    op.drop_index('ix_location_name', table_name='location')
    op.drop_table('location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('timezone', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='location_pkey')
    )
    op.create_index('ix_location_name', 'location', ['name'], unique=True)
    op.drop_index(op.f('ix_website_url'), table_name='website')
    op.drop_table('website')
    # ### end Alembic commands ###
