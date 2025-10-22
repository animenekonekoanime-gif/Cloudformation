import json
import boto3
import os


def lambda_handler(event, context):
    print("#event received")
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    message = f"A file has been uploaded to the bucket: {bucket_name}\n"
    message += f"File name : {object_key}"
    sqs =  boto3.client('sqs')
    queue_url = os.getenv('queue_url',None)

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(message)
    )
    print(message)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
