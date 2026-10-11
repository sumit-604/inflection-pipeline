"""assemble.py - builds the timeline and the audio mix from the per-sentence WAVs.
Timing rules (job section 2): first voice 0.3 s; 0.18 s between sentences of one speaker;
0.4 s on a speaker change; 0.7 s between scenes, filled with a soft whoosh.
Writes: timeline.js (read by video.html), out/audio.wav, out/timeline.json, out/listen_times.json"""
import json, pathlib, re, sys, importlib.util
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
from PIL import ImageFont
from kokoro_onnx.tokenizer import Tokenizer
import synth

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
SR = 48000
FIRST_VOICE, GAP_SAME, GAP_CHANGE, GAP_SCENE = 0.3, 0.18, 0.4, 0.7
TITLE_HOLD = 3.0          # title card hold after scene 1's last sentence (chime + soft pad under it)
END_CARD = 12.0           # end card; the last 5 s are left empty for the YouTube end screen
FPS = 25

spec = importlib.util.spec_from_file_location("script", HERE / "script.py")
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
man = json.loads((HERE / "wav" / "manifest.json").read_text())
tok = Tokenizer()
class _K: tokenizer = tok

def nph(text, lang="en-us"):
    t = synth.to_phonemes(_K, text, lang) if text.strip() else ""
    return max(1, len(t))

# ---------- captions: wrap into pages of at most two lines ----------
FONT = ImageFont.truetype(str(HERE / "assets/fonts/Inter.ttf"), 46)
try: FONT.set_variation_by_axes([14, 600])
except Exception: pass
CAP_W = 1500
def _greedy(words, width):
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if FONT.getlength(t) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def wrap_pages(text):
    words = text.split(); lines = _greedy(words, CAP_W)
    if len(lines) > 2 and len(lines) % 2 == 1:      # avoid a one-line orphan page: rebalance into an even number of lines
        w = CAP_W
        while w > 600:
            w -= 20; cand = _greedy(words, w)
            if len(cand) == len(lines) + 1: lines = cand; break
    return [lines[i:i + 2] for i in range(0, len(lines), 2)]

# ---------- timeline ----------
def build():
    t = FIRST_VOICE
    scenes, prev_spk = [], None
    for sc in S.SCENES:
        sid, title, rows = sc[0], sc[1], sc[2]
        rows_out, first_start, source, card = [], None, None, None
        ri_last_end = None
        for ri, row in enumerate(rows):
            spk = row[0]
            if spk == "Source": source = row[1]; continue
            if spk == "Card": card = row[1]; continue
            parts = []
            sents = synth.split_sentences(row[2])
            for pi, sent in enumerate(sents):
                m = man[f"s{sid:02d}_r{ri:02d}_p{pi}"]
                if prev_spk is not None and first_start is not None or parts:
                    pass
                parts.append({"wav": f"s{sid:02d}_r{ri:02d}_p{pi}", "dur": m["dur"], "text": sent})
            # place the parts
            for pi, p in enumerate(parts):
                if first_start is None and ri_last_end is None and pi == 0:
                    p["start"] = t   # t already holds the correct gap for scene start
                else:
                    if pi == 0: gap = GAP_SAME if spk == prev_spk else GAP_CHANGE
                    else: gap = GAP_SAME
                    t = ri_last_end + gap if ri_last_end is not None else t
                    p["start"] = t
                p["end"] = p["start"] + p["dur"]
                ri_last_end = p["end"]; t = p["end"]
                if first_start is None: first_start = p["start"]
            prev_spk = spk
            row_out = {"idx": ri, "speaker": spk, "caption": row[1], "spoken": row[2], "start": parts[0]["start"], "end": parts[-1]["end"], "parts": parts}
            # caption pages, timed in proportion to characters across the row's span
            pages = wrap_pages(row[1]); total = sum(len(" ".join(pg)) for pg in pages); acc = 0; cp = []
            span0, span1 = row_out["start"], row_out["end"]
            for pg in pages:
                n = len(" ".join(pg)); a = span0 + (span1 - span0) * acc / total; acc += n
                b = span0 + (span1 - span0) * acc / total
                cp.append({"lines": pg, "start": a - 0.05 if cp else a, "end": b})
            row_out["pages"] = cp
            # sub-sentence cues
            cues = []
            for ph in S.CUES.get((sid, ri), []):
                cues.append({"phrase": ph, "t": cue_time(row_out, ph)})
            row_out["cues"] = cues
            rows_out.append(row_out)
        last_end = ri_last_end
        scenes.append({"id": sid, "title": title, "kind": sc[3], "rows": rows_out, "source": source, "card": card,
                       "voice_start": first_start, "voice_end": last_end})
        t = last_end + GAP_SCENE + (TITLE_HOLD if sid == 1 else 0)
        prev_spk = None
        # next scene's first part starts at t
    return scenes, t

