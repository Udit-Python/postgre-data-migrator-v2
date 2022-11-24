import json


def insert_data_in_db(db_connection, base_sql, data):
    print("INSERTING V2:: ", base_sql)

    barcket_location = base_sql.find("(")
    sql_part = base_sql[:barcket_location]
    strings_part = base_sql[barcket_location:-1]

    try:
        cursor = db_connection.cursor()
        values = []
        for row in data:
            t = ()
            for column in row:
                if type(column) == str and column == "":
                    t = t + (None,)
                elif type(column) == dict or type(column) == list:
                    t = t + (json.dumps(column),)
                else:
                    t = t + (column,)

            values.append(t)

        args = ','.join(cursor.mogrify(strings_part, i).decode('utf-8') for i in values)
        cursor.execute(sql_part + args)
        db_connection.commit()

    except Exception as e:
        print("Some Exception while insertion to destination :: ", e)
        db_connection.rollback()


def truncate_table(db_connection, sql):
    print("Truncating :: ", sql)
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql)
        db_connection.commit()

    except Exception as e:
        print("Some Exception occurred while truncating :: ", e)
