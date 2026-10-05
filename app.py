from fastapi import FastAPI
import yt_dlp
import traceback
import threading

app = FastAPI()

def test_ytdlp():
    print("Testing yt-dlp on YouTube...")
    url = "https://www.youtube.com/watch?v=BaW_C9pBvwQ"
    ydl_opts = {
        'format': 'worst',
        'quiet': True,
        'simulate': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print("yt-dlp SUCCESS! Title:", info.get("title"))
    except Exception as e:
        print("yt-dlp ERROR:")
        print(traceback.format_exc())

@app.on_event("startup")
def on_startup():
    threading.Thread(target=test_ytdlp, daemon=True).start()

@app.get("/")
def ping():
    return {"status": "alive"}
