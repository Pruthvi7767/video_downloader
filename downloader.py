import yt_dlp
import time


def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "cookiefile": "cookies.txt",
        "format": "best",
        "nocheckcertificate": True,
        "retries": 10,
        "fragment_retries": 10
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

            raise Exception("No playable video format found")

        except Exception as e:

            print("Attempt failed:", e)

            if attempt < attempts - 1:
                time.sleep(5)
            else:
                return {
                    "status": "failed",
                    "error": str(e)
                }