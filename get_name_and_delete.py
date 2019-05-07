from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')

response = table.scan(Limit=1)   
server = response['Items'][0]

# Assign the server name to the new server:
server_name = response['Items'][0]["Name"]
print(server_name)

#### ASSIGN TO SERVER HERE

# delete the server name from the database


deleted_item = table.delete_item(
    Key={
        'Name': server_name
    }
)
