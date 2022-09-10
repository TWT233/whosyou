from khl import Message
from khl.command import Command

from ._query_pack import get_query_pack


@Command.command()
async def reg(m: Message, value: str, platform: str = None):
    """create"""
    try:
        q = get_query_pack(platform).reg(m, value)
    except ValueError as e:
        return await m.reply(f'wrong input: {e}')
    try:
        await q
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    ...
