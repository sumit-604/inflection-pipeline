"""counters.py - the frame counters for one draft. Loads the page, steps through EVERY frame (renderFrame(f), f = 0..N-1), and measures every text element.
  python counters.py <long|short> [--sfx]
Counters printed (0 is the goal):
  1 text outside the frame            visible text whose box leaves the frame
  2 text overlapping other text       two visible text boxes that intersect (boxes shrunk 12% in height, 2% in width)
  3 text held too briefly             captions and on-screen text: still for < 0.3 s per word + 0.5 s (still = fully opaque and not moving)
  6 runtime / render errors           page errors, console errors/warnings, failed requests
Counters 4 (dead air) and 5 (compliance) have their own scripts (deadair_check.py, compliance_sweep.py).
--sfx also writes out/sfx_<fmt>.json (sound-effect events: kind and the time of the visual event; assemble.py mix adds the one-frame lag)."""
import json, pathlib, sys
from collections import defaultdict
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import render

HERE = pathlib.Path(__file__).resolve().parent
PROBE = """
([f0, f1]) => {
  const texts = Array.from(document.querySelectorAll('text'));
  const eff = e => { let o = 1; for (let n = e; n && n.nodeType === 1 && n.id !== 'root'; n = n.parentNode) { if (n.getAttribute('display') === 'none') return 0; const a = n.getAttribute('opacity'); if (a !== null) o *= parseFloat(a); } return o; };
  const out = [];
  for (let f = f0; f < f1; f++) {
    renderFrame(f); const rows = [];
    texts.forEach((t, i) => { const o = eff(t); if (o > 0.02) { const r = t.getBoundingClientRect(); rows.push([i, +r.left.toFixed(2), +r.top.toFixed(2), +r.right.toFixed(2), +r.bottom.toFixed(2), +o.toFixed(3)]); } });
    out.push(rows);
  }
  return out;
}
"""
META = """() => Array.from(document.querySelectorAll('text')).map(t => ({ cap: t.getAttribute('data-cap'), os: t.getAttribute('data-os'), words: +t.getAttribute('data-words'), need: t.getAttribute('data-need'), text: (t.getAttribute('data-text') || t.textContent || '').slice(0, 60), size: +t.getAttribute('font-size') }))"""

def main():
    fmt = sys.argv[1]; T = render.tl(fmt); N, W, H, FPS = T["frames"], T["W"], T["H"], T["fps"]
    with sync_playwright() as p:
        b, pg, errs = render.open_page(p, fmt)
        meta = pg.evaluate(META); data = []
        for s in T["scenes"]:          # scene boundaries: the first and last frame of every scene must render that scene
            for f in (s["f0"], s["f1"] - 1):
                got = pg.evaluate("f => renderFrame(f)", f)
                if got != s["id"]: errs.append(f"frame {f} should be scene {s['id']}, rendered scene {got}")
        for f0 in range(0, N, 600): data += pg.evaluate(PROBE, [f0, min(N, f0 + 600)])
        if "--sfx" in sys.argv:
            sfx = pg.evaluate("window.SFXLIST()"); (HERE / "out" / f"sfx_{fmt}.json").write_text(json.dumps(sfx)); print("sfx events:", len(sfx))
        b.close()
    # 1: outside the frame
    outside = defaultdict(list)
    for f, rows in enumerate(data):
        for i, l, t, r, bt, o in rows:
            if l < -0.5 or t < -0.5 or r > W + 0.5 or bt > H + 0.5: outside[i].append(f)
    # 2: overlaps
    overlap = defaultdict(list)
    for f, rows in enumerate(data):
        rs = [(i, l + (r - l) * 0.02, t + (bt - t) * 0.12, r - (r - l) * 0.02, bt - (bt - t) * 0.12, o) for i, l, t, r, bt, o in rows if o > 0.05]
        for a in range(len(rs)):
            for c in range(a + 1, len(rs)):
                A, B = rs[a], rs[c]
                if min(A[3], B[3]) - max(A[1], B[1]) > 1.5 and min(A[4], B[4]) - max(A[2], B[2]) > 1.5: overlap[(A[0], B[0])].append(f)
    # 3: holds (stable = opacity >= .95 and the box moved <= .3 px since the previous frame)
    last = {}; stable = defaultdict(int); runs = defaultdict(list); epi_start = {}
    cur = defaultdict(int); epi = defaultdict(lambda: [0, 0])      # per element: current stable run, best stable run in the current episode
    viol = []
    prev_vis = set()
    for f, rows in enumerate(data + [[]]):
        now = {}
        for i, l, t, r, bt, o in rows:
            if o >= 0.95: now[i] = (l, t, r, bt)
        for i in set(now) | prev_vis:
            if i in now:
                if i in last and i in prev_vis and max(abs(a - b_) for a, b_ in zip(now[i], last[i])) <= 0.3: cur[i] += 1
                else: cur[i] = 1
                epi[i][1] = max(epi[i][1], cur[i]); epi[i][0] += 0
            else:                                              # episode ended
                if i in prev_vis:
                    m = meta[i]; words = m["words"]; need = float(m["need"]) if m["need"] else 0.3 * words + 0.5
                    held = epi[i][1] / FPS
                    if held + 1e-6 < need: viol.append((i, m["text"], words, round(need, 2), round(held, 2), f))
                    epi[i] = [0, 0]; cur[i] = 0
        last.update(now); prev_vis = set(now)
    n_out, n_ovl, n_hold, n_err = len(outside), len(overlap), len(viol), len(errs)
    print(f"[{fmt}] frames {N}, text elements {len(meta)}")
    print(f"1 text outside frame:        {n_out}")
    for i, fs in list(outside.items())[:8]: print("   ", meta[i]["text"], "frames", fs[0], "-", fs[-1], f"({len(fs)})")
    print(f"2 text overlaps:             {n_ovl}")
    for (a, c), fs in list(overlap.items())[:12]: print("   ", repr(meta[a]["text"][:30]), "x", repr(meta[c]["text"][:30]), "frames", fs[0], "-", fs[-1], f"({len(fs)})")
    print(f"3 text held too briefly:     {n_hold}")
    for v in viol[:14]: print("   ", v)
    print(f"6 runtime/render errors:     {n_err}", errs[:3])
    (HERE / "out" / f"counters_{fmt}.json").write_text(json.dumps({"outside": n_out, "overlap": n_ovl, "hold": n_hold, "errors": n_err}))
    sys.exit(1 if (n_out or n_ovl or n_hold or n_err) else 0)

if __name__ == "__main__":
    main()
