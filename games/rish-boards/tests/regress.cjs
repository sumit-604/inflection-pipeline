// Rish Board Games regression. Usage: NODE_PATH=$(npm root -g) node regress.cjs [path/to/index.html]
// Runs the page in Chromium with ?test=1 (no waiting between moves) and checks the rules of all four games.
const { chromium } = require("playwright");
const path = require("path"), fs = require("fs");
const FILE = path.resolve(process.argv[2] || path.join(__dirname, "..", "index.html"));
let pass = 0, fail = 0; const errs = [];
const ok = (name, cond, info = "") => { if (cond) pass++; else fail++; console.log(`${cond ? "PASS" : "FAIL"} ${name}${cond ? "" : " :: " + JSON.stringify(info).slice(0, 600)}`); };

(async () => {
  const b = await chromium.launch({ executablePath: fs.existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : undefined });
  const p = await b.newPage({ viewport: { width: 1200, height: 800 } });
  p.on("pageerror", (e) => errs.push(e.message));
  await p.route(/fonts\.(googleapis|gstatic)\.com/, (r) => r.abort());
  await p.goto("file://" + FILE + "?test=1"); await p.waitForFunction(() => window.__bg, null, { timeout: 30000 });
  const E = (f, a) => p.evaluate(f, a);
  // Seeded random numbers so runs repeat.
  await E(() => { let s = 12345; window.__bg.setRng(() => ((s = (s * 1103515245 + 12345) % 2147483648) / 2147483648)); window.until = async (f, ms = 20000) => { const t = Date.now(); while (!f()) { if (Date.now() - t > ms) return false; await new Promise((r) => setTimeout(r, 2)); } return true; }; });
  let r;

  // ---------------- A. Home ----------------
  r = await E(() => ({ title: document.title, boxes: [...document.querySelectorAll(".box h2")].map((h) => h.textContent), ver: document.getElementById("ver").textContent, credit: document.querySelector(".credit").textContent }));
  ok("A1 home: Rish Board Games with Ludo, Chess, Saanp Seedi, Checkers; version label; credit", r.title === "Rish Board Games" && r.boxes.join() === "Ludo,Chess,Saanp Seedi,Checkers" && r.ver === "Rish Board Games v1" && /Rishabh Sharma/.test(r.credit), r);
  await p.fill("#pname", "Rishabh"); await p.click("#b-about");
  r = await E(() => ({ name: window.__bg.SAVE.name, saved: JSON.parse(localStorage.getItem("rish-boards.v1") || "{}").name, photo: (document.querySelector(".modal img") || {}).src || "", text: document.querySelector(".modal").textContent }));
  ok("A2 your name is saved on this device; About shows the creator's photo and Game 4", r.name === "Rishabh" && r.saved === "Rishabh" && /^data:image/.test(r.photo) && /Game 4/.test(r.text), { ...r, photo: r.photo.slice(0, 20) });
  await p.click("#m-ok");

  // ---------------- C. Chess rules (perft: counts of all legal move sequences, known values) ----------------
  r = await E(() => { const C = window.__bg.CE, P = (fen, d) => C.perft(C.fromFen(fen), d);
    return { s1: P(C.START, 1), s2: P(C.START, 2), s3: P(C.START, 3), k1: P("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1", 1), k2: P("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1", 2),
      p3: P("8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1", 4), p4: P("r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1", 3), p5: P("rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8", 2), fen: C.toFen(C.fromFen(C.START)) }; });
  ok("C1 chess rules match the standard move counts (start 20/400/8902, Kiwipete 48/2039, endgame 43238, promotions 9467, 1486)", r.s1 === 20 && r.s2 === 400 && r.s3 === 8902 && r.k1 === 48 && r.k2 === 2039 && r.p3 === 43238 && r.p4 === 9467 && r.p5 === 1486 && r.fen === "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", r);
  // Two players: tap e2, tap e4, and the scholar's mate.
  r = await E(async () => { const B = window.__bg, C = B.CE; B.Chess.opt = { mode: "2p", level: "medium", side: "w" }; B.Chess.start(); const tap = (s) => document.querySelector(`#cb [data-i="${C.sqi(s)}"]`).click();
    tap("e2"); const dots = document.querySelectorAll("#cb .dot").length; tap("e4"); const o = { dots, e4: B.Chess.G.s.b[C.sqi("e4")], list: document.getElementById("c-moves").textContent };
    for (const [a, c] of [["e7", "e5"], ["f1", "c4"], ["b8", "c6"], ["d1", "h5"], ["g8", "f6"], ["h5", "f7"]]) { tap(a); tap(c); }
    await until(() => document.querySelector(".modal")); o.sans = B.Chess.G.sans.join(" "); o.status = document.getElementById("c-status").textContent; o.modal = document.querySelector(".modal h2").textContent; o.stats = JSON.parse(localStorage.getItem("rish-boards.v1")).played.chess; return o; });
  ok("C2 tap a piece, dots show its moves, tap a dot to move; moves are written down (1. e4)", r.dots === 2 && r.e4 === "P" && /1\. e4/.test(r.list), r);
  ok("C3 scholar's mate ends the game: Checkmate! White wins (moves Qxf7#)", /Qxf7#$/.test(r.sans) && /Checkmate/.test(r.status) && /White wins/.test(r.modal) && r.stats >= 1, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());
  r = await E(async () => { const B = window.__bg, C = B.CE; B.Chess.opt = { mode: "2p", level: "medium", side: "w" }; const tap = (s) => document.querySelector(`#cb [data-i="${C.sqi(s)}"]`).click(); const o = {};
    B.Chess.start("r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1"); tap("e1"); o.castleDots = [...document.querySelectorAll("#cb .dot")].map((d) => C.sqn(+d.parentElement.dataset.i)).filter((s) => s === "g1" || s === "c1").sort().join(); tap("g1"); o.rook = B.Chess.G.s.b[C.sqi("f1")]; o.san = B.Chess.G.sans[0];
    B.Chess.start("4k3/8/8/3pP3/8/8/8/4K3 w - d6 0 1"); tap("e5"); tap("d6"); o.ep = !B.Chess.G.s.b[C.sqi("d5")] && B.Chess.G.s.b[C.sqi("d6")] === "P";
    B.Chess.start("4k3/4r3/8/8/8/8/4B3/4K3 w - - 0 1"); tap("e2"); o.pinned = document.querySelectorAll("#cb .dot, #cb .ring").length;
    B.Chess.start("k7/8/2Q5/8/8/8/8/7K w - - 0 1"); tap("c6"); tap("b6"); await until(() => document.querySelector(".modal")); o.stale = document.querySelector(".modal").textContent;
    document.getElementById("m-home").click(); B.Chess.start("1k6/P7/8/8/8/8/8/7K w - - 0 1"); tap("a7"); tap("a8"); o.picker = document.querySelectorAll(".promo button").length; document.querySelector('.promo [data-t="n"]').click(); o.promo = B.Chess.G.s.b[0]; o.psan = B.Chess.G.sans[0];
    return o; });
  ok("C4 castling (O-O moves the rook), en passant, a pinned piece cannot move", r.castleDots === "c1,g1" && r.rook === "R" && r.san === "O-O" && r.ep && r.pinned === 0, r);
  ok("C5 stalemate is a draw; pawn promotion lets you pick the piece", /Stalemate/.test(r.stale) && r.picker === 4 && r.promo === "N" && r.psan === "a8=N", r);
  r = await E(async () => { const B = window.__bg, C = B.CE; const o = {}; B.Chess.opt = { mode: "cpu", level: "medium", side: "w" }; B.Chess.start(); const tap = (s) => document.querySelector(`#cb [data-i="${C.sqi(s)}"]`).click();
    tap("e2"); tap("e4"); await until(() => B.Chess.G.hist.length === 3); o.reply = B.Chess.G.sans[1]; o.legal = !!o.reply; o.yourTurn = /Your move/.test(document.getElementById("c-status").textContent);
    document.getElementById("c-hint").click(); o.hint = document.querySelectorAll("#cb .hint").length; o.toast = document.getElementById("toast").textContent;
    document.getElementById("c-undo").click(); o.undo = B.Chess.G.hist.length; o.fen = C.toFen(B.Chess.G.s);
    const mate = C.best(C.fromFen("6k1/5ppp/8/8/8/8/5PPP/R5K1 w - - 0 1"), 2); o.mate = C.san(C.fromFen("6k1/5ppp/8/8/8/8/5PPP/R5K1 w - - 0 1"), mate);
    const t0 = performance.now(); C.best(C.fromFen(C.START), 3); o.hardMs = Math.round(performance.now() - t0);
    B.Chess.opt.side = "b"; B.Chess.start(); await until(() => B.Chess.G.hist.length === 2); o.cpuWhite = B.Chess.G.sans[0]; o.flipped = B.Chess.G.flip; return o; });
  ok("C6 against the computer: it answers your move; 💡 Hint shows a good move; Undo goes back to your turn", r.legal && r.yourTurn && r.hint === 2 && /Try/.test(r.toast) && r.undo === 1 && /^rnbqkbnr\/pppppppp\/8\/8\/8\/8\/PPPPPPPP\/RNBQKBNR w/.test(r.fen), r);
  ok("C7 the computer finds checkmate (Ra8#), thinks fast on Hard, and moves first when you play Black (board flipped)", r.mate === "Ra8#" && r.hardMs < 8000 && !!r.cpuWhite && r.flipped, r);

  // ---------------- L. Ludo ----------------
  r = await E(async () => { const B = window.__bg, L = B.Ludo; const o = {}; L.start(["human", "off", "cpu", "off"]); const G = () => L.G;
    o.cells = window.__bg.LD.T.length; o.toks = document.querySelectorAll("#l-toks .tok").length; o.safe = [...window.__bg.LD.SAFE].length;
    G().force = [3]; document.getElementById("l-dice").click(); await until(() => G().turn === 1); o.passed = G().turn === 1;
    await until(() => G().turn === 0 && !G().busy && !G().rolled, 20000); // the computer plays its turn(s)
    G().force = [6]; document.getElementById("l-dice").click(); await until(() => G().movable.length); o.mov6 = G().movable.length; document.querySelector('#l-toks .tok.can[data-c="0"][data-k="2"]').dispatchEvent(new MouseEvent("click", { bubbles: true })); await until(() => !G().busy && G().players[0].tok[2] === 0);
    o.out = G().players[0].tok[2]; o.again = G().turn === 0 && !G().rolled; return o; });
  ok("L1 Ludo board: 52 track squares, 8 safe squares, 4 tokens each; no 6 with all at home = the turn passes", r.cells === 52 && r.safe === 8 && r.toks === 8 && r.passed, r);
  ok("L2 a 6 lets any token come out; tap the glowing token; a 6 gives another roll", r.mov6 === 4 && r.out === 0 && r.again, r);
  r = await E(async () => { const B = window.__bg, L = B.Ludo, LD = B.LD; const o = {}; L.start(["human", "off", "cpu", "off"]); const G = () => L.G, red = G().players[0], yel = G().players[1];
    const yr = (a) => (a - LD.COLORS[2].off + 52) % 52;
    red.tok = [7, -1, -1, -1]; yel.tok = [yr(10), -1, -1, -1]; G().force = [3]; document.getElementById("l-dice").click(); await until(() => !G().busy && red.tok[0] === 10);
    o.cut = yel.tok[0]; o.bonus = G().turn === 0 && !G().rolled;
    red.tok = [5, -1, -1, -1]; yel.tok = [yr(8), -1, -1, -1]; G().force = [3]; document.getElementById("l-dice").click(); await until(() => !G().busy && red.tok[0] === 8); await until(() => G().turn === 1 || G().turn === 0);
    o.safe = yel.tok[0] === yr(8);
    G().turn = 0; G().rolled = false; G().busy = false; red.tok = [54, -1, -1, -1]; G().force = [3]; G().log = []; document.getElementById("l-dice").click(); await until(() => G().rolled && !G().movable.length); o.exactNo = red.tok[0] === 54;
    await until(() => G().turn === 1); return o; });
  ok("L3 landing on another colour cuts it (back home) and gives another roll; a ★ safe square protects; home needs the exact number", r.cut === -1 && r.bonus && r.safe && r.exactNo, r);
  r = await E(async () => { const B = window.__bg, L = B.Ludo; const o = {}; L.start(["human", "off", "cpu", "off"]); const G = () => L.G, red = G().players[0];
    red.tok = [0, -1, -1, -1]; G().force = [6, 6, 6]; for (let i = 0; i < 2; i++) { document.getElementById("l-dice").click(); await until(() => G().movable.length); document.querySelector('#l-toks .tok.can[data-c="0"][data-k="0"]').dispatchEvent(new MouseEvent("click", { bubbles: true })); await until(() => !G().busy && !G().rolled); }
    document.getElementById("l-dice").click(); await until(() => G().turn === 1); o.three = /Three 6s/.test(document.getElementById("toast").textContent);
    L.start(["human", "off", "cpu", "off"]); const r2 = L.G.players[0]; r2.tok = [56, 56, 56, 53]; L.G.force = [3]; document.getElementById("l-dice").click(); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; o.rank = r2.rank; document.getElementById("m-home").click(); return o; });
  ok("L4 three 6s in a row lose the turn; taking all 4 tokens home wins (1st place)", r.three && /wins/.test(r.win) && r.rank === 1, r);
  r = await E(async () => { const B = window.__bg, L = B.Ludo; L.start(["cpu", "cpu", "cpu", "cpu"]); const done = await until(() => L.G.over, 120000); await until(() => document.querySelector(".modal"), 5000); return { done, ranks: L.G.ranks.length, cuts: L.G.log.filter((x) => x[0] === "cut").length, modal: !!document.querySelector(".modal") }; });
  ok("L5 four computer players play a whole game to the end: 1st, 2nd, 3rd, 4th (with cuts)", r.done && r.ranks === 4 && r.modal && r.cuts >= 1, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());

  // ---------------- S. Saanp Seedi ----------------
  r = await E(async () => { const B = window.__bg, S = B.Snakes; const o = {}; S.start(["human", "cpu", "off", "off"]); const G = () => S.G, me = G().players[0];
    G().force = [3]; document.getElementById("s-dice").click(); await until(() => G().turn === 1); o.first = me.pos; await until(() => G().turn === 0 && !G().busy);
    me.pos = 1; G().force = [3]; document.getElementById("s-dice").click(); await until(() => G().turn === 1); o.ladder = me.pos; await until(() => G().turn === 0 && !G().busy);
    me.pos = 14; G().force = [3]; document.getElementById("s-dice").click(); await until(() => G().turn === 1); o.snake = me.pos; await until(() => G().turn === 0 && !G().busy);
    me.pos = 98; G().force = [5]; document.getElementById("s-dice").click(); await until(() => G().turn === 1); o.exact = me.pos; await until(() => G().turn === 0 && !G().busy);
    me.pos = 10; G().force = [6]; document.getElementById("s-dice").click(); await until(() => !G().busy && me.pos === 16); o.six = G().turn === 0;
    G().force = [1]; await until(() => !G().busy); me.pos = 97; G().force = [3]; document.getElementById("s-dice").click(); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; o.svg = document.querySelectorAll("#sb rect").length; document.getElementById("m-home").click(); return o; });
  ok("S1 Saanp Seedi: move by the dice; ladder 4 → 14; snake 17 → 7; 100 needs the exact number; a 6 rolls again; reaching 100 wins", r.first === 3 && r.ladder === 14 && r.snake === 7 && r.exact === 98 && r.six && /wins/.test(r.win) && r.svg === 100, r);
  r = await E(async () => { const S = window.__bg.Snakes; S.start(["cpu", "cpu", "cpu", "cpu"]); const done = await until(() => S.G.over, 120000); return { done, ladders: S.G.log.filter((x) => x[0] === "ladder").length, snakes: S.G.log.filter((x) => x[0] === "snake").length }; });
  ok("S2 four computer players play Saanp Seedi to the end (ladders and snakes happen)", r.done && r.ladders >= 1 && r.snakes >= 1, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());

  // ---------------- K. Checkers ----------------
  r = await E(async () => { const B = window.__bg, K = B.CK, CH = B.Checkers; const o = {}; o.start = K.moves(K.start(), "r").length; o.count = K.start().filter(Boolean).length;
    const emp = () => Array(64).fill(null); let b = emp(); b[42] = "r"; b[35] = "b"; b[46] = "r"; o.forced = K.moves(b, "r").map((m) => m.path.join("-")).join();
    CH.opt = { mode: "2p", level: "medium" }; CH.start(b, "r"); const tap = (i) => document.querySelector(`#kb [data-i="${i}"]`).click(); tap(46); o.mustToast = (document.getElementById("toast") || {}).textContent || ""; tap(42); tap(28); o.took = !CH.G.b[35] && CH.G.b[28] === "r";
    b = emp(); b[49] = "r"; b[42] = "b"; b[28] = "b"; b[1] = "b"; CH.start(b, "r"); tap(49); tap(35); o.mid = CH.G.b[49] === "r" && CH.G.step === 1; tap(21); o.multi = CH.G.b[21] === "r" && !CH.G.b[42] && !CH.G.b[28];
    b = emp(); b[10] = "r"; b[63] = "b"; CH.start(b, "r"); tap(10); tap(1); o.king = CH.G.b[1];
    b = emp(); b[42] = "r"; b[35] = "b"; CH.start(b, "r"); tap(42); tap(28); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; document.getElementById("m-home").click(); return o; });
  ok("K1 checkers: 12 pieces each, 7 opening moves; a jump is a must; jumps take the piece", r.count === 24 && r.start === 7 && r.forced === "42-28" && /must jump/.test(r.mustToast) && r.took, r);
  ok("K2 a double jump goes on step by step; the far row makes a king; no pieces left = a win", r.mid && r.multi && r.king === "R" && /wins/.test(r.win), r);
  r = await E(async () => { const B = window.__bg, K = B.CK, CH = B.Checkers; const o = {}; CH.opt = { mode: "cpu", level: "medium" }; CH.start(); const tap = (i) => document.querySelector(`#kb [data-i="${i}"]`).click();
    const m = K.moves(CH.G.b, "r")[0]; tap(m.path[0]); tap(m.path[1]); await until(() => CH.G.turn === "r" && !CH.G.thinking); o.replied = CH.G.hist.length === 2; document.getElementById("k-undo").click(); o.undo = CH.G.hist.length === 0 && CH.G.turn === "r";
    let b = K.start(), turn = "r", plies = 0, end = ""; while (plies < 300) { const ms = K.moves(b, turn); if (!ms.length) { end = turn + " lost"; break; } const mv = K.best(b, turn, 2, 30); b = K.apply(b, mv); turn = turn === "r" ? "b" : "r"; plies++; } o.selfplay = end || "draw by length"; o.plies = plies; return o; });
  ok("K3 the computer answers your move; Undo goes back to your turn; computer vs computer games finish", r.replied && r.undo && /lost|draw/.test(r.selfplay), r);

  // ---------------- P. Phone ----------------
  const q = await b.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  q.on("pageerror", (e) => errs.push("phone: " + e.message)); await q.route(/fonts\.(googleapis|gstatic)\.com/, (rt) => rt.abort());
  await q.goto("file://" + FILE + "?test=1"); await q.waitForFunction(() => window.__bg, null, { timeout: 30000 });
  const fits = () => q.evaluate(() => ({ sw: document.documentElement.scrollWidth, w: innerWidth }));
  const out = {}; out.home = await fits();
  await q.evaluate(() => { window.__bg.Chess.opt = { mode: "2p", level: "easy", side: "w" }; window.__bg.Chess.start(); }); out.chess = await fits(); out.cb = await q.evaluate(() => document.getElementById("cb").getBoundingClientRect().width);
  await q.evaluate(() => window.__bg.Ludo.start(["human", "cpu", "cpu", "cpu"])); out.ludo = await fits(); out.lb = await q.evaluate(() => document.getElementById("lb").getBoundingClientRect().width);
  ok("P1 phone width 390: no sideways scrolling; the chess and Ludo boards fill the width", [out.home, out.chess, out.ludo].every((x) => x.sw <= x.w) && out.cb > 320 && out.lb > 320, out);
  await q.close();

  ok("Z1 no page errors", errs.length === 0, errs);
  console.log(`\n${pass} passed, ${fail} failed`);
  await b.close(); process.exit(fail ? 1 : 0);
})();
