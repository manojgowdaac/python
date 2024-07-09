import boto3

name = "manoj-1" # topic name for SNS 

region = "ap-southeast-2"
ec2 = boto3.resource("ec2", region_name = region)
client = boto3.client("sns", region_name = region)

#SNS Creation
response = client.create_topic(
        Name = name)
print(response)

response = client.subscribe(TopicArn = "arn:aws:sns:ap-southeast-2:058264404188:manoj-1",
                                Protocol = "email", Endpoint = "manojgowdaaac@gmail.com", ReturnSubscriptionArn=True)

vol_status = {"Name": "status", "Values":["available"]}

for vol in ec2.volumes.filter(Filters=[vol_status]):
    vol_id = vol.id
    volume = ec2.Volume(vol.id)
    print("clean up ECS volume: ", vol_id)
    volume.delete()

    msg = f'following EBS volume {vol_id} is deleted'
    client.publish(TopicArn ='arn:aws:sns:ap-southeast-2:058264404188:manoj-1', Message = msg)
   
