import requests, colorama
from colorama import Fore
from discord.ext import commands as zeenode
from zeenode.config import auth, prefix, nitro_sniper, giveaway_sniper

colorama.init()

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)

class load:
    def __init__(self):
        global token
        
        token = self.check_token(auth)

        nsign = ""
        gsign = ""
        nsign, nsniper = self.nitro_sniper(nsign, nitro_sniper)
        gsign, gsniper = self.nitro_sniper(gsign, giveaway_sniper)


        @bot.event
        async def on_ready():

            self.load_cogs()
            print(f'''{Fore.RESET}
                            {Fore.LIGHTBLACK_EX}╔═════════════════════════════╗
                            {Fore.LIGHTBLACK_EX}║ {Fore.GREEN}╔═╗ ╔═╗ ╔═╗ ╔╗╔ ╔═╗ ╔╦╗ ╔═╗ {Fore.LIGHTBLACK_EX}║ 
                            {Fore.LIGHTBLACK_EX}║ {Fore.LIGHTGREEN_EX}╔═╝ ║╣  ║╣  ║║║ ║ ║  ║║ ║╣  {Fore.LIGHTBLACK_EX}║ 
                            {Fore.LIGHTBLACK_EX}║ {Fore.WHITE}╚═╝ ╚═╝ ╚═╝ ╝╚╝ ╚═╝ ═╩╝ ╚═╝ {Fore.LIGHTBLACK_EX}║
                            {Fore.LIGHTBLACK_EX}╚═════════════════════════════╝

                                {Fore.WHITE}Logged in as {Fore.LIGHTGREEN_EX}{bot.user}
                             {Fore.WHITE}You are currecly in {Fore.LIGHTGREEN_EX}{len(list(bot.guilds))}{Fore.WHITE} server(s).
                          {Fore.WHITE}You have {Fore.LIGHTGREEN_EX}{len(list(bot.user.friends))}{Fore.WHITE} Friend(s) in friend list.
                   {Fore.WHITE}Zeenode's prefix is {Fore.LIGHTGREEN_EX}{prefix}{Fore.WHITE}, for command-list type {Fore.LIGHTGREEN_EX}{prefix}help{Fore.WHITE}.

                              {Fore.LIGHTBLACK_EX}[{nsign}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Nitro Sniper is {nsniper}{Fore.WHITE}.
                              {Fore.LIGHTBLACK_EX}[{gsign}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Giveaway Sniper is {gsniper}{Fore.WHITE}.
                                
                                    ''' + Fore.RESET)

        bot.run(token, bot=False)

    def nitro_sniper(self, nitrosniper_sign, nitrosniper):
        if nitrosniper == "true":
            nitrosniper_sign = f"{Fore.LIGHTGREEN_EX}!"
            nitrosniper = f"{Fore.LIGHTGREEN_EX}enabled"
            return nitrosniper_sign, nitrosniper

        elif nitrosniper == "false":
            nitrosniper_sign = f"{Fore.LIGHTRED_EX}-"
            nitrosniper = f"{Fore.LIGHTRED_EX}disabled"
            return nitrosniper_sign, nitrosniper
        else:
            nitrosniper_sign = f"{Fore.LIGHTYELLOW_EX}?"
            nitrosniper = f"{Fore.LIGHTYELLOW_EX}invalid"
            return nitrosniper_sign, nitrosniper

        
    def giveaway_sniper(self, giveawaysniper_sign, giveawaysniper):
        if giveawaysniper == "true":
            giveawaysniper = f"{Fore.LIGHTGREEN_EX}!"
            giveawaysniper = f"{Fore.LIGHTGREEN_EX}enabled"
            return giveawaysniper_sign, giveawaysniper

        elif giveawaysniper == "false":
            giveawaysniper = f"{Fore.LIGHTRED_EX}-"
            giveawaysniper = f"{Fore.LIGHTRED_EX}disabled"
            return giveawaysniper_sign, giveawaysniper
        else:
            giveawaysniper_sign = f"{Fore.LIGHTYELLOW_EX}?"
            giveawaysniper = f"{Fore.LIGHTYELLOW_EX}invalid"
            return giveawaysniper_sign, giveawaysniper

    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Check /zeenode/config.py file to setup auto-login with token (If you have already set token there please make sure token is valid)")
            print("Please insert your token below:")
            token_input = input()
            token = token_input
            return token
    def load_cogs(self):
         # Loading commands
        bot.load_extension("zeenode.cogs.[3] fun")
        bot.load_extension("zeenode.cogs.[1] main")
        bot.load_extension("zeenode.cogs.[2] activity")
        bot.load_extension("zeenode.cogs.text_encoding")

        # Loading events
        bot.load_extension("zeenode.events.on_message")
