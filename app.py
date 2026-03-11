from fastapi import FastAPI
from pydantic import BaseModel
from downloader import download_video

app = FastAPI()

class Request(BaseModel):
    url: str

@app.get("/")
def health():
    return {"status": "download service running"}

@app.post("/download")
def download(req: Request):
    return download_video(req.url)