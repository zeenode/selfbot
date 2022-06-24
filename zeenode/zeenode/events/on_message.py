import re
import requests
from colorama import Fore
from discord.ext import commands as zeenode
from zeenode.load import token
from zeenode.config import nitro_sniper
from datetime import datetime
import discord as zeenode_dm
time = datetime.now().strftime("%H:%M:%S")

class on_message(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    @zeenode.Cog.listener()
    async def on_message(self, message):
        
        if isinstance(message.channel, zeenode_dm.channel.DMChannel) and message.author != self.bot.user:
            await message.channel.send('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n\n**Ciao Combattente!**    :heart_on_fire:    Unisciti al\n:dragon_face:    **DRAGON ARENA    :trolleybus:    *BUS-IT***    :flag_it:\n\nLINK al server discord: https://discord.gg/fukMg7XUc7\n\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
      
        if nitro_sniper == "true":
            try:
                regex = re.search(r'(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)', message.content)
                regex2 = regex.group(2)
                if regex:
                    if len(regex2) == 16 or len(regex2) == 24:
                        claim = await self.claim_code(regex2)
                        status = claim['message']
                        if 'subscription_plan' in status:
                            print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}{time}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Someone sent nitro gift code ({Fore.LIGHTGREEN_EX}{regex2}{Fore.WHITE}). I claimed it!")
                        else:
                            print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}{time}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Someone sent nitro gift code ({Fore.LIGHTRED_EX}{regex2}{Fore.WHITE}). But it was claimed.{Fore.RESET}")
            except:
                pass
        else:
            pass

    async def claim_code(self, code: str):
            r = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',headers=self.client_headers(), json={'channel_id': None, 'payment_source_id': None})
            if 'subscription_plan' not in r.text:
                try:
                    message = r.json()['message']
                except (AttributeError, IndexError, KeyError):
                    message = "cloudflare"
                return {'valid': False, 'message': message}
            else:
                return {'valid': True, 'message': r.json()}

    def client_headers(self):
        return {
            'Authorization': token,
            'Content-Type': 'application/json',
        }

def setup(bot):
    bot.add_cog(on_message(bot))