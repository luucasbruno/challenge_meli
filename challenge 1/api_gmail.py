
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from dateutil import parser

def get_mails_info(query):
    """
    returns: 
        1. A list of dicts containing info from messages that matches the word query in subject or body. 
        The keys are 'Subject', 'Date', 'From'
        2. User's email
    """
    user_id = 'me'

    # Setup the Gmail API
    scopes = 'https://www.googleapis.com/auth/gmail.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', scopes)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to request user's email
    resp = service.users().getProfile(userId=user_id).execute()
    user_email = resp['emailAddress']
    
    # Call the Gmail API to resquest messages:
    resp = service.users().messages().list(userId=user_id,q=query).execute()
    mails = []

    def build_mail(id_ ): 
        """
            Get Subject, From and Date from a mssg given an id
        """
        resp = service.users().messages().get(userId=user_email, id=id_).execute()
        payload = resp['payload']
        headers = payload['headers']
        mail = {}
        for header in headers:
            if header['name'] == 'Subject':
                mail['Subject'] = header['value']
            elif header['name'] == 'Date': 
                mail['Date'] = parser.parse(header['value'])
            elif header['name']=='From':
                mail['From'] = header['value']
        return mail

    if 'messages' in resp:
        mails.extend(build_mail(m['id']) for m in resp['messages']) 
    while 'nextPageToken' in resp:
        page_token = resp['nextPageToken']
        resp = service.users().messages().list(userId=user_id, q=query,pageToken=page_token).execute()
        mails.extend(build_mail(m['id']) for m in resp['messages']) 
    return (mails, user_email)
