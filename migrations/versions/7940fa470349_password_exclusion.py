"""password exclusion

Revision ID: 7940fa470349
Revises: 5fd2acc3dcc0
Create Date: 2024-12-25 01:53:46.174577

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7940fa470349'
down_revision: Union[str, None] = '5fd2acc3dcc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_accounts', ['uid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_accounts', type_='unique')
    # ### end Alembic commands ###
