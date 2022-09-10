from khl import Message, Bot
from khl.command import Command


@Command.command()
async def who(m: Message, b: Bot, platform: str = None):
    """retrieve"""

