import datetime
import sys

from .db_connection import get_database_connection_v2, put_database_connection
from .destination_db_scripts import prepare_insert_script_for_exec, prepare_truncate_script
from .destination_execute_script import truncate_table, insert_data_in_db
from .src_fetch_data import fetch_data_from_source_server
from .get_table_conf import get_table_conf


def main(schema, table):
    # Create Connection to Source DB [PROD]
    dbconnection_source = get_database_connection_v2('src')

    # Fetch Data from Source
    data = fetch_data_from_source_server(dbconnection_source, schema, table)

    # Close Source Connection
    put_database_connection(dbconnection_source)

    # Create Connection to Destination DB [DEVL, QUAL, CERT]
    dbconnection_dest = get_database_connection_v2('dest')

    # Check length of data [So that we don't terminate when have nothing to insert]
    if data:
        # Truncate Destination Table
        truncate_script = prepare_truncate_script(schema, table)
        truncate_table(dbconnection_dest, truncate_script)

        # Prepare Insert Statements and Execute on Destination
        insert_script_holder = prepare_insert_script_for_exec(schema, table, data)
        insert_data_in_db(dbconnection_dest, insert_script_holder, data)

        # Close Destination DB Connection [DEVL, QUAL, CERT]
        put_database_connection(dbconnection_dest)


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    table_input = sys.argv[1]  # Table to migrate from console

    if "." in table_input:
        print("Using Schema and table from console")
        schema_name = table_input.split(".")[0]
        table_name = table_input.split(".")[1]
    else:
        table_conf = get_table_conf()
        full_table: str = table_conf.get(table_input)
        schema_name = full_table.split(".")[0]
        table_name = full_table.split(".")[1]

    print(schema_name, table_name)

    main(schema_name, table_name)

    end_time_rec = datetime.datetime.now()
    time_taken = (end_time_rec - start_time).total_seconds()

    print(f"{table_input} COMPLETED IN : ", time_taken)
