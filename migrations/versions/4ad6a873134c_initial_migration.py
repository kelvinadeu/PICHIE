"""initial migration

Revision ID: 4ad6a873134c
Revises: 
Create Date: 2019-02-12 16:48:00.638412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ad6a873134c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.Column('category_description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscribe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribe_email'), 'subscribe', ['email'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('pitchies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitchies_post'), 'pitchies', ['post'], unique=False)
    op.create_index(op.f('ix_pitchies_title'), 'pitchies', ['title'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pitchie_id', sa.Integer(), nullable=True),
    sa.Column('commenter_id', sa.Integer(), nullable=True),
    sa.Column('comment_itself', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['pitchie_id'], ['pitchies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_comment_itself'), 'comments', ['comment_itself'], unique=False)
    op.create_index(op.f('ix_comments_email'), 'comments', ['email'], unique=False)
    op.create_index(op.f('ix_comments_name'), 'comments', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_name'), table_name='comments')
    op.drop_index(op.f('ix_comments_email'), table_name='comments')
    op.drop_index(op.f('ix_comments_comment_itself'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_pitchies_title'), table_name='pitchies')
    op.drop_index(op.f('ix_pitchies_post'), table_name='pitchies')
    op.drop_table('pitchies')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_subscribe_email'), table_name='subscribe')
    op.drop_table('subscribe')
    op.drop_table('roles')
    op.drop_table('categories')
    # ### end Alembic commands ###