import os
from flask import Flask, send_from_directory

# Point Flask to frontend/dist where Vite builds the site
app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Catch all other routes and serve index.html (React Router support)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
