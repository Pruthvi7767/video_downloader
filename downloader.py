import yt_dlp

def get_stream_url(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "video_url": info["url"]
    }