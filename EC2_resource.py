import boto3

def check_instance_state(instance_id, region):
    # Create an EC2 resource
    ec2 = boto3.resource('ec2', region_name=region)

    # Get the instance
    instance = ec2.Instance(instance_id)

    # Get the instance state
    state = instance.state['Name']

    return state

def start_instance(instance_id):
    # Create an EC2 resource
    ec2 = boto3.resource('ec2', region)

    # Get the instance
    instance = ec2.Instance(instance_id)

    # Start the instance
    instance.start()

    # Wait until the instance is running
    instance.wait_until_running()

    return instance.state['Name']

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

