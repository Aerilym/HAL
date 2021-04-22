import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN_DISCORD')
GUILD = os.getenv('DISCORD_GUILD')
TOKEN_GOOGLE = os.getenv('TOKEN_GOOGLE')
ID_SEARCH_ENGINE = os.getenv('ID_SEARCH_ENGINE')

bot = commands.Bot(command_prefix='!')

from google_images_search import GoogleImagesSearch
gis = GoogleImagesSearch(TOKEN_GOOGLE, ID_SEARCH_ENGINE)

@bot.command(name='image', help='search on google')
async def roll(ctx, *args):
    terms = ''
    for n in args:
        terms += ' '+n  
    print(terms)
    # define search params:
    _search_params = {
        'q': terms,
        'num': 1,
        'safe': 'medium',
    }
    # this will search, download and resize:
    gis.search(search_params=_search_params, path_to_dir='images/', custom_image_name=f'{ctx.author}{terms}', width=500, height=500)
    
    await ctx.send(file=discord.File(f'images/{ctx.author}{terms}.jpg', filename=f'{ctx.author}{terms}.jpg'))

    
bot.run(TOKEN)