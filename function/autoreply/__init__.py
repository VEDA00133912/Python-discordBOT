from .hello import handle_hello
from .goodbye import handle_goodbye

REPLIES = {
    'hello': handle_hello,
    'goodbye': handle_goodbye,
}

async def handle_reply(message):
    reply_function = REPLIES.get(message.content.lower())
    if reply_function:
        await reply_function(message)
