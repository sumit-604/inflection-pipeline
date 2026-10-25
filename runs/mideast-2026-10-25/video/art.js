/* art.js - drawing library: one reusable Middle East map, flags, icons, characters. All flat 2D, generic people only. */
"use strict";
const PAL = { navy: "#16202A", sand: "#F4EFE6", teal: "#0F4C4C", orange: "#B4481A", olive: "#4A5D23", plum: "#5B2A4E", slate: "#2F4A6D", acc: "#F08A4B", cream: "#F4EFE6", red: "#D8352A", sea: "#2B5C7A" };

/* text measuring (canvas) so pills and cards fit their text; fonts are loaded before scenes are built */
const _cv = document.createElement("canvas").getContext("2d");
function measure(str, size, fam = "P", w = 600) { _cv.font = `${w} ${size}px ${fam === "P" ? "'IBM Plex Sans'" : "'Archivo'"}`; return _cv.measureText(str).width; }

/* ---------------- the map asset (one definition, reused with <use>) ---------------- */
function mapDefs() {
  const root = document.getElementById("root"); if (document.getElementById("land")) return;
  const defs = el("defs", {}, root); root.insertBefore(defs, root.firstChild);
  const land = el("g", { id: "land" }, defs);
  MAPDATA.countries.forEach(c => el("path", { d: c.d, "vector-effect": "non-scaling-stroke", "stroke-linejoin": "round" }, land));
  const iran = MAPDATA.countries.find(c => c.name === "Iran"); el("path", { id: "iranShape", d: iran.d, "vector-effect": "non-scaling-stroke", "stroke-linejoin": "round" }, defs);
  const sa = MAPDATA.countries.find(c => c.name === "Saudi Arabia"); el("path", { id: "saudiShape", d: sa.d, "vector-effect": "non-scaling-stroke", "stroke-linejoin": "round" }, defs);
  el("clipPath", { id: "mapClip" }, defs).appendChild(el("rect", { x: 0, y: 0, width: MAPDATA.W, height: MAPDATA.H }));
}
/* lon/lat -> map units */
function LL(lon, lat) { return [(lon - MAPDATA.lon0) * MAPDATA.cx * MAPDATA.k, (MAPDATA.lat1 - lat) * MAPDATA.k]; }
/* draws the map into `parent` (local units: MAPDATA.W x MAPDATA.H). o: land, border, iran (fill), iranStroke, saudi (fill) */
function drawMap(parent, o = {}) {
  mapDefs(); const m = g(parent, { "clip-path": "url(#mapClip)" });
  el("use", { href: "#land", fill: o.land, stroke: o.border, "stroke-width": o.bw || 1 }, m);
  if (o.iran) el("use", { href: "#iranShape", fill: o.iran, stroke: o.iranStroke || o.border, "stroke-width": 2.5 }, m);
  if (o.saudi) el("use", { href: "#saudiShape", fill: o.saudi, stroke: o.border, "stroke-width": 1.5 }, m);
  return m;
}
/* label chip: dark pill with cream text, text centred on (0,0); returns the group (add inside a sprite) */
function chip(parent, str, o = {}) {
  const size = o.size || 26, w = measure(str, size, "P", 600) + 28, h = size + 18;
  const gg = g(parent); rect(gg, -w / 2, -h / 2, w, h, o.fill || PAL.navy, h / 2, { opacity: o.op || 0.94 });
  const t = mkText(gg, str, { fam: "P", w: 600, size, fill: o.color || PAL.cream, anchor: "middle", id: o.id }); t.setAttribute("y", Math.round(size * 0.35)); return gg;
}

