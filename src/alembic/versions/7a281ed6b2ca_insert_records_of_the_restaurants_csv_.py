"""insert records of the restaurants.csv file

Revision ID: 7a281ed6b2ca
Revises: ed99fb44fc12
Create Date: 2021-08-07 13:50:51.252412

"""
import csv
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData


# revision identifiers, used by Alembic.
revision = '7a281ed6b2ca'
down_revision = 'ed99fb44fc12'
branch_labels = None
depends_on = None


def get_table():
    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('restaurants',))
    return Table('restaurants', meta)


def read_file():
    rows = []
    with open('alembic/data/restaurantes.csv') as csv_file:
        headers = ['id', 'rating', 'name', 'site', 'email',
                   'phone', 'street', 'city', 'state', 'lat', 'lng']
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            new_row = dict(zip(headers, row))
            new_row['site'] = new_row['site'].replace(" ", "")
            rows.append(new_row)
    return rows


def upgrade():
    restaurants_table = get_table()
    data = read_file()
    op.bulk_insert(restaurants_table, data)


def downgrade():
    restaurants_table = get_table()
    ids = []
    for row in read_file():
        ids.append(row['id'])
    op.execute(restaurants_table.delete(restaurants_table.c.id.in_(ids)))
