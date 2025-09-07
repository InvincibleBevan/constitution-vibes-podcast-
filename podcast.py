import os
from openai import OpenAI

# Remove Render’s injected proxy variables if they exist
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)

# Initialize OpenAI safely with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Generate one podcast episode
def generate_episode():
    try:
        # Generate script text
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Kenyan podcast host mixing Sheng, English and Swahili, covering news and culture with energy."},
                {"role": "user", "content": "Create a short podcast script with Kenyan vibes and a youthful feel."}
            ],
        )
        script = response.choices[0].message.content.strip()

        # Generate audio (theme + speech)
        tts = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=script
        )

        # Save episode audio
        filename = "static/episode.mp3"
        os.makedirs("static", exist_ok=True)
        with open(filename, "wb") as f:
            f.write(tts.read())

        return {"success": True, "script": script, "audio_file": filename}

    except Exception as e:
        return {"success": False, "error": str(e)}
