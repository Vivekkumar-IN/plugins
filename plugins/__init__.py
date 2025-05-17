from plugins.modules import HANDLERS, HELP

def setup(
    app: "Yukkibot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/corebot.py
    userbot: "Userbot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    call: "Call",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    config,  # https://github.com/TheTeamVivek/YukkiMusic/tree/master/config
    helpable: dict,  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/__init__.py#L38 HELPABLE
):
    for h, group in HANDLERS:
      app.add_handler(h, group)
    helpable.update(HELP)
    return len(HANDLERS)