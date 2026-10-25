/* long2.js - scenes 4 to 7 and their art. */
"use strict";

/* ---------- small art pieces (flat 2D, generic) ---------- */
function atomIcon(parent, R, col, nuc) {
  const gg = g(parent);
  [0, 60, 120].forEach(a => el("ellipse", { cx: 0, cy: 0, rx: R, ry: R * 0.38, fill: "none", stroke: col, "stroke-width": R * 0.07, transform: `rotate(${a})` }, gg));
  circ(gg, 0, 0, R * 0.2, nuc || col);
  [0, 60, 120].forEach((a, i) => { const e = g(gg, { transform: `rotate(${a})` }); circ(e, R * Math.cos(i * 2.1), R * 0.38 * Math.sin(i * 2.1), R * 0.085, col); });
  return gg;
}
function barrelIcon(parent, sc, body) {
  const gg = g(parent, { transform: `scale(${sc || 1})` });
  rect(gg, -70, -100, 140, 200, body || "#16202A", 28); rect(gg, -70, -62, 140, 14, "#F4EFE6", 0); rect(gg, -70, 48, 140, 14, "#F4EFE6", 0);
  rect(gg, -58, -92, 18, 184, "#2D3F52", 9);
  path(gg, "M0,-30 C22,6 26,22 0,38 C-26,22 -22,6 0,-30Z", "#F08A4B");
  return gg;
}
function wheelIcon(parent, R) {
  const gg = g(parent);
  for (let i = 0; i < 8; i++) { const a = i * 45; const sp = g(gg, { transform: `rotate(${a})` }); line(sp, 0, 0, R * 1.28, 0, "#F4EFE6", R * 0.085); circ(sp, R * 1.28, 0, R * 0.1, "#F4EFE6"); }
  circ(gg, 0, 0, R, "none", { stroke: "#F4EFE6", "stroke-width": R * 0.1 }); circ(gg, 0, 0, R * 0.26, "#F4EFE6"); circ(gg, 0, 0, R * 0.1, "#16202A");
  return gg;
}
function tanker(parent, hull, deck, flagKind) {
  const gg = g(parent);
  path(gg, "M-160,0 L160,0 L128,46 L-140,46 Z", hull);
  [-90, -30, 30, 90].forEach(x => rect(gg, x - 25, -30, 50, 30, deck, 14));
  rect(gg, -160, -50, 54, 50, "#EDE6D6", 6); rect(gg, -150, -40, 34, 14, "#16202A", 3); rect(gg, -138, -76, 18, 26, "#C9C0AA", 3);
  if (flagKind) { line(gg, 140, 0, 140, -64, "#16202A", 4); const f = g(gg, { transform: "translate(166,-52)" }); flag(f, flagKind, 48); }
  return gg;
}
function boatIcon(parent) {
  const gg = g(parent);
  path(gg, "M-70,0 L60,0 L84,-20 L-82,-20 Z", "#16202A"); path(gg, "M-70,0 L60,0 L40,22 L-56,22 Z", "#8C2F12");
  rect(gg, -20, -52, 46, 32, "#EDE6D6", 6); rect(gg, -10, -44, 26, 14, "#16202A", 3); line(gg, 40, -20, 40, -66, "#16202A", 4);
  return gg;
}
function mineIcon(parent) {
  const gg = g(parent);
  for (let i = 0; i < 8; i++) { const a = i * 45; const s = g(gg, { transform: `rotate(${a})` }); rect(s, -5, -42, 10, 18, "#16202A", 3); }
  circ(gg, 0, 0, 28, "#2A3440", { stroke: "#16202A", "stroke-width": 4 }); circ(gg, -9, -9, 6, "#5B6B7A"); line(gg, 0, 28, 0, 70, "#16202A", 4);
  return gg;
}
function markerX(parent, r) {
  const gg = g(parent); circ(gg, 0, 0, r, "#D8352A", { stroke: "#FFFFFF", "stroke-width": 5 }); line(gg, -r * 0.4, -r * 0.4, r * 0.4, r * 0.4, "#FFFFFF", r * 0.2); line(gg, r * 0.4, -r * 0.4, -r * 0.4, r * 0.4, "#FFFFFF", r * 0.2); return gg;
}
function navyShip(parent) {
  const gg = g(parent);
  path(gg, "M-180,0 L190,0 L150,44 L-150,44 Z", "#7F8C99"); rect(gg, -180, -8, 370, 10, "#5B6875", 0);
  rect(gg, -90, -50, 150, 50, "#A3AEB9", 6); rect(gg, -40, -92, 70, 44, "#B9C2CB", 6); line(gg, -5, -92, -5, -140, "#16202A", 5); rect(gg, -34, -124, 58, 8, "#16202A", 4);
  rect(gg, 90, -22, 56, 22, "#5B6875", 4); line(gg, 146, -14, 190, -26, "#16202A", 7);
  [-70, -40, -10, 20, 50].forEach(x => rect(gg, x, -34, 16, 12, "#16202A", 2));
  line(gg, 20, -140, 20, -164, "#16202A", 3); const f = g(gg, { transform: "translate(52,-156)" }); flag(f, "us", 44);
  return gg;
}
function planeIcon(parent, s) {
  const gg = g(parent, { transform: `scale(${s || 1})` });
  path(gg, "M0,-26 C5,-26 7,-20 7,-12 L7,-4 L28,8 L28,14 L7,8 L7,20 L14,26 L14,30 L0,27 L-14,30 L-14,26 L-7,20 L-7,8 L-28,14 L-28,8 L-7,-4 L-7,-12 C-7,-20 -5,-26 0,-26Z", "#F4EFE6");
  return gg;
}
function waves(parent, x, w, y, col, n = 7, amp = 6) { let d = ""; for (let i = 0; i < n; i++) { const x0 = x + i * w / n; d += `M${x0.toFixed(1)},${y} q${(w / n / 4).toFixed(1)},${-amp} ${(w / n / 2).toFixed(1)},0 t${(w / n / 2).toFixed(1)},0 `; } return path(parent, d, "none", { stroke: col, "stroke-width": 4, "stroke-linecap": "round" }); }
function dark(c, x, y, w, h, t, kind = "zoom", fill = PAL.navy, r = 22) { const s = c.sp(null, x, y); rect(s.g, 0, 0, w, h, fill, r); enter(s, t, kind, 0.55); return s; }

