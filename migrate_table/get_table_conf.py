import configparser
import json
import os


def get_table_conf() -> dict:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(this_folder, 'tables.conf')
    conf = configparser.ConfigParser()
    conf.read(init_file)

    try:
        tables = conf.get('tables', 'tables')
        return json.loads(tables)
    except (configparser.NoSectionError, configparser.NoOptionError):
        print("Table Configuration Missing")
        raise ValueError("Conf missing, Please reconfigure")
