from django.db.backends.postgresql_psycopg2 import base


class DatabaseWrapper(base.DatabaseWrapper):
    def get_new_connection(self, conn_params):
        conn = super(DatabaseWrapper, self).get_new_connection(conn_params)
        conn.set_session(readonly=True)
        return conn
