import yt_dlp
import os

DOWNLOAD_DIR = "/tmp/downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url):
    try:

        ydl_opts = {
            "noplaylist": True,
            "quiet": False,
            "cookiefile": "cookies.txt",
            "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
            "force_ipv4": True,

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
            "status": "success",
            "video_id": video_id,
            "title": info.get("title"),
            "video_path": f"{DOWNLOAD_DIR}/{video_id}.mp4"
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }