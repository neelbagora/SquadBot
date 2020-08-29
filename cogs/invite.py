import discord
from discord.ext import commands
import json

# New - The Cog class must extend the commands.Cog class
class Invite(commands.Cog):
    ctx = discord.Client().guilds[0]
    def __init__(self, bot):
        self.bot = bot
        self.invites = {}
        write_invites()
        # TODO: add invite uses information to a json file

    async def write_invites(self):
        with open("invite.json", "r") as f:
            data = json.load(f)
            print(data)
        with open("invite.json", "w") as f:
            invites = await ctx.invites()
            for invite in invites:
                if str(invite) not in data.keys():
                    data.update({
                        str(invite): invite.uses
                    })
            json.dump(data, f)

    # Define a new command
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("invite.json", "r") as f:
            data = json.load(f)
        
        invites = await ctx.invites()
        for i in invites:
            if i.uses != data[i].uses:
                # TODO: write invite to user.json



    



def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file