from flask import Flask, send_from_directory, jsonify
import os
import subprocess

app = Flask(__name__, static_folder="static")

# Ensure podcast.py runs at startup to generate anthem.mp3
try:
    print("🔊 Running podcast.py to generate anthem and episodes...")
    subprocess.run(["python", "podcast.py"], check=True)
except Exception as e:
    print("⚠️ Error running podcast.py:", e)

@app.route("/")
def index():
    return send_from_directory("frontend/dist", "index.html")

@app.route("/<path:path>")
def serve_frontend(path):
    full_path = os.path.join("frontend/dist", path)
    if os.path.exists(full_path):
        return send_from_directory("frontend/dist", path)
    return send_from_directory("frontend/dist", "index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/episodes")
def episodes():
    episodes = []
    for file in os.listdir("static"):
        if file.endswith(".mp3"):
            episodes.append({
                "title": file.replace(".mp3", ""),
                "url": f"/static/{file}"
            })
    return jsonify(episodes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
