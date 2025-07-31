# 📘 Documentation: Automate EC2 Start/Stop with AWS Lambda and EventBridge:

## 📌 Objective:
To automatically start or stop an EC2 instance using AWS Lambda and EventBridge (CloudWatch Events).

## 🛠️  Prerequisites:

- AWS Account
- One running EC2 instance
- IAM Role with proper permissions
- Basic knowledge of AWS Lambda and IAM

## 🧾 Step-by-Step Setup:

**Steps**

### 1.Create IAM Role for Lambda
-  Go to IAM > Roles > Create role

### 2.Navigate to IAM → Policies → Create policy
Add Permission policy →<policyname>
Use JSON policy enabling EC2 start/stop and log access:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

### 3.Create lambda function

- Lambda → Create Function → Author from scratch
- Runtime: Python 3.x
- Change Default execution role--use existing
- Existing role-<select role>
- Created function✅

- Use this code:
```
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
```
- Delpoy it ✅ 
**IMP**- Edit the Instance id in that

### 4.Test
- Test manually with
```
{}
```
### 5.Configuration -->Timeout-->30 Sec--> Save it-->Then Test

## Configure EventBridge Schedule Rules

Go to EventBridge → Scheduler → Create schedule

Choose a cron expression (e.g., cron(0 3 * * ? *) for 3 AM UTC)

📘 Explanation:
3 → minute (03)
11 → hour (11 AM UTC)
31 → day of month (31st)
7 → July
? → ignore day-of-week
2025 → year

Target: select relevant Lambda function

Pass custom payload like
```
{ "action": "start/stop" }
```

