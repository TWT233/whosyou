from khl import Message
from khl.command import Command

import dal.ch2pf


@Command.command()
async def bind(m: Message, platform: str):
    try:
        await dal.ch2pf.Binding.create(guild=m.ctx.guild, channel=m.ctx.channel, platform=platform)
    except Exception as e:
        return await m.reply(f'query failed: {e}')
    return await m.reply('done')
