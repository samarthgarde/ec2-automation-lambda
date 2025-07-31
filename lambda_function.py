import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')  # Replace with your region

    instance_id = 'i-0abce123efgh5578'  # Replace with your actual EC2 instance ID
    action = event.get('action', '').lower()  # Expect 'start' or 'stop'

    if action == 'start':
        response = ec2.start_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': f'Started instance {instance_id}. Response: {response}'
        }

    elif action == 'stop':
        response = ec2.stop_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': f'Stopped instance {instance_id}. Response: {response}'
        }

    else:
        return {
            'statusCode': 400,
            'body': 'Invalid action. Use "start" or "stop".'
        }
