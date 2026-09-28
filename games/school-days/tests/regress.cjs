// Full regression: every feature and fix the operator asked for, in a real browser, with real keys where it matters.
const { chromium } = require('playwright');
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
  try {
    p = await browser.newPage({ viewport: { width: 1280, height: 720 } }); await p.goto('http://localhost:8765/game.html'); await p.evaluate(() => localStorage.clear()); await p.reload();
    const ids = ['av-1p', 'av-2p', 'av-boy', 'av-girl', 'av-p2boy', 'av-p2girl', 'av-p2name', 'new-game', 'av-name', 'av-glasses'];
    const have = await ev(p, (ids) => ids.filter((i) => !document.getElementById(i)), ids); ok('A1 start screen has all buttons', have.length === 0, have.join(','));
    await p.click('#av-1p'); const hid = await ev(p, () => getComputedStyle(document.getElementById('av-p2row')).display); ok('A2 Player 2 choices hidden in 1-player mode', hid === 'none', hid);
    await p.click('#av-2p'); const sh = await ev(p, () => getComputedStyle(document.getElementById('av-p2row')).display); ok('A3 Player 2 choices shown in 2-player mode', sh !== 'none', sh);
    await p.click('#av-girl'); const def = await ev(p, () => document.getElementById('av-p2girl').classList.contains('on')); ok('A4 Player 2 defaults to the same gender as Player 1 (girl -> girl)', def);
    await p.screenshot({ path: 'R_start.png' }); await p.close();
  } catch (e) { ok('A start screen', false, e.message); }

  // ---------- B. Two players: genders, names, keys ----------
  try {
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
    for (const [who, key, want] of [[1, 'ArrowUp', 'up'], [1, 'ArrowDown', 'down'], [1, 'ArrowLeft', 'left'], [1, 'ArrowRight', 'right'], [2, 'w', 'up'], [2, 's', 'down'], [2, 'a', 'left'], [2, 'd', 'right']]) {
      const r = await dirTest(who, key, want); ok(`B-dir Player ${who} ${key} goes ${want} on the screen`, r.dot > 0.9 && r.dist > 0.3 && !r.camTurned, `dot ${r.dot.toFixed(2)}, moved ${r.dist.toFixed(1)}, camera turned ${r.camTurned}`);
    }
    // Holding up for 3 seconds: a straight line, camera still.
    await ev(p, () => { const g = window.__game; g.player.group.position.set(-40, 0, 5); g.player.camYaw = Math.PI / 2; g.player._placeCamera(1); g.p2.group.position.set(-40, 0, 8); }); await p.waitForTimeout(400);
    const path = []; await p.keyboard.down('ArrowUp'); for (let k = 0; k < 6; k++) { await p.waitForTimeout(500); path.push(await ev(p, () => { const a = window.__game.player.position; return [a.x, a.z, window.__game.player.camYaw]; })); } await p.keyboard.up('ArrowUp');
    let maxTurn = 0; for (let k = 2; k < path.length; k++) { const a1 = Math.atan2(path[k - 1][1] - path[k - 2][1], path[k - 1][0] - path[k - 2][0]), a2 = Math.atan2(path[k][1] - path[k - 1][1], path[k][0] - path[k - 1][0]); let d = Math.abs(a2 - a1); if (d > Math.PI) d = 2 * Math.PI - d; maxTurn = Math.max(maxTurn, d); }
    ok('B-straight holding UP walks Player 1 in a straight line', maxTurn < 0.15 && Math.abs(path[5][2] - path[0][2]) < 0.02, `max bend ${(maxTurn * 57.3).toFixed(1)} degrees; path ${JSON.stringify(path.map((q) => q.map((v) => +v.toFixed(2))))}`);
    ok('B6 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-boy'); await q.click('#av-p2girl'); await q.fill('#av-p2name', 'Meera'); } });
    const i2 = await ev(p, () => { const g = window.__game; const tag = g.p2.group.children.find((c) => c.isSprite); return { p1girl: !!g.player.girl, name: g.player.avatar.p2name, dress: g.p2.group.children.some((c) => c.geometry && c.geometry.type === 'CylinderGeometry' && c.geometry.parameters.radiusBottom === 0.4) }; });
    ok('B7 boy + girl named Meera', !i2.p1girl && i2.dress && i2.name === 'Meera', JSON.stringify(i2)); await p.close();
    p = await fresh({ setup: async (q) => { await q.click('#av-2p'); await q.click('#av-boy'); await q.click('#av-p2boy'); } });
    const i3 = await ev(p, () => { const g = window.__game; return { p1girl: !!g.player.girl, dress: g.p2.group.children.some((c) => c.geometry && c.geometry.type === 'CylinderGeometry' && c.geometry.parameters.radiusBottom === 0.4) }; });
    ok('B8 boy + boy: Player 2 is a boy (no sister)', !i3.p1girl && !i3.dress, JSON.stringify(i3)); await p.close();
  } catch (e) { ok('B two players', false, e.message); }

  // ---------- C. One player: W A S D and arrows both move ----------
  try {
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
  try {
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
  try {
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
  try {
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
  try {
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
  try {
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
  try {
    p = await fresh();
    const r = await ev(p, () => { const g = window.__game; if (g.world.currentRoom) g._exitRoom(); g._sim = { kind: 'fly', trip: { dest: 'Sydney', pax: 120, no: 101, leg: 1, stars: [] }, ui: {}, score: 4, max: 5, t: 0 }; g._simArrive(); document.querySelector('#sa-walk').click(); if (g._cut) g._endFlight(); window.__fin(); return { city: g._zone && g._zone.city, lm: g._landmark && g._landmark.userData.name, back: g.interactables.some((i) => i._zone && /cockpit/.test(i.prompt())) }; });
    ok('J1 pilot break: walk Sydney, Opera House in the city, back-to-cockpit spot', r.city === 'Sydney' && !!r.lm && r.back, JSON.stringify(r));
    ok('J2 no page errors', p.errs.length === 0, p.errs.join(' | ')); await p.close();
  } catch (e) { ok('J pilot break', false, e.message); }

  await browser.close();
  const fails = results.filter((r) => r[0] === 'FAIL'); console.log(`\n==== ${results.length - fails.length} PASS, ${fails.length} FAIL ====`); fails.forEach((f) => console.log('FAIL: ' + f[1] + ' -- ' + f[2]));
})();
