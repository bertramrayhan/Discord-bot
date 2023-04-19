import discord
from discord.ext import commands

class Setup(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
 


  #member join server
  @commands.Cog.listener()
  async def on_member_join(self, member):
    '''embed = discord.Embed(
      tite = "Welcome!!",
      description = "Welcome to ...",
      color = discord.Colour.teal()
      
    )
    embed.set_image(member.avatar_url)'''

    
    channel = self.bot.get_channel(1093375640943722536)
    await channel.send(f"Hello {member.mention}!!!")
    #await channel.send(embed=embed)
       
    
  #member leave server
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(1093375640943722536)

    await channel.send(f"Bye {member.mention} :(")
    
    '''embed = discord.Embed(
      tite = "Bye..  :(",
      color = discord.Colour.blue()
      
    )
    await channel.send(embed= embed)'''

  #bot online
  @commands.Cog.listener()
  async def on_ready(self):
    print()
    print("The bot is online")
    


async def setup(bot):
  await bot.add_cog(Setup(bot))
    