from khl import Bot

from .attach import attach
from .bind import bind
from .detach import detach
from .who import who


def register_cmds_for(bot: Bot):
    bot.command.add(attach)
    bot.command.add(detach)
    bot.command.add(bind)
    bot.command.add(who)
