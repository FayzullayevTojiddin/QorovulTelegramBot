from peewee import *
from .base import BaseModel

from .action import Action

class BadWord(BaseModel):

    word = CharField(max_length=100)
    action = ForeignKeyField(Action, backref='BadWords', on_delete='NULL')
    time=DateTimeField()

    class Meta():
        table_name='BadWords'