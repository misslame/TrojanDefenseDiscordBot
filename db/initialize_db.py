from utils.get_env_variable import get_env_variable
from db.db_constants import SCHEMA_PATH
from db.db import get_connection

def initialize_database(GUILD):
    connection = get_connection(GUILD.id)

    try:
        with open(SCHEMA_PATH, "r") as schema_file:
            schema = schema_file.read()

        connection.executescript(schema)
        connection.commit()

    finally:
        connection.close()