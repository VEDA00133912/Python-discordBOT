import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name='ephemeral', description='ephemeralメッセージを返します')
    async def ephemeral(interaction: discord.Interaction):
            await interaction.response.send_message('ephemeral command', ephemeral=True)