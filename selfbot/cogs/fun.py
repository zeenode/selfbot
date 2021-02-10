import discord, json, pyfiglet, requests, random, string, urllib
from colorama import Fore, Back, Style 
from discord.ext import commands
from ..login import token

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ascii(self, ctx, args):
        await ctx.message.delete()
        text = pyfiglet.figlet_format(args)
        await ctx.send(f'```{text}```')

    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} kissed {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


    @commands.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(color=RandomColor())
        embed.set_author(name="Here is the your meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
        embed.set_image(url=str(r["image"]))
        await ctx.send(embed=embed)


    @commands.command()
    async def nitro(self, ctx):
            await ctx.message.delete()
            await ctx.send(Nitro())


def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"
        
def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

def setup(bot):
    bot.add_cog(Fun(bot))
