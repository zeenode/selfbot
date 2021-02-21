import discord, requests, pyfiglet
from discord.ext import commands as zeenode

class emoticons(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


    @zeenode.command()
    async def listemoticons(self, ctx):
        await ctx.message.delete()
        text = "fuckyou, lenny, what, bear, worried, ak47, awp, lmg, sword, love, goodnight, smile"
        await ctx.send(text)

    @zeenode.command()
    async def fuckyou(self, ctx):
        await ctx.message.delete()
        middle = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middle)

    @zeenode.command()
    async def lenny(self, ctx):
        await ctx.message.delete()
        lenny = '( ͡° ͜ʖ ͡°)'
        await ctx.send(lenny)

    @zeenode.command()
    async def what(self, ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @zeenode.command()
    async def bear(self, ctx):
        await ctx.message.delete()
        bear = 'ʕ •ᴥ•ʔ'
        await ctx.send(bear)

    @zeenode.command()
    async def worried(self, ctx):
        await ctx.message.delete()
        worried = '(´･ _･｀)'
        await ctx.send(worried)

    @zeenode.command()
    async def ak47(self, ctx):
        await ctx.message.delete()
        ak = '︻╦╤─'
        await ctx.send(ak)


    @zeenode.command()
    async def awp(self, ctx):
        await ctx.message.delete()
        awp = '︻デ═一'
        await ctx.send(awp)

    @zeenode.command()
    async def lmg(self, ctx):
        await ctx.message.delete()
        lmg = '︻╦̵̵͇̿̿̿̿╤──'
        await ctx.send(lmg)

    @zeenode.command()
    async def sword(self, ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @zeenode.command()
    async def love(self, ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @zeenode.command()
    async def goodnight(self, ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @zeenode.command()
    async def smile(self, ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)



def setup(bot):
    bot.add_cog(emoticons(bot))
