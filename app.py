import os
import subprocess
from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

# --------------------
# Frontend routes
# --------------------
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# --------------------
# Episodes API
# --------------------
@app.route("/episodes")
def list_episodes():
    os.makedirs("episodes", exist_ok=True)
    files = [f for f in os.listdir("episodes") if f.endswith(".mp3")]
    return jsonify(files)


@app.route("/episodes/<path:filename>")
def serve_episode(filename):
    return send_from_directory("episodes", filename)


# --------------------
# Admin page
# --------------------
@app.route("/admin")
def admin_page():
    return """
    <html>
    <head>
        <title>Admin Panel</title>
        <style>
            body { background: #111; color: #fff; font-family: Arial; text-align: center; }
            form { margin-top: 50px; }
            input, button { padding: 10px; margin: 10px; }
            a { color: #0f9; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h2>🔐 Constitution Vibes Admin</h2>
        <form method="POST" action="/admin/regenerate">
            <input type="password" name="password" placeholder="Enter Admin Password" required>
            <br>
            <button type="submit">Regenerate Episodes</button>
        </form>
    </body>
    </html>
    """


@app.route("/admin/regenerate", methods=["POST"])
def regenerate():
    password = request.form.get("password")
    if password != os.getenv("ADMIN_PASSWORD", "changeme"):
        return "❌ Wrong password", 403

    try:
        subprocess.run(["python", "kenya_constitution_podcast.py"], check=True)

        files = [f for f in os.listdir("episodes") if f.endswith(".mp3")]
        episode_blocks = "".join([
            f"""
            <li>
                🎧 {f}<br>
                <audio controls preload="none" style="width:80%; margin:10px;">
                    <source src="/episodes/{f}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </li>
            """ for f in files
        ])

        return f"""
        <html>
        <head>
            <title>Episodes Regenerated</title>
            <style>
                body {{ background: #111; color: #fff; font-family: Arial; text-align: center; }}
                ul {{ list-style: none; padding: 0; }}
                li {{ margin: 15px 0; }}
                audio {{ outline: none; }}
                a {{ color: #0f9; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
            <h2>✅ Episodes regenerated successfully!</h2>
            <h3>Available Episodes:</h3>
            <ul>{episode_blocks}</ul>
            <br>
            <a href="/admin" style="color:#f33;">⬅ Back to Admin</a>
        </body>
        </html>
        """
    except Exception as e:
        return f"⚠️ Error: {str(e)}", 500


# --------------------
# Serve static frontend
# --------------------
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
