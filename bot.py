import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

async def set_presence(activity_type, name):
    current = bot.activity.name if bot.activity else None
    if current != name:
        if activity_type == "game":
            await bot.change_presence(activity=discord.Game(name=name))
        elif activity_type == "listening":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))

@bot.event
async def on_ready():
    print(f'{bot.user} 연결됨!')

    await bot.change_presence(status=discord.Status.dnd)

    # 듣는 중
    await set_presence("listening", "IRIS OUT")
    await asyncio.sleep(10)

    # 게임으로 표시, 접미사 중복 방지
    await set_presence("game", "서비스 준비")
    await asyncio.sleep(10)

    await set_presence("game", "지닉스 교육 시청")

bot.run("YOUR_BOT_TOKEN")
