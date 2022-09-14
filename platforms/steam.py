from khl import Message
from khl.card import CardMessage, Card, Module, Element

from dal.platforms import Steam
from .query_pack import QueryPack


async def bind(m: Message, value: str):
    try:
        friend_code = int(value)
    except Exception:
        raise ValueError('value should be an integer')
    return await Steam.update_or_create(khl=m.author.id, defaults=dict(friend_code=friend_code))


async def fetch(m: Message) -> int:
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


steam_query_pack = QueryPack(bind=bind, fetch=fetch, illu=illu)
