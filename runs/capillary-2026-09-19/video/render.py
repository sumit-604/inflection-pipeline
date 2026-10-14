"""render.py - deterministic frame renderer for video.html (Playwright + Chromium) and muxer.
  python render.py still <seconds> <out.png>      one frame (for checking)
  python render.py contact                        contact-sheet.png: mid-scene frame of each scene
  python render.py frames [workers [lo hi]]       all frames (or a frame range) -> frames/f000000.jpg (parallel)
  python render.py mux <out.mp4>                  frames + out/audio.wav -> H.264 CRF 20 / AAC 192k, 25 fps, faststart"""
import json, math, multiprocessing as mp, pathlib, subprocess, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE / "video.html").as_uri()
FRAMES = HERE / "frames"
TL = json.loads((HERE / "out" / "timeline.json").read_text())
FPS = TL["fps"]; TOTAL = math.ceil(TL["total"] * FPS)

def open_page(p):
    b = p.chromium.launch(args=["--disable-gpu", "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto(URL); pg.wait_for_function("window.READY === true")
    return b, pg, errs

def worker(args):
    a, b_, = args
    with sync_playwright() as p:
        br, pg, errs = open_page(p)
        for f in range(a, b_):
            pg.evaluate(f"setFrame({f})")
            pg.screenshot(path=str(FRAMES / f"f{f:06d}.jpg"), type="jpeg", quality=93)
        if errs: print("page errors:", errs[:3])
        br.close()
    return b_ - a

def still(t, out):
    with sync_playwright() as p:
        br, pg, errs = open_page(p)
        pg.evaluate(f"setFrame({round(t * FPS)})"); pg.screenshot(path=out); br.close()
        if errs: print("page errors:", errs[:5])

def contact():
    from PIL import Image, ImageDraw
    sc = TL["scenes"]; imgs = []
    with sync_playwright() as p:
        br, pg, errs = open_page(p)
        for s in sc:
            t = (s["t0"] + s["t1"]) / 2 if s["id"] != 1 else (s["voice_start"] + s["voice_end"]) / 2
            pg.evaluate(f"setFrame({round(t * FPS)})"); pg.screenshot(path=str(HERE / "out" / f"cs{s['id']:02d}.png")); imgs.append((s["id"], t))
        if errs: print("page errors:", errs[:5])
        br.close()
    W, H = 640, 360; sheet = Image.new("RGB", (W * 3, H * 5), "#000")
    for i, (sid, t) in enumerate(imgs):
        im = Image.open(HERE / "out" / f"cs{sid:02d}.png").resize((W, H)); d = ImageDraw.Draw(im); d.rectangle([0, 0, 150, 24], fill="#000"); d.text((6, 5), f"scene {sid}  t={t:.1f}s", fill="#fff")
        sheet.paste(im, ((i % 3) * W, (i // 3) * H))
    sheet.save(HERE / "out" / "contact-sheet.png")

def frames(n, lo=0, hi=None):
    FRAMES.mkdir(exist_ok=True); hi = TOTAL if hi is None else min(hi, TOTAL)
    step = max(1, math.ceil((hi - lo) / (n * 4))); chunks = [(a, min(hi, a + step)) for a in range(lo, hi, step)]
    with mp.Pool(n) as pool:
        done = 0
        for r in pool.imap_unordered(worker, chunks):
            done += r; print(f"{done}/{hi - lo}", flush=True)

def mux(out):
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-framerate", str(FPS), "-i", str(FRAMES / "f%06d.jpg"), "-i", str(HERE / "out/audio.wav"),
           "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-movflags", "+faststart", "-shortest", out]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    m = sys.argv[1]
    if m == "still": still(float(sys.argv[2]), sys.argv[3])
    elif m == "contact": contact()
    elif m == "frames": frames(int(sys.argv[2]) if len(sys.argv) > 2 else 4, *(int(x) for x in sys.argv[3:5]))
    elif m == "mux": mux(sys.argv[2])
