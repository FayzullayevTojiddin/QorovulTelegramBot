from peewee import *
from .base import database

from .user import User
from .RestrictType import RestrictType
from .Restrict import Restrict
from .badWord import BadWord

def create_tables():
    with database:
        database.create_tables([
            User,
            RestrictType,
            Restrict,
            BadWord
        ])