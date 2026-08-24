# Python lib imports
import asyncio
import os
import traceback

# Discord Imports
import discord
from discord.ext import commands

# Utils
from utils.get_env_variable import get_env_variable
from utils.parse_arguments import parse_arguments
from utils.init_guilds import init_guilds

# Event Handlers
from event_handlers.on_ready import start_as_test
from event_handlers.on_guild_join import init_guild_artifacts


# Parse terminal configurations immediately on startup
args = parse_arguments()

# Define bot instance with required intents
intents = discord.Intents.default()
intents.members = True

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
        if args.test: # TEST: Init & Test on specific server only. 
            await start_as_test(bot)
        else: # Normal Sequence: Runs on all servers. 
            synced = await bot.tree.sync()
            print(
                f"🚀 [PRODUCTION] Synced {len(synced)} commands globally (may take up to 1 hour)."
            )
            await init_guilds(bot)
    except discord.HTTPException as error:
        print(f"Failed to sync application commands with discord: {error}")
    except Exception as error:
        traceback.print_exception(error)
        print(f"Error occured : {error}")

@bot.event
async def on_guild_join(guild):
    try: 
        await init_guild_artifacts(bot, guild)
    except discord.HTTPException as error:
        print(f"Failed to init guild on join with discord: {error}")
    except Exception as error:
        traceback.print_exception(error)
        print(f"Error occured : {error}")

# Main function to start the bot
async def main():
    async with bot:
        try: 
            await load_extensions()
            await bot.start(get_env_variable("DISCORD_BOT_TOKEN"))
        except Exception as error:
            print(error)

asyncio.run(main())
