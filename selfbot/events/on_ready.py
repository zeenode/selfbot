from discord.ext import commands
from colorama import Fore

class on_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''{Fore.RESET}
                                {Fore.GREEN}╔═╗╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗  
                                {Fore.LIGHTBLACK_EX}╔═╝║╣ ║╣ ║║║║ ║ ║║║╣   
                                {Fore.WHITE}╚═╝╚═╝╚═╝╝╚╝╚═╝═╩╝╚═╝
        ''' + Fore.RESET)

def setup(bot):
    print("[+] on_ready event loaded!")
    bot.add_cog(on_ready(bot))