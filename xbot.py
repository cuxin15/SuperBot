import os
import discord
from discord.ext import commands
from urllib.request import urlretrieve
import random
import wikipedia
import io
import aiohttp

# setting for chat bot
TOKEN = 'NjM4MzYyNDQ2Mjk3MzAxMDEy.Xbj_uA.WIfvdrXmBGvPeH_mg04BNm-0OXU'
GUILD_ID = '638360375057973268'

# path to chat bot can download and save images here
IMAGES_FOLDER = 'discord_image'

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.id == GUILD_ID:
            break

    print(
            f'{bot.user} da duoc ket noi thanh cong toi guild:\n'
            f'{guild.name} (id: {guild.id})'
        )

    members = '\n - '.join([member.name for member in guild.members])
    print('Thành viên có trong guild:\n -', members)

# xử lý sự kiện một member mới tham gia guild
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Chào {member.name}, chào mừng người anh em đến với Xóm trọ vui vẻ :)'
        )



@bot.command(name='search', help='Search something')
async def search(ctx, *args):
    wikipedia.set_lang('vi')
    query = ' '.join(args)
    response = wikipedia.summary(query, sentences=2)
    await ctx.send(response)
    

    # tải hình ảnh từ wikipedia
    page = wikipedia.page(query)
    my_url = page.images[4]
    image_name = my_url.split('/')[-1]
    path_to_image = IMAGES_FOLDER+'/'+image_name
    urlretrieve(my_url,path_to_image) # download image

    file = discord.File(path_to_image, filename="image.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     reply = [
#         f'Chào người anh em, đây là một tin nhắn từ {bot.user.name}, em đang được Anh hàng xóm phát triển :)',
#         'Hừm, đây là một tin nhắn, đại loại thế',
#         'Yowh, chào người anh em thiện lành',
#         'Đây là một tin nhắn trong giai đoạn alpha bot',
#         'Tin nhắn này đang được trong quá trình phát triển'
#     ]

#     response = random.choice(reply)
#     await message.channel.send(response)

bot.run(TOKEN)
