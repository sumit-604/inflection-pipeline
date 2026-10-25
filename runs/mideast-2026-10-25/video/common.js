/* common.js - framework shared by the long video, the Short and the thumbnail.
   Render contract: window.renderAt(t) draws exactly the frame for time t (seconds). Everything is a pure function of t.
   No Date.now, no timers, no CSS transitions, no unseeded Math.random. Animated properties: transform and opacity only
   (plus text content of the one price counter, which is also a pure function of t). */
"use strict";
const NS = "http://www.w3.org/2000/svg";
const FPS = TL.fps, W = TL.W, H = TL.H;
const COL = { cream: "#F4EFE6", ink: "#16202A", orange: "#F08A4B", burnt: "#B4481A", white: "#FFFFFF", card: "#16202A", card2: "#1F2D3A" };
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const lerp = (a, b, t) => a + (b - a) * t;

/* seeded generator (mulberry32); used only while building scenes, never per frame */
function rng(seed) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }

/* ---------- easing: the job's curves ---------- */
function bez(x1, y1, x2, y2) {
  const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx, cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
  const X = t => ((ax * t + bx) * t + cx) * t, Y = t => ((ay * t + by) * t + cy) * t, D = t => (3 * ax * t + 2 * bx) * t + cx;
  return x => {
    if (x <= 0) return 0; if (x >= 1) return 1;
    let t = x;
    for (let i = 0; i < 8; i++) { const e = X(t) - x; if (Math.abs(e) < 1e-7) return Y(t); const d = D(t); if (Math.abs(d) < 1e-6) break; t -= e / d; }
    let lo = 0, hi = 1; t = x;
    for (let i = 0; i < 40; i++) { const e = X(t); if (Math.abs(e - x) < 1e-7) break; if (e < x) lo = t; else hi = t; t = (lo + hi) / 2; }
    return Y(t);
  };
}
const EASE = { enter: bez(0.16, 1, 0.3, 1), move: bez(0.76, 0, 0.24, 1), exit: bez(0.7, 0, 0.84, 0), lin: x => x };
/* damped spring step response over progress p in 0..1 (settles by p = 1); zeta .8 = premium, .55 = playful pop */
function springEase(zeta, settle = 4.6) {
  const w = settle / zeta, wd = w * Math.sqrt(1 - zeta * zeta), k = zeta / Math.sqrt(1 - zeta * zeta);
  return p => p <= 0 ? 0 : p >= 1 ? 1 : 1 - Math.exp(-zeta * w * p) * (Math.cos(wd * p) + k * Math.sin(wd * p));
}
EASE.spring8 = springEase(0.8); EASE.pop = springEase(0.55);

