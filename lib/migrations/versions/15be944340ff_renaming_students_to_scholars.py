"""Renaming students to scholars

Revision ID: 15be944340ff
Revises: 791279dd0760
Create Date: 2023-06-02 12:04:55.607103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15be944340ff'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
