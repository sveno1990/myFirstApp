from parliament import Context, event
import yagmail
import os
import json
import logging
import sys

@event
def main(context: Context):
  emaildata = json.loads(json.dumps(context.cloud_event.data))
  receiver = emaildata['recipient']
  
  print(receiver, file=sys.stderr)
  return 'received, 200'
