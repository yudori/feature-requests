"""empty message

Revision ID: 5734e4a91c6a
Revises:
Create Date: 2018-11-24 21:11:14.663213

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.choice import ChoiceType

from feature_requests.features.models import FeatureRequest


# revision identifiers, used by Alembic.
revision = '5734e4a91c6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'feature_requests',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=127), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column(
            'client',
            ChoiceType(FeatureRequest.CLIENTS, sa.String(length=8)),
            nullable=False,
        ),
        sa.Column('client_priority', sa.Integer(), nullable=False),
        sa.Column('target_date', sa.Date(), nullable=False),
        sa.Column(
            'product_area',
            ChoiceType(FeatureRequest.PRODUCT_AREAS, sa.String(length=4)),
            nullable=False,
        ),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_requests')
    # ### end Alembic commands ###
