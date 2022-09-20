import functools
from typing import Optional, List

from khl import Message, PublicChannel
from khl.card import CardMessage, Card, Module
from khl.card.interface import _Module

from dal.attach import Attachment


async def fetch_attached_pf(m: Message) -> Optional[str]:
    if not isinstance(m.ctx.channel, PublicChannel):
        return None
    guild_id = m.ctx.guild.id
    channel_id = m.ctx.channel.id

    items = await Attachment.filter(place=Attachment.make_place_for_khl(guild_id, channel_id))
    return None if len(items) == 0 else items[0].platform


def public_msg_only(func):
    @functools.wraps(func)
    async def checks(m: Message, *args, **kwargs):
        if not isinstance(m.ctx.channel, PublicChannel):
            return await m.reply('exclusive for public channel')
        return await func(m, *args, **kwargs)

    return checks


def help_helper_context() -> List[_Module]:
    return [Module.Divider(), Module.Context('想要其他命令用法？@我或输入 "/help" 即可')]


def done_card() -> CardMessage:
    return CardMessage(
        Card(Module.Section('成功！'), *help_helper_context())
    )


def missing_pf_card() -> CardMessage:
    return CardMessage(
        Card(Module.Section('不知道是在找哪个平台/游戏的ID呢'), *help_helper_context())
    )
