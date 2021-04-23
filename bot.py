import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

import giphy_client
from giphy_client.rest import ApiException
import random

load_dotenv()
TOKEN = os.getenv('TOKEN_DISCORD')
GUILD = os.getenv('DISCORD_GUILD')
TOKEN_GOOGLE = os.getenv('TOKEN_GOOGLE')
TOKEN_GIPHY = os.getenv('TOKEN_GIPHY')
ID_SEARCH_ENGINE = os.getenv('ID_SEARCH_ENGINE')

bot = commands.Bot(command_prefix='!')

from google_images_search import GoogleImagesSearch
gis = GoogleImagesSearch(TOKEN_GOOGLE, ID_SEARCH_ENGINE)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep uwu 🔪"))
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is in {len(bot.guilds)} servers:')
    for i in range(len(bot.guilds)):
        print(f'    {i}. ({bot.guilds[i].member_count-1})     {bot.guilds[i]}')

@bot.command(name='image', help='search on google')
async def image(ctx, *args):
    terms = ''
    for n in args:
        terms += ' '+n
    _search_params = {
        'q': terms,
        'num': 1,
        'safe': 'medium',
        'fileType': 'jpg'
    }
    gis.search(search_params=_search_params, path_to_dir='images/', custom_image_name=f'{ctx.author}{terms}', width=500, height=500)
    await ctx.send(file=discord.File(f'images/{ctx.author}{terms}.jpg', filename=f'{ctx.author}{terms}.jpg'))



@bot.command(name='gif', help='search on giphy')
async def gif(ctx, *args):
    terms = ''
    for n in args:
        terms += ' '+n

    giphy_instance = giphy_client.DefaultApi()

    api_response = giphy_instance.gifs_search_get(TOKEN_GIPHY,terms,limit=1)
    await ctx.send(api_response.data[0].embed_url)


@bot.command(name='randomgif', help='search on giphy and returns a random gif')
async def randomgif(ctx, *args):
    terms = ''
    for n in args:
        terms += ' '+n

    giphy_instance = giphy_client.DefaultApi()

    api_response = giphy_instance.gifs_search_get(TOKEN_GIPHY,terms,limit=7)
    giflst = list(api_response.data)
    gif = random.choice(giflst)
    await ctx.send(gif.embed_url)



@bot.command(name='gifblast', help='search on giphy and returns a random number of random gifs')
async def gifblast(ctx, *args):
    terms = ''
    for n in args:
        terms += ' '+n

    giphy_instance = giphy_client.DefaultApi()

    api_response = giphy_instance.gifs_search_get(TOKEN_GIPHY,terms,limit=7)
    giflst = list(api_response.data)
    gifs = random.choices(giflst,k=random.randint(2,len(giflst)))
    for gif in gifs:
        await ctx.send(gif.embed_url)

    
bot.run(TOKEN)