from pyrogram import Client, filters
from pyrogram.types import Message 
from pyrogram.handlers import MessageHandler

async def example_handler(client: Client, message: Message):
    await message.reply_text("This is an example about plugins template")
    

__handlers__ = [
  (MessageHandler(example_handler, filters.command("example") & filters.private), 0)
]
__mod__ = "Example" # Button  name
__help__ = """
This is an example of how to use plugins template
""" # Button help