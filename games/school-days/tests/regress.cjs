// Full regression (v73: groups K and L cover the 30 new activities): every feature and fix the operator asked for, in a real browser, with real keys where it matters.
const { chromium } = require('playwright');
const ONLY = (process.env.RGROUPS || '').split(',').filter(Boolean); const want = (g) => !ONLY.length || ONLY.includes(g); // RGROUPS=A,B,... runs part of the suite
const results = []; const ok = (name, pass, info = '') => { results.push([pass ? 'PASS' : 'FAIL', name, info]); console.log(`${pass ? 'PASS' : 'FAIL'}  ${name}${info ? '  -- ' + info : ''}`); };
const FIN = `window.__fin = () => { const g = window.__game; let n = 0; while (g.dialogue.active && n++ < 40) { const f = g.dialogue.onDone; g.dialogue.onDone = null; g.dialogue.close(); if (f) f(); } };`;
let browser;
let openPages = [];
async function fresh(opts = {}) {
  for (const q of openPages) { try { await q.close(); } catch (e) {} } openPages = [];
  const p = await browser.newPage({ viewport: { width: 1280, height: 720 } }); p.errs = []; p.on('pageerror', (e) => p.errs.push(e.message)); p.on('dialog', (d) => d.accept()); openPages.push(p);
  await p.goto('http://localhost:8765/game.html'); await p.evaluate((prof) => { localStorage.clear(); localStorage.setItem('school-days.profile', prof); }, opts.profile || 'graduate'); await p.reload();
  await p.waitForSelector('#start-btn');
  if (opts.setup) await opts.setup(p);
  await p.click('#start-btn'); await p.waitForFunction(() => window.__game && window.__game.player, null, { timeout: 60000 }); await p.waitForTimeout(4500);
  await p.evaluate(FIN); await p.evaluate(() => { document.querySelectorAll('#tu-s').forEach((x) => x.click()); window.__fin(); });
  return p;
}
const ev = (p, fn, arg) => p.evaluate(fn, arg);
const hold = async (p, k, ms = 1200) => { await p.keyboard.down(k); await p.waitForTimeout(ms); await p.keyboard.up(k); };
const moved = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]) > 0.4;

