import os
from flask import Flask, jsonify, send_from_directory
from podcast import generate_episode  # Import the function we made

app = Flask(__name__, static_folder="static", static_url_path="/static")

EPISODE_DIR = "episodes"

# Ensure episodes exist on startup
def ensure_episodes():
    os.makedirs(EPISODE_DIR, exist_ok=True)
    files = [f for f in os.listdir(EPISODE_DIR) if f.endswith(".mp3")]
    if not files:  # Generate only if empty
        print("🎙️ No episodes found, generating one...")
        generate_episode("Intro Episode", "Welcome to the Constitution Vibes podcast!")

ensure_episodes()

@app.route("/episodes")
def get_episodes():
    episodes = []
    for file in os.listdir(EPISODE_DIR):
        if file.endswith(".mp3"):
            episodes.append({
                "title": os.path.splitext(file)[0],
                "description": "Auto-generated podcast episode",
                "file": f"/{EPISODE_DIR}/{file}"
            })
    return jsonify(episodes)

@app.route("/episodes/<path:filename>")
def serve_episode(filename):
    return send_from_directory(EPISODE_DIR, filename)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")
