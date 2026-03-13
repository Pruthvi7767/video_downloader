from fastapi import FastAPI
from pydantic import BaseModel
from downloader import get_stream_url
import os  # Fixed the syntax error here
import uvicorn

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"status": "service running"}

@app.post("/stream")
def stream(req: VideoRequest):
    return get_stream_url(req.url)

if __name__ == "__main__":
    # Railway sets the PORT environment variable dynamically.
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)