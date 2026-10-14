"""shorts_build.py - six vertical Shorts (1080x1920) cut from the long MP4.
Each Short = hook clip (payoff frame + spoken/on-screen hook) + clips cut from the long video + end clip
('Full video on the channel.'). Large captions are drawn with Pillow. Usage: python shorts_build.py <long.mp4> <outdir>"""
import importlib.util, json, pathlib, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from scipy.signal import resample_poly

HERE = pathlib.Path(__file__).resolve().parent
LONG = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
TMP = HERE / "out" / "shorts_tmp"; TMP.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("shorts", HERE / "shorts.py"); SH = importlib.util.module_from_spec(spec); spec.loader.exec_module(SH)
TL = json.loads((HERE / "out" / "timeline.json").read_text())
MAN = json.loads((HERE / "wav_shorts" / "manifest.json").read_text())
ROWS = {(s["id"], r["idx"]): r for s in TL["scenes"] for r in s["rows"]}
W, H = 1080, 1920; VY, VH = 420, 616
GOLD, LILAC, TEXT, BASE = (242, 193, 78), (201, 167, 240), (244, 238, 248), (42, 28, 60)

def font(name, size, axes):
    f = ImageFont.truetype(str(HERE / "assets/fonts" / name), size)
    try: f.set_variation_by_axes(axes)
    except Exception: pass
    return f
def fraunces(size): return font("Fraunces.ttf", size, [72, 800, 0, 0])
def inter(size, w=800): return font("Inter.ttf", size, [28, w])

