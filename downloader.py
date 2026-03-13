import yt_dlp

def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,

        # let yt-dlp choose the best available format
        "format": "bestvideo+bestaudio/best",

        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },

        "nocheckcertificate": True,
        "cookiefile": "cookies.txt"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info.get("formats")

    if not formats:
        raise Exception("No formats available")

    # find a playable stream
    for f in reversed(formats):
        if f.get("url"):
            return {
                "title": info.get("title"),
                "stream_url": f["url"]
            }

    raise Exception("No valid stream found")