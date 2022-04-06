import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(">")

load_dotenv()

@client.event
async def on_ready():
    print("ready")

client.load_extension("cogs.runner")

client.run(os.environ["TOKEN"])
