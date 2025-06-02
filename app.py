import boto5

# Initialize S3 client
s3 = boto3.client('s3')

# 1. List all S3 buckets
response = s3.list_buckets()
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")

# Replace with your bucket and file info
bucket_name = 'your-bucket-name'
upload_file_path = 'path/to/local/file.txt'
download_file_path = 'path/to/save/file.txt'
s3_key = 'uploaded-file.txt'

# 2. Upload a file to S3
s3.upload_file(upload_file_path, bucket_name, s3_key)
print(f"Uploaded {upload_file_path} to s3://{bucket_name}/{s3_key}")

# 3. Download the same file back from S3
s3.download_file(bucket_name, s3_key, download_file_path)
print(f"Downloaded s3://{bucket_name}/{s3_key} to {download_file_path}")
