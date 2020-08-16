from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION,SCOPES)

def sendEmail():
   emailMsg = 'Bogus got a kill!'
   mimeMessage = MIMEMultipart()
   mimeMessage['to'] = 'valorantbot321@gmail.com'
   mimeMessage['subject'] = 'Valorant Kill'
   mimeMessage.attach(MIMEText(emailMsg, 'plain'))
   raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

   message = service.users().messages().send(userId = 'me', body = {'raw':raw_string}).execute()
   print(message)
   time.sleep(2)

def readEmail():
  try: 
    return service.users().messages().list(userId='me').execute()
  except Exception as error:
    print('An error occurred: %s' % error)

def deleteEmail():
  try: 
      inbox = readEmail()
      for i in range(inbox['resultSizeEstimate']):
        service.users().messages().trash(userId='me', id = inbox['messages'][i]['id']).execute()
  except Exception as error:
    print('An error occurred: %s' % error)
