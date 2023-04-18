import discord
from discord.ext import commands

class Setup(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel("1093375640943722536")

    
    embed = discord.Embed(
      tite = "Welcome!!",
      description = "Welcome to ...",
      color = discord.Colour.teal()
      
    )
    embed.set_image(member.avatar_url)
    await channel.send(embed= embed)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel("1093375640943722536")

    
    embed = discord.Embed(
      tite = "Bye..  :(",
      color = discord.Colour.blue()
      
    )
    await channel.send(embed= embed)

  @commands.Cog.listener()
  async def on_ready():
    print()
    print("The bot is online")

async def setup(bot):
  await bot.add_cog(Setup(bot))
    