import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EPISODES = [
    "Welcome to Constitution Vibes — breaking down Kenya’s constitution in a simple, vibey way.",
    "Today’s episode: The Bill of Rights — your freedoms and protections.",
    "Let’s talk about devolution — power to the counties, closer to the people.",
    "The role of parliament — making laws and holding leaders accountable.",
    "Final episode: Why knowing your constitution makes you powerful as a citizen."
]

os.makedirs("episodes", exist_ok=True)

for i, text in enumerate(EPISODES, start=1):
    filename = f"episodes/episode_{i}.mp3"
    if os.path.exists(filename):
        continue  # don’t overwrite existing files

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",  # closest to a Kenyan male accent available
        input=text
    ) as response:
        response.stream_to_file(filename)

    print(f"✅ Generated {filename}")
