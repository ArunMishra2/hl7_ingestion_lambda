# HL7 Ingestion Lambda Function

This AWS Lambda function receives an HCHB HL7 message via API Gateway, stores it in S3 using a unique file structure, and is designed for scalability and auditability.

## 🔧 Environment Variables
- `HL7_BUCKET`: Name of the S3 bucket to store HL7 messages.
- `SOURCE_ID`: Sender identifier (e.g., hchb).
- `IGUANA_ENDPOINT`: (optional, for Iguana Lambda) HTTP endpoint for Iguana.
- `IGUANA_API_KEY`: (optional) API Key header for posting to Iguana.

## 📦 Deployment
This function can be deployed via Serverless Framework, SAM, or the AWS Console. IAM roles must include `s3:PutObject` and `s3:GetObject` for the appropriate bucket.

## 🧪 Example Event
```
{
  "body": "MSH|^~\\&|... HL7 message ..."
}
```
