import os
import discord, time, random, openai, requests
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

#jika ada member join
@client.event
async def on_member_join(member):
  member, buangan = str(member).split("#")
  channel = client.get_channel(1093375640943722536)
  #role = discord.utils.get(member.guild.roles, name = "orang biasa")
  #await member.add_roles(role)
    
  await channel.send(f"Hello {member}!!")
  

#jika ada member keluar
@client.event
async def on_member_remove(member):
  member, buangan = str(member).split("#")
  channel = client.get_channel(762903325494083615)
  await channel.send(f"Bye {member} :(")

#---------------------------------------------------------------------------------#
#!weather
@client.command(aliases = ["weather"])
async def cuaca(ctx, kota: str):
#emoji untuk cuaca
  emoji = {
    "Clouds" : "☁️",
    "Clear" : "☀️"
  }
  
  if ctx == "":
    await ctx.send("input salah")
    return
  weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={kota}&units=imperial&APPID={my_weather_secret}")
  try:
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])
  except:
    await ctx.send("Kota tidak ditemukan")
    return
  ketemu = f"Cuaca di {kota} adalah {weather}{emoji.get(weather)}\nSuhu pada {kota} adalah {temp}°K"
  
  
  embed = discord.Embed(
    title="Cuaca",
    description= ketemu,
    color=discord.Color.blue(),
    timestamp= ctx.message.created_at
    )
  await ctx.send(embed = embed)
client.run(my_secret)