/* ---------------- flags (simple, generic) ---------------- */
let FID = 0;
function flag(parent, kind, w) {
  const h = Math.round(w * 2 / 3), gg = g(parent), id = "fc" + (++FID);
  el("clipPath", { id }, el("defs", {}, gg)).appendChild(el("rect", { x: -w / 2, y: -h / 2, width: w, height: h, rx: Math.round(w * 0.06) }));
  const f = g(gg, { "clip-path": `url(#${id})` }), x0 = -w / 2, y0 = -h / 2;
  if (kind === "us") {
    rect(f, x0, y0, w, h, "#FFFFFF");
    for (let i = 0; i < 7; i++) rect(f, x0, y0 + i * 2 * h / 13, w, h / 13, "#B22234");
    const cw = w * 0.42, ch = 7 * h / 13; rect(f, x0, y0, cw, ch, "#3C3B6E");
    for (let r = 0; r < 4; r++) for (let c = 0; c < 5; c++) circ(f, x0 + cw * (c + 0.7) / 5.4, y0 + ch * (r + 0.7) / 4.4, Math.max(1.2, w * 0.011), "#FFFFFF");
  } else if (kind === "ir") {
    rect(f, x0, y0, w, h / 3, "#239F40"); rect(f, x0, y0 + h / 3, w, h / 3, "#FFFFFF"); rect(f, x0, y0 + 2 * h / 3, w, h / 3 + 1, "#DA0000");
    const r = h * 0.1; el("circle", { cx: 0, cy: 0, r, fill: "none", stroke: "#DA0000", "stroke-width": Math.max(2, w * 0.016) }, f); line(f, 0, -r * 1.25, 0, r * 1.25, "#DA0000", Math.max(2, w * 0.016));
  } else if (kind === "cn") {
    rect(f, x0, y0, w, h, "#DE2910"); poly(f, star(x0 + w * 0.17, y0 + h * 0.25, h * 0.19), "#FFDE00");
    [[0.34, 0.1], [0.4, 0.2], [0.4, 0.33], [0.34, 0.43]].forEach(([a, b]) => poly(f, star(x0 + w * a, y0 + h * b, h * 0.06), "#FFDE00"));
  } else if (kind === "il") {
    rect(f, x0, y0, w, h, "#FFFFFF"); rect(f, x0, y0 + h * 0.1, w, h * 0.12, "#0038B8"); rect(f, x0, y0 + h * 0.78, w, h * 0.12, "#0038B8");
    const r = h * 0.2, sw = Math.max(2, w * 0.016);
    poly(f, [[0, -r], [r * 0.87, r * 0.5], [-r * 0.87, r * 0.5]], "none", { stroke: "#0038B8", "stroke-width": sw }); poly(f, [[0, r], [r * 0.87, -r * 0.5], [-r * 0.87, -r * 0.5]], "none", { stroke: "#0038B8", "stroke-width": sw });
  }
  rect(gg, x0, y0, w, h, "none", Math.round(w * 0.06), { stroke: "rgba(0,0,0,0.35)", "stroke-width": 2 });
  return gg;
}

/* ---------------- straight-segment "draw" lines (scaleX only, so only transform animates) ---------------- */
/* pts: [[x,y],...] in the parent's coordinates. The whole polyline is drawn by one eased progress (no linear motion),
   segment by segment. o.exitAt: time at which the line dims to o.dim opacity. */
function polyDraw(ctx, parent, pts, color, sw, t0, dur, o = {}) {
  const lens = []; let tot = 0; for (let i = 1; i < pts.length; i++) { const l = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); lens.push(l); tot += l; }
  const out = []; let acc = 0; const ease = o.ease || EASE.move;
  for (let i = 1; i < pts.length; i++) {
    const [x1, y1] = pts[i - 1], [x2, y2] = pts[i], l = lens[i - 1], ang = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI, a0 = acc;
    const sp = ctx.sp(parent, x1, y1, 1, ang); line(sp.g, 0, 0, l, 0, color, sw, o.extra);
    sp.fn = lt => {
      const s = clamp((ease(clamp((lt - t0) / dur)) * tot - a0) / l);
      let op = s > 0 ? 1 : 0; if (op && o.exitAt != null) op = lerp(1, o.dim == null ? 0 : o.dim, EASE.exit(clamp((lt - o.exitAt) / (o.exitDur || 0.4))));
      return { x: x1, y: y1, r: ang, sx: Math.max(s, 0.001), sy: 1, o: op };
    };
    out.push(sp); acc += l;
  }
  return out;
}
