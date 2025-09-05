from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_folder="frontend/dist", template_folder="frontend/dist")

@app.route("/episodes/<path:filename>")
def serve_episode(filename):
    return send_from_directory("episodes", filename)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists("frontend/dist/" + path):
        return send_from_directory("frontend/dist", path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
