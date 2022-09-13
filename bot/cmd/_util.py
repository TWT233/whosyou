import functools
from typing import Optional

from khl import Message, PublicChannel

from dal.binding import Binding


async def fetch_current_bind_pf(m: Message) -> Optional[str]:
    if not isinstance(m.ctx.channel, PublicChannel):
        return None
    guild_id = m.ctx.guild.id
    channel_id = m.ctx.channel.id

    items = await Binding.filter(place=Binding.make_place_for_khl(guild_id, channel_id))
    return None if len(items) == 0 else items[0]


def public_msg_only(func):
    @functools.wraps(func)
    async def checks(m: Message, *args, **kwargs):
        if not isinstance(m.ctx.channel, PublicChannel):
            return await m.reply('exclusive for public channel')
        return await func(m, *args, **kwargs)

    return checks