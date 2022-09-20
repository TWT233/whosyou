from khl import Bot, Cert

from config import config
from .cmd import register_cmds_for

cert = Cert(
    type=Cert.Types.WEBHOOK if config().verify_token else Cert.Types.WEBSOCKET,
    token=config().bot_token,
    verify_token=config().verify_token,
)

bot = Bot(cert=cert, port=9000, route='/')

register_cmds_for(bot)
