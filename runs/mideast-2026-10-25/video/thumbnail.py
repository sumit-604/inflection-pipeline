"""Render the 1280x720 thumbnail PNG from thumbnail.html.  python thumbnail.py <out.png>"""
import pathlib, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
out = sys.argv[1] if len(sys.argv) > 1 else str(HERE / "out" / "thumbnail.png")
with sync_playwright() as p:
    b = p.chromium.launch(args=["--font-render-hinting=none"]); pg = b.new_page(viewport={"width": 1280, "height": 720}); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e))); pg.goto((HERE / "thumbnail.html").as_uri()); pg.wait_for_function("window.READY === true"); pg.screenshot(path=out); b.close()
print("wrote", out, pathlib.Path(out).stat().st_size, "bytes; errors:", errs)
