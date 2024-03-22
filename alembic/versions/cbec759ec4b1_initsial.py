"""Initsial

Revision ID: cbec759ec4b1
Revises: 3c6b76bb2f11
Create Date: 2024-03-22 04:32:05.006882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbec759ec4b1'
down_revision: Union[str, None] = '3c6b76bb2f11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
