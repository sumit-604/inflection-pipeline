/* long.js - the 12 scenes of the long video. Each scene is built once; every frame is then a pure function of t (see common.js).
   Layout rules: content stays above the caption band (y < 890); text is left-aligned; colours follow the job (accent #F08A4B on dark,
   #B4481A on sand, cream on burnt orange). Where the accent would miss 4.5:1 on a mid-tone background, the number sits on a dark card. */
"use strict";

function pulse(c, x, y, t0, o = {}) {
  const col = o.color || PAL.acc, per = o.period || 1.9, R = o.r || 11, sc = o.scale || 4;
  const dot = c.sp(null, x, y, 1); circ(dot.g, 0, 0, R, col); circ(dot.g, 0, 0, R + 5, "none", { stroke: PAL.navy, "stroke-width": 3, opacity: 0.55 }); enter(dot, t0, "pop", 0.3);
  [0, 0.5].forEach(k => {
    const ring = c.sp(null, x, y, 1); circ(ring.g, 0, 0, R, "none", { stroke: col, "stroke-width": 4, "vector-effect": "non-scaling-stroke" });
    ring.fn = lt => { if (lt < t0 + 0.12) return { o: 0 }; const ph = (((lt - t0) / per) + k) % 1; return { sx: lerp(0.5, sc, EASE.enter(ph)), o: 0.85 * (1 - ph) }; };
  });
  c.sfx("ping", t0);
  return dot;
}
function mapLabel(c, str, x, y, t, kind = "zoom", o = {}) { const s = c.sp(null, x, y); chip(s.g, str, o); enter(s, t, kind, 0.45); return s; }

