"""revoking some nullables in outfit tables

Revision ID: f6b50103bca0
Revises: c50ab9518b5c
Create Date: 2022-06-05 22:56:18.732282

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f6b50103bca0'
down_revision = 'c50ab9518b5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('outfit', 'id_kategori',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('outfit', 'id_style',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('outfit', 'harga_sewa',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('outfit', 'harga_beli',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('outfit', 'detail_produk',
               existing_type=mysql.VARCHAR(length=300),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('outfit', 'detail_produk',
               existing_type=mysql.VARCHAR(length=300),
               nullable=False)
    op.alter_column('outfit', 'harga_beli',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('outfit', 'harga_sewa',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('outfit', 'id_style',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('outfit', 'id_kategori',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    # ### end Alembic commands ###