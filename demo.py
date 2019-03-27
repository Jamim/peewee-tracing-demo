from peewee import *
from opentracing_instrumentation.client_hooks import install_all_patches


install_all_patches()

psql_db = PostgresqlDatabase('peewee', user='peewee', password='peewee',
                             host='127.0.0.1', port=5432)


class DemoModel(Model):
    class Meta:
        database = psql_db

    demo = CharField()


psql_db.create_tables([DemoModel])
