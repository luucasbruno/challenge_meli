import api_gmail as apiGmail
from mysql_db import DevOpMail
def main():
    msgs = apiGmail.getMails()
    #print(msj)
    devopmail = DevOpMail()
    devopmail.insertMails(msgs)
main()