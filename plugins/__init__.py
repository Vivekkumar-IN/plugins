from pyrogram.handlers import (
    MessageHandler,
)
from .modules  import handlers

_handler_type_map = {
    "on_message": MessageHandler
}

def setup(ctx: "LoaderContext"):
    """
    ctx: LoaderContext instance provided by the main application.

    For details, see the LoaderContext class in YukkiMusic core modules:
    https://github.com/TheTeamVivek/YukkiMusic/tree/master/YukkiMusic/core/modules.py
    """
    for handler_def in handlers:
        handler_cls = _handler_type_map.get(handler_def["type"])
        if not handler_cls:
            raise ValueError(f"Unsupported handler type: {handler_def['type']}")
        
        func = handler_def["function"](ctx)  # bind context
        ctx.app.add_handler( # Fix it
            handler_cls(func, handler_def["filters"]),
            group=handler_def["group"]
        )
