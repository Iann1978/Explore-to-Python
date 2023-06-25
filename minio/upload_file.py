
print("hello")

import boto3

# Initialize the S3 client
s3 = boto3.client('s3',
                  endpoint_url='http://127.0.0.1:9900',
                  aws_access_key_id='EkWLEx1utoWwMRv1ddiY',
                  aws_secret_access_key='HDGWzmOLOerSTTuKSjW9Ljw3mOp8mVHyH871giDj',
                  region_name='dev',
                  verify=False)

# Set the name of the bucket and the name of the object
bucket_name = 'dev'
object_name = 'my-object2'

# Set the path to the file that you want to upload
file_path = 'minio/file.txt'

# Upload the file to MinIO
try:
    s3.upload_file(file_path, bucket_name, object_name)
    print(f'Successfully uploaded {file_path} to {bucket_name}/{object_name}')
except Exception as e:
    print(e)
