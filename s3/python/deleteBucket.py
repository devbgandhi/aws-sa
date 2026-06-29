import boto3
from botocore.exceptions import ClientError

print("Deleting S3 bucket...")

#list buckets
s3_client = boto3.client("s3", region_name="us-west-2")
buckets = s3_client.list_buckets()
print("Existing S3 buckets:")
for bucket in buckets["Buckets"]:
    print(f" - {bucket['Name']}")

bucket_name = input("Enter the S3 bucket name to delete: ")

s3_client = boto3.client("s3", region_name="us-west-2")

try:
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"S3 bucket '{bucket_name}' deleted successfully.")
except ClientError as e:
    print(e)