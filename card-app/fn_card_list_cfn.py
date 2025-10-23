import json
import boto3
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self,obj)
    
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_account_cfn')
    response = table.scan()['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(response, cls=DecimalEncoder)
    }
    
