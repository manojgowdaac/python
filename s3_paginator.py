import boto3

# Create a Boto3 client for the S3 service
s3_client = boto3.client('s3')

# Create a paginator for the list_objects_v2 operation
paginator = s3_client.get_paginator('list_objects_v2')

# Define the bucket name
bucket_name = 'manojgowdaac'

# Use the paginator to iterate over all pages of results
for page in paginator.paginate(Bucket=bucket_name):
    for obj in page.get('Contents', []):
        print(f"object key: {obj['Key']}, Creation Date: {obj['LastModified']}")

