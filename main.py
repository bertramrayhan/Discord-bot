import os
import discord, time, random, openai
from discord.ext import commands


my_weather_secret = os.environ['WEATHER_API']
my_secret = os.environ['DISCORD_TOKEN']
openai.api_key = os.environ['CHATGPT_API']

intents = discord.Intents.all()
intents.members = True
intents.reactions = True


client = commands.Bot(command_prefix = '!', intents = intents)

#untuk mengaktifkan bot
@client.event
async def on_ready():
  print()
  print("The bot is online")

client.run(my_secret)