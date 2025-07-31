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
- Existing role -->select role name
- Created function✅

- Use this code

- 👉 [view Code](lambda_fuction.py)

- Delpoy it ✅ 

**IMP**- Edit the Instance id in that

![View lambda function](images/lambda-function.png)

### 4.Test

- Test manually with

```
{}
```
### 5.Configuration

- timeout
- 30 sec
- configured ✅

### 6. Configure EventBridge Schedule Rules

![Define Shedule Rules](images/Define-cron.png)

- Go to EventBridge → Scheduler → Create schedule

- Choose a cron expression (e.g., cron(0 3 * * ? *) for 3 AM UTC)

- 📘 Explanation:

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
Created Function Rule - Update Rule ✅

![Stop Eventbridge created](images/Rule-stop.png)

### 7. Go to the lambda function

- Go to configuration
- Add Trigers:
- EventBridge (CloudWatch Events): ec2-stop-rule
- EventBridge (CloudWatch Events): ec2-start-rule

![Schedules Triggers](images/Trigger-lam.png)
