from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model,
    AutoField,
    IntegerField,
    CharField,
    FloatField,
    DateTimeField,
)

db = SqliteDatabase("notices.db")


class BaseModel(Model):
    class Meta:
        database = db


class NoticeModel(BaseModel):
    id = AutoField(unique=True)
    notice_id = IntegerField(unique=True)
    notice_number = CharField(unique=True)
    tender_name = CharField()
    procedure_status = CharField()
    contract_type = CharField()
    estimated_value = FloatField()
    created_at = DateTimeField(default=datetime.now())
    datetime = DateTimeField(default=datetime.now())
