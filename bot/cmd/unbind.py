from khl import Message
from khl.command import Command

import dal.ch2pf


@Command.command()
async def unbind(m: Message):
    try:
        await dal.ch2pf.Binding.filter(guild=m.ctx.guild, channel=m.ctx.channel).delete()
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply('done')
