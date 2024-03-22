"""Initsial

Revision ID: 2b8c1c05aea7
Revises: 7aed6d95b38a
Create Date: 2024-03-22 04:34:42.633726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b8c1c05aea7'
down_revision: Union[str, None] = '7aed6d95b38a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
