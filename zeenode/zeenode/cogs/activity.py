import discord, requests, pyfiglet
from discord.ext import commands as zeenode
from zeenode.load import token

Output = "Zeenode || "

class Activity(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


    @zeenode.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message,
            url = "https://www.twitch.tv/zeenode", 
        )
        await self.bot.change_presence(activity=stream)    

        
    @zeenode.command()
    async def playing(self, ctx, *, message):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.bot.change_presence(activity=game)
    
    
    @zeenode.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name=message, 
            ))
           
            
    @zeenode.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name=message
            ))


    @zeenode.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)


def setup(bot):
    bot.add_cog(Activity(bot))