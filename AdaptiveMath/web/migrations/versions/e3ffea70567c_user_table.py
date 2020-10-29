"""user table

Revision ID: e3ffea70567c
Revises: 
Create Date: 2020-10-15 11:30:48.395786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3ffea70567c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('qid', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=1000), nullable=True),
    sa.Column('answer', sa.String(length=1000), nullable=True),
    sa.Column('explain', sa.String(length=1000), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('questiontype', sa.String(length=1000), nullable=True),
    sa.Column('datecreated', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('qid')
    )
    op.create_index(op.f('ix_question_answer'), 'question', ['answer'], unique=False)
    op.create_index(op.f('ix_question_datecreated'), 'question', ['datecreated'], unique=False)
    op.create_index(op.f('ix_question_question'), 'question', ['question'], unique=True)
    op.create_index(op.f('ix_question_questiontype'), 'question', ['questiontype'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('testid', sa.Integer(), nullable=True),
    sa.Column('questionid', sa.Integer(), nullable=True),
    sa.Column('response', sa.String(length=1000), nullable=True),
    sa.Column('datecreated', sa.DateTime(), nullable=True),
    sa.Column('result', sa.Integer(), nullable=True),
    sa.Column('timetaken', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['questionid'], ['question.qid'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_datecreated'), 'record', ['datecreated'], unique=False)
    op.create_index(op.f('ix_record_questionid'), 'record', ['questionid'], unique=False)
    op.create_index(op.f('ix_record_testid'), 'record', ['testid'], unique=False)
    op.create_index(op.f('ix_record_userid'), 'record', ['userid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_record_userid'), table_name='record')
    op.drop_index(op.f('ix_record_testid'), table_name='record')
    op.drop_index(op.f('ix_record_questionid'), table_name='record')
    op.drop_index(op.f('ix_record_datecreated'), table_name='record')
    op.drop_table('record')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_question_questiontype'), table_name='question')
    op.drop_index(op.f('ix_question_question'), table_name='question')
    op.drop_index(op.f('ix_question_datecreated'), table_name='question')
    op.drop_index(op.f('ix_question_answer'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###