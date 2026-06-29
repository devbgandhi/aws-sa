import boto3
from botocore.exceptions import ClientError

print("Creating S3 bucket...")

bucket_name = input("Enter the S3 bucket name: ")

s3_client = boto3.client("s3", region_name="us-west-2") 

try:
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": "us-west-2"
        }
    )
    print(f"S3 bucket '{bucket_name}' created successfully.")
except ClientError as e:
    print(e)