import json
import boto3
from botocore.exceptions import ClientError
#When starting a new EC2 istnace: a
# ) retrieve a name from the database b) assign it to the new EC2 instance c) delete that name from the database

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')

# Helper function accepts an instance name and returns boolean: checks if instance contains a Name
def has_name(instance_id):
    instance = ec2.Instance(instance_id)
    for tags in instance.tags:
        if tags["Key"] == 'Name':
            if tags["Value"]:
                return True

# a) retrieve a name from the database
response = table.scan(Limit=1)   
server_name = response['Items'][0]["Name"]

def lambda_handler(event, context):
    # b) Assign it to a new EC2 instance
    instance_id = event['detail']['instance-id']
    tags=[
        {
            'Key': 'Name',
            'Value': server_name
        },
    ]
    
    try:
        client.create_tags(DryRun=False, Resources=[instance_id],Tags=tags)
    except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

    try:
        response = client.create_tags(DryRun=False,Resources=[instance_id],Tags=tags)
        print("Assigned a name to server successfully: ", response)
    except ClientError as e:
        print("Error: ", e)


    # C) delete server_name from the database
    deleted_item = table.delete_item(
    Key={
        'Name': server_name
    }
)
    return response, deleted_item