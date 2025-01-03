"""add user_uid foreignkey to books

Revision ID: bab0d3ac0112
Revises: 74a206c6c6c3
Create Date: 2024-12-25 21:04:55.810160

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bab0d3ac0112'
down_revision: Union[str, None] = '74a206c6c6c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('user_uid', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'books', 'user_accounts', ['user_uid'], ['uid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'user_uid')
    # ### end Alembic commands ###
