from discord.ext import commands, tasks
import gmail
import time
import asyncio
# New - The Cog class must extend the commands.Cog class
class Valorant(commands.Cog):
    
   def __init__(self, bot):
      self.bot = bot
      self.kills.start()
   
   def cog_unload(self):
      self.kills.cancel()
   
   @tasks.loop(seconds = 2.0)
   async def kills(self):
      channel = self.bot.get_channel(734982761886122095)
      #await channel.send(self.index)
      if gmail.readEmail()['resultSizeEstimate'] > 0:
         await channel.send('Bogus has big PP!')
         print('bogus pp')
         gmail.deleteEmail()


def setup(bot):
    bot.add_cog(Valorant(bot))
    # Adds the Email commands to the bot
    # Note: The "setup" function has to be there in every cog file