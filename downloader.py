import yt_dlp
import os

DOWNLOAD_DIR = "/tmp/downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url):

    ydl_opts = {
        "format": "bestvideo*+bestaudio/best",
        "noplaylist": True,
        "quiet": False,
        "cookiefile": "cookies.txt",
        "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",

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