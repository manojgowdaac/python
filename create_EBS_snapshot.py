import boto3


region = "ap-southeast-2"
ec2 = boto3.resource("ec2", region_name = region)

for vol in ec2.volumes.all():
    vol_id = vol.id
    volume = ec2.Volume(vol_id)
    desc = "this new the snapshot of EBS {}".format(vol_id)
    print("creating the snapshot for the following volume: ", vol_id)
    volume.create_snapshot(Description=desc)
