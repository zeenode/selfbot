import discord, pyfiglet, requests, json
from discord.ext import commands as zeenode 

class currency(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


    @zeenode.command()
    async def btc(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')



    @zeenode.command()
    async def xmr(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')




    @zeenode.command()
    async def xrp(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')


    @zeenode.command()
    async def doge(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')

    @zeenode.command()
    async def eth(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')


def setup(bot):
    bot.add_cog(currency(bot))
