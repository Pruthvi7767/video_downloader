from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def home():
    return {"status": "transcript service running"}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        segments = [
            {
                "text": t.text,
                "start": t.start,
                "duration": t.duration
            }
            for t in transcript
        ]

        full_text = " ".join([t["text"] for t in segments])

        return {
            "video_id": video_id,
            "segments": segments,
            "full_text": full_text
        }

    except Exception as e:
        return {"error": str(e)}