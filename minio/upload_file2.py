from minio import Minio
# from minio.error import ResponseError

# Initialize the MinIO client
client = Minio('http://127.0.0.1:9900',
               access_key='EkWLEx1utoWwMRv1ddiY',
               secret_key='HDGWzmOLOerSTTuKSjW9Ljw3mOp8mVHyH871giDj',
               secure=False)

# Set the name of the bucket and the name of the object
bucket_name = 'dev'
object_name = 'my-object'

# Set the path to the file that you want to upload
file_path = 'minio/file.txt'

# Upload the file to MinIO
try:
    client.fput_object(bucket_name, object_name, file_path)
    print(f'Successfully uploaded {file_path} to {bucket_name}/{object_name}')
except ResponseError as err:
    print(err)
