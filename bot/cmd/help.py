from khl import Message, Bot, PublicMessage, Event, ChannelPrivacyTypes
from khl.card import CardMessage, Card, Module, Element
from khl.command import Command, Rule


@Command.command(aliases=['man', '?', 'help'])
async def man_cmd(m: Message):
    if isinstance(m, PublicMessage):
        return await m.reply(CardMessage(build_index(), _build_temp_context()), True, True)
    return await m.reply(CardMessage(build_index()))


def man_tag(bot: Bot):
    @Command.command(regex=r'^\s*\(met\)\d+\(met\)\s*$', rules=[Rule.is_bot_mentioned(bot)])
    async def dec(m: Message):
        return await man_cmd.handler(m)

    @dec.on_exception(Exception)
    async def _(*_):
        ...

    return dec


def _build_temp_context() -> Card:
    return Card(Module.Context('该消息仅你可见'), color='#595959')


def build_index():
    result = Card(
        Module.Section('操作手册（点击按钮跳转到对应页）：'),
        Module.ActionGroup(
            Element.Button('绑ID', 'whosyou/man_bind'),
            Element.Button('查ID', 'whosyou/man_who'),
            Element.Button('支持的平台/游戏', 'whosyou/man_pf'),
        ),
        color='#21d8a4'
    )
    return result


def build_bind():
    result = Card(
        Module.Header('绑定游戏 ID / 好友代码 / 平台用户名'),
        Module.Context('以下指令功能相同'),
        Module.Divider(),
        Module.Section('/bind {id/代码/用户名} {平台名}'),
        Module.Context('例：/bind 123444555 steam'),
        Module.Divider(),
        Module.Section('{平台名}id {id/代码/用户名}'),
        Module.Context('例：steamid 123444555\n例：eaid twt233'),
        color='#cf8888',
    )
    return result


def build_who():
    result = Card(
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
        ),
        color='#8255c2'
    )
    return result


def build_pf():
    result = Card(
        Module.Header('支持的平台/游戏'),
        Module.Divider(),
        Module.Section('steam'),
        Module.Context('可用别名：st ST STEAM'),
        Module.Divider(),
        Module.Section('EA'),
        Module.Context('可用别名：ea'),
        Module.Divider(),
        Module.Section('Apex'),
        Module.Context('可用别名：ap apex APEX'),
        Module.Divider(),
        color='#88bdcf'
    )
    return result


_man_map = {
    'whosyou/man_bind': build_bind,
    'whosyou/man_who': build_who,
    'whosyou/man_pf': build_pf,
}


async def on_man_clicked(b: Bot, e: Event):
    if e.body['value'] not in _man_map:
        return

    builder = _man_map[e.body['value']]

    if e.body['channel_type'] == ChannelPrivacyTypes.GROUP.value:
        ch = await b.client.fetch_public_channel(e.body['target_id'])
        return await b.client.send(ch,
                                   CardMessage(build_index(), builder(), _build_temp_context(), ),
                                   temp_target_id=e.body['user_id'],
                                   )
    return (await b.client.fetch_user(e.body['user_id'])).send(
        CardMessage(builder(), build_index(), _build_temp_context()),
    )
