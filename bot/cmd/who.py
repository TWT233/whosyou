from khl import Message
from khl.command import Command

from platforms import get_query_pack
from ._util import fetch_current_bind_pf


@Command.command()
async def who(m: Message, platform: str = None):
    """retrieve"""
    platform = platform or await fetch_current_bind_pf(m)
    if platform is None:
        return await m.reply('platforms is required, or bind a platforms via /bind')

    qp = get_query_pack(platform)
    return await m.reply(await qp.illu(m, await qp.fetch(m)))
