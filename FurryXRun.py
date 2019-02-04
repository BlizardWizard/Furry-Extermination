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
from google.cloud import storage

project_dir = os.getcwd().replace('\\', '/')
# Change these values to the correct values for your files
googleAPIJsonPath = project_dir + "/GoogleVision.json"
discordTokenPath = project_dir + "/tokenSecret.txt"
discord_client = discord.Client()
bot = commands.Bot(command_prefix="%")


storage_client = storage.Client.from_service_account_json(googleAPIJsonPath)
vision_client = vision.ImageAnnotatorClient("#ce611d78e4f74b7b169081bb0fdb1ed7bd3daa8d")


@bot.event
async def on_ready():
    print("FurryXterminator is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Xterminating Furries"))


file = 'E:/Ivar/Desktop/Quarantine/download.jpg'
with io.open(file, 'rb') as image_file:
    file_content = image_file.read()
    image = vision.types.Image(content=file_content)

response = vision_client.label_detection(image=image)
labels = response.label_annotations
for label in labels:
    print(label.description)


token_file = open(discordTokenPath, 'r')
token = token_file.readline().replace('\n', '')
token_file.close()
bot.run(token)
