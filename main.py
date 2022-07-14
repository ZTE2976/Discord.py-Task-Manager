import psutil
import cpuinfo
import discord
import os

from cpuutilization import cpuutilization
from discord.ext import commands

client = discord.Client()


#This General section is where you can add your normal commands.
class General(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='hello')
  async def _hello(self, ctx: commands.Context):
    """ - This is a test command."""
    await ctx.send('Hello there!')

    
#This Host_info section is where the Status viewer is.
class Host_info(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
      
  @commands.command(name='stats', aliases=['Stats', 'STATS', 'status', 'Status', 'STATUS'])
  async def _stats(self, ctx: commands.Context):
    """ - Get host info and user/server counts."""
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
      members += guild.member_count - 1
    embed=discord.Embed(title="Stats", description="Discord user/server counts and Host status.", color=7306944)
    embed.set_author(name="{0.user.name}'s Status".format(bot))
    file = discord.File("./images/zte2976.png", filename="image.png")
    embed.set_thumbnail(url="attachment://image.png")
    embed.add_field(name="Discord stats:", value=f"Currently in {servers} servers with {members} members.", inline=False) 
    embed.add_field(name="CPU usage:", value=f"{round(cpuutilization.get_utilization())}% CPU usage from an {cpuinfo.get_cpu_info()['brand_raw']}.", inline=True)
    embed.add_field(name="Memory usage:", value=f"{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)}% of virtual memory free.", inline=True)
    embed.add_field(name="Ping:", value=f'{round(bot.latency * 1000)} ms', inline=True)
    embed.add_field(name="More:", value="[☰ - Github Page](https://github.com/ZTE2976/Discord.py-Task-Manager)", inline=False)
    embed.set_footer(text="v1.0  |  ZTE2976")
    await ctx.send(file=file, embed=embed)


bot = commands.Bot('!', description="ZTE2976's Task Manager Example")
bot.add_cog(General(bot))
bot.add_cog(Host_info(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}'.format(bot))


bot.run(os.getenv('TOKEN'))
