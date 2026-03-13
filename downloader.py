import yt_dlp

def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "cookiefile": "cookies.txt",
        "format": "best",
        "nocheckcertificate": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info.get("formats", [])

    for f in formats[::-1]:
        if f.get("url") and f.get("vcodec") != "none":
            return {
                "title": info.get("title"),
                "stream_url": f["url"]
            }

    raise Exception("No playable video found")