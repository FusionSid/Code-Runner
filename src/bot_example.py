import os 

import discord
from dotenv import load_dotenv
from discord.ext import commands

import runner

load_dotenv()

client = commands.Bot(".")


@client.command()
async def runcode(ctx, language: str, *, code):
    code = code.replace("`", "")

    output = await runner.run_code(repr(code), language, await_task=True)

    await ctx.send(
        embed=discord.Embed(
            title="Output",
            color=discord.Color.blue(),
            description=f"""```\n{output}\n```""",
        )
    )


@client.event
async def on_ready():
    print("Bot is online!")


client.run(os.environ["TOKEN"])