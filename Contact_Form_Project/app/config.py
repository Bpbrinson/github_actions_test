import os
from dotenv import load_dotenv

load_dotenv()   # Load environment variables from .env

class Config:
    SECRET_KEY = os.getenv('MY_SECRET')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    BUCKET_NAME = os.getenv('BUCKET_NAME')