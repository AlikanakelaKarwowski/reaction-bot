#!/usr/bin/python3
from clientkey import key
import discord
import sys
import time
import logging
from discord.utils import get

time.localtime()
intents = discord.Intents.all()
logging.basicConfig(filename='/reaction-bot/log1.log', level=logging.INFO)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S',time.localtime())
    logging.info(f"{cur_time} | Bot sucessfully logged in.")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 816697911781621761 or message_id == 816703783077019649:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
#        student = discord.utils.get(guild.roles, "Student")
        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S',time.localtime())
            member = payload.member
            if member is not None:
                logging.info(f"{cur_time} | {member}: was assigned {role.name}")
                await member.add_roles(role)
 #               await member.add_roles(student)
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 816697911781621761 or message_id == 816703783077019649:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S',time.localtime())
            member = get(guild.members, id=payload.user_id)
            if member is not None:
                logging.info(f"{cur_time} | {member}: was unassigned {role.name}")
                await member.remove_roles(role)
            else:
                cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
                logging.info(f"{cur_time} | Member not found")
        else:
            cur_time = time.strftime('%Y-%m-%d %A %H:%M:%S', time.localtime())
            logging.info(f"{cur_time} | {role.name} Role not found")


client.run(key)
