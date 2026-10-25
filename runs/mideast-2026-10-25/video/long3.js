/* long3.js - scenes 8 to 12 and their art. */
"use strict";

function carIcon(parent, col) {
  const gg = g(parent);
  rect(gg, -100, -52, 200, 42, col, 14); path(gg, "M-58,-50 L-38,-90 L40,-90 L66,-50 Z", col);
  path(gg, "M-48,-54 L-34,-82 L-2,-82 L-2,-54 Z", "#BFD9E6"); path(gg, "M6,-54 L6,-82 L36,-82 L56,-54 Z", "#BFD9E6");
  [-58, 58].forEach(x => { circ(gg, x, -8, 22, "#16202A"); circ(gg, x, -8, 9, "#8A97A3"); });
  rect(gg, 90, -40, 10, 10, "#F6D56A", 3);
  return gg;
}
function pumpIcon(parent) {
  const gg = g(parent);
  rect(gg, -44, -200, 88, 200, "#F08A4B", 14); rect(gg, -30, -180, 60, 50, "#16202A", 8); rect(gg, -22, -170, 44, 12, "#7ED3A0", 3); rect(gg, -44, -12, 88, 12, "#16202A", 0);
  path(gg, "M44,-120 C80,-120 80,-60 62,-40", "none", { stroke: "#16202A", "stroke-width": 8, "stroke-linecap": "round" }); rect(gg, 54, -48, 24, 30, "#16202A", 6);
  return gg;
}
function person(parent, o) {
  const gg = g(parent);
  if (o.kind === "w") { rect(gg, -46, -140, 92, 140, o.bottom, 16); rect(gg, -46, -22, 92, 14, "#F08A4B", 0); } else { rect(gg, -26, -120, 22, 120, o.bottom, 8); rect(gg, 4, -120, 22, 120, o.bottom, 8); ellipse(gg, -15, 0, 24, 10, "#16202A"); ellipse(gg, 15, 0, 24, 10, "#16202A"); }
  rect(gg, -58, -240, 18, 112, o.top, 9); rect(gg, 40, -240, 18, 112, o.top, 9); circ(gg, -49, -124, 11, o.skin); circ(gg, 49, -124, 11, o.skin);
  rect(gg, -42, -256, 84, o.kind === "m" ? 190 : 150, o.top, 30);
  if (o.kind === "w") { path(gg, "M-42,-236 L40,-150 L40,-124 L-42,-196 Z", "#F08A4B", { opacity: 0.95 }); }
  rect(gg, -9, -272, 18, 20, o.skin, 5); circ(gg, 0, -304, 37, o.skin);
  path(gg, "M-38,-304 Q-42,-356 0,-356 Q42,-356 38,-304 Q22,-330 0,-328 Q-22,-330 -38,-304Z", o.hair); if (o.kind === "w") circ(gg, 0, -352, 17, o.hair);
  circ(gg, -13, -302, 4.5, "#16202A"); circ(gg, 13, -302, 4.5, "#16202A"); path(gg, "M-12,-286 Q0,-276 12,-286", "none", { stroke: "#7A2E22", "stroke-width": 3.5, "stroke-linecap": "round" });
  if (o.kind === "m") path(gg, "M-14,-292 Q0,-296 14,-292", "none", { stroke: o.hair, "stroke-width": 4, "stroke-linecap": "round" });
  if (o.kind === "w") circ(gg, 0, -322, 3.5, "#D8352A");
  return gg;
}
function ellipse(p, cx, cy, rx, ry, fill) { return el("ellipse", { cx, cy, rx, ry, fill }, p); }

