import discord
from discord import app_commands
from discord.ext import commands


class Announce(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Check latency")
    async def announce(self, interaction: discord.Interaction):
        # Use interaction.response to reply to slash commands
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! {latency}ms.")


# The setup function that main.py calls to register the Command
async def setup(bot: commands.Bot):
    await bot.add_cog(Announce(bot))
