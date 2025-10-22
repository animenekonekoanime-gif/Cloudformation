import json


def lambda_handler(event, context):
    print("api, invoked!")
    return {
        "statusCode": 200,
        "body": "hello from api lambda"
    }