from db.db import add_user 

def add_user_to_db(GUILD_ID, user):
    add_user(GUILD_ID, user.id, user.name, user.display_name)