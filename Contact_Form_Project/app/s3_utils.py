import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(name, email, message):
    s3 = boto3.client('s3')

    bucket_name = os.getenv('BUCKET_NAME')
    key_name = f"contact_messages"
    content = f"Name: {name}\nEmail: {email}\nMessage: {message}\n"

    s3.put_object(Bucket=bucket_name, Key=key_name, Body=content)
    