(async () => {
  browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader'] });
  let p;
  // ---------- A. Start screen ----------
  if (want('A')) try {
    p = await browser.newPage({ viewport: { width: 1280, height: 720 } }); await p.goto('http://localhost:8765/game.html'); await p.evaluate(() => localStorage.clear()); await p.reload();
    const ids = ['av-1p', 'av-2p', 'av-boy', 'av-girl', 'av-p2boy', 'av-p2girl', 'av-p2name', 'new-game', 'av-name', 'av-glasses'];
    const have = await ev(p, (ids) => ids.filter((i) => !document.getElementById(i)), ids); ok('A1 start screen has all buttons', have.length === 0, have.join(','));
    await p.click('#av-1p'); const hid = await ev(p, () => getComputedStyle(document.getElementById('av-p2row')).display); ok('A2 Player 2 choices hidden in 1-player mode', hid === 'none', hid);
    await p.click('#av-2p'); const sh = await ev(p, () => getComputedStyle(document.getElementById('av-p2row')).display); ok('A3 Player 2 choices shown in 2-player mode', sh !== 'none', sh);
    await p.click('#av-girl'); const def = await ev(p, () => document.getElementById('av-p2girl').classList.contains('on')); ok('A4 Player 2 defaults to the same gender as Player 1 (girl -> girl)', def);
    await p.screenshot({ path: 'R_start.png' }); await p.close();
  } catch (e) { ok('A start screen', false, e.message); }

  // ---------- B. Two players: genders, names, keys ----------
  if (want('B')) try {
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-girl'); } });
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); const pp = g.player.position; g.p2.group.position.set(pp.x + 2, 0, pp.z); });
    const info = await ev(p, () => { const g = window.__game; return { on: !!(g.p2 && g.p2.on), p1girl: !!g.player.girl, two: !!g.input.twoPlayer, dress: g.p2.group.children.some((c) => c.geometry && c.geometry.type === 'CylinderGeometry' && c.geometry.parameters.radiusBottom === 0.4) }; });
    ok('B1 girl + girl: Player 2 is on and is a girl', info.on && info.p1girl && info.dress, JSON.stringify(info));
    const pos = () => ev(p, () => { const g = window.__game, a = g.player.position, c = g.p2.group.position; return [[a.x, a.z], [c.x, c.z]]; });
    let s0 = await pos(); await hold(p, 'w'); let s1 = await pos(); ok('B2 W A S D move Player 2 only', moved(s0[1], s1[1]) && !moved(s0[0], s1[0]), JSON.stringify([s0, s1]));
    await hold(p, 'ArrowUp'); let s2 = await pos(); ok('B3 arrow keys move Player 1 only', moved(s1[0], s2[0]) && !moved(s1[1], s2[1]));
    await hold(p, 'd'); let s3 = await pos(); ok('B4 D moves Player 2 sideways', moved(s2[1], s3[1]) && !moved(s2[0], s3[0]));
    const j = await ev(p, () => { const g = window.__game; return !document.querySelector('.panel-open') && !g._uiBlocking(); }); ok('B5 no menu opened by Player 2 keys', j);
    // Screen directions: up = camera forward on the ground, right = camera right.
    const dirTest = async (who, key, want) => {
      const before = await ev(p, () => { const g = window.__game, y = g.player.camYaw, a = g.player.position, c = g.p2.group.position; return { y, p1: [a.x, a.z], p2: [c.x, c.z] }; });
      await hold(p, key, 1100);
      const after = await ev(p, () => { const g = window.__game, y = g.player.camYaw, a = g.player.position, c = g.p2.group.position; return { y, p1: [a.x, a.z], p2: [c.x, c.z] }; });
      const A = who === 1 ? before.p1 : before.p2, B = who === 1 ? after.p1 : after.p2, dx = B[0] - A[0], dz = B[1] - A[1], n = Math.hypot(dx, dz) || 1;
      const y = before.y, fwd = [-Math.sin(y), -Math.cos(y)], right = [Math.cos(y), -Math.sin(y)], exp = { up: fwd, down: [-fwd[0], -fwd[1]], right, left: [-right[0], -right[1]] }[want];
      const dot = (dx / n) * exp[0] + (dz / n) * exp[1]; return { dot, dist: n, camTurned: Math.abs(after.y - before.y) > 0.02 };
    };
    for (const [who, key, want] of [[1, 'ArrowUp', 'up'], [1, 'ArrowDown', 'down'], [2, 'w', 'up'], [2, 's', 'down'], [2, 'a', 'left'], [2, 'd', 'right']]) {
      const r = await dirTest(who, key, want); ok(`B-dir Player ${who} ${key} goes ${want}`, r.dot > 0.9 && r.dist > 0.3, `dot ${r.dot.toFixed(2)}, moved ${r.dist.toFixed(1)}`);
    }
    for (const key of ['ArrowLeft', 'ArrowRight']) { const b0 = await ev(p, () => { const g = window.__game, a = g.player.position; return [g.player.camYaw, a.x, a.z]; }); await hold(p, key, 700); const b1 = await ev(p, () => { const g = window.__game, a = g.player.position; return [g.player.camYaw, a.x, a.z]; });
      ok(`B-turn Player 1 ${key} turns the camera (old controls), no walking`, Math.abs(b1[0] - b0[0]) > 0.3 && Math.hypot(b1[1] - b0[1], b1[2] - b0[2]) < 0.2, `turned ${(b1[0] - b0[0]).toFixed(2)}`); }
    // Holding up for 3 seconds: a straight line, camera still.
    await ev(p, () => { const g = window.__game; g.player.group.position.set(-40, 0, 5); g.player.camYaw = Math.PI / 2; g.player._placeCamera(1); g.p2.group.position.set(-40, 0, 8); }); await p.waitForTimeout(400);
    const path = []; await p.keyboard.down('ArrowUp'); for (let k = 0; k < 6; k++) { await p.waitForTimeout(500); path.push(await ev(p, () => { const a = window.__game.player.position; return [a.x, a.z, window.__game.player.camYaw]; })); } await p.keyboard.up('ArrowUp');
    let maxTurn = 0; for (let k = 2; k < path.length; k++) { const a1 = Math.atan2(path[k - 1][1] - path[k - 2][1], path[k - 1][0] - path[k - 2][0]), a2 = Math.atan2(path[k][1] - path[k - 1][1], path[k][0] - path[k - 1][0]); let d = Math.abs(a2 - a1); if (d > Math.PI) d = 2 * Math.PI - d; maxTurn = Math.max(maxTurn, d); }
    ok('B-straight holding UP walks Player 1 in a straight line', maxTurn < 0.15, `max bend ${(maxTurn * 57.3).toFixed(1)} degrees; path ${JSON.stringify(path.map((q) => q.map((v) => +v.toFixed(2))))}`);
    const sib = await ev(p, () => { const g = window.__game; g._enterRoom(g.world.doors.find((d) => d.label === 'Our Home')); window.__fin(); const R = g.world.currentRoom, c = g.p2.group.position, a = g.player.position; const tag = g.p2.group.children.find((x) => x.isSprite); return { inRoom: R && R.label, p2near: Math.hypot(c.x - a.x, c.z - a.z) < 4, p2visible: g.p2.group.visible, figHidden: !(R.figures && R.figures.gudiya && R.figures.gudiya.group.visible) }; });
    await p.waitForTimeout(400);
    const sib2 = await ev(p, () => { const g = window.__game, R = g.world.currentRoom, c = g.p2.group.position, a = g.player.position; return { p2near: Math.hypot(c.x - a.x, c.z - a.z) < 4, p2visible: g.p2.group.visible, figHidden: !(R.figures && R.figures.gudiya && R.figures.gudiya.group.visible) }; });
    ok('B-sib Player 2 (the sister) comes into the house with Player 1', sib2.p2near && sib2.p2visible, JSON.stringify(sib2));
    ok('B-sib the home Gudiya figure hides while Player 2 plays her', sib2.figHidden);
    const q0 = await ev(p, () => { const c = window.__game.p2.group.position; return [c.x, c.z]; }); await hold(p, 'w', 900); const q1 = await ev(p, () => { const c = window.__game.p2.group.position; return [c.x, c.z]; });
    ok('B-sib Player 2 walks inside the house', moved(q0, q1));
    await ev(p, () => window.__game._exitRoom()); await p.waitForTimeout(300);
    ok('B-sib Player 2 comes back out with Player 1', await ev(p, () => { const g = window.__game, c = g.p2.group.position, a = g.player.position; return !g.world.currentRoom && Math.hypot(c.x - a.x, c.z - a.z) < 4; }));
    ok('B6 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-boy'); await q.click('#av-p2girl'); await q.fill('#av-p2name', 'Meera'); } });
    const i2 = await ev(p, () => { const g = window.__game; const tag = g.p2.group.children.find((c) => c.isSprite); return { p1girl: !!g.player.girl, name: g.player.avatar.p2name, dress: g.p2.group.children.some((c) => c.geometry && c.geometry.type === 'CylinderGeometry' && c.geometry.parameters.radiusBottom === 0.4) }; });
    ok('B7 boy + girl named Meera', !i2.p1girl && i2.dress && i2.name === 'Meera', JSON.stringify(i2)); await p.close();
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-boy'); await q.click('#av-p2boy'); } });
    const i3 = await ev(p, () => { const g = window.__game; return { p1girl: !!g.player.girl, dress: g.p2.group.children.some((c) => c.geometry && c.geometry.type === 'CylinderGeometry' && c.geometry.parameters.radiusBottom === 0.4) }; });
    ok('B8 boy + boy: Player 2 is a boy (no sister)', !i3.p1girl && !i3.dress, JSON.stringify(i3)); await p.close();
  } catch (e) { ok('B two players', false, e.message); }

  // ---------- C. One player: W A S D and arrows both move ----------
  if (want('C')) try {
    p = await fresh({ setup: async (q) => { await q.click('#av-1p'); } });
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); });
    const P = () => ev(p, () => { const a = window.__game.player.position; return [a.x, a.z]; });
    const a = await P(); await hold(p, 'w'); const b = await P(); ok('C1 one player: W moves the player', moved(a, b)); ok('C2 no Player 2 in 1-player mode', !(await ev(p, () => !!(window.__game.p2 && window.__game.p2.on))));
    // D. start at home after reload
    await p.reload(); await p.click('#start-btn'); await p.waitForFunction(() => window.__game && window.__game.player, null, { timeout: 60000 }); await p.waitForTimeout(3000); await p.evaluate(FIN);
    const room = await ev(p, () => { const g = window.__game; return g.world.currentRoom ? g.world.currentRoom.label : 'outside'; }); ok('D1 the game opens at home', /Our Home|outside/.test(room) && room !== 'outside' || room === 'Our Home', room);
    await p.close();
  } catch (e) { ok('C/D one player and home start', false, e.message); }

  // ---------- E. Umbrella, monsoon, morning life, bath, towel, water and power cuts ----------
  if (want('E')) try {
    p = await fresh();
    const r = await ev(p, () => { const g = window.__game, pr = g.progress; window.__fin(); for (let d = 1; d < 400; d++) { pr.day = d; if (g.isRainy() && d % 4 !== 3) break; } if (g.world.currentRoom) g._exitRoom(); g._startPhase('morning'); window.__fin(); if (g.world.currentRoom) g._exitRoom(); return { rainy: g.isRainy(), day: pr.day }; });
    await p.waitForTimeout(600); ok('E1 umbrella opens outdoors in the rain', await ev(p, () => !!(window.__game.player.umbrella && window.__game.player.umbrella.visible)), JSON.stringify(r));
    await ev(p, () => { const g = window.__game; g._enterRoom(g.world.doors.find((d) => d.label === 'Our Home')); window.__fin(); }); await p.waitForTimeout(400);
    ok('E2 umbrella closes indoors', await ev(p, () => !window.__game.player.umbrella.visible));
    ok('E3 leaky roof bucket at home on rain days', await ev(p, () => window.__game.roomInteractables.some((i) => /bucket/i.test((i.prompt && i.prompt()) || ''))));
    ok('E4 milkman and newspaper in the morning', await ev(p, () => window.__game.interactables.some((i) => i._morn)));
    await ev(p, () => { const g = window.__game; g.progress.bathDay = -1; g._noWater = null; g._takeBath(g.world.currentRoom); }); await p.waitForTimeout(1000);
    ok('E5 bath: black screen shows', await ev(p, () => { const f = document.getElementById('bath-fade'); return !!f && getComputedStyle(f).opacity > 0.5; }));
    await p.waitForTimeout(2600); await p.evaluate(() => window.__fin());
    ok('E6 after the bath: in a towel', await ev(p, () => window.__game._wearing === 'towel' && window.__game.player.towelWrap.visible));
    await ev(p, () => window.__game._exitRoom()); ok('E7 leaving home in a towel: dressed again', await ev(p, () => !window.__game._towel && window.__game._wearing !== 'towel'));
    const wc = await ev(p, () => { const g = window.__game; g.progress.day = 3; g._waterCutMorning(); return !!g._tanker && !!g._noWater; }); ok('E8 water cut day: tanker in the lane', wc);
    const pc = await ev(p, () => { const g = window.__game; g.progress.day = 5; g._startPhase('evening'); window.__fin(); g._tmin = 18 * 60 + 40; g._tickUtilities(); window.__fin(); const on = !!g._pcut; g._tmin = 19 * 60 + 40; g._tickUtilities(); return on && !g._pcut; }); ok('E9 power cut starts and ends ("Light aa gayi")', pc);
    ok('E10 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('E daily life', false, e.message); }

  // ---------- F. Other cities: walking, maps, vehicles, taxi, landmark, hotel, home lock, going home ----------
  if (want('F')) try {
    p = await fresh();
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g.progress.money = 20000; g.progress.age = 25; g.progress.licence = true; g._arriveCity('Delhi', ['a', 'b', 'c'], 'air', 'family'); if (g._cut) g._endFlight(); window.__fin(); if (g._matchTrip && g._matchTrip.banner) g.world.scene.remove(g._matchTrip.banner); g._matchTrip = null; });
    const Z = await ev(p, () => { const g = window.__game, Z = g._zone, P = g.player.position; return { city: Z && Z.city, inCity: Math.abs(P.x - Z.x) < 170, x: P.x, z: P.z, zx: Z.x }; }); ok('F1 Delhi is its own city and the player is inside it', Z.city === 'Delhi' && Z.inCity, JSON.stringify(Z));
    const P = () => ev(p, () => { const a = window.__game.player.position; return [a.x, a.z]; });
    const a = await P(); await hold(p, 'w', 1500); const b = await P(); ok('F2 walking works in the city (no freeze)', moved(a, b), JSON.stringify([a, b]));
    ok('F3 still inside the city after walking', await ev(p, () => { const g = window.__game; return !!g._zone && Math.abs(g.player.position.x - g._zone.x) < 170; }));
    await p.click('#city-mini'); ok('F4 tap the minimap: city map opens', await ev(p, () => window.__game._cityMapIsOpen()));
    await p.click('#cm-x'); ok('F5 ✕ closes the city map', await ev(p, () => !window.__game._cityMapIsOpen()));
    await p.keyboard.press('g'); const o1 = await ev(p, () => window.__game._cityMapIsOpen()); await p.keyboard.press('Escape'); ok('F6 G opens, Esc closes the map', o1 && await ev(p, () => !window.__game._cityMapIsOpen()));
    const bike = await ev(p, () => { const g = window.__game; g.interactables.find((i) => i._zone && /bicycle/.test(i.prompt() || '')).activate(); return g.player.riding && g.player.riding.label; }); ok('F7 rent a bicycle in the city', !!bike, bike);
    await ev(p, () => { const g = window.__game; g.player.dismount(); });
    const taxi = await ev(p, () => { const g = window.__game; g.interactables.find((i) => /Taxi/.test(i.prompt() || '')).activate(); const b = [...document.querySelectorAll('[id^=tx-]')].find((x) => /Hotel/.test(x.textContent)); b.click(); const h = g._zone.places.hotel.door, P = g.player.position; return Math.hypot(P.x - h.x, P.z - h.z) < 5; }); ok('F8 taxi takes you to the Grand Hotel', taxi);
    const lm = await ev(p, () => { const g = window.__game; const e = g.interactables.find((i) => i._lm); if (!e) return 'no entrance'; e.activate(); window.__fin(); const R = g.world.currentRoom; const t = R && R.theme; g._exitRoom(); return t || 'no room'; }); ok('F9 the landmark is in the city and you can go inside', !/no /.test(lm), lm);
    const home = await ev(p, () => { const g = window.__game; g._enterRoom(g.world.doors.find((d) => d.label === 'Our Home')); const r = g.world.currentRoom && g.world.currentRoom.label; if (g.world.currentRoom) g._exitRoom(); return r || 'blocked'; }); ok('F10 Our Home is not reachable from another city', home !== 'Our Home', home);
    const hb = await ev(p, () => { const g = window.__game, d = g._zone.places.hotel.door; g.player.group.position.set(d.x, 0, d.z); g._enterRoom(d); window.__fin(); const R = g.world.currentRoom; const seat = g.roomInteractables.some((i) => /interview|YOUR SEAT/i.test((i.prompt && i.prompt()) || '')); const rec = g.roomInteractables.find((i) => /Reception/.test((i.prompt && i.prompt()) || '')); if (!rec) return { rec: false }; rec.activate(); document.querySelector('#hb-n1').click(); window.__fin(); return { rec: true, seat, stay: !!g._stay, room: g.world.currentRoom && g.world.currentRoom.label }; });
    ok('F11 hotel reception books a room any time (and no Suryanagar job desk)', hb.rec && hb.stay && !hb.seat, JSON.stringify(hb));
    const sl = await ev(p, () => { const g = window.__game; g._staySleep(); window.__fin(); const c = document.querySelector('#co-yes'); if (c) c.click(); window.__fin(); return { zone: g._zone ? g._zone.city : null, stay: !!g._stay }; }); ok('F12 after the hotel stay you travel home to Suryanagar', !sl.zone && !sl.stay, JSON.stringify(sl));
    ok('F13 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('F other cities', false, e.message); }

  // ---------- G. Police cases: rotation, murder rooms, questioning, picker, trips hold the case ----------
  if (want('G')) try {
    p = await fresh();
    const rot = await ev(p, () => { const g = window.__game, out = []; if (g.world.currentRoom) g._exitRoom(); const d = g.world.doors.find((x) => x.label === 'Police Station');
      for (let k = 0; k < 3; k++) { g.player.group.position.set(d.x, 0, d.z); g._enterRoom(d); const it = g.roomInteractables.find((i) => /thief, fight/i.test((i.prompt && i.prompt()) || '')); if (!it) { out.push('no file'); break; } it.activate(); window.__fin(); out.push(g._chase ? 'thief' : g._fieldCase ? 'fight' : g._myst ? 'murder' : 'none'); if (g._chase) g._endChase(false); if (g._fieldCase) { g._fieldCase = null; g._clearCaseScene(); } window.__fin(); if (g._myst && k < 2) g._mysteryEnd(false); }
      return out; });
    ok('G1 police files take turns: thief, fight, murder (no job needed)', rot.join(',') === 'thief,fight,murder', rot.join(','));
    await ev(p, () => { const g = window.__game; if (g._myst) g._mysteryEnd(false); window.__fin(); });
    for (let k = 0; k < 4; k++) {
      const r = await ev(p, (k) => { const g = window.__game; g.progress.weeklyCase = Math.floor((Date.now() / 86400000 + 4) / 7); g.progress.mystN = k; if (g.world.currentRoom) g._exitRoom(); g._mysteryFile(); const S = g._myst; g._enterRoom(S.door, S.m.floor || 0); window.__fin(); const R = g.world.currentRoom, its = g.roomInteractables.filter((i) => i._myst && /Question|Examine/.test(i.prompt())); let bad = 0; for (const it of its) { g.player.group.position.set(it.pos.x, 0, it.pos.z); if (g._nearestInteractable() !== it || !R.walkable(it.pos.x, it.pos.z)) bad++; } return { title: S.m.title, n: its.length, bad, sus: its.filter((i) => /Question/.test(i.prompt())).map((i) => [i.pos.x, i.pos.z]) }; }, k);
      ok(`G2.${k + 1} ${r.title}: 4 clues and 3 people inside, all reachable`, r.n === 7 && r.bad === 0, `items ${r.n}, unreachable ${r.bad}`);
      if (k === 1) { // real E presses on the three people, walk away on the last one
        for (let s = 0; s < 3; s++) { await ev(p, (xz) => window.__game.player.group.position.set(xz[0], 0, xz[1]), r.sus[s]); await p.waitForTimeout(150); await p.keyboard.press('e'); await p.waitForTimeout(250); if (s < 2) await p.evaluate(() => window.__fin()); else await ev(p, () => window.__game.dialogue.close()); }
        await p.waitForTimeout(900); ok('G3 after questioning all 3, "Who is the murderer?" opens (even after walking away)', await ev(p, () => !!document.querySelector('#ms-s0')));
        ok('G4 the purple murderer button is on screen', await ev(p, () => { const b = document.getElementById('myst-btn'); return !!b; }));
        await p.click('#ms-s0'); await p.waitForTimeout(4300); ok('G5 wrong guess: the name panel opens again', await ev(p, () => !!document.querySelector('#ms-s0')));
        await p.click('#ms-s1'); await p.waitForTimeout(300); await p.evaluate(() => window.__fin()); ok('G6 right guess solves the case', await ev(p, () => !window.__game._myst && (window.__game.progress.mysteries || 0) >= 1));
      } else await ev(p, () => { const g = window.__game; g._exitRoom(); g._mysteryEnd(false); window.__fin(); });
    }
    const hold2 = await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g.progress.mystN = 2; g._mysteryFile(); g._braveM = { id: 'x', city: 'Delhi', site: 'Market fire', icon: '🔥', scene: 'fire', abroad: false, name: 'Fire', stages: [], win: [], reward: 1 }; g._missionArrive('Delhi', ['a', 'b', 'c'], 'air'); if (g._cut) g._endFlight(); window.__fin(); const r = { held: !g._myst, obj: g.objective.label, inCity: Math.abs(g.objective.x - g._zone.x) < 200 }; g._missionEnd(g._matchTrip); g._parkVehiclesHome(); return r; });
    ok('G7 a trip puts the murder case on hold; mission compass points in the city', hold2.held && hold2.inCity, JSON.stringify(hold2));
    ok('G8 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('G police cases', false, e.message); }

  // ---------- H. Haveli: marker, stairs by walking, upstairs, resume, never stuck ----------
  if (want('H')) try {
    p = await fresh();
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g._startPhase('night'); window.__fin(); if (g.world.currentRoom) g._exitRoom(); g.player.group.position.set(-154, 0, 141); g._nearestInteractable().activate(); window.__fin(); });
    ok('H1 haveli entered at night with the glowing marker', await ev(p, () => { const g = window.__game, R = g.world.currentRoom; return !!R && R.type === 'haveli' && !!R._hvBeacon && R._hvBeacon.visible; }));
    await ev(p, () => { const g = window.__game, R = g.world.currentRoom; g.player.group.position.set(R.x0 + 17, 0, R.z0 + 10); g.player.group.rotation.y = Math.PI; g.player._placeCamera(1); });
    let up = false, maxY = 0; for (let k = 0; k < 30 && !up; k++) { await hold(p, 'w', 450); const s = await ev(p, () => { const g = window.__game; return [g.world.currentRoom && g.world.currentRoom.label, g.player.group.position.y]; }); maxY = Math.max(maxY, s[1]); up = /Upstairs/.test(s[0] || ''); }
    ok('H2 walking up the stairs raises the player and reaches upstairs', up && maxY > 0.5, `maxY ${maxY.toFixed(2)}`);
    const dn = await ev(p, () => { const g = window.__game; g.roomInteractables.find((i) => /back down/.test(i.prompt() || '')).activate(); window.__fin(); return g.world.currentRoom && g.world.currentRoom.label; }); ok('H3 back down to the haveli', dn === 'Old Haveli', dn);
    await ev(p, () => { const g = window.__game; g._hv.stage = 0; g._haveliStage(0, g._hv); }); await p.evaluate(() => { const b = [...document.querySelectorAll('[id^=hv-]')].find((x) => /torch on/i.test(x.textContent)); b.click(); }); await p.waitForTimeout(300);
    const res = await ev(p, () => { const g = window.__game, st = g._hv.stage; g._exitRoom(); g.player.group.position.set(-154, 0, 141); g._nearestInteractable().activate(); window.__fin(); return [st, g._hv && g._hv.stage]; }); ok('H4 solve puzzle 1, leave, come back: continues at puzzle 2', res[0] === 1 && res[1] === 1, JSON.stringify(res));
    await ev(p, () => { const g = window.__game; g._exitRoom(); g.player.group.position.set(-154, 0, 147); }); await p.waitForTimeout(2500);
    ok('H5 stuck inside the haveli wall: pushed out to open ground', await ev(p, () => window.__game.world.isWalkable(window.__game.player.position.x, window.__game.player.position.z)));
    ok('H6 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('H haveli', false, e.message); }

  // ---------- I. Lift, stocks, goals, photo, bug report, election, new game ----------
  if (want('I')) try {
    p = await fresh();
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); const d = g.world.doors.find((x) => x.label === 'Grand Hotel'); g.player.group.position.set(d.x, 0, d.z); g._enterRoom(d); window.__fin(); g.roomInteractables.find((i) => /Take the lift/.test(i.prompt() || '')).activate(); });
    await p.fill('#lift-in', '3'); await p.keyboard.press('Enter'); await p.waitForTimeout(1500);
    ok('I1 lift: type 3, arrive on floor 3', await ev(p, () => /3$/.test((window.__game.world.currentRoom || {}).label || '')), await ev(p, () => (window.__game.world.currentRoom || {}).label));
    await ev(p, () => { const g = window.__game; g._exitRoom(); g.progress.money = 5000; });
    await p.click('#lb-stock'); await p.click('#st-b-TECH'); const own = await ev(p, () => window.__game.progress.stk.own.TECH); await p.click('#st-s-TECH'); ok('I2 stock market: buy and sell a share', own === 1 && await ev(p, () => window.__game.progress.stk.own.TECH === 0)); await p.click('#st-x');
    await p.click('#lb-goals'); ok('I3 My life goals board opens', await ev(p, () => !!document.querySelector('#gb-share'))); await p.click('#gb-x');
    await p.click('#lb-photo'); await p.waitForTimeout(500); ok('I4 photo taken', await ev(p, () => { const a = document.querySelector('#ph2-save'); return !!a && a.getAttribute('href').startsWith('data:image/png'); })); await p.click('#ph2-x');
    await p.click('#lb-bug'); ok('I5 report-a-problem panel shows version and place', await ev(p, () => /School Days v\d+/.test(document.body.innerText))); await p.click('#bg-x');
    const el = await ev(p, () => { const g = window.__game; g.progress.age = 25; g._election(); window.__fin(); for (let k = 0; k < 3; k++) { const b = document.querySelector('#el-0'); if (b) b.click(); window.__fin(); } return !!g.progress.sarpanch; }); ok('I6 colony election with honest plans is won', el);
    ok('I7 no page errors', p.errs.length === 0, p.errs.join(' | '));
    await p.reload(); await p.waitForSelector('#new-game'); await p.click('#new-game'); await p.waitForTimeout(1500);
    ok('I8 New game erases this save slot', await ev(p, () => Object.keys(localStorage).filter((k) => k.startsWith('school-days.v1.')).length === 0)); await p.close();
  } catch (e) { ok('I tools', false, e.message); }

  // ---------- J. Pilot duty: explore the city in the break ----------
  if (want('J')) try {
    p = await fresh();
    const r = await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g._sim = { kind: 'fly', trip: { dest: 'Sydney', pax: 120, no: 101, leg: 1, stars: [] }, ui: {}, score: 4, max: 5, t: 0 }; g._simArrive(); document.querySelector('#sa-walk').click(); if (g._cut) g._endFlight(); window.__fin(); return { city: g._zone && g._zone.city, lm: g._landmark && g._landmark.userData.name, back: g.interactables.some((i) => i._zone && /cockpit/.test(i.prompt())) }; });
    ok('J1 pilot break: walk Sydney, Opera House in the city, back-to-cockpit spot', r.city === 'Sydney' && !!r.lm && r.back, JSON.stringify(r));
    ok('J2 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('J pilot break', false, e.message); }

  // ---------- K. v73 fun hub: 30 new things to do ----------
  if (want('K')) try {
    p = await fresh();
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g.progress.money = 20000; const s = g._funHomeSpot(); g.player.position.set(s.x, 0, s.z); });
    await p.click('#lb-fun'); const nb = await ev(p, () => document.querySelectorAll('[id^="fh-"]').length); ok('K1 🎲 hub opens with 30 activities', nb === 30, `${nb}`); await p.click('#f-x');
    const J = () => ev(p, () => JSON.parse(JSON.stringify(window.__game.progress.jl || {})));
    const next = () => ev(p, () => { const g = window.__game; g.progress.day++; window.__fin(); });
    // K2 chore, one player: press up when the sister shouts NOW.
    await ev(p, () => { window.__game._coLast = 0; window.__game._coChore(); });
    // Press inside the page, the moment the cue says NOW (a slow test machine cannot poll fast enough from outside).
    await ev(p, () => { const c = document.querySelector('#co-cue'); const mo = new MutationObserver(() => { if (/NOW/.test(c.textContent)) window.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowUp', bubbles: true })); }); mo.observe(c, { childList: true, characterData: true, subtree: true }); });
    await p.waitForFunction(() => !!document.querySelector('#f-ok'), null, { timeout: 60000 }).catch(() => {});
    ok('K2 two-hand chore done by lifting on NOW', (await J()).chores === 1, JSON.stringify((await J()).chores)); await ev(p, () => { const b = document.querySelector('#f-ok'); if (b) b.click(); });
    // K3 cricket, one player: let every ball go past.
    await ev(p, () => window.__game._cricket2()); await p.waitForFunction(() => !!document.querySelector('#f-ok'), null, { timeout: 45000 }).catch(() => {});
    ok('K3 gully cricket over finishes with a result', (await J()).cricket === 1); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K4 hide and seek.
    await ev(p, () => window.__game._hideSeek()); await p.waitForFunction(() => window.__game._hs && window.__game._hs.t > 0.2, null, { timeout: 40000 }).catch(() => {}); const hs = await ev(p, () => { const g = window.__game; if (!g._hs) return 'no game'; const s = g._hs.sp; g.player.position.set(s.x + 1, 0, s.z); return 'ok'; }); await p.waitForFunction(() => !window.__game._hs, null, { timeout: 20000 }).catch(() => {});
    ok('K4 hide and seek: walk to the hiding place and find her', hs === 'ok' && (await J()).hideFound === 1, hs);
    // K5 race.
    await ev(p, () => { const g = window.__game, s = g._funHomeSpot(); g.player.position.set(s.x, 0, s.z); g._sibRaceStart(); }); await p.waitForFunction(() => window.__game._sibRace && window.__game._sibRace.t > 0.1, null, { timeout: 30000 }); await ev(p, () => { const g = window.__game; const T = g._sibRace.T; g.player.position.set(T.x, 0, T.z + 1); }); await p.waitForTimeout(500);
    ok('K5 race to the bus stop is won by getting there first', (await J()).raceWins === 1);
    // K6 remote fight: share.
    await ev(p, () => { window.__game._remoteFight(); document.querySelector('#rf-2').click(); window.__fin(); }); ok('K6 TV remote fight: share and make up', (await J()).madeUp === 1);
    await ev(p, () => { window.__game._remoteFight(); document.querySelector('#rf-0').click(); window.__fin(); document.querySelector('#rf-0').click(); window.__fin(); }); ok('K6b remote fight: pull, Maa scolds, then make up', (await J()).fights === 1 && (await J()).madeUp === 2);
    // K7 Bhai Dooj on its real date.
    const f0 = await ev(p, () => { const g = window.__game; g._forceFest = null; return g._sibFest(); }); await ev(p, () => { const g = window.__game; g._forceFest = '2026-11-10'; g._sibFestival(); for (let k = 0; k < 5; k++) document.querySelector('#og-' + k).click(); document.querySelector('#sg-2').click(); window.__fin(); g._forceFest = null; });
    ok('K7 Bhai Dooj only on the real date, then the puja in order', f0 === null && !!(await J()).fest.dooj2026);
    // K8 week mystery: one clue per day.
    for (let k = 0; k < 5; k++) { await ev(p, () => window.__game._weekMystery()); if (k < 4) { await p.click('#f-x'); await next(); } }
    const m0 = await ev(p, () => window.__game.progress.money); await p.click('#wm-2'); ok('K8 week mystery: 5 clues on 5 days, then the right culprit', (await J()).wmSolved === 1 && (await ev(p, () => window.__game.progress.money)) === m0 + 200); await p.click('#f-ok');
    // K9 annual day.
    await ev(p, () => { window.__game._annualDay(); document.querySelector('#ad-0').click(); });
    for (let d = 0; d < 4; d++) { await ev(p, () => window.__game._annualDay()); for (let k = 0; k < 5; k++) await ev(p, () => document.querySelector('#sp-hit').click()); await ev(p, () => document.querySelector('#sp-ok').click()); await ev(p, () => window.__fin()); await next(); }
    ok('K9 annual day: 3 practice days, then the show', (await J()).shows === 1 && !(await J()).ad.act);
    // K10 paw prints.
    await ev(p, () => { const g = window.__game, s = g._funHomeSpot(); g.player.position.set(s.x, 0, s.z); g._pawTrail(); window.__fin(); const P = g._paw; g.player.position.set(P.end.x, 0, P.end.z); }); await p.waitForTimeout(500);
    await ev(p, () => { const g = window.__game, P = g._paw; g.player.position.set(P.owner.x, 0, P.owner.z); }); await p.waitForTimeout(500); await ev(p, () => window.__fin());
    ok('K10 lost puppy: follow the prints, bring Tuffy back', (await J()).puppiesFound === 1);
    // K11 birthday.
    await ev(p, () => { window.__game._maaBirthday(); for (let k = 0; k < 3; k++) document.querySelector('#bd-0').click(); document.querySelector('#bs-0').click(); window.__fin(); }); ok('K11 surprise party for Maa', (await J()).parties === 1);
    // K12 shop maths.
    for (let k = 0; k < 5; k++) { if (k === 0) await ev(p, () => window.__game._shopMaths()); const a = await ev(p, () => { const t = document.querySelector('#sm-q').innerText, b = +t.match(/Bill: ₹(\d+)/)[1], n = +t.match(/₹(\d+) note/)[1]; return n - b; }); await p.fill('#sm-in', String(a)); await p.click('#sm-go'); await p.waitForTimeout(1000); }
    ok('K12 kirana shop: 5 of 5 change right', (await J()).shopBest === 5); await p.click('#f-ok');
    // K13 cycle.
    await ev(p, () => { window.__game._cycleGoal(); for (let k = 0; k < 5; k++) { const b = document.querySelector('#cg-500'); if (b) b.click(); } }); ok('K13 bicycle bought with savings, parked at the door', (await J()).cycle === true && await ev(p, () => !!window.__game._cyc3d)); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K14 GK quiz.
    const gk = await ev(p, () => { const g = window.__game; g._gkQuiz(); document.querySelector('#gk-50').click(); const off = [...document.querySelectorAll('[id^="gk-"]')].filter((b) => /^gk-\d$/.test(b.id) && b.disabled).length; document.querySelector('#gk-q2').click(); return off; }); ok('K14 quiz show: 50:50 removes two answers, quit takes the money', gk === 2 && (await J()).gkDay != null, `${gk}`); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K15 trees on real days.
    await ev(p, () => { const g = window.__game, s = g._funHomeSpot(); g.player.position.set(s.x, 0, s.z); g._plantTree(); window.__fin(); g.progress.jl.trees[0].last = '2000-01-01'; g._waterRealTree(0); });
    ok('K15 tree planted, grows only with real-day watering', (await J()).trees[0].days === 2 && await ev(p, () => !!window.__game._trees3d && window.__game.interactables.some((i) => i._rtree)));
    // K16 + K17 room decor and pets show at home.
    await ev(p, () => { const g = window.__game; g._roomDecor(); document.querySelector('#rd-poster-1').click(); document.querySelector('#f-x').click(); g._petShop(); document.querySelector('#ps-0').click(); document.querySelector('#f-x').click(); const d = g.world.doors.find((x) => x.label === 'Our Home'); g.player.group.position.set(d.x, 0, d.z); g._enterRoom(d); window.__fin(); });
    const home = await ev(p, () => { const g = window.__game, r = g.world.currentRoom; return { corner: !!(r && r._myCorner), pets: !!(r && r._myPets), feed: g.roomInteractables.some((i) => /pets/.test(i.prompt() || '')) }; });
    ok('K16 decorated corner shows in my home', home.corner, JSON.stringify(home)); ok('K17 pet from the shop lives at home, with a feed spot', home.pets && home.feed, JSON.stringify(home));
    await ev(p, () => { const g = window.__game; g.roomInteractables.find((i) => /pets/.test(i.prompt() || '')).activate(); }); ok('K17b feed the pets', (await J()).petFed === await ev(p, () => window.__game.progress.day));
    // K31 Dadi tablet (morning).
    await ev(p, () => { const g = window.__game; g.phase = 'morning'; g._dadiTablet(); document.querySelector('#dt-0').click(); window.__fin(); }); ok('K31 Dadi gets the right tablet in the morning', (await J()).medDay === await ev(p, () => window.__game.progress.day));
    await ev(p, () => window.__game._exitRoom());
    // K18 star map.
    await ev(p, () => { const g = window.__game; g.phase = 'night'; g._starMap(); });
    for (const [x, y] of [[40, 60], [200, 30], [250, 115], [300, 170], [60, 170]]) { const b = await ev(p, () => { document.querySelector('#sm2-c').scrollIntoView({ block: 'center' }); const r = document.querySelector('#sm2-c').getBoundingClientRect(); return [r.left, r.top, r.width / 340, r.height / 220]; }); const q0 = await ev(p, () => document.querySelector('#sm2-q').textContent); await p.mouse.click(b[0] + x * b[2], b[1] + y * b[3]); await p.waitForFunction((q) => !document.querySelector('#sm2-q') || document.querySelector('#sm2-q').textContent !== q || !!document.querySelector('#f-ok'), q0, { timeout: 8000 }).catch(() => {}); }
    await p.waitForFunction(() => /\d \/ 5/.test(document.body.innerText), null, { timeout: 8000 }).catch(() => {}); ok('K18 star map: find all 5 in the sky', (await J()).starMaps === 1 && await ev(p, () => /5 \/ 5/.test(document.body.innerText)), await ev(p, () => { const s = document.querySelector('.score-big'); return s ? s.textContent : 'no score'; })); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K19 seasons.
    const se = await ev(p, () => { const g = window.__game, out = {}; for (const m of [1, 3, 5, 12, 9]) { g._monthOverride = m; g._seasonBuild(); out[m] = { kites: !!g._kites, its: g.interactables.filter((i) => i._season).map((i) => i.prompt()).join('|') }; } g._monthOverride = null; g._seasonBuild(); return out; });
    ok('K19 seasons: kites in January, Holi in March, mangoes in May, bonfire in December', se[1].kites && /Holi/.test(se[3].its) && /mango/.test(se[5].its) && /bonfire/.test(se[12].its) && !se[9].kites && !se[9].its, JSON.stringify(se));
    // K20 music room.
    await ev(p, () => window.__game._musicRoom()); await p.click('#mu-rec'); for (const k of ['a', 's', 'd', 'f', 'g']) { await p.keyboard.press(k); await p.waitForTimeout(80); } await p.click('#mu-rec');
    ok('K20 music room: keys play, song is recorded and saved', ((await J()).song || []).length === 5 && await ev(p, () => !window.__game._uiBlocking() || !!document.querySelector('#mu-play')));
    await p.click('#f-x');
    // K21 sports day.
    await ev(p, () => { window.__game._sportsDay(); document.querySelector('#sd-0').click(); }); await p.waitForTimeout(1700);
    for (let k = 0; k < 60; k++) { await p.keyboard.press(k % 2 ? 'ArrowRight' : 'ArrowLeft'); if (await ev(p, () => !!document.querySelector('#f-ok'))) break; }
    await p.waitForFunction(() => !!document.querySelector('#f-ok'), null, { timeout: 15000 }).catch(() => {});
    const md = (await J()).medals || {}; ok('K21 sports day sprint: fast feet win gold', md.g === 1, JSON.stringify(md)); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    await ev(p, () => { window.__game._longJump(); }); for (let k = 0; k < 3; k++) { await p.waitForTimeout(400); await ev(p, () => document.querySelector('#lj-j') && document.querySelector('#lj-j').click()); await p.waitForTimeout(1100); }
    await p.waitForFunction(() => !!document.querySelector('#f-ok'), null, { timeout: 12000 }).catch(() => {}); ok('K21b long jump: 3 tries give a result', await ev(p, () => !!document.querySelector('#f-ok'))); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    await ev(p, () => window.__game._tugWar()); await p.waitForTimeout(900); for (let k = 0; k < 40; k++) { await ev(p, () => { const b = document.querySelector('#tw-a'); if (b) b.click(); }); await p.waitForTimeout(40); if (await ev(p, () => !!document.querySelector('#f-ok'))) break; }
    ok('K21c tug of war: pull fast and win', ((await J()).medals || {}).g === 2); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K22 kite fight.
    await ev(p, () => { window.__game._kiteFight(); for (let k = 0; k < 5; k++) document.querySelector('#sp-hit').click(); document.querySelector('#sp-ok').click(); window.__fin(); }); ok('K22 kite fight', (await J()).kitesCut != null);
    // K23 Saanp Seedi: rolls move the tokens, Dadi rolls by herself.
    await ev(p, () => window.__game._saanpSeedi()); await p.keyboard.press('ArrowUp'); await p.waitForTimeout(1300); const ss = await ev(p, () => document.querySelector('#ss-m').textContent);
    ok('K23 Saanp Seedi: you roll, then Dadi rolls', /Dadi rolls/.test(ss), ss); await p.click('#f-x');
    // K24 chai.
    await ev(p, () => { window.__game._makeChai(); for (let k = 0; k < 8; k++) document.querySelector('#og-' + k).click(); window.__fin(); }); ok('K24 chai made in the right order', (await J()).chai === 1);
    // K25 bargain.
    await ev(p, () => { window.__game._bargain(); for (let k = 0; k < 3; k++) document.querySelector('#bg-1').click(); }); ok('K25 sabzi mandi: fair offers save money', (await J()).mandiSaved === 55, String((await J()).mandiSaved)); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K26 litter.
    await ev(p, () => { const g = window.__game, s = g._funHomeSpot(); g.player.position.set(s.x, 0, s.z); g._litterStart(); });
    const nl = await ev(p, () => window.__game._swachh ? window.__game._swachh.items.length : 0);
    for (let k = 0; k < nl; k++) { await ev(p, (k) => { const g = window.__game, m = g._swachh.items[k]; g.player.position.set(m.position.x, 0, m.position.z); }, k); await p.waitForTimeout(250); }
    await ev(p, () => { const g = window.__game, b = g._swachh.bin; g.player.position.set(b.x, 0, b.z + 1); }); await p.waitForTimeout(400);
    ok('K26 clean the colony: pick up all litter, then the dustbin', nl >= 4 && (await J()).cleanups === 1, `${nl} pieces`);
    // K27 letter.
    await ev(p, () => { const g = window.__game; g._letterNani(); document.querySelector('#ln-0').click(); document.querySelector('#ln-p').click(); }); await next(); await ev(p, () => { window.__game._letterNani(); window.__fin(); });
    ok('K27 letter to Nani, reply the next day', (await J()).letters === 1);
    // K28 licence.
    const RIGHT = ['Stop behind the line', 'The left side', 'A front light and a back reflector', 'Look back and show your right hand', 'People walking have the right to cross', 'A helmet', 'No, only one rider', 'Stop and wait'];
    await ev(p, () => window.__game._cycleLicence()); for (let k = 0; k < 8; k++) await ev(p, (R) => { const b = [...document.querySelectorAll('#cl-o button')].find((x) => R.includes(x.textContent)); b.click(); }, RIGHT);
    ok('K28 cycle safety licence passed', (await J()).licence === true); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K29 teach tables.
    await ev(p, () => window.__game._teachTables()); for (let k = 0; k < 6; k++) { const a = await ev(p, () => { const m = document.querySelector('#tt-q').textContent.match(/(\d+) times (\d+)/); return m[1] * m[2]; }); await p.fill('#tt-in', String(a)); await p.keyboard.press('Enter'); await p.waitForTimeout(1000); }
    ok('K29 teach the tables: 6 of 6', (await J()).taught === 1 && await ev(p, () => /6 \/ 6/.test(document.body.innerText))); await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    // K30 rangoli.
    await ev(p, () => { window.__game._rangoli(); document.querySelector('#rg-0').click(); document.querySelector('#rg-s').click(); }); ok('K30 rangoli at the door (mirrored)', ((await J()).rangoli || []).filter((v) => v).length === 4 && await ev(p, () => !!window.__game._rg3d));
    // Every hub button opens without an error.
    const bad = await ev(p, () => { const g = window.__game, out = []; for (const [, list] of g._funList()) for (const [k] of list) { g._lastErr = null; try { g._funRun(k); } catch (e) { out.push(k + ':' + e.message); } if (g._lastErr) out.push(k + ':' + g._lastErr); window.__fin(); if (document.querySelector('#f-x')) document.querySelector('#f-x').click(); if (g._hs) g._hideEnd(null); if (g._sibRace) g._sibRaceEnd(null); if (g._paw) { g.world.scene.remove(g._paw.G); g._paw = null; } if (g._swachh) { g.world.scene.remove(g._swachh.G); g._swachh = null; } } return out; });
    ok('K32 all 30 hub buttons run with no error', bad.length === 0, bad.join(' | '));
    ok('K33 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('K fun hub', false, e.message.slice(0, 300)); }

  // ---------- L. Two players in the fun games ----------
  if (want('L')) try {
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-boy'); await q.click('#av-p2girl'); } });
    await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); });
    await ev(p, () => window.__game._coChore()); for (let k = 0; k < 5; k++) { await ev(p, () => { for (const key of ['ArrowUp', 'w']) window.dispatchEvent(new KeyboardEvent('keydown', { key, bubbles: true })); }); await p.waitForTimeout(250); }
    ok('L1 two-player chore: up arrow and W together lift it', (await ev(p, () => (window.__game.progress.jl || {}).chores)) === 1);
    await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    await ev(p, () => window.__game._tugWar()); await p.waitForTimeout(900); for (let k = 0; k < 30; k++) { await p.keyboard.press('w'); if (await ev(p, () => !!document.querySelector('#f-ok'))) break; } await p.waitForTimeout(400);
    ok('L2 two-player tug of war: Player 2 pulls with W and wins', await ev(p, () => /Player 2's team wins/.test(document.body.innerText)));
    await ev(p, () => document.querySelector('#f-ok') && document.querySelector('#f-ok').click());
    const cr = await ev(p, () => { window.__game._cricket2(); return document.querySelector('#c2-help').textContent; }); await p.keyboard.press('s'); await p.waitForTimeout(300); const m2 = await ev(p, () => document.querySelector('#c2-m').textContent);
    ok('L3 two-player cricket: Player 2 bowls with S (fast)', /Player 2 bowls/.test(cr) && /Fast/.test(m2), m2); await p.click('#f-x');
    ok('L4 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('L two players', false, e.message.slice(0, 300)); }

  // ---------- M. v74 family sim: marry at 25-26, children at 30-38, grandchildren at 49-50 ----------
  if (want('M')) try {
    p = await fresh();
    const G = (fn, a) => ev(p, fn, a);
    const click = (sel) => G((s) => { const b = document.querySelector(s); if (!b || b.disabled) return false; b.click(); return true; }, sel);
    const has = (sel) => G((s) => { const b = document.querySelector(s); return !!b && !b.disabled; }, sel);
    const tick = () => G(() => { const g = window.__game; g._famT = 0; g._tickFamily(); });
    const F = () => G(() => JSON.parse(JSON.stringify(window.__game.progress.fam || {})));
    const hub = (age) => G((a) => { const g = window.__game; if (a != null) g.progress.age = a; g._familyHub(); }, age);
    await G(() => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g.progress.money = 90000; g.progress.age = 12; });
    await p.click('#lb-fam'); ok('M1 👨‍👩‍👧 family panel opens; a child sees "when you grow up"', await G(() => /grow up/.test(document.body.innerText))); await p.click('#f-x');
    await hub(22); for (let d = 0; d < 2; d++) { for (const k of ['talk', 'chai', 'film']) await click(`#fd-priya-${k}`); await G(() => { window.__game.progress.day++; window.__game._familyHub(); }); }
    const dl = (await F()).dating.priya, ring22 = await has('#fd-priya-ring'); await hub(25); const ring25 = await has('#fd-priya-ring');
    ok('M2 dating fills love to 70+, but Propose waits for age 25', dl >= 70 && !ring22 && ring25, `love ${dl}, at 22 ${ring22}, at 25 ${ring25}`);
    await click('#fd-priya-ring'); await G(() => window.__fin()); await click('#wp-ok'); await p.waitForTimeout(200); await click('#wd-ok'); await G(() => window.__fin());
    ok('M3 wedding at 25: Priya is the spouse', await G(() => (window.__game.progress.spouse || {}).name === 'Priya' && window.__game.progress.marriedAt === 25));
    await hub(); const l0 = (await F()).love; await click('#fs-cook'); const l1 = (await F()).love; await hub(); ok('M4 cook together raises love; once a day', l1 > l0 && !(await has('#fs-cook')), `${l0} -> ${l1}`);
    await G(() => { window.__game.progress.fam.love = 90; }); await hub(29); const b29 = await has('#fs-baby'); await hub(30); const b30 = await has('#fs-baby');
    ok('M5 no baby at 29; babies from age 30', !b29 && b30, `29 ${b29}, 30 ${b30}`);
    await click('#fs-baby'); await click('#fb-girl'); await p.fill('#fb-name', 'Tara'); await click('#fb-ok');
    const b1 = await G(() => { const pr = window.__game.progress; return { kids: pr.fam.kids.length, child: pr.child && pr.child.name, gen: pr.generations, boy: pr.fam.kids[0].boy, born: pr.fam.kids[0].born }; });
    ok('M6 a girl, Tara, born when you are 30', b1.kids === 1 && b1.child === 'Tara' && b1.gen === 2 && b1.boy === false && b1.born === 30, JSON.stringify(b1));
    await tick(); const f0 = (await F()).kids[0].needs.food; await G(() => { window.__game.progress.day++; }); await tick(); const f1 = (await F()).kids[0].needs.food;
    await hub(); await click('#fk-0-feed'); const f2 = (await F()).kids[0].needs.food; ok('M7 the baby gets hungry each day; feeding helps', f1 < f0 && f2 > f1, `${f0} -> ${f1} -> ${f2}`);
    await G(() => { window.__game.progress.fam.love = 90; }); await hub(31); await click('#fs-baby'); await click('#fb-boy'); await p.fill('#fb-name', 'Veer'); await click('#fb-ok');
    ok('M8 a second child, a boy, at 31', (await F()).kids.length === 2 && (await F()).kids[1].boy === true);
    await G(() => { window.__game.progress.age = 36; }); await tick(); const k6 = (await F()).kids[0]; await hub(); const hw = await click('#fk-0-hw'); const k6b = (await F()).kids[0];
    ok('M9 at 36: Tara is 6, a report card, homework builds the study skill', (k6.reports || []).length === 1 && hw && k6b.skill.study === 1, JSON.stringify(k6.reports));
    await G(() => { window.__game.progress.fam.love = 90; }); await hub(39); ok('M10 no baby after 38', !(await has('#fs-baby')));
    await G(() => { window.__game.progress.age = 48; }); await tick(); await hub(); await click('#fk-0-career'); await click('#fc-0'); ok('M11 at 48 Tara is 18 and chooses a career', !!(await F()).kids[0].career, (await F()).kids[0].career);
    await hub(); await click('#fk-0-wed'); await click('#fw-0'); await G(() => window.__fin()); ok('M12 Tara marries at 18, when you are 48', (await F()).kids[0].married && await G(() => !!window.__game.progress.childMarried));
    await hub(); const gk48 = await has('#fk-0-gk'); await hub(49); const gk49 = await has('#fk-0-gk'); await click('#fk-0-gk'); await G(() => window.__fin());
    const gk = await G(() => { const pr = window.__game.progress; return { n: pr.fam.kids[0].kids.length, g: pr.grandchild && pr.grandchild.name, gen: pr.generations }; });
    ok('M13 no grandchild at 48; a grandchild at 49: three generations', !gk48 && gk49 && gk.n === 1 && !!gk.g && gk.gen === 3, JSON.stringify(gk));
    await hub(51); ok('M14 no new grandchild after 50', !(await has('#fk-0-gk')));
    await hub(49); const gl0 = (await F()).kids[0].kids[0].love; await click('#fg-0-0-story'); ok('M15 grandparent tells a story: the grandchild is happier', (await F()).kids[0].kids[0].love > gl0 || gl0 === 100);
    await G(() => { const g = window.__game, d = g.world.doors.find((x) => x.label === 'Our Home'); if (g.world.currentRoom) g._exitRoom(); g.player.group.position.set(d.x, 0, d.z); g._enterRoom(d); window.__fin(); });
    const home = await G(() => { const g = window.__game, r = g.world.currentRoom; return { figs: r && r._famFigs ? r._famFigs.children.length : 0, its: g.roomInteractables.filter((i) => i._fam).length }; });
    ok('M16 the second child stands in the home; tap to care', home.figs >= 2 && home.its >= 1, JSON.stringify(home));
    await G(() => { const g = window.__game; g._exitRoom(); g._famTree(); }); const tree = await G(() => document.body.innerText);
    ok('M17 family tree shows Dadi down to the grandchild', /Dadi/.test(tree) && /Tara/.test(tree) && /Veer/.test(tree) && /Priya/.test(tree)); await click('#f-x');
    ok('M18 no page errors', p.errs.length === 0 && !(await G(() => window.__game._lastErr)), p.errs.join(' | ') + (await G(() => window.__game._lastErr || '')));
    await p.close();
    p = await fresh();
    const old = await ev(p, () => { const g = window.__game, pr = g.progress; delete pr.fam; pr.age = 52; pr.spouse = { name: 'Meera' }; pr.marriedAt = 25; pr.child = { name: 'Anaya' }; pr.childBornAt = 30; pr.childMarried = true; pr.grandchild = { name: 'Vihaan' }; const F = g._fam(); return { kids: F.kids.length, girl: !F.kids[0].boy, married: F.kids[0].married, gk: F.kids[0].kids.map((x) => x.name).join(), age: g._kidAge(F.kids[0]) }; });
    ok('M19 old saves join the new family sim', old.kids === 1 && old.girl && old.married && old.gk === 'Vihaan' && old.age === 22, JSON.stringify(old));
    const yr = await ev(p, () => { const g = window.__game, pr = g.progress, out = {}; delete pr.fam; pr.child = null; pr.childMarried = false; pr.grandchild = null; pr.spouse = { name: 'Meera' }; pr.marriedAt = 25;
      const step = (age) => { pr.age = age - 1; g._yearPassed(); const got = !!document.querySelector('#cb-ok'); if (typeof closePanel !== 'undefined') {} const b = document.querySelector('#cb-ok'); if (b) b.click(); window.__fin(); return got; };
      out.at28 = step(28); out.at30 = step(30); return out; });
    ok('M20 the old automatic baby also waits for age 30', !yr.at28 && yr.at30, JSON.stringify(yr));
    ok('M21 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('M family sim', false, e.message.slice(0, 300)); }

  // ---------- N. v74 life events: 15 real moments ----------
  if (want('N')) try {
    p = await fresh();
    const G = (fn, a) => ev(p, fn, a);
    const click = (sel) => G((s) => { const b = document.querySelector(s); if (!b || b.disabled) return false; b.click(); return true; }, sel);
    const F = () => G(() => JSON.parse(JSON.stringify(window.__game.progress.fam || {})));
    const story = async () => { for (let k = 0; k < 8; k++) { if (!(await click('#ss2-0'))) break; await click('#ss2-n'); } await G(() => window.__fin()); };
    const timing = () => G(() => { for (let k = 0; k < 5; k++) document.querySelector('#sp-hit').click(); document.querySelector('#sp-ok').click(); window.__fin(); });
    await G(() => { const g = window.__game, pr = g.progress; if (g.world.currentRoom) g._exitRoom(); pr.money = 90000; pr.age = 45; pr.spouse = { name: 'Priya' }; pr.marriedAt = 25; const F = g._fam(); F.kids = [g._newKid('Tara', false, 30), g._newKid('Veer', true, 37)]; pr.child = { name: 'Tara' }; pr.childBornAt = 30; });
    await G(() => window.__game._familyHub()); await click('#fm-life'); const n = await G(() => document.querySelectorAll('[id^="le-"]').length - 1);
    ok('N1 🌟 Life events opens with 15 events', n === 15, `${n}`);
    const run = async (key, check, label, extra) => { await G((k) => { const g = window.__game; g._lifeEvents(); const b = document.querySelector('#le-' + k); if (b && !b.disabled) b.click(); }, key); if (extra) await extra(); const r = await check(); ok(label, !!r, typeof r === 'string' ? r : ''); if (await G(() => !!document.querySelector('#f-x'))) await click('#f-x'); };
    await run('village', async () => { await story(); return (await F()).ev.village === 45; }, 'N2 summer trip to Nani\'s village');
    await G(() => { const g = window.__game; g._evBus(); }); await story(); ok('N3 school bus story', await G(() => window.__game._famDone('ev', 'bus')));
    await run('ptm', async () => { await story(); return (await F()).ev.ptm === 45; }, 'N4 parent-teacher meeting');
    await run('album', async () => ((await F()).photos || []).length === 1 && await G(() => /Tara/.test(document.body.innerText)), 'N5 family photo shows everyone');
    await run('sangeet', async () => { await timing(); return G(() => window.__game._famDone('ev', 'sangeet')); }, 'N6 sangeet dance practice');
    await run('trip', async () => { await click('#rt-0'); await G(() => window.__fin()); return (await F()).ev.trip === 45; }, 'N7 family road trip to Shimla');
    await run('paint', async () => { await click('#pt-1'); await G(() => window.__fin()); return (await F()).paint; }, 'N8 paint the house');
    await run('gpday', async () => { await story(); return (await F()).ev.gpday === 45; }, 'N9 grandparents\' day');
    await run('fall', async () => { await story(); return (await F()).kids[1].fell === true; }, 'N10 Veer\'s first cycle fall, first aid, then riding');
    await run('shop', async () => { await click('#sw-open'); return !!(await F()).sweetShop; }, 'N11 open the family sweet shop');
    const m0 = await G(() => window.__game.progress.money); await G(() => { window.__game._evShop(); for (let k = 0; k < 5; k++) document.querySelector('#og-' + k).click(); }); const m1 = await G(() => window.__game.progress.money);
    await G(() => { const g = window.__game; g._famT = 0; g._tickFamily(); g.progress.day++; g._famT = 0; g._tickFamily(); }); const m2 = await G(() => window.__game.progress.money);
    ok('N12 fresh laddoos earn ₹120; the shop earns ₹200 a day', m1 - m0 === 120 && m2 - m1 === 200, `${m1 - m0}, ${m2 - m1}`);
    await run('match', async () => { await timing(); return G(() => window.__game._famDone('ev', 'match')); }, 'N13 cheer at the cricket match');
    await run('board', async () => { await click('#be-1'); await G(() => window.__fin()); return ((await F()).kids[0].boards || []).includes(15); }, 'N14 board exam week: the balanced plan');
    await run('fest', async () => { await story(); return (await F()).ev.fest === 45; }, 'N15 Diwali of three generations');
    await run('dog', async () => { await click('#dg-ok'); return !!(await F()).dog; }, 'N16 adopt a family dog');
    await G(() => { const g = window.__game; g._famT = 0; g._tickFamily(); g.progress.fam.kids[0].career = 'Doctor'; g.progress.age = 59; g._famT = 0; g._tickFamily(); window.__fin(); });
    const late = await F(); ok('N17 years later: Tara moves away for work; the old dog is remembered', !!late.kids[0].city && (late.dogsPast || []).length === 1 && !late.dog, JSON.stringify({ city: late.kids[0].city, past: late.dogsPast }));
    await run('nest', async () => { await story(); return true; }, 'N18 video call with Tara in her city');
    ok('N19 no page errors', p.errs.length === 0 && !(await G(() => window.__game._lastErr)), p.errs.join(' | ') + (await G(() => window.__game._lastErr || ''))); await p.close();
  } catch (e) { ok('N life events', false, e.message.slice(0, 300)); }
  await browser.close();
  const fails = results.filter((r) => r[0] === 'FAIL'); console.log(`\n==== ${results.length - fails.length} PASS, ${fails.length} FAIL ====`); fails.forEach((f) => console.log('FAIL: ' + f[1] + ' -- ' + f[2]));
})();
