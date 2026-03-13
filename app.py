from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def home():
    return {"status": "transcript service running"}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        text = " ".join([t["text"] for t in transcript])

        return {
            "video_id": video_id,
            "segments": transcript,
            "full_text": text
        }

    except Exception as e:
        return {"error": str(e)}