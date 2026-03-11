import yt_dlp
import os

# Render allows writing safely in /tmp
DOWNLOAD_DIR = "/tmp/downloads"

# create folder if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_video(url):

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "noplaylist": True,
        "quiet": False,
        "cookiefile": "cookies.txt",  # use exported YouTube cookies
        "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",

        # helps avoid YouTube bot detection
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    video_id = info["id"]

    return {
        "video_id": video_id,
        "video_path": f"{DOWNLOAD_DIR}/{video_id}.mp4",
        "title": info.get("title")
    }