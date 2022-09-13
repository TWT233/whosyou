from khl import Message
from khl.command import Command

from dal.binding import Binding
from ._util import public_msg_only


@Command.command()
@public_msg_only
async def bind(m: Message, platform: str):
    try:
        await Binding.create(place=Binding.make_place_for_khl(m.ctx.guild.id, m.ctx.channel.id),
                             platform=platform)
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply('done')
