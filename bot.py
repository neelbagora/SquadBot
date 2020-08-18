import discord
from discord.ext import commands
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

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
            guap = 0
            await msg.channel.send("Here is ten guap $10.")
        
        if msg.content.lower() == 'guap':
            with open("guap.json", "r") as f:
                data = json.load(f)
                if str(msg.author.id) in data.keys():
                    guap = data[str(msg.author.id)]['guap']
                    await msg.channel.send("You got {} guap!".format(guap))

    await bot.process_commands(msg)

@bot.event
async def on_voice_state_update(member, before, after):
    if member != bot.user:
        if (before != None and before.name == 'Guap Generator'):
            #TODO: get current time of event
            print(member)

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