import yt_dlp
import os
import traceback

DOWNLOAD_DIR = "/tmp/downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url):

    format_strategies = [
        "bestvideo+bestaudio/best",
        "bestvideo*+bestaudio/best",
        "best",
        "bv*+ba/b",
        "b"
    ]

    for fmt in format_strategies:
        try:

            ydl_opts = {
                "format": fmt,
                "noplaylist": True,
                "quiet": True,
                "force_ipv4": True,
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
                "title": info.get("title"),
                "status": "success"
            }

        except Exception as e:
            last_error = str(e)

    return {
        "status": "failed",
        "error": last_error
    }