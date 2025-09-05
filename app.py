import os
import subprocess
from flask import Flask, send_from_directory, render_template_string, request

app = Flask(__name__)

# Serve episodes
@app.route("/episodes/<path:filename>")
def episodes(filename):
    return send_from_directory("episodes", filename)

# Homepage
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Constitution Vibes</title>
        <style>
            body, html { margin:0; padding:0; height:100%; overflow:hidden; font-family:Arial; }
            video.bg { position:fixed; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index:-1; }
            .content { position:relative; text-align:center; top:30%; color:white; }
            h1 { font-size:3em; text-shadow:2px 2px 6px black; }
            ul { list-style:none; padding:0; }
            li { margin:20px 0; font-size:1.2em; }
            audio { width:70%; margin-top:10px; }
        </style>
    </head>
    <body>
        <video autoplay loop muted playsinline class="bg">
            <source src="/static/Kenya_flag.mp4" type="video/mp4">
        </video>
        <div class="content">
            <h1>🇰🇪 Constitution Vibes Podcast</h1>
            <h3>Latest Episodes:</h3>
            <ul>
                {% for file in files %}
                <li>
                    🎧 {{file}} <br>
                    <audio controls preload="none">
                        <source src="/episodes/{{file}}" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </li>
                {% endfor %}
            </ul>
            <p><a href="/admin" style="color:#0f9;">Admin Panel</a></p>
        </div>
    </body>
    </html>
    """, files=[f for f in os.listdir("episodes") if f.endswith(".mp3")])

# Admin page
@app.route("/admin")
def admin():
    return """
    <html>
    <body style='background:#111; color:white; text-align:center; font-family:Arial'>
        <h2>🔐 Admin Panel</h2>
        <form method="post" action="/admin/regenerate">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Regenerate Episodes</button>
        </form>
    </body>
    </html>
    """

# Regenerate episodes
@app.route("/admin/regenerate", methods=["POST"])
def regenerate():
    password = request.form.get("password")
    if password != os.getenv("ADMIN_PASSWORD", "changeme"):
        return "❌ Wrong password", 403

    try:
        subprocess.run(["python", "podcast.py"], check=True)

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
                body {{ background:#111; color:white; font-family:Arial; text-align:center; }}
                ul {{ list-style:none; padding:0; }}
                li {{ margin:15px 0; }}
                a {{ color:#0f9; }}
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

if __name__ == "__main__":
    os.makedirs("episodes", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
