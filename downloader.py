import yt_dlp

def get_stream_url(url):

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "nocheckcertificate": True,

        # safer format selection
        "format": "best[ext=mp4]/best",

        # helps bypass some YouTube bot checks
        "extractor_args": {
            "youtube": {
                "player_client": ["web"]
            }
        },

        # avoid DASH-only streams
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info.get("formats", [])

    # filter only real video streams
    video_formats = [
        f for f in formats
        if f.get("url") and f.get("vcodec") != "none"
    ]

    if not video_formats:
        raise Exception("No playable video streams found")

    best = video_formats[-1]

    return {
        "title": info.get("title"),
        "stream_url": best["url"]
    }