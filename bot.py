import discord
from discord.ext import commands
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime
import time
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
    guap = 0
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
            await msg.channel.send("Here is ten guap $10.")
        
        if msg.content.lower() == 'guap':
            with open("guap.json", "r") as f:
                data = json.load(f)
                if str(msg.author.id) in data.keys():
                    guap = data[str(msg.author.id)]['guap']
                    await msg.channel.send("{}, you got {} guap!".format(msg.author.name, guap))

    await bot.process_commands(msg)

@bot.event
async def on_voice_state_update(member, before, after):
    if member != bot.user:
        print(member)
        print(before)
        print(after)

        if (after.channel != None and after.channel.name == 'Guap Generator'):
            with open("guap.json", "r") as f:
                data = json.load(f)
                print()
                print(data)
            with open("guap.json", "w") as f:
                if (str(member.id) in data.keys() and 'joined' in data[str(member.id)].keys()):
                    data[str(member.id)]['joined'] = time.time()
                else:
                    data.update({
                        str(member.id): {
                            'joined': time.time(),
                            'guap': 0
                        }
                    })
                print()
                print(data)
                json.dump(data, f)
        elif (before.channel != None and before.channel.name == 'Guap Generator'):
            with open("guap.json", "r") as f:
                data = json.load(f)
                print()
                print(data)
                guap = 0
                joined_time = 0

                if (str(member.id) in data.keys()):
                    joined_time = data[str(member.id)]['joined']
                    guap = data[str(member.id)]['guap']
                diff = int(time.time() - joined_time) / 10

            with open("guap.json", "w") as f:                   
                guap += diff * 2
                if (str(member.id) in data.keys()):
                    data[str(member.id)]['guap'] = guap
                else:
                    data.update({
                        str(member.id): {
                            'joined': joined_time,
                            'guap': guap
                        }
                    })
                print(data)
                json.dump(data, f)

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