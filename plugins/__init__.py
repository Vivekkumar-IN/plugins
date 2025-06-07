from pymongo import AsyncMongoClient
from plugins.modules import handlers

def setup(
    app: "Yukkibot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/corebot.py
    userbot: "Userbot",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    call: "Call",  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/call.py
    mongo_client : AsyncMongoClient, # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/core/mongo.py
    config,  # https://github.com/TheTeamVivek/YukkiMusic/tree/master/config
    helpable: dict,  # https://github.com/TheTeamVivek/YukkiMusic/blob/master/YukkiMusic/__init__.py#L38 HELPABLE
):
    handlers, help = handlers()
    for h, group in handlers:
      app.add_handler(h, group)
    helpable.update(help)
    db = mongo_client.Yukki # Do what ever that you want to do with "db" a Async MongoClient 
    return len(HANDLERS)