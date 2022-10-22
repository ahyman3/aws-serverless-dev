import json


def handler(event, context):
    name = event['firstName'] + ' ' + event['lastName']

    payload = {
        "statusCode": 200,
        "body": json.dumps(f"Hello from lambda {name}")
    }

    return payload
