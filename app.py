import yt_dlp
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class VideoRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"status": "yt-dlp service running"}


@app.post("/info")
def get_video_info(data: VideoRequest):

    try:

        ydl_opts = {
            "quiet": True,
            "nocheckcertificate": True,
            "ignoreerrors": False,
            "cookiefile": "cookies.txt",
            "skip_download": True,
            "retries": 5,
            "format": "bv*+ba/b",
            "extractor_args": {
                "youtube": {
                    "player_client": ["android", "web"]
                }
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(data.url, download=False)

        if not info:
            raise Exception("Video extraction failed")

        # handle playlist type response
        if "entries" in info:
            info = info["entries"][0]

        formats = info.get("formats", [])

        stream_url = None

        for f in formats:
            if f.get("url"):
                stream_url = f["url"]
                break

        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "stream_url": stream_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))