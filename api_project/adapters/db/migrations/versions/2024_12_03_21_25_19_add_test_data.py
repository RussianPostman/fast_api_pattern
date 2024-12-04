"""add_test_data

Revision ID: 582b32faa8ab
Revises: 2f1f0a4fff95
Create Date: 2024-12-03 21:25:19.895021

"""
from dataclasses import dataclass
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '582b32faa8ab'
down_revision: Union[str, None] = '2f1f0a4fff95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


@dataclass
class Rate:
    name: str
    date_to: datetime
    rate: float


workshops_table = sa.table(
    'rates',
    sa.column('id', sa.Integer),
    sa.column('name', sa.Unicode),
    sa.column('date_to', sa.DateTime),
    sa.column('rate', sa.Float),
    # schema='my_db',
)


base_rates = [
    Rate(name='Glass', date_to=datetime(2000, 1, 1), rate=0.03),
    Rate(name='Other', date_to=datetime(2000, 1, 1), rate=0.04),
    Rate(name='Glass', date_to=datetime(2020, 1, 1), rate=0.05),
    Rate(name='Other', date_to=datetime(2020, 1, 1), rate=0.06),
    Rate(name='Glass', date_to=datetime(2021, 1, 1), rate=0.08),
    Rate(name='Other', date_to=datetime(2021, 1, 1), rate=0.09),
]


def upgrade() -> None:
    # connection = op.get_bind()

    for rate in base_rates:
        print(rate)
        op.execute(workshops_table.insert().values(rate.__dict__))


def downgrade() -> None:
    connection = op.get_bind()

    for rate in base_rates:
        connection.execute(
            workshops_table
            .delete()
            .where(
                workshops_table.c.name == rate.name,
                workshops_table.c.date_to == rate.date_to,
            )
        )
