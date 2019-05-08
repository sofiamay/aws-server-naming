import boto3
import json
# Adds a name to the DynoDB table
ec2 = boto3.resource('ec2')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')

def get_instance_name(instance_id):
    instance = ec2.Instance(instance_id)
    instancename = ''
    for tags in instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename

def lambda_handler(event, context):
    # Get server name
    instance_id = event['detail']['instance-id']
    instance_name = get_instance_name(instance_id)
    
    # Delete row with server name from the DB
    response = table.put_item(
   Item={
        'Name': instance_name,
    })
    
    print("PutItem succeeded:")
    return(json.dumps(response))
     