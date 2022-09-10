from tortoise.models import Model
from tortoise import fields


class Binding(Model):
    id = fields.IntField(pk=True)
    guild = fields.TextField()
    channel = fields.TextField()
    platform = fields.TextField()

    def __str__(self):
        return f'({self.id}){self.guild}:{self.channel}-{self.platform}'
