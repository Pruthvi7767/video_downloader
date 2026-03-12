import yt_dlp


def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info.get("formats")

    if not formats:
        raise Exception("No formats found")

    best = formats[-1]

    return {
        "title": info.get("title"),
        "video_url": best.get("url")
    }