from khl import Message
from khl.card import CardMessage, Card, Module, Element

from dal.platforms import EA, Steam
from .query_pack import QueryPack


async def bind(m: Message, value: str):
    try:
        friend_code = int(value)
    except Exception:
        await m.reply('看起来这不是一个 steam 好友代码，所以将看作 EA 账号进行绑定')
        return await EA.update_or_create(khl=m.author.id, defaults=dict(username=value))
    await m.reply('看起来这可以作为一个 steam 好友代码，所以将看作 steam 好友代码进行绑定\n'
                  f'如果需要绑定 EA 账号，请使用 /bind {value} ea')
    return await Steam.update_or_create(khl=m.author.id, defaults=dict(friend_code=friend_code))


async def fetch(m: Message) -> (int, str):
    steam = await Steam.filter(khl=m.author.id).first()
    ea = await EA.filter(khl=m.author.id).first()
    return steam and steam.friend_code, ea and ea.username


async def illu(m: Message, value: (int, str)) -> CardMessage:
    if not value or not value[0] and not value[1]:
        return CardMessage(Card(Module.Context(Element.Text('未绑定过 steam 好友代码/EA 账号'))))

    result = Card()
    if value[0]:
        result.append(Module.Section(Element.Text(f'TA 的 steam 好友代码: {value[0]}')))
    if value[1]:
        result.append(Module.Section(Element.Text(f'TA 的 EA 账号：{value[1]}')))
    return CardMessage(result)


apex_query_pack = QueryPack(bind=bind, fetch=fetch, illu=illu)
