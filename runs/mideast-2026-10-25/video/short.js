/* short.js - the 1080x1920 Short. Big text sits in the middle third (y 640 to 1280); visuals above and below it; captions band at y 1450. */
"use strict";

function buildShort() {
  mapDefs(); const CR = COL.cream;

  /* ---- S1 hook (navy): map pulse over Hormuz ---- */
  defScene(1, c => {
    const ms = 1.35, [hx, hy] = LL(56.35, 26.55), mx = 700 - ms * hx, my = 400 - ms * hy, P = (lon, lat) => { const [x, y] = LL(lon, lat); return [Math.round(mx + ms * x), Math.round(my + ms * y)]; };
    const panel = c.sp(null, 0, 0); enter(panel, 0, "zoom", 0.7);
    el("clipPath", { id: "p1" }, panel.g).appendChild(el("rect", { x: 40, y: 60, width: 1000, height: 620, rx: 30 }));
    const pm = g(panel.g, { "clip-path": "url(#p1)" }); rect(pm, 40, 60, 1000, 620, "#101921"); const mg = g(pm, { transform: `translate(${mx},${my}) scale(${ms})` });
    drawMap(mg, { land: "#2A3B4B", border: "#41566A", iran: "#33495D", iranStroke: PAL.acc });
    const H0 = P(56.35, 26.55), I0 = P(54.2, 32.3);
    pulse(c, I0[0], I0[1], 0.5, { r: 11 }); mapLabel(c, "Iran", I0[0] - 80, I0[1] - 4, 0.75, "slideL");
    pulse(c, H0[0], H0[1], 1.2, { r: 12, scale: 4.5 }); mapLabel(c, "Strait of Hormuz", H0[0] - 10, H0[1] + 66, 1.5, "slideR");
    const t = c.text([[["Oil at", { fill: CR }]], [["$117.", { fill: PAL.acc }], [" Why?", { fill: CR }]]], 60, 860, { size: 150, lh: 150, fill: CR, id: "hookTxt" }); enter(t, 0.35, "slideL", 0.7);
    const bar = c.sp(null, 60, 1040); rect(bar.g, 0, 0, 260, 12, PAL.acc, 2); enter(bar, 1.2, "stretchX", 0.6);
    const bb = c.sp(null, 230, 1250, 1.5); barrelIcon(bb.g, 1, "#2E4256"); enter(bb, 1.8, "pop", 0.5); c.sfx("pop", 1.8);
  });

  /* ---- S2 two blockades (sand): the two vignettes ---- */
  defScene(2, c => {
    const INK = PAL.navy, SEA = "#1B3A4D", cw = 1000, ch = 330;
    const v1 = c.sp(null, 40, 90); rect(v1.g, 0, 0, cw, ch, SEA, 28); waves(v1.g, 24, cw - 48, 276, "#3F7894", 12); enter(v1, 0.1, "zoom", 0.6);
    const tk = c.sp(v1.g, 560, 206, 0.95); tanker(tk.g, "#EDE6D6", "#B4481A"); enter(tk, 0.2, "rise", 0.6);
    const bt = c.sp(v1.g, -120, 246, 1); boatIcon(bt.g); const bA = c.S[0].t0 + 0.7; bt.to("x", bA, 1.5, -120, 270, EASE.move).to("o", bA, 0.1, 0, 1, EASE.lin);
    [[800, 226], [900, 248]].forEach(([x, y], i) => { const m = c.sp(v1.g, x, y, 1); mineIcon(m.g); const t0 = c.S[0].t0 + 1.4 + i * 0.2; m.fn = lt => { const p = clamp((lt - t0) / 0.6); return { x, y: y + (p >= 1 ? Math.sin(lt * 1.6 + i * 2) * 4 : 0), sx: lerp(0.3, 1, EASE.pop(p)), o: lt < t0 ? 0 : 1 }; }; c.sfx("pop", t0); });
    const mk = c.sp(v1.g, 560, 70); markerX(mk.g, 30); enter(mk, c.S[0].t0 + 2.2, "pop", 0.4); c.sfx("alert", c.S[0].t0 + 2.2);
    const t = c.text(["Two blockades", "at sea"], 60, 830, { size: 118, lh: 126, fill: INK, id: "blockTxt" }); enter(t, 0.35, "slideL", 0.7);
    const v2 = c.sp(null, 40, 1030); rect(v2.g, 0, 0, cw, ch, SEA, 28); waves(v2.g, 24, cw - 48, 286, "#3F7894", 12); enter(v2, c.S[1].t0 - 0.2, "zoom", 0.6);
    const ns = c.sp(v2.g, 1250, 226, 0.95); navyShip(ns.g); const nA = c.S[1].t0 + 0.1; ns.to("x", nA, 1.3, 1250, 720, EASE.move).to("o", nA, 0.1, 0, 1, EASE.lin);
    const it = c.sp(v2.g, 190, 236, 0.8); tanker(it.g, "#EDE6D6", "#2A7D3F", "ir"); const iA = c.S[1].t0 + 0.9;
    it.fn = lt => { const a = clamp((lt - iA) / 1.0), b = clamp((lt - (iA + 1.4)) / 0.5), d = clamp((lt - (iA + 1.9)) / 1.3); return { x: lerp(190, 440, EASE.move(a)) + lerp(0, -250, EASE.move(d)), y: 236, sx: lerp(1, -1, EASE.move(b)), o: lt < iA - 0.4 ? 0 : clamp((lt - (iA - 0.4)) / 0.3) }; };
    c.sfx("whoosh", nA);
  });

  /* ---- S3 Saudi pipeline (teal) ---- */
  defScene(3, c => {
    const ms = 1.6, [ox, oy] = LL(36, 25), mx = 40 - ms * ox, my = 190 - ms * oy, P = (lon, lat) => { const [x, y] = LL(lon, lat); return [Math.round(mx + ms * x), Math.round(my + ms * y)]; };
    const mg = c.sp(null, mx, my, ms); drawMap(mg.g, { land: "#2C7070", border: "#4B9393", saudi: "#3B8686", iran: "#2C7070", iranStroke: "#4B9393" }); enter(mg, 0, "slideR", 0.8);
    const A = P(49.7, 25.9), M1 = P(46.6, 24.9), M2 = P(42.0, 24.1), Y = P(38.06, 24.09), O = P(44.6, 15.5);
    const tP = 0.5;
    const src = c.sp(null, A[0], A[1]); circ(src.g, 0, 0, 13, PAL.acc, { stroke: PAL.navy, "stroke-width": 4 }); enter(src, tP - 0.2, "pop", 0.4);
    polyDraw(c, null, [A, M1, M2, Y], PAL.acc, 9, tP, 1.5, { exitAt: c.S[0].t1 - 0.5, dim: 0.28, exitDur: 0.6 });
    const yb = c.sp(null, Y[0], Y[1]); circ(yb.g, 0, 0, 13, PAL.acc, { stroke: PAL.navy, "stroke-width": 4 }); enter(yb, tP + 1.4, "pop", 0.4);
    mapLabel(c, "Yanbu", Y[0] + 10, Y[1] - 50, tP + 1.7, "drop");
    mapLabel(c, "Yemen", P(47.2, 15.3)[0], P(47.2, 15.3)[1] + 6, c.S[0].t0 + 0.3, "slideR");
    const ap = [P(42.6, 16.9), P(39.17, 21.7)], tA = c.cue(0, "airports");
    ap.forEach((p, i) => { const s = c.sp(null, p[0], p[1]); circ(s.g, 0, 0, 30, PAL.navy, { stroke: "#F4EFE6", "stroke-width": 4 }); planeIcon(s.g, 0.8); enter(s, tA - 0.3 + i * 0.15, "pop", 0.4); });
    const arrow = (to, t0, dur) => {
      const dx = to[0] - O[0], dy = to[1] - O[1], L = Math.hypot(dx, dy), ang = Math.atan2(dy, dx) * 180 / Math.PI;
      const sp = c.sp(null, O[0], O[1], 1, ang); line(sp.g, 0, 0, L - 40, 0, "#F4EFE6", 7, { "stroke-dasharray": "18 12" }); poly(sp.g, [[L - 40, -14], [L - 6, 0], [L - 40, 14]], "#F4EFE6");
      sp.fn = lt => ({ x: O[0], y: O[1], r: ang, sx: Math.max(EASE.move(clamp((lt - t0) / dur)), 0.001), sy: 1, o: lt < t0 ? 0 : 1 });
      const ip = c.sp(null, to[0], to[1]); circ(ip.g, 0, 0, 12, "none", { stroke: "#F4EFE6", "stroke-width": 4, "vector-effect": "non-scaling-stroke" });
      ip.fn = lt => { const q = clamp((lt - (t0 + dur)) / 1.2); return { sx: lerp(0.5, 3.2, EASE.enter(q)), o: lt < t0 + dur ? 0 : 0.9 * (1 - q) }; }; c.sfx("alert", t0);
    };
    arrow(ap[0], tA, 0.9); arrow(ap[1], tA + 0.5, 1.3); arrow(P(41.2, 24.0), c.cue(0, "pipeline"), 1.5);
    const card = c.sp(null, 40, 770); rect(card.g, 0, 0, 1000, 330, PAL.navy, 30, { opacity: 0.97 }); enter(card, 0.25, "rise", 0.7);
    const t = c.text(["War moves to", "Saudi Arabia"], 76, 770 + 130, { size: 112, lh: 128, fill: CR, id: "saudiTxt" }); enter(t, 0.55, "slideL", 0.7);
  });

  /* ---- S4 calendar and odds (burnt orange; numbers cream) ---- */
  defScene(4, c => {
    const INK = PAL.navy, ACC = PAL.orange;
    const tile = c.sp(null, 60, 110); rect(tile.g, 0, 0, 640, 470, "#FFFFFF", 30, { stroke: INK, "stroke-width": 6 }); path(tile.g, "M0,90 L0,30 Q0,0 30,0 L610,0 Q640,0 640,30 L640,90 Z", INK);
    [130, 510].forEach(rx => rect(tile.g, rx - 9, -18, 18, 60, INK, 9)); enter(tile, 0.15, "slideL", 0.7);
    const d = c.text("3 Nov", 380, 110 + 320, { size: 150, fill: ACC, id: "novTxt", anchor: "middle" }); enter(d, 0.7, "slideL", 0.7);
    const e = c.sp(null, 60 + 320, 110 + 262); el("ellipse", { cx: 0, cy: 0, rx: 296, ry: 104, fill: "none", stroke: ACC, "stroke-width": 10 }, e.g);
    const tc = c.cue(0, "third") ; e.to("sx", tc, 0.6, 1.4, 1, EASE.pop).to("sy", tc, 0.6, 1.4, 1, EASE.pop).to("o", tc, 0.1, 0, 1, EASE.lin).to("r", tc, 0.6, 12, -3, EASE.enter); c.sfx("pop", tc);
    const tB = c.S[1].t0 + 0.1, tBar = c.cue(1, "about");
    const t = c.text([[["Strike within a year:", { fam: "P", w: 600, size: 62 }]], [["about ", { size: 76 }], ["70%", { size: 190 }]]], 60, 800, { size: 76, lh: 170, fill: CR, id: "oddsTxt" }); enter(t, tB, "slideL", 0.7);
    const tr = c.sp(null, 60, 1090); rect(tr.g, 0, 0, 960, 56, CR, 28, { opacity: 0.28 }); enter(tr, tB, "stretchX", 0.5);
    const bar = c.sp(null, 60, 1090); rect(bar.g, 0, 0, 672, 56, CR, 28); bar.to("sx", tBar, 1.1, 0.001, 1, EASE.move).to("o", tBar, 0.05, 0, 1, EASE.lin); c.sfx("pop", tBar);
  });

  /* ---- S5 India kitchen (olive): the number sits on a dark card ---- */
  defScene(5, c => {
    kitchen(c, 60, 60, 0.85, 0.0);
    const card = c.sp(null, 40, 740); rect(card.g, 0, 0, 1000, 480, PAL.navy, 30); const tc = c.cue(0, "ninety") - 0.4; enter(card, tc, "rise", 0.6);
    const t = c.text([[["90%", { fill: PAL.acc, size: 230 }]], [["of India's cooking gas", { fam: "P", w: 600, size: 58, fill: CR }]], [["comes via Hormuz", { fam: "P", w: 600, size: 58, fill: CR }]]], 80, 740 + 215, { size: 58, lh: 76, fill: CR, id: "gasTxt" });
    enter(t, tc + 0.3, "slideL", 0.7); c.sfx("pop", tc);
  });

  /* ---- S6 end card (plum) ---- */
  defScene(6, c => {
    const ms = 1.1, mx = 20, my = 20; const map = c.sp(null, mx, my, ms); drawMap(map.g, { land: "#6E3A60", border: "#8A5479", iran: "#7A4469", iranStroke: "#8A5479" }); enter(map, 0, "slideR", 0.8);
    const card = c.sp(null, 40, 760); rect(card.g, 0, 0, 1000, 340, PAL.navy, 30); enter(card, 0.2, "rise", 0.6);
    const t = c.text([[["Follow", { fill: CR, size: 100 }]], [["@Keerti__Sharma", { fill: PAL.acc, size: 86 }]]], 76, 760 + 140, { size: 100, lh: 124, fill: CR, id: "followTxt" }); enter(t, 0.45, "slideL", 0.7);
  });
}
