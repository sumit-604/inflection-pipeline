"""audio_final.py - two-pass loudnorm of the raw mix to about -14 LUFS / -1 dBTP, then verify on the DECODED MP4 (after the AAC encode).
  python audio_final.py norm <long|short> [tp]     out/audio_<fmt>.wav -> out/audio_<fmt>_norm.wav
  python audio_final.py measure <file.mp4|wav>     prints integrated loudness, true peak, LRA"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent; OUT = HERE / "out"
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
def measure(path):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    tail = r[r.rindex("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", tail).group(1)); LRA = float(re.search(r"LRA:\s+([\d.]+) LU", tail).group(1)); TP = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail).group(1))
    return I, TP, LRA
def norm(fmt, tp=-1.5):
    src = OUT / f"audio_{fmt}.wav"; dst = OUT / f"audio_{fmt}_norm.wav"
    r = run(["ffmpeg", "-hide_banner", "-i", str(src), "-af", f"loudnorm=I=-14:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"]).stderr
    j = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP={tp}:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src), "-af", af, "-ar", "48000", str(dst)], check=True)
    print(f"{fmt}: raw I={j['input_i']} TP={j['input_tp']} -> normalised {measure(dst)} (I, TP, LRA) -> {dst.name}")
if __name__ == "__main__":
    if sys.argv[1] == "norm": norm(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else -1.5)
    else: print("I=%.1f LUFS  TP=%.1f dBFS  LRA=%.1f LU" % measure(sys.argv[2]))
