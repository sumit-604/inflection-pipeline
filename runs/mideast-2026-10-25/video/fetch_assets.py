"""fetch_assets.py - downloads the build-time assets into ./assets (git-ignored): the Kokoro model files, the Archivo and IBM Plex Sans font files
(the same files the Google Fonts CSS points to, https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&family=IBM+Plex+Sans:wght@400;500;600&display=block),
and the Natural Earth 1:50m country shapes (public domain) used by build_map.py. Nothing is fetched at render time."""
import pathlib, re, urllib.request
A = pathlib.Path(__file__).resolve().parent / "assets"; (A / "fonts").mkdir(parents=True, exist_ok=True)
REL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
for n in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
    if not (A / n).exists(): urllib.request.urlretrieve(REL + n, A / n)
css = urllib.request.urlopen(urllib.request.Request("https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&family=IBM+Plex+Sans:wght@400;500;600&display=block", headers={"User-Agent": "Mozilla/5.0 Chrome/120"})).read().decode()
for fam, w, u in re.findall(r"font-family: '([^']+)';.*?font-weight: (\d+);.*?src: url\((.*?)\)", css, re.S):
    out = A / "fonts" / f"{fam.replace(' ', '')}-{w}.ttf"
    if not out.exists(): urllib.request.urlretrieve(u, out)
ne = A / "ne_countries.geojson"
if not ne.exists(): urllib.request.urlretrieve("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson", ne)
print("assets ready in", A)
