import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EPISODES = [
    "Welcome to Constitution Vibes – today we dive into the history of Kenya’s constitution...",
    "In this episode we explore the Bill of Rights, a pillar of Kenyan democracy...",
    "Let’s talk about devolution and why counties matter in Kenya’s governance...",
]

os.makedirs("episodes", exist_ok=True)

for i, script in enumerate(EPISODES, start=1):
    filename = f"episodes/episode{i}.mp3"
    if not os.path.exists(filename):
        print(f"🎙 Generating {filename}")
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=script
        ) as response:
            response.stream_to_file(filename)

print("✅ Podcast episodes generated!")
