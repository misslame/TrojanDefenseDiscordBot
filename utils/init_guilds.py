from db.initialize_db import initialize_database
from db.user_db import add_user_to_db

async def init_guild(guild):
    count = 0
    async for user in guild.fetch_members(limit=None):
        count += 1 
        add_user_to_db(guild.id, user)
    print(f"Processed {count} members within guild: {guild.name}")


async def init_guilds(bot):
    for guild in bot.guilds:
        initialize_database(guild.id)
        await init_guild(guild)
        
