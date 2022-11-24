import os

from migrate_table.get_db_details_conf import fetch_db_details_v2


def configure_connection():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(this_folder, 'connection_details.conf')

    src_db_host = input("Enter Source DB host endpoint : ")
    src_db_user = input("Enter Source DB User [default-> postgres] : ")
    src_db_port = input("Enter Source DB User [default-> 5432] : ")
    src_db_pass = input("Enter Source DB Password : ")
    src_db_schema = input("Enter Source DB database : ")

    with open(init_file, 'w') as file:
        file.write("[src] \n")
        file.write("host=" + src_db_host + "\n")
        file.write("user=" + src_db_user + "\n")
        file.write("password=" + src_db_pass + "\n")
        file.write("database=" + src_db_schema + "\n")
        file.write("port=" + src_db_port + "\n")

    print("Source details configured Successfully")

    dest_db_host = input("Enter Destination DB host endpoint : ")
    dest_db_user = input("Enter Destination DB User [default-> postgres] : ")
    dest_db_port = input("Enter Destination DB User [default-> 5432] : ")
    dest_db_pass = input("Enter Destination DB Password : ")
    dest_db_schema = input("Enter Destination DB database : ")

    with open(init_file, 'a') as file:
        file.write("[dest] \n")
        file.write("host=" + dest_db_host + "\n")
        file.write("user=" + dest_db_user + "\n")
        file.write("password=" + dest_db_pass + "\n")
        file.write("database=" + dest_db_schema + "\n")
        file.write("port=" + dest_db_port + "\n")

    print("Destination details configured Successfully")

    data = fetch_db_details_v2('src')
    print(data)


if __name__ == '__main__':
    configure_connection()
