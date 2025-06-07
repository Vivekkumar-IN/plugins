from plugins.modules import handlers

def setup(
    app: "Yukkibot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/corebot.py
    userbot: "Userbot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    call: "Call",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    config,  # https://github.com/TheTeamVivek/YukkiMusic/tree/master/config
    helpable: dict,  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/__init__.py#L38 HELPABLE
):
    handlers, help = handlers()
    for h, group in handlers:
      app.add_handler(h, group)
    helpable.update(help)
    return len(HANDLERS)