"""Make models unique by name

Revision ID: 515c705df387
Revises: 52fa625b02a8
Create Date: 2023-04-22 23:41:25.005792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '515c705df387'
down_revision = '52fa625b02a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'expense_categories', ['name'])
    op.drop_index('ix_shops_name', table_name='shops')
    op.create_index(op.f('ix_shops_name'), 'shops', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shops_name'), table_name='shops')
    op.create_index('ix_shops_name', 'shops', ['name'], unique=False)
    op.drop_constraint(None, 'expense_categories', type_='unique')
    # ### end Alembic commands ###
