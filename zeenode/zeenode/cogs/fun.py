import discord, pyfiglet, requests, random, string, aiohttp, io, hashlib, base64
from discord.ext import commands as zeenode 

class Fun(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @zeenode.command()
    async def slap(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(res["url"]) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except:
                    pass

        
    @zeenode.command()
    async def hug(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(res["url"]) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except:
                    pass

        
    @zeenode.command(aliases=['dong', 'penis'])
    async def dick(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        size = random.randint(1, 50)
        dong = ""
        for _i in range(0, size):
            dong += "="
        await ctx.send(f"{user}'s Dick size:\n" + f"8{dong}D")
    
    @zeenode.command()
    async def zoki(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/931953860988252170/947183625932267541/unknown.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    pass
    
    @zeenode.command()
    async def kiss(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(res["url"]) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except:
                    pass
     
   
    
    @zeenode.command()
    async def panda(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/panda").json()
        async with aiohttp.ClientSession() as session:
            async with session.get(str(r["link"])) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    pass
    
    
    @zeenode.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/meme").json()
        async with aiohttp.ClientSession() as session:
            async with session.get(str(r["image"])) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    pass

        
    @zeenode.command()
    async def cat(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/cat").json()
        async with aiohttp.ClientSession() as session:
            async with session.get(str(r["link"])) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    pass 
    
    
    @zeenode.command()
    async def dog(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/dog").json()
        async with aiohttp.ClientSession() as session:
            async with session.get(str(r["link"])) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    pass  


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
    bot.add_cog(Fun(bot))
