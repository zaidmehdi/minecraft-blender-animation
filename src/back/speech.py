from pathlib import Path
from flask import current_app

def text_to_speech(text):
    """Convert text to speech by calling openai"""

    speech_file_path = Path.cwd() / "audio/speech.mp3"
    response = current_app.openai_client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    response.stream_to_file(speech_file_path)

    return speech_file_path