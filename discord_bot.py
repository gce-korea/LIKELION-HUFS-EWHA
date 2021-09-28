import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def 시작(ctx):
    await ctx.send("안녕!")

@bot.command()
async def 배고파(ctx):
    await ctx.send("치킨 먹자")

@bot.command()
async def 랜덤(ctx):
    number = random.randrange(1,101)
    await ctx.send(f"뽑힌 숫자: {number}")
    
@bot.event
async def on_message(message):
    if message.author.bot == False:
        await message.channel.send("누군가가 메시지를 입력했습니다")

@bot.event
async def on_reaction_add(reaction, user):
    await user.send("네가... 이모티콘을 눌렀니...?")
    
bot.run("ODkxOTk4MjgwNzUyNDYzODk1.YVGgIg.t-TH9pjDDTd8jV1p7dAwKfW3uhk")
