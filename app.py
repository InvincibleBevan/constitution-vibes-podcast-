from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="dist", static_url_path="")

# Serve React index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve other static files (JS, CSS, images, etc.)
@app.route("/<path:path>")
def static_proxy(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

# Episodes API
@app.route("/episodes")
def get_episodes():
    return jsonify({"message": "Episodes will be generated soon!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
