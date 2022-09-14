from khl import Message, Bot, ChannelPrivacyTypes
from khl.card import CardMessage, Card, Module
from khl.command import Command, Rule


def man(bot: Bot):
    @Command.command(regex=r'^\s*\(met\)\d+\(met\)\s*$', rules=[Rule.is_bot_mentioned(bot)])
    async def man_dec(m: Message):
        if m.channel_type is ChannelPrivacyTypes.GROUP:
            return await m.reply(build_help())
        return await m.reply(build_help())

    return man_dec


def build_help():
    result = CardMessage()
    result.append(Card(Module.Header('指令手册')))
    result.append(Card(
        Module.Header('绑定游戏 ID / 好友代码 / 平台用户名'),
        Module.Context('以下指令功能相同'),
        Module.Divider(),
        Module.Section('/bind {id/代码/用户名} {平台名}'),
        Module.Context('例：/bind 123444555 steam'),
        Module.Divider(),
        Module.Section('{平台名}id {id/代码/用户名}'),
        Module.Context('例：steamid 123444555\n例：eaid twt233')
    ))
    result.append(Card(
        Module.Header('查询我的游戏 ID / 好友代码 / 平台用户名'),
        Module.Context('以下指令功能相同'),
        Module.Divider(),
        Module.Section('/who {平台名}'),
        Module.Context('例：/who steam\n(机器人会回复你：123444555)'),
        Module.Divider(),
        Module.Section('{平台名}id'),
        Module.Context(
            '例：steamid\n(机器人会回复你：123444555)\n'
            '例：eaid\n(机器人会回复你：twt233)\n'
        )
    ))

    return result
