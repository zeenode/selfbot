from discord.ext import commands
from selfbot.config import auth
import requests

bot = commands.Bot(command_prefix="!", self_bot=True)

class load:
    def __init__(self):
        global token

        token = self.check_token(auth)

        # Loading commands
        bot.load_extension("selfbot.cogs.fun")
        bot.load_extension("selfbot.cogs.main")

        # Loading events
        bot.load_extension("selfbot.events.on_message")
        bot.load_extension("selfbot.events.on_ready")

        bot.run(token, bot=False)

    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Check /selfbot/config.py file to setup auto-login with token (If you have already set token there make sure token is valid)")
            print("Please insert your token below:")
            token_input = input()
            token = token_input
            return token