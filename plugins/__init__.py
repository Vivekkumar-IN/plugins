from pymongo import AsyncMongoClient
from plugins.modules import handlers

def setup(ctx: "LoaderContext"):
    """
    ctx: LoaderContext instance provided by the main application.

    For details, see the LoaderContext class in YukkiMusic core modules:
    https://github.com/TheTeamVivek/YukkiMusic/tree/master/YukkiMusic/core/modules.py
    """