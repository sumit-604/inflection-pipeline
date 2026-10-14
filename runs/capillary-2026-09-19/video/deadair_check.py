import re, subprocess, sys

def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", path], capture_output=True, text=True).stdout
    return float(out.strip())

def check(path, max_gap=0.9, first_voice=0.5):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                          f"silencedetect=noise=-50dB:d={max_gap}", "-vn", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duration(path)
    problems = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else total
        if s < 0.05 and e > first_voice:
            problems.append(f"opening silence until {e:.2f}s (limit {first_voice}s)")
        elif s >= 0.05 and s < total - 1.0:
            problems.append(f"silence {s:.2f}s to {e:.2f}s ({e - s:.2f}s)")
    print(f"{path}: duration {total:.2f}s, silences found {len(starts)}")
    for p in problems:
        print("  FAIL", p)
    if not problems:
        print("  PASS: voice within 0.5 s, no gap of 0.9 s or more before the last second")
    return not problems

if __name__ == "__main__":
    ok = all(check(p) for p in sys.argv[1:])
    sys.exit(0 if ok else 1)
