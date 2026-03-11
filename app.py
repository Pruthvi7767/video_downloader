from fastapi import FastAPI
from pydantic import BaseModel
from downloader import get_stream_url
import traceback

app = FastAPI()

class Request(BaseModel):
    url: str

@app.get("/")
def health():
    return {"status": "stream service running"}

@app.post("/stream")
def stream(req: Request):
    try:
        return get_stream_url(req.url)
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}