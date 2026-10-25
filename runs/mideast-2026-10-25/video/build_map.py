"""build_map.py - turns Natural Earth 1:50m country shapes (public domain, downloaded by fetch_assets.py) into map_data.js,
the single Middle East map asset reused by every scene, the Short and the thumbnail. Projection: equirectangular, lat scale cos(25 deg)."""
import json, math, pathlib
from shapely.geometry import shape, box, mapping
HERE = pathlib.Path(__file__).resolve().parent
LON0, LON1, LAT0, LAT1, K = 30.0, 66.0, 10.0, 40.0, 32.0
CX = math.cos(math.radians(25))
def px(lon, lat): return ((lon - LON0) * CX * K, (LAT1 - lat) * K)
W, H = (LON1 - LON0) * CX * K, (LAT1 - LAT0) * K
KEEP = {"Iran", "Iraq", "Saudi Arabia", "Yemen", "Oman", "United Arab Emirates", "Qatar", "Kuwait", "Bahrain", "Egypt", "Sudan", "Eritrea", "Djibouti", "Israel", "Jordan",
        "Syria", "Turkey", "Pakistan", "Ethiopia", "Somalia", "Somaliland", "Palestine", "Lebanon", "Cyprus", "Afghanistan", "Turkmenistan", "Libya", "Azerbaijan", "Armenia",
        "Georgia", "India", "N. Cyprus", "Uzbekistan", "S. Sudan", "Chad", "Saudi Arabia", "Russia", "Kazakhstan", "Tajikistan", "Kyrgyzstan", "Ukraine", "Greece", "Bulgaria", "Romania", "Kenya", "Uganda", "Niger", "Central African Rep.", "Tunisia", "Algeria", "Dem. Rep. Congo"}
g = json.load(open(HERE / "assets" / "ne_countries.geojson")); clip = box(LON0 - 0.5, LAT0 - 0.5, LON1 + 0.5, LAT1 + 0.5)
out = []
def ring_d(coords):
    pts = [px(*c) for c in coords]
    return "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"
for f in g["features"]:
    n = f["properties"]["NAME"]
    if n not in KEEP: continue
    geom = shape(f["geometry"]).intersection(clip)
    if geom.is_empty: continue
    geom = geom.simplify(0.04, preserve_topology=True)
    polys = [geom] if geom.geom_type == "Polygon" else [p for p in geom.geoms if p.geom_type == "Polygon"]
    d = ""
    for p in polys:
        if p.area < 0.02: continue
        d += ring_d(list(p.exterior.coords))
        for r in p.interiors: d += ring_d(list(r.coords))
    if d: out.append({"name": n, "d": d})
data = {"W": round(W, 1), "H": round(H, 1), "lon0": LON0, "lat1": LAT1, "k": K, "cx": CX, "countries": out}
(HERE / "map_data.js").write_text("window.MAPDATA = " + json.dumps(data, separators=(",", ":")) + ";\n")
print(len(out), "countries,", (HERE / "map_data.js").stat().st_size, "bytes; map units", data["W"], "x", data["H"])
