import discord, requests
from discord.ext import commands
from ..load import token

Output = "Zeenode || "

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message,
            url = "https://www.twitch.tv/zeenode", 
        )
        await self.bot.change_presence(activity=stream)    


    @commands.command()
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
        else:
            self.ctx.message.channel.send('That option is invalid. Please enter some of these options: bravery, brilliance, balance')


    @commands.command()
    async def embed(self, ctx, title, *, description):
            await ctx.message.delete()
            embed=discord.Embed(title=title, description=description)
            await ctx.send(embed=embed)


    @commands.command()
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

def setup(bot):
    print("[+] main cog loaded!")
    bot.add_cog(Main(bot))