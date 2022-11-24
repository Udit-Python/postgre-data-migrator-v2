def prepare_insert_script_for_exec(schema, table, data):
    number_of_columns = len(data[0])
    number_of_strs = "%s," * number_of_columns

    number_of_strs = number_of_strs[:-1]
    base_sql = f"INSERT INTO {schema}.{table} VALUES({number_of_strs});"

    return base_sql


def prepare_truncate_script(schema, table):
    truncate_sql = f"TRUNCATE TABLE {schema}.{table} CASCADE;"
    return truncate_sql

