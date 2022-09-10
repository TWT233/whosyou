from khl import Bot

from .bind import bind
from .reg import reg
from .unbind import unbind
from .who import who


def register_cmds_for(bot: Bot):
    bot.command.add(bind)
    bot.command.add(unbind)
    bot.command.add(reg)
    bot.command.add(who)