function buildLong() {
  mapDefs();

  /* ============ 1 HOOK (navy) ============ */
  defScene(1, c => {
    const ms = 0.84, mx = 1004, my = 44, P = (lon, lat) => { const [x, y] = LL(lon, lat); return [Math.round(mx + ms * x), Math.round(my + ms * y)]; };
    const map = c.sp(null, mx, my, ms); drawMap(map.g, { land: "#2A3B4B", border: "#41566A", iran: "#33495D", iranStroke: PAL.acc });
    map.to("x", 0, 0.9, mx + 80, mx, EASE.enter).to("o", 0, 0.5, 0, 1, EASE.enter);                    // hero: the map slides in
    const iran = P(54.2, 32.3), horm = P(56.35, 26.55), red = P(37.2, 20.6), bab = P(43.4, 12.7);
    const t1 = 1.0, t2 = c.S[1].t0 + 0.05, t3 = c.S[1].t0 + 1.0, tt = c.S[2].t0 + 0.5;
    pulse(c, iran[0], iran[1], t1);       mapLabel(c, "Iran", iran[0] - 78, iran[1] - 4, t1 + 0.25, "slideL");
    pulse(c, horm[0], horm[1], t2);       mapLabel(c, "Strait of Hormuz", horm[0] + 40, horm[1] + 62, t2 + 0.25, "slideR");
    pulse(c, red[0], red[1], t3);         mapLabel(c, "Red Sea", red[0] - 82, red[1] - 4, t3 + 0.25, "slideL");
    mapLabel(c, "Bab al-Mandab", bab[0] - 108, bab[1] + 40, t3 + 0.55, "slideL");
    const lines = ["The Middle East", "war, in plain", "words"];
    lines.forEach((s, i) => { const t = c.text(s, 96, 372 + i * 112, { size: 100, fill: COL.cream, id: "title" + i }); enter(t, tt + i * 0.2, "slideL", 0.7); });
    const bar = c.sp(null, 96, 612, 1); rect(bar.g, 0, 0, 300, 12, PAL.acc, 2); enter(bar, tt + 0.8, "stretchX", 0.6); bar.g.setAttribute("data-deco", 1);
    c.sfx("whoosh", tt);
  });

  /* ============ 2 WHY IT STARTED (sand) ============ */
  defScene(2, c => {
    const INK = PAL.navy, ACC = PAL.orange;
    // centrifuge, top view, spinning
    const cx = 330, cy = 440, R = 200;
    const base = c.sp(null, cx, cy + R + 36, 1); rect(base.g, -R * 1.15, -18, R * 2.3, 36, INK, 10); rect(base.g, -R * 0.7, -34, R * 1.4, 22, "#3B4A58", 8);
    const body = c.sp(null, cx, cy, 1); circ(body.g, 0, 0, R, "#D7CBB2", { stroke: INK, "stroke-width": 8 }); circ(body.g, 0, 0, R * 0.82, INK);
    for (let i = 0; i < 12; i++) { const a = i * 30 * Math.PI / 180; circ(body.g, Math.cos(a) * R * 0.91, Math.sin(a) * R * 0.91, 5, "#9C8F76"); }
    enter(base, 0.15, "rise", 0.7); enter(body, 0.0, "zoom", 0.8);
    const rotor = c.sp(null, cx, cy, 1); [0, 90, 180, 270].forEach(a => { const arm = g(rotor.g, { transform: `rotate(${a})` }); rect(arm, -22, -R * 0.74, 44, R * 0.62, ACC, 20); rect(arm, -22, -R * 0.74, 44, 18, "#F4EFE6", 9, { opacity: 0.5 }); });
    circ(rotor.g, 0, 0, 34, "#F4EFE6", { stroke: INK, "stroke-width": 6 }); circ(rotor.g, 0, 0, 9, INK);
    rotor.fn = lt => ({ r: lt * 150, o: lt < 0.4 ? clamp((lt - 0.2) / 0.2) : 1 }); // rotation only: linear, as allowed
    // gauge
    const gx = 780, gw = 84, gt = 130, gb = 770, ih = gb - gt - 16, gy = p => gb - 8 - ih * p / 100;
    const tube = c.sp(null, gx, gt, 1); rect(tube.g, 0, 0, gw, gb - gt, "#FFFFFF", gw / 2, { stroke: INK, "stroke-width": 7 }); enter(tube, c.S[0].t0 + 0.6, "drop", 0.7);
    const gid = "gaugeclip"; el("clipPath", { id: gid }, tube.g).appendChild(el("rect", { x: 10, y: 10, width: gw - 20, height: gb - gt - 20, rx: (gw - 20) / 2 }));
    const fill = c.sp(tube.g, 0, 0, 1); const fg = g(fill.g, { "clip-path": `url(#${gid})` });
    const fillS = c.sp(fg, 10, gb - gt - 10, 1); rect(fillS.g, 0, -(gb - gt - 20), gw - 20, gb - gt - 20, ACC);
    const tA = c.S[2].t0 + 0.15, tB = c.S[3].t0 + 0.1, tC = c.S[4].t0 + 0.05;
    fillS.fn = lt => { const lv = lt < tA ? 0 : lt < tB ? 0.05 * EASE.move(clamp((lt - tA) / 0.6)) : lt < tC ? lerp(0.05, 0.6, EASE.move(clamp((lt - tB) / 0.9))) : lerp(0.6, 0.9, EASE.move(clamp((lt - tC) / 0.8))); return { x: 10, y: gb - gt - 10, sx: 1, sy: Math.max(lv, 0.0001), o: lt < tA ? 0 : 1 }; };
    [[5, "5%", "power plant fuel", tA], [60, "60%", "Iran reached here", tB], [90, "90%", "bomb grade", tC]].forEach(([p, n, d, t]) => {
      const y = Math.round(gy(p)); const tick = c.sp(null, gx + gw + 4, y, 1); rect(tick.g, 0, -3, 30, 6, INK, 3); enter(tick, t + 0.3, "stretchX", 0.4);
      const lab = c.text([[[n, { fill: ACC, size: 72 }], ["  " + d, { fill: INK, fam: "P", w: 600, size: 36 }]]], gx + gw + 52, y + 24, { size: 72, id: "gauge" + p }); enter(lab, t + 0.35, "slideL", 0.6);
      c.sfx("pop", t + 0.3);
    });
    // speech bubbles
    const bubble = (x, y, kind, lines, tailLeft, t, id) => {
      const s = c.sp(null, x, y, 1), w = 500, h = 196; rect(s.g, 0, 0, w, h, "#FFFFFF", 30, { stroke: INK, "stroke-width": 5 });
      const tx = tailLeft ? 70 : w - 70; poly(s.g, [[tx - 22, h - 2], [tx + (tailLeft ? -26 : 26), h + 38], [tx + 22, h - 2]], "#FFFFFF", { stroke: INK, "stroke-width": 5, "stroke-linejoin": "round" }); rect(s.g, tx - 20, h - 8, 40, 12, "#FFFFFF");
      const fl = g(s.g, { transform: `translate(${tailLeft ? 90 : 90},${h / 2})` }); flag(fl, kind, 124);
      const tt = mkText(s.g, lines, { fam: "P", w: 600, size: 38, lh: 48, fill: INK, id }); tt.setAttribute("transform", `translate(172,${h / 2 - 6})`);
      enter(s, t, "pop", 0.4); c.sfx("pop", t); return s;
    };
    bubble(1360, 130, "us", ["Never a nuclear", "weapon"], true, c.S[5].t0 + 0.2, "bubbleUS");
    bubble(1360, 440, "ir", ["Our right", "to enrich"], false, c.S[6].t0 + 0.2, "bubbleIR");
  });

  /* ============ 3 HOW WE GOT HERE (teal) ============ */
  defScene(3, c => {
    const Y = 470, xs = [150, 470, 760, 1010, 1330, 1650], T0 = [0, 1, 2, 3, 4, 5].map(i => c.S[i].t0 + 0.05);
    const rail = c.sp(null, 110, Y, 1); rect(rail.g, 0, -5, 1700, 10, "#FFFFFF", 5, { opacity: 0.22 }); enter(rail, 0.05, "stretchX", 0.6);
    const prog = c.sp(null, 110, Y, 1); rect(prog.g, 0, -6, 1, 12, PAL.acc, 6);
    prog.fn = lt => { let x = xs[0]; for (let i = 1; i < 6; i++) { const a = T0[i] - 0.5; if (lt >= a) x = lerp(xs[i - 1], xs[i], EASE.move(clamp((lt - a) / 0.8))); } return { x: 110, y: Y, sx: Math.max(x - 110, 1), sy: 1, o: 1 }; };
    const labels = [
      [0, [[["2015:", { fill: PAL.acc, size: 60 }]], [["Nuclear deal", { fam: "P", w: 600, size: 36 }]]], "above", xs[0] - 22],
      [1, [[["2018:", { fill: PAL.acc, size: 60 }]], [["US leaves", { fam: "P", w: 600, size: 36 }]], [["the deal", { fam: "P", w: 600, size: 36 }]]], "below", xs[1] - 22],
      [3, [[["June 2025:", { fill: PAL.acc, size: 60 }]], [["12-day war", { fam: "P", w: 600, size: 36 }]]], "above", xs[3] - 22],
      [4, [[["28 Feb 2026:", { fill: PAL.acc, size: 60 }]], [["US and Israel", { fam: "P", w: 600, size: 36 }]], [["strike Iran", { fam: "P", w: 600, size: 36 }]]], "below", xs[4] - 22],
      [5, [[["Since then:", { fill: PAL.acc, size: 60 }]], [["Hormuz blocked", { fam: "P", w: 600, size: 36 }]]], "above", xs[5] - 130],
    ];
    xs.forEach((x, i) => {
      const small = i === 2, d = c.sp(null, x, Y, 1); circ(d.g, 0, 0, small ? 14 : 24, PAL.acc); circ(d.g, 0, 0, small ? 21 : 32, "none", { stroke: "#F4EFE6", "stroke-width": 4 }); enter(d, T0[i], "pop", 0.35); c.sfx("pop", T0[i]);
      if (small) { const a = c.sp(null, x, Y - 62, 1); poly(a.g, [[0, -26], [24, 4], [8, 4], [8, 26], [-8, 26], [-8, 4], [-24, 4]], "#F4EFE6"); enter(a, T0[i] + 0.15, "rise", 0.5); }
    });
    labels.forEach(([i, lines, side, lx], k) => {
      const nl = lines.length, lh = 46; const y = side === "above" ? Y - 56 - (nl - 1) * lh - 8 : Y + 100;
      // the accent date sits on a dark card: #F08A4B on this teal is only 3.9:1, on the card it is 6.6:1
      const wd = Math.max(...lines.map((ln, j) => measure(ln[0][0], j === 0 ? 60 : 36, j === 0 ? "A" : "P", j === 0 ? 900 : 600))) + 56, hh = 60 + 18 + (nl - 1) * lh + 22;
      const card = c.sp(null, lx - 28, y - 62); rect(card.g, 0, 0, Math.round(wd), hh, PAL.navy, 20); enter(card, T0[i] + 0.1, side === "above" ? "drop" : "rise", 0.6);
      const t = c.text(lines, lx, y, { size: 60, lh, fill: COL.cream, id: "tl" + i }); enter(t, T0[i] + 0.3, side === "above" ? "drop" : "rise", 0.6);
    });
  });
}
