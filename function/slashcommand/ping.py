import discord
from discord import app_commands
import time

async def setup(tree: app_commands.CommandTree):
    @tree.command(name='ping', description='ping値測定結果を表示します')
    async def ping(interaction: discord.Interaction):
            start_time = time.monotonic()
            await interaction.response.send_message('🏓 Pinging...')
            elapsed_time = time.monotonic() - start_time
            
            await interaction.edit_original_response(content=f'🏓 Pong! Response time: {elapsed_time * 1000:.2f} ms')