import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def upload_to_s3(bucket, key, data):
    try:
        logger.info(f"Uploading file to S3 - Bucket: {bucket}, Key: {key}")
        s3_client.put_object(
            Bucket=bucket,
            Key=key,
            Body=data.encode('utf-8'),
            ContentType='text/plain'
        )
        logger.info("Upload successful.")
    except Exception as e:
        logger.error(f"Failed to upload file to S3: {e}")
        raise