"""update db

Revision ID: 800442f3096e
Revises: eaedb940607a
Create Date: 2024-05-24 11:48:42.265820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800442f3096e'
down_revision = 'eaedb940607a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_cattle_admin_id', 'admin', ['admin_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.drop_constraint('fk_cattle_admin_id', type_='foreignkey')
        batch_op.drop_column('admin_id')

    # ### end Alembic commands ###
