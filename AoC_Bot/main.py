import discord
import requests
import json
import os

from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

# Load environment
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
discord_channel = os.getenv('DISCORD_CHANNEL')
aoc_token = os.getenv('AOC_TOKEN')

star_0 = '✰'
star_1 = '✪'
star_2 = '★'



def get_leaderboard(year):
    urlString = f'https://adventofcode.com/{year}/leaderboard/private/view/1550722.json'
    response = requests.get(urlString, cookies={'session': aoc_token})

    return response.text


def test_json():
    with open("data.json") as f:
        return f.read()


def init_stars():
    arr = []
    arr = [star_0 for i in range(25)]

    return arr
    

def leaderboard(year):
    # data = json.loads(test_json())
    data = json.loads(get_leaderboard(year))
    embed = discord.Embed(title=f"AoC Leaderboard {year}")
    
    for member in data['members']:
        stars_arr = init_stars()    
        current_member = data['members'][member]
        user = current_member['name']
        score = current_member['local_score']
        total_stars = current_member['stars']
        
        if current_member['completion_day_level']: 
            for completed_day in current_member['completion_day_level']:
                if len(current_member['completion_day_level'][completed_day]) > 1:
                    stars_arr[int(completed_day)-1] = star_2
                else:
                    stars_arr[int(completed_day)-1] = star_1
        
        stars_list = ' '.join(stars_arr)
        embed.add_field(name=f'{user}', value=f"Score:{score} Total Stars: {total_stars} \n {stars_list}", inline=False)
    
    return embed


def discord_bot(bot):    

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')


    @bot.command()
    async def aoc(ctx, arg=None):        
        try:
            if type(arg) == str:            
                year = int(arg)
                if int(arg) < 2015:
                    raise ValueError
            else:
                year = datetime.now().year
            msg = leaderboard(year)
            await ctx.send(embed=msg)
        
        except ValueError:
            await ctx.send('ValueError!!')
        

    bot.run(discord_token)

def main():
    bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
    discord_bot(bot)

if __name__ == '__main__':
    main()