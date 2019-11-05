import discord
from discord.ext import commands
from urllib.request import urlretrieve
from os import listdir
from os.path import isfile, join
from utility_functions import *

import os
import random
import wikipedia
import io
import aiohttp
import requests
import json
import unidecode

# SETTING==================================================
TOKEN = 'NjM4MzYyNDQ2Mjk3MzAxMDEy.XcBdKA.Unb5wU38zMk0-PPSlvMGLsADr3A'
GUILD_ID = '638360375057973268'
# token for OpenWeather
OPEN_WEATHER = '0092e33dc81d0caadd56e552dacd5717'
# path to chat bot can download and save images here
IMAGES_FOLDER = 'discord_image'
# dont delete this line
bot = commands.Bot(command_prefix='$')


# BODY=============================================
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.id == GUILD_ID:
            break

    print(f'{bot.user} da duoc ket noi thanh cong toi guild:\n'
            f'{guild.name} (id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print('Thành viên có trong guild:\n -', members)

# xử lý sự kiện một member mới tham gia guild
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Chào {member.name}, chào mừng người anh em đến với Xóm trọ vui vẻ :)'
        )

@bot.command(name='search', help='Search something on wikipedia and attach an images')
async def search(ctx, *args):
    wikipedia.set_lang('vi')
    query = ' '.join(args)
    response = wikipedia.summary(query, sentences=2)
    await ctx.send(response)
    
    # tải hình ảnh từ wikipedia
    # lấy ra một list các url ảnh phù hợp, sau đó chọn ngẫu nhiên một trong số chúng để đính kèm
    # ban đầu sẽ check xem thư mục chứa image có chứa ảnh có query hay không
    # nếu có dùng cái đó để tải lên
    # nếu không thì tải ảnh từ wiki xuống và tải lên#
    
    # check in folder and get image to upload
    onlyfiles = [f for f in listdir(IMAGES_FOLDER) if isfile(join(IMAGES_FOLDER, f))]

    list_image_paths = filter(inQuery, onlyfiles, query)
    print(list_image_paths)
    if list_image_paths != []:
        print('Select in local')
        path_to_image = random.choice(list_image_paths)
        file = discord.File(path_to_image, filename="image.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

    # get url from page
    else:
        page = wikipedia.page(query)
        list_image_urls = filter(isUrlImageJPG, page.images)
        # list_image_urls.extend(filter(inQueryAndPNG, page.images, query))
        print(list_image_urls)
        my_url = random.choice(list_image_urls)

        image_name = my_url.split('/')[-1]
        path_to_image = IMAGES_FOLDER+'/'+query+'-'+image_name # query to mark image
        urlretrieve(my_url,path_to_image) # download image

        file = discord.File(path_to_image, filename="image.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

@bot.command(name='weather', help='Show weather information at a location')
async def weather(ctx, *args):
    # args = ('Đà','Nẵng') => danang
    args = map(toLowcase,args)
    print(args)
    location = ' '.join(args)
    print('location:',location)
    with open('city.json','r') as f:
        data = json.load(f)
    for i in data:
        if location in i['name'].lower():
            print('id:',i['id'])
            params = {'id':i['id'], 'appid':OPEN_WEATHER}
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?', params)
            json_string = json.loads(r.text)
            print(json_string)
            await ctx.send(json_string)
            break

bot.run(TOKEN)
