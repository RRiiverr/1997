import discord
from discord.ext import commands

token = "mfa.MP9KYxu1YIA5tRLdo5UjGyWs260-P5tQXKmZLRuXAwbtW5S8KeNDo28B1f51aOyDsfKfoEBvgwHkgZesI7Uk"

bot = commands.Bot(command_prefix = "123456789")

print('What would you like to stream?')
status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/ratirl'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)  