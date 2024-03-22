"""Initsial

Revision ID: 7aed6d95b38a
Revises: cbec759ec4b1
Create Date: 2024-03-22 04:34:32.926471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7aed6d95b38a'
down_revision: Union[str, None] = 'cbec759ec4b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
