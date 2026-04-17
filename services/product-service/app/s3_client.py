import os
import boto3
from botocore.config import Config

AWS_ENDPOINT_URL   = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
AWS_ACCESS_KEY_ID  = os.getenv("AWS_ACCESS_KEY_ID", "test")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")
AWS_REGION         = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET          = os.getenv("S3_BUCKET", "shopapi-product-images")

def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=AWS_ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
        config=Config(signature_version="s3v4")
    )

def upload_image(file_bytes: bytes, filename: str, content_type: str) -> str:
    client = get_s3_client()
    key = f"products/{filename}"
    client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=file_bytes,
        ContentType=content_type
    )
    return f"{AWS_ENDPOINT_URL}/{S3_BUCKET}/{key}"
