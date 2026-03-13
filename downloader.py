import yt_dlp
import time


def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "cookiefile": "cookies.txt",

        # safer format selection
        "format": "bestvideo+bestaudio/best",

        # reduce bot detection
        "extractor_args": {
            "youtube": {
                "player_client": ["web", "android"]
            }
        },

        # retry inside yt-dlp
        "retries": 10,
        "fragment_retries": 10,
        "nocheckcertificate": True
    }

    attempts = 5

    for attempt in range(attempts):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            formats = info.get("formats", [])

            for f in formats[::-1]:
                if f.get("url") and f.get("vcodec") != "none":
                    return {
                        "title": info.get("title"),
                        "stream_url": f["url"]
                    }

            raise Exception("No playable formats found")

        except Exception as e:

            print("Attempt", attempt + 1, "failed:", e)

            if attempt < attempts - 1:
                time.sleep(8)
            else:
                return {
                    "status": "failed",
                    "error": str(e)
                }