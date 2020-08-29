import discord
from discord.ext import commands
from datetime import datetime as d

# New - The Cog class must extend the commands.Cog class
class Invite(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # Define a new command
    @commands.Cog.listener()
    async def on_member_join(self, member):
        



def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file