"""delete 2 colomns in users table

Revision ID: adfb8225644d
Revises: fb01ff1880da
Create Date: 2023-10-10 21:00:44.676225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "adfb8225644d"
down_revision: Union[str, None] = "fb01ff1880da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "price")
    op.drop_column("users", "description")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("description", sa.VARCHAR(), nullable=False))
    op.add_column("users", sa.Column("price", sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###
