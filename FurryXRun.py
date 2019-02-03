import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

Client = discord.Client()
bot = commands.Bot(command_prefix="%")



@bot.event
async def on_ready():
    print("FurryXterminator is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="do \'.help\'"))
    servers.update_servers(bot)


token_file = open('tokenSecret.txt', 'r')
token = token_file.readline()
token_file.close()
bot.run(token)
