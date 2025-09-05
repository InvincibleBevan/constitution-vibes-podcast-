import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

# Serve React frontend
@app.route("/")
def index():
    return send_from_directory("frontend/dist", "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    file_path = os.path.join("frontend/dist", path)
    if os.path.exists(file_path):
        return send_from_directory("frontend/dist", path)
    return send_from_directory("frontend/dist", "index.html")

# API for listing episodes
@app.route("/api/episodes")
def get_episodes():
    episodes_dir = "episodes"
    files = sorted(os.listdir(episodes_dir))
    episodes = [
        {"title": f.replace(".mp3", ""), "url": f"/episodes/{f}"}
        for f in files if f.endswith(".mp3")
    ]
    return jsonify(episodes)

# Serve episodes
@app.route("/episodes/<path:filename>")
def serve_episode(filename):
    return send_from_directory("episodes", filename)

# Serve static assets (anthem + Kenya flag video)
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
