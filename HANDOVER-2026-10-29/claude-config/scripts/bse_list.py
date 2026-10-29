import sys, requests, datetime
sys.path.insert(0, ".")
from collect_to_repo import BSE_ANN, BSE_HEADERS
scrip=sys.argv[1]; windows=int(sys.argv[2])
end=datetime.date.today(); rows=[]
for w in range(windows):
    frm=end-datetime.timedelta(days=180)
    for page in range(1,10):
        r=requests.get(BSE_ANN,timeout=30,headers=BSE_HEADERS,params={"pageno":page,"strCat":"-1","strType":"C","strPrevDate":frm.strftime("%Y%m%d"),"strToDate":end.strftime("%Y%m%d"),"strScrip":scrip,"strSearch":"P","subcategory":"-1"})
        b=(r.json() or {}).get("Table") or []
        rows+=b
        if len(b)<50: break
    end=frm-datetime.timedelta(days=1)
seen=set()
for x in rows:
    if x["NEWSID"] in seen: continue
    seen.add(x["NEWSID"])
    print((x.get("NEWS_DT") or "")[:10], "|", (x.get("CATEGORYNAME") or ""), "|", (x.get("NEWSSUB") or "")[:120].replace("\n"," "), "|", x.get("ATTACHMENTNAME"))
