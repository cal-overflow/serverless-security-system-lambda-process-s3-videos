import boto3
import os
import time

bucket_name = os.environ.get('S3_BUCKET')


current_time = time.time()
folder_to_check = f"{time.strftime('%Y-%m-%d', time.localtime(current_time))}/"

def handler(event, context):
    print('Inside lambda handler function')

    s3_client = boto3.client("s3")

    # TODO - handle scenarios where there are > 1000 objects in bucket (this is unlikely since we're only getting the things in the "folder")
    response = s3_client.list_objects_v2(Bucket=bucket_name, prefix=folder_to_check)
    s3_objects = response.get("Contents")
    
    for obj in s3_objects:
        if folder_to_check in file:
            print(f"file_name: {file['Key']}, size: {file['Size']}")
