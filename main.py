import discord
import os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    file_to_open = random.choice(os.listdir("images"))
    with open(f"images/{file_to_open}", 'rb') as f:
        mem = discord.File(f)
    await ctx.send("Zobacz na ten mem", file=mem)

bot.run("TOKEN")