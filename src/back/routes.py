from flask import Blueprint, jsonify, request

from back.speech import text_to_speech


routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/speech", methods=["POST"])
def get_audio():
    """When a user submits a prompt, get the corresponding audio"""

    text = request.json.get("text")
    audio_path = text_to_speech(text)

    return jsonify({
        "success": True,
        "audio_path": str(audio_path)
    }), 201