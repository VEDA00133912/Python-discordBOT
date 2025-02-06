async def handle_goodbye(message):
        await message.reply(content='Goodbye', mention_author=False)