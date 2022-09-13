from khl import Message
from khl.command import Command

from ._query_pack import get_query_pack
from ._util import fetch_current_bind_pf


@Command.command()
async def who(m: Message, platform: str = None):
    """retrieve"""
    platform = platform or await fetch_current_bind_pf(m)
    if platform is None:
        return await m.reply('platform is required, or bind a platform via /bind')

    qp = get_query_pack(platform)
    value = await qp.fetch(m)
    if not value:
        return await m.reply('not registered')
    return await m.reply(f'you are {value}')
