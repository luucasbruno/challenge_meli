from peewee import *
from datetime import date
db = SqliteDatabase('challenge2_meli.db')

class DevOpMail(Model):
    user_id = CharField()
    date  = DateTimeField()
    sender = CharField()
    subject = CharField()
    class Meta:
        database = db
    def insertMails(self,mails):    
        db.connect()
        db.create_tables([DevOpMail])
        for mail in mails['messages']:
            dev_mail = DevOpMail(user_id=mails['user'], date = mail['Date'], sender=mail['Sender'], subject=mail['Subject'])
            dev_mail.save()
        for mail in DevOpMail.select():
            print(mail.sender)
            print(mail.user_id)
            print(mail.date)
            print(mail.subject)