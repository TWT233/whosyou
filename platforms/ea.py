from khl import Message
from khl.card import CardMessage, Card, Module, Element

from dal.platforms import EA
from .query_pack import QueryPack


async def bind(m: Message, value: str):
    return await EA.update_or_create(khl=m.author.id, defaults=dict(username=value))


async def fetch(m: Message) -> str:
    ea = await EA.filter(khl=m.author.id).first()
    return ea and ea.username


async def illu(m: Message, value: str) -> CardMessage:
    if not value:
        return CardMessage(Card(Module.Context(Element.Text('未绑定过 EA 账号'))))

    result = Card(
        Module.Header('TA 的 EA 账号'),
        Module.Section(Element.Text(f'{value}')),
        Module.Divider(),
        Module.Context('想要其他命令用法？@我 / 输入"/help" 即可'),
    )
    return CardMessage(result)


ea_query_pack = QueryPack(bind=bind, fetch=fetch, illu=illu)