def cue_time(row, phrase):
    spoken = row["spoken"]; i = spoken.lower().find(phrase.lower())
    assert i >= 0, (phrase, spoken)
    # locate the part containing char i
    off = 0
    for p in row["parts"]:
        j = spoken.find(p["text"], off)
        if j <= i < j + len(p["text"]) + 1:
            lang = "en-gb" if row["speaker"] == "Meera" else "en-us"
            pre = p["text"][: i - j]
            frac = nph(pre, lang) / nph(p["text"], lang) if pre.strip() else 0.0
            return round(p["start"] + frac * p["dur"], 3)
        off = j + len(p["text"])
    raise AssertionError(phrase)

def main():
    scenes, t_end_voice = build()
    # fix: the t cursor logic above sets each scene's first part start from t; verify gaps
    for i, sc in enumerate(scenes):
        # boundaries for visuals: scene visible from (voice_start - 0.35); first scene from 0
        sc["t0"] = 0.0 if i == 0 else sc["voice_start"] - 0.35
    for i, sc in enumerate(scenes):
        sc["t1"] = scenes[i + 1]["t0"] if i + 1 < len(scenes) else scenes[-1]["voice_end"] + 0.35
    end_t0 = scenes[-1]["voice_end"] + 0.35
    total = end_t0 + END_CARD
    # stamp thuds: scene 4 envelope (on the sentence naming warrants), scene 13 WRONG IF stamp (end of last sentence)
    s4 = next(s for s in scenes if s["id"] == 4); s13 = next(s for s in scenes if s["id"] == 13)
    stamps = {"warrants": s4["rows"][2]["start"] + 1.25, "wrongif": s13["rows"][5]["end"] - 0.55}
    tl = {"fps": FPS, "total": total, "end_t0": end_t0, "scenes": scenes, "stamps": stamps, "title_hold": TITLE_HOLD,
          "values": json.loads((HERE / "scene11_values.json").read_text())}
    (OUT / "timeline.json").write_text(json.dumps(tl, indent=1, ensure_ascii=False))
    (HERE / "timeline.js").write_text("window.TL = " + json.dumps(tl, ensure_ascii=False) + ";\n")
    mix(tl)
    listen_times(scenes)
    print(f"total {total:.2f}s ({int(total//60)}:{total%60:05.2f}); voice ends {end_t0-0.35:.2f}s")
    for sc in scenes: print(f"scene {sc['id']:2d} t0={sc['t0']:7.2f} voice {sc['voice_start']:7.2f}-{sc['voice_end']:7.2f}")

