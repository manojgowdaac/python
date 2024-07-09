import boto3

def check_instance_state(instance_id, region):
    # Create an EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    # Describe the instance to get its state
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']

    return state

def start_instance(instance_id):
    # Create an EC2 client
    ec2_client = boto3.client('ec2', region)

    # Start the instance
    ec2_client.start_instances(InstanceIds=[instance_id])

    # Wait until the instance is running
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

    # Describe the instance to get its new state
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']

    return state

if __name__ == "__main__":
    # Replace with your EC2 instance ID
    instance_id = 'i-0e9fd1772ca27c401'
    region = 'ap-southeast-2'
    
    state = check_instance_state(instance_id, region)
    print(f"The state of the instance {instance_id} is: {state}")

    if state == 'stopped':
        print(f"Starting the instance {instance_id}...")
        new_state = start_instance(instance_id)
        print(f"The state of the instance {instance_id} is now: {new_state}")
    else:
        print(f"The instance {instance_id} is already in the {state} state.")

