import os
from flask import Flask, jsonify, send_from_directory
from podcast import generate_episode

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Podcast backend is running."})

@app.route("/generate", methods=["POST"])
def generate():
    result = generate_episode()
    return jsonify(result)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
