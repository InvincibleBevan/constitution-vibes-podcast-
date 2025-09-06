import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

# --- Config ---
EPISODES_DIR = os.path.join("static", "episodes")
STATIC_DIR = "static"

os.makedirs(EPISODES_DIR, exist_ok=True)


# Serve frontend
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# Serve frontend routes (for React router support)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")


# Get list of episodes
@app.route("/episodes")
def list_episodes():
    try:
        files = [
            f for f in os.listdir(EPISODES_DIR)
            if f.endswith(".mp3")
        ]
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Serve specific episode file
@app.route("/episodes/<path:filename>")
def get_episode(filename):
    return send_from_directory(EPISODES_DIR, filename)


# Serve static files (anthem, flag video, etc.)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
