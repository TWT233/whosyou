from tortoise import fields
from tortoise.models import Model


class Attachment(Model):
    """attach a place to a specific platform, then platform arg can be omitted in some commands"""
    place = fields.CharField(max_length=64, pk=True)
    platform = fields.TextField()

    def __str__(self):
        return f'{self.place}-{self.platform}'

    @staticmethod
    def make_place_for_khl(guild_id: str, channel_id: str) -> str:
        return f'{guild_id}:{channel_id}'
