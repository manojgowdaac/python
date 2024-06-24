import boto3

def check_ec2_instance_state(instance_id, region):
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)
    
    try:
        # Describe the instance
        response = ec2.describe_instances(InstanceIds=[instance_id])
        
        # Extract the instance state
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        return state
    except Exception as e:
        return f"An error occurred: {str(e)}"

def start_ec2_instance(instance_id, region):
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)
    
    try:
        # Start the instance
        ec2.start_instances(InstanceIds=[instance_id])

        # Wait for the instance to be running
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        
        # Return the new state
        return 'running'
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    instance_id = ''  # Replace with your instance ID
    region = 'ap-southeast-2'  # Replace with your desired region

    # Check instance state
    state = check_ec2_instance_state(instance_id, region)
    print(f"The state of instance {instance_id} is: {state}")

    if state == 'stopped':
        # Start the instance if it is stopped
        new_state = start_ec2_instance(instance_id, region)
        print(f"Attempted to start the instance. New state: {new_state}")
    else:
        print(f"Instance {instance_id} is not in a stopped state. Current state: {state}")