/* the kitchen with the LPG cylinder and a generic family; x,y = top-left, s = scale (long video: 1) */
function kitchen(c, x, y, s, t0) {
  const k = c.sp(null, x, y, s); enter(k, t0, "zoom", 0.8);
    rect(k.g, 0, 0, 914, 640, "#F2DFC0", 28); rect(k.g, 0, 250, 914, 180, "#E7C99B", 0); for (let x = 0; x < 914; x += 61) rect(k.g, x, 250, 3, 180, "#D4B07D", 0); for (let y = 250; y < 430; y += 60) rect(k.g, 0, y, 914, 3, "#D4B07D", 0);
    rect(k.g, 70, 60, 230, 150, "#BFE3EE", 8, { stroke: "#7A4A2B", "stroke-width": 9 }); line(k.g, 185, 60, 185, 210, "#7A4A2B", 7); line(k.g, 70, 135, 300, 135, "#7A4A2B", 7);
    rect(k.g, 380, 110, 330, 14, "#7A4A2B", 4); [[400, "#D8786A"], [470, "#79B6B0"], [540, "#F6D56A"], [610, "#C9C0AA"]].forEach(([x, col]) => rect(k.g, x, 70, 54, 42, col, 8));
    rect(k.g, 0, 400, 914, 240, "#7A3E26", 0); rect(k.g, 0, 390, 914, 24, "#5A2B18", 0); rect(k.g, 0, 640, 914, 140, "#5B3A29", 0); rect(k.g, 0, 640, 914, 10, "#3E2517", 0);
    rect(k.g, 470, 330, 240, 62, "#2B3440", 8); [510, 590, 670].forEach(x => circ(k.g, x, 360, 14, "#6B7886")); rect(k.g, 520, 276, 150, 56, "#B8B8C0", 10); rect(k.g, 508, 292, 14, 8, "#8A8A92", 3); rect(k.g, 668, 292, 14, 8, "#8A8A92", 3);
    // LPG cylinder
    const cyl = c.sp(k.g, 790, 700); rect(cyl.g, -52, -250, 104, 250, "#D8352A", 40); rect(cyl.g, -52, -150, 104, 18, "#F4EFE6", 0); rect(cyl.g, -26, -286, 52, 44, "#16202A", 10); circ(cyl.g, 0, -296, 14, "#16202A"); rect(cyl.g, -36, -262, 72, 14, "#8C1F18", 6); rect(cyl.g, -52, -20, 104, 20, "#8C1F18", 10);
    enter(cyl, t0 + 0.5, "pop", 0.5); c.sfx("pop", t0 + 0.5);
    const fam = [[230, { kind: "w", skin: "#C98B5E", hair: "#1B1210", top: "#1F7A6E", bottom: "#1F7A6E" }, 1.3, "slideL"], [450, { kind: "m", skin: "#B87A4D", hair: "#1B1210", top: "#3B6EA8", bottom: "#E8DCC3" }, 1.3, "rise"], [610, { kind: "c", skin: "#C98B5E", hair: "#1B1210", top: "#F2C14E", bottom: "#4B3868" }, 0.85, "pop"]];
    fam.forEach(([x, o, s, kind], i) => { const p = c.sp(k.g, x, 700, s); person(p.g, o); enter(p, t0 + 0.3 + i * 0.35, kind, 0.6); });
  return k;
}

