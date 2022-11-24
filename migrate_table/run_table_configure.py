import json
import os


def register_tables():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(this_folder, 'tables.conf')

    number_of_tables = int(input("How many tables you want to register ? "))
    tables = {}
    for i in range(0, number_of_tables):
        table_details = input("Enter table name in format SCHEMA.TABLE ")
        alias = input("Alias for the table :: ")
        tables[alias] = table_details

    with open(init_file, 'w') as file:
        file.write("[tables] \n")
        file.write("tables=" + json.dumps(tables))

    print("Tables registered successfully")


if __name__ == '__main__':
    register_tables()
