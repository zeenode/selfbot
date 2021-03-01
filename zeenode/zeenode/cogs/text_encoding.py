import discord, pyfiglet, requests, random, string, base64, hashlib
from discord.ext import commands as zeenode 

class encode(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @zeenode.command()
    async def encode_base64(self, ctx, *, args):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(args).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)
    

    @zeenode.command()
    async def encode_md5(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.md5(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @zeenode.command()
    async def encode_sha1(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha1(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)


    @zeenode.command()
    async def encode_sha384(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_384(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)


    @zeenode.command()
    async def encode_sha224(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_224(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)


    @zeenode.command()
    async def encode_sha512(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_512(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
        

    @zeenode.command()
    async def encode_leet(self, ctx, *, args):
        await ctx.message.delete()
        encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
        await ctx.send(f'`{encoded}`')


def setup(bot):
    bot.add_cog(encode(bot))