function buildLong3() {
  const CR = COL.cream;

  /* ============ 8 INSIDE IRAN (navy) ============ */
  defScene(8, c => {
    const CARD = "#22303D", cw = 544, ch = 270, cy0 = 60;
    const run = (lines, x, t, kind, id) => {
      const k = c.sp(null, x, cy0); rect(k.g, 0, 0, cw, ch, CARD, 26); enter(k, t, kind, 0.6); c.sfx("pop", t);
      const tx = c.text(lines, x + 36, cy0 + 112, { size: 38, lh: 52, fill: CR, id }); enter(tx, t + 0.25, "slideL", 0.6);
    };
    const A = { fill: PAL.acc, size: 96 }, B = { fam: "P", w: 600, size: 38 };
    run([[["27 lakh", A]], [["rials = 1 dollar", B]]], 96, c.S[1].t0 + 0.1, "drop", "card1");
    run([[["~90%", A]], [["price rise in a year", B]]], 96 + cw + 40, c.S[2].t0 + 0.1, "rise", "card2");
    run([[["Zero", A]], [["oil sold from ports", B]], [["in September", B]]], 96 + 2 * (cw + 40), c.S[2].t1 - 0.2, "drop", "card3");
    // street: road, shops, pump; the queue forms, then the street goes quiet
    const road = c.sp(null, 0, 0); rect(road.g, 0, 720, W, 90, "#2C3A47"); rect(road.g, 0, 810, W, 70, "#1F2C38"); for (let x = 40; x < W; x += 200) rect(road.g, x, 762, 90, 8, "#8793A0", 3); enter(road, 0.2, "rise", 0.7);
    const shops = [[100, 250], [420, 300], [760, 240], [1080, 290], [1400, 250]];
    shops.forEach(([x, h], i) => { const s = c.sp(null, x, 720 - h); rect(s.g, 0, 0, 250, h, "#2B3B4A", 8); rect(s.g, 24, 26, 80, 54, "#33485B", 6); rect(s.g, 130, 26, 80, 54, "#33485B", 6); enter(s, 0.3 + i * 0.08, "rise", 0.6);
      const sh = c.sp(null, x + 20, 720 - h + h - 76); rect(sh.g, 0, 0, 210, 76, "#52667A", 4); for (let k = 1; k < 5; k++) rect(sh.g, 0, k * 15, 210, 3, "#3E5163", 0); const tq = c.S[4].t0 + 1.6 + i * 0.12; sh.to("sy", tq, 0.6, 0.001, 1, EASE.move).to("o", tq, 0.05, 0, 1, EASE.lin); });
    const pump = c.sp(null, 1720, 800, 1.5); pumpIcon(pump.g); const tq0 = c.S[3].t0; enter(pump, tq0 - 0.1, "pop", 0.4);
    pump.to("o", c.S[4].t0 + 1.2, 0.5, 1, 0.0, EASE.exit);
    const cols = ["#F4EFE6", "#F08A4B", "#79B6B0", "#C9C0AA", "#D8786A"], xs = [1420, 1110, 800, 490, 180];
    cols.forEach((col, i) => {
      const car = c.sp(null, xs[i], 800, 1.45); carIcon(car.g, col); const a = tq0 + 0.15 + i * 0.28, b = c.S[4].t0 + 0.2 + i * 0.12;
      car.to("x", a, 1.6, xs[i] - 1500, xs[i], EASE.move).to("o", a, 0.05, 0, 1, EASE.lin).to("x", b, 1.1, xs[i], xs[i] - 1900, EASE.exit);
      c.sfx("whoosh", a);
    });
    const lamp = c.sp(null, 1580, 800); line(lamp.g, 0, 0, 0, -300, "#8793A0", 10); path(lamp.g, "M0,-300 Q40,-310 54,-280", "none", { stroke: "#8793A0", "stroke-width": 10, "stroke-linecap": "round" }); rect(lamp.g, 36, -282, 40, 16, "#F6D56A", 6);
    enter(lamp, c.S[4].t0 + 1.9, "rise", 0.7);
  });

  /* ============ 9 THE ELECTION WINDOW (sand) ============ */
  defScene(9, c => {
    const INK = PAL.navy, ACC = PAL.orange;
    const tile = (x, lines, t, circled, id, kind) => {
      const s = c.sp(null, x, 90); rect(s.g, 0, 0, 340, 270, "#FFFFFF", 22, { stroke: INK, "stroke-width": 5 }); path(s.g, "M0,56 L0,22 Q0,0 22,0 L318,0 Q340,0 340,22 L340,56 Z", ACC);
      [80, 260].forEach(rx => { rect(s.g, rx - 7, -12, 14, 40, INK, 7); });
      enter(s, t, kind, 0.6);
      const tx = c.text(lines, x + 36, 90 + 140, { size: 62, lh: 62, fill: ACC, id }); enter(tx, t + 0.3, "slideL", 0.6);
      if (circled) { const e = c.sp(null, x + 150, 90 + 118); el("ellipse", { cx: 0, cy: 0, rx: 142, ry: 46, fill: "none", stroke: ACC, "stroke-width": 7 }, e.g); const tc = t + 1.0; e.to("sx", tc, 0.6, 1.5, 1, EASE.pop).to("sy", tc, 0.6, 1.5, 1, EASE.pop).to("o", tc, 0.1, 0, 1, EASE.lin); e.to("r", tc, 0.6, 12, -3, EASE.enter); c.sfx("pop", tc); }
    };
    const L2 = { fam: "P", w: 600, size: 38, fill: INK };
    tile(96, [[["27 Oct:", { fill: ACC }]], [["Israel votes", L2]]], c.S[0].t0 - 0.5, true, "tile1", "slideL");
    tile(476, [[["3 Nov:", { fill: ACC }]], [["US midterms", L2]]], c.S[0].t0 + 0.3, true, "tile2", "rise");
    tile(1036, [[["3 Jan:", { fill: ACC }]], [["new Congress", L2]]], c.S[0].t0 + 0.9, false, "tile3", "slideR");
    // hourglass between 3 Nov and 3 Jan
    const hx = 926, hy = 225, tw = c.S[4].t0 + 0.1, td = 3.4, tOn = c.S[0].t0 + 0.9;
    const hg = c.sp(null, hx, hy); rect(hg.g, -52, -96, 104, 14, INK, 6); rect(hg.g, -52, 82, 104, 14, INK, 6);
    path(hg.g, "M-42,-82 L42,-82 L6,0 L42,82 L-42,82 L-6,0 Z", "rgba(255,255,255,0.65)", { stroke: INK, "stroke-width": 6, "stroke-linejoin": "round" }); enter(hg, c.S[0].t0 + 0.6, "pop", 0.5);
    const top = c.sp(null, hx, hy); poly(top.g, [[-34, -74], [34, -74], [0, -6]], ACC);
    top.fn = lt => ({ sy: lerp(1, 0.08, clamp((lt - tw) / td)), o: lt < tOn ? 0 : 1, x: hx, y: hy });
    const bot = c.sp(null, hx, hy + 76); poly(bot.g, [[-36, 0], [36, 0], [0, -64]], ACC);
    bot.fn = lt => ({ sy: lerp(0.12, 1, clamp((lt - tw) / td)), o: lt < tOn ? 0 : 1, x: hx, y: hy + 76 });
    const stream = c.sp(null, hx, hy); line(stream.g, 0, -4, 0, 70, ACC, 4); stream.fn = lt => ({ o: lt > tw && lt < tw + td ? 1 : 0, x: hx, y: hy });
    const wl = c.text("window", hx, 372, { fam: "P", w: 600, size: 34, fill: INK, anchor: "middle", id: "windowlbl" }); enter(wl, c.S[0].t0 + 1.0, "drop", 0.5);
    const wt = c.text([[["Window: ", { fill: INK }], ["Nov to Jan", { fill: ACC }]]], 96, 470, { size: 72, fill: INK, id: "windowtxt" }); enter(wt, c.S[4].t0 + 0.1, "slideL", 0.7);
    // Senate hemicycle: 100 dots, the first 67 (left to right) highlighted
    const ccx = 600, ccy = 868, counts = [16, 21, 27, 36], radii = [150, 205, 260, 315], dots = [];
    counts.forEach((n, r) => { for (let k = 0; k < n; k++) { const a = Math.PI * (1 - k / (n - 1)); dots.push([ccx + radii[r] * Math.cos(a), ccy - radii[r] * Math.sin(a), a]); } });
    dots.sort((p, q) => q[2] - p[2]); const tS = c.S[2].t0 + 0.1;
    dots.forEach(([x, y], i) => {
      x = Math.round(x); y = Math.round(y);
      const d = c.sp(null, x, y); circ(d.g, 0, 0, 12.5, "#CFC4AE"); enter(d, tS - 0.6 + (1 - dots[i][2] / Math.PI) * 0.5, "zoom", 0.4);
      if (i < 67) { const h = c.sp(null, x, y); circ(h.g, 0, 0, 12.5, ACC); const th = tS + 0.4 + i * 0.03; h.to("sx", th, 0.35, 0.3, 1, EASE.pop).to("sy", th, 0.35, 0.3, 1, EASE.pop).to("o", th, 0.08, 0, 1, EASE.lin); }
    });
    c.sfx("whoosh", tS - 0.6); [0, 1, 2, 3, 4, 5].forEach(i => c.sfx("tick", tS + 0.4 + i * 0.35));
    const rt = c.text([[["Removal needs", { fill: INK }]], [["67", { fill: ACC }], [" of 100 senators", { fill: INK }]]], 1040, 640, { size: 66, lh: 78, fill: INK, id: "removal" }); enter(rt, tS + 0.2, "slideL", 0.7);
  });

  /* ============ 10 THE ODDS (teal) ============ */
  defScene(10, c => {
    const rows = [["A short strike, then a deal:", 35], ["A long siege, no deal:", 27], ["Big escalation, oil above $150:", 15], ["A deal with no new strikes:", 13], ["Iran's regime cracks:", 10]];
    const T = [c.S[2].t0 + 0.1, c.S[3].t0 - 0.1, c.S[3].t0 + 1.3, c.S[4].t0, c.S[4].t0 + 1.6];
    const x0 = 96, y0 = 70, pitch = 116, BAR = 1000;
    rows.forEach(([, v], i) => {      // faint tracks give the empty chart a frame from the first second
      const y = y0 + i * pitch, tr = c.sp(null, x0, y + 52); rect(tr.g, 0, 0, BAR, 46, "#FFFFFF", 8, { opacity: 0.1 }); enter(tr, 0.15 + i * 0.12, "stretchX", 0.5);
    });
    rows.forEach(([lab, v], i) => {
      const y = y0 + i * pitch, w = Math.round(BAR * v / 35);
      const lt = c.text(lab, x0, y + 34, { fam: "P", w: 600, size: 38, fill: CR, id: "odds" + i }); enter(lt, T[i], "slideL", 0.55);
      const b = c.sp(null, x0, y + 52); rect(b.g, 0, 0, w, 46, PAL.acc, 8); b.to("sx", T[i] + 0.1, 0.9, 0.001, 1, EASE.move).to("o", T[i] + 0.1, 0.05, 0, 1, EASE.lin);
      const px = x0 + w + 18, pill = c.sp(null, px, y + 44); rect(pill.g, 0, 0, 148, 62, PAL.navy, 31); enter(pill, T[i] + 0.85, "pop", 0.4);
      const pt = c.text(v + "%", 74, 46, { size: 44, fill: PAL.acc, anchor: "middle", id: "pct" + i, words: 1 }, pill.g); enter(pt, T[i] + 0.85, "cut");
      c.sfx("pop", T[i]);
    });
    const fc = c.sp(null, 96, 690); rect(fc.g, 0, 0, 1728, 190, PAL.navy, 26); const tF = c.cue(1, "about") - 0.4; enter(fc, tF, "rise", 0.6);
    const f1 = c.text([[["New strike within a year: about ", { fill: CR }], ["70%", { fill: PAL.acc }]]], 140, 690 + 78, { size: 58, fill: CR, id: "foot1" }); enter(f1, tF + 0.3, "slideL", 0.6);
    const f2 = c.text("Judgment-based estimates, not market prices.", 140, 690 + 138, { fam: "P", w: 500, size: 36, fill: CR, id: "foot2" }); enter(f2, tF + 0.7, "slideL", 0.6);
    // emphasis on the big-escalation bar when the narration says "above one hundred and fifty"
    const te = c.cue(4, "above");
  });

  /* ============ 11 WHY INDIA SHOULD CARE (burnt orange; numbers cream) ============ */
  defScene(11, c => {
    kitchen(c, 96, 90, 1, 0.0);
    // the three numbers
    const hd = c.text("Through Hormuz:", 1100, 180, { fam: "P", w: 600, size: 50, fill: CR, id: "thru" }); enter(hd, c.S[0].t0 + 0.4, "slideL", 0.6);
    const items = [["40%", "of crude", c.cue(1, "forty")], ["60%", "of LNG", c.cue(1, "sixty")], ["90%", "of cooking gas", c.cue(1, "ninety")]];
    items.forEach(([n, d, t], i) => {
      const y = 360 + i * 190;
      const tx = c.text([[[n, { size: 150, fill: CR }], ["  " + d, { fam: "P", w: 600, size: 54, fill: CR }]]], 1100, y, { size: 150, fill: CR, id: "num" + i }); enter(tx, t - 0.1, i === 1 ? "rise" : "pop", 0.55); c.sfx("pop", t - 0.1);
    });
  });

  /* ============ 12 CLOSE (navy) ============ */
  defScene(12, c => {
    const ms = 0.7, mx = 1170, my = 90; const map = c.sp(null, mx, my, ms); drawMap(map.g, { land: "#243445", border: "#35495C", iran: "#2B3F52", iranStroke: "#3F5569" }); enter(map, 0, "slideR", 0.9);
    const nm = c.text("Keerti Sharma", 96, 420, { size: 132, fill: CR, id: "chname" }); enter(nm, 0.3, "slideL", 0.8);
    const hd = c.text("@Keerti__Sharma", 96, 520, { fam: "A", w: 800, size: 68, fill: PAL.acc, id: "chhandle" }); enter(hd, 0.9, "slideL", 0.7);
    const bar = c.sp(null, 96, 566); rect(bar.g, 0, 0, 220, 10, PAL.acc, 2); enter(bar, 1.3, "stretchX", 0.5);
    const ds = c.text("For learning only. Not investment advice.", 96, 640, { fam: "P", w: 500, size: 34, fill: CR, id: "disclaimer" }); enter(ds, 1.8, "rise", 0.6);
    [["27 Oct", c.S[1].t0 + 0.8, 1380], ["3 Nov", c.S[2].t0 + 0.6, 1600]].forEach(([s, t, x]) => { const sp = c.sp(null, x, 800); chip(sp.g, s, { size: 40, fill: PAL.acc, color: PAL.navy, op: 1 }); enter(sp, t, "pop", 0.4); c.sfx("pop", t); });
  });
}
