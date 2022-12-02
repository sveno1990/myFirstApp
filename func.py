from parliament import Context, event
import yagmail
import os
import json
import logging
import sys

@event
def main(context: Context):
  sender_email_address = os.environ['SENDER_EMAIL_ADDRESS']
  sender_email_password = os.environ['SENDER_EMAIL_PASSWORD']
  print(context.cloud_event, file=sys.stderr)
  emaildata = json.loads(json.dumps(context.cloud_event.data))
  receiver = emaildata['recipient']
  
  print(receiver, file=sys.stderr)
  return 'received, 200'
