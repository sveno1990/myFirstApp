from parliament import Context
from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary
import requests
import boto3

#s3url = os.environ["s3url"]
#s3bucket = os.environ["s3bucket"]
#s3Key = os.environ["s3key"]
url="http://my-first-channel-kn-channel.myfirstapp.svc.cluster.local"

def main(context: Context):
    """ 
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    #uuidForMessage = uuid.uuid4()
    attributes = {
      "source": "https://local-service",
      "type": "com.example.sampletype1"
    }
    data = '{"blobName": 'context.data' }'
    event = CloudEvent(attributes,data)
    headers, body = to_binary(event)
    requests.post(url,data=body, headers=headers)
    return { "message": "hallo" }, 200
