from peewee import *
from datetime import date
db = SqliteDatabase('challenge_meli.db')

class DevOpMail(Model):
    user_id = CharField()
    date  = DateField()
    sender = CharField()
    subject = CharField()
    class Meta:
        database = db
    def insertMails(mails):    
        db.connect()
        db.create_tables([DevOpMail])
        for mail in mails:
            dev_mail = DevOpMail(user_id='lucas', date = date(w,1,1), sender=mail['Sender'])
            dev_mail.save()
        for mail in DevOpMail.select():
            print(mail.sender)