from flask import Blueprint, jsonify, request

from back.utils import get_animation_type, get_video_path, text_to_speech, assemble_video


routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/animate", methods=["POST"])
def get_animation():
    """Return the full animation of the minecraft character with the audio"""

    text = request.json.get("text")

    animation_type = get_animation_type(text)
    video_path = get_video_path(animation_type)
    audio_path = text_to_speech(text)

    output_path = assemble_video(video_path, audio_path)
    
    return jsonify({
        "success": True,
        "video_path": output_path
    }), 201