from utils.get_env_variable import get_env_variable
from utils.setup_single_guild import setup_single_guild

async def start_as_test(bot):
    TEST_GUILD = bot.get_guild(int(get_env_variable("DISCORD_SERVER_ID_FOR_TESTING")))
    if TEST_GUILD is not None:

        synced = await setup_single_guild(bot, TEST_GUILD)

        print(
            f"🧪 [TEST MODE] Instantly synced {len(synced)} commands to Guild: {bot.get_guild(TEST_GUILD.id).name}"
        )
    else: 
        raise AttributeError (
            f"The provided test guild ID does not exist or cannot be found."
        )