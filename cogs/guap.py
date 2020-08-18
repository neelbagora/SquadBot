import discord
from discord.ext import commands
import json

# New - The Cog class must extend the commands.Cog class
class Guap(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.Cog.listener()
    async def on_message(self, msg):
        guap = 0
        if self.bot.user !=  msg.author:         
            if msg.content.lower() == 'gimme cash':
                with open("guap.json", "r") as f:
                    data = json.load(f)
                    if str(msg.author.id) in data.keys():
                        guap = data[str(msg.author.id)]['guap']
                        guap += 10
                    print(data)
                with open("guap.json", "w") as f:
                    if guap == 0:
                        data.update({
                            str(msg.author.id):{
                                'guap': 10}
                        })
                    else:
                        data.update({
                            str(msg.author.id):{
                                'guap': guap}
                        })
                    json.dump(data, f)
                await msg.channel.send("Here is ten guap $10.")
            
            if msg.content.lower() == 'guap':
                with open("guap.json", "r") as f:
                    data = json.load(f)
                    if str(msg.author.id) in data.keys():
                        guap = data[str(msg.author.id)]['guap']
                        await msg.channel.send("{}, you got {} guap!".format(msg.author.name, guap))

        await self.bot.process_commands(msg)


def setup(bot):
    bot.add_cog(Guap(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file