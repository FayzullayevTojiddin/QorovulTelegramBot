from peewee import *
from .base import BaseModel

class Action(BaseModel):
    name=CharField(max_length=100)

    class Meta():
        table_name='Actions'