/* ---------- svg helpers ---------- */
function el(tag, attrs, parent) { const e = document.createElementNS(NS, tag); if (attrs) for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
const g = (parent, attrs) => el("g", attrs, parent);
const rect = (p, x, y, w, h, fill, rx, extra) => el("rect", Object.assign({ x, y, width: w, height: h, fill, rx: rx || 0 }, extra || {}), p);
const circ = (p, x, y, r, fill, extra) => el("circle", Object.assign({ cx: x, cy: y, r, fill }, extra || {}), p);
const path = (p, d, fill, extra) => el("path", Object.assign({ d, fill: fill || "none" }, extra || {}), p);
const line = (p, x1, y1, x2, y2, stroke, sw, extra) => el("line", Object.assign({ x1, y1, x2, y2, stroke, "stroke-width": sw, "stroke-linecap": "round" }, extra || {}), p);
const poly = (p, pts, fill, extra) => el("polygon", Object.assign({ points: pts.map(q => q.join(",")).join(" "), fill }, extra || {}), p);
function star(cx, cy, r, rot = -90, n = 5, inner = 0.382) { const out = []; for (let i = 0; i < n * 2; i++) { const a = (rot + i * 180 / n) * Math.PI / 180, rr = i % 2 ? r * inner : r; out.push([+(cx + rr * Math.cos(a)).toFixed(2), +(cy + rr * Math.sin(a)).toFixed(2)]); } return out; }

/* ---------- text ----------
   o: size, fam ('A' Archivo | 'P' Plex), w weight, fill, anchor, lh (line height), ls (letter-spacing), id.
   str: string or array of lines; a line may be [[text, {fill, fam, w, size}], ...] for coloured runs (tspans). Baseline of line 1 is y=0. */
let TID = 0;
function mkText(parent, str, o = {}) {
  const t = el("text", { x: 0, y: 0, "font-family": o.fam === "P" ? "'IBM Plex Sans', sans-serif" : "'Archivo', sans-serif", "font-size": o.size || 40, "font-weight": o.w || (o.fam === "P" ? 500 : 900),
    fill: o.fill || COL.cream, "text-anchor": o.anchor || "start" }, parent);
  if (o.ls) t.setAttribute("letter-spacing", o.ls);
  const lines = Array.isArray(str) ? str : [str];
  lines.forEach((ln, i) => {
    const runs = Array.isArray(ln) ? ln : [[ln, {}]];
    runs.forEach((r, j) => {
      const s = el("tspan", {}, t); s.textContent = r[0]; const ro = r[1] || {};
      if (j === 0) { s.setAttribute("x", 0); if (i > 0) s.setAttribute("dy", (o.lh || (o.size || 40) * 1.2)); }
      if (ro.fill) s.setAttribute("fill", ro.fill);
      if (ro.fam) s.setAttribute("font-family", ro.fam === "P" ? "'IBM Plex Sans', sans-serif" : "'Archivo', sans-serif");
      if (ro.w) s.setAttribute("font-weight", ro.w);
      if (ro.size) s.setAttribute("font-size", ro.size);
    });
  });
  const flat = lines.map(l => Array.isArray(l) ? l.map(r => r[0]).join("") : l).join(" ");
  if ((o.anchor === "middle" || o.anchor === "end") && lines.length === 1 && (!Array.isArray(lines[0]) || lines[0].length === 1) && typeof measure === "function") {
    // resting text is snapped to whole pixels: centred/right-aligned single runs become left-anchored at a rounded x
    const w = measure(flat, o.size || 40, o.fam === "P" ? "P" : "A", o.w || (o.fam === "P" ? 500 : 900)), x0 = -Math.round(o.anchor === "middle" ? w / 2 : w);
    t.setAttribute("text-anchor", "start"); t.setAttribute("x", x0); t.querySelectorAll("tspan").forEach(s => s.setAttribute("x", x0));
  }
  t.setAttribute("data-os", o.id || ("os" + (++TID))); t.setAttribute("data-words", o.words != null ? o.words : flat.trim().split(/\s+/).length);
  t.setAttribute("data-text", flat);
  return t;
}

/* ---------- sprite: a <g> whose transform/opacity are pure functions of local time ---------- */
const ORDER = ["x", "y", "sx", "sy", "r", "o"];
class Sp {
  constructor(parent, x = 0, y = 0, s = 1, r = 0) { this.g = g(parent); this.bx = x; this.by = y; this.bs = s; this.br = r; this.tracks = { x: [], y: [], sx: [], sy: [], r: [], o: [] }; this.fn = null; this.vis = true; this.apply(-1e9); }
  /* track: prop, start time, duration, from, to, ease. x,y,r,o absolute; sx,sy are multipliers of the base scale */
  to(prop, t0, d, from, to, ease = EASE.enter) { this.tracks[prop].push({ t0, d, from, to, ease }); return this; }
  val(prop, lt) {
    const tr = this.tracks[prop]; let v = prop === "x" ? this.bx : prop === "y" ? this.by : prop === "r" ? this.br : prop === "o" ? (tr.length ? tr[0].from : 1) : 1;
    for (let i = 0; i < tr.length; i++) {
      const k = tr[i];
      if (lt < k.t0) { if (i === 0) v = k.from; break; }
      const p = clamp((lt - k.t0) / k.d); v = p >= 1 ? k.to : lerp(k.from, k.to, k.ease(p));
    }
    return v;
  }
  apply(lt) {
    let x, y, sx, sy, r, o;
    if (this.fn) { const s = this.fn(lt); x = s.x != null ? s.x : this.bx; y = s.y != null ? s.y : this.by; sx = s.sx != null ? s.sx : 1; sy = s.sy != null ? s.sy : sx; r = s.r != null ? s.r : this.br; o = s.o != null ? s.o : 1; }
    else { x = this.val("x", lt); y = this.val("y", lt); sx = this.val("sx", lt); sy = this.val("sy", lt); r = this.val("r", lt); o = this.val("o", lt); }
    const rn = v => Math.abs(v - Math.round(v)) < 1e-4 ? String(Math.round(v)) : v.toFixed(3);
    const vis = o > 0.001 && sx !== 0;
    if (vis !== this.vis) { this.g.setAttribute("display", vis ? "inline" : "none"); this.vis = vis; }
    if (!vis) return;
    this.g.setAttribute("transform", `translate(${rn(x)},${rn(y)})` + (r ? ` rotate(${rn(r)})` : "") + ` scale(${rn(sx * this.bs)},${rn(sy * this.bs)})`);
    this.g.setAttribute("opacity", o >= 0.999 ? "1" : o.toFixed(3));
  }
}

/* entrance / exit presets. Entrances use the job's entrance curve (no overshoot on text); pops use a 0.55 spring on scale only. */
function enter(sp, t, kind = "zoom", d = 0.6) {
  const E = EASE.enter;
  switch (kind) {
    case "slideL": sp.to("x", t, d, sp.bx - 70, sp.bx, E).to("o", t, d * 0.6, 0, 1, E); break;
    case "slideR": sp.to("x", t, d, sp.bx + 70, sp.bx, E).to("o", t, d * 0.6, 0, 1, E); break;
    case "drop": sp.to("y", t, d, sp.by - 48, sp.by, E).to("o", t, d * 0.6, 0, 1, E); break;
    case "rise": sp.to("y", t, d, sp.by + 40, sp.by, E).to("o", t, d * 0.6, 0, 1, E); break;
    case "zoom": sp.to("sx", t, d, 0.86, 1, E).to("sy", t, d, 0.86, 1, E).to("o", t, d * 0.6, 0, 1, E); break;
    case "pop": sp.to("sx", t, d + 0.2, 0.3, 1, EASE.pop).to("sy", t, d + 0.2, 0.3, 1, EASE.pop).to("o", t, 0.12, 0, 1, EASE.lin); break;
    case "spring": sp.to("sx", t, d + 0.1, 0.8, 1, EASE.spring8).to("sy", t, d + 0.1, 0.8, 1, EASE.spring8).to("o", t, d * 0.5, 0, 1, E); break;
    case "stretchX": sp.to("sx", t, d, 0.001, 1, EASE.move).to("o", t, 0.05, 0, 1, EASE.lin); break;
    case "stretchY": sp.to("sy", t, d, 0.001, 1, EASE.move).to("o", t, 0.05, 0, 1, EASE.lin); break;
    case "cut": sp.to("o", t, 0.001, 0, 1, EASE.lin); break;
    default: throw new Error("enter " + kind);
  }
  return sp;
}
function exitSp(sp, t, d = 0.3) { sp.to("o", t, d, 1, 0, EASE.exit); return sp; }
function moveTo(sp, t, d, x, y, ease = EASE.move) { const fx = sp.val("x", t), fy = sp.val("y", t); if (x != null) sp.to("x", t, d, fx, x, ease); if (y != null) sp.to("y", t, d, fy, y, ease); return sp; }

/* ---------- scenes ---------- */
const SCENE_LIST = []; const SFX = []; let CUR = null;
function normW(s) { return s.toLowerCase().replace(/[^a-z0-9%$']/g, ""); }
function defScene(id, build) {
  const meta = TL.scenes.find(s => s.id === id); if (!meta) throw new Error("no scene " + id);
  const root = document.getElementById("root"); const gs = g(root, { id: "scene" + id, display: "none" });
  const sc = { id, meta, g: gs, sprites: [], updaters: [], t0: meta.f0 / FPS, t1: meta.f1 / FPS, dur: (meta.f1 - meta.f0) / FPS };
  const sents = meta.sentences.map(s => ({ t0: s.t0 - meta.t0, t1: s.t1 - meta.t0, words: s.words.map(w => ({ w: normW(w.w), t0: w.t0 - meta.t0, t1: w.t1 - meta.t0 })) }));
  const ctx = {
    id, g: gs, sc, S: sents, dur: sc.dur, bg: meta.bg, bgname: meta.bgname,
    /* local time of the first word of `phrase` inside sentence i (word-level, proportional to phonemes) */
    cue(i, phrase) {
      const want = phrase.split(/\s+/).map(normW), ws = sents[i].words;
      for (let k = 0; k + want.length <= ws.length; k++) if (want.every((x, j) => ws[k + j].w === x)) return ws[k].t0;
      throw new Error(`cue not found: s${id} sentence ${i} '${phrase}'`);
    },
    sp(parent, x, y, s, r) { const p = new Sp(parent || gs, x, y, s, r); sc.sprites.push(p); return p; },
    text(str, x, y, o = {}, parent) { const p = ctx.sp(parent, x, y, o.s || 1); mkText(p.g, str, o); return p; },
    sfx(kind, t) { SFX.push({ kind, t: +(sc.t0 + t).toFixed(4), scene: id }); },
    update(fn) { sc.updaters.push(fn); },
  };
  CUR = sc; rect(gs, 0, 0, W, H, meta.bg); build(ctx); CUR = null; SCENE_LIST.push(sc);
  sc.sprites.forEach(p => p.apply(-1e9));
}

/* ---------- captions: burned in, white text on a semi-transparent dark band, at most two lines ---------- */
function buildCaptions(root, geo) {
  const band = g(root, { id: "captions" });
  const pages = TL.captions.map((c, i) => {
    const pg = g(band, { display: "none" }); rect(pg, geo.x, geo.y, geo.w, geo.h, "#0B1218", geo.r || 14, { opacity: 0.78 });
    const one = c.lines.length === 1; const y0 = geo.y + geo.h / 2 + (one ? geo.size * 0.36 : -geo.lh / 2 + geo.size * 0.36);
    const t = el("text", { x: geo.x + geo.pad, y: Math.round(y0), "font-family": "'IBM Plex Sans', sans-serif", "font-size": geo.size, "font-weight": 500, fill: "#FFFFFF", "data-cap": i, "data-words": c.n, "data-need": c.need }, pg);
    c.lines.forEach((ln, j) => { const s = el("tspan", { x: geo.x + geo.pad }, t); if (j) s.setAttribute("dy", geo.lh); s.textContent = ln; });
    return { g: pg, t0: c.t0, t1: c.t1, on: false };
  });
  return pages;
}
function drawCaptions(pages, t) { pages.forEach(p => { const on = t >= p.t0 - 1e-6 && t < p.t1 - 1e-6; if (on !== p.on) { p.g.setAttribute("display", on ? "inline" : "none"); p.on = on; } }); }

/* ---------- renderAt ---------- */
let CAPS = null, CAPSTATE = null;
function setupRender(capGeo) {
  CAPS = buildCaptions(document.getElementById("root"), capGeo);
  window.renderAt = function (t) {
    t = Math.max(0, Math.min(t, TL.total - 1e-6));
    let cur = null;
    for (const sc of SCENE_LIST) {
      const on = t >= sc.t0 - 1e-4 && t < sc.t1 - 1e-4;   // scene edges are whole frames; the tolerance covers float error
      if (on) cur = sc;
      if (on !== !!sc.shown) { sc.g.setAttribute("display", on ? "inline" : "none"); sc.shown = on; }
    }
    if (cur) { const lt = t - cur.t0; cur.sprites.forEach(p => p.apply(lt)); cur.updaters.forEach(f => f(lt)); }
    drawCaptions(CAPS, t);
    return cur ? cur.id : -1;
  };
  window.renderFrame = f => window.renderAt(f / FPS);   // frame f is exactly time f / 30
  window.SFXLIST = () => SFX.slice().sort((a, b) => a.t - b.t);
  window.TOTAL_FRAMES = TL.frames;
}
function ready(cb) { document.fonts.ready.then(() => Promise.all(["800 40px Archivo", "900 40px Archivo", "400 20px 'IBM Plex Sans'", "500 20px 'IBM Plex Sans'", "600 20px 'IBM Plex Sans'"].map(f => document.fonts.load(f)))).then(() => { cb(); window.renderAt(0); window.READY = true; }); }
