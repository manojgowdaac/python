import boto3

# Create a Boto3 resource for S3
s3_resource = boto3.resource('s3')

# Accessing meta information
resource_meta = s3_resource.meta

# Print the client type
print(resource_meta.client)

# Print the resource service name
print(resource_meta.service_name)

