from khl import Message
from khl.command import Command

from dal.binding import Binding


@Command.command()
async def unbind(m: Message):
    try:
        await Binding.filter(place=Binding.make_place_for_khl(m.ctx.guild.id, m.ctx.channel.id)).delete()
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply('done')
