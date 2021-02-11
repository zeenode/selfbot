from discord.ext import commands as zeenode
import re
import requests
from selfbot.load import token

class on_message(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    @zeenode.Cog.listener()
    async def on_message(self, message):
        try:
            regex = re.search(r'(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)', message.content)
            regex2 = regex.group(2)
            if regex:
                if len(regex2) == 16 or len(regex2) == 24:
                    claim = await self.claim_code(regex2)
                    status = claim['message']
                    if 'subscription_plan' in status:
                        print(f"[+] Someone sent nitro code. I claimed it!")
                    else:
                        print(f"[-] Someone sent nitro code. It was claimed.")
        except:
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
    print("[+] on_message event loaded!")
    bot.add_cog(on_message(bot))