from khl import Message
from khl.command import Command

from platforms import get_query_pack
from ._util import fetch_attached_pf


@Command.command()
async def bind(m: Message, value: str, platform: str = None):
    """create"""
    platform = platform or await fetch_attached_pf(m)
    if platform is None:
        return await m.reply('platforms is required, or bind a platforms via /bind')

    try:
        q = await get_query_pack(platform).bind(m, value)
    except ValueError as e:
        return await m.reply(f'wrong input: {e}')
    except Exception as e:
        return await m.reply(f'query failed: {e}')

    return await m.reply(f'done')
