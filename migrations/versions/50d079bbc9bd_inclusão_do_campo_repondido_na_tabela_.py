"""Inclusão do campo 'repondido' na tabela contatos

Revision ID: 50d079bbc9bd
Revises: c9de039a2851
Create Date: 2025-05-24 18:01:02.766041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d079bbc9bd'
down_revision = 'c9de039a2851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respondido', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('respondido')

    # ### end Alembic commands ###
