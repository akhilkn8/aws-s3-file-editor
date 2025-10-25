import os
import boto3
from dotenv import load_dotenv

load_dotenv()


client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    # aws_session_token=SESSION_TOKEN,
)

response = client.list_objects_v2(
    Bucket='test-bucket-696793786196'
)

for content in response['Contents']:
    print(content.get('Key'))