function buildLong2() {
  const CR = COL.cream;

  /* ============ 4 MORE THAN ONE MOTIVE (burnt orange; numbers and text cream) ============ */
  defScene(4, c => {
    const cells = [[96, 90], [1000, 90], [96, 490], [1000, 490]];
    const T = [c.S[0].t0 + 0.1, c.S[2].t0 + 0.1, c.S[4].t0 + 0.1, c.S[5].t0 + 0.1];
    const labels = [["Nuclear", "fears"], ["China's", "cheap oil"], ["Control of", "Hormuz"], ["Israel's", "goals"]];
    const kinds = ["pop", "slideR", "zoom", "pop"];
    cells.forEach(([x, y], i) => {
      const ic = c.sp(null, x + 180, y + 190, 1); const gg = g(ic.g);
      if (i === 0) { const a = c.sp(ic.g, 0, 0, 1); atomIcon(a.g, 150, CR, PAL.navy); a.fn = lt => ({ r: lt * 24 }); }
      if (i === 1) { barrelIcon(gg, 1.45); const f = g(gg, { transform: "translate(104,-130)" }); flag(f, "cn", 136); }
      if (i === 2) {
        const [hx, hy] = LL(56.3, 26.5), s = 5.2; const cid = "wheelclip"; el("clipPath", { id: cid }, gg).appendChild(el("circle", { cx: 0, cy: 0, r: 128 }));
        circ(gg, 0, 0, 128, PAL.navy); const mm = g(gg, { "clip-path": `url(#${cid})` }); const mg = g(mm, { transform: `translate(${-hx * s},${-hy * s}) scale(${s})` });
        el("use", { href: "#land", fill: "#3F566B", stroke: "#8FA3B5", "stroke-width": 1 }, mg); wheelIcon(gg, 132); circ(gg, 0, 0, 14, PAL.acc);
      }
      if (i === 3) flag(gg, "il", 330);
      enter(ic, T[i], kinds[i], 0.6); c.sfx("pop", T[i]);
      const t = c.text(labels[i], x + 400, y + 160, { size: 70, lh: 78, fill: CR, id: "motive" + i }); enter(t, T[i] + 0.25, "slideL", 0.6);
    });
  });

  /* ============ 5 TWO BLOCKADES (olive) ============ */
  defScene(5, c => {
    // map panel (the one map asset, zoomed on Hormuz)
    const px0 = 96, py0 = 100, pw = 604, ph = 760, ms = 1.55, [hx, hy] = LL(56.3, 26.5), mx = px0 + pw / 2 - ms * hx, my = py0 + 300 - ms * hy;
    const panel = c.sp(null, 0, 0); enter(panel, 0.0, "zoom", 0.7);
    const pid = "panelclip"; el("clipPath", { id: pid }, panel.g).appendChild(el("rect", { x: px0, y: py0, width: pw, height: ph, rx: 30 }));
    rect(panel.g, px0, py0, pw, ph, "#2A3912", 30); const pm = g(panel.g, { "clip-path": `url(#${pid})` }); const mg = g(pm, { transform: `translate(${mx},${my}) scale(${ms})` });
    drawMap(mg, { land: "#6C8239", border: "#8DA356", iran: "#7F9847", iranStroke: PAL.acc });
    const H0 = [Math.round(mx + ms * hx), Math.round(my + ms * hy)];
    pulse(c, H0[0], H0[1], c.S[0].t0 + 0.2, { r: 10, scale: 4.5 });
    mapLabel(c, "Strait of Hormuz", H0[0] + 40, H0[1] + 62, c.S[0].t0 + 0.5, "slideR");
    // headers and the two vignettes
    const vx = 780, vw = 1044, vh = 290; const SEA = "#1B3A4D";
    const h1 = c.text("Iran blocks the sea", vx, 156, { size: 56, fill: CR, id: "hdr1" }); enter(h1, c.S[1].t0 - 0.3, "slideL", 0.6);
    const v1 = c.sp(null, vx, 180); rect(v1.g, 0, 0, vw, vh, SEA, 26); waves(v1.g, 24, vw - 48, 236, "#3F7894", 12); enter(v1, c.S[1].t0 - 0.2, "zoom", 0.6);
    const tk = c.sp(v1.g, 640, 170, 0.95); tanker(tk.g, "#EDE6D6", "#B4481A"); enter(tk, c.S[1].t0 - 0.1, "rise", 0.6);
    const bt = c.sp(v1.g, -120, 210, 1); boatIcon(bt.g); const bA = c.S[1].t0 + 0.6; bt.to("x", bA, 1.5, -120, 350, EASE.move).to("o", bA, 0.1, 0, 1, EASE.lin);
    [[880, 190], [980, 212]].forEach(([x, y], i) => { const m = c.sp(v1.g, x, y, 1); mineIcon(m.g); const t0 = c.S[1].t0 + 1.4 + i * 0.2; m.fn = lt => { const p = clamp((lt - t0) / 0.6); return { x, y: y + (p >= 1 ? Math.sin(lt * 1.6 + i * 2) * 4 : 0), sx: lerp(0.3, 1, EASE.pop(p)), o: lt < t0 ? 0 : 1 }; }; c.sfx("pop", t0); });
    const mk = c.sp(v1.g, 640, 56, 1); markerX(mk.g, 30); enter(mk, c.S[1].t0 + 2.2, "pop", 0.4); c.sfx("alert", c.S[1].t0 + 2.2);
    const h2 = c.text("The US blocks Iran", vx, 540, { size: 56, fill: CR, id: "hdr2" }); enter(h2, c.S[2].t0 - 0.3, "slideL", 0.6);
    const v2 = c.sp(null, vx, 570); rect(v2.g, 0, 0, vw, vh, SEA, 26); waves(v2.g, 24, vw - 48, 246, "#3F7894", 12); enter(v2, c.S[2].t0 - 0.2, "zoom", 0.6);
    const ns = c.sp(v2.g, 1300, 190, 0.95); navyShip(ns.g); const nA = c.S[2].t0 + 0.1; ns.to("x", nA, 1.3, 1300, 760, EASE.move).to("o", nA, 0.1, 0, 1, EASE.lin);
    const it = c.sp(v2.g, 190, 196, 0.8); tanker(it.g, "#EDE6D6", "#2A7D3F", "ir"); const iA = c.S[2].t0 + 0.9;
    it.fn = lt => { const a = clamp((lt - iA) / 1.0), b = clamp((lt - (iA + 1.4)) / 0.5), d = clamp((lt - (iA + 1.9)) / 1.3); const x = lerp(190, 440, EASE.move(a)) + lerp(0, -250, EASE.move(d)); return { x, y: 196, sx: lerp(1, -1, EASE.move(b)), o: lt < iA - 0.4 ? 0 : clamp((lt - (iA - 0.4)) / 0.3) }; };
    c.sfx("whoosh", nA);
    // counter
    const cd = c.sp(null, 120, 668); rect(cd.g, 0, 0, 556, 170, PAL.navy, 26, { opacity: 0.97 }); const tC = c.S[4].t0 + 0.1; enter(cd, tC, "rise", 0.6);
    const num = c.text("$0.00", 36, 112, { size: 104, fill: PAL.acc, id: "price", words: 1 }, cd.g); const nEl = num.g.querySelector("text");
    const sub = c.text("Brent, 23 Oct", 40, 152, { fam: "P", w: 600, size: 32, fill: CR, id: "brentlbl" }, cd.g);
    c.update(lt => { const p = EASE.enter(clamp((lt - (tC + 0.25)) / 1.7)); const v = (116.72 * p).toFixed(2); const s = "$" + v; if (nEl.firstChild.firstChild.nodeValue !== s) nEl.firstChild.firstChild.nodeValue = s; });
    enter(num, tC + 0.05, "cut"); enter(sub, tC + 0.5, "slideL", 0.5);
    [0, 1, 2, 3, 4, 5].forEach(i => c.sfx("tick", tC + 0.3 + i * 0.28));
  });

  /* ============ 6 THE SAUDI FRONT (plum) ============ */
  defScene(6, c => {
    const ms = 1.25, [ax, ay] = LL(33, 32), mx = 790 - ms * ax, my = 90 - ms * ay, P = (lon, lat) => { const [x, y] = LL(lon, lat); return [Math.round(mx + ms * x), Math.round(my + ms * y)]; };
    const px0 = 760, py0 = 70, pw = 1090, ph = 810;
    const panel = c.sp(null, 0, 0); enter(panel, 0, "slideR", 0.8);
    el("clipPath", { id: "panel6" }, panel.g).appendChild(el("rect", { x: px0, y: py0, width: pw, height: ph, rx: 30 }));
    rect(panel.g, px0, py0, pw, ph, "#3C1832", 30); const pm = g(panel.g, { "clip-path": "url(#panel6)" }); const mg = g(pm, { transform: `translate(${mx},${my}) scale(${ms})` });
    drawMap(mg, { land: "#78456A", border: "#9A6A8D", saudi: "#8E5380", iran: "#78456A", iranStroke: "#9A6A8D" });
    const A = P(49.7, 25.9), M1 = P(46.6, 24.9), M2 = P(42.0, 24.1), Y = P(38.06, 24.09);
    const tP = c.S[0].t0 + 0.7;
    const src = c.sp(null, A[0], A[1]); circ(src.g, 0, 0, 14, PAL.acc, { stroke: PAL.navy, "stroke-width": 4 }); enter(src, tP - 0.2, "pop", 0.4);
    const pipe = polyDraw(c, null, [A, M1, M2, Y], PAL.acc, 9, tP, 1.8, { exitAt: c.S[3].t0 + 0.3, dim: 0.28, exitDur: 0.6 });
    const yb = c.sp(null, Y[0], Y[1]); circ(yb.g, 0, 0, 14, PAL.acc, { stroke: PAL.navy, "stroke-width": 4 }); enter(yb, tP + 1.6, "pop", 0.4); c.sfx("pop", tP + 1.7);
    mapLabel(c, "Yanbu", Y[0] - 20, Y[1] - 46, tP + 1.9, "drop");
    mapLabel(c, "Red Sea", P(36.2, 20.5)[0] - 10, P(36.2, 20.5)[1], c.S[0].t0 + 0.4, "slideL");
    mapLabel(c, "Yemen", P(46.5, 14.8)[0], P(46.5, 14.8)[1] + 4, c.S[1].t0, "slideR");
    mapLabel(c, "Saudi Arabia", P(45.5, 21.4)[0], P(45.5, 21.4)[1], c.S[0].t0 + 0.3, "zoom");
    // airports and arrows from Yemen
    const O = P(44.6, 15.5);
    const ap = [P(42.6, 16.9), P(39.17, 21.7)];
    const tA = c.cue(1, "airports");
    ap.forEach((p, i) => { const s = c.sp(null, p[0], p[1]); circ(s.g, 0, 0, 30, PAL.navy, { stroke: "#F4EFE6", "stroke-width": 4 }); planeIcon(s.g, 0.8); enter(s, tA - 0.3 + i * 0.15, "pop", 0.4); });
    const arrow = (to, t0, dur, col) => {
      const dx = to[0] - O[0], dy = to[1] - O[1], L = Math.hypot(dx, dy), ang = Math.atan2(dy, dx) * 180 / Math.PI, ux = dx / L, uy = dy / L;
      const sp = c.sp(null, O[0], O[1], 1, ang); line(sp.g, 0, 0, L - 40, 0, col, 7, { "stroke-dasharray": "18 12" }); poly(sp.g, [[L - 40, -14], [L - 6, 0], [L - 40, 14]], col);
      sp.fn = lt => { const p = EASE.move(clamp((lt - t0) / dur)); return { x: O[0], y: O[1], r: ang, sx: Math.max(p, 0.001), sy: 1, o: lt < t0 ? 0 : 1 }; };
      const ip = c.sp(null, to[0], to[1]); circ(ip.g, 0, 0, 12, "none", { stroke: "#F4EFE6", "stroke-width": 4, "vector-effect": "non-scaling-stroke" });
      ip.fn = lt => { const q = clamp((lt - (t0 + dur)) / 1.2); return { sx: lerp(0.5, 3.2, EASE.enter(q)), o: lt < t0 + dur ? 0 : 0.9 * (1 - q) }; };
      c.sfx("alert", t0); return sp;
    };
    arrow(ap[0], tA, 0.9, "#F4EFE6"); arrow(ap[1], tA + 0.5, 1.3, "#F4EFE6");
    arrow(P(41.2, 24.0), c.cue(2, "pipeline"), 1.5, "#F4EFE6");
    const tt = c.text(["Target: Saudi", "Arabia's bypass", "pipeline"], 96, 340, { size: 76, lh: 88, fill: CR, id: "target" }); enter(tt, c.S[2].t0 + 0.1, "slideL", 0.7);
    const bar = c.sp(null, 96, 560); rect(bar.g, 0, 0, 260, 12, PAL.acc, 2); enter(bar, c.S[2].t0 + 0.9, "stretchX", 0.6);
  });

  /* ============ 7 UNDER THE SEA (slate) ============ */
  defScene(7, c => {
    const sx0 = 96, sw = 1728, surf = 360, sbot = 880, SEAC = "#2E6A93";
    const sea = c.sp(null, 0, 0); enter(sea, 0.0, "rise", 0.8);
    rect(sea.g, sx0, surf, sw, sbot - surf, SEAC, 0); waves(sea.g, sx0, sw, surf, "#8FC1DE", 24, 7);
    path(sea.g, `M${sx0},${sbot - 100} C${sx0 + 300},${sbot - 120} ${sx0 + 500},${sbot - 84} ${sx0 + 800},${sbot - 108} S${sx0 + 1300},${sbot - 130} ${sx0 + sw},${sbot - 96} L${sx0 + sw},${sbot} L${sx0},${sbot} Z`, "#8B6B45");
    [[300, 850], [700, 860], [1100, 848], [1500, 862]].forEach(([x, y]) => circ(sea.g, x, y, 10, "#6F5334"));
    const yy = x => sbot - 108 + Math.sin(x / 260) * 8;
    const tc = c.S[1].t0 + 0.2; const xs = [sx0, 300, 520, 740, 880, 1100, 1320, 1540, sx0 + sw];
    [[0, PAL.acc, 6], [1, "#F4EFE6", 5], [2, "#E8B87D", 5]].forEach(([k, col, w]) => {
      polyDraw(c, null, xs.map(x => [x, Math.round(yy(x)) + 22 + k * 18]), col, w, tc + k * 0.25, 3.6);
    });
    mapLabel(c, "India", sx0 + 90, 640, tc, "pop", { size: 28 });
    mapLabel(c, "Europe", sx0 + sw - 100, 640, tc + 0.2, "pop", { size: 28 });
    const rs = c.sp(null, 880, 650); line(rs.g, 0, -80, 0, 70, "#F4EFE6", 4, { "stroke-dasharray": "10 10" });
    mapLabel(c, "Red Sea", 880, 570, c.S[2].t0 + 0.2, "drop", { size: 30 }); enter(rs, c.S[2].t0 + 0.2, "stretchY", 0.5);
    const BIG = 80, SM = 36;
    const l1 = [[["Red Sea: over", { fam: "P", w: 600, size: SM }]], [["90%", { fill: PAL.acc, size: BIG }], [" of Europe-Asia data", { fam: "P", w: 600, size: SM }]]];
    const l2 = [[["60%", { fill: PAL.acc, size: BIG }], [" of India's", { fam: "P", w: 600, size: SM }]], [["internet goes west", { fam: "P", w: 600, size: SM }]]];
    const w1 = Math.round(measure("90%", BIG, "A", 900) + measure(" of Europe-Asia data", SM) + 70), w2 = Math.round(measure("60%", BIG, "A", 900) + measure(" of India's", SM) + 70);
    dark(c, 96, 60, w1, 214, c.S[2].t0 - 0.1, "slideL"); const t1 = c.text(l1, 96 + 36, 60 + 66, { size: SM, lh: 78, fill: CR, id: "lab1" }); enter(t1, c.S[2].t0 + 0.25, "slideL", 0.6);
    const c2x = 96 + w1 + 40; dark(c, c2x, 60, w2, 214, c.S[3].t0 - 0.1, "slideR"); const t2 = c.text(l2, c2x + 36, 60 + 106, { size: SM, lh: 62, fill: CR, id: "lab2" }); enter(t2, c.S[3].t0 + 0.25, "slideR", 0.6);
    // repair ship waits beside a sign
    const tS = c.S[4].t0 + 0.2;
    const ship = c.sp(null, 1690, surf - 6, 0.85); path(ship.g, "M-130,0 L130,0 L100,40 L-110,40 Z", "#16202A"); rect(ship.g, -120, -6, 250, 10, "#B4481A"); rect(ship.g, -90, -54, 90, 48, "#EDE6D6", 6); rect(ship.g, -76, -42, 24, 18, "#16202A", 3); rect(ship.g, -40, -42, 24, 18, "#16202A", 3);
    line(ship.g, 40, -6, 40, -90, "#EDE6D6", 8); line(ship.g, 40, -90, 110, -60, "#EDE6D6", 8); line(ship.g, 110, -60, 110, -10, "#F08A4B", 3); circ(ship.g, 110, -6, 6, "#F08A4B");
    ship.to("x", tS, 1.4, 2200, 1690, EASE.move).to("o", tS, 0.1, 0, 1, EASE.lin); c.sfx("whoosh", tS);
    const sign = c.sp(null, 1440, surf - 6); line(sign.g, 0, 0, 0, -110, "#16202A", 8); rect(sign.g, -150, -190, 300, 84, "#F4EFE6", 10, { stroke: "#D8352A", "stroke-width": 6 });
    const st = mkText(sign.g, "Permit needed", { fam: "P", w: 600, size: 34, fill: PAL.navy, anchor: "middle", id: "permit" }); st.setAttribute("y", -138);
    enter(sign, tS + 1.0, "pop", 0.45); c.sfx("pop", tS + 1.0);
  });
}
