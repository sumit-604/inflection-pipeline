import sys, requests
sys.path.insert(0, r"C:\Users\SUMIT SHARMA\repos\inflection-pipeline\tools\collector")
from collect_to_repo import BSE_HEADERS
R=r"C:\Users\SUMIT SHARMA\repos\inflection-pipeline\runs\tll-2026-09-26\inputs"
bases=["https://www.bseindia.com/xml-data/corpfiling/AttachLive/","https://www.bseindia.com/xml-data/corpfiling/AttachHis/"]
for line in open(sys.argv[1], encoding="utf-8"):
    line=line.strip()
    if not line or line.startswith("#"): continue
    folder, name, att = [p.strip() for p in line.split("|")]
    ok=False
    for b in bases:
        try:
            body=requests.get(b+att,timeout=60,headers=BSE_HEADERS).content
        except Exception as e:
            continue
        if body.startswith(b"%PDF"):
            open(f"{R}\{folder}\{name}.pdf","wb").write(body); ok=True; break
    print(("OK  " if ok else "FAIL"), folder, name, att, len(body) if ok else "")
