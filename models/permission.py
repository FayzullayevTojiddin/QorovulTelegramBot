from peewee import *
from .base import BaseModel

class Permission(BaseModel):
    can_it=CharField(max_length=100)

    class Meta():
        table_name='permissions'