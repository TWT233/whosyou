from khl import Message
from khl.command import Command

from dal.attach import Attachment
from ._util import public_msg_only, done_card


@Command.command()
@public_msg_only
async def attach(m: Message, platform: str):
    try:
        await Attachment.create(place=Attachment.make_place_for_khl(m.ctx.guild.id, m.ctx.channel.id),
                                platform=platform)
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply(done_card())
