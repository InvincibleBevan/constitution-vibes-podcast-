import os
from pathlib import Path
from openai import OpenAI

# Load OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Directories
EPISODES_DIR = Path("episodes")
STATIC_DIR = Path("static")
EPISODES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

# Anthem path
ANTHEM_FILE = STATIC_DIR / "anthem.mp3"

# --- Generate Anthem if missing ---
def generate_anthem():
    if ANTHEM_FILE.exists():
        print("🎶 Anthem already exists, skipping...")
        return
    print("🎶 Generating Kenyan Anthem intro...")
    speech_text = (
        "Welcome to Constitution Vibes Podcast. "
        "Here, we break down Kenya’s Constitution with unity, freedom, and vibes!"
    )
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=speech_text,
    )
    with open(ANTHEM_FILE, "wb") as f:
        f.write(response.read())
    print(f"✅ Anthem saved: {ANTHEM_FILE}")

# --- Generate Episodes if missing ---
def generate_episodes():
    topics = [
        "The Spirit of the Constitution",
        "Bill of Rights Explained",
        "Devolution and County Governments",
        "Separation of Powers",
        "Citizen Participation in Governance"
    ]

    for i, topic in enumerate(topics, start=1):
        filename = EPISODES_DIR / f"episode_{i}.mp3"
        if filename.exists():
            print(f"🎧 {filename} exists, skipping...")
            continue

        print(f"🎧 Generating {filename} ...")
        script = f"Welcome to Episode {i}: {topic}. In this session, we explore {topic.lower()} in the Kenyan Constitution."
        
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=script,
        )
        with open(filename, "wb") as f:
            f.write(response.read())

        print(f"✅ Saved {filename}")

if __name__ == "__main__":
    print("🔊 Running podcast generator...")
    generate_anthem()
    generate_episodes()
    print("🚀 All done!")
