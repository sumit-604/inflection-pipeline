// Desi Drive regression. Usage: NODE_PATH=$(npm root -g) node regress.cjs http://localhost:8765/test.html [shotDir]
const { chromium } = require("playwright");
const URL = process.argv[2] || "http://localhost:8765/test.html", SHOTS = process.argv[3] || ".";
const ARGS = ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"];
let pass = 0, fail = 0; const errs = [];
const ok = (name, cond, info = "") => { if (cond) pass++; else fail++; console.log(`${cond ? "PASS" : "FAIL"} ${name}${cond ? "" : " :: " + JSON.stringify(info)}`); };

// In-page helpers: run the game for N seconds of game time without waiting for real frames.
const HELPERS = () => {
  const G = window.__dd.game; window.G = G; window.S = window.__dd.S;
  window.sim = (sec, dt = 0.05) => { for (let t = 0; t < sec; t += dt) { G.T += dt; G.step(dt); } };
  window.keys = (...k) => { G.keys.clear(); k.forEach((x) => G.keys.add(x)); };
  window.visible = (sel) => { const e = document.querySelector(sel); return !!e && !document.querySelector("#scr").hidden && document.querySelector("#card").contains(e); };
  window.noTraffic = () => { window._tc = G.traffic.cars; G.traffic.cars = []; };
  window.yesTraffic = () => { if (window._tc) G.traffic.cars = window._tc; };
  // Teleport the car around the track, index by index, to complete laps.
  window.lapTeleport = (laps) => { const W = G.world, N = W.tN, c = G.car; let i = W.trackNearest(c.x, c.z).i; for (let k = 0; k < N * laps + 30; k += 3) { const j = (i + k) % N, p = W.tp[j], q = W.tp[(j + 1) % N]; G.setPos(p.x, p.z, Math.atan2(q.x - p.x, q.z - p.z)); G.T += 0.05; G.step(0.05); if (G.mode.kind !== "race") return k; } return -1; };
};

