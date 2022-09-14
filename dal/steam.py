from tortoise.models import Model
from tortoise import fields


class Steam(Model):
    khl = fields.CharField(max_length=64, pk=True)
    friend_code = fields.IntField()

    def __str__(self):
        return f'{self.khl}:{self.friend_code}'
