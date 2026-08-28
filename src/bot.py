# Python lib imports
import asyncio
import importlib
import traceback
from pathlib import Path

# Discord Imports
import discord
from discord.ext import commands

from event_handlers.on_guild_join import init_guild_artifacts

# Event Handlers
from event_handlers.on_ready import start_as_test

# Utils
from utils.get_env_variable import get_env_variable
from utils.init_guilds import init_guilds
from utils.parse_arguments import parse_arguments

# Parse terminal configurations immediately on startup
args = parse_arguments()

# Define bot instance with required intents
intents = discord.Intents.default()
intents.members = True

# discord.py requires a prefix even for pure slash command bots
bot = commands.Bot(command_prefix="!", intents=intents)


# Automatically load all separate Commands Files
async def load_extensions():
    commands_package = importlib.import_module("commands")
    commands_root = Path(next(iter(commands_package.__path__)))
    for command_path in sorted(commands_root.rglob("*.py")):
        if command_path.name == "__init__.py":
            continue
        relative_path = command_path.relative_to(commands_root).with_suffix("")
        module_name = ".".join(("commands", *relative_path.parts))
        await bot.load_extension(module_name)
        print(f"Loaded command file: {module_name}")


@bot.event
async def on_ready():
    """Triggers once Discord websocket connection succeeds."""
    print(f"Logged in as {bot.user.name}")

    try:
        if args.test:  # TEST: Init & Test on specific server only.
            await start_as_test(bot)
        else:  # Normal Sequence: Runs on all servers.
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
