import os
from pathlib import Path

from peewee import *

DPATH = Path(__file__).parent.parent.parent  # inp_editing prject folder

db_path = DPATH / "test.sqlite"
db = SqliteDatabase(db_path, check_same_thread=False)


class BaseModel(Model):
    class Meta:
        database = db


class Node(BaseModel):
    x = FloatField()
    y = FloatField()
    z = FloatField()


def init_db():
    if not db_path.parent.is_dir():
        os.makedirs(db_path.parent)

    Node.create_table()


def node_id(x, y, z):
    n = Node.get_or_none(Node.x == x & Node.y == y & Node.z == z)
    if n:
        return n.id
