import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import io
import os
import sys
import json
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

# project_dir = os.getcwd().replace('\\', '/')
# Change these values to the correct values for your files

vision_client = vision.ImageAnnotatorClient(
    credentials=service_account.Credentials.from_service_account_info(
        json.loads(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))))

discord_client = discord.Client()
bot = commands.Bot(command_prefix="%")
#
#
@bot.event
async def on_ready():
    print("FilterBot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Filtering Images"))


file = 'E:/Ivar/Desktop/Quarantine/download.jpg'
url = 'https://media1.tenor.com/images/59371e16bf2c92a158a0bf84e1e70bb6/tenor.gif'

image = types.Image()
image.source.image_uri = url

# response = vision_client.label_detection(image=image)
# labels = response.label_annotations
# for label in labels:
#     print(labels)


# token_file = open(discordTokenPath, 'r')
# token = token_file.readline().replace('\n', '')
# token_file.close()
# bot.run(token)

bot.run(os.environ.get('BOT_TOKEN'))
