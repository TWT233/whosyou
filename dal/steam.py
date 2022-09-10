from tortoise.models import Model
from tortoise import fields


class Steam(Model):
    khl = fields.TextField(pk=True)
    friend_code = fields.IntField()

    def __str__(self):
        return f'{self.khl}:{self.friend_code}'
