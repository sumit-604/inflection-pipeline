"""
prep_review.py — mechanical prep for the daily deep review (no Claude needed).

For one announcements folder (default: the newest under announcements/):
  1. text/<pdf stem>.txt          full text, "===== PAGE n =====" markers
  2. page_images/<stem>_p<n>.png  every page with no text layer (scans, signed pages)
  3. deep/work/T##.json           companies IN COMPANIES MASTER (Opus analysts)
     deep/work/N##.json           companies NOT in master (Sonnet analysts)
  4. deep/work/unmapped.json      Screener names not yet in review_spec/notion_map.json;
                                  the Claude run must match these to Notion first, add them
                                  to notion_map.json, and re-run this script.

Usage:
    python prep_review.py                      # newest folder
    python prep_review.py announcements/<dir>
"""

import glob
import json
import os
import sys

import pymupdf

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, "review_spec")
MAP_FILE = os.path.join(SPEC, "notion_map.json")
BLANK_CHARS = 80


def read_index(run):
    rows = []
    # split on "\n" only: a stray "\r" inside a Screener title must not break the row
    for line in open(os.path.join(run, "INDEX.md"), encoding="utf-8", newline="").read().split("\n"):
        line = line.replace("\r", " ")
        if not line.startswith("| ") or line.startswith("| #"):
            continue
        c = line.rstrip("\n").split(" | ")
        if len(c) < 6 or not c[0][2:].strip().isdigit():
            continue
        rows.append({"index_no": int(c[0][2:]), "day": c[1], "company": c[2],
                     "type": c[3], "screener_summary": c[4], "file": c[5].rstrip(" |")})
    return rows


def extract(run, pdf):
    stem = pdf[:-4]
    txt = os.path.join(run, "text", stem + ".txt")
    doc = pymupdf.open(os.path.join(run, pdf))
    parts, images = [], []
    for i, page in enumerate(doc, 1):
        t = page.get_text()
        parts.append(f"\n===== PAGE {i} =====\n{t}")
        if len(t.strip()) < BLANK_CHARS:
            png = f"page_images/{stem}_p{i}.png"
            if not os.path.exists(os.path.join(run, png)):
                page.get_pixmap(dpi=110).save(os.path.join(run, png))
            images.append(png)
    with open(txt, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return {"pdf": pdf, "text": f"text/{stem}.txt", "pages": doc.page_count,
            "image_pages": len(images), "images": images}


def pack(companies, max_pages, max_cos, prefix, run):
    groups = []
    for c in sorted(companies, key=lambda c: -c["pages"]):
        g = next((g for g in groups if sum(x["pages"] for x in g) + c["pages"] <= max_pages
                  and len(g) < max_cos), None)
        g.append(c) if g else groups.append([c])
    names = []
    for k, g in enumerate(groups, 1):
        name = f"{prefix}{k:02d}"
        with open(os.path.join(run, "deep", "work", name + ".json"), "w", encoding="utf-8") as f:
            json.dump({"root": run, "output": f"deep/out/{name}.md", "companies": g},
                      f, indent=1, ensure_ascii=False)
        names.append(name)
    return names


def main():
    run = sys.argv[1] if len(sys.argv) > 1 else max(
        (d for d in glob.glob(os.path.join(ROOT, "announcements", "*")) if os.path.isdir(d)),
        key=os.path.getmtime)
    run = os.path.abspath(run)
    for d in ("text", "page_images", "deep/work", "deep/out"):
        os.makedirs(os.path.join(run, d), exist_ok=True)

    nmap = json.load(open(MAP_FILE, encoding="utf-8")) if os.path.exists(MAP_FILE) else {}
    companies, unmapped, pages, img = {}, set(), 0, 0
    for r in read_index(run):
        item = {k: r[k] for k in ("index_no", "day", "type", "screener_summary")}
        if r["file"].endswith(".pdf") and os.path.exists(os.path.join(run, r["file"])):
            item.update(extract(run, r["file"]))
            pages += item["pages"]
            img += item["image_pages"]
        else:
            item.update(pdf=None, pages=0,
                        note="No PDF. Insider trade or rating update; the type is the disclosure.")
        if r["company"] not in nmap:
            unmapped.add(r["company"])
        c = companies.setdefault(r["company"], {"company": r["company"],
                                                "notion_page": nmap.get(r["company"]),
                                                "items": []})
        c["items"].append(item)
    for c in companies.values():
        c["pages"] = sum(i["pages"] for i in c["items"])

    with open(os.path.join(run, "deep", "work", "unmapped.json"), "w", encoding="utf-8") as f:
        json.dump(sorted(unmapped), f, indent=1, ensure_ascii=False)

    cos = list(companies.values())
    t = pack([c for c in cos if c["notion_page"]], 90, 3, "T", run)
    n = pack([c for c in cos if not c["notion_page"]], 110, 8, "N", run)
    items = sum(len(c["items"]) for c in cos)
    print(f"PREP: run={run} items={items} companies={len(cos)} pages={pages} "
          f"image_pages={img} T_groups={len(t)} N_groups={len(n)} unmapped={len(unmapped)}")


if __name__ == "__main__":
    main()
