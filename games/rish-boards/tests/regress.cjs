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
  ok("A1 home: Rish Board Games with 15 games; version label; credit", r.title === "Rish Board Games" && r.boxes.join() === "Ludo,Chess,Carrom,Rish Business,Saanp Seedi,Checkers,Chaar Line,Reversi,Kaata Zero,Dots and Boxes,Navakankari,Bagh Bakri,Mancala,Navy Battle,Panch Line" && r.ver === "Rish Board Games v3" && /Rishabh Sharma/.test(r.credit), r);
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

  // ---------------- N. New games (v2) ----------------
  r = await E(async () => { const B = window.__bg, T = B.TTT; const o = {}; let xWins = 0, games = 0;
    for (let g = 0; g < 40; g++) { const b = Array(9).fill(null); let turn = "X", w = null; while (!(w = T.winner(b))) { const free = b.map((v, i) => (v ? -1 : i)).filter((i) => i >= 0); const i = turn === "X" ? free[Math.floor(Math.random() * free.length)] : T.cpuMove(b.slice(), "hard"); b[i] = turn; turn = turn === "X" ? "O" : "X"; } games++; if (w.p === "X") xWins++; }
    o.xWins = xWins; o.games = games;
    T.opt = { mode: "2p", level: "hard" }; T.start(); const tap = (i) => document.querySelector(`#tb [data-i="${i}"]`).click(); for (const i of [0, 3, 1, 4, 2]) { tap(i); await until(() => true); } await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; o.line = document.querySelectorAll("#tb .tc.win").length; document.getElementById("m-home").click();
    T.opt = { mode: "cpu", level: "hard" }; T.start(); tap(4); await until(() => T.G.b.filter(Boolean).length === 2); o.reply = T.G.b.filter(Boolean).length; return o; });
  ok("N1 Kaata Zero: 3 in a row wins (the line lights up); the Hard computer never loses (40 games vs random moves); it answers your move", r.xWins === 0 && r.games === 40 && /wins/.test(r.win) && r.line === 3 && r.reply === 2, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());
  r = await E(async () => { const B = window.__bg, C = B.C4; const o = {}; const e = () => Array(42).fill(null);
    let b = e(); for (const c of [0, 1, 2]) C.drop(b, c, "R"); o.block = C.best(b, "Y", 4); b = e(); for (const c of [0, 1, 2]) C.drop(b, c, "Y"); C.drop(b, 6, "R"); o.take = C.best(b, "Y", 4);
    b = e(); for (let k = 0; k < 4; k++) C.drop(b, 2, "R"); o.vert = (C.win(b) || {}).p; b = e(); [[0, "R"], [1, "Y"], [1, "R"], [2, "Y"], [2, "Y"], [2, "R"], [3, "Y"], [3, "Y"], [3, "Y"], [3, "R"]].forEach(([c, p]) => C.drop(b, c, p)); o.diag = (C.win(b) || {}).p;
    C.opt = { mode: "2p", level: "medium" }; C.start(); const tap = (c) => document.querySelector(`#c4b [data-c="${c}"]`).click(); tap(3); o.bottom = C.G.b[38]; o.drop = !!document.querySelector("#c4b .c4d.drop");
    for (const c of [4, 3, 4, 3, 4, 3]) tap(c); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; o.cells = document.querySelectorAll("#c4b .c4d.win").length; document.getElementById("m-home").click();
    C.opt = { mode: "cpu", level: "hard" }; C.start(); tap(3); await until(() => C.G.b.filter(Boolean).length === 2, 20000); o.reply = C.G.b.filter(Boolean).length; return o; });
  ok("N2 Chaar Line: discs fall to the bottom; 4 down or slanting wins; the computer blocks your 3 and takes its own 4; it answers on Hard", r.block === 3 && r.take === 3 && r.vert === "R" && r.diag === "R" && r.bottom === "R" && r.drop && /Red wins/.test(r.win) && r.cells === 4 && r.reply === 2, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());
  r = await E(async () => { const B = window.__bg, R = B.RV; const o = {}; R.opt = { mode: "2p", level: "medium" }; R.start(); o.start = R.moves(R.G.b, "B").map((m) => m.i).sort((a, c) => a - c).join();
    document.querySelector('#rvb [data-i="19"]').click(); o.flip = R.G.b[27] === "B" && R.G.b.filter((x) => x === "B").length === 4 && R.G.turn === "W";
    let b = Array(64).fill(null); b[0] = "B"; b[1] = "W"; b[63] = "W"; R.start(b, "W"); o.passBoard = R.moves(R.G.b, "W").length;
    b = Array(64).fill(null); b[0] = "B"; b[1] = "W"; R.start(b, "B"); document.querySelector('#rvb [data-i="2"]').click(); await until(() => document.querySelector(".modal")); o.end = document.querySelector(".modal").textContent; document.getElementById("m-home").click();
    let bb = Array(64).fill(null); bb[27] = bb[36] = "W"; bb[28] = bb[35] = "B"; let turn = "B", n = 0; while (n < 80) { const ms = R.moves(bb, turn), op = turn === "B" ? "W" : "B"; if (!ms.length) { if (!R.moves(bb, op).length) break; turn = op; continue; } bb = R.apply(bb, R.best(bb, turn, 2, 10), turn); turn = op; n++; } o.selfplay = bb.filter(Boolean).length; return o; });
  ok("N3 Reversi: 4 opening moves; a move flips the trapped disc; no move left for both = the game ends with the count; computer games fill the board", r.start === "19,26,37,44" && r.flip && /wins 3-0|Black wins/.test(r.end) && r.selfplay >= 50, r);
  r = await E(async () => { const B = window.__bg, D = B.DB; const o = {}; o.lines = D.all().length; let L = {}; L["h0-0"] = L["v0-0"] = L["v0-1"] = "A"; o.take = D.cpuLine(L, "medium"); L = { "h0-0": "A", "v0-0": "A" }; const pick = D.cpuLine(L, "medium"); o.safe = !["h1-0", "v0-1"].includes(pick);
    D.opt = { mode: "2p", level: "medium" }; D.start(); const click = (k) => document.querySelector(`#db .ln[data-k="${k}"]`).dispatchEvent(new MouseEvent("click", { bubbles: true }));
    click("h0-0"); click("v0-0"); click("v0-1"); o.turnB = D.G.turn === "B"; click("h1-0"); o.box = D.G.owner["0-0"] === "B" && D.G.score.B === 1 && D.G.turn === "B";
    let LL = {}, turn = "A", sc = { A: 0, B: 0 }; while (Object.keys(LL).length < 40) { const k = D.cpuLine(LL, "hard"); LL[k] = turn; let got = 0; for (const [r, c] of D.boxesOf(k)) if (D.sides(LL, r, c) === 4) got++; sc[turn] += got; if (!got) turn = turn === "A" ? "B" : "A"; } o.total = sc.A + sc.B; return o; });
  ok("N4 Dots and Boxes: 40 lines; the 4th side wins the box and another turn; the computer takes free boxes and avoids giving them away; a full game shares out all 16 boxes", r.lines === 40 && r.take === "h1-0" && r.safe && r.turnB && r.box && r.total === 16, r);
  r = await E(async () => { const B = window.__bg, CR = B.CR, K = B.Carrom; const o = {}; const rk = CR.rack(); o.rack = [rk.filter((d) => d.c === "w").length, rk.filter((d) => d.c === "b").length, rk.filter((d) => d.c === "q").length].join();
    let overlap = 0; for (let i = 0; i < rk.length; i++) for (let j = i + 1; j < rk.length; j++) if (Math.hypot(rk[i].x - rk[j].x, rk[i].y - rk[j].y) < rk[i].r + rk[j].r) overlap++; o.overlap = overlap;
    const coin = [{ id: "w0", c: "w", x: 300, y: 300, vx: 0, vy: 0, r: 19, m: 1 }]; const P = CR.PK[0], ux = 300 - P[0], uy = 300 - P[1], ul = Math.hypot(ux, uy), gx = 300 + ux / ul * 44, gy = 300 + uy / ul * 44;
    const sx = 500, sy = CR.BASE.b.y; o.pot = CR.simulate(coin, sx, sy, Math.atan2(gy - sy, gx - sx), 0.8).pocketed.map((d) => d.c).join(); o.foul = CR.simulate([], 230, sy, Math.atan2(CR.PK[2][1] - sy, CR.PK[2][0] - 230), 0.6).pocketed.map((d) => d.c).join();
    // Rules, two players. Put a coin right in front of a pocket and shoot at it.
    K.opt = { mode: "2p", level: "medium" }; K.start(); const G = () => K.G; const only = (list) => { G().coins.forEach((d) => (d.gone = true)); list.forEach(([id, x, y]) => { const d = G().coins.find((q) => q.id === id); d.gone = false; d.x = x; d.y = y; d.vx = d.vy = 0; }); };
    const potShot = (x, y) => { const pr = CR.PK[0], a = x - pr[0], b2 = y - pr[1], l = Math.hypot(a, b2), gx2 = x + a / l * 44, gy2 = y + b2 / l * 44, B2 = CR.BASE[K.side()]; G().sx = 500; K.shoot(Math.atan2(gy2 - B2.y, gx2 - 500), 0.85); };
    const wid = G().coins.filter((d) => d.c === "w").map((d) => d.id), bid = G().coins.filter((d) => d.c === "b").map((d) => d.id);
    only([[wid[0], 300, 300], [wid[1], 700, 450], [bid[0], 650, 300], ["q", 500, 500]]); potShot(300, 300); o.own = G().pk.w === 1 && G().turn === "w";
    G().sx = 230; K.shoot(Math.atan2(CR.PK[2][1] - CR.BASE.b.y, CR.PK[2][0] - 230), 0.6); o.foulRule = G().pk.w === 0 && G().turn === "b" && /Foul/.test(G().msg) && G().coins.filter((d) => d.c === "w" && !d.gone).length === 2;
    G().turn = "w"; only([["q", 300, 300], [wid[0], 700, 450], [wid[1], 640, 520], [bid[0], 650, 300]]); potShot(300, 300); o.pending = G().pending === "w" && G().turn === "w" && /cover/.test(G().msg);
    only([[wid[0], 300, 300], [wid[1], 700, 450], [bid[0], 650, 300]]); G().coins.find((d) => d.c === "q").gone = true; potShot(300, 300); o.covered = G().queen === "w" && G().turn === "w";
    G().queen = null; G().pending = null; G().turn = "w"; only([["q", 300, 300], [wid[0], 700, 450], [bid[0], 650, 300]]); potShot(300, 300); G().sx = 500; K.shoot(Math.PI / 2 * -1, 0.05); o.notCovered = !G().coins.find((d) => d.c === "q").gone && G().pending === null && G().turn === "b";
    G().turn = "w"; G().queen = "w"; G().pk.w = 8; only([[wid[0], 300, 300], [bid[0], 650, 300]]); potShot(300, 300); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal").textContent; document.getElementById("m-home").click();
    K.opt = { mode: "2p", level: "medium" }; K.start(); const c = document.getElementById("crc"); o.sharp = c.width === Math.round(c.clientWidth * Math.min(3, devicePixelRatio || 1)) && c.width > 0;
    let shots = 0; const t0 = performance.now(); while (!K.G.over && shots < 400) { const s = K.cpuShot(); K.G.sx = s.x; K.shoot(s.dir, s.power); shots++; } o.aiShots = shots; o.aiOver = !!K.G.over; o.pocketed = K.G.pk.w + K.G.pk.b; o.ms = Math.round(performance.now() - t0); return o; });
  ok("N5 Carrom: 9 white, 9 black and the red queen with no overlap; a straight shot pockets a coin; the striker in a pocket is a foul", r.rack === "9,9,1" && r.overlap === 0 && r.pot === "w" && r.foul === "s", r);
  ok("N6 Carrom rules: your coin in = shoot again; foul = a coin comes back and the turn passes; the queen needs a cover; last coin + covered queen wins", r.own && r.foulRule && r.pending && r.covered && r.notCovered && /wins/.test(r.win), r);
  ok("N7 Carrom: the board is drawn at the screen's full sharpness; the computer players finish a whole game", r.sharp && r.aiOver && r.pocketed >= 9, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());

  // ---------------- G. More games (v3) ----------------
  r = await E(async () => { const B = window.__bg, GM = B.GM; const o = {}; const N = 15, e = () => Array(N * N).fill(null);
    let b = e(); for (let c = 3; c < 8; c++) b[7 * N + c] = "B"; o.five = (GM.five(b, 7 * N + 5) || []).length; b = e(); for (let c = 3; c < 7; c++) b[7 * N + c] = "B"; o.block = [7 * N + 2, 7 * N + 7].includes(GM.best(b, "W")); b = e(); for (let c = 3; c < 7; c++) b[5 * N + c] = "W"; b[7 * N + 3] = b[7 * N + 4] = b[7 * N + 5] = "B"; o.win = [5 * N + 2, 5 * N + 7].includes(GM.best(b, "W"));
    GM.opt = { mode: "2p", level: "medium" }; GM.start(); const tap = (i) => document.querySelector(`#gmb .gpt[data-i="${i}"]`).dispatchEvent(new MouseEvent("click", { bubbles: true }));
    for (const i of [112, 0, 113, 1, 114, 2, 115, 3, 116]) tap(i); await until(() => document.querySelector(".modal")); o.modal = document.querySelector(".modal h2").textContent; document.getElementById("m-home").click();
    GM.opt = { mode: "cpu", level: "hard" }; GM.start(); tap(112); await until(() => GM.G.b.filter(Boolean).length === 2); o.reply = GM.G.b.filter(Boolean).length; return o; });
  ok("G1 Panch Line: 5 in a row wins (across); the computer blocks your 4 and finishes its own 4; it answers your move", r.five === 5 && r.block && r.win && /Black wins/.test(r.modal) && r.reply === 2, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());
  r = await E(async () => { const B = window.__bg, NM = B.NM; const o = {}; NM.opt = { mode: "2p", level: "medium" }; NM.start(); const tap = (i) => document.querySelector(`#nmb .npt[data-i="${i}"]`).dispatchEvent(new MouseEvent("click", { bubbles: true }));
    o.first = NM.moves(NM.G.s).length; tap(0); tap(9); tap(1); tap(21); tap(2); o.mill = !!NM.G.pend && document.getElementById("nm-status").textContent.includes("Mill"); tap(9); o.took = NM.G.s.b[9] === null && NM.G.s.b[21] === "K" && NM.G.s.turn === "K";
    const st = { b: Array(24).fill(null), turn: "R", hand: { R: 0, K: 0 }, quiet: 0 }; st.b[0] = st.b[1] = st.b[22] = "R"; st.b[9] = st.b[10] = st.b[11] = "K"; st.b[23] = "K"; o.fly = NM.moves(st).some((m) => m.from === 22 && m.to === 2);
    const s2 = { b: Array(24).fill(null), turn: "R", hand: { R: 0, K: 0 }, quiet: 0 }; s2.b[0] = s2.b[1] = s2.b[3] = s2.b[14] = "R"; s2.b[9] = s2.b[10] = s2.b[22] = "K"; NM.start(s2); tap(14); tap(2); o.lost = !!NM.G.pend || NM.G.over; if (NM.G.pend) tap(22); await until(() => document.querySelector(".modal"), 3000); o.modal = (document.querySelector(".modal h2") || {}).textContent || ""; if (document.getElementById("m-home")) document.getElementById("m-home").click();
    let s = { b: Array(24).fill(null), turn: "R", hand: { R: 9, K: 9 }, quiet: 0 }, n = 0; while (!NM.lost(s) && s.quiet <= 100 && n < 400) { s = NM.apply(s, NM.best(s, 2, 30)); n++; } o.selfplay = n; o.ended = NM.lost(s) || s.quiet > 100 || n >= 400; return o; });
  ok("G2 Navakankari: 24 points to place on; a mill lets you tap a piece to take; 3 pieces left can fly; under 3 pieces loses; computer games run", r.first === 24 && r.mill && r.took && r.fly && /wins/.test(r.modal) && r.ended, r);
  r = await E(async () => { const B = window.__bg, BG = B.BG; const o = {}; const s0 = BG.init(); o.goats = BG.moves(s0).length; o.tigerStart = BG.moves(Object.assign({}, s0, { turn: "T" })).length;
    let s = BG.init(); s.b[1] = "G"; s.turn = "T"; o.jump = BG.moves(s).some((m) => m.from === 0 && m.to === 2 && m.cap === 1);
    s = { b: Array(25).fill(null), turn: "T", left: 0, eaten: 0, quiet: 0 }; s.b[0] = "T"; for (const i of [1, 2, 5, 10, 6, 12]) s.b[i] = "G"; o.trapped = BG.result(s) === "G";
    BG.opt = { mode: "2p", level: "medium", side: "goat" }; BG.start(); const tap = (i) => document.querySelector(`#bgb .bpt[data-i="${i}"]`).dispatchEvent(new MouseEvent("click", { bubbles: true })); tap(1); tap(0); tap(2); o.ate = BG.G.s.eaten === 1 && BG.G.s.b[1] === null && BG.G.s.b[2] === "T";
    BG.opt = { mode: "cpu", level: "medium", side: "goat" }; BG.start(); tap(12); await until(() => BG.G.s.turn === "G"); o.cpuTiger = BG.G.s.b.filter((x) => x === "T").length === 4;
    BG.opt = { mode: "cpu", level: "medium", side: "tiger" }; BG.start(); await until(() => BG.G.s.turn === "T"); o.cpuGoat = BG.G.s.left === 19;
    let t = BG.init(), n = 0; while (!BG.result(t) && n < 300) { t = BG.apply(t, BG.best(t, 2, 10)); n++; } o.end = BG.result(t) || "running"; return o; });
  ok("G3 Bagh Bakri: 25 points for the first goat; tigers start at 4 corners; a tiger jumps a goat to eat it; a trapped tiger loses; the computer plays tigers or goats", r.goats === 21 && r.tigerStart > 0 && r.jump && r.trapped && r.ate && r.cpuTiger && r.cpuGoat && r.end !== "running", r);
  r = await E(async () => { const B = window.__bg, MC = B.MC; const o = {}; const s = MC.init(); let x = MC.sow(s, 2); o.again = x.again && x.s.b[6] === 1 && x.s.turn === 0; x = MC.sow(s, 0); o.normal = !x.again && x.s.turn === 1 && x.s.b[1] === 5;
    const c = { b: [0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0], turn: 0 }; c.b[12] = 0; c.b[7] = 3; const before = c.b[8]; x = MC.sow({ b: [0, 0, 1, 0, 0, 0, 0, 2, 3, 4, 0, 0, 0, 0], turn: 0 }, 2); o.cap = x.cap === 5 && x.s.b[6] === 5 && x.s.b[9] === 0;
    MC.opt = { mode: "2p", level: "medium" }; MC.start(); document.querySelector('#mcb .mpit[data-i="2"]').click(); o.ui = MC.G.s.b[6] === 1 && /again/.test(document.getElementById("mc-msg").textContent);
    let g = MC.init(), n = 0, over = false; while (!over && n < 300) { const r2 = MC.sow(g, MC.best(g, 3, 2)); g = r2.s; over = r2.over; n++; } o.total = g.b[6] + g.b[13]; o.over = over;
    MC.opt = { mode: "cpu", level: "hard" }; MC.start(); document.querySelector('#mcb .mpit[data-i="0"]').click(); await until(() => MC.G.s.turn === 0 && !MC.G.busy, 10000); o.cpu = MC.G.s.b.slice(7, 13).some((v) => v !== 4) || MC.G.s.b[13] > 0; return o; });
  ok("G4 Mancala: last seed in your store = play again; seeds go round; an empty pit captures the seeds across; a full game keeps all 48 seeds; the computer plays", r.again && r.normal && r.cap && r.ui && r.over && r.total === 48 && r.cpu, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());
  r = await E(async () => { const B = window.__bg, BS = B.BS; const o = {}; const f = BS.place(); o.cells = f.used.size; o.ships = f.ships.map((s) => s.cells.length).join();
    BS.opt = { mode: "cpu", level: "hard" }; BS.start(); const G = () => BS.G; const target = [...G().cpu.used.keys()][0]; document.querySelector(`#bs-enemy [data-i="${target}"]`).click(); o.hit = G().myShots[target] === "hit"; o.locked = document.getElementById("bs-shuffle").disabled;
    await until(() => G().turn === "me"); o.cpuShots = Object.keys(G().cpuShots).length;
    // Hunt mode: after a hit, the next shots go next to it.
    G().cpuShots = {}; G().hunt = []; const ship = G().me.ships[0]; G().me.ships.forEach((s) => (s.hits = 0)); G().turn = "cpu"; const first = ship.cells[2]; BS.shot(G().me, G().cpuShots, first); const row = Math.floor(first / 10), col = first % 10; G().hunt = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]].filter(([a, b]) => a >= 0 && a < 10 && b >= 0 && b < 10).map(([a, b]) => a * 10 + b); const nxt = BS.cpuPick(); o.hunt = Math.abs(nxt - first) === 1 || Math.abs(nxt - first) === 10;
    BS.start(); for (const i of [...G().cpu.used.keys()]) { if (G().over) break; await until(() => G().turn === "me" || G().over); if (G().over) break; G().turn = "me"; document.querySelector(`#bs-enemy [data-i="${i}"]`).click(); }
    await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; document.getElementById("m-home").click(); return o; });
  ok("G5 Navy Battle: 5 ships (5, 4, 3, 3, 2) on 17 squares; a shot on a ship is a hit; the computer fires back and hunts round a hit; sinking every ship wins", r.cells === 17 && r.ships === "5,4,3,3,2" && r.hit && r.locked && r.cpuShots === 1 && r.hunt && /win/.test(r.win), r);
  r = await E(async () => { const B = window.__bg, BZ = B.BZ, Z = B.Business; const o = {}; o.squares = BZ.SQ.length; o.groups = new Set(BZ.SQ.filter((s) => s.t === "city").map((s) => s.g)).size;
    Z.start(["human", "human", "off", "off"]); const G = () => Z.G, p0 = G().players[0], p1 = G().players[1]; const click = (id) => document.getElementById(id).click();
    G().force = [[2, 1]]; click("bz-roll"); await until(() => G().phase === "buy"); click("bz-buy"); o.bought = G().own[3] === 0 && p0.cash === 1420; click("bz-end");
    G().force = [[1, 2]]; click("bz-roll"); await until(() => G().phase === "end"); o.rent = p1.cash === 1500 - 8 && p0.cash === 1428; click("bz-end");
    G().own[1] = 0; G().force = [[3, 1]]; click("bz-roll"); await until(() => G().phase === "buy" || G().phase === "end"); if (G().phase === "buy") click("bz-skip"); o.buildBtn = !!document.getElementById("bz-build"); Z.build(1); o.house = G().houses[1] === 1 && p0.cash === 1428 - 30; click("bz-end");
    p1.pos = 0; G().force = [[1, 0]]; G().force[0] = [1, 2]; p1.pos = 25; G().force = [[1, 2]]; click("bz-roll"); await until(() => G().phase === "end" || G().phase === "buy"); o.passStart = p1.pos === 0 && p1.cash >= 1492 + 200 - 0; if (G().phase === "buy") click("bz-skip"); click("bz-end");
    p0.pos = 18; G().force = [[1, 2]]; click("bz-roll"); await until(() => G().phase === "end"); o.jail = p0.pos === 7 && p0.jail === 1; click("bz-end");
    click("bz-end" in {} ? "x" : "bz-roll"); await until(() => G().phase !== "roll" || G().turn === 0); 
    if (G().turn === 1 && G().phase === "end") click("bz-end"); else if (G().phase === "buy") { click("bz-skip"); click("bz-end"); }
    await until(() => G().turn === 0); o.bail = !!document.getElementById("bz-bail"); click("bz-bail"); o.bailed = p0.jail === 0;
    G().forceCard = [6]; p0.pos = 0; G().force = [[1, 1]]; const c1 = p1.cash; click("bz-roll"); await until(() => G().phase !== "roll" || G().busy === false); o.card = p0.pos === 2 && p1.cash === c1 - 20;
    // Bankrupt: the other player cannot pay a big rent.
    p1.cash = 5; for (const k of Object.keys(G().own)) if (G().own[k] === 1) delete G().own[k]; Z.pay(p1, 500, p0); o.out = p1.out; await until(() => document.querySelector(".modal") || Z.checkEnd()); await until(() => document.querySelector(".modal")); o.win = document.querySelector(".modal h2").textContent; document.getElementById("m-home").click();
    Z.rounds = 8; Z.start(["cpu", "cpu", "cpu", "cpu"]); const done = await until(() => Z.G.over, 60000); await until(() => document.querySelector(".modal"), 5000); o.cpuGame = done && /wins/.test((document.querySelector(".modal h2") || {}).textContent || ""); o.cpuBought = Object.keys(Z.G.own).length; o.rounds = Z.G.round; Z.rounds = 25; return o; });
  ok("G6 Rish Business: 28 squares, 6 colour groups; buy a city; pay rent to its owner; build a house on a full colour; pass Start for ₹200; Go to Jail and pay to leave; a birthday card; running out of money ends it", r.squares === 28 && r.groups === 6 && r.bought && r.rent && r.buildBtn && r.house && r.passStart && r.jail && r.bail && r.bailed && r.card && r.out && /wins/.test(r.win), r);
  ok("G7 Rish Business: four computer players buy cities and finish a short game (richest wins)", r.cpuGame && r.cpuBought >= 4 && r.rounds > 8, r);
  await E(() => document.getElementById("m-home") && document.getElementById("m-home").click());

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
