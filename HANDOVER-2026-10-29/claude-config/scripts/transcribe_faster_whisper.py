import sys, types, subprocess, time, os
sys.modules['av'] = types.ModuleType('av')  # av DLL blocked by Application Control; ffmpeg decodes instead
import numpy as np
from faster_whisper import WhisperModel

src, out, model_name = sys.argv[1], sys.argv[2], sys.argv[3]
CHUNK = 600  # seconds; keeps the audio buffer near 38 MB on a low-RAM machine
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                           capture_output=True, text=True, check=True).stdout)
partdir = out + ".parts"
os.makedirs(partdir, exist_ok=True)
model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=6)
prompt = ("Fedbank Financial Services earnings call, Q2 FY27. Federal Bank, Parvez Mulla, gold loan, LAP, "
          "loan against property, AUM, PCR, GNPA, NNPA, Stage 2, Stage 3, CRAR, credit cost, direct assignment, "
          "co-lending, crore, lakh, basis points, tonnage, LTV.")
t0 = time.time()
start = 0.0
while start < dur:
    part = os.path.join(partdir, f"{int(start):05d}.txt")
    if not os.path.exists(part):
        pcm = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-ss", str(start), "-t", str(CHUNK), "-i", src,
                              "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
        audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
        segs, _ = model.transcribe(audio, language="en", beam_size=5, vad_filter=True,
                                   initial_prompt=prompt, condition_on_previous_text=False)
        lines = []
        for s in segs:
            t = int(start + s.start)
            lines.append(f"[{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}] {s.text.strip()}")
        with open(part + ".tmp", "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        os.replace(part + ".tmp", part)
        del audio, pcm
    print(f"chunk {int(start)}s done, elapsed {time.time()-t0:.0f}s", flush=True)
    start += CHUNK
with open(out, "w", encoding="utf-8") as f:
    for name in sorted(os.listdir(partdir)):
        if name.endswith(".txt"):
            f.write(open(os.path.join(partdir, name), encoding="utf-8").read())
print(f"done in {time.time()-t0:.0f}s", flush=True)
