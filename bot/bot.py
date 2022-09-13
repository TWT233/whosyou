from khl import Bot

from config import config
from .cmd import register_cmds_for

bot = Bot(config().bot_token)

register_cmds_for(bot)
