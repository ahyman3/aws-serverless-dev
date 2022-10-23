import json
import logging
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

logger = logging.getLogger()
logger.debug("Connecting to dynamodb")
# Creating a client for dynamosb
dynamodb = boto3.resource("dynamodb")
# Connecting to the movie database
table = dynamodb.Table('movieRecommender')
# Writing the time to a human readable format
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


def handler(event, context):
    logger.debug(msg="Event information:")
    logger.debug(msg=event)
    event = json.loads(event['body'])
    name = event['firstName'] + ' ' + event['lastName']
    response = table.put_item(
        Item={
            'ID': name,
            'LastGreetingTime': now
        }
    )
    payload = {
        "statusCode": 200,
        "body": json.dumps(f"Hello from lambda {name}")
    }

    return payload
