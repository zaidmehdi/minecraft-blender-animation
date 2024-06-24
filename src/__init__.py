import os

from dotenv import load_dotenv
from flask import Flask, current_app
from openai import OpenAI


def create_app():
    """Initialize the app"""

    app = Flask(__name__)

    load_dotenv(".env")
    load_dotenv(".flaskenv")

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config['PORT'] = os.getenv("FLASK_PORT_PROD")
    app.config["DEBUG"] = True

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with app.app_context():
        current_app.openai_client = openai_client
        
    return app