from colorama import Fore
from discord.ext import commands

bot = commands.Bot(command_prefix="!", self_bot=True)

class login:
    def __init__(self):
        global token
        print("please insert your token below:")
        token = input()
        
        bot.load_extension("selfbot.cogs.fun")
        bot.load_extension("selfbot.cogs.extra")

        @bot.event
        async def on_ready():
            print(f'''{Fore.RESET}
                                    {Fore.GREEN}╔═╗╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗  
                                    {Fore.LIGHTBLACK_EX}╔═╝║╣ ║╣ ║║║║ ║ ║║║╣   
                                    {Fore.WHITE}╚═╝╚═╝╚═╝╝╚╝╚═╝═╩╝╚═╝
            ''' + Fore.RESET)

        bot.run(token, bot=False)