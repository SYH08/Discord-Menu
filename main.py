import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def hello(ctx):
    await ctx.send('ㅂㅅ')

bot.run("MTIyNTgxNTUxMTQyMjczNDQ0OA.GrRiH2.J5wjGd2KAgzaFxBicSxY4dbMXAvVetgG2onph4")
