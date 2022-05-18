token='OTczMTQwMjU3OTk2NDMxMzgw.G3pYGO.XmMNJHO0AJjIS5f7liUwO83kGu6I_dwQ2Gl478'
import nest_asyncio 
nest_asyncio.apply()
import discord
from discord.ext import commands
from discord import Embed

intents = discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='m', case_insensitive=True)

@bot.event 
async def on_ready():
    print (bot.user.name, ' đã kết nối đến Discord.')
    await bot.change_presence(activity=discord.Game('Đặt tên kênh là **🥶moderator🤢 ** để bot nhắn vào kênh đó.'))
    
@bot.event
async def on_message(message):
    channel = discord.utils.get(message.guild.channels, name='🥶moderator🤢')
    embed = discord.Embed(title = "Message sent", description = message.author, color = message.author.color)
    embed.add_field(name = "The message is", value = message.content)
    embed.add_field(name = "The channel is", value = message.channel)
    embed.set_footer(text = "Bot viết bởi Vinh tm | God#7345")
    await channel.send(embed = embed)

bot.run(token)
