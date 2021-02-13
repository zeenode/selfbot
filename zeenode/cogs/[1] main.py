import discord, requests, pyfiglet
from discord.ext import commands as zeenode
from zeenode.load import token

Output = "Zeenode || "

class Main(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


   




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
    async def ascii(self, ctx, args):
        await ctx.message.delete()
        text = pyfiglet.figlet_format(args)
        await ctx.send(f'```{text}```')
        
    @zeenode.command()
    async def hypesquad(self, ctx, house):
        await ctx.message.delete()
        request = requests.session()
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        global payload
        
        if house == "bravery":
            payload = {'house_id': 1}
        elif house == "brilliance":
            payload = {'house_id': 2}
        elif house == "balance":
            payload = {'house_id': 3}

        try:
            requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
            print(f"{Output}Succesfully set your HypeSquad house to {house}!")
        except:
            print(f"{Output}Failed to set your HypeSquad house to {house}.") 


    @zeenode.command()
    async def embed(self, ctx, title, *, description):
            await ctx.message.delete()
            embed=discord.Embed(title=title, description=description)
            await ctx.send(embed=embed)


    @zeenode.command()
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

def setup(bot):
    bot.add_cog(Main(bot))
