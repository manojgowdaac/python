#creating S3-Bucket in 'ap-southeast-1' region
"""import boto3

client =  boto3.client('s3')

response = client.create_bucket(
        Bucket = 'manoj-gowda-ac-s3-bucket-boto3',
        CreateBucketConfiguration = {
            'LocationConstraint' : 'ap-southeast-1',
            },
)

print(response)"""

#Deleting S3-Bucket
import boto3

client = boto3.client('s3')

response = client.delete_bucket(
        Bucket='manoj-gowda-ac-s3-bucket-boto3',
        )
print("S3-Bucket-deleted")



