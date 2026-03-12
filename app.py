from fastapi import FastAPI
from pydantic import BaseModel
from downloader import get_stream_url

app = FastAPI()

class VideoRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"status": "service running"}


@app.post("/stream")
def stream(req: VideoRequest):
    return get_stream_url(req.url)