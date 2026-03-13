import yt_dlp
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "yt-dlp service running"}

@app.post("/info")
def get_video_info(data: dict):
    url = data.get("url")

    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    title = info.get("title")
    duration = info.get("duration")

    transcript = ""
    subs = info.get("automatic_captions") or {}

    if "en" in subs:
        transcript = subs["en"][0]["url"]

    return {
        "title": title,
        "duration": duration,
        "transcript_url": transcript
    }