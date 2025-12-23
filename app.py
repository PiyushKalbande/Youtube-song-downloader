import os
import json
import yt_dlp
from uuid import uuid4
from flask import jsonify
from utils import cleanup_temp
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file, Response, abort

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret")

TEMP_FOLDER = "temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)

# Load config safely
try:
    with open("config.json", "r", encoding="utf-8") as f:
        app_config = json.load(f)
except Exception:
    app_config = {
        "app_name": "Media Downloader",
        "tagline": "Fast & Simple Media Downloader",
        "about": "Configuration file missing or invalid.",
        "how_to_use": [],
        "features": [],
        "footer_note": ""
    }

progress_data = {}

@app.route("/")
def index():
    return render_template(
        "index.html",
        config=app_config,
        socials={
            "github": os.getenv("SOCIAL_GITHUB"),
            "instagram": os.getenv("SOCIAL_INSTAGRAM"),
            "linkedin": os.getenv("SOCIAL_LINKEDIN"),
            "facebook": os.getenv("SOCIAL_FACEBOOK"),
            "email": os.getenv("PERSONAL_EMAIL")
        }
    )

# ---------------- ERROR HANDLER ---------------- #
def fail(uid, message, code=400):
    progress_data[uid] = "ERROR"
    return jsonify({"status": "error", "message": message}), code


# ---------------- PROGRESS ---------------- #

def progress_hook(d, uid):
    try:
        if d["status"] == "downloading":
            progress_data[uid] = d.get("_percent_str", "0%").strip()
        elif d["status"] == "finished":
            progress_data[uid] = "100%"
    except Exception:
        progress_data[uid] = "0%"

@app.route("/progress/<uid>")
def progress(uid):
    def generate():
        last = ""
        while True:
            current = progress_data.get(uid, "0%")

            if current != last:
                yield f"data:{current}\n\n"
                last = current

            if current in ("100%", "ERROR"):
                break

    return Response(generate(), mimetype="text/event-stream")

# ---------------- DOWNLOAD ---------------- #

@app.route("/download", methods=["POST"])
def download():
    cleanup_temp()

    url = request.form.get("url")
    format_type = request.form.get("format")
    quality = request.form.get("quality")
    uid = request.form.get("uid") or str(uuid4())

    if not url:
        return fail(uid, "Please enter a valid YouTube URL")

    if format_type not in ("mp3", "mp4"):
        return fail(uid, "Invalid format selected")

    output_path = os.path.join(TEMP_FOLDER, uid)

    ydl_opts = {
        "outtmpl": output_path,
        "progress_hooks": [lambda d: progress_hook(d, uid)],
        "noplaylist": True,
        "quiet": True,
        "retries": 3
    }

    try:
        if format_type == "mp3":
            ydl_opts.update({
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": quality or "192"
                }]
            })
            final_ext = ".mp3"

        else:
            ydl_opts.update({
                "format": f"bestvideo[height<={quality or 720}][ext=mp4]+bestaudio[ext=m4a]/best",
                "merge_output_format": "mp4"
            })
            final_ext = ".mp4"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except yt_dlp.utils.DownloadError:
        return fail(uid, "Invalid or unsupported YouTube URL")
    except Exception:
        return fail(uid, "Server failed to process the request")

    final_file = output_path + final_ext

    if not os.path.exists(final_file):
        return fail(uid, "Failed to generate file")

    return send_file(final_file, as_attachment=True)

# ---------------- ENTRY ---------------- #

if __name__ == "__main__":
    app.run()
