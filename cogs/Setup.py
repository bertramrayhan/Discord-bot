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
    
  #list command
  @commands.command()
  async def commands(self, ctx):
    embed = discord.Embed(title="Command List", color=0x00ff00, timestamp= ctx.message.created_at)

    embed.add_field(name="halo", value="Menyapa bot\nContoh : !halo", inline=False)
    embed.add_field(name="ping", value="mengetes apakah bot online\nContoh : !ping", inline=False)
    embed.add_field(name="roll", value="Mengocok dadu enam sisi\nContoh : !roll 3", inline=False)
    embed.add_field(name="cuaca jember", value="Menampilkan informasi cuaca dan suhu di kota-kota di dunia\nContoh : !cuaca jember, !weather jember", inline=False)
    embed.add_field(name="tebak angka", value="Menebak angka dari 1-10\nContoh : !tebakangka", inline=False)
    embed.add_field(name="suit", value="Bermain suit dengan bot\nContoh : !suit gunting, !gubake gunting", inline=False)
    embed.add_field(name="latency", value="Untuk mengetahui apakah bot sedang berjalan dengan lancar atau tidak\nContoh !latency")

    await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Setup(bot))
    