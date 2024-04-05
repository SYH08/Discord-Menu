import discord
from discord.ext import commands
import functions

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=discord.Intents.default())

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

getPrivate = functions.getPrivate()
bot.run(getPrivate.getToken())
