import discord, pyfiglet, requests, random, string, base64, hashlib
from discord.ext import commands as zeenode 

class encode(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @zeenode.command()
    async def encode_base64(self, ctx, message):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(message).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)
    

    @zeenode.command()
    async def encode_md5(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.md5(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @zeenode.command()
    async def encode_sha1(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.sha1(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)



    @zeenode.command()
    async def encode_sha384(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.sha3_384(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @zeenode.command()
    async def encode_sha224(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.sha3_224(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
    
    @zeenode.command()
    async def encode_shake128(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.shake_128(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
        
        
        
    @zeenode.command()
    async def encode_sha512(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.sha3_512(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
        
        
        
    
    
    
    @zeenode.command()
    async def encode_shake256(self, ctx, message):
        await ctx.message.delete()
        msg = hashlib.shake_256(message.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

def setup(bot):
    bot.add_cog(encode(bot))
