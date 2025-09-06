import os
from flask import Flask, send_from_directory, jsonify, request, render_template
from kenya_constitution_podcast import generate_podcast

app = Flask(__name__, static_folder="frontend/dist/assets", template_folder="frontend/dist")

# Serve frontend build
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<path:path>")
def static_proxy(path):
    file_path = os.path.join(app.template_folder, path)
    if os.path.isfile(file_path):
        return send_from_directory(app.template_folder, path)
    return render_template("index.html")

# API: List episodes
@app.route("/api/episodes", methods=["GET"])
def list_episodes():
    episodes_dir = "episodes"
    files = [f for f in os.listdir(episodes_dir) if f.endswith(".mp3")]
    return jsonify([{"title": f.replace(".mp3", ""), "url": f"/episodes/{f}"} for f in files])

# Serve episodes
@app.route("/episodes/<path:filename>")
def get_episode(filename):
    return send_from_directory("episodes", filename)

# Admin: Regenerate episodes
@app.route("/api/regenerate", methods=["POST"])
def regenerate():
    password = request.json.get("password")
    if password != os.environ.get("ADMIN_PASSWORD", "changeme"):
        return jsonify({"error": "Unauthorized"}), 401
    generate_podcast()
    return jsonify({"status": "Episodes regenerated ✅"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
