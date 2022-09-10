from khl import Message, Bot
from khl.command import Command

from dal.binding import Binding
from ._util import fetch_current_bind_pf


@Command.command()
async def who(m: Message, platform: str = None):
    """retrieve"""
    platform = platform or await fetch_current_bind_pf(m)
    if platform is None:
        return await m.reply('platform is required, or bind a platform via /bind')
