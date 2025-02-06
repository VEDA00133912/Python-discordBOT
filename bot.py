import discord
from discord import app_commands
import os
from color import Color
import config
import loader  
from function.autoreply import handle_reply 

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = config.DISCORD_TOKEN

@client.event
async def on_ready():
    try:
        token_preview = token[:8] 
        Color.print_green(f'[LOGIN] {client.user} is online! ({token_preview}...)')  

        await client.change_presence(activity=discord.Game('d.py test'))  
        Color.print_green(f'[SUCCESS] Activity setup complete!')

        tree = app_commands.CommandTree(client)
        await loader.load_commands(tree)
        await tree.sync()
        Color.print_green(f'[SUCCESS] Command registration complete!')
    except Exception as e:
        Color.print_red(f'[ERROR] An error occurred during setup: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await handle_reply(message)  

@client.event
async def on_error(event, *args, **kwargs):
    Color.print_red(f'[ERROR] An error occurred in the event handler: {event}, Args: {args}, Kwargs: {kwargs}')

try:
    client.run(token)
except Exception as e:
    Color.print_red(f'[ERROR] Failed to run the bot: {e}')