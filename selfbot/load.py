from colorama.ansi import Fore
from discord.ext import commands as zeenode
from selfbot.config import auth, prefix
import requests

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)

class load:
    def __init__(self):
        global token

        token = self.check_token(auth)

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
                             {Fore.WHITE}You are currecly in {Fore.LIGHTGREEN_EX}{len(list(bot.guilds))}{Fore.WHITE} server.
                          {Fore.WHITE}You have {Fore.LIGHTGREEN_EX}{len(list(bot.user.friends))}{Fore.WHITE} Friend(s) in friend list.
                   {Fore.WHITE}Zeenode's prefix is {Fore.LIGHTGREEN_EX}{prefix}{Fore.WHITE}, for command-list type {Fore.LIGHTGREEN_EX}{prefix}help

                              {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Nitro Sniper is enabled
                              {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Giveaway Sniper is enabled
                                
                                    ''' + Fore.RESET)

        bot.run(token, bot=False)

    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Check /selfbot/config.py file to setup auto-login with token (If you have already set token there please make sure token is valid)")
            print("Please insert your token below:")
            token_input = input()
            token = token_input
            return token
    def load_cogs(self):
         # Loading commands
        bot.load_extension("selfbot.cogs.fun")
        bot.load_extension("selfbot.cogs.main")

        # Loading events
        bot.load_extension("selfbot.events.on_message")
