import discord
from discord.ext import commands
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path
dotenv_path = join(dirname(__file__), '.env') 

# Load file from the path.
load_dotenv(dotenv_path)

com = discord.ext.commands
secret_token = os.getenv("TOKEN")
description = '''I am Squad Bot.'''
bot = commands.Bot(command_prefix='?', description=description)
cogs=['cogs.basic','cogs.admin','cogs.valorant']

def is_me(m):
    return m.author == bot.user

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for c in cogs:
        #try:
            bot.load_extension(c)
            print('Loaded {}'.format(c))
        #except Exception:
        #    print('Failed to load {}'.format(c))
    return

@bot.event
async def on_message(msg):
    if not is_me(msg):    
        if (msg.content.lower() == 'bet'):
            await msg.channel.send('bet')

        if (msg.content.lower() == 'word'):
            await msg.channel.send('word')
        
        if msg.content.lower() == 'f':
            await msg.channel.send("f")

    await bot.process_commands(msg)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def unload(ctx, cog:str):
    try:
        bot.unload_extension(cog)
        await ctx.send('{} unloaded!'.format(cog))
        
    except Exception:
        await ctx.send('{} failed to unload'.format(cog))

@bot.command()
@commands.has_permissions(manage_guild=True)
async def reload(ctx, cog:str):
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.send('{} reloaded!'.format(cog))

    except com.ExtensionAlreadyLoaded:
        await ctx.send('{} already loaded!'.format(cog))

    except com.ExtensionNotFound:
        await ctx.send('{} not found!'.format(cog))

    except com.ExtensionFailed:
        await ctx.send('{} failed to load!'.format(cog))

@bot.command()
@commands.has_permissions(manage_guild=True)
async def load(ctx, cog:str):
    try:
        bot.load_extension(cog)
        await ctx.send('{} loaded!'.format(cog))

    except com.ExtensionAlreadyLoaded:
        await ctx.send('{} already loaded!'.format(cog))

    except com.ExtensionNotFound:
        await ctx.send('{} not found!'.format(cog))

    except com.ExtensionFailed:
        await ctx.send('{} failed to load!'.format(cog))
    
    except Exception:
        await ctx.send('{} failed to load!'.format(cog))
       



bot.run(secret_token)