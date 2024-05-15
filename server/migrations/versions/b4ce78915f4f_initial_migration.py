"""initial migration

Revision ID: b4ce78915f4f
Revises: 
Create Date: 2024-05-15 08:17:56.145252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4ce78915f4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('farm_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cattle',
    sa.Column('serial_number', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('breed', sa.String(length=100), nullable=True),
    sa.Column('father', sa.Integer(), nullable=True),
    sa.Column('mother', sa.Integer(), nullable=True),
    sa.Column('method_bred', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['father'], ['cattle.serial_number'], ),
    sa.ForeignKeyConstraint(['mother'], ['cattle.serial_number'], ),
    sa.PrimaryKeyConstraint('serial_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cattle')
    op.drop_table('admin')
    # ### end Alembic commands ###