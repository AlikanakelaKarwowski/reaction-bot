import discord
import sys
import time
import logging
from discord.utils import get
time.localtime()
intents = discord.Intents.all()
logging.basicConfig(filename='log1.log', level=logging.INFO)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S',time.localtime())
    logging.info(f"{cur_time} : Bot is logged in.")

@client.event 
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 769645416672919572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'OTP':
            role = discord.utils.get(guild.roles, name='Off Topic Ping')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            logging.info(role.name)
            member = payload.member
            if member is not None:
                await member.add_roles(role)
            else:
                cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
                logging.info(f"{cur_time} : Member not found")
        else:
            cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
            logging.info(f"{cur_time} : {role} Role not found")
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 769645416672919572:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'OTP':
            role = discord.utils.get(guild.roles, name='Off Topic Ping')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            logging.info(role.name)
            member = get(guild.members, id=payload.user_id)
            if member is not None:
                await member.remove_roles(role)
            else:
                cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
                logging.info(f"{cur_time} : Member not found")
        else:
            cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
            logging.info(f"{cur_time} : {role} Role not found")


client.run('NzQ3NTEwOTQ3NTU5NzY4MTk0.X0P70Q.H6I1jBBKis2CGjaVD4NRhgHEph0')
