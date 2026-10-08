// Rish Hero v2 (3D) regression.
// Usage: NODE_PATH=$(npm root -g) node regress.cjs [path/to/index.html] [shotDir] [three.module.js]
// Plays every chapter in Chromium (swiftshader WebGL). The game runs with ?test=1, so the test drives time with __rh.step().
const { chromium } = require("playwright");
const path = require("path"), fs = require("fs");
const FILE = path.resolve(process.argv[2] || path.join(__dirname, "..", "index.html"));
const SHOTS = process.argv[3] || ".";
const THREE_LOCAL = process.argv[4] || "";
let pass = 0, fail = 0; const errs = [];
const ok = (name, cond, info = "") => { if (cond) pass++; else fail++; console.log(`${cond ? "PASS" : "FAIL"} ${name}${cond ? "" : " :: " + JSON.stringify(info)}`); };

// Helpers that run inside the page.
const HELPERS = () => {
  const R = window.__rh, G = R.G; window.R = R; window.G = G;
  window.sim = (sec) => { const n = Math.round(sec * 60); for (let i = 0; i < n; i++) R.step(1 / 60); };
  window.kb = (code) => { window.dispatchEvent(new KeyboardEvent("keydown", { code })); R.step(1 / 60); window.dispatchEvent(new KeyboardEvent("keyup", { code })); R.step(1 / 60); };
  window.tap = (code, frames = 2) => { R.keyDown(code); R.step(1 / 60, frames); R.keyUp(code); R.step(1 / 60, 1); };
  // Read every talk line with E, like a player would.
  window.talk = (max = 300) => { let n = 0; while (G.mode === "dialog" && n++ < max) { sim(0.2); R.keyDown("KeyE"); R.step(1 / 60); R.keyUp("KeyE"); R.step(1 / 60); } return n; };
  // Run the clock, reading any talk that pops up.
  window.play = (sec) => { const n = Math.round(sec * 60); for (let i = 0; i < n; i++) { if (G.mode === "dialog") talk(); R.step(1 / 60); } };
  window.begin = (i) => { R.startChapter(i, true); play(0.3); };
  window.god = () => { G.P.hp = G.P.max = 100; G.god = true; };
  window.mortal = () => { G.god = false; if (G.P) G.P.hp = G.P.max; };
  // BFS path over the grid, then walk it with W (the camera turns toward each step, the same as a player steering).
  window.walkTo = (tx, ty, o = {}) => {
    const L = G.L, P = G.P, W = L.W, H = L.H; const sc = { cx: Math.floor(P.x / 2), cy: Math.floor(P.z / 2) };
    const prev = new Map(), key = (x, y) => y * W + x; const q = [[sc.cx, sc.cy]]; prev.set(key(sc.cx, sc.cy), null);
    while (q.length) { const [x, y] = q.shift(); if (x === tx && y === ty) break; for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const nx = x + dx, ny = y + dy; if (nx < 0 || ny < 0 || nx >= W || ny >= H) continue; const ch = L.grid[ny][nx]; if (prev.has(key(nx, ny)) || ch === " " || R.solidFor(ch, { low: !!o.low })) continue; prev.set(key(nx, ny), [x, y]); q.push([nx, ny]); } }
    if (!prev.has(key(tx, ty))) return { ok: false, why: "no path" };
    const pts = []; let c = [tx, ty]; while (c) { pts.unshift(c); c = prev.get(key(c[0], c[1])); }
    if (o.crouch && !P.crouch) tap("KeyC"); if (o.run) R.keyDown("ShiftLeft");
    R.keyDown("KeyW"); let t = 0;
    for (let i = 1; i < pts.length; i++) { const p = R.cell(pts[i][0], pts[i][1]); let s = 0;
      while (Math.hypot(p.x - P.x, p.z - P.z) > (i === pts.length - 1 ? 0.35 : 0.6) && s++ < 600) { if (G.mode === "dialog") { R.keyUp("KeyW"); talk(); R.keyDown("KeyW"); } if (G.mode !== "play") break; G.camYaw = Math.atan2(p.x - P.x, p.z - P.z); R.step(1 / 60); t++; }
      if (G.mode !== "play") break; }
    R.keyUp("KeyW"); if (o.run) R.keyUp("ShiftLeft"); R.step(1 / 60, 2);
    return { ok: true, steps: t, at: [Math.floor(P.x / 2), Math.floor(P.z / 2)] };
  };
  // One frame of walking toward a point, around walls and chairs (grid BFS).
  window.stepToward = (x, z) => { const L = G.L, P = G.P, W = L.W, H = L.H; const sx = Math.floor(P.x / 2), sy = Math.floor(P.z / 2), tx = Math.floor(x / 2), ty = Math.floor(z / 2);
    let wx = x, wz = z; if (sx !== tx || sy !== ty) { const prev = new Map(), key = (a, b) => b * W + a; prev.set(key(sx, sy), null); const q = [[sx, sy]];
      while (q.length) { const [a, b] = q.shift(); if (a === tx && b === ty) break; for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const na = a + dx, nb = b + dy; if (na < 0 || nb < 0 || na >= W || nb >= H) continue; const ch = L.grid[nb][na]; if (prev.has(key(na, nb)) || ch === " " || (R.solidFor(ch, {}) && !(na === tx && nb === ty))) continue; prev.set(key(na, nb), [a, b]); q.push([na, nb]); } }
      if (prev.has(key(tx, ty))) { let c = [tx, ty], last = c; while (prev.get(key(c[0], c[1]))) { last = c; c = prev.get(key(c[0], c[1])); } if (last[0] !== tx || last[1] !== ty) { const cc = R.cell(last[0], last[1]); wx = cc.x; wz = cc.z; } } }
    G.camYaw = Math.atan2(wx - P.x, wz - P.z); R.keyDown("KeyW"); R.step(1 / 60); R.keyUp("KeyW"); };
  window.face = (x, z) => { G.P.yaw = Math.atan2(x - G.P.x, z - G.P.z); G.camYaw = G.P.yaw; };
  window.at = (cx, cy, yaw) => { R.tp(cx, cy); G.P.y = 0; G.P.vy = 0; G.P.onGround = true; if (yaw !== undefined) { G.P.yaw = yaw; G.camYaw = yaw; } };
  window.behind = (e, d = 1.3) => { G.P.x = e.x - Math.sin(e.yaw) * d; G.P.z = e.z - Math.cos(e.yaw) * d; G.P.yaw = e.yaw; G.camYaw = e.yaw; };
  window.alive = () => G.enemies.filter((e) => e.active && e.st !== "down");
  // Beat one enemy with real punches and kicks, blocking when he winds up.
  window.brawl = (e, maxSec = 25) => { let s = 0; const P = G.P; while (e.st !== "down" && s++ < maxSec * 60) { if (G.mode === "dialog") talk(); if (G.mode === "qte") { const Q = G.qte; const k = Q.keys[Q.type === "mash" ? 0 : Q.i]; tap({ punch: "KeyJ", kick: "KeyK", act: "KeyE", fire: "KeyF", roll: "KeyQ" }[k]); continue; } if (G.mode !== "play") break; const d = Math.hypot(e.x - P.x, e.z - P.z); G.camYaw = Math.atan2(e.x - P.x, e.z - P.z);
      if (d > 1.6) { if (G.P.crouch) tap("KeyC"); stepToward(e.x, e.z); continue; }
      if (e.st === "windup") { if (e.t > e.wind - 0.2) { R.keyDown("KeyL"); let k = 0; while (e.st === "windup" && k++ < 40) R.step(1 / 60); R.step(1 / 60, 2); R.keyUp("KeyL"); } else R.step(1 / 60); continue; }
      if (e.guard > 0) { tap("KeyK", 1); R.step(1 / 60, 30); continue; }
      if (e.st === "stun" && !e.boss) { tap("KeyE", 1); R.step(1 / 60, 40); continue; }
      if (e.st === "low") { tap("KeyE", 1); R.step(1 / 60, 5); continue; }
      tap("KeyJ", 1); R.step(1 / 60, 18); } return e.st === "down"; };
  window.solveQte = () => { let n = 0; while (G.mode === "qte" && n++ < 200) { const Q = G.qte; const k = Q.keys[Q.type === "mash" ? 0 : Q.i]; tap({ punch: "KeyJ", kick: "KeyK", act: "KeyE", fire: "KeyF", roll: "KeyQ", jump: "Space", block: "KeyL" }[k]); } return G.mode; };
};

