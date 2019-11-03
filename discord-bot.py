import os
from discord.ext import commands
import random
import wikipedia
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')

class XBot(commands.Bot):

    def __init__(self, *, loop=None, **options):
        super().__init__(loop=None,**options)
        
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD_ID = os.getenv('DISCORD_GUILD')

    async def on_ready(self):
        for guild in self.guilds:
            if guild.id == GUILD_ID:
                break

        print(
            f'{self.user} da duoc ket noi thanh cong toi guild:\n'
            f'{guild.name} (id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print('Thành viên có trong guild:\n -',members)

    # xử lý sự kiện một member mới tham gia guild
    async def on_member_join(self,member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Chào {member.name}, chào mừng người anh em đến với Xóm trọ vui vẻ :)'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        reply = [
            f'Chào người anh em, đây là một tin nhắn từ {self.user}, em đang được Anh hàng xóm phát triển :)',
            'Hừm, đây là một tin nhắn, đại loại thế',
            'Yowh, chào người anh em thiện lành',
            'Đây là một tin nhắn trong giai đoạn alpha bot',
            'Tin nhắn này đang được trong quá trình phát triển'
        ]

        response = random.choice(reply)
        await message.channel.send(response)

    @Xbot.command(name='tra cứu', help='Em sẽ trả về thông tin cần tra cứu')
    async def searchWikipedia(self, ctx, *args):
        search = ' '.join(args)
        print(wikipedia.search(search))


c = XBot(command_prefix='!')
c.run(c.TOKEN)
