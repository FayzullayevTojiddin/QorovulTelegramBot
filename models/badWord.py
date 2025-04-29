from peewee import *
from .base import BaseModel

from .RestrictType import RestrictType

class BadWord(BaseModel):
    word = CharField(max_length=100, unique=True)
    restrict_type_id = ForeignKeyField(RestrictType, backref='restrictType')
    duration=IntegerField()

    class Meta():
        table_name='bad_words'