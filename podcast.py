import os
from openai import OpenAI

client = OpenAI()
STATIC_DIR = "static"
ANTHEM_FILE = os.path.join(STATIC_DIR, "anthem.mp3")

os.makedirs(STATIC_DIR, exist_ok=True)

try:
    if not os.path.exists(ANTHEM_FILE):
        print("🎶 Generating anthem.mp3 ...")
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input="Karibu to Constitution Vibes. This is the heartbeat of Kenya — unity, freedom, and vibes. Let's celebrate together!"
        ) as response:
            response.stream_to_file(ANTHEM_FILE)
        print("✅ anthem.mp3 generated successfully.")
    else:
        print("✅ anthem.mp3 already exists, skipping generation.")
except Exception as e:
    print(f"⚠️ Skipping anthem generation due to error: {e}")
