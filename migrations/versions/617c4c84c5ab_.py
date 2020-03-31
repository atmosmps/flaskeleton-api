"""empty message

Revision ID: 617c4c84c5ab
Revises: 
Create Date: 2020-03-31 15:39:07.455844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '617c4c84c5ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ALUNOS',
    sa.Column('CODIGO', sa.Integer(), nullable=False),
    sa.Column('NOME', sa.String(), nullable=True),
    sa.Column('EMAIL', sa.String(), nullable=True),
    sa.Column('ENDERECO', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('CODIGO')
    )
    op.create_table('CAMPUS',
    sa.Column('CODIGO', sa.Integer(), nullable=False),
    sa.Column('DESCRICAO', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('CODIGO')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CAMPUS')
    op.drop_table('ALUNOS')
    # ### end Alembic commands ###