from typing import Callable, Coroutine

from khl import Message
from khl.command import Command

import dal.steam


@Command.command()
async def reg(m: Message, value: str, platform: str = None):
    """create"""
    try:
        q = gen_query(m, platform, value)
    except ValueError as e:
        return await m.reply(f'wrong input: {e}')
    try:
        await q
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    ...


async def gen_steam_query(m: Message, value: str) -> Coroutine:
    try:
        friend_code = int(value)
    except Exception:
        raise ValueError('value should be an integer')
    return dal.steam.Steam.create(khl=m.author.id, friend_code=friend_code)


query_generator: dict[str, Callable] = {
    'steam': gen_steam_query
}


def gen_query(m: Message, platform: str, value: str) -> Coroutine:
    if platform not in query_generator:
        raise ValueError(f'unknown platform: {platform}')
    return query_generator[platform](m, value)
