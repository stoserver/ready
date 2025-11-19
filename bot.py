import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 연결됨!')
    # 방해금지 상태로 설정
    await bot.change_presence(status=discord.Status.dnd)

bot.run ("MTQ0MDY0NjY2MzM3ODMwNTE0Nw.GxPiUh.bzJ5Os0aDgwRnuYVGLTMPuxyNYHRfxbMAlMy2I")  # 여기에 실제 토큰 넣기
