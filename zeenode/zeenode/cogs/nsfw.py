import discord, pyfiglet, requests, io, aiohttp, warnings, colorama
from colorama import Fore
from http.client import HTTPException
from discord.ext import commands as zeenode 

# Ignore shitty warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

Output = "[ERROR] -"

class nsfw(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


    @zeenode.command()
    async def blowjob(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/blowjob")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Output} {Fore.YELLOW}This user has disabled NSFW content in their dms")



    @zeenode.command()
    async def boobs(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/boobs")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Output} {Fore.YELLOW}This user has disabled NSFW content in their dms")
    
    
    @zeenode.command()
    async def anal(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/anal")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Output} {Fore.YELLOW}This user has disabled NSFW content in their dms")
    
    
    @zeenode.command()
    async def hentai(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Output} {Fore.YELLOW}This user has disabled NSFW content in their dms")


def setup(bot):
    bot.add_cog(nsfw(bot))