import boto3
import os

bucket_name = os.environ.get('S3_BUCKET')


def handler(event, context):
    print('Inside lambda handler function')

    s3_client = boto3.client("s3")
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")
