from pymongo import AsyncMongoClient
from plugins.modules import handlers

def setup(ctx: "LoaderContext"):
    """
    ctx: LoaderContext instance provided by the main application.

    For details, see the LoaderContext class in YukkiMusic core modules:
    https://github.com/TheTeamVivek/YukkiMusic/tree/master/YukkiMusic/core/modules.py
    """

    handlers, help = handlers()
    for h, group in handlers:
      app.add_handler(h, group)
    helpable.update(help)
    db = mongo_client.Yukki # Do what ever that you want to do with "db" a Async MongoClient 
    return len(HANDLERS)