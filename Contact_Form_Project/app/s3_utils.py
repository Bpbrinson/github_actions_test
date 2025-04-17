import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(name, email, message):
    s3 = boto3.client('s3', 
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    bucket_name = os.getenv('BUCKET_NAME')
    key_name = f"contact_messages"
    content = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"

    s3.put_object(Bucket=bucket_name, Key=key_name, Body=content)
    
