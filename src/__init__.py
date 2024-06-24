import os

from dotenv import load_dotenv
from flask import Flask, current_app
from flask_cors import CORS
from openai import OpenAI


def create_app():
    """Initialize the app"""

    app = Flask(__name__)
    CORS(app)

    load_dotenv(".env")

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with app.app_context():
        current_app.openai_client = openai_client
        
    return app