def wrap(text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def fit_hook(text):
    for size in range(84, 48, -4):
        f = fraunces(size); ls = wrap(text, f, 940)
        if len(ls) <= 3: return f, ls, size
    return f, ls, size

def header(hook):
    im = Image.new("RGBA", (W, VY), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([50, 40, 330, 96], 14, fill=(227, 161, 59)); d.text((190, 68), "Business Decoded", font=inter(28, 800), fill=(17, 17, 17), anchor="mm")
    d.rounded_rectangle([W - 140, 36, W - 50, 126], 20, fill=GOLD); d.text((W - 95, 82), "KS", font=fraunces(52), fill=(31, 20, 48), anchor="mm")
    f, ls, size = fit_hook(hook); y = 128
    for l in ls: d.text((W // 2, y), l, font=f, fill=GOLD, anchor="ma"); y += int(size * 1.08)
    return im

def caption_png(lines, color, name, size=66):
    f = inter(size, 800); lh = int(size * 1.22); im = Image.new("RGBA", (W, lh * len(lines) + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        d.text((W // 2, 10 + i * lh), l, font=f, fill=color, anchor="ma", stroke_width=0)
    p = TMP / (name + ".png"); im.save(p); return p, im.size[1]

def pages_for(text, max_lines=4, size=66):
    f = inter(size, 800); ls = wrap(text, f, 960)
    return [ls[i:i + max_lines] for i in range(0, len(ls), max_lines)]

SPK_COL = {"Narrator": TEXT, "Meera": LILAC, "Ramesh": (255, 217, 138)}

def run(cmd): subprocess.run(cmd, check=True, capture_output=True)
def probe_frame(t, out): run(["ffmpeg", "-y", "-ss", f"{t:.3f}", "-i", str(LONG), "-frames:v", "1", str(out)])

ENC = ["-r", "25", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

def clip(name, vin, ain, dur, hdr, caps, fade_header=False):
    """vin: ['-ss',a,'-t',d,'-i',long] or ['-loop','1','-framerate','25','-t',d,'-i',png]; ain: same or wav path list; caps: [(png,h,t0,t1)]"""
    out = TMP / (name + ".mp4")
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=#2A1C3C:s={W}x{H}:r=25:d={dur:.3f}"]
    cmd += vin
    n_in = 2
    cmd += ["-loop", "1", "-framerate", "25", "-t", f"{dur:.3f}", "-i", str(hdr)]; hdr_i = n_in; n_in += 1
    cap_idx = []
    for c in caps: cmd += ["-i", str(c[0])]; cap_idx.append(n_in); n_in += 1
    aud_i = None
    if ain is not None: cmd += ain; aud_i = n_in; n_in += 1
    fc = f"[1:v]crop=1536:876:192:84,scale={W}:{VH}[v];[0:v][v]overlay=0:{VY}[a0];"
    hv = f"[{hdr_i}:v]format=rgba" + (",fade=in:st=0:d=0.35:alpha=1" if fade_header else "") + "[h];"
    fc += hv + "[a0][h]overlay=0:0[a1];"
    last = "a1"
    for k, (c, i) in enumerate(zip(caps, cap_idx)):
        fc += f"[{last}][{i}:v]overlay=0:1090:enable='between(t,{c[2]:.3f},{c[3]:.3f})'[c{k}];"; last = f"c{k}"
    fc += f"[{last}]format=yuv420p[vout]"
    if aud_i is not None: fc += f";[{aud_i}:a]aresample=48000,apad=whole_dur={dur:.3f}[aout]"
    cmd += ["-filter_complex", fc, "-map", "[vout]"] + (["-map", "[aout]"] if aud_i is not None else []) + ["-t", f"{dur:.3f}"] + ENC + [str(out)]
    run(cmd); return out

def voice_wav(sid, ri, lead, tail, name):
    parts = [v for k, v in MAN.items() if v["scene"] == sid and v["row"] == ri]; parts.sort(key=lambda v: v["part"])
    sig, pos = [], 0.0; chunks = []
    for v in parts:
        a, sr = sf.read(HERE / "wav_shorts" / f"s{sid:02d}_r{ri:02d}_p{v['part']}.wav"); a = resample_poly(a.astype(np.float64), 48000 // sr, 1)
        a = a * (10 ** (-20 / 20) / (np.sqrt(np.mean(a ** 2)) + 1e-9)); chunks.append(a)
    gap = np.zeros(int(.18 * 48000)); body = chunks[0]
    for c in chunks[1:]: body = np.concatenate([body, gap, c])
    full = np.concatenate([np.zeros(int(lead * 48000)), body, np.zeros(int(tail * 48000))])
    p = TMP / (name + ".wav"); sf.write(p, np.clip(full, -.95, .95).astype(np.float32), 48000); return p, len(full) / 48000

def build(s):
    n = s["n"]; sid = 100 + n; clips = []
    hdr = TMP / f"hdr{n}.png"; header(s["hook"]).save(hdr)
    # payoff frame
    ps, pr, po = s["payoff"]; row = ROWS[(ps, pr)]; pt = row["start"] + po
    pf = TMP / f"payoff{n}.png"; probe_frame(pt, pf)
    # hook clip
    wav, d = voice_wav(sid, 0, 0.2, 0.4, f"hook{n}")
    clips.append(clip(f"c{n}_hook", ["-loop", "1", "-framerate", "25", "-t", f"{d:.3f}", "-i", str(pf)], ["-i", str(wav)], d, hdr, [], fade_header=True))
    # segments
    last_end = None
    for k, (sc, ri) in enumerate(s["picks"]):
        r = ROWS[(sc, ri)]; a = max(0, r["start"] - 0.12); e = r["end"] + 0.2; dur = e - a
        caps = []; pages = pages_for(r["caption"]); tot = sum(len(" ".join(p)) for p in pages); acc = 0
        for pi, pg in enumerate(pages):
            t0 = (r["start"] - a) + (r["end"] - r["start"]) * acc / tot; acc += len(" ".join(pg)); t1 = (r["start"] - a) + (r["end"] - r["start"]) * acc / tot
            png, h = caption_png(pg, SPK_COL[r["speaker"]], f"cap{n}_{k}_{pi}"); caps.append((png, h, t0 - 0.03 if pi else 0.0, t1 + (0.2 if pi == len(pages) - 1 else 0)))
        clips.append(clip(f"c{n}_{k}", ["-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", str(LONG)], ["-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", str(LONG)], dur, hdr, caps))
        last_end = r["end"]
    # end clip
    ef = TMP / f"end{n}.png"; probe_frame(last_end + 0.05, ef)
    wav, d = voice_wav(sid, 1, 0.25, 0.9, f"endv{n}")
    png, h = caption_png(["Full video on", "the channel."], GOLD, f"endcap{n}", size=96)
    clips.append(clip(f"c{n}_end", ["-loop", "1", "-framerate", "25", "-t", f"{d:.3f}", "-i", str(ef)], ["-i", str(wav)], d, hdr, [(png, h, 0.0, d)]))
    lst = TMP / f"list{n}.txt"; lst.write_text("".join(f"file '{c}'\n" for c in clips))
    out = OUT / s["file"]
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(out)])
    return out

if __name__ == "__main__":
    only = [int(x) for x in sys.argv[3:]] if len(sys.argv) > 3 else None
    for s in SH.SHORTS:
        if only and s["n"] not in only: continue
        o = build(s); print("built", o)