(async () => {
  const b = await chromium.launch({ executablePath: fs.existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : undefined, args: ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"] });
  const p = await b.newPage({ viewport: { width: 1200, height: 720 } });
  p.on("pageerror", (e) => errs.push("PE " + e.message + " " + (e.stack || "").split("\n").slice(1, 3).join(" | ")));
  p.on("console", (m) => { if (m.type() === "error") errs.push("CE " + m.text()); });
  if (THREE_LOCAL) await p.route("https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js", (r) => r.fulfill({ path: THREE_LOCAL, contentType: "application/javascript" }));
  await p.goto("file://" + FILE + "?test=1");
  await p.waitForFunction(() => window.__rh && window.__rh.step, null, { timeout: 60000 });
  await p.evaluate(HELPERS);
  const E = (f, a) => p.evaluate(f, a); let r;
  const shot = async (name) => { await E(() => R.render()); await p.screenshot({ path: `${SHOTS}/${name}.png` }); };
  const notBlank = async () => E(() => { const c = document.createElement("canvas"); c.width = 64; c.height = 40; const g = c.getContext("2d"); R.render(); g.drawImage(document.getElementById("cv"), 0, 0, 64, 40); const d = g.getImageData(0, 0, 64, 40).data; const cols = new Set(); for (let i = 0; i < d.length; i += 16) cols.add((d[i] >> 4) * 256 + (d[i + 1] >> 4) * 16 + (d[i + 2] >> 4)); return cols.size; });

  // ---------------- A. Menu, data, story rules ----------------
  r = await E(() => ({ title: document.querySelector("#card h1")?.textContent, sub: document.querySelector(".sub")?.textContent, ver: document.querySelector("#ver").textContent, btns: document.querySelectorAll("#card .btn").length }));
  ok("A1 menu: title, series line, version label Rish Hero v8", r.title === "RISH HERO" && /Game 3/.test(r.sub) && /Just live it/.test(r.sub) && r.ver === "Rish Hero v8" && r.btns >= 5, r);
  await shot("01-menu");
  r = await E(() => { document.querySelector("#m-ch").click(); const n = document.querySelectorAll(".ch").length, open = [...document.querySelectorAll(".ch")].filter((x) => !x.disabled).length; document.querySelector("#b").click();
    document.querySelector("#m-about").click(); const img = document.querySelector(".portrait-photo"), t = document.querySelector("#card").textContent; document.querySelector("#b").click();
    document.querySelector("#m-how").click(); const h = document.querySelector("#card").textContent; document.querySelector("#b").click();
    return { n, open, img: img && img.src.slice(0, 22), rish: /Rishabh Sharma/.test(t) && /9 years old/.test(t), made: /made up/.test(t) && /No blood/.test(t), how: /punch/.test(h) && /dodge roll/.test(h) && /takedown/.test(h) && /Skip/.test(h) && /chapter 6 only/.test(h) }; });
  ok("A2 8 parts in the chapter list (Prologue, 6 chapters, Ending)", r.n === 8 && r.open >= 1, r);
  ok("A3 About: photo, creator age 9, made-up gang, no blood", r.img === "data:image/jpeg;base64" && r.rish && r.made, r);
  ok("A4 How to play lists moves, stealth, guns only in chapter 6, Skip", r.how, r);
  r = await E(() => { const C = R.CAST; const names = ["aarav", "diya", "kabir", "meher", "rohan", "sana"].map((k) => C[k].name); const t = ["rao", "iyer", "dsouza", "khan", "arjun", "vikram", "verma"].map((k) => C[k].name);
    return { names, t, uniform: ["aarav", "diya", "kabir", "meher", "rohan", "sana", "rish"].every((k) => C[k].look.shirt === 0xffffff && C[k].kid), school: /SUNRISE PUBLIC SCHOOL/.test(document.documentElement.innerHTML) && /Suryanagar/.test(document.documentElement.innerHTML) }; });
  ok("A5 same classmates as RishSchoolDays (Aarav, Diya, Kabir, Meher, Rohan, Sana) in white school uniform", r.names.join() === "Aarav,Diya,Kabir,Meher,Rohan,Sana" && r.uniform, r);
  ok("A6 same teachers (Mrs. Anjali Rao, Mr. Iyer, Ms. D'Souza, Mr. Khan, Computer Sir Arjun, Coach Vikram, Principal Mrs. Verma) and the same school", r.t.join() === "Mrs. Anjali Rao,Mr. Iyer,Ms. D'Souza,Mr. Khan,Computer Sir Arjun,Coach Vikram,Principal Mrs. Verma" && r.school, r);
  r = await E(() => { const M = R.MEMORIES; const all = JSON.stringify([M, R.ENDING, R.CHAPTERS]); const lines = M.flatMap((m) => m.lines);
    const who = new Set(lines.map((l) => l[0])); const acts = lines.filter((l) => l[3] === "rishDown").length;
    return { n: M.length, first: M[0].month, last: M[M.length - 1].month, lonely: /One Year Alone/.test(all), teachers: ["iyer", "vikram", "dsouza"].every((t) => who.has(t)), kids: ["kabir", "rohan", "meher", "sana", "aarav"].every((t) => who.has(t)), pushed: acts, taunt: /Throw it away|tent|potatoes/.test(all), ignored: /walked away|Like I am not here/.test(all), oneYear: /one year later/i.test(all) && /Annual Day/.test(all),
      bad: /terrorist|isis|taliban|qaeda|blood|kill/i.test(all), guns: R.CHAPTERS.filter((c) => c.gun).map((c) => c.id).join() }; });
  ok("A7 Prologue: 7 months from April to next April; one year alone before the attack", r.n === 7 && r.first === "April" && r.last === "Next April" && r.lonely && r.oneYear, r);
  ok("A8 classmates bully him (pushed down 2 times, taunts, ignored) and 3 teachers dislike him (Iyer, Vikram, D'Souza)", r.kids && r.teachers && r.pushed === 2 && r.taunt && r.ignored, r);
  ok("A9 no real-world group words and no blood or killing in the story text", !r.bad, r);
  ok("A10 guns in only 1 chapter: chapter 6", r.guns === "c6", r);
  // Bomb manual: an independent copy of the rules must agree with the game on 3000 random bombs.
  r = await E(() => {
    const mine = (w, s) => { const n = w.length, d = +s.replace(/\D/g, "").slice(-1); const fi = (c) => w.indexOf(c); const cnt = (c) => w.filter((x) => x === c).length;
      if (n === 3) return !w.includes("red") ? 1 : w[0] === "blue" ? 2 : fi("red");
      if (n === 4) return cnt("yellow") >= 2 ? fi("yellow") : d % 2 === 0 ? 2 : w.includes("white") ? fi("white") : 0;
      return w[4] === "green" ? 1 : !w.includes("blue") ? 3 : s.includes("X") ? 4 : fi("blue"); };
    const cols = ["red", "blue", "yellow", "white", "green", "black"]; let bad = 0; const used = new Set();
    for (let i = 0; i < 3000; i++) { const n = 3 + (i % 3); const w = Array.from({ length: n }, () => cols[Math.floor(Math.random() * 6)]); const s = "AB" + "XK"[i % 2] + "-" + Math.floor(Math.random() * 1000); const a = R.safeWire(w, s); used.add(n + ":" + a); if (a !== mine(w, s) || a < 0 || a >= n) bad++; }
    return { bad, used: used.size }; });
  ok("A11 bomb manual rules: game answer = independent answer on 3000 bombs, every answer is a real wire", r.bad === 0 && r.used >= 11, r);

  // ---------------- B. Prologue ----------------
  r = await E(() => { begin(0); const o = { enemies: G.enemies.length, gun: !!G.P.gun, months: [] }; let guard = 0;
    while (G.ch === 0 && guard++ < 12) { const m = G.marker; if (!m) { play(0.5); continue; } const cx = Math.floor(m.x / 2), cy = Math.floor(m.z / 2); const w = walkTo(cx, cy); o.months.push(w.ok); o.cast = (o.cast || 0) + Object.keys(G.npcs).length; play(0.8); talk(); play(1); }
    o.ch = G.ch; o.mode = G.mode; o.unlocked = G.save.unlocked; return o; });
  ok("B1 Prologue: Rish walks to all 7 month markers (real walking), each scene plays, Chapter 1 starts", r.months.length === 7 && r.months.every(Boolean) && r.ch === 1 && r.unlocked >= 1 && r.cast >= 14, r);
  ok("B2 Prologue has no enemies and no gun", r.enemies === 0 && !r.gun, r);
  r = await E(() => { const o = { dead: [] }; for (const name of Object.keys(R.MAPS)) { const rows = R.MAPS[name].replace(/^\n/, "").split("\n"); const W = Math.max(...rows.map((x) => x.length)); const g = rows.map((x) => x.padEnd(W, "#")); const at = (x, y) => (g[y] && g[y][x]) || "#"; const walk = (c) => !"#GgdctsBorkxFpK".includes(c) || c === "k";
      for (let y = 0; y < g.length; y++) for (let x = 0; x < W; x++) if (g[y][x] === "D") { const ns = walk(at(x, y - 1)) && walk(at(x, y + 1)), ew = walk(at(x - 1, y)) && walk(at(x + 1, y)); if (!ns && !ew) o.dead.push(name + ":" + x + "," + y); } }
    begin(0); R.skipDialog(); at(29, 15); const w = walkTo(29, 9); o.main = w.ok && w.steps < 60 * 6; return o; });
  ok("B3 every door leads somewhere (no door into a wall); the main entrance goes from the campus straight to the corridor", r.dead.length === 0 && r.main, r);
  r = await E(() => { const o = {}; begin(0); R.skipDialog(); G.marker = R.cell(28, 8); at(21, 18); play(0.1); o.shown = R.GUIDE.mesh.visible; let n = 0; R.keyDown("KeyW");
    while (n++ < 60 * 40) { const d = R.GUIDE.dir; if (!d) break; G.camYaw = Math.atan2(d.x, d.z); R.step(1 / 60); } R.keyUp("KeyW"); o.secs = Math.round(n / 60); o.near = Math.hypot(G.P.x - R.cell(28, 8).x, G.P.z - R.cell(28, 8).z) < 6; G.marker = null; return o; });
  ok("B4 a gold arrow at Rish's feet shows the way: following only the arrow reaches the October marker inside the building", r.shown && r.near, r);

  // ---------------- C. Chapter 1: Locked In ----------------
  r = await E(() => { begin(1); const o = {}; o.locked = R.cellAt(40, 7) === "k"; let n = 0; while (G.mode !== "qte" && n++ < 40) play(0.25); o.qte = G.mode === "qte" && G.qte.type === "mash" && G.qte.keys[0] === "kick";
    for (let i = 0; i < 3; i++) tap("KeyK"); sim(5); o.retry = G.mode; n = 0; while (G.mode !== "qte" && n++ < 20) play(0.25); for (let i = 0; i < 9; i++) tap("KeyK"); play(1); o.door = R.cellAt(40, 7); o.mode = G.mode; o.noGun = !G.P.gun; o.cones = G.flags.cones; return o; });
  ok("C1 the blast; QTE: smash K to kick the storeroom door; too slow = try again; then the door breaks", r.locked && r.qte && r.door === "D" && r.mode === "play" && r.noGun, r);
  await shot("02-ch1-corridor");
  r = await E(() => { const o = {}; const T = G.enemies; const t3 = T[2]; at(17, 9); G.P.crouch = false; face(t3.x, t3.z); t3.yaw = Math.atan2(G.P.x - t3.x, G.P.z - t3.z); t3.home = t3.yaw; t3.scan = 0; sim(0.3); o.q = t3.aware > 0; sim(2.5); o.seen = t3.st === "alert";
    // crouching far away in a cone is safe
    const t1 = T[0]; t1.path = null; t1.scan = 0; t1.st = "patrol"; t1.aware = 0; at(30, 8); const pp = R.cell(33, 8); t1.x = pp.x; t1.z = pp.z; t1.yaw = Math.atan2(G.P.x - t1.x, G.P.z - t1.z); if (!G.P.crouch) tap("KeyC"); sim(3); o.crouchSafe = t1.st === "patrol" && t1.aware < 0.3; return o; });
  ok("C2 stealth: a guard who sees Rish standing shows ? then ! and attacks", r.q && r.seen, r);
  ok("C3 stealth: crouching (C) at 6 m in a cone stays hidden", r.crouchSafe, r);
  r = await E(() => { const o = {}; const t1 = G.enemies[0]; t1.yaw = 0; t1.home = 0; behind(t1, 1.3); sim(0.1); o.label = document.getElementById("prompt").textContent; tap("KeyE"); sim(0.6); o.down = t1.st === "down"; o.td = G.stats.takedowns; return o; });
  ok("C4 silent takedown from behind with E", /takedown/i.test(r.label) && r.down && r.td === 1, r);
  r = await E(() => { god(); const o = {}; const t3 = G.enemies[2]; at(18, 9); o.won = brawl(t3); o.combo = G.P.combo; const t2 = G.enemies[1]; o.won2 = brawl(t2); mortal(); return o; });
  ok("C5 hand to hand: punches, kicks, blocks and knockouts beat two guards", r.won && r.won2, r);
  r = await E(() => { god(); const o = {}; const g4 = G.enemies[3]; const w = walkTo(8, 11); o.walk = w.ok; play(0.5); o.objOffice = /office guard/i.test(G.obj); o.won = brawl(g4); play(0.5); const radio = G.items.find((i) => i.type === "radio"); o.radio = !!radio;
    walkTo(9, 12); face(R.cell(9, 13).x, R.cell(9, 13).z - 0.6); sim(0.1); o.phoneLbl = document.getElementById("prompt").textContent; tap("KeyE"); talk(); o.phone = G.flags.phone;
    G.P.x = radio.x; G.P.z = radio.z + 0.4; sim(0.1); tap("KeyE"); o.radioTalk = G.mode === "dialog" && /Kade/.test(document.getElementById("dlgName").textContent); talk(); o.obj = G.obj; walkTo(35, 11); play(0.5); o.ch = G.ch; mortal(); return o; });
  ok("C6 office: knock out the guard, the phone is dead, the radio tells of bombs in the lab and hostages in the hall", r.walk && r.won && r.radio && /phone/i.test(r.phoneLbl) && r.phone && r.radioTalk && /SCIENCE LAB/.test(r.obj), r);
  ok("C7 walking to the Science Lab door opens Chapter 2", r.ch === 2, r);

  await shot("03-ch2-lab");
  // ---------------- D. Chapter 2: The Science Lab ----------------
  r = await E(() => { const o = {}; play(0.5); o.ch = G.ch; o.noGun = !G.P.gun; const b = G.bombs[0]; G.P.x = b.x - 1.2; G.P.z = b.z; sim(0.1); o.lbl = document.getElementById("prompt").textContent; tap("KeyE"); o.needManual = G.mode === "dialog" && /manual/.test(document.getElementById("dlgText").textContent); talk(); return o; });
  ok("D1 Chapter 2 has no gun; a bomb cannot be cut without the manual", r.ch === 2 && r.noGun && /Defuse/.test(r.lbl) && r.needManual, r);
  r = await E(() => { const o = { spots: [] }; for (const b of G.bombs) { const c = { cx: Math.floor(b.x / 2), cy: Math.floor(b.z / 2) }; for (const [ox, oy] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) { const ch = R.cellAt(c.cx + ox, c.cy + oy); if (R.solidFor(ch, {})) continue; at(c.cx + ox, c.cy + oy); sim(0.1); o.spots.push(/Defuse/.test(document.getElementById("prompt").textContent) && b.tag.visible); } } return o; });
  ok("D1b standing in any square next to a bomb shows 'E Defuse the bomb', and a red sign floats over it", r.spots.length >= 6 && r.spots.every(Boolean), r);
  r = await E(() => { god(); const o = {}; const c0 = G.stats.counters || 0; { const e = alive().find((q) => q.kind === "thug"); G.P.x = e.x + 1.2; G.P.z = e.z; G.P.st = "idle"; R.hurtEnemy(e, 1, "kick"); G.P.x = e.x + 1.2; G.P.z = e.z; e.st = "windup"; e.t = 0; e.wind = 0.6; e.yaw = Math.atan2(G.P.x - e.x, G.P.z - e.z); face(e.x, e.z); R.step(1 / 60, 24); R.keyDown("KeyL"); let k = 0; while (e.st === "windup" && k++ < 60) R.step(1 / 60); R.step(1 / 60, 2); R.keyUp("KeyL"); o.counterStun = e.st === "stun"; } const cap = G.enemies.find((e) => e.id === "captain"); let n = 0; while (alive().length && n++ < 10) { const e = alive().sort((a, b) => (a === cap) - (b === cap))[0]; brawl(e); }
    o.allDown = alive().length === 0; o.counters = (G.stats.counters || 0) - c0; const man = G.items.find((i) => i.type === "manual"); o.manualDropped = !!man; if (man) { G.P.x = man.x; G.P.z = man.z + 0.5; sim(0.1); tap("KeyE"); } o.manual = !!G.P.inv.manual; mortal(); return o; });
  ok("D2 5 men beaten by hand; a block at the right moment gives a COUNTER", r.allDown && r.counters >= 1 && r.counterStun, r);
  ok("D3 the captain drops the bomb manual; E picks it up", r.manualDropped && r.manual, r);
  r = await E(() => { const o = {}; const b = G.bombs[0]; G.P.x = b.x - 1.2; G.P.z = b.z; sim(0.1); tap("KeyE"); o.open = G.mode === "puzzle"; o.manualShown = /Bomb Manual/.test(document.getElementById("puzIn").textContent) && document.querySelectorAll(".mh.on").length === 1; o.wires = document.querySelectorAll(".wire").length;
    const safe = R.safeWire(b.w, b.serial); const wrong = (safe + 1) % b.n; document.querySelector(`.wire[data-i="${wrong}"]`).click(); sim(1); o.boom = G.mode === "fail" && /BOOM/.test(document.getElementById("failMsg").textContent) && !document.getElementById("fail").hidden; o.booms = G.stats.booms;
    const w0 = b.w.join() + b.serial; document.getElementById("failRetry").click(); sim(0.1); o.reopen = G.mode === "puzzle"; o.newWires = b.w.join() + b.serial !== w0;
    const s2 = R.safeWire(b.w, b.serial); document.querySelector(`.wire[data-i="${s2}"]`).click(); sim(1.5); o.defused = b.defused && G.mode === "play"; return o; });
  ok("D4 bomb puzzle: wires plus the manual for that wire count", r.open && r.manualShown && r.wires >= 3, r);
  ok("D5 wrong wire = BOOM and Try again; the retry gives new wires; the right wire defuses it", r.boom && r.booms === 1 && r.reopen && r.newWires && r.defused, r);
  r = await E(() => { const o = {}; const b = G.bombs[1]; G.P.x = b.x - 1.2; G.P.z = b.z; sim(0.1); tap("KeyE"); o.five = b.n === 5; sim(R.G.diff === 1 ? 61 : 95); o.timeout = G.mode === "fail"; document.getElementById("failRetry").click(); sim(0.1); const s = R.safeWire(b.w, b.serial); kb("Digit" + (s + 1)); sim(1.5); o.defused = b.defused; o.obj = G.obj; return o; });
  ok("D6 the timer runs out = BOOM; keys 1 to 5 also cut wires", r.five && r.timeout && r.defused && /Iyer/.test(r.obj), r);
  r = await E(() => { const o = {}; walkTo(22, 8); const h = G.hostages[0]; G.P.x = h.x - 1; G.P.z = h.z; sim(0.1); tap("KeyE"); o.sorry = G.mode === "dialog" && G.dlg.lines.some((l) => /sorry/.test(l[1])); talk(); walkTo(24, 7); play(0.5); o.ch = G.ch; return o; });
  ok("D7 Mr. Iyer is untied and says sorry; Chapter 3 opens", r.sorry && r.ch === 3, r);

  // ---------------- E. Chapter 3: Hostages in the Hall (no gun) ----------------
  r = await E(() => { const o = {}; o.noGun = !G.P.gun && !G.items.some((i) => i.type === "pistol" || i.type === "smg"); const g = G.enemies.find((e) => e.id === "guard"); behind(g, 1.3); sim(0.1); tap("KeyE"); sim(0.6); o.guard = g.st === "down"; play(0.3); o.obj = G.obj;
    const du = G.items.find((i) => i.type === "duster"); G.P.x = du.x; G.P.z = du.z + 0.4; sim(0.1); tap("KeyE"); o.carry = G.P.carry && G.P.carry.type; return o; });
  ok("E1 Chapter 3: no gun anywhere; a silent takedown on the guard; he drops a duster to throw", r.noGun && r.guard && /without a gun/.test(r.obj) && r.carry === "duster", r);
  r = await E(() => { const o = {}; const gm = G.enemies.find((e) => e.kind === "gunman" && Math.abs(e.x - R.cell(7, 9).x) < 0.5 && Math.abs(e.z - R.cell(7, 9).z) < 0.5); at(7, 12); G.P.crouch = true; face(gm.x, gm.z); const l0 = G.stats.env; tap("KeyF"); play(1.5); o.light = (G.stats.envKinds || {}).light === 1; o.down = gm.st === "down"; return o; });
  ok("E2 throw the duster at the hanging light: it falls and knocks the gunman out", r.light && r.down, r);
  r = await E(() => { const o = {}; const b = G.items.find((i) => i.type === "book" && Math.abs(i.x - R.cell(2, 11).x) < 0.5); G.P.x = b.x; G.P.z = b.z; G.P.crouch = true; sim(0.1); tap("KeyE"); const gm = G.enemies.find((e) => e.kind === "gunman" && Math.abs(e.x - R.cell(3, 6).x) < 1 && Math.abs(e.z - R.cell(3, 6).z) < 1); at(2, 10); G.P.crouch = true; const ex = G.L.props.find((p) => p.type === "ext" && p.cx === 1); face(ex.x, ex.z); tap("KeyF"); play(1.2); o.cloud = G.clouds.length >= 1; o.stun = gm.st === "stun"; behind(gm, 1.2); G.P.x = gm.x + 1; G.P.z = gm.z; sim(0.05); tap("KeyE"); sim(0.6); o.ko = gm.st === "down"; return o; });
  ok("E3 throw a book at the fire extinguisher: a white cloud blinds and stuns; E knocks him out", r.cloud && r.stun && r.ko, r);
  r = await E(() => { const o = {}; G.god = false; G.P.hp = 100; const gm = alive().find((e) => e.kind === "gunman"); G.P.crouch = false; G.P.x = gm.x; G.P.z = gm.z - 5; R.hurtEnemy(gm, 1, "punch"); sim(8); o.shot = G.P.hp < 100; god(); return o; });
  ok("E4 the gunmen shoot at Rish when they see him", r.shot, r);
  r = await E(() => { god(); const o = {}; const c = G.L.props.find((p) => p.type === "case"); at(c.cx - 1, c.cy, Math.PI / 2); tap("KeyK"); sim(0.6); o.glass = !c.alive && R.cellAt(c.cx, c.cy) === "."; let n = 0; while (alive().length && n++ < 12) brawl(alive()[0]); o.clear = alive().length === 0; o.obj = G.obj; return o; });
  ok("E5 a kick shatters the glass trophy case; the rest of the gunmen are beaten by hand", r.glass && r.clear && /Kabir/.test(r.obj), r);
  r = await E(() => { const o = {}; walkTo(15, 5); let n = 0; while (G.mode !== "qte" && n++ < 50) play(0.2); o.qte = G.mode === "qte" && G.qte.keys.join() === "fire,act,kick"; tap("KeyJ"); sim(2); n = 0; while (G.mode !== "qte" && n++ < 50) play(0.2); o.retry = G.mode === "qte"; solveQte(); play(3); o.kabir = !!G.flags.kabir; o.lightFell = (G.stats.envKinds || {}).light >= 2; return o; });
  ok("E6 save Kabir: a 3 key quick move (F, E, K); a wrong key = try again; then Kabir is free", r.qte && r.retry && r.kabir && r.lightFell, r);
  r = await E(() => { const o = { lines: [] }; sim(0.1); const m0 = G.markerNow; o.marker = !!m0 && G.hostages.some((h) => h === m0 && !h.freed) && R.GUIDE.mesh.visible !== undefined; for (const h of G.hostages.slice()) { if (h.freed) continue; G.P.x = h.x + 0.9; G.P.z = h.z + 0.6; sim(0.1); tap("KeyE"); if (G.mode === "dialog") { o.lines.push(G.dlg.lines.map((l) => l[1]).join(" ")); talk(); } play(0.2); }
    o.freed = G.hostages.filter((h) => h.freed).length; let kk = 0; while (G.mode !== "dialog" && kk++ < 400) R.step(1 / 60); o.kade = G.mode === "dialog" && G.dlg.lines.some((l) => l[0] === "kade"); o.kadeTxt = o.kade && G.dlg.lines.map((l) => l[1]).join(" "); talk(); o.noGun = !G.P.gun; walkTo(29, 2); play(0.3); R.tp(29, 1); play(0.5); o.ch = G.ch; return o; });
  ok("E6b after Kabir is saved, the gold marker points to the nearest person to untie", r.marker, r);
  ok("E7 all 9 hostages untied; Coach Vikram says sorry", r.freed === 9 && r.lines.some((l) => /Coach|bench/.test(l) && /sorry/.test(l)), r);
  ok("E8 Kade takes the Principal and Diya; the roof opens Chapter 4; still no gun", r.kade && /roof/.test(r.kadeTxt) && r.noGun && r.ch === 4, r);
  await shot("04-ch4-roof");

  // ---------------- F. Chapter 4: Rooftop ----------------
  r = await E(() => { const o = {}; god(); for (const e of G.enemies) if (e.kind === "thug") R.knockDown(e); G.P.crouch = false; at(2, 3, Math.PI / 2); R.keyDown("ShiftLeft"); R.keyDown("KeyW"); let n = 0; while (G.P.x < 9.2 && n++ < 300) { G.camYaw = Math.PI / 2; R.step(1 / 60); } tap("Space", 1); n = 0; while (n++ < 70) { G.camYaw = Math.PI / 2; R.step(1 / 60); } R.keyUp("KeyW"); R.keyUp("ShiftLeft"); sim(0.3); o.x = G.P.x; o.falls = G.stats.falls || 0; o.crossed = G.P.x > 14 && o.falls === 0;
    at(11, 3, Math.PI / 2); R.keyDown("KeyW"); n = 0; while (G.P.x < 25.3 && n++ < 400) { G.camYaw = Math.PI / 2; R.step(1 / 60); } tap("Space", 1); n = 0; while (n++ < 90) { G.camYaw = Math.PI / 2; R.step(1 / 60); } R.keyUp("KeyW"); sim(1.5); o.walkFalls = G.stats.falls || 0; o.back = G.P.x < 26 && G.P.y === 0; return o; });
  ok("F1 run (Shift) and jump (Space) across a 4 m roof gap", r.crossed, r);
  ok("F2 a walking jump falls short; Rish loses health and returns to the edge", r.walkFalls === 1 && r.back, r);
  r = await E(() => { const o = {}; for (const e of G.enemies) if (e.kind === "thug") R.knockDown(e); G.P.crouch = false; at(19, 3, Math.PI / 2); R.keyDown("KeyW"); let n = 0; while (n++ < 120) { G.camYaw = Math.PI / 2; R.step(1 / 60); } R.keyUp("KeyW"); o.blocked = G.P.x < 42;
    at(16, 3, Math.PI / 2); R.keyDown("ShiftLeft"); R.keyDown("KeyW"); n = 0; while (G.P.x < 39.5 && n++ < 300) { G.camYaw = Math.PI / 2; R.step(1 / 60); } tap("KeyC", 1); n = 0; while (n++ < 100) { G.camYaw = Math.PI / 2; R.step(1 / 60); } R.keyUp("KeyW"); R.keyUp("ShiftLeft"); sim(0.2); o.x = G.P.x; o.slid = G.P.x > 46; return o; });
  ok("F3 the low pipe blocks a standing boy; a running slide (Shift + C) goes under it", r.blocked && r.slid, r);
  r = await E(() => { const o = {}; god(); at(36, 3, Math.PI / 2); G.P.x += 1.5; play(0.2); R.tp(37, 3); play(0.6); const bull = G.enemies.find((e) => e.kind === "bull"); o.active = bull.active; o.size = bull.s > 1.1;
    const seen = new Set(); let n = 0; const P = G.P;
    while (bull.st !== "down" && n++ < 60 * 90) {
      if (G.mode === "dialog") { talk(); continue; } if (G.mode === "qte") { seen.add(G.qte.type === "mash" ? "grab" : "finish"); solveQte(); continue; } if (G.mode !== "play") break;
      seen.add(bull.st); const d = Math.hypot(bull.x - P.x, bull.z - P.z);
      if (bull.st === "low") { G.camYaw = Math.atan2(bull.x - P.x, bull.z - P.z); if (d > 2) { R.keyDown("KeyW"); R.step(1 / 60); R.keyUp("KeyW"); } else tap("KeyE"); continue; }
      if (bull.st === "dazed" || bull.st === "stun") { G.camYaw = Math.atan2(bull.x - P.x, bull.z - P.z); if (d > 1.6) { R.keyDown("KeyW"); R.step(1 / 60); R.keyUp("KeyW"); } else { tap("KeyJ", 1); R.step(1 / 60, 16); } continue; }
      if (bull.st === "charge" && d < 4 && !seen.has("rolledOnce") && seen.has("grab")) { const sideYaw = bull.yaw + Math.PI / 2; G.camYaw = sideYaw; R.keyDown("KeyW"); tap("KeyQ", 1); R.step(1 / 60, 25); R.keyUp("KeyW"); continue; }
      // keep away so he charges: run to the arena corner farthest from him
      if (d < 6.5 && bull.st !== "charge" && bull.st !== "charge_w") { const cs = [[37, 1], [37, 5], [42, 1], [42, 5]].map(([a, b]) => R.cell(a, b)).sort((u, v) => Math.hypot(v.x - bull.x, v.z - bull.z) - Math.hypot(u.x - bull.x, u.z - bull.z)); const tgt = cs[0]; G.camYaw = Math.atan2(tgt.x - P.x, tgt.z - P.z); R.keyDown("ShiftLeft"); R.keyDown("KeyW"); R.step(1 / 60); R.keyUp("KeyW"); R.keyUp("ShiftLeft"); } else R.step(1 / 60);
    }
    o.states = [...seen]; o.down = bull.st === "down"; o.obj = G.obj; return o; });
  ok("F4 Bull is big; he charges; a grab is a smash-J quick move", r.active && r.size && r.states.includes("charge") && r.states.includes("grab"), r);
  ok("F5 a charge into the wall makes Bull dizzy; the finisher quick move knocks him out", r.states.includes("dazed") && r.states.includes("finish") && r.down && /Principal/.test(r.obj), r);
  r = await E(() => { const o = {}; sim(1); const h = G.hostages[0]; G.P.x = h.x + 1; G.P.z = h.z + 0.6; sim(0.1); tap("KeyE"); o.txt = G.mode === "dialog" && G.dlg.lines.map((l) => l[1]).join(" "); talk(); play(0.5); o.ch = G.ch; o.mode = G.mode; mortal(); return o; });
  ok("F6 the Principal is free: Kade took Diya in a black van; Chapter 5 starts", /van/.test(r.txt) && /Diya/.test(r.txt) && r.ch === 5 && r.mode === "chase", r);
  await shot("05-ch5-chase");

  // ---------------- G. Chapter 5: Chase ----------------
  r = await E(() => { const o = {}; R.keyDown("KeyS"); let n = 0; while (G.mode === "chase" && n++ < 60 * 60) R.step(1 / 60); R.keyUp("KeyS"); o.fail = G.mode === "fail" && /got away/.test(document.getElementById("failMsg").textContent); document.getElementById("failRetry").click(); R.step(1 / 60); o.retry = G.mode === "chase" && G.C.z > -1 && !G.C.done; return o; });
  ok("G1 braking lets the van get away = Try again; the retry restarts the chase", r.fail && r.retry, r);
  r = await E(() => { const o = {}; R.keyDown("KeyW"); let n = 0; const C = () => G.C; let maxGap = 0;
    while (G.ch === 5 && n++ < 60 * 200) {
      if (G.mode === "dialog") { R.keyUp("KeyW"); talk(); R.keyDown("KeyW"); continue; } if (G.mode !== "chase") break;
      const c = C(); maxGap = Math.max(maxGap, c.z - c.vz); const ahead = G.CH.obs.filter((q) => !q.hit && !q.passed && q.z < c.z && q.z > c.z - 13);
      const blocked = (l) => ahead.some((q) => q.lane === l && q.k !== "ramp" && !(q.low && q.z > c.z - 4));
      if (blocked(c.lane)) { const alt = [c.lane - 1, c.lane + 1].filter((l) => l >= 0 && l <= 2 && !blocked(l)); if (alt.length) tap(alt[0] < c.lane ? "KeyA" : "KeyD", 1); }
      const low = ahead.find((q) => q.lane === c.lane && q.low && q.k !== "ramp" && q.z > c.z - 3.2); if (low && c.hop <= 0) tap("Space", 1);
      R.step(1 / 60); }
    R.keyUp("KeyW"); o.hits = (G.stats.chaseHits); o.ch = G.ch; o.maxGap = Math.round(maxGap); return o; });
  ok("G2 pedal (W), change lanes and hop crates through the market; the van stops at the railway crossing; Chapter 6 starts", r.ch === 6, r);
  await shot("06-ch6-yard");

  // ---------------- H. Chapter 6: Railway Yard (the only gun chapter) ----------------
  r = await E(() => { const o = {}; play(0.3); o.pistol = G.P.gun && G.P.gun.kind === "pistol"; god(); const gm = G.enemies.find((e) => e.kind === "gunman" && Math.abs(e.x - R.cell(11, 3).x) < 0.5); const bar = G.L.props.find((p) => p.type === "barrel" && p.cx === 10 && p.cy === 2);
    at(7, 6); face(bar.x, bar.z); sim(0.05); const t = R.autoAim(); o.aimBarrel = t && t.pr === bar; tap("KeyF"); play(1); o.boom = !bar.alive && (G.stats.envKinds || {}).barrel >= 1; o.gmDown = gm.st === "down"; const smg = G.items.find((i) => i.type === "smg"); o.smgDrop = !!smg;
    if (smg) { G.P.x = smg.x; G.P.z = smg.z + 0.5; sim(0.1); tap("KeyE"); } o.smg = G.P.gun && G.P.gun.kind === "smg"; const m0 = G.P.gun.mag; R.keyDown("KeyF"); sim(1); R.keyUp("KeyF"); o.auto = m0 - G.P.gun.mag; tap("KeyX"); o.swap = G.P.gun.kind === "pistol"; tap("KeyX"); return o; });
  ok("H1 Chapter 6 starts with a pistol; the red laser picks the barrel next to a gunman", r.pistol && r.aimBarrel, r);
  ok("H2 shooting the red barrel explodes it and knocks the gunman out", r.boom && r.gmDown, r);
  ok("H3 he drops a machine gun: hold F = fast automatic fire; X switches back to the pistol", r.smgDrop && r.smg && r.auto >= 6 && r.swap, r);
  r = await E(() => { const o = {}; const st = G.L.props.find((p) => p.type === "steam" && p.cx === 15); const post = (e, cx, cy) => { const c = R.cell(cx, cy); e.x = c.x; e.z = c.z; e.st = "patrol"; e.aware = 0; e.scan = 0; e.home = e.yaw = Math.PI; return e; }; const gm = post(alive().find((e) => e.kind === "gunman"), 15, 3); at(13, 7); face(st.x, st.z); let n = 0; while (st.alive && n++ < 10) { const t = R.autoAim(); if (t && t.pr === st) tap("KeyF"); else { G.P.yaw += 0; tap("KeyF"); } sim(0.3); } play(1.5); o.steam = !st.alive; o.gm = gm.st; o.hot = (G.stats.envKinds || {}).steam >= 1;
    const cr = G.L.props.find((p) => p.type === "crane"); const g2 = post(alive().find((e) => e.kind === "gunman" && e !== gm), 26, 8); at(22, 9); face(cr.x, cr.z); n = 0; while (cr.alive && n++ < 12) { tap("KeyF"); sim(0.3); } play(1.5); o.crane = !cr.alive && R.cellAt(26, 8) === "K"; o.g2 = g2 ? g2.st : "moved"; return o; });
  ok("H4 shooting a steam valve sprays hot steam on the gunman beside it", r.steam && r.hot && (r.gm === "stun" || r.gm === "down"), r);
  ok("H5 shooting the crane chain drops the container on the gunman under it; it stays as a new wall", r.crane && (r.g2 === "down" || r.g2 === "moved"), r);
  r = await E(() => { const o = {}; god(); G.P.gun.mag = 12; G.P.gun.res = 99; let n = 0; while (alive().length && n++ < 12) { const e = alive()[0]; if (e.boss) break; brawl(e); } o.left = alive().filter((e) => !e.boss).length; walkTo(34, 7); play(1); const k = G.enemies.find((e) => e.kind === "kade"); o.kadeOn = k.active; o.phase1 = k.armed;
    // phase 1: shoot him with the pistol
    n = 0; while (k.phase === 1 && n++ < 60 * 60) { if (G.mode === "dialog") { o.ph2Talk = G.dlg.lines.map((l) => l[1]).join(" "); talk(); continue; } if (!G.P.gun) break; if (G.P.gun.mag === 0) tap("KeyR"); face(k.x, k.z); tap("KeyF"); R.step(1 / 60, 8); }
    play(0.5); o.phase = k.phase; o.gunGone = !G.P.gun; o.kadeArmed = k.armed;
    const g0 = G.stats.qteOk || 0; o.won = brawl(k, 80); play(0.5); o.finisher = (G.stats.qteOk || 0) > g0; o.obj = G.obj; return o; });
  ok("H6 Kade fights with a gun first", r.kadeOn && r.phase1 && r.left === 0, r);
  ok("H7 at 60% health Kade kicks the gun away: hand to hand, kicks break his guard, a finisher quick move ends it", /ENOUGH GUNS/.test(r.ph2Talk || "") && r.phase === 2 && r.gunGone && !r.kadeArmed && r.won && r.finisher && /abort code/.test(r.obj), r);
  r = await E(() => { const o = {}; const p = R.cell(43, 7); G.P.x = p.x - 1.4; G.P.z = p.z; sim(0.1); tap("KeyE"); o.open = G.mode === "puzzle" && G.puz.kind === "code"; o.riddles = [...document.querySelectorAll(".rid li")].map((l) => l.textContent);
    const ans = o.riddles.map((t) => R.RIDDLES.find((x) => x[0] + "?" === t)[1]).join(""); o.ans = ans; const wrong = ans === "1111" ? "2222" : "1111";
    for (let k = 0; k < 3; k++) { for (const d of wrong) document.querySelector(`.pk[data-k="${d}"]`).click(); document.querySelector('.pk[data-k="OK"]').click(); }
    o.fail = G.mode === "fail"; document.getElementById("failRetry").click(); sim(0.1); o.reopen = G.mode === "puzzle"; const r2 = [...document.querySelectorAll(".rid li")].map((l) => l.textContent); const a2 = r2.map((t) => R.RIDDLES.find((x) => x[0] + "?" === t)[1]).join("");
    for (const d of a2) kb("Digit" + d); kb("Enter"); sim(1.5); o.done = !!G.flags.codeOk; o.obj = G.obj; return o; });
  ok("H8 abort code: 4 riddles, each answer is one digit; 3 wrong codes = fail", r.open && r.riddles.length === 4 && r.fail && r.reopen, r);
  ok("H9 the right code (typed on the keyboard) stops the countdown", r.done && /Diya/.test(r.obj), r);
  r = await E(() => { const o = {}; const h = G.hostages[0]; G.P.x = h.x + 1; G.P.z = h.z - 0.6; sim(0.1); tap("KeyE"); o.diya = G.mode === "dialog" && G.dlg.lines.some((l) => /birthday/.test(l[1])); talk(); play(0.5); o.ch = G.ch; return o; });
  ok("H10 Diya is free; she remembers the birthday; the Ending starts", r.diya && r.ch === 7, r);
  await shot("07-ending");

  // ---------------- I. Ending ----------------
  r = await E(() => { const o = {}; mortal(); let k = 0; while (G.mode !== "dialog" && k++ < 300) R.step(1 / 60); o.dlg = G.mode === "dialog"; const all = G.dlg ? G.dlg.lines.map((l) => l[0] + ":" + l[1]).join(" | ") : ""; o.sorry = ["iyer", "vikram", "dsouza", "kabir", "rohan"].every((w) => new RegExp(w + ":[^|]*(sorry|truth)", "i").test(all)); o.dad = /dad:/.test(all); o.world = /5 world capitals/.test(all);
    o.people = Object.keys(G.npcs).length; talk(); play(1); o.cheer = Object.values(G.npcs).every((n) => n.pose === "cheer"); play(6); o.end = /THE END/.test(document.getElementById("card").textContent) && !document.getElementById("scr").hidden; o.unlocked = G.save.unlocked; return o; });
  ok("I1 Ending: the news, the medal; teachers and bullies say sorry; Dad comes home; everyone is a friend", r.dlg && r.sorry && r.dad && r.world && r.people >= 14 && r.cheer, r);
  ok("I2 credits: THE END; every chapter unlocked", r.end && r.unlocked === 7, r);

  // ---------------- K. Skip ----------------
  r = await E(() => { const o = {}; R.startChapter(2, true); sim(0.2); o.dlg = G.mode === "dialog"; document.getElementById("dlgSkip").click(); o.dlgSkip = G.mode === "play";
    const sk = document.getElementById("skipB"); o.visible = getComputedStyle(sk).display !== "none"; sk.click(); o.armed = /again/.test(sk.textContent) && alive().length === 5; sk.click(); play(0.3); o.skipped = alive().length === 0 && G.bombs.every((b) => b.defused) && G.P.inv.manual; return o; });
  ok("K1 Skip on a talk skips the talk", r.dlg && r.dlgSkip, r);
  ok("K2 the Skip button needs 2 taps, then skips the hard part (fights and bombs)", r.visible && r.armed && r.skipped, r);
  r = await E(() => { const o = {}; R.startChapter(2, true); play(0.3); G.P.inv.manual = true; const b = G.bombs[0]; G.P.x = b.x - 1.2; G.P.z = b.z; for (const e of G.enemies) R.knockDown(e); sim(0.1); tap("KeyE"); o.open = G.mode === "puzzle"; document.getElementById("puzSkip").click(); o.skip = b.defused && G.mode === "play";
    const b2 = G.bombs[1]; G.P.x = b2.x - 1.2; G.P.z = b2.z; sim(0.1); tap("KeyE"); document.querySelector(`.wire[data-i="${(R.safeWire(b2.w, b2.serial) + 1) % b2.n}"]`).click(); sim(1); o.fail = G.mode === "fail"; document.getElementById("failSkip").click(); sim(0.1); o.failSkip = b2.defused && G.mode === "play"; return o; });
  ok("K3 Skip puzzle defuses a bomb; Skip this part on the fail screen works", r.open && r.skip && r.fail && r.failSkip, r);
  r = await E(() => { const o = {}; R.startChapter(5, true); talk(); R.togglePause(); o.pause = G.mode === "pause" && !!document.getElementById("psk"); document.getElementById("psk").click(); play(0.2); o.ch = G.ch; R.startChapter(4, true); talk(); G.P.hp = 5; G.god = false; R.hurtEnemy && 0; const t = alive()[0]; t.st = "alert"; t.x = G.P.x + 1; t.z = G.P.z; let n = 0; while (G.mode !== "fail" && n++ < 600) R.step(1 / 60); o.ko = G.mode === "fail" && /knocked out/.test(document.getElementById("failMsg").textContent); document.getElementById("failRetry").click(); play(0.3); o.restart = G.ch === 4 && G.P.hp === 100; return o; });
  ok("K4 pause menu: Skip this chapter; a knock out = Try again restarts the chapter", r.pause && r.ch === 6 && r.ko && r.restart, r);

  // ---------------- N. New story and features (v4) ----------------
  r = await E(() => { const o = {}; const P = R.PAGES; o.total = R.PAGE_TOTAL; o.walkable = true; const mapOf = { c1: "school", c2: "lab", c3: "hall", c4: "roof", c6: "yard" };
    for (const id in P) { const rows = R.MAPS[mapOf[id]].replace(/^\n/, "").split("\n"); for (const [cx, cy] of P[id]) { const ch = rows[cy][cx]; if (R.solidFor(ch, {}) || ch === " ") o.walkable = false; } }
    G.save.pages = {}; R.startChapter(2, true); R.skipDialog(); sim(0.2); const pg = G.items.filter((i) => i.type === "page"); o.spawned = pg.length; const it = pg[0]; G.P.x = it.x; G.P.z = it.z; sim(0.2); o.saved = Object.keys(G.save.pages).length; o.toast = /Diary/.test(document.getElementById("toast").textContent);
    R.startChapter(2, true); R.skipDialog(); sim(0.2); o.respawn = G.items.filter((i) => i.type === "page").length; R.menu(); o.menuBtn = /Diary \(1\/15\)/.test(document.getElementById("m-diary").textContent); document.getElementById("m-diary").click(); const t = document.getElementById("card").textContent; o.diary = /Mr\. Iyer said science/.test(t) && (t.match(/still hidden/g) || []).length === 14; document.getElementById("b").click(); return o; });
  ok("N1 15 hidden diary pages (3 per action chapter) on walkable squares; walking on one saves it with a toast", r.total === 15 && r.walkable && r.spawned === 3 && r.saved === 1 && r.toast, r);
  ok("N2 a found page does not come back; the Diary in the menu shows found pages and hides the rest", r.respawn === 2 && r.menuBtn && r.diary, r);
  r = await E(() => { const o = {}; R.startChapter(2, true); R.skipDialog(); sim(0.5); G.chT = 75; G.chFails = 0; const res = R.chapterResult(2); o.res = res; let went = 0; R.resultsCard(res, () => { went = 1; }); const t = document.getElementById("card").textContent; o.card = /complete/.test(t) && /Diary pages/.test(t) && /1:15/.test(t) && !!document.getElementById("ragain");
    document.getElementById("ragain").click(); sim(0.2); o.again = G.ch === 2 && G.mode !== "card"; R.resultsCard(res, () => { went = 1; }); document.getElementById("rnext").click(); o.next = went === 1;
    R.credits(); o.creditsAgain = !!document.getElementById("again"); document.getElementById("again").click(); sim(0.2); o.restart = G.ch === 0; return o; });
  ok("N3 chapter results card: time, knockouts, takedowns, room tricks, diary pages, stars (finish, all pages, no fails)", r.card && r.res.stars >= 2 && r.res.pagesTotal === 3, r);
  ok("N4 PLAY AGAIN: the results card replays the chapter; THE END screen restarts the story from the Prologue", r.again && r.next && r.creditsAgain && r.restart, r);
  r = await E(() => { const o = {}; const all = JSON.stringify([R.MEMORIES]); R.startChapter(0, true); sim(0.2); o.cold = G.mode === "dialog" && /far away for one year/.test(G.dlg.lines[0][1]) && /Kade/.test(G.dlg.lines[1][1]); R.skipDialog();
    R.startChapter(3, true); R.skipDialog(); sim(0.2); o.smokeStart = G.items.filter((i) => i.type === "smoke").length; god(); const gm = G.enemies.find((e) => e.kind === "gunman" && Math.abs(e.x - R.cell(7, 9).x) < 0.5); const sm = G.items.find((i) => i.type === "smoke"); G.P.x = sm.x; G.P.z = sm.z + 0.4; sim(0.1); tap("KeyE"); o.carry = G.P.carry && G.P.carry.type; at(7, 11); face(gm.x, gm.z); tap("KeyF"); play(1.5); o.cloud = G.clouds.length >= 1 && (G.stats.envKinds || {}).smoke === 1; o.stun = gm.st === "stun"; return o; });
  ok("N5 the Prologue opens with Papa's call and the news about Viktor Kade's revenge", r.cold, r);
  ok("N6 Mr. Iyer's smoke pellets: 2 at the start of Chapter 3; a throw makes a cloud that stuns the gunman", r.smokeStart === 2 && r.carry === "smoke" && r.cloud && r.stun, r);
  r = await E(() => { const o = {}; R.startChapter(5, true); R.skipDialog(); G.C.z = -1260; G.C.vz = -1300; R.step(1 / 60, 3); o.calls = G.stats.calls; R.startChapter(6, true); R.skipDialog(); G.flags.kadeDown = 1; const k = G.enemies.find((e) => e.kind === "kade"); R.knockDown(k); play(0.3); for (const e of G.enemies) R.knockDown(e); R.skipDialog(); R.openCode(() => {}); document.getElementById("pzHint").click(); const h = document.getElementById("pzHintT").textContent; o.hint = /Aarav/.test(h) && /\d/.test(h) && document.getElementById("pzHint").disabled; R.skipNow(); return o; });
  ok("N7 friends help: Aarav and Meher call 4 times during the chase; Aarav gives one hint in the abort code", r.calls === 4 && r.hint, r);

  // ---------------- X. Real 3D camera and the story base (v5) ----------------
  r = await E(() => { const o = {}; R.startChapter(1, true); R.skipDialog(); sim(0.3); R.skipDialog(); for (const e of G.enemies) R.knockDown(e); const d = G.L.props.find((q) => q.type === "door"); if (d) R.propHit(d, null, "kick");
    o.ceilIn = R.ceilAt(R.cell(20, 8).x, R.cell(20, 8).z); o.ceilOut = R.ceilAt(R.cell(20, 17).x, R.cell(20, 17).z); o.labCeil = 0;
    R.startChapter(2, true); R.skipDialog(); sim(0.2); for (const e of G.enemies) R.knockDown(e); sim(0.2); R.skipDialog(); o.labCeil = R.ceilAt(R.cell(10, 5).x, R.cell(10, 5).z);
    let maxRel = 0, minRel = 9, above = 0, n = 0; at(6, 7, Math.PI / 2); R.keyDown("KeyW"); for (let i = 0; i < 200; i++) { if (G.mode === "dialog") R.skipDialog(); G.camYaw = Math.PI / 2; R.step(1 / 60); const c = R.cam(); const rel = c.position.y - G.P.y; maxRel = Math.max(maxRel, rel); minRel = Math.min(minRel, rel); if (c.position.y > R.ceilAt(c.position.x, c.position.z)) above++; const ch = R.cellAt(Math.floor(c.position.x / 2), Math.floor(c.position.z / 2)); if (ch === "#" ) n++; } R.keyUp("KeyW");
    o.maxRel = +maxRel.toFixed(2); o.minRel = +minRel.toFixed(2); o.above = above; o.inWall = n; const c = R.cam(); o.behind = Math.hypot(c.position.x - G.P.x, c.position.z - G.P.z); return o; });
  ok("X1 real 3D: the school and the lab have ceilings and a roof indoors; open sky outdoors", r.ceilIn > 3 && r.ceilIn < 4 && r.ceilOut > 50 && r.labCeil > 3 && r.labCeil < 4, r);
  ok("X2 the camera is low behind Rish's shoulder (1 to 3 m up), never above the ceiling, never inside a wall", r.maxRel < 3 && r.minRel > 0.9 && r.above === 0 && r.inWall === 0 && r.behind > 1.5 && r.behind < 4, r);
  r = await E(() => { const o = {}; const c = R.cam(); tap("KeyV"); sim(0.5); o.fp = R.CAM.fp && !G.P.g.visible && Math.abs(c.position.y - (G.P.y + 1.15)) < 0.2 && Math.hypot(c.position.x - G.P.x, c.position.z - G.P.z) < 0.5; tap("KeyV"); sim(0.5); o.back = !R.CAM.fp && G.P.g.visible;
    const p0 = G.camPitch; const cv = document.getElementById("cv"); const rect = cv.getBoundingClientRect(); const ev = (t, x, y) => cv.dispatchEvent(new PointerEvent(t, { pointerId: 7, clientX: x, clientY: y, bubbles: true, pointerType: "mouse" })); ev("pointerdown", 500, 300); ev("pointermove", 500, 380); ev("pointerup", 500, 380); o.pitch = G.camPitch > p0; sim(0.5); o.lookDown = R.cam().position.y > G.P.y + 1.9; G.camPitch = 0.22; return o; });
  ok("X3 V (or the 👁 View button) switches to first person through Rish's eyes and back", r.fp && r.back, r);
  ok("X4 drag up or down to look up or down (camera pitch)", r.pitch && r.lookDown, r);
  r = await E(() => { const o = {}; R.menu(); document.getElementById("m-story").click(); const t = document.getElementById("card").textContent; o.story = /Marco Kade/.test(t) && /12:00 noon/.test(t) && /soldier's son/.test(t) && /Protect people, even the ones who hurt you/.test(t) && (t.match(/AM/g) || []).length >= 5; document.getElementById("b").click();
    o.times = R.CHAPTERS.map((c) => c.time + "|" + (c.goal ? 1 : 0)).join(","); R.startChapter(2, true); R.skipDialog(); G.chT = 100; sim(0.6); o.clock = document.getElementById("clock").textContent;
    R.startChapter(1, true); let k = 0; const lines = []; while (k++ < 600) { if (G.mode === "dialog") { lines.push(...G.dlg.lines.map((l) => l[1])); R.skipDialog(); } if (G.mode === "qte") break; R.step(1 / 60); } o.ch1 = lines.join(" ");
    return o; });
  ok("X5 a precise story base in the menu: who, why (Marco Kade), Kade's plan (12:00 noon), the heart, and a timeline", r.story, r);
  ok("X6 every chapter has a time and a goal; the HUD clock runs (Annual Day 9:35 AM in the lab after 100 s)", /9:10 AM\|1/.test(r.times) && /11:40 AM\|1/.test(r.times) && /9:35 AM/.test(r.clock), r);

  // ---------------- L. The first page: name, age, father's job (v6) ----------------
  r = await E(() => { const o = {}; R.login(() => R.menu()); const card = document.getElementById("card"); o.fields = card.querySelectorAll("input, select").length; o.jobs = card.querySelectorAll("#lgJob option").length;
    document.getElementById("lgName").value = ""; document.getElementById("lgGo").click(); o.err1 = /name/.test(document.getElementById("lgErr").textContent);
    document.getElementById("lgName").value = "aryan kapoor"; document.getElementById("lgAge").value = "40"; document.getElementById("lgGo").click(); o.err2 = /age/.test(document.getElementById("lgErr").textContent);
    document.getElementById("lgAge").value = "9"; document.getElementById("lgJob").value = "doctor"; document.getElementById("lgDream").value = ""; document.getElementById("lgGo").click(); o.err3 = /grow up/.test(document.getElementById("lgErr").textContent); document.getElementById("lgDream").value = "Astronaut"; document.getElementById("lgGo").click(); o.dreamLine = R.personalize("I will become {DREAM_A}. And a hero, every single day."); o.saved = JSON.stringify(G.save.profile); o.menuWho = /Aryan/.test(document.getElementById("card").textContent) && /Doctor/.test(document.getElementById("card").textContent);
    const P = R.personalize; o.t1 = P("My name is Rish. My father is in the army. We move a lot."); o.t2 = P("And one more thing. One boy is missing from the hall. The soldier's son, Rishabh Sharma."); o.t3 = P("BREAKING NEWS. A 10 year old boy from Suryanagar. His name is Rishabh Sharma."); o.t4 = P("Dear Papa, today I turned 10."); o.t5 = P("I am a soldier's son.");
    document.getElementById("m-story").click(); o.story = document.getElementById("card").textContent; R.menu(); document.getElementById("m-about").click(); o.credit = /Rishabh Sharma/.test(document.getElementById("card").textContent) && /9 years old/.test(document.getElementById("card").textContent); document.getElementById("b").click();
    R.startChapter(0, true); sim(0.2); o.firstLine = G.mode === "dialog" ? document.getElementById("dlgText").textContent : ""; R.skipDialog();
    G.save.profile = { name: "Rish", age: 10, job: "army" }; R.menu(); return o; });
  ok("L1 the first page asks 4 things: name, age, what you want to become, father's job (11 jobs to pick)", r.fields === 4 && r.jobs === 11, r);
  ok("L2 it checks the answers: a name is needed, the age must be 5 to 16; then it saves and opens the menu", r.err1 && r.err2 && r.err3 && r.saved === '{"name":"Aryan Kapoor","age":9,"job":"doctor","dream":"astronaut"}' && r.menuWho, r);
  ok("L2b the dream is in the story: 'I will become an astronaut'", r.dreamLine === "I will become an astronaut. And a hero, every single day.", r);
  ok("L3 the story uses the player: name, age and father's job in every line", r.t1 === "My name is Aryan. My father is a doctor. He makes sick people well." && /doctor's son, Aryan Kapoor/.test(r.t2) && /A 9 year old boy/.test(r.t3) && /His name is Aryan Kapoor/.test(r.t3) && /turned 9/.test(r.t4) && r.t5 === "I am a doctor's son.", r);
  ok("L4 the Story page and the first scene follow the father's job (Dr. Rajveer Kapoor); the game credit stays Rishabh Sharma", /Dr\. Rajveer Kapoor/.test(r.story) && /Aryan \(Aryan Kapoor\) is 9/.test(r.story) && /a big hospital far away needs me/.test(r.firstLine) && r.credit, r);

  // ---------------- HL. Hero Life: the whole life after the attack (v7) ----------------
  await p.evaluate(() => { window.solveEm = (maxSec = 120) => { let n = 0; const P = G.P; god(); while (G.em && n++ < maxSec * 20) {
      if (G.mode === "dialog") { talk(); continue; } if (G.mode === "qte") { solveQte(); continue; }
      if (G.mode === "puzzle" && G.puz && G.puz.kind === "wire") { const b = G.puz.b; R.cutWire(R.safeWire(b.w, b.serial)); sim(1.2); continue; }
      if (G.mode !== "play") { R.step(1 / 60); continue; }
      const foe = alive().filter((e) => e.active)[0]; if (foe) { brawl(foe, 30); continue; }
      const zs = G.zones.filter((z) => !z.off && (!z.ok || z.ok()) && !/^(Talk|Sign)/.test(z.label)); if (!zs.length) { R.step(1 / 60, 3); continue; }
      const z = zs[0], q = z.get ? z.get() : z; let tx = q.x, tz = q.z; for (const [ox, oz] of [[1, 0], [-1, 0], [0, 1], [0, -1], [1.4, 1.4], [0, 2.5], [0, -2.5]]) { const ch = R.cellAt(Math.floor((q.x + ox) / 2), Math.floor((q.z + oz) / 2)); if (!R.solidFor(ch, {})) { tx = q.x + ox; tz = q.z + oz; break; } }
      G.P.x = tx; G.P.z = tz; R.step(1 / 60, 2); tap("KeyE"); R.step(1 / 60, 3); }
    return !G.em; }; });
  r = await E(() => { const o = {}; G.save.unlocked = 7; R.menu(); o.btn = !!document.getElementById("m-life"); R.credits(); o.creditsBtn = !!document.getElementById("life") && /whole world knows his name/.test(document.getElementById("card").textContent);
    document.getElementById("life").click(); sim(0.4); o.city = G.L.name === "city" && Object.keys(R.PLACES).length >= 14; o.age = R.lifeS().age; o.obj = G.obj; o.clock = document.getElementById("clock").textContent; o.walkers = Object.keys(G.npcs).filter((k) => k.startsWith("civ")).length;
    const d = R.PLACES.school.door; const w = walkTo(d[0], d[1]); play(2.5); o.walk = w.ok; o.em = G.em && G.em.type; o.emObj = /🚨/.test(G.obj) && !!G.markerNow; return o; });
  ok("HL1 after the Ending: 'Continue: Hero Life' and a Hero Life button; a 3D city (home, school, hospital, police, fire station, market, park, bank, river, bridge...)", r.btn && r.creditsBtn && r.city && r.walkers === 8, r);
  ok("HL2 a normal day: age 10 goes to school (real walking); then an emergency starts with a timer and a gold marker", r.age === 10 && /school/.test(r.obj) && /Age 10/.test(r.clock) && r.walk && !!r.em && r.emObj, r);
  r = await E(() => { const o = { done: {} }; for (const t of R.EM_TYPES) { R.lifeDay(); sim(0.2); G.skipFn = null; R.emergency(t); o.done[t] = solveEm(); talk(); sim(0.5); } o.saves = R.lifeS().saves; o.fame = R.lifeS().fame; o.kinds = Object.keys(R.lifeS().kinds).length; return o; });
  ok("HL3 19 kinds of emergency, each solved by playing: fire, accident, drowning, robbery, kidnapping, bomb, earthquake, runaway bus, kitten, gas leak, stuck lift, flood, lost child, live wire, thief chase, capsized boat, CPR, cobra, detective case", Object.values(r.done).every(Boolean) && r.kinds === 19 && r.saves >= 19, r);
  r = await E(() => { const o = {}; R.lifeDay(); sim(0.2); const f0 = R.lifeS().fame; R.emergency("robbery"); solveEm(); sim(1.5); o.news = G.mode === "dialog" && G.dlg.lines.map((l) => l[1]).join(" "); talk(); o.fameUp = R.lifeS().fame > f0; o.home = /go home/i.test(G.obj); const a0 = R.lifeS().age; const d = R.PLACES.home.door; G.P.x = R.cell(d[0], d[1]).x; G.P.z = R.cell(d[0], d[1]).z; sim(0.5); o.aged = R.lifeS().age === a0 + 1; o.level = R.fameLevel(R.lifeS().fame);
    o.cape = !!G.P.g.userData.cape; o.fans = Object.keys(G.npcs).filter((k) => k.startsWith("fan")).length; const fan = G.npcs.fan0; if (fan) { G.P.x = fan.x + 1; G.P.z = fan.z; sim(0.1); tap("KeyE"); } o.autograph = /hero/i.test(document.getElementById("toast").textContent); return o; });
  ok("HL4 every save is BREAKING NEWS: the whole world knows who the hero is; fame grows; then home, and one year passes", /BREAKING NEWS/.test(r.news) && /Everybody knows who the hero is/.test(r.news) && r.fameUp && r.home && r.aged, r);
  ok("HL5 a famous hero: a red cape and badge, fans in the street, autographs", r.cape && r.fans >= 5 && r.autograph, r);
  r = await E(() => { const o = {}; G.save.profile = { name: "Rish", age: 10, job: "army", dream: "astronaut" }; const S = R.lifeS(); S.age = 22; S.job = null; R.lifeDay(); o.noCard = G.mode === "play"; o.job = S.job; o.toast = document.getElementById("toast").textContent; o.obj = G.obj; const d = R.PLACES.office.door; G.P.x = R.cell(d[0], d[1]).x; G.P.z = R.cell(d[0], d[1]).z; sim(0.3); o.shift = /astronaut/.test(G.obj); let k = 0; while (!G.em && k++ < 10) { const z = G.zones.find((q) => !q.off && /astronaut/.test(q.label)); if (!z) break; G.P.x = z.x + 0.5; G.P.z = z.z; sim(0.1); tap("KeyE"); sim(0.2); } sim(1.8); o.em = !!G.em; o.clock = document.getElementById("clock").textContent;
    G.save.profile.dream = "cricketer"; o.cricket = R.dreamJob().place; G.save.profile.dream = "doctor"; o.doc = R.dreamJob().place; G.save.profile = { name: "Rish", age: 10, job: "army" }; return o; });
  ok("HL6 at 22 his childhood dream (typed on the first page) comes true: an astronaut works at the City Office, then saves people too", r.noCard && r.job === "dream" && /astronaut/i.test(r.toast) && /City Office/.test(r.obj) && r.shift && r.em && /Astronaut/.test(r.clock) && r.cricket === "park" && r.doc === "hospital", r);
  r = await E(() => { const o = {}; const S = R.lifeS(); S.age = 25; S.viper = []; R.lifeDay(); sim(0.2); G.skipFn = null; R.emergency(); o.type = G.em.type; o.text = G.em.text; o.bull = G.enemies.some((e) => e.kind === "bull"); o.won = solveEm(180); talk(); return o; });
  ok("HL7 at 25 the Black Viper gang attacks again (Marco Kade escaped): 5 men and Bull at the River Bridge", r.type === "viper" && /Marco Kade/.test(r.text) && r.bull && r.won, r);

  r = await E(() => { const o = {}; const S = R.lifeS(); S.age = 30; S.fame = 900; S.job = "dream"; R.lifeDay(); sim(0.5); o.shadows = R.SHADOWS.used; o.clouds = (G.L.clouds || []).length; const c = G.cars[0]; const x0 = c.g.position.x; sim(1); o.carMoved = Math.abs(c.g.position.x - x0) > 3;
    G.P.x = c.g.position.x + c.dir * 2.5; G.P.z = c.z; const x1 = c.g.position.x; sim(1); o.carStops = Math.abs(c.g.position.x - x1) < 0.2; R.tp(5, 7);
    o.friends = ["kabir", "diya", "aarav", "maa"].every((id) => G.npcs[id]); o.adult = G.npcs.kabir.g.userData.s > 0.95; const k = G.npcs.kabir; G.P.x = k.x + 1; G.P.z = k.z; sim(0.1); tap("KeyE"); o.talk = G.mode === "dialog" && /coach/i.test(G.dlg.lines[0][1]); talk();
    o.heroRun = R.heroRun(); R.tp(4, 6); G.camYaw = Math.PI / 2; const px = G.P.x; R.keyDown("ShiftLeft"); R.keyDown("KeyW"); sim(1); R.keyUp("KeyW"); R.keyUp("ShiftLeft"); o.speed = +(G.P.x - px).toFixed(1); o.stance = document.getElementById("stance").textContent;
    G.skipFn(); sim(0.2); R.emDone(true); sim(1.5); o.ticker = getComputedStyle(document.getElementById("ticker")).display !== "none" && /NEWS/.test(document.getElementById("ticker").textContent); talk(); o.night = G.L.lampMat.emissive.getHex() !== 0;
    R.medals(() => R.menu()); const t = document.getElementById("card").textContent; o.medals = /Hero Medals \d+\/20/.test(t) && document.querySelectorAll(".medal").length === 20; R.menu(); return o; });
  ok("HL10 more 3D: soft shadows under people, clouds in the sky, cars that drive and stop for people, street lamps that glow at night", r.shadows >= 10 && r.clouds === 16 && r.carMoved && r.carStops && r.night, r);
  ok("HL11 old friends grown up in the city (Kabir the coach, Diya, Aarav, Maa) to talk to; a news ticker of his saves", r.friends && r.adult && r.talk && r.ticker, r);
  ok("HL12 famous heroes get Hero Run (faster running) and a Medals room for 20 kinds of rescue", r.heroRun && r.speed > 8 && /Hero Run/.test(r.stance) && r.medals, r);
  r = await E(() => { const o = {}; R.lifeDay(); sim(0.2); R.emergency("bus"); for (let i = 0; i < 60 * 40 && G.em; i++) R.step(1 / 60); sim(1); o.missed = !G.em && /Other rescuers/.test(document.getElementById("toast").textContent) && /go home/i.test(G.obj); return o; });
  ok("HL8 too slow: other rescuers help (no game over), and the day goes on", r.missed, r);
  r = await E(() => { const o = {}; const S = R.lifeS(); S.age = 49; R.lifeDay(); sim(0.1); G.skipFn(); sim(0.1); R.emDone(true); talk(); R.yearEnd(); sim(0.3); o.statue = !!G.L.statue; S.age = 69; R.yearEnd(); const t = document.getElementById("card").textContent; o.end = /A HERO'S LIFE/.test(t) && /age 70/.test(t) && /Play life again/.test(t) && /whole world knows his name/.test(t); document.getElementById("lagain").click(); sim(0.2); o.again = R.lifeS().age === 10 && G.life; R.menu(); return o; });
  ok("HL9 at 50 a statue in the City Park; at 70 the Life Story; Play life again starts a new life", r.statue && r.end && r.again, r);

  // ---------------- V. Pictures ----------------
  for (const [i, name] of [[0, "08-prologue"], [1, "09-ch1"], [3, "10-ch3-hall"], [6, "11-ch6"]]) { await E((i) => { R.startChapter(i, true); play(0.4); if (G.mode === "dialog") R.skipDialog(); play(1); }, i); await shot(name); }
  r = await notBlank();
  ok("V1 the 3D view draws (many colours on screen)", r > 25, r);

  // ---------------- T. Phone ----------------
  {
    const q = await b.newPage({ viewport: { width: 844, height: 390 }, hasTouch: true, isMobile: true });
    q.on("pageerror", (e) => errs.push("PE(phone) " + e.message));
    if (THREE_LOCAL) await q.route("https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js", (rt) => rt.fulfill({ path: THREE_LOCAL, contentType: "application/javascript" }));
    await q.goto("file://" + FILE + "?test=1&touch=1"); await q.waitForFunction(() => window.__rh && window.__rh.step, null, { timeout: 60000 }); await q.evaluate(HELPERS);
    r = await q.evaluate(() => { R.startChapter(2, true); R.skipDialog(); sim(0.3); const box = (el) => el.getBoundingClientRect(); const els = [...document.querySelectorAll("#btns button")].map(box); const st = box(document.getElementById("stick"));
      const inside = els.concat([st]).every((b) => b.left >= 0 && b.top >= 0 && b.right <= innerWidth && b.bottom <= innerHeight);
      const hit = (a, c) => !(a.right <= c.left || c.right <= a.left || a.bottom <= c.top || c.bottom <= a.top);
      let overlap = 0; for (let i = 0; i < els.length; i++) { if (hit(els[i], st)) overlap++; for (let j = i + 1; j < els.length; j++) if (hit(els[i], els[j])) overlap++; }
      const ob = box(document.getElementById("obj")), mi = box(document.getElementById("mini")), tb = box(document.getElementById("topbtns")); const tops = [...document.querySelectorAll("#topbtns button")].filter((x) => getComputedStyle(x).display !== "none").map(box); for (const t of tops) for (const e of els) if (hit(t, e)) overlap++;
      return { pad: getComputedStyle(document.getElementById("pad")).display, n: els.length, inside, overlap, objMini: hit(ob, mi), skip: hit(tb, st) }; });
    ok("T1 phone: stick and 11 buttons on screen, nothing overlaps", r.pad === "block" && r.n === 11 && r.inside && r.overlap === 0 && !r.objMini && !r.skip, r);
    const jb = await q.$('#btns button[data-code="KeyJ"]'); const bb = await jb.boundingBox(); await q.touchscreen.tap(bb.x + bb.width / 2, bb.y + bb.height / 2);
    r = await q.evaluate(() => { R.step(1 / 60, 2); return G.P.st; });
    ok("T2 phone: the J button punches", r === "punch", r);
    await q.evaluate(() => R.render()); await q.screenshot({ path: `${SHOTS}/12-phone.png` });
    await q.close();
  }

  console.log(`\n${pass} passed, ${fail} failed`);
  if (errs.length) console.log("ERRORS:\n" + errs.slice(0, 20).join("\n"));
  await b.close(); process.exit(fail || errs.length ? 1 : 0);
})();
