import configparser
import os

from .app_literals import AppLiterals


def fetch_db_details_v2(src):
    if not src == 'src' and not src == 'dest':
        raise ValueError("SRC Variable Issue")

    this_folder = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(this_folder, 'connection_details.conf')
    conf = configparser.ConfigParser()
    conf.read(init_file)

    if not conf.has_section(src):
        raise ValueError("Configuration Issue, please reconfigure")

    db_host = conf.get(src, 'host')
    db_pass = conf.get(src, 'password')
    db_name = conf.get(src, 'database')
    db_user = conf.get(src, 'user') if conf.get(src, 'user') else AppLiterals.DB_USER
    db_port = conf.get(src, 'port') if conf.get(src, 'port') else AppLiterals.DB_PORT

    print("DB Details :: ", db_host, db_user, db_port, db_pass)

    return db_host, db_user, db_pass, db_name, db_port
