from peewee import Model, SqliteDatabase, CharField, DateTimeField

db = SqliteDatabase('challenge2_meli.db')

class DevOpsMail(Model):
    user_id = CharField()
    datetime  = DateTimeField()
    sender = CharField()
    subject = CharField()
    class Meta:
        database = db

db.create_tables([DevOspMail])