
"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import dateutil.parser as parser
def getMails():
    user_id = 'me'
    # Setup the Gmail API
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API0():
    response = service.users().messages().list(userId=user_id,q='subject: DevOps').execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id, q='subject: DevOps',pageToken=page_token).execute()
        messages.extend(response['messages'])

    
    temp_dict = {}
    mssgs = []

    # Get Subject, Sender and Date from mssgs
    for message in messages:
        resp = service.users().messages().get(userId=user_id, id=message['id']).execute()
        payId = resp['payload']
        headers = payId['headers']
        for header in headers:
            if header['name'] == 'Subject':
                msg_subject = header['value']
                temp_dict['Subject'] = msg_subject
            elif header['name'] == 'Date':
                msg_date = header['value']
                date_parse = (parser.parse(msg_date))
                m_date = (date_parse.date())
                temp_dict['Date'] = str(m_date)
            elif header['name']=='From':
                msg_from = header['value']
                temp_dict['Sender'] = msg_from
            else:
                pass
        print(temp_dict)    
        #mssgs.append(temp_dict)        
        
    #print(mssgs)
    return mssgs



