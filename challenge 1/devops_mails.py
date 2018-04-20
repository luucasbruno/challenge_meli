import api_gmail
from sqli_db import DevOpsMail

def fetch_and_store_():
    mails, user_email = api_gmail.get_mails_info('devops')
    for m in mails:
        DevOpsMail.create(
            user_id = user_email,
            datetime = m['Date'],
            sender = m['From'],
            subject = m['Subject']
        )

def list_():
    fmt = u'{:25} {:24} {:25} {}'
    print(fmt.format('User_id', 'DateTime', 'Sender', 'Subject'))    
    for mail in DevOpsMail.select():
        print(fmt.format(mail.user_id, mail.datetime, mail.sender, mail.subject))    


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'list':
        list_()
    else:
        fetch_and_store_()