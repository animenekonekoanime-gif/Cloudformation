import json


def lambda_handler(event, context):
    print("api, invoked!")
    print("#event ")
    print(json.dumps(event, indent=2))
    name = event.get("queryStringParameters").get("name", "")    
    #status code 200 means ok
    return {
        "statusCode": 200,
        "body": f"hello {name} from api lambda"
    }
    