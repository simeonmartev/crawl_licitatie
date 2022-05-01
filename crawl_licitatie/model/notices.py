import datetime
from peewee import SqliteDatabase, Model, CharField, FloatField, DateTimeField

db = SqliteDatabase("../notices.db")


class BaseModel(Model):
    class Meta:
        database = db


class NoticeModel(BaseModel):
    notice_id = FloatField(unique=True)
    notice_number = CharField(unique=True)
    tender_name = CharField()
    procedure_status = CharField()
    contract_type = CharField()
    estimated_value = CharField()
    datetime = DateTimeField(default=datetime.datetime.now)
