import os
import boto3
import uuid
import datetime
import logging
from utils.s3_utils import upload_to_s3

# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables
BUCKET_NAME = os.environ.get("HL7_BUCKET")
SOURCE_ID = os.environ.get("SOURCE_ID", "hchb")


def lambda_handler(event, context):
    try:
        logger.info("Received event: %s", event)

        # Extract HL7 message from POST body
        if 'body' not in event:
            raise ValueError("Missing 'body' in event")

        hl7_data = event['body']
        now = datetime.datetime.utcnow()
        timestamp = now.strftime('%Y%m%dT%H%M%S')
        unique_id = str(uuid.uuid4())
        file_key = f"hl7/raw/{SOURCE_ID}/{now.year}/{now.month:02d}/{now.day:02d}/{timestamp}_{unique_id}.hl7"

        # Upload HL7 message to S3
        upload_to_s3(bucket=BUCKET_NAME, key=file_key, data=hl7_data)

        return {
            'statusCode': 200,
            'body': f"HL7 message stored as {file_key}"
        }

    except Exception as e:
        logger.error("Error processing HL7 message: %s", str(e), exc_info=True)
        return {
            'statusCode': 500,
            'body': 'Failed to store HL7 message.'
        }