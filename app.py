from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="dist", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

@app.route("/episodes")
def get_episodes():
    return jsonify({"message": "Episodes will be generated soon!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
