import boto3
import json, csv
from tqdm import tqdm

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ServerNames')

# Use in AWS Cloud9 with word_list.csv and ServNames table in DynamoDB

# Open CSV
with open('word_list.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')

    # Parse Each Line
    with table.batch_writer() as batch:
        for row in reader:

            if not row: 
                continue

            # Create JSON Object
            # Push to DynamoDB

            data = {}
            data["Name"] = row[0]

            response = batch.put_item(
              Item=data
            )

                # Repeat