import os
import asyncio
import discord, time, random, openai, requests
from discord.ext import commands


my_weather_secret = os.environ['WEATHER_API']
my_secret = os.environ['DISCORD_TOKEN']
openai.api_key = os.environ['CHATGPT_API']

intents = discord.Intents.all()
intents.members = True
intents.reactions = True


bot = commands.Bot(command_prefix = '!', intents = intents)

async def load():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{filename[:-3]}")
      print(filename)

async def main():
  async with bot:
    await asyncio.gather(load())
    await bot.start(my_secret)



#---------------------------------------------------------------------------------#


asyncio.run(main())