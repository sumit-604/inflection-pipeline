// Rish Hero regression. Usage: NODE_PATH=$(npm root -g) node regress.cjs http://localhost:8766/test.html [shotDir]
const { chromium } = require("playwright");
const URL = process.argv[2] || "http://localhost:8766/test.html", SHOTS = process.argv[3] || ".";
let pass = 0, fail = 0; const errs = [];
const ok = (name, cond, info = "") => { if (cond) pass++; else fail++; console.log(`${cond ? "PASS" : "FAIL"} ${name}${cond ? "" : " :: " + JSON.stringify(info)}`); };
const HELPERS = () => { const R = window.__rh, G = R.G; window.R = R; window.G = G; window.S = R.S;
  window.sim = (s) => { for (let t = 0; t < s; t += 0.05) R.step(0.05); };
  window.begin = (i) => { R.startChapter(i); sim(0.5); R.dialogSkip(); sim(0.1); };
  window.godMode = () => { G.p.hp = G.p.maxHp = 5000; };
  window.clearEnemies = () => { for (let n = 0; n < 400; n++) { const e = G.ents.find((q) => q.k === "enemy" && !q.dead); if (!e) break; G.p.x = e.x - 40; G.p.y = e.y; if (!G.p.weapons.length) R.giveWeapon("pistol", true); if (G.p.wi < 0) G.p.wi = 0; G.p.weapons[G.p.wi].mag = 99; G.input.keys.add("fire"); sim(0.3); G.input.keys.delete("fire"); } };
  window.freeAll = () => { for (const h of G.ents.filter((q) => q.k === "host" && !q.freed)) { G.p.x = h.x - 20; G.p.y = h.y; R.takedownOrAct(); sim(1.2); for (let i = 0; i < 20 && G.mode === "dialog"; i++) R.dialogSkip(); } };
  window.toExit = () => { G.p.x = G.exit.x; G.p.y = G.exit.y; sim(0.2); sim(1.5); for (let i = 0; i < 20 && G.mode === "dialog"; i++) R.dialogSkip(); sim(0.1); return document.querySelector("#card h2")?.textContent || G.mode; }; };
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 700 } });
  p.on("pageerror", (e) => errs.push("PE " + e.message)); p.on("console", (m) => { if (m.type() === "error") errs.push("CE " + m.text()); });
  await p.goto(URL); await p.waitForFunction(() => window.__rh && window.__rh.step, null, { timeout: 60000 }); await p.evaluate(HELPERS); const E = (f, a) => p.evaluate(f, a); let r;
  // A. Menu and pages
  r = await E(() => ({ title: document.querySelector("#card h1")?.textContent, sub: document.querySelector(".sub")?.textContent, ver: document.querySelector("#ver").textContent, btns: document.querySelectorAll("#card .btn").length }));
  ok("A1 title, series line and version", r.title === "RISH HERO" && /Game 3/.test(r.sub) && /Just live it/.test(r.sub) && r.ver === "Rish Hero v1" && r.btns >= 6, r);
  await p.screenshot({ path: `${SHOTS}/01-menu.png` });
  r = await E(() => { R.chapters(); const n = document.querySelectorAll("[data-ch]").length, open = [...document.querySelectorAll("[data-ch]")].filter((x) => !x.disabled).length; document.querySelector("#c-back").click(); document.querySelector("#m-about").click(); const img = document.querySelector(".portrait-photo"), t = document.querySelector("#card").textContent; document.querySelector("#a-back").click(); document.querySelector("#m-how").click(); const h = document.querySelector("#card").textContent; document.querySelector("#h-back").click(); return { n, open, img: img && img.src.slice(0, 22), rish: /Rishabh Sharma/.test(t) && /9 years old/.test(t), made: /made up/.test(t), how: /punch/.test(h) && /grenade/.test(h) && /reload/i.test(h) }; });
  ok("A2 7 chapters, only the prologue open at the start", r.n === 7 && r.open === 1, r);
  ok("A3 About: photo, creator, the gang is made up", r.img === "data:image/jpeg;base64" && r.rish && r.made, r);
  ok("A4 How to play lists the moves", r.how, r);
  // B. Prologue
  r = await E(() => { begin(0); const talked = []; for (const n of G.ents.filter((q) => q.k === "npc")) { G.p.x = n.x - 30; G.p.y = n.y; R.takedownOrAct(); talked.push(G.mode); R.dialogSkip(); } const done = R.objectivesDone(); const end = toExit(); return { talk: G.ob.talk, talked, done, end, unlocked: S.unlocked }; });
  ok("B1 Prologue: talk to 3 classmates, go to the desk, Chapter 1 opens", r.talk === 3 && r.talked.every((m) => m === "dialog") && r.done && /Prologue/.test(r.end) && r.unlocked === 1, r);
  // C. Chapter 1 combat
  r = await E(() => { begin(1); const o = {}; o.noGun = G.p.weapons.length === 0; const rif = G.ents.find((e) => e.type === "rifle"); G.p.x = rif.x - 220; G.p.y = rif.y; G.p.hp = 100; sim(4); o.shotAt = 100 - G.p.hp; o.riflemanAlert = rif.alert;
    const gd = G.drops.find((d) => d.k === "gun"); G.p.x = gd.x + 30; G.p.y = gd.y; sim(0.1); o.gun = G.p.weapons.map((w) => w.id).join(","); o.equipped = G.p.wi === 0; godMode(); return o; });
  ok("C1 Chapter 1 starts with fists; a rifleman spots Rish and shoots", r.noGun && r.riflemanAlert && r.shotAt > 0, r);
  ok("C2 walking near a gun picks it up and equips it", r.gun === "pistol" && r.equipped, r);
  r = await E(() => { const o = {}; const W = G.p.weapons[0], m0 = W.mag; const th = G.ents.find((e) => e.type === "thug" && !e.dead); G.p.x = th.x - 80; G.p.y = th.y; G.p.face = 0; G.input.mouse.active = -99; G.input.keys.add("fire"); sim(0.2); G.input.keys.delete("fire"); o.fired = m0 - W.mag; o.aimOk = Math.abs(Math.atan2(th.y - G.p.y, th.x - G.p.x) - G.p.aim) < 0.3; W.mag = 0; W.res = 20; sim(1.2); o.reloaded = W.mag === 12 && W.res === 8;
    G.p.wi = -1; const th2 = G.ents.find((e) => e.type === "thug" && !e.dead); th2.stun = 0; th2.hp = th2.maxHp = 100; G.p.x = th2.x - 30; G.p.y = th2.y; G.p.aim = G.p.face = 0; G.p.combo = 0; G.p.comboT = 0; const h0 = th2.hp; for (let i = 0; i < 3; i++) { G.p.x = th2.x - 30; G.p.y = th2.y; G.p.aim = 0; R.melee(false); G.p.melee = 0; } o.combo = h0 - th2.hp; G.p.x = th2.x - 30; G.p.y = th2.y; o.stunned = th2.stun > 0 || th2.dead; if (!th2.dead) { R.takedownOrAct(); } o.takedown = th2.dead && S.stats.takedowns > 0; return o; });
  ok("C3 auto aim at the nearest enemy; shooting uses ammo; reload refills the magazine", r.fired >= 1 && r.aimOk && r.reloaded, r);
  ok("C4 punch combo ends with an uppercut that dazes; E does a takedown", r.combo >= 40 && r.stunned && r.takedown, r);
  r = await E(() => { const o = {}; G.p.hp = 100; G.p.maxHp = 100; G.input.keys.add("roll"); sim(0.05); G.input.keys.delete("roll"); const inRoll = G.p.roll > 0; R.hurtPlayer(30, G.p.x + 10, G.p.y); o.rollSafe = inRoll && G.p.hp === 100; sim(0.6); const e = G.ents.find((q) => q.k === "enemy" && !q.dead); const n0 = G.nades.length; G.p.x = e.x - 120; G.p.y = e.y; G.p.aim = 0; const nn = G.p.nades; R.throwNade(); o.nade = G.nades.length === n0 + 1 && G.p.nades === nn - 1; const h0 = e.hp; sim(2); o.boom = e.hp < h0 || e.dead; G.p.focus = 80; R.toggleFocus(); o.focus = G.p.focusOn; sim(1); o.drain = G.p.focus < 80; R.toggleFocus(); godMode(); return o; });
  ok("C5 a roll dodges damage; grenade throws and explodes; focus slows time and drains", r.rollSafe && r.nade && r.boom && r.focus && r.drain, r);
  r = await E(() => { clearEnemies(); freeAll(); const o = { ko: G.ob.ko, koN: G.ob.koN, free: G.ob.free, freeN: G.ob.freeN }; o.end = toExit(); o.kit = S.kit && S.kit.weapons.map((w) => w.id).join(","); o.unlocked = S.unlocked; o.stars = S.stars; return o; });
  ok("C6 Chapter 1 complete: all enemies stopped, all hostages free, the gun carries on", r.ko === r.koN && r.free === r.freeN && /Chapter 1/.test(r.end) && r.kit === "pistol" && r.unlocked === 2 && r.stars > 0, r);
  await p.screenshot({ path: `${SHOTS}/02-c1-done.png` });
  // D. Chapter 2 bombs
  r = await E(() => { begin(2); godMode(); const o = { timer: G.timer > 200, guns: G.p.weapons.map((w) => w.id).concat(G.drops.filter((d) => d.k === "gun").map((d) => d.id)).join(",") }; const bm = G.ents.find((q) => q.k === "bomb"); G.p.x = bm.x - 20; G.p.y = bm.y; R.takedownOrAct(); o.mini = G.mode === "mini"; G.mini.x = G.mini.z0 > 0.2 ? 0.02 : 0.98; const hp = G.p.hp; R.miniHit(); o.zap = G.p.hp < hp && G.mini.hits === 0; for (const b2 of G.ents.filter((q) => q.k === "bomb")) { if (!G.mini) { G.p.x = b2.x - 20; G.p.y = b2.y; R.takedownOrAct(); } for (let k = 0; k < 3; k++) { G.mini.x = G.mini.z0 + G.mini.zw / 2; R.miniHit(); } } o.defused = G.ob.defuse; clearEnemies(); o.end = toExit(); return o; });
  ok("D1 Chapter 2: an SMG waits on the map, a bomb timer runs, a wrong cut zaps", r.timer && /pistol,smg/.test(r.guns) && r.mini && r.zap, r);
  ok("D2 all 4 bombs defused, chapter complete", r.defused === 4 && /Chapter 2/.test(r.end), r);
  r = await E(() => { begin(2); G.timer = 0.5; sim(1); return { over: G.mode === "over", t: document.querySelector("#card h2")?.textContent }; });
  ok("D3 the timer running out fails the chapter, with Try again", r.over && /bombs went off/.test(r.t), r);
  r = await E(() => { document.querySelector("#f-retry").click(); sim(0.2); const o = { mode: G.mode, li: G.li }; G.p.hp = 5; G.p.armor = 0; R.hurtPlayer(50, G.p.x + 5, G.p.y); sim(1.2); o.fail = /Rish is down/.test(document.querySelector("#card h2")?.textContent || ""); return o; });
  ok("D4 retry restarts the chapter; losing all health shows Rish is down", r.mode === "play" && r.li === 2 && r.fail, r);
  // E. Chapter 3 boss
  r = await E(() => { begin(3); G.p.hp = G.p.maxHp = 50000; const bull = G.ents.find((e) => e.type === "bull"); const o = { guns: G.p.weapons.map((w) => w.id).join(",") }; let charge = false, dizzy = false, summoned = false;
    for (let k = 0; k < 900 && !bull.dead; k++) { if (bull.ph === 1 || bull.ph === 2) charge = true; if (bull.dizzy > 0) dizzy = true; if (G.ents.some((e) => e.k === "enemy" && e.type !== "bull")) summoned = true; G.p.x = bull.x - 90; G.p.y = bull.y; if (G.p.x < 60) G.p.x = bull.x + 90; if (G.p.wi < 0) G.p.wi = 0; G.p.weapons[G.p.wi].mag = 99; G.input.keys.add("fire"); sim(0.1); }
    G.input.keys.delete("fire"); o.hp = Math.round(G.p.hp); o.bhp = Math.round(bull.hp); o.mode = G.mode; o.dead = bull.dead; o.charge = charge; o.summoned = summoned; sim(3); for (let i = 0; i < 30 && G.mode === "dialog"; i++) R.dialogSkip(); sim(0.1); o.end = document.querySelector("#card h2")?.textContent; return o; });
  ok("E1 Bull boss: charges, calls his men, and goes down; chapter complete", r.dead && r.charge && r.summoned && /Chapter 3/.test(r.end || ""), r);
  // F. Chapter 4 city
  r = await E(() => { begin(4); godMode(); const o = {}; const sn = G.ents.find((e) => e.type === "sniper"); G.p.hp = 100; G.p.maxHp = 100; G.p.x = sn.x - 300; G.p.y = sn.y; let laser = false; for (let i = 0; i < 80; i++) { sim(0.05); if (sn.snipe > 0) laser = true; } o.laser = laser; o.sniperHit = G.p.hp < 100; godMode(); clearEnemies(); freeAll(); o.free = G.ob.free + "/" + G.ob.freeN; o.end = toExit(); return o; });
  ok("F1 Chapter 4: the sniper shows a laser before shooting", r.laser, r);
  ok("F2 city people rescued, harbour reached", /Chapter 4/.test(r.end) && r.free.split("/")[0] === r.free.split("/")[1], r);
  // G. Chapter 5 island
  r = await E(() => { begin(5); godMode(); const o = {}; const sh = G.ents.find((e) => e.type === "shield"); G.p.wi = 0; G.p.weapons[0].mag = 50; G.p.x = sh.x + Math.cos(sh.face) * 90; G.p.y = sh.y + Math.sin(sh.face) * 90; sh.alert = true; sh.face = Math.atan2(G.p.y - sh.y, G.p.x - sh.x); const h0 = sh.hp; G.input.mouse.active = -99; for (let i = 0; i < 6; i++) { G.p.aim = Math.atan2(sh.y - G.p.y, sh.x - G.p.x); sh.face = Math.atan2(G.p.y - sh.y, G.p.x - sh.x); G.input.keys.add("fire"); R.step(0.05); } G.input.keys.delete("fire"); sim(0.3); o.blocked = sh.hp === h0; G.p.x = sh.x + Math.cos(sh.face) * 40; G.p.y = sh.y + Math.sin(sh.face) * 40; G.p.aim = Math.atan2(sh.y - G.p.y, sh.x - G.p.x); G.p.kick = 0; R.melee(true); o.shieldGone = !sh.shield;
    const L = G.lasers[0]; G.p.hp = 100; G.p.maxHp = 100; G.lvT = (3 - L.ph + 0.2) % 3; G.p.x = L.x; G.p.y = L.y; R.step(0.02); o.laser = G.p.hp < 100; godMode(); o.door = G.map.some((row) => row.includes("D")); for (const d of G.drops.filter((q) => q.k === "key")) { G.p.x = d.x; G.p.y = d.y; sim(0.1); } o.open = !G.map.some((row) => row.includes("D")); clearEnemies(); const dad = G.ents.find((e) => e.k === "host" && e.dad); G.p.x = dad.x - 20; G.p.y = dad.y; R.takedownOrAct(); sim(1.2); o.dadTalk = G.mode === "dialog"; for (let i = 0; i < 20 && G.mode === "dialog"; i++) R.dialogSkip(); o.end = toExit(); return o; });
  ok("G1 shield trooper blocks bullets from the front; a kick knocks the shield away", r.blocked && r.shieldGone, r);
  ok("G2 lasers hurt; 3 keycards open the big door", r.laser && r.door && r.open, r);
  ok("G3 Rish finds his father; chapter complete", r.dadTalk && /Chapter 5/.test(r.end), r);
  // H. Chapter 6 final boss and ending
  r = await E(() => { begin(6); godMode(); const kade = G.ents.find((e) => e.type === "kade"); const o = { guns: G.p.weapons.length }; let shield = false, drones = false, minigun = false; const genSet = new Set();
    for (let k = 0; k < 2500 && !kade.dead; k++) { if (kade.invuln) shield = true; if (kade.ph === 1) minigun = true; if (G.ents.some((e) => e.type === "drone")) drones = true; const tgt = G.ents.find((e) => e.type === "gen" && !e.dead) || (kade.invuln ? null : kade) || G.ents.find((e) => e.k === "enemy" && !e.dead); if (!tgt) { sim(0.1); continue; } for (const g2 of G.ents) if (g2.type === "gen") genSet.add(g2); G.p.x = tgt.x - 80; G.p.y = tgt.y; G.p.weapons[G.p.wi].mag = 99; G.input.keys.add("fire"); sim(0.1); }
    G.input.keys.delete("fire"); o.dead = kade.dead; o.shield = shield; o.drones = drones; o.gens = genSet.size; o.minigun = minigun; sim(3); o.code = !!(G.mini && G.mini.code); if (o.code) { const wrong = (G.mini.seq[0] + 1) % 4; sim(5); R.codeKey(wrong); o.reset = G.mini.i === 0 && G.mini.show === 0; sim(5); for (const x of G.mini.seq.slice()) R.codeKey(x); } sim(0.2); for (let i = 0; i < 60 && G.mode === "dialog"; i++) R.dialogSkip(); o.end = document.querySelector("#card h1")?.textContent; o.ending = S.ending; o.unlocked = S.unlocked; return o; });
  ok("H1 Kade: minigun, drones, energy shield with 3 generators", r.minigun && r.drones && r.shield && r.gens >= 3 && r.dead, r);
  ok("H2 launch code: a wrong arrow resets; the right code stops Skyfall; THE END", r.code && r.reset && r.end === "THE END" && r.ending && r.unlocked === 7, r);
  await p.screenshot({ path: `${SHOTS}/03-end.png` });
  // I. Training, settings, save
  r = await E(() => { S.stars = 1000; R.training(() => R.menu()); const c = document.querySelector('[data-up="hp"]'); const s0 = S.stars; c.click(); const o = { hp: S.up.hp, paid: s0 - S.stars }; R.settings(); document.querySelector('[data-df="easy"]').click(); o.diff = S.diff; document.querySelector('[data-df="normal"]').click(); begin(1); o.maxHp = G.p.maxHp; return o; });
  ok("I1 training buys +20 health; settings change difficulty", r.hp >= 1 && r.paid === 80 && r.diff === "easy" && r.maxHp >= 120, r);
  r = await E(() => { const k = Object.keys(localStorage).find((x) => x.startsWith("rish-hero")); const d = JSON.parse(localStorage.getItem(k)); return { k, unlocked: d.unlocked, up: d.up.hp }; });
  ok("I2 progress is saved", r.k === "rish-hero.v1" && r.unlocked === 7 && r.up >= 1, r);
  // J. Story wording stays kind: made-up gang, no real groups
  r = await E(() => { const all = JSON.stringify(R.G && window.__rh.LEVELS); return { kade: /Black Viper/.test(all), friends: /Will you be my friend/.test(all), dad: /Major Arjun Sharma/.test(all), bad: /terrorist|ISIS|Taliban|al-?Qaeda/i.test(all) }; });
  ok("J1 the story: the made-up Black Viper gang, Rish finds his father, his classmates become friends", r.kade && r.friends && r.dad && !r.bad, r);
  r = await E(() => G.lastErr || ""); ok("J2 no loop errors", !r, r.slice(0, 300));
  // K. Phone layout
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true }); const mp = await m.newPage(); mp.on("pageerror", (e) => errs.push("M " + e.message)); await mp.goto(URL); await mp.waitForFunction(() => window.__rh && window.__rh.step, null, { timeout: 60000 }); await mp.evaluate(HELPERS);
  r = await mp.evaluate(() => { begin(1); const ids = ["joy", "t-fire", "t-punch", "t-kick", "t-roll", "t-nade", "t-act", "t-swap", "t-focus", "bars", "mini", "pause", "wpn", "obj"], R2 = ids.map((i) => [i, document.getElementById(i).getBoundingClientRect()]), bad = []; for (let i = 0; i < R2.length; i++) for (let j = i + 1; j < R2.length; j++) { const [a, p2] = R2[i], [bb, q] = R2[j]; if (p2.left < q.right && q.left < p2.right && p2.top < q.bottom && q.top < p2.bottom) bad.push(a + "/" + bb); } const vis = getComputedStyle(document.querySelector("#touch")).display; return { bad, vis }; });
  ok("K1 phone: stick and 8 buttons shown, nothing overlaps", r.vis === "block" && r.bad.length === 0, r);
  r = await mp.evaluate(() => { const fire = document.querySelector("#t-fire"); fire.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 5 })); const on = !!G.input.touch.fire; fire.dispatchEvent(new PointerEvent("pointerup", { bubbles: true, pointerId: 5 })); const joy = document.querySelector("#joy"), jr = joy.getBoundingClientRect(); joy.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerId: 7, clientX: jr.left + jr.width / 2 + 40, clientY: jr.top + jr.height / 2 })); const x0 = G.p.x; sim(0.5); const moved = G.p.x - x0; joy.dispatchEvent(new PointerEvent("pointerup", { bubbles: true, pointerId: 7 })); return { on, moved }; });
  ok("K2 phone: fire button and stick work", r.on && r.moved > 20, r);
  await mp.screenshot({ path: `${SHOTS}/04-phone.png` });
  ok("K3 no page errors", errs.length === 0, errs.slice(0, 5));
  console.log(`\nRESULT ${pass} passed, ${fail} failed`); await b.close(); process.exit(fail ? 1 : 0);
})().catch((e) => { console.log("CRASH", e); process.exit(2); });
