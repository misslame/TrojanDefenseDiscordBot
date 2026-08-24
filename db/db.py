import sqlite3
from db.db_constants import DATABASE_PATH

def get_connection(GUILD_ID):
    # Make sure the data directory exists
    db_path = DATABASE_PATH / f"{GUILD_ID}.db"

    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)

    # Allows us to access columns by name instead of index
    connection.row_factory = sqlite3.Row

    return connection

def add_user(GUILD_ID, user_id, user_name, user_nickname):
    try: 
        connection = get_connection(GUILD_ID)
        connection.execute(
            """
            INSERT OR REPLACE INTO Users (
                discord_id,
                username,
                nickname
            ) VALUES ( ?, ?, ?)
            """, 
            (
                user_id,
                user_name,
                user_nickname
            )
        )
        return True
    except Exception as error:
        print("Error adding a new user: ", error) 
        return False
    finally:
        connection.commit()
        connection.close()