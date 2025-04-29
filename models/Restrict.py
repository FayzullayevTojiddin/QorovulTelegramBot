from peewee import *
from .base import BaseModel

from .RestrictType import RestrictType

class Restrict(BaseModel):
    restrict_type = ForeignKeyField(RestrictType, backref='restricts')
    restrict_in = CharField()

    class Meta():
        table_name='restricts'