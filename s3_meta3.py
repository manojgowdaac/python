import boto3

# Create a Boto3 session
session = boto3.Session()

# Accessing meta information
session_meta = session._session

# Print the available services
print(session_meta.get_available_services())

