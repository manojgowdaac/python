import boto3

#specify the AWS region for EC2 
region_name = "ap-southeast-2"

#create a boto3 EC2 client
ec2_client = boto3.client('ec2',region_name = region_name)

def create_ec2_instance(ami_id, instance_type, security_group_id, key_name):
    try:
      response = ec2_client.run_instances(
                    ImageId = ami_id,
                        InstanceType = instance_type,
                        KeyName = key_name,
                        SecurityGroupIds = [security_group_id],
                        MinCount=1,
                        MaxCount=1
                        )
      #return response['Reservations'][0]['Instances'][0]

      print(f"instance is created successfully ")
    except Exception as e:
        print(f"Error creating EC2 instance: {e}")
        raise

#start the EC2 instance
def start_ec2_instance(instance_id):
    try:
        response = ec2_client.start_instances(InstanceIds = [instance_id])
        print(f"Inastance {instance_id} started successfully.")
    except Exception as e:
        print(f"Error starting EC2 Instance {instance_id}: {e}")
        raise

#to stop the EC2 instance
def stop_ec2_instance(instance_id):

    try:
        response = ec2_client.stop_instances(InstanceIds = [instance_id])
        print(f"instance {instance_id} stopped successfully.")
    except Excepiton as e:
        print(f"Error stopping Ec2 instance {instance_id}: {e}")
        raise


# main fuction provid the values for placeholder here

def main():
    ami_id = "ami-080660c9757080771"
    instance_type = 't2.micro'
    security_group_id = 'sg-08b89f8f7067f8b62'
    key_name = 'manoj'

#creat a new EC2 instance
    try:
        new_instance = create_ec2_instance(ami_id, instance_type, security_group_id, key_name)
        instance_id = new_instance['InstanceId']
        print(f"created new EC2 instance with ID : {instance_id}")
    except Exception as e:
        print(f"An error occured while creating the instance: {e}")
        return

    #start the created instance(optional)
    #start_ec2_instance()

    #stop the instance(optional)
    stop_ec2_instance(instance_id)

if __name__ == '__main__':
    main()







