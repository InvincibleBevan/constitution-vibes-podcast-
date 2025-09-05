from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

@app.route("/api/episodes")
def episodes():
    return jsonify([
        {"title": "Episode 1", "date": "2025-01-01", "audio": "/sample1.mp3"},
        {"title": "Episode 2", "date": "2025-02-01", "audio": "/sample2.mp3"}
    ])

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
