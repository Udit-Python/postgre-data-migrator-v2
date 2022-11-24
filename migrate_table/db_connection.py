from psycopg2 import pool

from .get_db_details_conf import fetch_db_details_v2


def get_database_connection_v2(src):
    global connection_pool
    db_host, db_user, db_pass, db_name, db_port = fetch_db_details_v2(src)

    try:
        connection_pool = pool.ThreadedConnectionPool(minconn=1, maxconn=5, host=db_host, database=db_name,
                                                      user=db_user, password=db_pass, port=db_port)
        connection = connection_pool.getconn()
        return connection

    except Exception as e:
        print("Cannot Create Connection ", e)
        raise Exception


def put_database_connection(connection):
    if connection_pool:
        print("Closing Connection : ", id(connection))
        connection_pool.putconn(connection)
        connection_pool.closeall()
