import boto3

region = "ap-southeast-2"
ec2 = boto3.resource("ec2", region_name = region)

vol_status = {"Name":"status", "Values":["available"]}

for vol in ec2.volumes.filter(Filters=[vol_status]):
                     vol_id = vol.id
                     print("this is the volume id which is in available state: ", vol_id)
                     volume = ec2.Volume(vol_id)
                     #print(dir(volume)) to check the method for volume
                     print("clean the EBS volume which is in available: ", vol_id)
                     volume.delete()
