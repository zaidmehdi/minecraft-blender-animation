from flask import current_app
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from pathlib import Path


def text_to_speech(text):
    """Convert text to speech by calling openai"""

    speech_file_path = Path.cwd() / "audio/speech.mp3"
    response = current_app.openai_client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    response.stream_to_file(speech_file_path)

    return str(speech_file_path)


def prompt_gpt(client, history, prompt):
    """Send a prompt to openai's gpt model"""

    history.append(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= history
    )
    content = response.choices[0].message.content

    return content


def get_animation_type(text):
    """Ask ChatGPT what animation matches the given text"""

    history = [
        {
            "role": "system", "content": "You are a classification model specialized in determining \
                what type of animation corresponds to a given text. Your role is to say which of the \
                following four animations should be used for a character saying some specific text. \
                The four animations are: 1- Waving hello. | 2. Pointing a finger at something. | \
                3. Shrugging. | 4. Catching one's breath. \n \
                Keep in mind you are expected to write only one number and nothing else."
        }
    ]

    prompt = {"role": "user", "content": f"The text is: {text}"}

    return str(prompt_gpt(current_app.openai_client, history, prompt))


def get_video_path(animation_type):
    """Given the animation type, returns the path to the video"""

    video_map = {"1": "renders/wave_hi.mkv",
                 "2": "renders/point_finger.mkv",
                 "3": "renders/shrug.mkv",
                 "4": "renders/tired.mkv"}

    return video_map[animation_type]


def assemble_video(video_path, audio_path, output_path="output_video.mp4"):
    """Put the video and audio together and makes video loop if audio is longer"""

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    num_repeats = int(audio_clip.duration / video_clip.duration) + 1
    
    video_clips = [video_clip] * num_repeats
    
    final_video_clip = concatenate_videoclips(video_clips)
    final_video_clip = final_video_clip.set_audio(audio_clip)

    final_video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    final_video_clip.close()
    audio_clip.close()

    return output_path