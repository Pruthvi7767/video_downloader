from fastapi import FastAPI
from pydantic import BaseModel
from downloader import get_stream_url

app = FastAPI()

class Request(BaseModel):
    url: str

@app.post("/stream")
def stream(req: Request):
    return get_stream_url(req.url)