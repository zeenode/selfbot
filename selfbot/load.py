from discord.ext import commands

bot = commands.Bot(command_prefix="!", self_bot=True)

class load:
    def __init__(self):
        global token
        print("please insert your token below:")
        token = input()
        
        # Loading commands
        bot.load_extension("selfbot.cogs.fun")
        bot.load_extension("selfbot.cogs.main")

        # Loading events
        bot.load_extension("selfbot.events.on_message")
        bot.load_extension("selfbot.events.on_ready")

        bot.run(token, bot=False)