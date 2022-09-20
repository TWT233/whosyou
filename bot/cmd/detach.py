from khl import Message
from khl.command import Command

from dal.attach import Attachment
from ._util import public_msg_only, done_card


@Command.command()
@public_msg_only
async def detach(m: Message):
    try:
        await Attachment.filter(place=Attachment.make_place_for_khl(m.ctx.guild.id, m.ctx.channel.id)).delete()
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply(done_card())
