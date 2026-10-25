"""render.py - deterministic frame renderer (Playwright + Chromium) and muxer. Frame f is exactly time f/30 s; frames 0..N-1 only.
  python render.py still <long|short> <seconds> <out.png>        one frame
  python render.py sheet <long|short> [step]                     contact sheet of every `step`-th frame (default 24), 4 across -> out/contact_<fmt>.png
  python render.py firsts <long|short>                           first frame of every scene -> out/first_<fmt>_<id>.png
  python render.py frames <long|short> [workers] [scale] [dir]   all frames -> <dir>/f000000.png (scale 1 = full size)
  python render.py mux <long|short> <audio.wav> <out.mp4> [dir]  frames + audio -> H.264 yuv420p, 30 fps constant, AAC"""
import json, math, multiprocessing as mp, pathlib, subprocess, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGES = {"long": "video.html", "short": "short.html"}

def tl(fmt): return json.loads((HERE / "out" / f"timeline_{fmt}.json").read_text())

def open_page(p, fmt, scale=1.0):
    t = tl(fmt)
    b = p.chromium.launch(args=["--disable-gpu", "--font-render-hinting=none", "--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": t["W"], "height": t["H"]}, device_scale_factor=scale)
    errs = []
    pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e))); pg.on("console", lambda m: errs.append("console: " + m.text) if m.type in ("error", "warning") else None)
    pg.on("requestfailed", lambda r: errs.append("requestfailed: " + r.url))
    pg.goto((HERE / PAGES[fmt]).as_uri()); pg.wait_for_function("window.READY === true", timeout=60000)
    return b, pg, errs

def shot(pg, f, path, **kw):
    pg.evaluate(f"renderFrame({f})"); pg.screenshot(path=str(path), **kw)

def worker(a):
    fmt, lo, hi, scale, outdir = a
    with sync_playwright() as p:
        b, pg, errs = open_page(p, fmt, scale)
        for f in range(lo, hi): shot(pg, f, pathlib.Path(outdir) / f"f{f:06d}.png")
        b.close()
    return hi - lo, errs

def frames(fmt, workers=4, scale=1.0, outdir=None):
    T = tl(fmt); N = T["frames"]; outdir = pathlib.Path(outdir or HERE / ("frames" if fmt == "long" else "frames_short")); outdir.mkdir(exist_ok=True)
    step = max(1, math.ceil(N / (workers * 6))); chunks = [(fmt, a, min(N, a + step), scale, str(outdir)) for a in range(0, N, step)]
    done = 0; allerr = []
    with mp.Pool(workers) as pool:
        for n, errs in pool.imap_unordered(worker, chunks):
            done += n; allerr += errs; print(f"{done}/{N}", flush=True)
    print("render errors:", len(allerr), allerr[:3])
    return N

def mux(fmt, audio, out, framedir=None):
    framedir = framedir or HERE / ("frames" if fmt == "long" else "frames_short")
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-framerate", "30", "-i", str(framedir / "f%06d.png") if hasattr(framedir, "joinpath") else f"{framedir}/f%06d.png",
           "-i", str(audio), "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30", "-vsync", "cfr", "-g", "60", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-movflags", "+faststart", "-shortest", out]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    m, fmt = sys.argv[1], sys.argv[2]
    if m == "still":
        with sync_playwright() as p:
            b, pg, errs = open_page(p, fmt); shot(pg, round(float(sys.argv[3]) * 30), sys.argv[4]); b.close(); print("errors:", errs[:5])
    elif m == "firsts":
        T = tl(fmt)
        with sync_playwright() as p:
            b, pg, errs = open_page(p, fmt)
            for s in T["scenes"]: shot(pg, round(s["t0"] * 30), HERE / "out" / f"first_{fmt}_{s['id']:02d}.png")
            b.close(); print("errors:", errs[:5])
    elif m == "sheet":
        from PIL import Image, ImageDraw
        step = int(sys.argv[3]) if len(sys.argv) > 3 else 24; T = tl(fmt); fr = list(range(0, T["frames"], step)); tw = 320 if fmt == "long" else 180; th = round(tw * T["H"] / T["W"])
        per = 48 if fmt == "long" else 24; tmp = HERE / "out" / "sheet_tmp.png"; pages = []
        with sync_playwright() as p:
            b, pg, errs = open_page(p, fmt)
            for pi in range(0, len(fr), per):
                chunk = fr[pi:pi + per]; sheet = Image.new("RGB", (tw * 4, th * math.ceil(len(chunk) / 4)), "#000")
                for i, f in enumerate(chunk):
                    shot(pg, f, tmp); im = Image.open(tmp).convert("RGB").resize((tw, th)); d = ImageDraw.Draw(im); d.rectangle([0, 0, 80, 14], fill="#000"); d.text((3, 2), f"f{f} {f/30:.1f}s", fill="#fff")
                    sheet.paste(im, ((i % 4) * tw, (i // 4) * th))
                name = HERE / "out" / f"contact_{fmt}_{pi // per + 1}.png"; sheet.save(name); pages.append(name.name)
            b.close(); print("errors:", errs[:5])
        print("contact sheets", len(fr), "frames:", pages)
    elif m == "frames": frames(fmt, int(sys.argv[3]) if len(sys.argv) > 3 else 4, float(sys.argv[4]) if len(sys.argv) > 4 else 1.0, sys.argv[5] if len(sys.argv) > 5 else None)
    elif m == "mux": mux(fmt, sys.argv[3], sys.argv[4], pathlib.Path(sys.argv[5]) if len(sys.argv) > 5 else None)
