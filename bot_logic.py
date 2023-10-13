import discord
from discord.ext import commands
import random
import requests 
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof'
    res = requests.get(url)
    data = res.json()https://www.iloveimg.com/download/
    return data['image']


@bot.command('fox')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url) 

bot.run("MTE1NDgwNjk4Mjk3MzM0NTg4Mg.GVF6ol.t02Q198OtLFewBURxm4dBOAUTyvDOPxxvJG0VM")
