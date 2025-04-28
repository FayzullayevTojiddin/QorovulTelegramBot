from peewee import *
from .base import BaseModel

class User(BaseModel):
    telegram_id=BigIntegerField(unique=True)
    first_name=CharField(max_length=255)
    last_name=CharField(max_length=255, null=True)
    username=CharField(max_length=255)
    lang=CharField(max_length=2)
    status=BooleanField(default=True)

    class Meta():
        table_name="TelegramUsers"

    @classmethod
    def getUserByTelegramId(cls, TelegramId):
        return cls.get_or_none(cls.telegram_id == TelegramId)

    @classmethod
    def getLangByTelegramId(cls, TelegramId):
        try:
            user = cls.getUserByTelegramId(TelegramId)
            return user.lang
        except Exception as error:
            print(error)
            return False