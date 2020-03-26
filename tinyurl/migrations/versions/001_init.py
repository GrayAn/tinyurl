import sqlalchemy as sa

metadata = sa.MetaData()

urlassociation = sa.Table(
    'urlassociation',
    metadata,
    sa.Column('fullurl', sa.Text()),
    sa.Column('shorturl', sa.Text(), primary_key=True),
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine

    urlassociation.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine

    urlassociation.drop()
