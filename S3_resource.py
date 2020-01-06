import boto3
# s3 = boto3.client('s3')
# result = s3.get_bucket_website(Bucket='BUCKET_NAME')
session = boto3.Session(profile_name='terraform')
s3 = boto3.resource('s3')
# obj = s3.Object(bucket_name='boto3', key='test.py')
bucket = s3.create_bucket(Bucket='cucu101')
print(bucket.name)