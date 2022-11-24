def fetch_data_from_source_server(dbconnection, schema, table, limit=0, where_clause=" 1 = 1 "):
    try:
        select_sql = f"SELECT * FROM {schema}.{table}  where {where_clause} order by 1 "

        if type(limit) == int and limit > 0:
            select_sql = f" {select_sql} limit {limit}"

        cursor = dbconnection.cursor()
        cursor.execute(select_sql)
        data = cursor.fetchall()

        return data

    except Exception as e:
        print("Exception Occurred while fetching from source server :: ", e)

