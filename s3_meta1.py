import boto3

# Create a Boto3 client for the S3 service
s3_client = boto3.client('s3')

# Accessing meta information
client_meta = s3_client.meta

# Print the service name
print(client_meta.service_model)

# Print the endpoint URL
print(client_meta.endpoint_url)

