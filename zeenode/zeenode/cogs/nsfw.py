import discord, pyfiglet, requests
from discord.ext import commands as zeenode 

class nsfw(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot




    @zeenode.command()
    async def blowjob(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/blowjob")
        json = api.json()
        msg = discord.Embed(description=user.mention + " This could be you and me")
        msg.set_image(url=json['url'])
        
        await ctx.send(embed=msg)

    @zeenode.command()
    async def boobs(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/boobs")
        json = api.json()
        msg = discord.Embed(description=user.mention + " This could be you and me ")
        msg.set_image(url=json['url'])
        
        await ctx.send(embed=msg)
    
    
    
    @zeenode.command()
    async def anal(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/anal")
        json = api.json()
        msg = discord.Embed(description=user.mention + " This could be you and me ")
        msg.set_image(url=json['url'])
        
        await ctx.send(embed=msg)
    
    
    
    @zeenode.command()
    async def hentai(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        json = api.json()
        msg = discord.Embed(description=user.mention + " This could be you and me ")
        msg.set_image(url=json['url'])
        
        await ctx.send(embed=msg)
    
  
    
   
def setup(bot):
    bot.add_cog(nsfw(bot))