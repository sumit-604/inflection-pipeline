// RishDrive regression. Usage: NODE_PATH=$(npm root -g) node regress.cjs http://localhost:8765/test.html [shotDir]
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
  window.lapTeleportRev = (laps) => { const W = G.world, N = W.tN, c = G.car; let i = W.trackNearest(c.x, c.z).i; for (let k = 0; k < N * laps + 30; k += 3) { const j = ((i - k) % N + N) % N, p = W.tp[j], q = W.tp[(j - 1 + N) % N]; G.setPos(p.x, p.z, Math.atan2(q.x - p.x, q.z - p.z)); G.T += 0.05; G.step(0.05); if (G.mode.kind !== "race") return k; } return -1; };
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
  ok("A1 menu opens", r.menu, r); ok("A2 version label bottom right", r.ver === "RishDrive v10", r.ver); ok("A3 chip shows 300 points", r.pts === "300", r.pts);
  ok("A4 title and slogan", r.title === "RishDrive" && r.sub.includes("Just live it!"), r); ok("A5 menu buttons", r.n >= 9, r.n);
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
  await p.keyboard.press("l"); await p.keyboard.press("r"); for (let i = 0; i < 4; i++) await p.keyboard.press("c"); await p.keyboard.press("q");
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
  ok("W1 all 11 vehicles drive", Object.values(r).length === 11 && Object.values(r).every((v) => v > 15), r);
  await E(() => { S.car = "gt"; G.respawnCar(); G.setPos(3.5, -150, 0); keys("up"); sim(1); keys(); }); await p.waitForTimeout(2000); await p.screenshot({ path: `${SHOTS}/07-gt.png` });

  // X. Level up from points
  r = await E(() => { const l0 = __dd.level(); G.addPts(5000, "test"); return { l0, l1: __dd.level() }; }); ok("X1 points raise the level", r.l1 > r.l0, r);

  // ===== v3 features (ideas 6 to 14) =====
  await E(() => { noTraffic(); G.startFree(); S.points = 2000; S.damage = 0; S.fuel = 100; G.car.broken = false; S.car = "hatch"; G.respawnCar(); });
  // 6. Monsoon puddles
  r = await E(() => { if (!S.rain) G.toggleRain(); const pd = G.world.puddles[0], vis = pd.m.visible, sp0 = S.stats.splashes, p0 = S.points; G.setPos(pd.x, pd.z, 0); G.car.z -= 12; G.car.x = pd.x; keys("up"); G.car.s = 14; sim(1.2); keys(); const o = { vis, d: S.stats.splashes - sp0, dp: S.points - p0 }; G.toggleRain(); o.hidden = !pd.m.visible; return o; });
  ok("N6 puddles show in rain and splash", r.vis && r.d >= 1 && r.hidden, r);
  // 7. Toll plaza
  r = await E(() => { G.world.gates.forEach((g) => (g.open = 0, g.a = 0)); G.setPos(5.5, 420, 0); G.car.s = 12; keys("up"); let blocked = true; const g0 = G.world.gates[0]; for (let i = 0; i < 80; i++) { G.T += 0.05; G.step(0.05); if (G.car.z > 450.5 && g0.a < 0.9) blocked = false; } keys(); G.world.gates.forEach((g) => (g.open = 0, g.a = 0)); G.setPos(5.5, 441, 0); const p0 = S.points, t0 = S.stats.tolls; sim(0.3); const paid = p0 - S.points; keys("up"); sim(4); keys(); return { blocked, paid, tolls: S.stats.tolls - t0, passed: G.car.z > 462 }; });
  ok("N7a closed toll barrier stops the car", r.blocked, r); ok("N7b stop to pay 20 and pass", r.paid === 20 && r.tolls === 1 && r.passed, r);
  r = await E(() => { G.startHighway(); sim(3.5); G.setPos(5.5, 420, 0); G.car.s = 25; keys("up"); const p0 = S.points; sim(3); keys(); const o = { passed: G.car.z > 460, dp: p0 - S.points }; G.startFree(); return o; });
  ok("N7c races use the FASTag lane", r.passed && r.dp <= 0, r);
  // 8. Petrol pump game
  r = await E(async () => { S.fuel = 50; S.points = 1000; G.pumpPanel(); document.querySelector("#p-game").click(); const out = document.querySelector("#pg-v"); await new Promise((res) => { const t = setInterval(() => { if (parseInt(out.textContent) >= 99) { clearInterval(t); document.querySelector("#pg-stop").click(); res(); } }, 2); }); const msg = document.querySelector("#pg-msg").textContent; const o = { msg, fuel: S.fuel, perfect: S.stats.perfectFill }; document.querySelector("#pg-stop").click(); o.closed = !G.paused; return o; });
  ok("N8 pump fill game", r.msg.length > 5 && r.fuel >= 98 && r.closed, r);
  // 9. Daily gift
  r = await E(() => { S.daily = { d: "", streak: 0 }; G.openMenu(); const btn = visible("#m-daily"); const p0 = S.points; document.querySelector("#m-daily").click(); const o = { btn, dp: S.points - p0, st: S.daily.streak }; document.querySelector("#dg-ok").click(); o.gone = !document.querySelector("#m-daily");
    const y = new Date(); y.setDate(y.getDate() - 1); S.daily = { d: `${y.getFullYear()}-${String(y.getMonth() + 1).padStart(2, "0")}-${String(y.getDate()).padStart(2, "0")}`, streak: 2 }; G.openMenu(); const p1 = S.points; document.querySelector("#m-daily").click(); o.d2 = S.points - p1; o.st2 = S.daily.streak; G.checkBadges(); o.badge = !!S.badges.daily3; document.querySelector("#dg-ok").click(); return o; });
  ok("N9a daily gift once per day", r.btn && r.dp === 100 && r.st === 1 && r.gone, r); ok("N9b streak grows the gift", r.d2 === 200 && r.st2 === 3 && r.badge, r);
  // 10. Number plate and stickers
  r = await E(() => { G.garage(false); const inp = document.querySelector("#g-plate"); inp.value = "keerti 1"; document.querySelector("#g-plate-save").click(); const p0 = S.points; document.querySelector('[data-stk="2"]').click(); let plates = 0; G.car.m.traverse((o) => { if (o.isMesh && o.material.map && o.geometry.parameters && o.geometry.parameters.width === 0.9) plates++; }); const o = { plate: S.plate.hatch, stk: S.sticker.hatch, cost: p0 - S.points, plates, kids: G.car.m.children.length }; document.querySelector("#g-close").click(); return o; });
  ok("N10a own number plate", r.plate === "KEERTI 1" && r.plates >= 2, r); ok("N10b sticker costs 30", r.stk === 2 && r.cost === 30, r);
  await p.keyboard.type("wasd"); r = await E(() => S.plate.hatch); ok("N10c typing a plate does not drive", r === "KEERTI 1", r);
  // 11. Car wash
  r = await E(() => { S.dirt = 0.8; G._washCd = 0; const w0 = S.stats.washes; G.setPos(-175, -63.5, Math.PI / 2); G.car.s = 8; keys("up"); for (let i = 0; i < 200 && G.car.x < -130; i++) { G.T += 0.05; G.step(0.05); G.car.s = Math.min(G.car.s, 8); } keys(); return { dirt: S.dirt, w: S.stats.washes - w0, x: G.car.x }; });
  ok("N11 car wash cleans the car", r.dirt === 0 && r.w === 1, r);
  // 12. Stunt ramps
  r = await E(() => { const j0 = S.stats.jumps, p0 = S.points; G.setPos(-39, 6, 0); G.car.s = 24; keys("up"); let maxY = 0, air = false; for (let i = 0; i < 80; i++) { G.T += 0.05; G.step(0.05); maxY = Math.max(maxY, G.car.y); air = air || G.car.air; } keys(); return { maxY, air, j: S.stats.jumps - j0, dp: S.points - p0, y: G.car.y }; });
  ok("N12 ramp jump with points", r.air && r.maxY > 2.5 && r.j === 1 && r.dp > 0 && r.y < 0.01, r);
  r = await E(() => { G.setPos(-21, 10, 0); G.car.s = 15; keys("up"); sim(1.5); keys(); return { y: G.car.y, z: G.car.z }; });
  ok("N12b high end of a ramp is a wall", r.y < 0.5 && r.z < 27, r);
  await E(() => { G.setPos(-39, 12, 0); G.car.s = 24; keys("up"); sim(1.05); keys(); }); await p.waitForTimeout(1200); await p.screenshot({ path: `${SHOTS}/10-jump.png` });
  // 13. Badges
  r = await E(() => { G.checkBadges(); G.openMenu(); document.querySelector("#m-badges").click(); return { n: document.querySelectorAll(".badge").length, on: document.querySelectorAll(".badge.on").length, jump: !!S.badges.jump1, wash: !!S.badges.wash, toll: !!S.badges.toll, plate: !!S.badges.plate }; });
  ok("N13 34 badges, earned ones lit", r.n === 34 && r.on >= 5 && r.jump && r.wash && r.toll && r.plate, r);
  await p.screenshot({ path: `${SHOTS}/11-badges.png` });
  // 14. Village and Sunrise Hill: drive the road with a simple autopilot
  r = await E(() => { document.querySelector("#b-back").click(); document.querySelector("#m-free").click(); const W = G.world, v0 = S.stats.village, h0 = S.stats.hilltop; S.fuel = 100; G.setPos(-180, -3.5, -Math.PI / 2); keys("up"); let i = 0, maxY = 0;
    const path = W.vp.concat(W.hp); for (let k = 0; k < 3600; k++) { const c = G.car; let best = 1e9, bi = i; for (let j = Math.max(0, i - 5); j < Math.min(path.length, i + 30); j++) { const d = Math.hypot(path[j].x - c.x, path[j].z - c.z); if (d < best) { best = d; bi = j; } } i = bi; const t = path[Math.min(path.length - 1, i + 5)]; c.h = Math.atan2(t.x - c.x, t.z - c.z); c.s = Math.min(c.s, 14); G.T += 0.05; G.step(0.05); maxY = Math.max(maxY, c.y); if (i >= path.length - 3) break; }
    keys(); G.setPos(__dd.HILL.x, __dd.HILL.z + 8, 0); sim(0.2); return { village: S.stats.village - v0, maxY: Math.round(maxY), hill: S.stats.hilltop - h0, i, n: path.length }; });
  ok("N14a village visit", r.village >= 1, r); ok("N14b car climbs Sunrise Hill road", r.maxY >= 20 && r.i >= r.n - 10, r); ok("N14c hill top bonus", r.hill >= 1, r);
  await E(() => { G.setPos(__dd.HILL.x + 14, __dd.HILL.z - 4, -Math.PI / 2); G.camMode = 1; sim(0.3); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/12-hilltop.png` });
  await E(() => { G.camMode = 0; const q = G.world.vp[60], q2 = G.world.vp[64]; G.setPos(q.x, q.z, Math.atan2(q2.x - q.x, q2.z - q.z)); sim(0.3); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/13-village.png` });
  await E(() => { G.world.gates.forEach((g) => (g.open = 0)); G.setPos(5.5, 425, 0); sim(0.3); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/14-toll.png` });
  await E(() => { G.setPos(-168, -63.5, Math.PI / 2); sim(0.3); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/15-wash.png` });
  r = await E(() => { G.setPos(-3.5, -150, 0); G.car.s = 0; S.fuel = 100; S.damage = 0; G.car.broken = false; keys("up"); sim(3); keys(); return G.car.kmh; }); ok("N15 city driving still works after the new features", r > 40, r);
  await E(() => yesTraffic());

  // ===== v5: new vehicles, races, Skill Park, garage and real-feel extras =====
  await E(() => { noTraffic(); S.points = 50000; S.damage = 0; S.fuel = 100; G.startFree(); });
  r = await E(() => { const o = { cycleOwned: S.owned.includes("cycle") }; S.car = "bike"; if (!S.owned.includes("bike")) S.owned.push("bike"); G.respawnCar(); G.setPos(-3.5, -150, 0); G.car.s = 15; keys("up", "left"); sim(1); o.lean = G.car.m.rotation.z; keys(); S.car = "cycle"; G.respawnCar(); G.setPos(-3.5, -150, 0); S.fuel = 50; keys("up"); sim(5); keys(); o.fuel = S.fuel; o.cyc = Math.round(G.car.kmh); o.rider = !!G.car.m.userData.rider; return o; });
  ok("V1 everyone owns the cycle", r.cycleOwned, r); ok("V2 bikes lean into turns", r.lean < -0.15, r); ok("V3 the cycle needs no fuel", r.fuel === 50 && r.cyc >= 20 && r.rider, r);
  // Manual gearbox
  await E(() => { S.car = "hatch"; G.respawnCar(); S.manual = true; G.car.gN = 1; G.setPos(-3.5, -150, 0); keys("up"); sim(4); });
  r = await E(() => ({ gear: G.car.gear, kmh: Math.round(G.car.kmh), rpm: G.car.rpm }));
  await p.keyboard.press("g"); const q2 = await E(() => { const o = { gear: G.car.gear, boost: G.car.boost > 0 }; sim(1.5); o.kmh2 = Math.round(G.car.kmh); keys(); S.manual = false; return o; });
  ok("V4a manual 1st gear has a limiter", r.gear === "M1" && r.kmh < 60 && r.rpm > 0.9, r); ok("V4b G shifts up with a perfect-shift boost", q2.gear === "M2" && q2.boost && q2.kmh2 > r.kmh, q2);
  // Drag race and replay
  r = await E(() => { G.startDrag(); sim(3.3); keys("up"); sim(0.1); let k = 0; for (let i = 0; i < 600 && G.mode.kind === "race"; i++) { G.T += 0.05; G.step(0.05); if (G.car.rpm >= 0.88) G.shift(1); k = i; } keys(); return { title: document.querySelector("#card h2")?.textContent, best: S.best.drag, replay: !!document.querySelector("#d-replay") }; });
  ok("V5a drag race with gears", /Drag/.test(r.title) && r.best > 5 && r.best < 30, r); ok("V5b replay button after a race", r.replay, r);
  r = await E(() => { document.querySelector("#d-replay").click(); const k = G.mode.kind; sim(1); const cam = G.camera.position.clone(); sim(1); for (let i = 0; i < 800 && G.mode.kind === "replay"; i++) { G.T += 0.05; G.step(0.05); } return { k, back: document.querySelector("#card h2")?.textContent, kind: G.mode.kind }; });
  ok("V5c replay plays and returns to the result", r.k === "replay" && /Drag/.test(r.back) && r.kind === "free", r);
  await E(() => { G.startDrag(); sim(3.3); keys("up"); sim(2); keys(); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/16-drag.png` }); await E(() => G.startFree());
  // Elimination, night and reverse races
  r = await E(() => { G.startCircuit({ elim: true }); sim(3.5); const W = G.world, N = W.tN, c = G.car; let i = W.trackNearest(c.x, c.z).i, n1 = 3; for (let k = 0; k < N * 1.3; k += 3) { const j = (i + k) % N, p = W.tp[j], q = W.tp[(j + 1) % N]; G.setPos(p.x, p.z, Math.atan2(q.x - p.x, q.z - p.z)); G.T += 0.05; G.step(0.05); } n1 = G.mode.ai.length; const k2 = lapTeleport(3); return { n1, k2, title: document.querySelector("#card h2")?.textContent }; });
  ok("V6 elimination knocks out the last car each lap", r.n1 === 2 && r.k2 > 0 && /WIN/.test(r.title), r);
  r = await E(() => { const n0 = S.night; G.startCircuit({ night: true }); sim(0.3); const n1 = S.night, lamps = G.world.lampMats.some((m) => m.emissiveIntensity > 1); G.startFree(); return { n0, n1, lamps, n2: S.night }; });
  ok("V7 night race turns night on and back off", !r.n0 && r.n1 && r.lamps && !r.n2, r);
  r = await E(() => { G.startCircuit({ rev: true }); sim(3.5); const u0 = G.mode.ai.map((a) => a.u); sim(2); const back = G.mode.ai.every((a, i) => a.u < u0[i] - 5); const k = lapTeleportRev(3); return { back, k, title: document.querySelector("#card h2")?.textContent }; });
  ok("V8 reverse circuit runs the other way and finishes", r.back && r.k > 0 && /WIN|finished/.test(r.title), r);
  // Skill Park
  r = await E(() => { G.startSlalom(); const W = G.world; for (let i = 0; i < W.cones.length; i++) { const k = W.cones[i], zz = k.z + (i % 2 === 0 ? -3 : 3); G.setPos(k.x - 4, zz, Math.PI / 2); G.T += 0.05; G.step(0.05); G.setPos(k.x + 4, zz, Math.PI / 2); G.T += 0.05; G.step(0.05); } G.setPos(595, 225, Math.PI / 2); G.T += 0.05; G.step(0.05); return { title: document.querySelector("#card h2")?.textContent, text: document.querySelector("#card p")?.textContent, best: S.best.slalom }; });
  ok("V9a clean slalom", /[Ss]lalom/.test(r.title) && /0 cones hit, 0 wrong side/.test(r.text), r);
  r = await E(() => { G.startSlalom(); const k = G.world.cones[0]; G.setPos(k.x - 3, k.z + 3, Math.PI / 2); sim(0.1); G.setPos(k.x, k.z, Math.PI / 2); sim(0.1); const o = { down: k.down, bar: document.querySelector("#mission-bar").textContent }; G.startFree(); return o; });
  ok("V9b hitting a cone costs time", r.down && /cones hit 1/.test(r.bar), r);
  r = await E(() => { G.startStop(); const St = { line: 610, z: 345 }; G.car.s = 16; sim(0.3); G.setPos(St.line - G.car.m.userData.L / 2 - 0.1, St.z, Math.PI / 2); sim(0.3); return { title: document.querySelector("#card h2")?.textContent, best: S.best.stop }; });
  ok("V10 precision stop", /PERFECT/.test(r.title) && r.best === 300, r);
  r = await E(() => { G.startDirt(); sim(3.5); const W = G.world, N = W.dp.length; for (let k = 0; k <= N + 5 && G.mode.kind === "race"; k += 2) { const p = W.dp[k % N], q = W.dp[(k + 1) % N]; G.setPos(p.x, p.z, Math.atan2(q.x - p.x, q.z - p.z)); G.T += 0.05; G.step(0.05); } return { title: document.querySelector("#card h2")?.textContent, best: S.best.dirt, dirt: G.world.onDirt(W.dp[5].x, W.dp[5].z), bump: Math.max(...[0, 1, 2, 3, 4].map((i) => G.world.groundAt(W.dp[i * 3].x, W.dp[i * 3].z))) }; });
  ok("V11 dirt rally lap with bumps", /[Dd]irt rally/.test(r.title) && r.best > 0 && r.dirt && r.bump > 0.1, r);
  r = await E(() => { S.car = "gt"; G.respawnCar(); G.skillMenu(); document.querySelector("#k-lj").click(); keys("up", "nitro"); sim(9); keys(); return { jump: S.best.jump, y: G.car.y }; });
  ok("V12 long jump measures the distance", r.jump > 25, r);
  await E(() => { G.skillMenu(); document.querySelector("#k-lj").click(); keys("up", "nitro"); sim(5.9); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/17-longjump.png` }); await E(() => keys());
  r = await E(() => { G.setPos(530, 270, Math.PI / 2); G.car.s = 35; keys("up"); sim(1.5); keys(); return S.best.trap; });
  ok("V13 speed trap records km/h", r > 100, r);
  r = await E(() => { const p0 = S.points; G.setPos(410, 335, Math.PI / 2); G.car.s = 22; keys("up", "left", "hand"); sim(3); keys(); sim(0.6); return { best: S.best.drift, dp: S.points - p0 }; });
  ok("V14 drift zone combo", r.best > 0 && r.dp > 0, r);
  // Garage: showroom and extras
  r = await E(() => { S.car = "hatch"; G.respawnCar(); G.garage(false); document.querySelector('[data-view="scooty"]').click(); sim(0.2); const o = { on: !!G.showroom, sr: document.body.classList.contains("sr"), clear: document.querySelector("#scr").classList.contains("clear") }; if (S.owned.includes("scooty")) S.owned.splice(S.owned.indexOf("scooty"), 1); G.openShowroom("scooty", false); const p0 = S.points; document.querySelector("#sr-buy").click(); o.bought = S.owned.includes("scooty") && p0 - S.points === 300 && S.car === "scooty"; document.querySelector("#sr-next").click(); o.next = G.showroom.id; document.querySelector("#sr-back").click(); o.off = !G.showroom && !document.body.classList.contains("sr"); return o; });
  ok("V15 3D showroom: view, buy, next, back", r.on && r.sr && r.clear && r.bought && r.next === "bike" && r.off, r);
  r = await E(() => { S.car = "sedan"; if (!S.owned.includes("sedan")) S.owned.push("sedan"); G.respawnCar(); G.garage(false); const p0 = S.points; document.querySelector('[data-rim="2"]').click(); document.querySelector('[data-spo="2"]').click(); document.querySelector('[data-neon="0"]').click(); document.querySelector('[data-gb="1"]').click(); const o = { cost: p0 - S.points, rim: S.rims.sedan, spo: S.spoiler.sedan, neon: S.neon.sedan, light: !!G.car.m.userData.neonLight, manual: S.manual }; document.querySelector('[data-gb="0"]').click(); o.auto = !S.manual; document.querySelector("#g-close").click(); return o; });
  ok("V16 wheels, spoiler, neon and gearbox", r.cost === 600 && r.rim === 2 && r.spo === 2 && r.neon === 0 && r.light && r.manual && r.auto, r);
  // Fog, mirror, cockpit, speed blur, turbo pops
  await p.keyboard.press("o"); r = await E(() => ({ fog: S.fog, far: G.scene.fog.far })); await p.keyboard.press("o"); const q3 = await E(() => ({ fog: S.fog, far: G.scene.fog.far }));
  ok("V17 fog mode toggles with O", r.fog && r.far <= 80 && !q3.fog && q3.far > 300, { r, q3 });
  await E(() => { S.mirror = true; G.setPos(-3.5, -150, 0); }); await p.waitForTimeout(1200); r = await E(() => getComputedStyle(document.querySelector("#mirror-frame")).display); await p.keyboard.press("m"); await p.waitForTimeout(800); const q4 = await E(() => getComputedStyle(document.querySelector("#mirror-frame")).display); await p.keyboard.press("m");
  ok("V18 rear-view mirror shows and hides with M", r === "block" && q4 === "none", { r, q4 });
  r = await E(() => { G.camMode = 4; keys("up"); sim(1); keys(); G.hudT = 0; G.hud(0.1); const ud = G.car.m.userData; return { ck: ud.cockpit.visible, glass: ud.glass.every((g) => !g.visible), dist: G.camera.position.distanceTo(G.car.m.position) }; });
  ok("V19 dashboard camera inside the car", r.ck && r.glass && r.dist < 3, r); await p.waitForTimeout(1200); await p.screenshot({ path: `${SHOTS}/18-cockpit.png` }); await E(() => { G.camMode = 0; G.placeCam(true); });
  r = await E(() => { S.car = "gt"; G.respawnCar(); G.setPos(5.5, 250, 0); G.car.s = 50; keys("up", "nitro"); sim(0.5); const fx = G._fxOn; S.up.gt = Object.assign({}, S.up.gt, { engine: 3 }); keys("up"); sim(0.5); const before = Array.from(G.sp.life).filter((l) => l > 0).length; keys(); G.T += 0.05; G.step(0.05); const after = Array.from(G.sp.life).filter((l) => l > 0).length; return { fx, before, after }; });
  ok("V20 speed blur at high speed", r.fx, r); ok("V21 turbo pop flames when lifting off", r.after > r.before, r);
  await E(() => { G.toggleNight(); G.setPos(5.5, 300, 0); G.car.s = 55; keys("up", "nitro"); sim(0.6); keys(); }); await p.waitForTimeout(1500); await p.screenshot({ path: `${SHOTS}/19-night-neon-blur.png` }); await E(() => { G.toggleNight(); S.car = "hatch"; G.respawnCar(); });
  // Nitro: one tap keeps it on, and it works while turning with no gas key held.
  await E(() => { S.car = "hatch"; G.respawnCar(); G.startFree(); S.nitro = 100; S.fuel = 100; S.damage = 0; G.car.broken = false; G.setPos(5.5, 230, 0); G.car.s = 15; keys(); });
  await p.keyboard.press("n"); await p.keyboard.down("ArrowLeft");
  r = await E(() => { const s0 = G.car.s, h0 = G.car.h; sim(0.8); return { on: G.car.nitroOn, latch: G.car.nitroLatch, faster: G.car.s > s0 + 3, turned: Math.abs(G.car.h - h0) > 0.3 }; });
  await p.keyboard.up("ArrowLeft");
  ok("V24 nitro tap stays on and works in a turn", r.on && r.latch && r.faster && r.turned, r);
  await p.keyboard.down("ArrowDown"); r = await E(() => { sim(0.3); return { on: G.car.nitroOn, latch: G.car.nitroLatch }; }); await p.keyboard.up("ArrowDown");
  ok("V25 braking stops the nitro", !r.on && !r.latch, r);
  await p.keyboard.press("n"); r = await E(() => { sim(0.2); const a = G.car.nitroLatch; return a; }); await p.keyboard.press("n"); const q5 = await E(() => G.car.nitroLatch);
  ok("V26 a second tap turns nitro off", r === true && q5 === false, { r, q5 });
  r = await E(() => { G.startCircuit(); sim(3.5); const W = G.world, N = W.tN; G.nitroTap(); let minS = 1e9, hits = 0, fast = false; const d0 = S.damage; for (let k = 0; k < 120; k++) { const c = G.car, n = W.trackNearest(c.x, c.z), t = W.tp[(n.i + 8) % N], want = Math.atan2(t.x - c.x, t.z - c.z), d = Math.atan2(Math.sin(want - c.h), Math.cos(want - c.h)); keys(d > 0.05 ? "left" : d < -0.05 ? "right" : "x"); G.T += 0.05; G.step(0.05); if (G.car.kmh > 100) fast = true; if (fast && G.car.nitroOn) minS = Math.min(minS, G.car.s); } keys(); const o = { minKmh: Math.round(minS * 3.6), dmg: S.damage - d0, off: W.trackNearest(G.car.x, G.car.z).d }; G.startFree(); return o; });
  ok("V27 nitro carries through the circuit bends", r.minKmh > 85 && r.minKmh < 1e6 && r.off < 12 && r.dmg === 0, r);
  // v7: power drift with W + S + A or D (and the arrows), drift button
  for (const [k1, k2, k3, side] of [["w", "s", "a", 1], ["ArrowUp", "ArrowDown", "ArrowRight", -1]]) {
    await E(() => { S.car = "hatch"; G.respawnCar(); G.startFree(); S.damage = 0; G.car.broken = false; G.setPos(5.5, 230, 0); G.car.s = 22; keys(); G.car.nitroLatch = false; });
    await p.keyboard.down(k1); await p.keyboard.down(k2); await p.keyboard.down(k3);
    r = await E(() => { const h0 = G.car.h; let maxLat = 0; for (let i = 0; i < 24; i++) { G.T += 0.05; G.step(0.05); maxLat = Math.max(maxLat, Math.abs(G.car.lat)); } return { pd: G.car.pdOn, lat: G.car.lat, maxLat, dh: G.car.h - h0, kmh: Math.round(G.car.kmh) }; });
    await p.keyboard.up(k3); await p.keyboard.up(k2); await p.keyboard.up(k1);
    ok(`V28 power drift ${k1}+${k2}+${k3}`, r.pd && r.maxLat > 3 && Math.sign(r.dh) === side && r.kmh > 40, r);
  }
  r = await E(() => { G.setPos(5.5, 230, 0); G.car.s = 22; G.touch.drift = true; G.touch.left = true; sim(1); const o = { pd: G.car.pdOn, lat: Math.abs(G.car.lat) }; G.touch = {}; sim(0.5); return o; });
  ok("V29 the drift button with a turn key drifts", r.pd && r.lat > 2, r);
  r = await E(() => { G.setPos(5.5, 230, 0); G.car.s = 22; keys("up", "down"); sim(1); const o = { pd: G.car.pdOn, kmh: Math.round(G.car.kmh) }; keys("down"); sim(1); o.brake = Math.round(G.car.kmh); keys(); return o; });
  ok("V30 gas+brake with no turn is not a drift, brake still brakes", !r.pd && r.brake < r.kmh, r);
  // v7: Track Challenges
  r = await E(() => { S.tracks = {}; S.tghost = {}; G.openMenu(); document.querySelector("#m-tracks").click(); const btns = [...document.querySelectorAll("[data-trk]")]; return { n: btns.length, open: btns.filter((b) => !b.disabled).length }; });
  ok("V31 track menu: 15 tracks, only the first open", r.n === 15 && r.open === 1, r);
  r = await E(() => { document.querySelector('[data-trk="0"]').click(); const built = !!G.world.trk; sim(3.4); const tk = G.world.trk, N = tk.N; for (let k = 0; k < N * 3 && G.mode.kind === "race"; k += 2) { const a = tk.pts[(N - 5 + k) % N], b = tk.pts[(N - 4 + k) % N]; G.setPos(a.x, a.z, Math.atan2(b.x - a.x, b.z - a.z)); G.T += 0.05; G.step(0.05); } return { built, title: document.querySelector("#card h2")?.textContent, rec: S.tracks.ring, ghost: !!S.tghost.ring, keep: !!G.world.trk, unlockText: /Unlocked/.test(document.querySelector("#card p").textContent) }; });
  ok("V32 finish a track: stars, best time, ghost, next unlocked", r.built && /Rishu Ring/.test(r.title) && r.rec && r.rec.stars >= 1 && r.ghost && r.unlockText, r);
  r = await E(() => { const vis = !!G.world.trk; document.querySelector("#d-replay").click(); sim(1); const during = !!G.world.trk && G.mode.kind === "replay"; for (let i = 0; i < 1500 && G.mode.kind === "replay"; i++) { G.T += 0.05; G.step(0.05); } const after = !!G.world.trk; document.querySelector("#d-free").click(); return { vis, during, after, gone: !G.world.trk }; });
  ok("V33 track replay shows the track, keep driving clears it", r.vis && r.during && r.after && r.gone, r);
  r = await E(() => { G.tracksMenu(); const open = [...document.querySelectorAll("[data-trk]")].filter((b) => !b.disabled).length; G.startTrack(0); sim(3.6); const g = G.mode.ghost, p0 = g && g.position.clone(); sim(1); const moved = g && g.position.distanceTo(p0) > 2; G.startFree(); return { open, ghost: !!g, moved }; });
  ok("V34 second track open and your ghost races you", r.open === 2 && r.ghost && r.moved, r);
  r = await E(() => { const ids = ["ring", "hairpin", "eight", "chicane", "jump", "monsoon", "snake", "fog", "dirt", "narrow", "star", "gp"], out = []; for (let i = 0; i < 12; i++) { if (i) S.tracks[ids[i - 1]] = S.tracks[ids[i - 1]] || { best: 999, stars: 1 }; G.startTrack(i); const tk = G.world.trk, T = tk.T, cond = { night: S.night === !!T.night, rain: S.rain === !!T.rain, fog: S.fog === !!T.fog }; sim(3.4); const N = tk.N; for (let k = 0; k < N * 4 && G.mode.kind === "race"; k += 2) { const a = tk.pts[(N - 5 + k) % N], b = tk.pts[(N - 4 + k) % N]; G.setPos(a.x, a.z, Math.atan2(b.x - a.x, b.z - a.z)); G.T += 0.05; G.step(0.05); } out.push({ i, done: /⭐/.test(document.querySelector("#card h2")?.textContent || ""), cond: cond.night && cond.rain && cond.fog }); } G.startFree(); return { all: out.every((o) => o.done && o.cond), bad: out.filter((o) => !(o.done && o.cond)), clean: !G.world.trk && !S.night && !S.rain && !S.fog, err: G.lastErr || "" }; });
  ok("V35 all 12 tracks build, set their weather and finish", r.all && r.clean && !r.err, r);
  r = await E(() => { G.startTrack(4); sim(3.4); const tk = G.world.trk, rp = tk.ramps[0], i = tk.pts.findIndex((p) => Math.hypot(p.x - rp.x, p.z - rp.z) < 2); const a = tk.pts[(i - 15 + tk.N) % tk.N], b = tk.pts[(i - 14 + tk.N) % tk.N]; G.setPos(a.x, a.z, Math.atan2(b.x - a.x, b.z - a.z)); G.car.s = 30; keys("up"); let air = false; for (let k = 0; k < 40; k++) { G.T += 0.05; G.step(0.05); air = air || G.car.air; } keys(); G.startFree(); return { ramps: tk.ramps.length, air }; });
  ok("V36 Jump Junction ramps launch the car", r.ramps === 2 && r.air, r);
  r = await E(() => { G.startTrack(0); sim(3.4); const tk = G.world.trk, p0 = tk.pts[50]; G.setPos(p0.x + 40, p0.z + 40, 0); sim(3); const n = G.world._pathNear(tk.pts, G.car.x, G.car.z).d; G.startFree(); return { back: n < 3 }; });
  ok("V37 far off the track: put back with a penalty", r.back, r);
  // v7: realistic two-wheelers
  r = await E(() => { const o = {}; for (const t of ["cycle", "scooty", "bike"]) { const m = __dd.makeCar(t, 0xff0000); let meshes = 0; m.traverse((x) => { if (x.isMesh) meshes++; }); o[t] = { meshes, rider: !!m.userData.rider, wheels: m.userData.wheels.length, steer: m.userData.front.length }; } o.crank = !!__dd.makeCar("cycle", 0xff0000).userData.crank; return o; });
  ok("V38 detailed cycle, scooty and bike models with riders", ["cycle", "scooty", "bike"].every((t) => r[t].meshes >= 40 && r[t].rider && r[t].wheels === 2 && r[t].steer === 1) && r.crank, r);
  r = await E(() => { S.car = "cycle"; G.respawnCar(); G.setPos(-3.5, -150, 0); const c0 = G.car.m.userData.crank.rotation.x; keys("up"); sim(1); keys(); return G.car.m.userData.crank.rotation.x !== c0; });
  ok("V39 cycle pedals turn while riding", r === true, r);
  await E(() => { S.car = "hatch"; G.respawnCar(); });
  r = await E(() => { G.checkBadges(); return { drag: !!S.badges.drag, slalom: !!S.badges.slalom, two: !!S.badges.twowheel }; }); ok("V22 new badges", r.drag && r.slalom && r.two, r);
  r = await E(() => G.lastErr || ""); ok("V23 no loop errors after v5 checks", !r, r.slice(0, 300));
  await E(() => yesTraffic());

  // ===== v8: one-lap tracks, sky and space tracks, new modes and new places =====
  await E(() => { noTraffic(); G.startFree(); });
  r = await E(() => { const { TRACKS } = __dd; S.tracks = {}; G.tracksMenu(); return { n: TRACKS.length, menu: document.querySelectorAll("[data-trk]").length, laps: [...new Set(TRACKS.map((t) => t.laps))], hard: TRACKS.filter((t) => t.elev).map((t) => t.id) }; });
  ok("W8-01 15 tracks, every track is one lap, 3 sky tracks", r.n === 15 && r.menu === 15 && r.laps.length === 1 && r.laps[0] === 1 && r.hard.join() === "skygap,coaster,space", r);
  r = await E(() => { for (const t of ["ring", "hairpin", "eight", "chicane", "jump", "monsoon", "snake", "fog", "dirt", "narrow", "star", "gp", "skygap", "coaster"]) S.tracks[t] = { best: 999, stars: 1 };
    const run = (idx, speed) => { G.startTrack(idx); sim(3.5); const tk = G.world.trk, N = tk.N, gap = tk.gaps[0], i0 = Math.floor((gap[0] - 0.06) * N), a = tk.pts[i0], b2 = tk.pts[i0 + 1]; G.setPos(a.x, a.z, Math.atan2(b2.x - a.x, b2.z - a.z)); G.car.s = speed; keys("up"); let air = false;
      for (let k = 0; k < 90; k++) { const c = G.car, n = G.world._pathNear(tk.pts, c.x, c.z), t = tk.pts[(n.i + 6) % N], want = Math.atan2(t.x - c.x, t.z - c.z); if (!c.air) c.h += Math.atan2(Math.sin(want - c.h), Math.cos(want - c.h)) * 0.5; c.s = Math.min(c.s, speed); G.T += 0.05; G.step(0.05); air = air || c.air; }
      keys(); const n = G.world._pathNear(tk.pts, G.car.x, G.car.z); return { air, past: n.i / N > gap[1], y: G.car.y, h: tk.h(n.i / N), board: document.querySelector("#race-board").textContent }; };
    const fast = run(12, 32), slow = run(12, 13), space = run(14, 34); const ground = G.world.groundMesh.visible; G.startFree(); return { fast, slow, space, groundInSpace: ground, groundBack: G.world.groundMesh.visible, gone: !G.world.trk }; });
  ok("W8-02 Sky Gap: a fast car jumps the gap and lands on the road", r.fast.air && r.fast.past && Math.abs(r.fast.y - r.fast.h) < 1, r.fast);
  ok("W8-03 Sky Gap: a slow car falls and is put back with a penalty", /\+3|penalty|fell/i.test(r.slow.board + JSON.stringify(r.slow)) || !r.slow.past, r.slow);
  ok("W8-04 Space Hopper: jump down to the next island; ground hidden, back after", r.space.air && r.space.past && r.groundInSpace === false && r.groundBack && r.gone, r);
  r = await E(() => { const { BOSSES } = __dd; S.bossBeat = 0; G.bossMenu(); const open = [...document.querySelectorAll("[data-boss]")].filter((b) => !b.disabled).length; document.querySelector('[data-boss="0"]').click(); sim(3.5); const ai = G.mode.ai.length, laps = G.mode.laps; const k = lapTeleport(1); return { n: BOSSES.length, open, ai, laps, k, beat: S.bossBeat, title: document.querySelector("#card h2")?.textContent }; });
  ok("W8-05 boss rivals: 5 bosses, one lap one against one, beating one unlocks the next", r.n === 5 && r.open === 1 && r.ai === 1 && r.k > 0 && r.beat === 1, r);
  r = await E(() => { G.startFree(); G.spawnCop(true); const c0 = !!G.cop; sim(1); const e0 = S.stats.copEscapes; G.setPos(G.cop.x + 300, G.cop.z, 0); G.setPos(-3.5, 120, 0); sim(0.5); return { c0, gone: !G.cop, esc: S.stats.copEscapes - e0 }; });
  ok("W8-06 cop chase: police come, escape far away gives points", r.c0 && r.gone && r.esc === 1, r);
  r = await E(() => { G.startFree(); G.spawnCop(true); const p0 = S.points; G.cop.x = G.car.x + 2; G.cop.z = G.car.z; sim(0.2); return { gone: !G.cop, fine: p0 - S.points }; });
  ok("W8-07 cop chase: caught means a fine", r.gone && r.fine > 0, r);
  r = await E(() => { const { TRAIN, HW } = __dd; G.startTrainRace(); sim(5); const W = G.world, s1 = W.trainSpeed, z1 = W.trainZ; sim(3); const fast = W.trainSpeed > s1 && W.trainZ > z1 + 10; G.setPos(5.5, HW.z1 - 35, 0); G.car.s = 30; W.trainZ = HW.z1 - 120; keys("up"); sim(2); keys(); return { fast, title: document.querySelector("#card h2")?.textContent, best: S.best.train }; });
  ok("W8-08 train race: the express speeds up; reach the end first to win", r.fast && /beat the train/.test(r.title || "") && r.best > 0, r);
  r = await E(() => { const { TRAIN } = __dd; G.startFree(); const W = G.world, z0 = W.trainZ; W.trainWait = 0; sim(2); const moved = Math.abs(W.trainZ - z0); W.trainDir = 1; W.trainWait = 99; G.setPos(TRAIN.x, W.trainZ - 30, 0); sim(0.3); return { moved, pushed: Math.abs(G.car.x - TRAIN.x) > 1.5 || Math.abs(G.car.z - (W.trainZ - 30)) > 1.5 }; });
  ok("W8-09 the train runs on its rails and is solid", r.moved > 20 && r.pushed, r);
  await E(() => { G.world.trainWait = 0; });
  r = await E(() => { const { HILL } = __dd; G.startHill(); sim(3.5); G.setPos(HILL.x + 5, HILL.z + 5, 0); sim(0.3); return { title: document.querySelector("#card h2")?.textContent, best: S.best.hill }; });
  ok("W8-10 king of the hill: reach the top to finish", /King of the Hill|reached the top/.test(r.title || "") && r.best > 0, r);
  r = await E(() => { G.startTag(); sim(0.5); for (const a of G.mode.ai) { G.setPos(a.x - 2, a.z, Math.PI / 2); G.T += 0.05; G.step(0.05); } sim(0.2); return { title: document.querySelector("#card h2")?.textContent }; });
  ok("W8-11 tag: touch all 5 cars to win", /tagged them all/.test(r.title || ""), r);
  r = await E(() => { const { PARK_LV } = __dd; S.parkLv = 0; G.parkMenu(); const n = document.querySelectorAll("[data-pk]").length, open = [...document.querySelectorAll("[data-pk]")].filter((b) => !b.disabled).length; G.startPark(0); sim(0.5); const L = PARK_LV[0], P = { cx: 90, cz: -90 }, h = L.need === "rev" ? L.t[2] + Math.PI : L.t[2]; G.setPos(P.cx + L.t[0], P.cz + L.t[1], h); sim(1.6); return { n, open, lv: S.parkLv, title: document.querySelector("#card h2")?.textContent }; });
  ok("W8-12 parking puzzles: 10 levels, park in the box to pass", r.n === 10 && r.open === 1 && r.lv === 1 && /Parked/.test(r.title || ""), r);
  r = await E(() => { const { LOOP } = __dd; G.startFree(); const l0 = S.stats.loops; G.setPos(LOOP.x - 30, LOOP.z, Math.PI / 2); G.car.s = 20; keys("up"); let maxY = 0, upside = false; for (let i = 0; i < 80; i++) { G.car.h = Math.PI / 2; G.T += 0.05; G.step(0.05); maxY = Math.max(maxY, G.car.y); if (G.car.loop && G.car.y > LOOP.r * 1.8) upside = true; } keys(); const fast = S.stats.loops - l0; G.setPos(LOOP.x - 8, LOOP.z, Math.PI / 2); G.car.loopCd = 0; for (let i = 0; i < 30; i++) { G.car.h = Math.PI / 2; G.car.s = 8; G.T += 0.05; G.step(0.05); } return { fast, slow: S.stats.loops - l0 - fast, maxY, upside, y: G.car.y }; });
  ok("W8-13 loop the loop: fast goes round upside down, slow does not", r.fast === 1 && r.slow === 0 && r.upside && r.maxY > 12 && r.y < 0.5, r);
  r = await E(() => { const { ROLL } = __dd; G.startFree(); const r0 = S.stats.rolls; G.setPos(ROLL.x - 40, ROLL.z, Math.PI / 2); G.car.s = 26; keys("up"); let spun = 0; for (let i = 0; i < 80; i++) { if (!G.car.air) G.car.h = Math.PI / 2; G.car.s = Math.min(G.car.s, 26); G.T += 0.05; G.step(0.05); spun = Math.max(spun, G.car.roll || 0); } keys(); return { rolls: S.stats.rolls - r0, spun, rz: G.car.m.rotation.z }; });
  ok("W8-14 barrel roll ramp: the car spins in the air and lands upright", r.rolls === 1 && r.spun > 6 && Math.abs(r.rz) < 0.2, r);
  r = await E(() => { const { BRIDGE } = __dd; S.car = "hatch"; G.respawnCar(); G.startBridge(); const two = G.car.def.two; sim(2.5); G.setPos(BRIDGE.x0 + 30, BRIDGE.z + 4, Math.PI / 2); sim(1); const back = G.car.x < BRIDGE.x0; G.setPos(BRIDGE.x0 - 3, BRIDGE.z, Math.PI / 2); for (let i = 0; i < 400 && G.mode.kind === "mission"; i++) { const c = G.car; c.z += (BRIDGE.z - c.z) * 0.5; c.h = Math.PI / 2; c.s = 8; G.T += 0.05; G.step(0.05); } return { two, back, best: S.best.bridge, car: S.car, title: document.querySelector("#card h2")?.textContent }; });
  ok("W8-15 balance bridge: two wheels only, a splash sends you back, crossing wins, car given back", r.two && r.back && r.best > 0 && r.car === "hatch" && /bridge|balance/i.test(r.title || ""), r);
  r = await E(() => { G.startFree(); G._cbT = -99; const p0 = S.points; G.comboAdd("jump", 100); G.comboAdd("drift", 100); G.comboAdd("loop", 100); return { n: G._cbN, bonus: S.points - p0, best: S.best.combo }; });
  ok("W8-16 stunt combo: three tricks in a row give a x3 bonus", r.n === 3 && r.bonus >= 300 && r.best >= 3, r);
  r = await E(() => { S.weekly = null; const w = G.weekly(); const key = w.ch[2]; S.stats[key] = (S.stats[key] || 0) + w.n + 1; const p0 = S.points; G.checkWeekly(); const p1 = S.points; G.checkWeekly(); G.openMenu(); return { got: p1 - p0, again: S.points - p1, card: /Weekly|weekly/.test(document.querySelector("#card").textContent) }; });
  ok("W8-17 weekly challenge: done once, +1500, card in the menu", r.got === 1500 && r.again === 0 && r.card, r);
  r = await E(() => { G.settingsMenu(); const has = !!document.querySelector("#st-day"); S.dayCycle = false; document.querySelector("#st-day").click(); G.startFree(); G.tod = 0.9; sim(1); const night = S.night, clock = getComputedStyle(document.querySelector("#clock")).display; G.tod = 0.5; sim(1); const day = !S.night; S.dayCycle = false; S.night = false; G.applyWorldLook(); sim(0.2); return { has, night, day, clock, hidden: getComputedStyle(document.querySelector("#clock")).display }; });
  ok("W8-18 day and night cycle from Settings, with a clock", r.has && r.night && r.day && r.clock === "block" && r.hidden === "none", r);
  r = await E(() => { G.startFree(); G.enterPhoto(); const on = !!G.photo && document.body.classList.contains("photo"); const x0 = G.car.x; sim(1); const frozen = G.car.x === x0; G.takePhoto(); const img = document.querySelector("#photo-shot img")?.getAttribute("src") || ""; document.querySelector("#ps-x")?.click(); G.exitPhoto(); return { on, frozen, img: img.slice(0, 22), off: !G.photo && !document.body.classList.contains("photo") }; });
  ok("W8-19 photo mode: game stops, picture taken, exit", r.on && r.frozen && r.img.startsWith("data:image/png") && r.off, r);
  r = await E(() => { const { eff, CARS } = __dd; const d = CARS.find((c) => c.id === "hatch"); S.tune = { hatch: 0 }; const t0 = eff(d).top, g0 = eff(d).grip; S.tune.hatch = 1; const t1 = eff(d).top, g1 = eff(d).grip; S.tune.hatch = -1; const g2 = eff(d).grip; S.tune.hatch = 0; return { faster: t1 > t0, lessGrip: g1 < g0, moreGrip: g2 > g0 }; });
  ok("W8-20 tuning slider: speed or grip", r.faster && r.lessGrip && r.moreGrip, r);
  r = await E(() => { S.points += 500; S.car = "hatch"; G.respawnCar(); G.garage(true); const snd = document.querySelectorAll("[data-snd]").length; document.querySelector('[data-snd="roar"]').click(); const pack = S.sound.hatch; const p0 = S.points; document.querySelector('[data-roof="3"]').click(); const roof = (S.design.hatch || {}).roof, cost = p0 - S.points; const tune = !!document.querySelector("#g-tune"); G.startFree(); return { snd, pack, roof, cost, tune, cab: !!G.car.m.userData.cab }; });
  ok("W8-21 garage: 4 engine sounds, roof colour designer (50), tuning slider", r.snd === 4 && r.pack === "roar" && r.roof === 3 && r.cost === 50 && r.tune, r);
  r = await E(() => { const { BEACH } = __dd; G.startFree(); const W = G.world; const road = W.onRoad(0, -300) && W.onRoad(120, BEACH.road); G.setPos(60, BEACH.sea - 4, Math.PI); G.car.s = 20; sim(0.5); const slow = G.car.s < 10; G.setPos(60, BEACH.sea - 20, Math.PI); G.car.s = 20; keys("up"); sim(3); keys(); return { road, slow, z: G.car.z, min: BEACH.sea - 26.5, waves: !!W.sea }; });
  ok("W8-22 beach and coast road: roads, the sea slows you and stops you", r.road && r.slow && r.z >= r.min && r.waves, r);
  r = await E(() => { const W = G.world, D = W.desertRoad.pts, k = D.findIndex((q) => q.x < -400); G.startFree(); G.setPos(D[k].x, D[k].z, 0); sim(0.5); const reg = G._region, fogFar = G.scene.fog.far, dune = W.dune(-500, -400), onR = W.onRoad(D[k].x, D[k].z); G.setPos(-3.5, -100, 0); sim(0.3); return { reg, fogFar, dune, onR, after: G._region, far2: G.scene.fog.far }; });
  ok("W8-23 desert dunes: sandstorm fog, dunes, a sand road; clear again outside", r.reg === "desert" && r.fogFar < 600 && r.dune > 0.5 && r.onR && r.after === null && r.far2 >= 700, r);
  r = await E(() => { const W = G.world, P = W.snowPts; G.startFree(); G.setPos(P[120].x, P[120].z, Math.atan2(P[122].x - P[120].x, P[122].z - P[120].z)); sim(0.3); return { reg: G._region, flakes: W.flakes.visible, y: G.car.y, onR: W.onRoad(P[120].x, P[120].z), snowy: W.inSnow(P[120].x, P[120].z) }; });
  ok("W8-24 snow pass: up the mountain road, snowflakes, slippery", r.reg === "snow" && r.flakes && r.y > 8 && r.onR && r.snowy, r);
  r = await E(() => { const { TUNNEL, HILL } = __dd; const W = G.world; G.startFree(); G.setPos(-470, TUNNEL.z, -Math.PI / 2); G.car.s = 18; keys("up"); let maxY = 0, inT = false; for (let i = 0; i < 260 && G.car.x > -735; i++) { const c = G.car; c.h = -Math.PI / 2; c.z += (TUNNEL.z - c.z) * 0.3; G.T += 0.05; G.step(0.05); maxY = Math.max(maxY, c.y); if (W.inTunnel(c.x, c.z)) inT = true; } keys(); let road = 0; for (const p of W.hp) if (Math.abs(p.z - TUNNEL.z) < 8) road = Math.max(road, Math.abs(W.groundAt(p.x, p.z, W.groundAt(p.x, p.z)) - W.groundAt(p.x, p.z))); return { x: G.car.x, maxY, inT, top: W.groundAt(HILL.x, TUNNEL.z), road, cam: G.camera.position.y }; });
  ok("W8-25 tunnel: drive under Sunrise Hill and out the other side", r.x < -720 && r.maxY < 0.5 && r.inT && r.top > 15 && r.road === 0, r);
  r = await E(() => { G.skillMenu(); const ids = ["k-loop", "k-roll", "k-bridge", "k-tag", "k-park", "k-beach", "k-desert", "k-snow", "k-tunnel"].filter((i) => document.getElementById(i)).length; G.racesMenu(); const rs = ["r-boss", "r-train", "r-hill", "r-cop"].filter((i) => document.getElementById(i)).length; G.startFree(); return { ids, rs }; });
  ok("W8-26 menus: 9 new skill and place buttons, 4 new race buttons", r.ids === 9 && r.rs === 4, r);
  r = await E(() => G.lastErr || ""); ok("W8-27 no loop errors after v8 checks", !r, r.slice(0, 300));
  await E(() => { S.car = "hatch"; G.respawnCar(); G.startFree(); yesTraffic(); });

  // ===== v10: flips work the way children press the keys =====
  r = await E(() => { const jump = (ramp, held, race) => { G.startFree(); if (race) G.mode.kind = "race"; S.damage = 0; const f0 = S.stats.flips || 0; G.setPos(ramp.x, ramp.z, ramp.h); G.car.s = ramp.v; keys(...held); let air = 0, maxF = 0;
      for (let i = 0; i < 120; i++) { const c = G.car; c.h = ramp.h; if (!c.air) c.s = ramp.v; G.T += 0.05; G.step(0.05); if (c.air) air += 0.05; maxF = Math.max(maxF, Math.abs(c.flip || 0)); if (air > 0 && !c.air) break; }
      keys(); const o = { air, maxF, flips: (S.stats.flips || 0) - f0, dmg: S.damage, rx: G.car.m.rotation.x, s: G.car.s }; G.mode.kind = "free"; return o; };
    const park = { x: -39, z: 10, h: 0, v: 20 }, big = { x: 400, z: 395, h: Math.PI / 2, v: 30 };
    const o = { parkS: jump(park, ["down"]), parkW: jump(park, ["up"]), parkWS: jump(park, ["up", "down"]), bigS: jump(big, ["down"]), raceW: jump(park, ["up"], true) }; G.checkBadges(); o.badge = !!S.badges.flip; o.fronts = S.stats.frontflips; o.backs = S.stats.backflips; S.damage = 0; G.startFree(); return o; });
  ok("W9-01 hold ⬇ from before a small ramp: one backflip, clean landing", r.parkS.flips === 1 && r.parkS.dmg === 0 && Math.abs(r.parkS.rx) < 0.1, r.parkS);
  ok("W9-02 hold ⬆ from before a small ramp: one frontflip", r.parkW.flips === 1 && r.parkW.dmg === 0 && r.fronts >= 1, r.parkW);
  ok("W9-03 big ramp, hold ⬇: a double backflip, landed clean", r.bigS.flips === 2 && r.bigS.dmg === 0 && r.backs >= 3 && r.bigS.s > 20, r.bigS);
  ok("W9-04 gas and brake held together still flip; in a race the held gas does not flip", r.parkWS.flips === 1 && r.raceW.flips === 0, { WS: r.parkWS, race: r.raceW });
  ok("W9-05 Flip master badge", r.badge, r);
  r = await E(() => { const { MEGA, TRAMPS } = __dd; const jump = (setup, held) => { G.startFree(); S.damage = 0; const st0 = JSON.parse(JSON.stringify(S.stats)); setup(); const v0 = G.car.s, h0 = G.car.h; keys(...held); let air = 0, side = 0; for (let i = 0; i < 140; i++) { const c = G.car; c.h = h0; if (!c.air && air === 0) c.s = v0; G.T += 0.05; G.step(0.05); if (c.air) { air += 0.05; const dx = G.camera.position.x - c.x, dz = G.camera.position.z - c.z; side = Math.max(side, Math.abs(dx * Math.cos(c.h) - dz * Math.sin(c.h))); } if (air > 0 && !c.air) break; } keys(); const d = (k) => (S.stats[k] || 0) - (st0[k] || 0); return { air, flips: d("flips"), spins: d("spins"), cork: d("corkscrews"), tr: d("tramps"), dmg: S.damage, side }; };
    const o = { mega: jump(() => { G.setPos(MEGA.x - 60, MEGA.z, Math.PI / 2); G.car.s = 40; }, ["down", "left"]), tramp: jump(() => { G.setPos(TRAMPS[1][0], TRAMPS[1][1] - 6, 0); G.car.s = 8; }, ["down"]) }; G.checkBadges(); o.spinBadge = !!S.badges.spin5 || (S.stats.spins || 0) < 5; S.damage = 0; G.startFree(); return o; });
  ok("W10-01 mega ramp: flips plus 360 spins make a CORKSCREW", r.mega.air > 1.2 && r.mega.flips >= 1 && r.mega.spins >= 1 && r.mega.cork === 1 && r.mega.dmg === 0, r.mega);
  ok("W10-02 trampoline throws the car up for a double flip", r.tramp.tr === 1 && r.tramp.flips === 2 && r.tramp.dmg === 0, r.tramp);
  ok("W10-03 stunt camera shows the car from the side in the air", r.mega.side > 8, r.mega);
  r = await E(() => { const { OILS } = __dd; G.startFree(); G.setPos(OILS[0][0], OILS[0][1] - 10, 0); G.car.s = 20; const o0 = S.stats.oil || 0; sim(1); const oil = (S.stats.oil || 0) - o0; S.letters = []; const p0 = S.points; for (const L of G.world.letters) { G.startFree(); G.setPos(L.x, L.z, 0); G.car.y = L.y - 0.8; G.car.air = true; G.car.vy = 0; G.T += 0.05; G.step(0.05); } G.checkBadges(); return { oil, n: S.letters.length, gain: S.points - p0, badge: !!S.badges.letters }; });
  ok("W10-04 oil slick spins the car; the 9 RISHDRIVE letters give 2900 points and a badge", r.oil === 1 && r.n === 9 && r.gain >= 2900 && r.badge, r);
  r = await E(() => { G.skillMenu(); const btn = !!document.querySelector("#k-mega") && !!document.querySelector("#k-book"); G.stuntBook(); const book = /Stunt book/.test(document.querySelector("#card").textContent) && /Corkscrews/.test(document.querySelector("#card").textContent); G.settingsMenu(); const cam = !!document.querySelector("#st-scam"); G.startShow(); sim(3.5); for (let i = 0; i < 4; i++) G.comboAdd("flip", 400); sim(91); const medal = /Silver medal/.test(document.querySelector("#card p").textContent); G.startFree(); return { btn, book, cam, medal, air: S.best.air }; });
  ok("W10-05 mega ramp and stunt book buttons, stunt camera setting, stunt show medals, air time record", r.btn && r.book && r.cam && r.medal && r.air > 1, r);
  r = await E(() => G.lastErr || ""); ok("W9-06 no loop errors after flips", !r, r.slice(0, 300));
  r = await E(async () => { const cvs = []; G.scene.traverse((o) => { for (const m of o.material ? [].concat(o.material) : []) if (m.map && m.map.image && m.map.image.getContext) cvs.push(m.map.image); }); cvs.push(G.mapBase.cv);
    const soft = cvs.every((c) => c.getContext("2d").getContextAttributes().willReadFrequently === true); const ext = G.renderer.getContext().getExtension("WEBGL_lose_context"); ext.loseContext(); await new Promise((res) => setTimeout(res, 300)); ext.restoreContext(); await new Promise((res) => setTimeout(res, 1200)); sim(0.5);
    const tex = cvs[0].getContext("2d").getImageData(0, 0, 8, 8).data.some((v, i) => i % 4 !== 3 && v > 0); return { n: cvs.length, soft, tex, lost: G.renderer.getContext().isContextLost(), err: G.lastErr || "" }; });
  ok("W9-07 after a GPU reset the city keeps its colours and the mini map (no black buildings)", r.n > 20 && r.soft && r.tex && !r.lost && !r.err, r);
  // v9: 25 ideas
  r = await E(() => { const { CANYON } = __dd, out = []; for (const [i, car] of [[0, "hatch"], [2, "hatch"], [3, "gt"], [4, "sedan"]]) { S.car = car; G.respawnCar(); S.canyonLv = 4; G.startCanyon(i); sim(3.5); keys("up"); G.nitroTap(); for (let k = 0; k < 600 && G.mode.kind === "mission"; k++) { const c = G.car; c.h = Math.PI / 2; c.z += (CANYON.lanes[i].z - c.z) * 0.3; if (!c.nitroLatch && S.nitro > 30 && !c.air) G.nitroTap(); G.T += 0.05; G.step(0.05); } keys(); out.push(document.querySelector("#card h2")?.textContent || ""); } S.car = "hatch"; G.respawnCar(); return out; });
  ok("W9-08 Stunt Canyon: 20 m, 40 m, 50 m and the 8-bus jump can be cleared", r.every((t) => /cleared/.test(t)), r);
  r = await E(() => { const { CANYON } = __dd; S.car = "cycle"; G.respawnCar(); G.startCanyon(1); sim(3.5); keys("up"); let splash = false; for (let k = 0; k < 500; k++) { const c = G.car; c.h = Math.PI / 2; c.z += (CANYON.lanes[1].z - c.z) * 0.3; G.T += 0.05; G.step(0.05); if (/try 2/.test(document.querySelector("#race-board").textContent)) { splash = true; break; } } keys(); const back = G.car.x < CANYON.x0; G.startFree(); S.car = "hatch"; G.respawnCar(); return { splash, back }; });
  ok("W9-09 Stunt Canyon: too slow means a splash in the river and a new try", r.splash && r.back, r);
  r = await E(() => { const { CANYON } = __dd; G.startFree(); const L = CANYON.lanes[0], r0 = S.stats.rings || 0; G.setPos(CANYON.x0 + 100, L.z, Math.PI / 2); for (let i = 0; i < 80; i++) { G.car.h = Math.PI / 2; if (!G.car.air) G.car.s = 95 / 3.6; G.T += 0.05; G.step(0.05); } return (S.stats.rings || 0) - r0; });
  ok("W9-10 ring of fire over the gap", r === 1, r);
  r = await E(() => { S.cySkip = {}; S.canyonLv = 0; G.canyonMenu(); const lanes = document.querySelectorAll("[data-cy]").length, open0 = [...document.querySelectorAll("[data-cy]")].filter((b) => !b.disabled).length; document.querySelector('[data-cyskip="0"]').click(); const open1 = [...document.querySelectorAll("[data-cy]")].filter((b) => !b.disabled).length; S.tracks = {}; S.tskip = {}; G.tracksMenu(); const tsk = document.querySelectorAll("[data-tskip]").length; document.querySelector('[data-tskip="0"]').click(); const topen = [...document.querySelectorAll("[data-trk]")].filter((b) => !b.disabled).length; return { lanes, open0, open1, tsk, topen }; });
  ok("W9-11 Skip buttons: skip a track challenge or a canyon jump to open the next", r.lanes === 5 && r.open0 === 1 && r.open1 === 2 && r.tsk === 1 && r.topen === 2, r);
  r = await E(() => { G.startFree(); G.setPos(4.5, 376, 0); G.car.s = 15; const b0 = S.stats.boosts || 0; sim(0.5); const boost = (S.stats.boosts || 0) - b0; const p = G.world.pickups.find((q) => q.type === "coin" && q.gone <= 0), c0 = S.stats.coins || 0; G.setPos(p.x, p.z, 0); G.car.y = p.y - 0.8; G.car.air = true; G.car.vy = 0; sim(0.05); const coin = (S.stats.coins || 0) - c0; S.nitro = 5; const q = G.world.pickups.find((z) => z.type === "nitro" && z.gone <= 0); G.setPos(q.x, q.z, 0); sim(0.1); return { boost, coin, nitro: S.nitro, coins: G.world.pickups.filter((z) => z.type === "coin").length }; });
  ok("W9-12 boost pads, sky coins and nitro bottles", r.boost === 1 && r.coin === 1 && r.nitro >= 100 && r.coins > 30, r);
  r = await E(() => { G.startFree(); G._slowCd = 0; G.slowmo(); const c = G.car; c.s = 20; const z0 = c.z; sim(0.5); const moved = c.z - z0; sim(3); return { cls: !document.body.classList.contains("slowmo"), moved }; });
  ok("W9-13 slow motion for 3 seconds", r.moved < 5 && r.moved > 2 && r.cls, r);
  r = await E(() => { S.car = "bike"; G.respawnCar(); G.startFree(); G.setPos(-3.5, -150, 0); G.car.s = 15; const w0 = S.stats.wheelies || 0; keys("up", "wheelie"); let rx = 0; sim(2, 0.05); rx = G.car.m.rotation.x; keys("up"); sim(0.2); keys(); S.car = "hatch"; G.respawnCar(); return { rx, w: (S.stats.wheelies || 0) - w0 }; });
  ok("W9-14 wheelie on a bike with X", r.rx < -0.3 && r.w === 1, r);
  r = await E(() => { G.startThief(); sim(3.5); const th = G.mode.ai[0], z0 = th.z; sim(3); const moved = Math.abs(th.z - z0) + Math.abs(th.x); G.setPos(th.x + Math.sin(th.h) * 2, th.z + Math.cos(th.h) * 2, th.h + Math.PI); sim(0.1); return { moved, t: document.querySelector("#card h2")?.textContent }; });
  ok("W9-15 catch the thief: the thief runs, touch it to win", r.moved > 20 && /Caught/.test(r.t || ""), r);
  r = await E(() => { G.startRush(); sim(3.5); for (const q of G.mode.rush.slice()) { G.setPos(q.x, q.z, 0); sim(0.1); } return document.querySelector("#card h2")?.textContent; });
  ok("W9-16 checkpoint rush: 8 checkpoints", /Checkpoint|checkpoints/.test(r || ""), r);
  r = await E(() => { G.startShow(); sim(3.5); G.comboAdd("jump", 100); G.comboAdd("flip", 400); const sc = G.mode.show; sim(91); const t1 = document.querySelector("#card h2")?.textContent; G.startFlipChallenge(); sim(3.5); S.stats.flips = (S.stats.flips || 0) + 3; sim(0.1); return { sc, t1, t2: document.querySelector("#card h2")?.textContent }; });
  ok("W9-17 stunt show scores tricks for 90 s; flip challenge", r.sc === 500 && /stunt show/i.test(r.t1 || "") && /Flip champion/.test(r.t2 || ""), r);
  r = await E(() => { G.startFree(); const cw = G.world.cows[0]; G.setPos(cw.x - 8, cw.z, Math.PI / 2); G.horn(); sim(1); const moved = Math.hypot(cw.x - cw.hx, cw.z - cw.hz); S.rain = true; G.applyWorldLook(); G._ltT = 0.01; const l0 = S.stats.lightning || 0; sim(0.5); const light = (S.stats.lightning || 0) - l0; S.rain = false; G.applyWorldLook(); G.world.plane.t = 5; sim(0.2); S.night = true; G._ssT = 0.01; const s0 = S.stats.shootingStars || 0; sim(0.2); const ss = (S.stats.shootingStars || 0) - s0; S.night = false; G.applyWorldLook(); const f0 = S.stats.fireworks || 0; G.done("🏆 Test", "x"); return { cows: G.world.cows.length, moved, light, plane: G.world.plane.g.visible, balloons: G.world.balloons.length, ss, fw: (S.stats.fireworks || 0) - f0 }; });
  ok("W9-18 cows move when you honk; lightning, plane, balloons, shooting stars, fireworks", r.cows === 4 && r.moved > 1 && r.light === 1 && r.plane && r.balloons === 6 && r.ss === 1 && r.fw === 1, r);
  r = await E(() => { S.points += 3000; S.car = "hatch"; G.respawnCar(); G.garage(true); const p0 = S.points; document.querySelector('[data-spp="gold"]').click(); const gold = S.special.hatch === "gold" && p0 - S.points === 500; document.querySelector('[data-spp="rainbow"]').click(); G.startFree(); sim(0.2); const c1 = G.car.m.userData.body.color.getHex(); sim(1); const rainbow = c1 !== G.car.m.userData.body.color.getHex(); G.garage(true); document.querySelector('[data-smk="2"]').click(); document.querySelector('[data-trl="1"]').click(); G.startFree(); G.setPos(-3.5, -150, 0); G.car.s = 20; keys("up"); sim(1.5); keys(); const trail = !!G.trailM && G.trailM.userData.pts.length > 10; G.garage(true); document.querySelector('[data-spp=""]').click(); document.querySelector('[data-trl="-1"]').click(); G.startFree(); sim(0.1); return { gold, rainbow, smoke: S.smoke.hatch, trail, off: !G.trailM }; });
  ok("W9-19 garage: gold, chrome and rainbow paint, drift smoke colour, light trail", r.gold && r.rainbow && r.smoke === 2 && r.trail && r.off, r);
  r = await E(() => { G.settingsMenu(); document.querySelector('[data-hrn="duck"]').click(); const horn = S.horn; document.querySelector('[data-rad="2"]').click(); const on = !!G._radioI; G.setRadio(0); S.horn = "classic"; return { horn, on, off: !G._radioI, n: __dd.RADIO.length }; });
  ok("W9-20 4 horns and a radio with 3 stations", r.horn === "duck" && r.on && r.off && r.n === 3, r);
  r = await E(() => { S.spin = null; G.openMenu(); const btn = !!document.querySelector("#m-spin"); document.querySelector("#m-spin").click(); const won = G.lastSpin; G.openMenu(); return { btn, won, again: !document.querySelector("#m-spin") }; });
  ok("W9-21 daily spin wheel, once a day", r.btn && !!r.won && r.again, r);
  r = await E(() => { G.startFree(); G.setPos(4.5, 250, 0); for (let i = 0; i < 20; i++) { G.car.s = 60; G.T += 0.05; G.step(0.05); } G.checkBadges(); return { top: S.best.top, badge: !!S.badges.speed200 }; });
  ok("W9-22 top speed record and the 200 club badge", r.top >= 200 && r.badge, r);
  r = await E(() => { G.skillMenu(); const a = ["k-canyon", "k-show", "k-flip"].filter((i) => document.getElementById(i)).length; G.missionsMenu(); const m = ["mi-thief", "mi-rush"].filter((i) => document.getElementById(i)).length; G.startFree(); return { a, m, err: G.lastErr || "" }; });
  ok("W9-23 new buttons in Skill Park and Missions; no loop errors", r.a === 3 && r.m === 2 && !r.err, r);
  await E(() => { S.car = "hatch"; S.damage = 0; G.respawnCar(); G.startFree(); });


  // Y. Save survives reload
  const saved = await E(() => { __dd.save(); return S.points; });
  await p.reload(); await p.waitForFunction(() => window.__dd, null, { timeout: 90000 }); await p.evaluate(HELPERS);
  r = await E(() => ({ pts: S.points, car: S.car, lic: S.licence, plate: S.plate.hatch, badges: Object.keys(S.badges).length })); ok("Y1 save persists", r.pts === saved && r.lic && r.plate === "KEERTI 1" && r.badges >= 5, r);

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
  r = await mp.evaluate(() => { const ids = ["t-left", "t-right", "t-brake", "t-gas", "t-hand", "t-nitro", "t-drift", "dash", "map", "top-left", "top-right"], R = ids.map((i) => [i, document.getElementById(i).getBoundingClientRect()]), bad = [];
    for (let i = 0; i < R.length; i++) for (let j = i + 1; j < R.length; j++) { const [a, p] = R[i], [b, q] = R[j]; if (p.left < q.right && q.left < p.right && p.top < q.bottom && q.top < p.bottom) bad.push(a + "/" + b); } return bad; });
  ok("ZM1b phone HUD has no overlaps", r.length === 0, r);
  await mp.waitForTimeout(2000); await mp.screenshot({ path: `${SHOTS}/09-phone-drive.png` });
  ok("ZM2 no phone errors", !errs.some((e) => e.startsWith("M ")), errs);

  console.log(`\nRESULT ${pass} passed, ${fail} failed`); await b.close(); process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("CRASH", e); process.exit(2); });
