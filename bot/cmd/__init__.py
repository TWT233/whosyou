from khl import Bot, EventTypes

from .attach import attach
from .bind import bind, regex_bind
from .detach import detach
from .help import man_tag, on_man_clicked, man_cmd
from .who import who, regex_who


def register_cmds_for(bot: Bot):
    bot.command.add(attach)

    bot.command.add(detach)

    bot.command.add(bind)
    bot.command.add(regex_bind)

    bot.command.add(who)
    bot.command.add(regex_who)

    bot.command.add(man_cmd)
    bot.command.add(man_tag(bot))
    bot.on_event(EventTypes.MESSAGE_BTN_CLICK)(on_man_clicked)
