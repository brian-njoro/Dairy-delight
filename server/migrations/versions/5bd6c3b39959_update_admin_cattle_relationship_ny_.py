"""update admin cattle relationship ny adding admin foreign key

Revision ID: 5bd6c3b39959
Revises: eaedb940607a
Create Date: 2024-05-24 10:19:09.607537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bd6c3b39959'
down_revision = 'eaedb940607a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_cattle_admin', 'admin', ['admin_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.drop_constraint('fk_cattle_admin', type_='foreignkey')
        batch_op.drop_column('admin_id')

    # ### end Alembic commands ###
