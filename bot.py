import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="@")  #指令前綴字

@bot.event
async def on_ready():
    print("<<< Bot is working >>>")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1006448929472249856) # 自己的 channel 不是字串喔
    await channel.send(f'{member} welcome!')
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1006467336716427284) # 自己的 channel 不是字串喔
    await channel.send(f'{member} leave!')
    
#這裡放機器人Token    
bot.run("MTAwNjQzOTM3MTMzMjkzMTY0NA.GpcKEX.TiwlSpcw371C0Giia2y5AM3z3FXegVhW4G72_c")  