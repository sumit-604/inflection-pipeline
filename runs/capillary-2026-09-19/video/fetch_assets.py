"""Download the Kokoro model files and the three fonts into ./assets (git-ignored)."""
import pathlib, urllib.parse, urllib.request
A = pathlib.Path(__file__).resolve().parent / "assets"
(A / "fonts").mkdir(parents=True, exist_ok=True)
REL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
for n in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
    if not (A / n).exists(): urllib.request.urlretrieve(REL + n, A / n)
for f in ("ofl/fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf", "ofl/inter/Inter[opsz,wght].ttf", "ofl/caveat/Caveat[wght].ttf"):
    out = A / "fonts" / (pathlib.Path(f).name.split("[")[0] + ".ttf")
    if not out.exists():
        urllib.request.urlretrieve("https://github.com/google/fonts/raw/main/" + urllib.parse.quote(f), out)
print("assets ready in", A)
