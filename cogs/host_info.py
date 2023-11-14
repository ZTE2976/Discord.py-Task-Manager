import discord
import psutil
import cpuinfo
from cpuutilization import cpuutilization
from discord.ext import commands

class HostInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
      self.bot = bot
    
    @commands.command(name="stats", aliases=["Stats", "STATS", "status", "Status", "STATUS"])
    async def stats(self, ctx: commands.Context) -> None:
      """ - Get host info and user/server counts."""
      servers = len(ctx.bot.guilds)
      members = sum(guild.member_count for guild in ctx.bot.guilds)
      embed=discord.Embed(title="Stats", description="Discord user/server counts and Host status.", color=7306944)
      embed.set_author(name=f"{ctx.bot.user.name}'s Status")
      embed.set_thumbnail(url="https://i.imgur.com/orxWumx.jpg")
      embed.add_field(name="Discord stats:", value=f"Currently in {servers} servers with {members} members.", inline=False) 
      embed.add_field(name="CPU usage:", value=f"{cpuutilization.get_utilization():.4g}% CPU usage from an {cpuinfo.get_cpu_info()['brand_raw']}.", inline=True)
      embed.add_field(name="Memory usage:", value=f"{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total:.4g}% of virtual memory free.", inline=True)
      embed.add_field(name="Ping:", value=f"{round(self.bot.latency * 1000)} ms", inline=True)
      embed.add_field(name="More:", value="[☰ - Github Page](https://github.com/ZTE2976/Discord.py-Task-Manager)", inline=False)
      embed.set_footer(text="v1.0  |  ZTE2976")
      await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HostInfo(bot))