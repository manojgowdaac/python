# script to start & stop multpile instance at once according to some requirements

import boto3

region = "ap-southeast-2"
ec2 = boto3.resource("ec2",region_name = region)

# filter according to storage
ec2_filter = {
            'Name': 'instance-type',
            'Values': [
                't2.nano'
            ]
        }
# according to tag name and more....
ec2_tag = {'Name':'tag:Name', 'Values':['abc']}
for instance in ec2.instances.filter(Filters = [ec2_tag]):
   instance.stop()
   # instance.start()
