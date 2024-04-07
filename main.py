import os

import discord
from discord.ext import commands
import functions

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=discord.Intents.default())
getData = functions.get()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await (bot.change_presence(activity=discord.CustomActivity(name="Testing, Attention Please")))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def hello(ctx):
    await ctx.send('ㅂㅅ')


bot.run(getData.Token())