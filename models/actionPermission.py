from peewee import *
from .base import BaseModel

from .action import Action
from .permission import Permission

class ActionPermission(BaseModel):
    action_id = ForeignKeyField(Action, backref='permissions')
    permission_id = ForeignKeyField(Permission, backref='actions')

    class Meta():
        table_name="ActionPermissions"