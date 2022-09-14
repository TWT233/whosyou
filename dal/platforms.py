from tortoise import fields
from tortoise.models import Model


class Steam(Model):
    khl = fields.CharField(max_length=64, pk=True)
    friend_code = fields.IntField()

    def __str__(self):
        return f'{self.khl}:{self.friend_code}'


class EA(Model):
    khl = fields.CharField(max_length=64, pk=True)
    username = fields.TextField()

    def __str__(self):
        return f'{self.khl}:{self.username}'
