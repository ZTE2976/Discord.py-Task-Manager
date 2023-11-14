import os
import platform
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), description="ZTE2976's Task Manager Example")

@bot.event
async def on_ready() -> None:
    print(f"{bot.user} is now online!")
    print(f"Logged in as {bot.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")

async def setup_hook() -> None:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Successfully loaded the {filename} cog!")

if __name__ == "__main__":
    bot.setup_hook = setup_hook
    bot.run(os.environ["TOKEN"])

