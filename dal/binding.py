from tortoise.models import Model
from tortoise import fields


class Binding(Model):
    place = fields.TextField(pk=True)
    platform = fields.TextField()

    def __str__(self):
        return f'{self.place}-{self.platform}'

    @staticmethod
    def make_place_for_khl(guild_id: str, channel_id: str) -> str:
        return f'{guild_id}:{channel_id}'
