# POSTGRES DATA MIGRATOR

This is a Python code executed on Dev Machine to migrate DATA from Production to Lower Env

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirement.txt
```
or
```shell
./setup.bat
```

## Usage

#### Configure Database Details
We need to configure Source and Destination Database details using file ```python -m migrate_table.run_db_configure``` <br>
We need to put All DB details **[Host, Port, User, Password and Database name]** <br>
All details will be stored to *```connection_details.conf```* <br>
Modify As per requirement Otherwise run configuration again <br>

```shell
python -m migrate_table.run_db_configure
```

#### Configure Tables for migration
We need to configure Schemas for migration using file ```python -m migrate_table.run_table_configure``` <br>
All details will be stored to *```tables.conf```* <br>
Modify As per requirement Otherwise run configuration again <br>

```shell
python -m migrate_table.run_table_configure

```


```OR```

Pass SCHEMA.TABLE_NAME as argument

```commandline
NOTE DO NOT CHECK IN above mentioned *.conf files
```

#### Run Migration
We need to pass table alias as argument to ***migrate_table.py***

> * Table Alias Name [Table we need to migrate] $(table_name)

#### To Run the migration use below command in commandline

```shell
python -m migrate_table.run_migration $(table_name)

#sample
python -m migrate_table.run_migration my_table_alias
#or
python -m migrate_table.run_migration my_schema.my_table

```
