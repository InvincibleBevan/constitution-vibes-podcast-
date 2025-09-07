import os
from openai import OpenAI

client = OpenAI()

EPISODE_DIR = "episodes"

def generate_episode(title, text):
    os.makedirs(EPISODE_DIR, exist_ok=True)
    filepath = os.path.join(EPISODE_DIR, f"{title}.mp3")

    if os.path.exists(filepath):
        return filepath  # Skip if already exists

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(filepath)

    return filepath
