import discord
from discord import app_commands

BOT_NAME = 'DISCORD-BOT'
BOT_VERSION = '1.0.0'
BOT_DESCRIPTION = 'Discord.pyのBOTです'
BOT_SUPPORT_SERVER = 'https://discord.gg/discord'
COMMANDS = '/ping, /about'
AUTOREPLY = 'hello, goodbye'

async def setup(tree: app_commands.CommandTree):
    @tree.command(name='about', description='BOTの情報を表示します')
    async def about(interaction: discord.Interaction):
            embed = discord.Embed(
                title=f'{BOT_NAME} の情報',
                description=BOT_DESCRIPTION,
                color=discord.Color.blue()
            )

            embed.add_field(name='バージョン', value=BOT_VERSION, inline=False)
            embed.add_field(name='サポートサーバー', value=BOT_SUPPORT_SERVER, inline=False)
            embed.add_field(name='コマンド', value=COMMANDS, inline=False)
            embed.add_field(name='自動返信', value=AUTOREPLY, inline=False)

            await interaction.response.send_message(embed=embed)
