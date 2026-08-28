from db.initialize_db import initialize_database
from utils.init_guilds import init_guild


async def setup_single_guild(bot, guild):
    bot.tree.copy_global_to(guild=guild)
    synced = await bot.tree.sync(guild=guild)
    initialize_database(guild)
    await init_guild(guild)
    return synced
