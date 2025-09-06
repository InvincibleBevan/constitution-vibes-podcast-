import os
from flask import Flask, send_from_directory

# Absolute path to frontend/dist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "frontend", "dist")

app = Flask(__name__, static_folder=DIST_DIR, static_url_path="")

@app.route("/")
def index():
    return send_from_directory(DIST_DIR, "index.html")

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(DIST_DIR, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
