"""create all

Revision ID: 192bf3f9143a
Revises: 
Create Date: 2024-03-23 15:06:05.034940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '192bf3f9143a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('event_type', sa.Enum('meeting', 'task', 'important_date', 'personal', 'no_category', name='eventtype'), nullable=False),
    sa.Column('priority', sa.Enum('important', 'requires_attention', 'without_priority', name='eventpriority'), nullable=False),
    sa.Column('repeatability', sa.Enum('every_day', 'every_week', 'every_month', 'no_repeats', name='eventrepitabilyty'), nullable=False),
    sa.Column('event_location', sa.Enum('skype', 'zoom', 'goglemeet', 'telegram', 'b24', 'other', name='eventlocation'), nullable=False),
    sa.Column('organizer', sa.String(), nullable=True),
    sa.Column('start_time', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('end_time', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('duration', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_end_time'), 'event', ['end_time'], unique=False)
    op.create_index(op.f('ix_event_id'), 'event', ['id'], unique=False)
    op.create_index(op.f('ix_event_start_time'), 'event', ['start_time'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_created_at'), 'comment', ['created_at'], unique=False)
    op.create_index(op.f('ix_comment_id'), 'comment', ['id'], unique=False)
    op.create_table('event_user',
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_user')
    op.drop_index(op.f('ix_comment_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_created_at'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_event_start_time'), table_name='event')
    op.drop_index(op.f('ix_event_id'), table_name='event')
    op.drop_index(op.f('ix_event_end_time'), table_name='event')
    op.drop_table('event')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###