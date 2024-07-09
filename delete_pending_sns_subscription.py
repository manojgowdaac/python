import boto3
region = "ap-southeast-2"
# Initialize the SNS client
sns_client = boto3.client('sns', region_name = region)

# List all subscriptions
subscriptions = sns_client.list_subscriptions()

# Iterate over the subscriptions to find the pending one
for subscription in subscriptions['Subscriptions']:
    if subscription['SubscriptionArn'] == 'PendingConfirmation':
        # Unsubscribe the pending subscription
        sns_client.unsubscribe(SubscriptionArn=subscription['SubscriptionArn'])
        print(f"Unsubscribed pending subscription: {subscription['SubscriptionArn']}")
