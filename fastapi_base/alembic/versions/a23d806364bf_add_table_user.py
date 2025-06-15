"""add table user

Revision ID: a23d806364bf
Revises: 650aa851ed1d
Create Date: 2025-06-12 17:03:45.397676

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a23d806364bf"
down_revision: Union[str, None] = "650aa851ed1d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
