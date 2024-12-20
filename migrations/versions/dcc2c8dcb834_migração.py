"""Migração

Revision ID: dcc2c8dcb834
Revises: 
Create Date: 2024-11-19 12:21:01.520412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc2c8dcb834'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artistas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('genero', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albuns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=True),
    sa.Column('ano_lancamento', sa.Integer(), nullable=True),
    sa.Column('artista_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artista_id'], ['artistas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('albuns')
    op.drop_table('artistas')
    # ### end Alembic commands ###
