async def handle_hello(message):
        await message.reply(content='Hello', mention_author=False)