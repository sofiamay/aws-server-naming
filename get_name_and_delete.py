import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client('ec2')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')

response = table.scan(Limit=1)   
server = response['Items'][0]

# Assign the server name to the new server:
server_name = response['Items'][0]["Name"]

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    # Retrieve a name from the database
    
    
    response = client.create_tags(
    DryRun=False,
    Resources=[
        instance_id,
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': server_name
        },
    ]
)
    deleted_item = table.delete_item(
    Key={
        'Name': server_name
    }
)
    return response, deleted_item