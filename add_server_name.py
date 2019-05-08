from __future__ import print_function # Python 2/3 compatibility
import boto3
import json

#Adds a name to the table


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')


# Edit this to be the name of the terminated server
name = "test"


response = table.put_item(
   Item={
        'Namw': name,
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4))
