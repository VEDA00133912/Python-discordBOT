import discord
from discord import app_commands 
import config
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 起動イベント, コマンドの同期
@client.event
async def on_ready():
    print(f'{client.user} is online!') 
    await client.change_presence(activity=discord.Game('d.py test'))  
    await tree.sync()

# メッセージイベント
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello': 
        await message.reply(content='Hello', mention_author=False)  

# スラッシュコマンド
@tree.command(name='ping', description='Ping!') 
async def test(interaction: discord.Interaction): 
  await interaction.response.send_message('🏓Pong!')

client.run(config.DISCORD_TOKEN)