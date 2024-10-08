"""empty message

Revision ID: f9940d95a9cf
Revises: 5cb07f0a8c22
Create Date: 2024-09-04 10:46:58.624863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9940d95a9cf'
down_revision = '5cb07f0a8c22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('run_time', sa.String(), nullable=True),
    sa.Column('music_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['music_id'], ['musics.id'], name=op.f('fk_songs_music_id_musics')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs')
    # ### end Alembic commands ###
