from fastapi import FastAPI
from pydantic import BaseModel
from downloader import get_stream_url
import os
import uvicorn

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"status": "service running"}

@app.post("/stream")
def stream(req: VideoRequest):
    try:
        return get_stream_url(req.url)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port)