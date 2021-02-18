import discord, requests, pyfiglet, datetime, aiohttp
import io 
from discord.ext import commands as zeenode
from zeenode.load import token

Output = "[ERROR] - "


class Main(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

        
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
            print(f"{Fore.GREEN} Succesfully set your HypeSquad house to {house}!")
        except:
            print(f"{Fore.RED}{Output} {Fore.YELLOW}Failed to set your HypeSquad house to {house}.") 


    @zeenode.command()
    async def embed(self, ctx, *, description):
        await ctx.message.delete()
        embed = discord.Embed(description=description, color=0x0000)
        await ctx.send(embed=embed)
            
            
    @zeenode.command(aliases=["suggestion"])
    async def suggest(self, ctx, *, suggestion):
            await ctx.message.delete()
            embed = discord.Embed(title="Suggestion:", color=0x0000, description=suggestion)
            embed.set_thumbnail(url="")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('\U0001F44D')
            await msg.add_reaction('\U0001F44E')
            
            
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
    

    @zeenode.command(aliases=["guildinfo"])
    async def serverinfo(self,ctx):
        await ctx.message.delete()
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                            description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                            timestamp=datetime.datetime.utcnow(), color=0x0000)
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        await ctx.send(embed=embed)

        
    @zeenode.command()
    async def guildicon(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
        embed.set_image(url=ctx.guild.icon_url)
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
