"""contrast.py - text contrast (WCAG ratio, must be >= 4.5) measured on rendered pixels.
For every 10th frame it takes each fully visible text run (tspan), hides all text, and compares the run's fill colour with the pixels under its box.
Reports the worst pixel-group ratio per run (the 5th-percentile ratio, so a stray corner does not fail a run but a bad background does).
  python contrast.py <long|short> [step]"""
import io, json, pathlib, re, sys
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import render
JS = """(f) => { renderFrame(f); const eff = e => { let o = 1; for (let n = e; n && n.nodeType === 1 && n.id !== 'root'; n = n.parentNode) { if (n.getAttribute('display') === 'none') return 0; const a = n.getAttribute('opacity'); if (a !== null) o *= parseFloat(a); } return o; };
  const out = []; document.querySelectorAll('text').forEach(t => { if (eff(t) < 0.95) return; const runs = t.querySelectorAll('tspan'); const els = runs.length ? Array.from(runs) : [t];
    els.forEach(e => { const r = e.getBoundingClientRect(); if (r.width < 2) return; out.push({ text: (e.textContent || '').slice(0, 30), x0: r.left, y0: r.top, x1: r.right, y1: r.bottom, fill: getComputedStyle(e).fill, size: parseFloat(getComputedStyle(e).fontSize) }); }); }); return out; }"""
def lum(c): c = c / 255.0; c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
def main():
    fmt = sys.argv[1]; step = int(sys.argv[2]) if len(sys.argv) > 2 else 10; T = render.tl(fmt)
    fails = {}; checked = 0; worst = 99
    with sync_playwright() as p:
        b, pg, errs = render.open_page(p, fmt); pg.add_style_tag(content=".hide text { visibility: hidden; }")
        for f in range(0, T["frames"], step):
            items = pg.evaluate(JS, f)
            if not items: continue
            pg.evaluate("document.body.classList.add('hide')"); img = np.asarray(Image.open(io.BytesIO(pg.screenshot())).convert("RGB")).astype(float); pg.evaluate("document.body.classList.remove('hide')")
            for it in items:
                m = re.findall(r"[\d.]+", it["fill"]); fg = np.array([float(x) for x in m[:3]])
                x0, y0, x1, y1 = [int(round(v)) for v in (max(it["x0"], 0), max(it["y0"], 0), min(it["x1"], T["W"]), min(it["y1"], T["H"]))]
                if x1 - x0 < 2 or y1 - y0 < 2: continue
                # use the middle 70% of the box height (the box includes ascender/descender space)
                dy = (y1 - y0) * 0.15; reg = img[int(y0 + dy):int(y1 - dy), x0:x1].reshape(-1, 3)
                lf = lum(fg); lb = lum(reg); ratio = np.where(lf > lb, (lf + 0.05) / (lb + 0.05), (lb + 0.05) / (lf + 0.05)); r5 = float(np.percentile(ratio, 5)); checked += 1; worst = min(worst, r5)
                if r5 < 4.5: fails.setdefault((it["text"], it["fill"]), (f, round(r5, 2)))
        b.close()
    print(f"[{fmt}] contrast: {checked} text runs sampled (every {step}th frame), worst 5th-percentile ratio {worst:.2f}, runs below 4.5: {len(fails)}")
    for (t, fl), (f, r) in list(fails.items())[:20]: print("   ", repr(t), fl, "first at frame", f, "ratio", r)
    sys.exit(1 if fails else 0)
if __name__ == "__main__": main()
