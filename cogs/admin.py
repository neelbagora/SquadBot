from discord.ext import commands

# New - The Cog class must extend the commands.Cog class
class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # Define a new command
    @commands.command(
        name='purge',
        description='Purges given number of messages',
        aliases=['delete']
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, messages: int):
        """Purges channel of given number of messages"""
        
        deleted = await ctx.channel.purge(limit=messages)
        await ctx.send('Deleted {} message(s)'.format(len(deleted)))


def setup(bot):
    bot.add_cog(Admin(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file