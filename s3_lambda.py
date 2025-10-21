import json


def handler(event, context):
    print("S3 event!")
    print(json.dumps(event, indent=2))
    return "ok"