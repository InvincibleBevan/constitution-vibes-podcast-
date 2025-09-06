import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

# ✅ Serve frontend build
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# ✅ Serve episodes list
@app.route("/episodes")
def list_episodes():
    episodes_dir = os.path.join(os.getcwd(), "episodes")
    if not os.path.exists(episodes_dir):
        os.makedirs(episodes_dir)

    files = [f for f in os.listdir(episodes_dir) if f.endswith(".mp3")]
    return jsonify(files)

# ✅ Serve individual episode files
@app.route("/episodes/<path:filename>")
def get_episode(filename):
    return send_from_directory("episodes", filename)

# ✅ Serve static assets (Kenya flag + anthem)
@app.route("/static/<path:filename>")
def get_static(filename):
    return send_from_directory("static", filename)

# ✅ Catch-all: serve React frontend
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
