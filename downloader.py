import yt_dlp

def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "best",
        "nocheckcertificate": True,

        # helps bypass some bot detection
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },

        # use cookies if available
        "cookiefile": "cookies.txt"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info.get("formats")

    if not formats:
        raise Exception("No formats found")

    best = formats[-1]

    return {
        "title": info.get("title"),
        "stream_url": best.get("url")
    }