"""empty message

Revision ID: 2c7de37c6995
Revises: None
Create Date: 2015-08-15 08:27:16.429525

"""

# revision identifiers, used by Alembic.
revision = '2c7de37c6995'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=35), nullable=True),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
