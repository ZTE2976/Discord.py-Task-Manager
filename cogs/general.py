import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        """ - This is a test command."""
        await ctx.send("Hello there!")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))