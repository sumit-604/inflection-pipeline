"""X clip: from 0:00 up to and including Meera's 'So the points business is booming?'. Cut with ffmpeg -c copy."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
long_mp4, out = sys.argv[1], sys.argv[2]
tl = json.loads((HERE / "out" / "timeline.json").read_text())
row = tl["scenes"][0]["rows"][4]
assert row["speaker"] == "Meera" and row["caption"].startswith("So the points business is booming")
end = row["end"] + 0.25
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", long_mp4, "-t", f"{end:.3f}", "-c", "copy", "-movflags", "+faststart", out], check=True)
print("x clip", out, "cut at", round(end, 2), "s")
