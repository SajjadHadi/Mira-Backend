from alembic import op
import sqlalchemy as sa

revision = '2_create_statements'
down_revision = '1_create_users'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'statements',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('statement', sa.String(length=1000), nullable=False),
        sa.Column('disorders', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_statements_id'), 'statements', ['id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_statements_id'), table_name='statements')
    op.drop_table('statements')