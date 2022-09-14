from khl import Message
from khl.card import CardMessage, Card, Module, Element

from dal.platforms import EA
from .query_pack import QueryPack


async def bind(m: Message, value: str):
    return await EA.create(khl=m.author.id, username=value)


async def fetch(m: Message) -> str:
    ea = await EA.filter(khl=m.author.id).first()
    return ea and ea.username


async def illu(m: Message, value: str) -> CardMessage:
    if not value:
        return CardMessage(Card(Module.Context(Element.Text('未绑定过 EA 账号'))))

    result = Card(Module.Section(Element.Text(f'TA 的 EA 账号：{value}')))
    return CardMessage(result)


ea_query_pack = QueryPack(bind=bind, fetch=fetch, illu=illu)
