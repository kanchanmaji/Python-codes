from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import yt_dlp
import time
import os

app = FastAPI()

# ---------------- RATE LIMIT ----------------
RATE_LIMIT = 6
WINDOW = 60
clients = {}

def allow(ip):
    now = time.time()
    history = clients.get(ip, [])
    history = [t for t in history if now - t < WINDOW]
    if len(history) >= RATE_LIMIT:
        return False
    history.append(now)
    clients[ip] = history
    return True

# ---------------- UI ----------------
HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>YT Downloader</title>
<style>
* {{
    box-sizing: border-box;
    font-family: system-ui, -apple-system, BlinkMacSystemFont;
}}
body {{
    margin: 0;
    background: #f1f5f9;
}}
header {{
    background: white;
    padding: 16px;
    border-bottom: 1px solid #e5e7eb;
}}
h1 {{
    margin: 0;
    font-size: 20px;
}}
.container {{
    padding: 16px;
    max-width: 900px;
    margin: auto;
}}
.card {{
    background: white;
    border-radius: 12px;
    padding: 16px;
    margin-top: 16px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}}
input {{
    width: 100%;
    padding: 14px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #d1d5db;
}}
button {{
    width: 100%;
    padding: 14px;
    font-size: 16px;
    margin-top: 12px;
    border: none;
    border-radius: 8px;
    background: #2563eb;
    color: white;
}}
.grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 12px;
}}
.quality {{
    border: 1px solid #e5e7eb;
    border-radius: 10px;
    padding: 12px;
    text-align: center;
}}
.quality a {{
    display: block;
    margin-top: 6px;
    text-decoration: none;
    color: #2563eb;
    font-weight: 600;
}}
footer {{
    padding: 20px;
    font-size: 13px;
    color: #6b7280;
    text-align: center;
}}
.icon {{
    width: 20px;
    height: 20px;
    vertical-align: middle;
}}
.badge {{
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    padding: 4px 8px;
    border-radius: 999px;
    font-size: 12px;
}}
</style>
</head>

<body>

<header>
<h1>📥 YouTube Downloader</h1>
</header>

<div class="container">
<div class="card">
<form method="post">
<input name="url" placeholder="Paste YouTube link here" required>
<button>Fetch Video</button>
</form>
</div>

{content}

<div class="card">
<h3>ℹ️ Disclaimer</h3>
<p style="font-size:14px;color:#6b7280">
For personal and educational use only. Respect copyright laws and platform terms.
</p>
</div>

<div class="card">
<h3>📢 Ad Space</h3>
<p style="color:#6b7280">Your banner or ad code goes here</p>
</div>
</div>

<footer>
© 2026 | Built for learning
</footer>

</body>
</html>
"""

# ---------------- ROUTES ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return HTML.format(content="")

@app.post("/", response_class=HTMLResponse)
def fetch(request: Request, url: str = Form(...)):
    ip = request.client.host
    if not allow(ip):
        raise HTTPException(429, "Too many requests")

    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    qualities = {}
    for f in info["formats"]:
        if f.get("vcodec") != "none" and f.get("height"):
            qualities[f["height"]] = f["format_id"]

    cards = ""
    for h, fid in sorted(qualities.items()):
        cards += f"""
        <div class="quality">
            <div class="badge">{h}p</div>
            <a href="/download?url={url}&fmt={fid}">Download</a>
        </div>
        """

    content = f"""
    <div class="card">
        <h3>🎬 {info.get("title")}</h3>
        <img src="{info.get("thumbnail")}" width="100%" style="border-radius:10px">
        <p style="font-size:14px;color:#6b7280">Select quality</p>
        <div class="grid">
            {cards}
        </div>
    </div>
    """

    return HTML.format(content=content)

@app.get("/download")
def download(request: Request, url: str, fmt: str):
    ip = request.client.host
    if not allow(ip):
        raise HTTPException(429, "Too many requests")

    filename = f"/storage/emulated/0/Download/video_{int(time.time())}.mp4"

    ydl_opts = {
        "format": fmt,
        "outtmpl": filename,
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return StreamingResponse(
        open(filename, "rb"),
        media_type="video/mp4",
        headers={"Content-Disposition": "attachment; filename=video.mp4"}
    )