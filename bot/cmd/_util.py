from typing import Optional

from khl import Message

from dal.binding import Binding


async def fetch_current_bind_pf(m: Message) -> Optional[str]:
    guild_id = m.ctx.guild.id
    channel_id = m.ctx.channel.id

    items = await Binding.filter(place=Binding.make_place_for_khl(guild_id, channel_id))
    return None if len(items) == 0 else items[0]
