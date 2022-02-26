from argparse import ArgumentParser
from ctypes import ArgumentError
from http.client import InvalidURL
import discord, requests, pyfiglet, datetime, aiohttp, urllib3, asyncio, warnings, colorama, io
from colorama import Fore
from discord.ext import commands as zeenode
from zeenode.load import token
from zeenode.config import prefix

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

colorama.init()

Output = "[ERROR] -"

# Ignore shitty warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

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
    async def help(self, ctx, category=None):
        await ctx.message.delete()
        if category is None:
            await ctx.send("Zeenode Self-Bot | Prefix: " + str(bot.command_prefix) + "\n" + "`\uD83D\uDCF1 - Activity`" + " - " + "Shows all **activity** commands." + "\n" + "`\uD83D\uDCB0 - Currency`" + " - " + "Shows all **currency** commands." + "\n" + "`\uD83D\uDC40 - Emoticons`" + " - " + "Shows all **emoticons** commands." + "\n" + "`\uD83D\uDE02 - Fun`" + " - " + "Shows all **fun** commands." + "\n" + "`\uD83D\uDD25 - Main`" + " - " + "Shows all **main** commands." + "\n" + "`\uD83D\uDEE1\uFE0F - Mass`" + " - " + "Shows all **mass** commands." + "\n" + "`\uD83D\uDD1E - Nsfw`" + " - " + "Shows all **nsfw** commands." + "\n" + "`\uD83D\uDCC3 - TextEncoding`" + " - " + "Shows all **text encoding** commands.")
        elif str(category).lower() == "activity":
            await ctx.send(f"`\uD83D\uDCF1 - Activity Commands`\n`" + str(bot.command_prefix) + " listening <text>` - Shows listening status.\n`" + str(bot.command_prefix) + " playing <text>` - Shows playing status.\n`" + str(bot.command_prefix) + " watching <text>` - Shows watching status.\n`" + str(bot.command_prefix) + " streaming <text>` - Shows streaming status.\n`" + str(bot.command_prefix) + " stopactivity` - Stops activity.")
        elif str(category).lower() == "currency":
            await ctx.send(f"`\uD83D\uDCB0 - Currency Commands`\n`" + str(bot.command_prefix) + " btc` - Shows Bitcoin price. \n`" + str(bot.command_prefix) + " doge` - Shows Doge price.\n`" + str(bot.command_prefix) + " eth` - Shows Ethereum price.\n`" + str(bot.command_prefix) + " xmr` - Shows Monero price.\n`" + str(bot.command_prefix) + " xrp` - Shows Ripple price.")
        elif str(category).lower() == "emoticons":
            await ctx.send(f"`\uD83D\uDC40 - Emoticons Commands`\n`" + str(bot.command_prefix) + " fuckyou` - Sends fuckyou emoticon. \n`" + str(bot.command_prefix) + " lenny` - Sends lenny emoticon.\n`" + str(bot.command_prefix) + " what` - Sends what emoticon.\n`" + str(bot.command_prefix) + " bear` - Sends bear emoticon.\n`" + str(bot.command_prefix) + " worried` - Sends worried emoticon.\n`" + str(bot.command_prefix) + " ak47` - Sends ak47 emoticon.\n`" + str(bot.command_prefix) + " awp` - Sends awp emoticon.\n`" + str(bot.command_prefix) + " lmg` - Sends lmg emoticon.\n`" + str(bot.command_prefix) + " sword` - Sends sword emoticon.\n`" + str(bot.command_prefix) + " love` - Sends love emoticon.\n`" + str(bot.command_prefix) + " goodnight` - Sends goodnight emoticon.\n`" + str(bot.command_prefix) + " smile` - Sends smile emoticon.")
        elif str(category).lower() == "fun":
            await ctx.send(f"`\uD83D\uDE02 - Fun Commands`\n`" + str(bot.command_prefix) + " cat` - Sends a random cat image.\n`" + str(bot.command_prefix) + " dog` - Sends a random dog image.\n`" + str(bot.command_prefix) + " panda` - Sends a random panda image.\n`" + str(bot.command_prefix) + " dick <@user>` - Shows user dick size.\n`" + str(bot.command_prefix) + " hug <@user>` - Sends a hug to user.\n`" + str(bot.command_prefix) + " kiss <@user>` - Sends a kiss to user.\n`" + str(bot.command_prefix) + " slap <@user>` - Sends a slap to user.\n`" + str(bot.command_prefix) + " meme` - Sends a random meme.\n`" + str(bot.command_prefix) + " nitro` - Sends a nitro." + "\n`" + str(bot.command_prefix) + " zoki` - Sends a picture of zoki")
        elif str(category).lower() == "main":
            await ctx.send(f"`\uD83D\uDD25 - Main Commands`\n`" + str(bot.command_prefix) + " ascii <message>` - Sends message as ascii art. \n`" + str(bot.command_prefix) + " av <@user>` - Sends your avatar in the chat.\n`" + str(bot.command_prefix) + " servericon` - Shows server's (guild) icon.\n`" + str(bot.command_prefix) + " serverinfo` - Shows server info.\n`" + str(bot.command_prefix) + " whois <@user>` - Sends info about user.\n`" + str(bot.command_prefix) + " hypesquad <house>` - Allows you to change your hypesquad house/badge.\n`" + str(bot.command_prefix) + " purge <number of messages>` - Deletes messages.\n`" + str(bot.command_prefix) + " suggest <question>` - Sends question with embed leaving thumbsup & thumbsdown react.")
        elif str(category).lower() == "mass":
            await ctx.send(f"`\uD83D\uDEE1\uFE0F - Mass Commands`\n`" + str(bot.command_prefix) + " massreact <emoji>` - Reacts to last 20 messages with emojis.\n`" + str(bot.command_prefix) + " spam <number of messages> <message> ` - Spams messages.")
        elif str(category).lower() == "nsfw":
            await ctx.send(f"`\uD83D\uDD1E - Nsfw Commands`\n`" + str(bot.command_prefix) + " anal <user>` - Sends nsfw anime content.\n`" + str(bot.command_prefix) + " blowjob <user>` - Sends nsfw anime content.\n`" + str(bot.command_prefix) + " boobs <user>` - Sends nsfw anime content.\n`" + str(bot.command_prefix) + " hentai <user>` - Sends hentai (anime porn).")
        elif str(category).lower() == "textencoding":
            await ctx.send(f"`\uD83D\uDCC3 - Text Encoding Commands`\n`" + str(bot.command_prefix) + " encode_base64 <word/message>` - Encodes text with Base64.\n`" + str(bot.command_prefix) + " encode_leet <word/message>` - Encodes text with leet speak.\n`" + str(bot.command_prefix) + " encode_md5 <word/message>` - Encodes text with MD5 hash.\n`" + str(bot.command_prefix) + " encode_sha1 <word/message>` - Encodes text with Sha1.\n`" + str(bot.command_prefix) + " encode_sha224 <word/message>` - Encodes text wish SHA224.\n`" + str(bot.command_prefix) + " encode_sha384 <word/message>` - Encodes text with Sha384.\n`" + str(bot.command_prefix) + " encode_sha512 <word/message>` - Encodes text with Sha512.")


    @zeenode.command(aliases=["suggestion"])
    async def suggest(self, ctx, *, suggestion):
        await ctx.message.delete()
        msg = await ctx.send("Suggestion: " + suggestion)
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
        try:
            await ctx.send(f"Server Info of {ctx.guild.name}:" + "\n" + "Server created at" + " - " + f"{ctx.guild.created_at.strftime(date_format)}" + "\n" + "Server Owner" + " - " + f"<@{ctx.guild.owner_id}>" + "\n" + "Server ID" + " - " + f"{ctx.guild.id}" + "\n" + f"{ctx.guild.member_count} Members\n{len(ctx.guild.roles)} Roles\n{len(ctx.guild.text_channels)} Text-Channels\n{len(ctx.guild.voice_channels)} Voice-Channels\n{len(ctx.guild.categories)} Categories")
        except AttributeError:
            print(f"{Fore.RED}{Output} {Fore.YELLOW}You tried to get info of someones dm not a server!") 

        
    @zeenode.command(aliases=["servericon"])
    async def guildicon(self, ctx):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(str(ctx.guild.icon_url)) as resp:
                    if resp.status != 200:
                        return await ctx.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'img.png'))
            except AttributeError:
                print(f"{Fore.RED}{Output} {Fore.YELLOW}You tried to get icon of someones dm not a server!")
            except:
                 print(f"{Fore.RED}{Output} {Fore.YELLOW}This server doesn't have an icon set!")

    @zeenode.command()
    async def whois(self, ctx, *, user: discord.User = None): 
        await ctx.message.delete()
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        return await ctx.send("Registered: " + user.created_at.strftime(date_format))
      
      
    @zeenode.command(aliases=["clear"])
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    @zeenode.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, zeenode.MissingRequiredArgument):
            await ctx.message.delete()
            print(f"{Fore.RED}{Output} {Fore.YELLOW}You need to specify how many messages you would like to delete!")

def setup(bot):
    bot.add_cog(Main(bot))
