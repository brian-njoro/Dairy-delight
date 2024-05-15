"""run recent migrations

Revision ID: 64d0ee55f7c8
Revises: b4ce78915f4f
Create Date: 2024-05-15 08:21:26.923506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64d0ee55f7c8'
down_revision = 'b4ce78915f4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=100), nullable=True),
    sa.Column('contact', sa.String(length=100), nullable=True),
    sa.Column('billing_address', sa.String(length=255), nullable=True),
    sa.Column('credit_limit', sa.Float(), nullable=True),
    sa.Column('shipping_address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('last_maintenance_date', sa.Date(), nullable=True),
    sa.Column('next_maintenance_date', sa.Date(), nullable=True),
    sa.Column('maintenance_cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity_on_hand', sa.Integer(), nullable=True),
    sa.Column('minimum_stock_level', sa.Integer(), nullable=True),
    sa.Column('maximum_stock_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=True),
    sa.Column('unit_price', sa.Float(), nullable=True),
    sa.Column('quantity_available', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dehorning',
    sa.Column('dehorning_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('cattle_serial_number', sa.Integer(), nullable=True),
    sa.Column('vet_name', sa.String(length=100), nullable=True),
    sa.Column('method', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['cattle_serial_number'], ['cattle.serial_number'], ),
    sa.PrimaryKeyConstraint('dehorning_id')
    )
    op.create_table('payment',
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('product', sa.String(length=100), nullable=True),
    sa.Column('payment_status', sa.String(length=100), nullable=True),
    sa.Column('method_of_payment', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    op.create_table('periodic_treatment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('cattle_serial_number', sa.Integer(), nullable=True),
    sa.Column('vet_name', sa.String(length=100), nullable=True),
    sa.Column('disease', sa.String(length=100), nullable=True),
    sa.Column('method_of_administration', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['cattle_serial_number'], ['cattle.serial_number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pest_control',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('cattle_serial_number', sa.Integer(), nullable=True),
    sa.Column('method', sa.String(length=100), nullable=True),
    sa.Column('pest_type', sa.String(length=100), nullable=True),
    sa.Column('pesticide_used', sa.String(length=100), nullable=True),
    sa.Column('vet_name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['cattle_serial_number'], ['cattle.serial_number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pest_control')
    op.drop_table('periodic_treatment')
    op.drop_table('payment')
    op.drop_table('dehorning')
    op.drop_table('product')
    op.drop_table('inventory')
    op.drop_table('equipment')
    op.drop_table('customer')
    # ### end Alembic commands ###
