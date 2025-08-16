from pyrogram import Client, filters
from pyrogram.types import Message 

from ..context import with_context
from . import register_handler


@register_handler(filters.command("foo"), group=1, handler_type="on_message")
@with_context
async def example_handler(ctx, client: Client, message: Message):
    await message.reply_text("This is an example about plugins template")
   
 
