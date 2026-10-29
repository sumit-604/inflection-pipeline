"""
stitch_review.py — build REVIEW.md from the analysts' company sections, word for word.

Inputs in <run>/deep/:  out/*.md (company sections), assembly/order.json,
assembly/holdings.md (holdings_table.py, placed first under the title),
assembly/front.md, assembly/back.md.  Output: <run>/REVIEW.md

Company sections start with "## <Company>: <headline>". Per-batch extras
("## Unknowns...", "## Three things...", "## PUBLISH CANDIDATE") are skipped here:
the assembler merges them into back.md. DATA comment blocks are removed from the
body; their content lives in the Notion payload appendix.

Usage: python stitch_review.py [run folder]   (default: newest announcements folder)
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
EXTRA = re.compile(r"^(unknowns|three things|publish candidate|cross-links|rulings|next action|notion save|appendix|reading notes)", re.I)
DATA = re.compile(r"<!--\s*DATA.*?-->", re.S)


def sections(run):
    secs, items = {}, {}
    for path in sorted(glob.glob(os.path.join(run, "deep", "out", "*.md"))):
        text = open(path, encoding="utf-8").read()
        for part in re.split(r"(?m)^(?=## )", text):
            m = re.match(r"## (.+?)(?::\s|\n)", part)
            if not m or EXTRA.match(m.group(1)):
                continue
            name = m.group(1).strip()
            for blk in re.findall(r"items_covered:\s*\[([^\]]*)\]", part):
                for n in re.findall(r"\d+", blk):
                    items[int(n)] = name
            secs[name] = DATA.sub("", part).rstrip() + "\n"
    return secs, items


def demote(sec):
    return re.sub(r"(?m)^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", sec)


def main():
    run = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else max(
        (d for d in glob.glob(os.path.join(ROOT, "announcements", "*")) if os.path.isdir(d)),
        key=os.path.getmtime)
    asm = os.path.join(run, "deep", "assembly")
    order = json.load(open(os.path.join(asm, "order.json"), encoding="utf-8"))
    secs, items = sections(run)

    used, missing = set(), []

    def take(names, level_down):
        out = []
        for n in names:
            key = n if n in secs else next((k for k in secs if k.lower() == n.lower()), None)
            if key is None:
                missing.append(n)
                continue
            used.add(key)
            out.append(demote(secs[key]) if level_down else secs[key])
        return out

    front = open(os.path.join(asm, "front.md"), encoding="utf-8").read().rstrip() + "\n"
    # The holdings price table (holdings_table.py) opens the review, under the title.
    hold_path = os.path.join(asm, "holdings.md")
    if os.path.exists(hold_path):
        hold = open(hold_path, encoding="utf-8").read().rstrip() + "\n\n"
        title, sep, rest = front.partition("\n")
        front = (title + "\n\n" + hold + rest.lstrip("\n")) if title.startswith("# ") else hold + front
    else:
        print("STITCH WARNING: deep/assembly/holdings.md missing; run holdings_table.py first")
    parts = [front]
    parts += take(order.get("material_in_master", []), False)
    brief = take(order.get("brief_in_master", []), True)
    if brief:
        parts.append("## The others, briefly\n")
        parts += brief
    notable = take(order.get("notable_not_in_master", []), True)
    routine = take(order.get("routine_not_in_master", []), True)
    leftover = [k for k in secs if k not in used]
    if notable or routine or leftover:
        parts.append("## Not in COMPANIES MASTER\n")
        parts += notable + routine + [demote(secs[k]) for k in leftover]
    parts.append(open(os.path.join(asm, "back.md"), encoding="utf-8").read().rstrip() + "\n")

    # Coverage: an item counts when its group's output file lists it in any items_covered line.
    owner = {}
    for wf in glob.glob(os.path.join(run, "deep", "work", "[TN]*.json")):
        w = json.load(open(wf, encoding="utf-8"))
        out = os.path.join(run, w["output"])
        listed = set()
        if os.path.exists(out):
            for blk in re.findall(r"items_covered:\s*\[?([^\]\n]*)", open(out, encoding="utf-8").read()):
                listed |= {int(x) for x in re.findall(r"\d+", blk)}
        for c in w["companies"]:
            for it in c["items"]:
                owner[it["index_no"]] = (c["company"], it["index_no"] in listed)
    index_items = sorted(int(m) for m in re.findall(
        r"(?m)^\| (\d+) \|", open(os.path.join(run, "INDEX.md"), encoding="utf-8").read()))
    rows = [f"| {n} | {owner.get(n, ('?', False))[0]} | "
            f"{'yes' if owner.get(n, ('', False))[1] else 'NOT COVERED'} |" for n in index_items]
    covered = sum(1 for n in index_items if owner.get(n, ("", False))[1])
    parts.append("## Appendix B: item coverage\n\n"
                 f"Items covered: {covered} of {len(index_items)}\n\n"
                 "| Item | Company | Reviewed |\n|---|---|---|\n" + "\n".join(rows) + "\n")

    with open(os.path.join(run, "REVIEW.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts).replace(" — ", ": "))
    print(f"STITCH: sections={len(secs)} placed={len(used)} leftover_appended={len(leftover)} "
          f"order_names_not_found={missing} items_covered={covered}/{len(index_items)}")


if __name__ == "__main__":
    main()
