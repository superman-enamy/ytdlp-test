from fastapi import FastAPI
import yt_dlp
import traceback

app = FastAPI()

@app.get("/")
def ping():
    return {"status": "alive"}

@app.get("/test")
def test_dl(url: str = "https://www.youtube.com/watch?v=BaW_C9pBvwQ"):
    ydl_opts = {
        'format': 'worst',
        'quiet': True,
        'simulate': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {"status": "success", "title": info.get("title")}
    except Exception as e:
        return {"status": "error", "message": str(e), "trace": traceback.format_exc()}
