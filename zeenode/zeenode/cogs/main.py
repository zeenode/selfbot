import discord, requests, pyfiglet, datetime, aiohttp, urllib3, asyncio
import io 
from discord.ext import commands as zeenode
from zeenode.load import token
from zeenode.config import prefix

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

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
            

    @zeenode.command()
    async def help(self, ctx, category=None):
        await ctx.message.delete()
        if category is None:
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.add_field(name="`\uD83D\uDCF1 - Activity`", value="Shows all **activity** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDCB0 - Currency`", value="Shows all **currency** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDC40 - Emoticons`", value="Shows all **emoticons** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDE02 - Fun`", value="Shows all **fun** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDD25 - Main`", value="Shows all **main** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDEE1\uFE0F - Mass`", value="Shows all **mass** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDD1E - Nsfw`", value="Shows all **nsfw** commands.", inline=False)
            embed.add_field(name="`\uD83D\uDCC3 - Text Encoding`", value="Shows all **text encoding** commands.", inline=False)
            await ctx.send(embed=embed)
        elif str(category).lower() == "activity":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDCF1 - Activity Commands`\n`> listening <text>` - Shows listening status.\n`> playing <text>` - Shows playing status.\n`> watching <text>` - Shows watching status.\n`> streaming <text>` - Shows streaming status.\n`> stopactivity` - Stops activity."
            await ctx.send(embed=embed)
        elif str(category).lower() == "currency":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDCB0 - Currency Commands`\n`> btc` - Shows BitCoin price. \n`> doge` - Shows Doge price.\n`> eth` - Shows Ethereum price.\n`> xmr` - Shows Monero price.\n`> xrp` - Shows Ripple price."
            await ctx.send(embed=embed)
        elif str(category).lower() == "emoticons":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDC40 - Emoticons Commands`\n`> fuckyou` - Sends fuckyou emoticon. \n`> lenny` - Sends lenny emoticon.\n`> what` - Sends what emoticon.\n`> bear` - Sends bear emoticon.\n`> worried` - Sends worried emoticon.\n`> ak47` - Sends ak47 emoticon.\n`> awp` - Sends awp emoticon.\n`> lmg` - Sends lmg emoticon.\n`> sword` - Sends sword emoticon.\n`> love` - Sends love emoticon.\n`> goodnight` - Sends goodnight emoticon.\n`> smile` - Sends smile emoticon."
            await ctx.send(embed=embed)
        elif str(category).lower() == "fun":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDE02 - Fun Commands`\n`> cat` - Sends a random cat image.\n`> dog` - Sends a random dog image.\n`> panda` - Sends a random panda image.\n`> dick <@user>` - Shows user dick size.\n`> hug <@user>` - Sends a hug to user.\n`> kiss <@user>` - Sends a kiss to user.\n`> slap <@user>` - Sends a slap to user.\n`> meme` - Sends a random meme.\n`> nitro` - Sends a nitro."
            await ctx.send(embed=embed)
        elif str(category).lower() == "main":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDD25 - Main Commands`\n`> ascii <message>` - Sends message as ascii art. \n`> embed <message>` - Sends embed message.\n`> av <@user>` - Sends your avatar in the chat.\n`> guildicon` - Shows server (guild) icon.\n`> serverinfo` - Shows server info.\n`> whois <@user>` - Sends info about user.\n`> hypesquad <house>` - Allows you to change your hypesquad house/badge.\n`> purge <number of messages>` - Deletes messages.\n`> suggest <question>` - Sends question with embed leaving thumbsup & thumbsdown react."
            await ctx.send(embed=embed)
        elif str(category).lower() == "mass":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDEE1\uFE0F - Mass Commands`\n`> massreact <emoji>` - Reacts to last 20 messages with emojis.\n`> spam <number of messages>` - Spams messages."
            await ctx.send(embed=embed)
        elif str(category).lower() == "nsfw":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDD1E - Nsfw Commands`\n`> anal <user>` - Sends nsfw anime content.\n`> blowjob <user>` - Sends nsfw anime content.\n`> boobs <user>` - Sends nsfw anime content.\n`> hentai <user>` - Sends hentai (anime porn)."
            await ctx.send(embed=embed)
        elif str(category).lower() == "textencoding":
            embed = discord.Embed(color=0x0000, timestamp=ctx.message.created_at)
            embed.set_author(name="Zeenode Self-Bot | Prefix: " + str(bot.command_prefix),
                            icon_url="https://cdn.discordapp.com/attachments/796868392095186976/812453623309008927/zeenode_logo.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/796868392095186976/812744896439910450/zeenode_banner.gif")
            embed.description = f"`\uD83D\uDCC3 - Text Encoding Commands`\n`> encode_base64 <word/message>` - Encodes text with Base64.\n`> encode_leet <word/message>` - Encodes text with leet speak.\n`> encode_md5 <word/message>` - Encodes text with MD5 hash.\n`> encode_sha1 <word/message>` - Encodes text with Sha1.\n`> encode_sha224 <word/message>` - Encodes text wish SHA224.\n`> encode_sha384 <word/message>` - Encodes text with Sha384.\n`> encode_sha251 <word/message>` - Encodes text with Sha512."
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
    async def whois(self, ctx, *, user: discord.User = None): 
        await ctx.message.delete()
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        return await ctx.send(embed=em)
      
      
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
