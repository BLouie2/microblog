"""new fields in user model

Revision ID: 93c076cc8210
Revises: 4a8711d4c162
Create Date: 2019-02-01 11:30:32.578152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93c076cc8210'
down_revision = '4a8711d4c162'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