# ---------- audio ----------
def load(name):
    a, sr = sf.read(HERE / "wav" / (name + ".wav")); a = a.astype(np.float64)
    a = resample_poly(a, SR // sr, 1) if SR % sr == 0 else a
    rms = np.sqrt(np.mean(a ** 2)) + 1e-9
    return a * (10 ** (-20 / 20) / rms)          # equalise voices to about -20 dBFS RMS

def whoosh(dur=0.62, peak=0.16, seed=0):
    rng = np.random.default_rng(seed); n = int(dur * SR); x = rng.standard_normal(n)
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    cutoff = 300 * (14 ** np.sin(np.linspace(0, np.pi, n)))   # sweeps up then down
    y = np.zeros(n); a_prev = 0.0
    for i in range(n):
        a = 1 - np.exp(-2 * np.pi * cutoff[i] / SR); a_prev += a * (x[i] - a_prev); y[i] = a_prev
    y2 = np.zeros(n); b = 0.0
    for i in range(n):
        a = 1 - np.exp(-2 * np.pi * (cutoff[i] * 0.35) / SR); b += a * (y[i] - b); y2[i] = b
    y = y - y2   # band-pass-ish
    y = y / (np.max(np.abs(y)) + 1e-9) * peak * env
    return y

def thud(dur=0.5, peak=0.7):
    n = int(dur * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (62 + 40 * np.exp(-t * 30)) * t) * np.exp(-t * 11)
    rng = np.random.default_rng(3); noise = rng.standard_normal(n) * np.exp(-t * 60)
    k = np.ones(40) / 40; noise = np.convolve(noise, k, "same")
    y = body + 0.35 * noise
    return y / np.max(np.abs(y)) * peak

def bell(dur, f=523.25, peak=0.12):
    n = int(dur * SR); t = np.arange(n) / SR
    y = sum(a * np.sin(2 * np.pi * f * m * t) * np.exp(-t * d) for m, a, d in ((1, 1, 1.4), (2.0, .35, 2.2), (3.01, .15, 3.5)))
    return y / np.max(np.abs(y)) * peak

def pad(dur, f=(196.0, 293.66, 392.0), peak=0.05, fade_in=0.6, fade_out=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    y = sum(np.sin(2 * np.pi * x * t + i) * (1 + 0.15 * np.sin(2 * np.pi * 0.3 * t + i)) for i, x in enumerate(f))
    env = np.minimum(1, t / fade_in) * np.minimum(1, (dur - t) / fade_out)
    return y / np.max(np.abs(y)) * peak * env

def mix(tl):
    n = int((tl["total"] + 0.2) * SR); m = np.zeros(n)
    def put(sig, t0):
        i = int(round(t0 * SR)); m[i:i + len(sig)] += sig[: max(0, n - i)]
    for sc in tl["scenes"]:
        for row in sc["rows"]:
            for p in row["parts"]: put(load(p["wav"]), p["start"])
    scs = tl["scenes"]
    for i in range(len(scs) - 1):
        a = scs[i]["voice_end"]
        if scs[i]["id"] == 1:
            put(bell(2.6), a + 0.45); put(pad(TITLE_HOLD + 0.7, peak=0.04), a + 0.05)   # title card chime + soft pad
            put(whoosh(0.62, seed=i), a + TITLE_HOLD + 0.08)
        else:
            put(whoosh(0.62, seed=i), a + 0.04)
    put(whoosh(0.62, seed=99), scs[-1]["voice_end"] + 0.04)          # into the end card
    put(thud(), tl["stamps"]["warrants"]); put(thud(), tl["stamps"]["wrongif"])
    # soft outro tone under the end card (no music): sustained pad + a slow bell
    put(pad(tl["total"] - tl["end_t0"] + 0.2, peak=0.07, fade_in=1.0, fade_out=0.9), tl["end_t0"])
    put(bell(4.0, f=392.0, peak=0.10), tl["end_t0"] + 0.4)
    m = m[: int(tl["total"] * SR)]
    pk = np.max(np.abs(m)); m = m / pk * 0.89 if pk > 0.89 else m
    sf.write(OUT / "audio.wav", m.astype(np.float32), SR)

# ---------- operator listen list ----------
def listen_times(scenes):
    words = ["Capillary", "aiRA", "Kognitiv", "SessionM", "Optum", "Bengaluru", "K P M G", "Sharma's"]
    out = {w: [] for w in words}; nums = []
    for sc in scenes:
        for row in sc["rows"]:
            for w in words:
                for mm in re.finditer(re.escape(w), row["spoken"], re.I):
                    out[w].append({"scene": sc["id"], "t": cue_time_idx(row, mm.start()), "line": row["caption"][:70]})
            if sc["id"] in (7, 8, 11):
                for mm in re.finditer(r"₹?\d[\d,.]*%?|\b(?:one and a half|under four|thirteen and a half|thirty one) percent|\b(?:zero|seven|twelve|twenty|one|two|four|five|fifty|[a-z]+ hundred) ?[a-z ]*?crore\b", row["caption"] + "", re.I):
                    nums.append((sc["id"], row["idx"], mm.group(0)))
    # numbers by spoken phrase (scenes 7, 8, 11)
    numlist = []
    for sc in scenes:
        if sc["id"] not in (7, 8, 11): continue
        for row in sc["rows"]:
            if row["cues"]:
                for c in row["cues"]: numlist.append({"scene": sc["id"], "t": c["t"], "say": c["phrase"], "line": row["caption"][:60]})
    for sid, ridx, phrases in NUM_PHRASES:
        sc = next(s for s in scenes if s["id"] == sid); row = sc["rows"][ridx]
        for ph in phrases:
            numlist.append({"scene": sid, "t": cue_time(row, ph), "say": ph, "line": row["caption"][:60]})
    numlist.sort(key=lambda x: x["t"])
    (OUT / "listen_times.json").write_text(json.dumps({"names": out, "numbers": numlist}, indent=1, ensure_ascii=False))

def cue_time_idx(row, i):
    off = 0
    for p in row["parts"]:
        j = row["spoken"].find(p["text"], off)
        if j <= i < j + len(p["text"]) + 1:
            lang = "en-gb" if row["speaker"] == "Meera" else "en-us"
            pre = p["text"][: i - j]
            return round(p["start"] + (nph(pre, lang) / nph(p["text"], lang) if pre.strip() else 0) * p["dur"], 2)
        off = j + len(p["text"])
    return round(row["start"], 2)

V = S.V
NUM_PHRASES = [
 (7, 1, ["after staff share costs"]), (8, 1, ["Under four"]),
 (11, 1, [S.say_int(S.R27) + " crore", S.say_int(S.R30) + " crore"]),
 (11, 2, [S.say_int(S.E27) + " crore", S.say_int(S.E30) + " crore", "thirty one percent"]),
 (11, 3, [S.say_int(S.P27) + " crore", S.say_int(S.P30) + " crore"]),
 (11, 5, [S.say_int(S.BEAR30) + " crore", S.say_int(S.BULL30) + " crore"]),
 (8, 4, ["above ten percent"]), (8, 1, ["thirteen and a half"]),
]

if __name__ == "__main__":
    main()
