import asyncio
import os

import discord
from discord.ext import commands

import utils

# Parse terminal configurations immediately on startup
args = utils.parse_arguments()

# Define bot instance with required intents
intents = discord.Intents.default()

# discord.py requires a prefix even for pure slash command bots
bot = commands.Bot(command_prefix="!", intents=intents)


# Automatically load all separate Commands Files
async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")
            print(f"Loaded command file: {filename[:-3]}")


@bot.event
async def on_ready():
    """Triggers once Discord websocket connection succeeds."""
    print(f"Logged in as {bot.user.name}")

    try:
        if args.test:
            TEST_GUILD = discord.Object(
                id=utils.get_env_variable("DISCORD_SERVER_ID_FOR_TESTING")
            )
            bot.tree.copy_global_to(guild=TEST_GUILD)
            synced = await bot.tree.sync(guild=TEST_GUILD)

            print(
                f"🧪 [TEST MODE] Instantly synced {len(synced)} commands to Guild: {bot.get_guild(TEST_GUILD.id).name}"
            )
        else:
            synced = await bot.tree.sync()
            print(
                f"🚀 [PRODUCTION] Synced {len(synced)} commands globally (may take up to 1 hour)."
            )

    except discord.HTTPException as error:
        print(f"Failed to sync application commands: {error}")


# Main function to start the bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(utils.get_env_variable("DISCORD_BOT_TOKEN"))


asyncio.run(main())
