from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.routes import bp as route
    app.register_blueprint(route)
    
    return app