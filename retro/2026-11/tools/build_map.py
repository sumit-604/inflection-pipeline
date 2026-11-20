"""Build company_map.json (canonical ticker -> run folders, company files, local review dirs) and aliases.json."""
import os, re, json, collections, sys
QR = sys.argv[1] if len(sys.argv) > 1 else r"C:\QuarterlyReviewer\QuarterlyReviewer\reviews"
named = json.load(open("keys_named.json")); qr = json.load(open("qr_dirs.json"))
MERGE = {"544555":"AMEENJI","ameenji":"AMEENJI","d-dev":"DEEDEV","deedev":"DEEDEV","divgi":"DIVGIITTS","divgiitts":"DIVGIITTS",
 "gocl":"GOCLCORP","goclcorp":"GOCLCORP","raymondrealty":"RAYMONDREL","raymondrel":"RAYMONDREL","sona":"SONACOMS","sonacoms":"SONACOMS",
 "qualitek":"QLL","qll":"QLL","ecosmobility":"ECOSMOBLTY","bandhan":"BANDHANBNK","goldium":"GOLDIAM","mtar":"MTARTECH","pngs":"PNGSREVA",
 "utlsolar":"UTLSOLAR","totem":"TOTEM","540686":"SMRUTHI","543709":"GARGI","544091":"QLL","544518":"LTELEVATOR","544710":"ACCORD","544740":"TIPCO","544793":"SUSAN","544826":"MILLWORKS","544895":"KWICK","544186":"TOTEM","credo":"MUFTI","mufti":"MUFTI","_template":"_SKIP"}
NAMES = {"DEEDEV":"DEE Development Engineers Ltd","GOCLCORP":"GOCL Corporation Ltd","RAYMONDREL":"Raymond Realty Ltd","SONACOMS":"Sona BLW Precision Forgings Ltd",
 "ECOSMOBLTY":"Ecos (India) Mobility & Hospitality Ltd","BANDHANBNK":"Bandhan Bank Ltd","GOLDIAM":"Goldiam International Ltd","MTARTECH":"MTAR Technologies Ltd",
 "PNGSREVA":"PNGS Reva","530077":"Puretrop Fruits Ltd"}
cm = {}
def ent(t):
    return cm.setdefault(t, {"ticker": t, "name": "", "runs": [], "company_files": [], "qr_dirs": [], "keys": []})
for k, v in named.items():
    t = MERGE.get(k) or (v["ticker"].split()[0] if v["ticker"] else k.upper())
    e = ent(t); e["runs"] += v["runs"]; e["keys"].append(k)
    n = v["name"]
    if n.startswith("??"):
        m = re.search(r"[—–\-�:]\s*([A-Z][A-Za-z0-9&.\(\) ']+?(Limited|Ltd))", n)
        n = m.group(1) if m else ""
    if n and not e["name"]: e["name"] = n.replace("&amp;", "&")
for t, n in NAMES.items():
    if t in cm: cm[t]["name"] = n
for f in sorted(os.listdir("corpus/companies")):
    t = f.split("__")[0]
    t2 = MERGE.get(t.lower(), t)
    if t2 not in cm:
        e = ent(t2)
        h = open("corpus/companies/"+f, encoding="utf-8", errors="replace").read(400)
        m = re.search(r"^# .*?[—–-]\s*(.+)$", h, re.M)
        e["name"] = m.group(1).strip() if m else ""
    cm[t2]["company_files"].append("corpus/companies/"+f)
for d, batches in qr.items():
    t = d if d in cm else MERGE.get(d.lower(), d)
    e = ent(t)
    for b in batches: e["qr_dirs"].append(os.path.join(QR, b, d))
    if not e["name"]:
        for b in batches:
            for fn in ("SIMPLE_BRIEF.md", "NARRATIVE.md", "REVIEW.md"):
                p = os.path.join(QR, b, d, fn)
                if os.path.exists(p):
                    h = [l for l in open(p, encoding="utf-8", errors="replace").read(600).splitlines() if l.startswith("#")]
                    if h: e["name"] = "?" + h[0].lstrip("# ")[:80]; break
            if e["name"]: break
STOP = re.compile(r"\b(ltd|limited|india|\(.*?\)|company|corporation|industries|technologies|solutions|services)\b\.?", re.I)
al = {}
for t, e in cm.items():
    a = {t}
    for k in e["keys"]:
        if len(k) >= 6 and not k.isdigit(): a.add(k)
    n = e["name"].lstrip("?")
    if n and not e["name"].startswith("?"):
        full = re.sub(r"\b(ltd|limited)\b\.?", "", n, flags=re.I).strip(" ,.")
        if len(full) >= 6: a.add(full)
        short = " ".join(STOP.sub("", n).split()[:2]).strip(" ,.&")
        if len(short) >= 6: a.add(short)
    al[t] = sorted(a)
cm.pop("_SKIP",None); al.pop("_SKIP",None)
json.dump(cm, open("company_map.json", "w"), indent=1); json.dump(al, open("aliases.json", "w"), indent=1)
print(len(cm), "companies;", sum(1 for e in cm.values() if e["runs"]), "with repo runs;", sum(1 for e in cm.values() if e["qr_dirs"]), "with QR dirs;",
      sum(1 for e in cm.values() if not e["runs"] and not e["qr_dirs"]), "company-file only")
for t, e in sorted(cm.items()):
    if not e["runs"]: print(f"{t:12s} {e['name'][:60]:60s} qr={len(e['qr_dirs'])} cf={len(e['company_files'])}")
