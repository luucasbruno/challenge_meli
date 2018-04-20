import api_gmail
from sqli_db import DevOpMail
def main():
    mssgs, user_email = api_gmail.getMails() ## Nombrar mejor
    #print(msj)
    devopmail = DevOpMail()
    devopmail.insertMails(msgs)

if __name__ == '__main__':
    main()