(async () => {
  const b = await chromium.launch({ args: ARGS });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 } });
  const p = await ctx.newPage();
  p.on("pageerror", (e) => errs.push("PE " + e.message)); p.on("console", (m) => { if (m.type() === "error") errs.push("CE " + m.text()); });
  p.on("dialog", (d) => d.accept("Rishu"));
  await p.goto(URL); await p.waitForFunction(() => window.__dd, null, { timeout: 90000 }); await p.evaluate(HELPERS);
  const E = (f, a) => p.evaluate(f, a);

  // A. Start and menu
  let r = await E(() => ({ menu: visible("#m-free"), n: document.querySelectorAll("#card .btn").length, ver: document.querySelector("#ver").textContent, pts: document.querySelector("#pts").textContent, title: document.querySelector(".title").textContent, sub: document.querySelector(".sub").textContent }));
  ok("A1 menu opens", r.menu, r); ok("A2 version label bottom right", r.ver === "Desi Drive v2", r.ver); ok("A3 chip shows 300 points", r.pts === "300", r.pts);
  ok("A4 title and slogan", r.title === "Desi Drive" && r.sub.includes("Just live it!"), r); ok("A5 menu buttons", r.n >= 9, r.n);
  await p.screenshot({ path: `${SHOTS}/01-menu.png` });

  // B. Free drive: speed, gears, fuel
  r = await E(() => { noTraffic(); document.querySelector("#m-free").click(); keys("up"); const f0 = S.fuel, x0 = G.car.z; sim(5); const o = { kmh: G.car.kmh, gear: G.car.gear, fuel: S.fuel, f0, moved: G.car.z - x0, paused: G.paused }; yesTraffic(); return o; });
  ok("B1 free drive unpaused", r.paused === false, r); ok("B2 car speeds up", r.kmh > 40, r); ok("B3 gear shown", r.gear !== "N" && r.gear !== "R", r); ok("B4 fuel used", r.fuel < r.f0, r); ok("B5 car moves", r.moved > 30, r);
  await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/02-drive.png` });

  // C. Pause under the menu
  r = await E(() => { G.openMenu(); const z0 = G.car.z, t0 = G.traffic.cars.map((t) => t.pos).join(); sim(2); const o = { dz: G.car.z - z0, tr: t0 === G.traffic.cars.map((t) => t.pos).join(), resume: visible("#m-resume") }; document.querySelector("#m-resume").click(); return o; });
  ok("C1 car frozen under menu", r.dz === 0, r); ok("C2 traffic frozen under menu", r.tr, r); ok("C3 resume button", r.resume, r);

  // D. Brake, reverse, steer
  r = await E(() => { keys("down"); sim(4); const s = G.car.s; keys(); sim(1); keys("up", "left"); const h0 = G.car.h; sim(2); return { s, dh: G.car.h - h0 }; });
  ok("D1 brake then reverse", r.s < -1, r); ok("D2 steering turns", Math.abs(r.dh) > 0.3, r);

  // E. Building crash damages the car
  r = await E(() => { noTraffic(); keys(); S.damage = 0; const bx = G.world.boxes[0], cx = (bx.x0 + bx.x1) / 2, cz = (bx.z0 + bx.z1) / 2, sx = cx, sz = bx.z0 - 15; G.setPos(sx, sz, 0); G.car.s = 25; keys("up"); sim(2); keys(); yesTraffic(); return { dmg: S.damage, inside: G.car.x > bx.x0 && G.car.x < bx.x1 && G.car.z > bx.z0 && G.car.z < bx.z1 }; });
  ok("E1 crash adds damage", r.dmg > 0, r); ok("E2 car does not pass through walls", !r.inside, r);

  // F. Traffic moves
  r = await E(() => { const a = G.traffic.cars.map((t) => t.pos); sim(2); return G.traffic.cars.filter((t, i) => Math.abs(t.pos - a[i]) > 1).length; });
  ok("F1 traffic cars move", r >= 8, r);

  // G. Garage: buy, upgrade, paint, repair
  r = await E(() => { G.setPos(3.5, -150, 0); S.points = 6000; G.garage(false); const noRep = !document.querySelector("#g-rep"); document.querySelector('[data-buy="sedan"]').click(); const o = { noRep, owned: S.owned.includes("sedan"), car: S.car, pts: S.points, model: G.car.def.id };
    const top0 = __dd.eff(G.car.def).top, p0 = S.points; document.querySelector('[data-up="engine"]').click(); o.top = __dd.eff(G.car.def).top > top0; o.upCost = p0 - S.points;
    const p1 = S.points; document.querySelector('[data-paint="4"]').click(); o.paint = S.paint.sedan === 0xf1f1f1 && p1 - S.points === 50;
    S.damage = 50; G.garage(true); const rb = document.querySelector("#g-rep"); o.repBtn = !!rb; rb.click(); o.dmg = S.damage; document.querySelector("#g-close").click(); o.paused = G.paused; return o; });
  ok("G1 no repair away from garage", r.noRep, r); ok("G2 buy sedan", r.owned && r.car === "sedan" && r.pts === 3500 && r.model === "sedan", r);
  ok("G3 engine upgrade raises top speed", r.top && r.upCost === 245, r); ok("G4 paint costs 50", r.paint, r); ok("G5 repair at garage", r.repBtn && r.dmg === 0, r); ok("G6 garage closes to the road", r.paused === false, r);

  // H. Petrol pump opens when you stop there
  r = await E(() => { S.fuel = 20; S.points = 1000; keys(); G._atPump = false; const SP = G._specials || null; G.setPos(90, 90, 0); sim(0.3); const o = { open: visible("#p-full") }; if (o.open) { document.querySelector("#p-full").click(); o.fuel = S.fuel; o.pts = S.points; } return o; });
  ok("H1 pump panel opens", r.open, r); ok("H2 full tank", r.fuel === 100 && r.pts === 840, r);

  // I. Night, rain, camera, horn, indicator
  await p.keyboard.press("l"); await p.keyboard.press("r"); await p.keyboard.press("c"); await p.keyboard.press("h"); await p.keyboard.press("q");
  r = await E(() => ({ night: S.night, rain: S.rain && G.rain.visible, bg: G.scene.background.getHex(), cam: G.camMode, ind: G.ind, head: G.headL.intensity }));
  ok("I1 night toggles", r.night && r.bg < 0x202020 && r.head > 0, r); ok("I2 rain toggles", r.rain, r); ok("I3 camera cycles", r.cam === 1, r); ok("I4 indicator", r.ind === -1, r);
  await E(() => { G.setPos(3.5, -100, 0); keys("up"); sim(2); keys(); }); await p.waitForTimeout(2000); await p.screenshot({ path: `${SHOTS}/03-night-rain.png` });
  await p.keyboard.press("l"); await p.keyboard.press("r"); await p.keyboard.press("c"); await p.keyboard.press("c"); await p.keyboard.press("c"); await p.keyboard.press("q");
  r = await E(() => ({ night: S.night, rain: S.rain, cam: G.camMode }));
  ok("I5 toggles back", !r.night && !r.rain && r.cam === 0, r);

  // J. Red light fine and speed camera fine
  r = await E(() => { noTraffic(); const sg = G.world.signals[0]; G.T = 12 - 0.05; const st = G.world.signalState(G.T + 0.05); S.points = 500; G.car.wasIn = null; G.setPos(sg.x - 20, sg.z, Math.PI / 2); G.car.s = 15; keys("up"); sim(1.5); keys(); return { st: st.x, pts: S.points }; });
  ok("J1 red light jump fined 50", r.st === "r" && r.pts <= 450 + 5 && r.pts >= 440, r);
  r = await E(() => { const cm = G.world.cams[0]; S.points = 500; G._camHit = null; G.setPos(cm.x, cm.z - 25, 0); G.car.s = 30; keys("up"); sim(1.4); keys(); const o = { pts: S.points, kmh: G.car.kmh }; yesTraffic(); return o; });
  ok("J2 speed camera fined 40", r.pts < 500 && r.pts >= 455, r);

  // K. Stars give points in free drive
  r = await E(() => { const s = G.world.stars.find((x) => x.gone <= 0); const p0 = S.points; G.setPos(s.x, s.z, 0); sim(0.1); return { d: S.points - p0, gone: s.gone > 0 }; });
  ok("K1 star +25", r.d >= 25 && r.gone, r);

  // L. Circuit race
  r = await E(() => { G.startCircuit(); sim(3.5); const ai0 = G.mode.ai.map((a) => a.u); sim(3); const moved = G.mode.ai.every((a, i) => a.u > ai0[i] + 5); const board = document.querySelector("#race-board").textContent; const p0 = S.points, r0 = S.stats.races; const k = lapTeleport(3); const lapsOk = k > G.world.tN * 2.5; return { lapsOk, moved, board, k, done: visible("#d-free"), title: document.querySelector("#card h2")?.textContent, dp: S.points - p0, races: S.stats.races - r0, kind: G.mode.kind }; });
  ok("L1 AI racers drive", r.moved, r); ok("L2 race board shows positions", r.board.includes("Lap") && r.board.includes("Rocket Raju"), r.board);
  ok("L3 three laps finish the race", r.lapsOk && r.done && r.races === 1, r); ok("L4 race prize", r.dp >= 60, r);
  await E(() => { G.startCircuit(); sim(1); }); await p.waitForTimeout(2500); await p.screenshot({ path: `${SHOTS}/04-race.png` });

  // M. Time trial, ghost, challenge link
  r = await E(() => { S.best = {}; S.ghost = null; G.startTimeTrial(null); sim(3.5); const k = lapTeleport(1); return { k, best: S.best.track, ghost: !!S.ghost, share: visible("#tt-share") }; });
  ok("M1 time trial lap recorded", r.k > 0 && r.best > 5 && r.ghost && r.share, r);
  r = await E(() => { document.querySelector("#tt-menu").click(); const o = { menu: visible("#m-free") }; document.querySelector("#m-races").click(); document.querySelector("#r-back").click(); o.back = visible("#m-free"); return o; });
  ok("M1b Menu and Back buttons open the menu after driving", r.menu && r.back, r);
  r = await E(() => { S.name = "Rishu"; const link = G.challengeLink(G.lastRun); location.hash = link.split("#")[1]; const fg = G.readChallenge(); const dec = G.decodeGhost(fg.code); return { link: link.length, name: fg.name, t: fg.t, best: S.best.track, samples: dec.length, x0: dec[0][0] }; });
  ok("M2 challenge link round trip", r.name === "Rishu" && Math.abs(r.t - r.best) < 0.01 && r.samples > 10, r);
  r = await E(() => { G.friendGhost = G.readChallenge(); G.openMenu(); const btn = visible("#m-fg"); document.querySelector("#m-fg").click(); sim(3.5); const g0 = G.mode.ghost.position.clone(); sim(2); return { btn, ghostMoved: G.mode.ghost.position.distanceTo(g0) > 1, board: document.querySelector("#race-board").textContent }; });
  ok("M3 friend ghost race from menu", r.btn && r.ghostMoved && r.board.includes("Rishu"), r);
  await p.waitForTimeout(2000); await p.screenshot({ path: `${SHOTS}/05-ghost.png` });
  r = await E(() => { const k = lapTeleport(1); return { k, title: document.querySelector("#card h2")?.textContent }; }); ok("M4 ghost lap finishes", r.k > 0, r);
  await E(() => { location.hash = ""; G.friendGhost = null; });

  // N. Highway sprint
  r = await E(() => { G.startHighway(); sim(3.5); keys("up", "nitro"); sim(3); keys(); const ai = G.mode.ai.map((a) => a.z); const p0 = S.points; G.setPos(4, 900, 0); G.car.z = 800; sim(0.1); return { ai, done: visible("#d-free"), dp: S.points - p0, title: document.querySelector("#card h2")?.textContent }; });
  ok("N1 highway race finishes", r.done && r.dp > 0, r);

  // O. Taxi mission: 3 rides
  r = await E(() => { noTraffic(); G.startTaxi(); let n = 0; while (G.mode.kind === "mission" && n < 20) { const b = G.beacon.position; G.setPos(b.x, b.z, 0); sim(0.2); n++; } const o = { n, title: document.querySelector("#card h2")?.textContent, done: visible("#d-free") }; return o; });
  ok("O1 taxi 3 rides", r.done && r.title.includes("Taxi"), r);
  // P. Delivery
  r = await E(() => { G.startDelivery(); let n = 0; while (G.mode.kind === "mission" && n < 20) { const b = G.beacon.position; G.setPos(b.x, b.z, 0); sim(0.2); n++; } return { n, title: document.querySelector("#card h2")?.textContent }; });
  ok("P1 delivery 3 parcels", r.title && r.title.includes("delivered"), r);
  // Q. Delivery timeout
  r = await E(() => { G.startDelivery(); const b = G.beacon.position; G.setPos(b.x, b.z, 0); sim(0.2); sim(200, 0.25); return document.querySelector("#card h2")?.textContent; });
  ok("Q1 delivery can time out", r && r.includes("late"), r);
  // R. Parking
  r = await E(() => { G.startParking(); const m = G.world.bayMark.position, bay = G.world.bays.find((x) => Math.abs(x.x - m.x) < 0.01 && Math.abs(x.z - m.z) < 0.01); G.setPos(bay.x, bay.z, bay.h); sim(1.5); return document.querySelector("#card h2")?.textContent; });
  ok("R1 parking test", r && r.includes("Parked"), r);
  // S. Licence pass and fail
  r = await E(() => { S.licence = false; const p0 = S.points; G.startLicence(); let n = 0; while (G.mode.kind === "mission" && n < 20) { const b = G.beacon.position; G.setPos(b.x, b.z, 0); sim(0.3); n++; } return { title: document.querySelector("#card h2")?.textContent, lic: S.licence, dp: S.points - p0, chip: document.querySelector("#car-chip").textContent }; });
  ok("S1 licence test pass +500", r.title.includes("passed") && r.lic && r.dp >= 500 && r.chip.includes("🪪"), r);
  r = await E(() => { S.damage = 0; S.fuel = 100; G.car.broken = false; G.startLicence(); G.car.s = 25; keys("up"); sim(10); keys(); return document.querySelector("#card h2")?.textContent; });
  ok("S2 licence fails when too fast", r && r.includes("failed"), r);
  await E(() => yesTraffic());

  // T. Broken car and tow truck
  r = await E(() => { G.startFree(); noTraffic(); G.setPos(-3.5, -150, 0); S.damage = 100; G.car.broken = true; G.car.s = 0; S.points = 50; keys("up"); const z0 = G.car.z; sim(2); const crawl = G.car.kmh > 3 && G.car.kmh <= 20; keys(); yesTraffic(); G.openMenu(); const tow = visible("#m-tow"); document.querySelector("#m-tow").click(); return { crawl, tow, dmg: S.damage, broken: G.car.broken, pts: S.points, x: G.car.x }; });
  ok("T1 broken car only crawls", r.crawl, r); ok("T2 tow truck works with few points", r.tow && r.dmg === 40 && !r.broken && r.pts === 0, r);

  // U. About us and how to play
  r = await E(async () => { G.openMenu(); document.querySelector("#m-about").click(); const t = document.querySelector("#card").innerText, img = document.querySelector("#about-photo"); await img.decode().catch(() => {}); return { t, src: img.src.slice(0, 23), w: img.naturalWidth }; });
  ok("U1 about photo", r.src === "data:image/jpeg;base64," && r.w > 50, r.src); ok("U2 about text", r.t.includes("Rishabh Sharma") && r.t.includes("9 years old") && r.t.includes("Just live it!"), r.t.slice(0, 200));
  ok("U3 no AI or Gemini words", !/\bAI\b|Gemini|artificial/i.test(r.t), "");
  await p.screenshot({ path: `${SHOTS}/06-about.png` });
  r = await E(() => { document.querySelector("#a-back").click(); document.querySelector("#m-howto").click(); return document.querySelector("#card").innerText; });
  ok("U4 how to play", r.includes("Handbrake") && r.includes("Nitro"), r.slice(0, 100));

  r = await E(() => { document.querySelector("#h-back").click(); document.querySelector("#m-resume").click(); const a = G.paused; window.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" })); const b = visible("#m-free"); window.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" })); return { a, b, c: G.paused }; });
  ok("U5 Esc opens and closes the menu", r.a === false && r.b && r.c === false, r);

  // V. Drift gives points
  r = await E(() => { noTraffic(); G.startFree(); G.setPos(0, 200, 0); G.car.s = 30; const p0 = S.points; keys("up", "left", "hand"); sim(1.5); keys(); sim(0.5); yesTraffic(); return { d: S.points - p0, drifts: S.stats.drift }; });
  ok("V1 drift gives points", r.d > 0 && r.drifts > 0, r);

  // W. Each car spawns and drives
  r = await E(() => { const out = {}; for (const c of __dd.CARS) { if (!S.owned.includes(c.id)) S.owned.push(c.id); S.car = c.id; G.respawnCar(); G.setPos(0, 300, 0); S.fuel = 100; S.damage = 0; G.car.broken = false; keys("up"); sim(3); keys(); out[c.id] = Math.round(G.car.kmh); } return out; });
  ok("W1 all 7 vehicles drive", Object.values(r).length === 7 && Object.values(r).every((v) => v > 15), r);
  await E(() => { S.car = "gt"; G.respawnCar(); G.setPos(3.5, -150, 0); keys("up"); sim(1); keys(); }); await p.waitForTimeout(2000); await p.screenshot({ path: `${SHOTS}/07-gt.png` });

  // X. Level up from points
  r = await E(() => { const l0 = __dd.level(); G.addPts(5000, "test"); return { l0, l1: __dd.level() }; }); ok("X1 points raise the level", r.l1 > r.l0, r);

  // Y. Save survives reload
  const saved = await E(() => { __dd.save(); return S.points; });
  await p.reload(); await p.waitForFunction(() => window.__dd, null, { timeout: 90000 }); await p.evaluate(HELPERS);
  r = await E(() => ({ pts: S.points, car: S.car, lic: S.licence })); ok("Y1 save persists", r.pts === saved && r.car === "gt" && r.lic, r);

  r = await E(() => G.lastErr || ""); ok("Z1 no loop errors", !r, r.slice(0, 300));
  ok("Z2 no page errors", errs.length === 0, errs.slice(0, 5));

  // AA. The operator's flow: many modes one after another, with traffic, real keys (arrows and WASD).
  r = await E(() => { S.damage = 99; S.fuel = 100; G.car.broken = true; return 0; });
  const modes = [["free", ["#m-free"]], ["circuit", ["#m-races", "#r-circ"]], ["highway", ["#m-races", "#r-hw"]], ["trial", ["#m-races", "#r-tt"]], ["taxi", ["#m-missions", "#mi-taxi"]], ["delivery", ["#m-missions", "#mi-del"]], ["parking", ["#m-missions", "#mi-park"]], ["licence", ["#m-missions", "#mi-lic"]]];
  for (const round of [1, 2]) for (const [name, clicks] of modes) {
    await E(() => G.openMenu()); for (const c of clicks) await p.click(c);
    const key = round === 1 ? "ArrowUp" : "w"; await p.keyboard.down(key);
    r = await E(() => { const x0 = G.car.x, z0 = G.car.z; let maxK = 0; for (let i = 0; i < 140; i++) { G.T += 0.05; G.step(0.05); if (G.paused) break; maxK = Math.max(maxK, G.car.kmh); } return { moved: Math.round(Math.hypot(G.car.x - x0, G.car.z - z0)), maxK: Math.round(maxK), dmg: Math.round(S.damage), kind: G.mode.kind }; });
    await p.keyboard.up(key);
    ok(`AA${round} ${name} drives after other modes`, (r.moved > 25 || r.kind !== "mission") && r.maxK > 40, r);
  }
  r = await E(() => { G.openMenu(); document.querySelector("#m-free").click(); return 0; });
  await p.keyboard.down("ArrowUp"); await p.keyboard.down("ArrowLeft");
  r = await E(() => { const h0 = G.car.h; sim(2); return { kmh: G.car.kmh, dh: G.car.h - h0 }; });
  await p.keyboard.up("ArrowLeft"); await p.keyboard.up("ArrowUp"); await p.keyboard.down("d"); await p.keyboard.down("w");
  const r2 = await E(() => { const h0 = G.car.h; sim(2); return G.car.h - h0; }); await p.keyboard.up("d"); await p.keyboard.up("w");
  ok("AB arrows and WASD steer both ways", r.dh > 0.2 && r2 < -0.2, { r, r2 });
  r = await E(() => { G.setPos(-3.5, -150, 0); G.car.s = 0; const W = G.world, bx = W.boxes[0]; G.setPos((bx.x0 + bx.x1) / 2, bx.z0 - 2.2, 0); keys("up"); sim(3); keys(); return { kmh: G.car.kmh, toast: document.querySelector("#toast").textContent }; });
  ok("AC auto-unstick when pushing a wall", r.toast.includes("Unstuck"), r);

  // Phone layout with touch buttons
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });
  const mp = await m.newPage(); mp.on("pageerror", (e) => errs.push("M " + e.message)); await mp.goto(URL); await mp.waitForFunction(() => window.__dd, null, { timeout: 90000 }); await mp.evaluate(HELPERS);
  await mp.screenshot({ path: `${SHOTS}/08-phone-menu.png` });
  r = await mp.evaluate(() => { document.querySelector("#m-free").click(); const tb = getComputedStyle(document.querySelector("#touch")).display; const g = document.querySelector("#t-gas"); g.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true })); sim(3); const k = G.car.kmh; g.dispatchEvent(new PointerEvent("pointerup", { bubbles: true })); return { tb, k }; });
  ok("ZM1 touch buttons on phone", r.tb === "block" && r.k > 20, r);
  r = await mp.evaluate(() => { const ids = ["t-left", "t-right", "t-brake", "t-gas", "t-hand", "t-nitro", "dash", "map", "top-left", "top-right"], R = ids.map((i) => [i, document.getElementById(i).getBoundingClientRect()]), bad = [];
    for (let i = 0; i < R.length; i++) for (let j = i + 1; j < R.length; j++) { const [a, p] = R[i], [b, q] = R[j]; if (p.left < q.right && q.left < p.right && p.top < q.bottom && q.top < p.bottom) bad.push(a + "/" + b); } return bad; });
  ok("ZM1b phone HUD has no overlaps", r.length === 0, r);
  await mp.waitForTimeout(2000); await mp.screenshot({ path: `${SHOTS}/09-phone-drive.png` });
  ok("ZM2 no phone errors", !errs.some((e) => e.startsWith("M ")), errs);

  console.log(`\nRESULT ${pass} passed, ${fail} failed`); await b.close(); process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("CRASH", e); process.exit(2); });
