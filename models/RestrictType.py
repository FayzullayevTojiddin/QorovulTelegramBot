from peewee import *
from .base import BaseModel

class RestrictType(BaseModel):
    type = CharField(unique=True)
    
    class Meta():
        table_name='restrict_types'