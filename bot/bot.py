from khl import Bot

from config import _BOT_TOKEN_
from .cmd import register_cmds_for

bot = Bot(_BOT_TOKEN_)

register_cmds_for(bot)
