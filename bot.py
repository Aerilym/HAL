import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN_DISCORD')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    for guild in client.guilds:

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(TOKEN)