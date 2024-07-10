#Flow logs :- Basically captures all the traffic which is going in and out of VPC and that traffic is coming out of
# your elastic network interface  

import boto3
from botocore.exceptions import ClientError

region = "ap-southeast-2"
client = boto3.client ("ec2",region_name = region)
client_log = boto3.client('logs', region_name = region)

#response = client.describe_vpcs()
# print(response) # to get the dictionary
for vpcid in  client.describe_vpcs()['Vpcs']:
     vpc_id = vpcid['VpcId']

     log_group = vpc_id + "-flowlog" # vpc-052a9f1ad558c1c2c-flowlog

     try:
         response = client_log.create_log_group(
                 logGroupName = log_group)
     except ClientError:
         print("log group already exist for the following VPC:" , vpc_id)
flow_log_filter={"Name": "resource-id","Values":[vpc_id]}
response = client.describe_flow_logs(Filters=[flow_log_filter])
if len(response['FlowLogs']) > 0:
    print("vpc folw log is already enabled for this vpc:", vpc_id)
else:
    print("enabliing flow logs for the  follwoing vpc:" ,vpc_id)
    response = client.create_flow_logs(
                ResourceIds=[vpc_id],
                ResourceType='VPC',
                TrafficType='ALL',
                LogGroupName=log_group,
                DeliverLogsPermissionArn = "arn:aws:iam::role/flow_log"#"role_ARN" #provide the Role ARN from IAM roles which is the permission to push the logs
                                            # to VPC flow to the Cloud watch logs
            )

    
