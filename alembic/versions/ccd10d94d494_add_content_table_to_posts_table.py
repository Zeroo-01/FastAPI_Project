"""add content table to posts table

Revision ID: ccd10d94d494
Revises: a658d2237334
Create Date: 2024-08-07 19:09:52.272399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccd10d94d494'
down_revision: Union[str, None] = 'a658d2237334'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass