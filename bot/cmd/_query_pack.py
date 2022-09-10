from dataclasses import dataclass
from typing import Callable, Coroutine

from khl import Message

from dal.steam import Steam


class QueryPack(dataclass):
    reg: Callable
    fetch: Callable


async def steam_reg(m: Message, value: str) -> Coroutine:
    try:
        friend_code = int(value)
    except Exception:
        raise ValueError('value should be an integer')
    return Steam.create(khl=m.author.id, friend_code=friend_code)


steam_query_pack = QueryPack(reg=steam_reg)
query_generator: dict[str, QueryPack] = {
    'steam': steam_query_pack
}


def get_query_pack(platform: str) -> QueryPack:
    if platform not in query_generator:
        raise ValueError(f'unknown platform: {platform}')
    return query_generator[platform]