"""assosiating a list of books to user

Revision ID: c97f085a1d93
Revises: bab0d3ac0112
Create Date: 2024-12-26 17:06:14.482262

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c97f085a1d93'
down_revision: Union[str, None] = 'bab0d3ac0112'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###