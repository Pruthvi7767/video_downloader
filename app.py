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
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(data.url, download=False)

        captions = info.get("automatic_captions", {})
        transcript_url = ""

        if "en" in captions:
            transcript_url = captions["en"][0]["url"]

        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "transcript_url": transcript_url,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))