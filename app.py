from fastapi import FastAPI
from pydantic import BaseModel
from downloader import download_video
import traceback

app = FastAPI()

class Request(BaseModel):
    url: str

@app.get("/")
def health():
    return {"status": "download service running"}

@app.post("/download")
def download(req: Request):
    try:
        return download_video(req.url)
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}