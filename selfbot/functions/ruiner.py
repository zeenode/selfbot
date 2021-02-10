import discord
client = discord.Client()

class ruiner:
    async def removeFriends():
        for friend in client.user.friends:
            await friend.remove_friend()
            print(f"removed {friend.name}#{friend.discriminator} from friend list")

    async def leaveServers():
        for i in range(0, len(client.guilds), 10):
            guilds = client.guilds[i:i + 10]
        
            for guild in guilds:
                gid = client.get_guild(guild.id)
                try:
                    await gid.leave()
                    print(f"i left {guild}")
                except:
                    await gid.delete()
                    print(f"i deleted {guild}")

    async def messageFriends():
        for friend in client.user.friends:
            print("Please input your message:")
            message = input()
            try:
                friend.send(message)
                print(f"Successfully DM-ed {friend.name}#{friend.discriminator}")
            except:
                print(f"Something went wrong while trying to DM {friend.name}#{friend.discriminator}")
    
    