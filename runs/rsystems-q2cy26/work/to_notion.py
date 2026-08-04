#!/usr/bin/env python3
"""Convert the GitHub-flavored review markdown to Notion-flavored markdown.
- pipe tables -> <table header-row="true"> blocks
- fenced code blocks passed through verbatim
- outside code: escape <, >, $, ^ and stray | ; keep **bold**, `code`, headings, ---
Cells: escape <, >, $, ^ ; keep **bold**.
"""
import re, sys

src = sys.argv[1]
lines = open(src).read().split("\n")

def esc_text(s):
    # escape characters that would be misinterpreted in Notion-flavored markdown prose
    s = s.replace("\\|", "|")          # normalise any escaped pipe first
    for ch in ["<", ">", "$", "^"]:
        s = s.replace(ch, "\\" + ch)
    s = s.replace("|", "\\|")          # stray pipes outside tables
    return s

def esc_cell(s):
    s = s.strip()
    s = s.replace("\\|", "|")
    for ch in ["<", ">", "$", "^"]:
        s = s.replace(ch, "\\" + ch)
    return s

def is_table_row(l):
    return l.lstrip().startswith("|")

def is_sep_row(l):
    return bool(re.fullmatch(r"\s*\|[\s:|\-]+\|\s*", l)) and set(l.strip()) <= set("|:- ")

out = []
i = 0
in_code = False
while i < len(lines):
    l = lines[i]
    stripped = l.strip()
    # code fences
    if stripped.startswith("```"):
        out.append(l)
        i += 1
        while i < len(lines) and not lines[i].strip().startswith("```"):
            out.append(lines[i])   # verbatim, no escaping
            i += 1
        if i < len(lines):
            out.append(lines[i])   # closing fence
            i += 1
        continue
    # table block
    if is_table_row(l) and i + 1 < len(lines) and is_sep_row(lines[i+1]):
        header = l
        i += 2  # skip header + separator
        body = []
        while i < len(lines) and is_table_row(lines[i]) and not is_sep_row(lines[i]):
            body.append(lines[i]); i += 1
        def cells(row):
            r = row.strip()
            if r.startswith("|"): r = r[1:]
            if r.endswith("|"): r = r[:-1]
            # split on unescaped pipe
            parts = re.split(r"(?<!\\)\|", r)
            return [esc_cell(p) for p in parts]
        out.append('<table header-row="true">')
        hc = cells(header)
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in hc) + "</tr>")
        for b in body:
            bc = cells(b)
            # pad/truncate to header width
            while len(bc) < len(hc): bc.append("")
            bc = bc[:len(hc)]
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in bc) + "</tr>")
        out.append("</table>")
        continue
    # normal line
    out.append(esc_text(l))
    i += 1

open(sys.argv[2], "w").write("\n".join(out))
print("wrote", sys.argv[2], "lines", len(out))
