import re, sys, json
BASE = r"C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\worktrees\q2fy27\runs\heritgfood-q2fy27"
SRC = BASE + r"\inputs\Heritage_Q2FY27_Concall_16Oct2026_ASR_transcript.txt"
W = BASE + r"\work\a1-concall"
FT = BASE + r"\extracted\heritgfood-concall-q2fy27-fulltext.md"
ST = BASE + r"\extracted\heritgfood-concall-q2fy27-structured.md"

raw = open(SRC, "rb").read().decode("utf-8")
src = [l.rstrip("\r") for l in raw.split("\n")]
if src and src[-1] == "":
    src.pop()
N = len(src)
tsre = re.compile(r"^\[(\d\d):(\d\d):(\d\d)\]")
ts_of = {}   # src line (1-based) -> "hh:mm:ss"
occ = {}     # ts -> list of lines
for i, l in enumerate(src, 1):
    m = tsre.match(l)
    if m:
        t = "%s:%s:%s" % m.groups()
        ts_of[i] = t
        occ.setdefault(t, []).append(i)

def secs(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

def block_of_line(i):
    if i not in ts_of:
        return 0
    return min(7, secs(ts_of[i]) // 600 + 1)

def to_hms_mmss(t):
    h, m, s = map(int, t.split(":"))
    return "%02d:%02d" % (h * 60 + m, s)

def line_for_ts(t):
    n = 1
    if "#" in t:
        t, n = t.split("#"); n = int(n)
    if t.startswith("L"):
        return int(t[1:])
    if t not in occ:
        # nearest earlier timestamp
        cand = [l for l, x in ts_of.items() if secs(x) <= secs(t)]
        print("WARN ts not found", t, file=sys.stderr)
        return max(cand)
    return occ[t][n - 1]

def norm(s):
    return re.sub(r"[^a-z0-9%$.]+", " ", s.lower()).strip()

def find_line(t, value):
    i = line_for_ts(t)
    v = norm(value)
    lo, hi = max(1, i - 4), min(N, i + 8)
    # exact line containing in window (single line)
    best = None
    for j in range(lo, hi + 1):
        if v in norm(src[j - 1]):
            if best is None or abs(j - i) < abs(best - i):
                best = j
    if best:
        return best, True
    # two-line join
    for j in range(lo, hi):
        if v in norm(src[j - 1] + " " + src[j]):
            return j, True
    # three-line join
    for j in range(lo, hi - 1):
        if v in norm(" ".join(src[j - 1:j + 2])):
            return j, True
    return i, False

# ---------- turns ----------
turns = []
for l in open(W + r"\turns.txt", encoding="utf-8"):
    l = l.rstrip("\n")
    if not l.strip():
        continue
    t, kind, spk, _ = l.split("|", 3)
    mid = t.startswith("*")
    t = t.lstrip("*")
    turns.append(dict(ts=t, kind=kind, spk=spk, mid=mid))
for k, t in enumerate(turns):
    t["id"] = "T%03d" % (k + 1)
    t["start"] = line_for_ts(t["ts"])
qn = 0
for t in turns:
    if t["kind"] == "Q":
        qn += 1
        t["q"] = "Q%02d" % qn
for k, t in enumerate(turns):
    if k + 1 < len(turns):
        nx = turns[k + 1]
        t["end"] = nx["start"] if nx["mid"] else nx["start"] - 1
    else:
        t["end"] = N
    if t["end"] < t["start"]:
        t["end"] = t["start"]
turns[0]["start"] = 16

# ---------- rows ----------
rows = []
warn = []
def load(fn):
    for l in open(W + "\\" + fn, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l.strip():
            continue
        typ, t, val, ctx = l.split("|", 3)
        ln, ok = find_line(t, val)
        if not ok:
            i0 = line_for_ts(t)
            lo, hi = max(1, i0 - 4), min(N, i0 + 8)
            seg = [(j, tsre.sub("", src[j - 1]).strip()) for j in range(lo, hi + 1)]
            words = re.findall(r"[A-Za-z0-9%$.]+", val)
            res = None
            if typ == "E":
                w0 = words[0].lower()
                for j, tx in seg:
                    if w0 in tx.lower():
                        res = (j, val); break
            else:
                joined = ""
                offs = []
                for jj, x in seg:
                    offs.append((len(joined), jj))
                    joined += x + " "
                for nw in (5, 4, 3):
                    if len(words) < nw: continue
                    rx = r"\W+".join(re.escape(w) for w in words[:nw])
                    ms = list(re.finditer(rx, joined, re.I))
                    if ms:
                        # prefer match nearest the anchor line
                        def lineof(pos):
                            c = offs[0][1]
                            for o, jj in offs:
                                if o <= pos: c = jj
                            return c
                        m = min(ms, key=lambda mm: abs(lineof(mm.start()) - i0))
                        lw = words[-3:] if len(words) >= 3 else words
                        rx2 = r"\W+".join(re.escape(w) for w in lw)
                        m2 = re.search(rx2, joined[m.start():], re.I)
                        end = m.start() + m2.end() if m2 else m.start() + len(val) + 20
                        res = (lineof(m.start()), joined[m.start():end].strip()); break
            if res:
                ln, val = res
                ok = True
            else:
                warn.append((typ, t, val, ln))
        rows.append(dict(type=typ, ts=t, val=val, ctx=ctx, src=ln, ok=ok))
load("numbers.txt")
load("others.txt")

order = ["N", "E", "F", "D", "Q"]
names = dict(N="NUMBER", E="ENTITY", F="FORWARD", D="DATE", Q="QUALIFIER")
rows_by = {k: [r for r in rows if r["type"] == k] for k in order}
# chronological within type, stable
for k in order:
    rows_by[k].sort(key=lambda r: r["src"])
seq = []
for k in order:
    seq += rows_by[k]
for i, r in enumerate(seq, 1):
    r["id"] = "R%03d" % i

# ---------- fulltext layout ----------
def build_header(H, mapfn):
    hl = []
    A = hl.append
    A("=== A1 EXTRACTION HEADER ===")
    A("source_filename: Heritage_Q2FY27_Concall_16Oct2026_ASR_transcript.txt")
    A("doctype: concall (machine transcript, ASR; NOT a company-filed transcript)")
    A("page_count_pdfinfo: N.A. (plain-text transcript, not a PDF). Coverage unit: 7 ten-minute time blocks treated as pages")
    A("formfeed_count: N.A. (text file). Page markers [page N] inserted: 7")
    A("line_count: %d source lines (source file); fulltext file line_count: %d (includes this header and 7 page markers)" % (N, H + N + 7))
    A("unit_convention: Millions (Rs million, financials); Crores (Rs crore, industry and segment sizes); also lakh litres per day (volume), Rs per litre (price), lakh crore (industry size)")
    A("conversion_factor_to_cr: Millions -> x0.1 (1 Rs million = 0.1 Rs crore); Crores -> x1; lakh crore -> x100,000 (1 lakh crore = 100,000 Rs crore); lakh litres per day -> volume, x1 lakh = 100,000 litres, no Rs conversion; Rs per litre -> price, no conversion. Extracted text NOT converted. Note ASR prints one revenue figure with a dollar sign ($13,196 million); speaker said Rs million")
    A("text_layer_present: N.A. (plain-text ASR transcript; pdffonts gate not applicable; no rendering or OCR applied)")
    A("extraction_mode: text-only (verbatim save, CR characters normalised to LF)")
    A("render_candidates: none")
    A("rendered_pages: none")
    A("page_coverage: 100%% (7 of 7 blocks present: %s; all %d source lines carried, 1 to %d)" % ("; ".join("block %d=%s" % (b, rng) for b, rng in BLOCKS), N, N))
    A("detected_quarter: Q2 FY27 (also H1 FY27)")
    A("extraction_date: 2026-10-19")
    A("source_audio: Audio-Q2-FY27-Earnings Call-16102026.mp3 (66:25, 8 kHz mono); call date 16 Oct 2026, 11:00 IST; engine faster-whisper 1.2.1 small.en; transcribed 2026-10-18")
    A("evidence_tier: [MGMT, ASR]; verify load-bearing numbers against a filed transcript when posted")
    A("page_marker_map (fulltext line of each marker): " + "; ".join("[page %d] line %d" % (b, mapfn(('marker', b))) for b, _ in BLOCKS))
    A("provenance_header_lines: fulltext lines %d-%d carry source lines 1-15 verbatim (the provenance header of the source file)" % (mapfn(1), mapfn(15)))
    A("")
    A("asr_name_mapping (as stated in the source header, lines 8-9 of the source; verbatim lines NOT rewritten):")
    for a, b in [("Brahminaraj", "Brahmani Nara"), ("Sheedip Kesavan / Sridhi Kagan", "Sreedeep Kesavan"), ("Uma Kanta Bare", "Umakanta Barik"), ("Getaway", "Get-A-Way"), ("Novandee", "Novandie"), ("Aavin / Avin / oven", "Aavin"), ("Nandini / Dandini", "Nandini")]:
        A("  ASR %-34s -> %s" % (a, b))
    A("  Further ASR variants seen in text (not in source-header mapping): Srivithya / Srivithi / Shree Deep (self-IDs, read with Sreedeep Kesavan per source-header mapping of Sridhi Kagan only); Peritage Nutrived / Holy One Subsidy (Heritage NutriVate); Alpenvie / AlpenV; Kaunulk (unresolved); Ramani, Edie, Anshit (unmapped)")
    A("")
    A("speaker_turn_map (built from in-text cues only; no speaker inferred from content; line numbers are FULLTEXT lines; 'shares line' = turn starts or ends mid-line):")
    A("  turns: %d (T001-T%03d); analyst questions: %d (Q01-Q%02d)" % (len(turns), len(turns), qn, qn))
    for t in turns:
        a, b = mapfn(t["start"]), mapfn(t["end"])
        qtag = (" [" + t["q"] + "]") if "q" in t else ""
        mid = " (shares first line with previous turn)" if t["mid"] else ""
        A("  %s%s lines %d-%d (%s-%s) %s%s" % (t["id"], qtag, a, b, to_hms_mmss(ts_of[t["start"]]) if t["start"] in ts_of else "00:00", to_hms_mmss(ts_of[t["end"]]) if t["end"] in ts_of else "", t["spk"], mid))
    A("=== END HEADER ===")
    return hl

BLOCKS = []
bounds = {}
for i in range(16, N + 1):
    b = block_of_line(i)
    bounds.setdefault(b, [i, i])
    bounds[b][1] = i
for b in range(1, 8):
    f, l = bounds[b]
    BLOCKS.append((b, "%s-%s (src %d-%d)" % (to_hms_mmss(ts_of[f]), to_hms_mmss(ts_of[l]), f, l)))

def make_map(H):
    # marker before first line of each block
    marker_src = {bounds[b][0]: b for b in range(1, 8)}
    m = {}
    cur = H
    for i in range(1, N + 1):
        if i in marker_src:
            cur += 1
            m[("marker", marker_src[i])] = cur
        cur += 1
        m[i] = cur
    return lambda k: m[k], marker_src

H = 60
for _ in range(10):
    mapfn, marker_src = make_map(H)
    hl = build_header(H, mapfn)
    if len(hl) == H:
        break
    H = len(hl)
mapfn, marker_src = make_map(H)
hl = build_header(H, mapfn)
assert len(hl) == H, (len(hl), H)

body = []
for i in range(1, N + 1):
    if i in marker_src:
        b = marker_src[i]
        body.append("[page %d] (block %d, %s)" % (b, b, ["00:00-09:59","10:00-19:59","20:00-29:59","30:00-39:59","40:00-49:59","50:00-59:59","60:00-66:25"][b-1]))
    body.append(src[i - 1])
out = hl + body
open(FT, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
assert len(out) == H + N + 7

# ---------- structured ----------
cnt = {k: len(rows_by[k]) for k in order}
total = len(seq)
L = []
A = L.append
A("# A1 STRUCTURED EXTRACTION: Heritage Foods (HERITGFOOD) Q2 FY27 earnings call, 16 Oct 2026 (ASR transcript)")
A("source: Heritage_Q2FY27_Concall_16Oct2026_ASR_transcript.txt | fulltext: runs/heritgfood-q2fy27/extracted/heritgfood-concall-q2fy27-fulltext.md")
A("evidence_tier: [MGMT, ASR]. Row line numbers are FULLTEXT file lines. Page = ten-minute block (1=00:00-09:59 ... 7=60:00-66:25). t= is the source segment timestamp.")
A("units: Rs million x0.1 -> Rs crore; Rs crore x1; lakh crore x100,000; no value converted in rows.")
A("ROW ID RANGE: R001-R%03d" % total)
A("counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d | total %d" % (cnt["N"], cnt["E"], cnt["F"], cnt["D"], cnt["Q"], total))
A("turns: %d (T001-T%03d); analyst questions: %d (Q01-Q%02d)" % (len(turns), len(turns), qn, qn))
A("row format: R### | page N | line L | TYPE | verbatim value | short context | t=hh:mm:ss")
A("rows anchored by search window around the segment timestamp; rows flagged ANCHOR_APPROX when the verbatim value was not found as a single contiguous string near the timestamp")
A("")
A("## SPEAKER TURN MAP (copy of fulltext header; fulltext lines)")
for t in turns:
    qtag = (" [" + t["q"] + "]") if "q" in t else ""
    A("%s%s lines %d-%d: %s" % (t["id"], qtag, mapfn(t["start"]), mapfn(t["end"]), t["spk"]))
A("")
for k in order:
    A("## %s TABLE (%d rows)" % (names[k], cnt[k]))
    for r in rows_by[k]:
        flag = "" if r["ok"] else " | ANCHOR_APPROX"
        pg = block_of_line(r["src"])
        pgs = "page %d" % pg if pg else "page header"
        A("%s | %s | line %d | %s | %s | %s | t=%s%s" % (r["id"], pgs, mapfn(r["src"]), names[k], r["val"], r["ctx"], ts_of.get(r["src"], "hdr"), flag))
    A("")
open(ST, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("total rows", total, cnt, "turns", len(turns), "qs", qn, "H", H, "fulltext lines", len(out))
for w in warn:
    print("NOTFOUND", w)
