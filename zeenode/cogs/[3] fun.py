import discord, pyfiglet, requests, random, string, aiohttp, io
from discord.ext import commands as zeenode 

class Fun(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    @zeenode.command()
    async def slap(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @zeenode.command()
    async def hug(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @zeenode.command(aliases=['dong', 'penis'])
    async def dick(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(title=f"{user}'s Dick size:", description=f"8{dong}D", colour=0x0000)
        await ctx.send(embed=em)
    

    
    
    @zeenode.command()
    async def kiss(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} kissed {user.mention}!**", color=RandomColor())
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
     
    @zeenode.command(aliases=['pfp', 'avatar'])
    async def av(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        format = "gif"
        user = user or ctx.author
        if user.is_avatar_animated() != True:
            format = "png"
        avatar = user.avatar_url_as(format=format if format != "gif" else None)
        async with aiohttp.ClientSession() as session:
            async with session.get(str(avatar)) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Avatar.{format}"))
    
    
    @zeenode.command()
    async def guildicon(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    

    @zeenode.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(color=RandomColor())
        embed.set_author(name="Here is the your meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
        embed.set_image(url=str(r["image"]))
        await ctx.send(embed=embed)


    @zeenode.command()
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
    print("[+] fun cog loaded!")
    bot.add_cog(Fun(bot))
