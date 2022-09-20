from khl import Message
from khl.command import Command

from platforms import get_query_pack
from ._util import fetch_attached_pf, missing_pf_card


@Command.command()
async def who(m: Message, platform: str = None):
    """retrieve"""
    platform = platform or await fetch_attached_pf(m)
    if platform is None:
        return await m.reply(missing_pf_card())

    try:
        qp = get_query_pack(platform)
    except ValueError:
        return
    return await m.reply(await qp.illu(m, await qp.fetch(m)))


@Command.command(regex=r'^(\w+)id|ID$')
async def regex_who(m: Message, platform: str):
    return await who.handler(m, platform)
