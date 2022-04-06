import os
import string
import random
import asyncio
from subprocess import run

import discord
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(">")

load_dotenv()

@client.event
async def on_ready():
    print("ready")


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def ricklang(ctx, *, code):
    code = code.replace("`", "")
    
    random_code_list = string.ascii_lowercase + string.digits
    random_code = "".join([random.choice(random_code_list) for i in range(12)])
    
    with open("main.rickroll", "w") as f:
        f.write(code)

    build = run(["bash", "main.sh", random_code])
    output = run(["docker", "run", random_code], capture_output=True).stdout.decode()
    if len(output) > 4000:
        output = output[:4000]
    await ctx.send(
        embed=discord.Embed(title = "Output", color=discord.Color.blue(), description=f"""```\n{output}\n```""")
    )
    image = run(["docker", "images", "-q", random_code], capture_output=True).stdout.decode()
    await asyncio.sleep(10)
    os.system(f"docker image rm -f {image}")

    os.remove("main.rickroll")


client.run(os.environ["TOKEN"])
