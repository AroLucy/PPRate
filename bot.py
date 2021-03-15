import discord
from discord.ext import commands
from pathlib import Path
from random import choice
import json

def load_config():
    try:
        with open(str(Path(__file__).parent.absolute()) + '/config.json', 'r') as json_file:
            config = json.load(json_file)
        return config
    except FileNotFoundError:
        print("Confing file not found!")
        print("Exiting...")
        exit()
        
def load_token():
    try:
        with open(str(Path(__file__).parent.absolute()) + '/token.json', 'r') as json_file:
            config = json.load(json_file)
        return config
    except FileNotFoundError:
        print("Confing file not found!")
        print("Exiting...")
        exit()
    
config = load_config()
tok = load_token()

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
    activity = discord.Game(name="with my measuring tape untill someone uses `My pp`", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('The measuring tape is out to measure everyones PPs!')

@bot.command(aliases=['PP', 'Pp', 'pP'])
async def pp(ctx):
    embed=discord.Embed(title=(choice(config['responses'])),color =discord.Colour.random())
    await ctx.reply(embed=embed)

@commands.is_owner()
@bot.command()
async def reload(ctx):
    config = load_config()
    await ctx.reply('Config reloaded.')

bot.run(tok['token'])

