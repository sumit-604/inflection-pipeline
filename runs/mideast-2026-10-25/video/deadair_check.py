import re, subprocess, sys
path = sys.argv[1]
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=nw=1:nk=1", path], capture_output=True, text=True).stdout.strip())
log = subprocess.run(["ffmpeg", "-i", path, "-af", "silencedetect=noise=-40dB:d=1.2", "-f", "null", "-"],
    capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
hits = 0
for i, s in enumerate(starts):
    e = ends[i] if i < len(ends) else dur
    if s < 0.5 or e > dur - 1.5:
        continue
    print(f"dead air {s:.2f}s to {e:.2f}s ({e - s:.2f}s)")
    hits += 1
print(f"dead air hits: {hits}")
sys.exit(1 if hits else 0)
