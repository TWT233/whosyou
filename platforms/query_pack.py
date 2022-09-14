from dataclasses import dataclass
from typing import Callable, Awaitable, Any

from khl import Message
from khl.card import CardMessage


async def default_illustrator(_: Message, value) -> str:
    if not value:
        return 'not registered'
    return f'you are {value}'


@dataclass
class QueryPack:
    bind: Callable[[Message, ...], Awaitable[Any]]
    fetch: Callable[[Message], Awaitable[Any]]

    """illu stands for illustrate, generates a user-friendly message to show value"""
    illu: Callable[[Message, ...], Awaitable[str | CardMessage]] = default_illustrator
