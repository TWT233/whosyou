from khl import Message
from khl.card import CardMessage, Card, Module, Element

from dal.steam import Steam
from .query_pack import QueryPack


async def reg(m: Message, value: str):
    try:
        friend_code = int(value)
    except Exception:
        raise ValueError('value should be an integer')
    return await Steam.create(khl=m.author.id, friend_code=friend_code)


async def fetch(m: Message) -> str:
    dao = await Steam.filter(khl=m.author.id).first()
    return dao and dao.friend_code


async def illu(m: Message, value: int) -> CardMessage:
    if not value:
        return CardMessage(Card(Module.Context(Element.Text('未绑定过 steam ID'))))

    try:
        value = int(value)
    except Exception as e:
        return CardMessage(Card(Module.Context(Element.Text('illegal value'))))

    result = CardMessage(
        Card(
            Module.Section(
                Element.Text(f'TA 的 steam 好友代码: {value}')
            )
        )
    )
    return result


steam_query_pack = QueryPack(reg=reg, fetch=fetch, illu=illu)
