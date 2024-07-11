import boto3

region = ""
s3 = boto3.client("s3", region_name = region)

for bucket in s3.list_buckets()['Buckets']:
    bucket_name = bucket['Name']


    all_objects = s3.list_objects(Bucket = bucket_name)

    if 'Contents' in all_objects:
        for obj in all_objects['Contents']:
            bucket_key = obj['Key']

# why we are using "get_object_acl" here?
# bcz we are will get more infomation in GRANTS, If Grants is public we will get some more information
        response = s3.get_object_acl(Bucket = bucket_name, Key = bucket_key)
        if len(response['Grants']) > 1:
            for grant in response['Grants']:
                if 'URI' in grant['Grantee'] and 'AllUsers' in grant['Grantee']['URI']:
                    s3.put_object_acl(Bucket=bucket_name, Key=bucket_key, ACL='private')
                    print(f"The object {bucket_key} in bucket {bucket_name} is now marked as private")
                    break
            #print(f"the bucket {bucket_name} with key {bucket_key} is now marked as private")
            #s3.put_object_acl(Bucket = bucket_name, Key = bucket_key, ACL = 'private')
            #print(f"the bucket {bucket_name} with key {bucket_key} is now marked as private")

    else:
        print(f"No objects found in bucket: {bucket_name}")
