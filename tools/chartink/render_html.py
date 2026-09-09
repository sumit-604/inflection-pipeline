#!/usr/bin/env python3
"""Render the digests and briefs as browser-readable HTML.

Markdown in Notepad is hard to read and its tables do not render. This writes
a styled page per document plus an index per folder, so the history is
browsable by double-clicking one file.

Folders handled, both under data/chartink/analysis/:
    digest/   the computed daily digest (and its short market read)
    briefs/   the full nightly breadth brief

Output per folder: <date>.html, latest.html, index.html. Plus one
analysis/index.html that links both folders.

Markdown subset handled: YAML front matter (title, subtitle), # to ###
headings, pipe tables, bullet and numbered lists, > callout boxes, **bold**,
`code`, and the brief's status tags ([BULL], [BEAR], [FLAG], [ACTION],
[WATCH], [HIT], [OK], [NEW], [STALE]), which become coloured pills.

No dependencies.

    python tools/chartink/render_html.py
"""

from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = REPO_ROOT / "data" / "chartink" / "analysis"
FOLDERS = [
    ("briefs", "Market breadth briefs", "Full nightly brief: regime, indices, "
     "sectors, screeners, flow, thirty action points, three theses."),
    ("digest", "Daily digests", "Computed digest with percentiles, plus the "
     "short market read."),
]

TAGS = {
    "BULL": ("bull", "supports risk"),
    "BEAR": ("bear", "argues against risk"),
    "FLAG": ("flag", "needs a decision"),
    "ACTION": ("action", "do tomorrow"),
    "WATCH": ("watch", "check tomorrow"),
    "HIT": ("hit", "threshold fired"),
    "OK": ("ok", "threshold quiet"),
    "NEW": ("new", "first appearance"),
    "STALE": ("stale", "older than trade date"),
}

CSS = """
:root{--bg:#fbfaf8;--fg:#23201d;--mut:#6b645c;--line:#e2ddd6;--card:#fff;
--accent:#8a5a2c;--pos:#1a7f4b;--neg:#b3341f;--code:#f2efea;
--bull:#0a7a0a;--bullbg:#d2f0d2;--bear:#b00000;--bearbg:#ffdada;
--flag:#b05b00;--flagbg:#ffe6bf;--action:#0050b0;--actionbg:#d2e1f7;
--watch:#7a6200;--watchbg:#fff1b8;--hit:#b00000;--hitbg:#ffcfcf;
--ok:#0a7a0a;--okbg:#e0f2e0;--new:#4b0082;--newbg:#ece0f7;
--stale:#4a4a4a;--stalebg:#dddddd;--thesis:#4b0082;--thesisbg:#f3ecfa}
@media(prefers-color-scheme:dark){:root{--bg:#171513;--fg:#eae6e1;--mut:#9c948a;
--line:#332e29;--card:#1f1c19;--accent:#d9a066;--pos:#4ec98a;--neg:#f2765a;
--code:#26221e;--bullbg:#173a17;--bull:#7fe07f;--bearbg:#3d1414;--bear:#ff8a8a;
--flagbg:#3d2a0a;--flag:#ffc06a;--actionbg:#0f2747;--action:#8ab8ff;
--watchbg:#3a3208;--watch:#ffe27a;--hitbg:#3d1414;--hit:#ff8a8a;
--okbg:#173a17;--ok:#7fe07f;--newbg:#2a1440;--new:#d7b3ff;
--stalebg:#2a2a2a;--stale:#bbb;--thesisbg:#231533;--thesis:#d7b3ff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:64rem;margin:0 auto;padding:2rem 1.25rem 4rem}
h1{font-size:1.7rem;margin:0 0 .25rem;letter-spacing:-.01em}
h2{font-size:1.15rem;margin:2.2rem 0 .7rem;padding-bottom:.35rem;
border-bottom:1px solid var(--line);letter-spacing:-.01em}
h3{font-size:1rem;margin:1.5rem 0 .5rem}
p{margin:.7rem 0}
ul,ol{margin:.6rem 0;padding-left:1.4rem}
li{margin:.3rem 0}
code{background:var(--code);padding:.1rem .35rem;border-radius:4px;
font:12.5px/1.4 ui-monospace,SFMono-Regular,Consolas,monospace}
.tw{overflow-x:auto;margin:.8rem 0;border:1px solid var(--line);
border-radius:10px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{padding:.45rem .65rem;text-align:left;border-bottom:1px solid var(--line);
vertical-align:top}
th{background:var(--code);font-weight:600;color:var(--mut);
font-size:12px;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
tr:last-child td{border-bottom:none}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.pos{color:var(--pos)}.neg{color:var(--neg)}
.nf{color:var(--mut);font-style:italic}
.sub{color:var(--mut);font-size:13.5px;margin:0 0 1.6rem}
.box{background:var(--card);border:1px solid var(--line);
border-left:4px solid var(--accent);border-radius:10px;
padding:.5rem 1.1rem .7rem;margin:1rem 0}
.box p{margin:.5rem 0}
.box.action{border-left-color:var(--action);background:var(--actionbg)}
.box.flag{border-left-color:var(--flag);background:var(--flagbg)}
.box.thesis{border-left-color:var(--thesis);background:var(--thesisbg)}
.read{background:var(--card);border:1px solid var(--line);
border-left:3px solid var(--accent);border-radius:10px;padding:.4rem 1.1rem 1rem;
margin-top:1rem}
.read h2{border:none;margin-top:.9rem}
.tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.05em;
padding:.05rem .45rem;border-radius:999px;margin-right:.3rem;vertical-align:middle;
white-space:nowrap}
.tag.bull{color:var(--bull);background:var(--bullbg)}
.tag.bear{color:var(--bear);background:var(--bearbg)}
.tag.flag{color:var(--flag);background:var(--flagbg)}
.tag.action{color:var(--action);background:var(--actionbg)}
.tag.watch{color:var(--watch);background:var(--watchbg)}
.tag.hit{color:var(--hit);background:var(--hitbg)}
.tag.ok{color:var(--ok);background:var(--okbg)}
.tag.new{color:var(--new);background:var(--newbg)}
.tag.stale{color:var(--stale);background:var(--stalebg)}
a{color:var(--accent)}
.idx{list-style:none;padding:0}
.idx li{border-bottom:1px solid var(--line);padding:.55rem .2rem}
.idx a{text-decoration:none;font-weight:600}
.nav{margin-bottom:1.4rem;font-size:13px}
.nav a{margin-right:1rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr));
gap:1rem;margin-top:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:1rem 1.2rem}
.card h2{border:none;margin:0 0 .3rem;font-size:1.05rem}
.card p{margin:.3rem 0;color:var(--mut);font-size:13.5px}
"""


def esc(t):
    return html.escape(t, quote=False)


def inline(t):
    """Bold, code, tags, NOT FOUND."""
    t = esc(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)

    def tag(m):
        name = m.group(1)
        cls, title = TAGS[name]
        return f'<span class="tag {cls}" title="{title}">{name}</span>'

    t = re.sub(r"\[(" + "|".join(TAGS) + r")\]", tag, t)
    t = t.replace("NOT FOUND", '<span class="nf">NOT FOUND</span>')
    return t


def cell(t):
    inner = inline(t)
    s = t.strip()
    if re.fullmatch(r"[+-][\d,]+\.?\d*%?", s):
        cls = "pos" if s.startswith("+") else "neg"
        if re.fullmatch(r"\+0+\.?0*%?", s):
            cls = ""
        return f'<td class="num"><span class="{cls}">{inner}</span></td>'
    if re.fullmatch(r"-?[\d,]+\.?\d*%?", s) or s.startswith("n="):
        return f'<td class="num">{inner}</td>'
    return f"<td>{inner}</td>"


def split_front_matter(md):
    """Return (meta dict, body). Meta is {} when there is no front matter."""
    if not md.startswith("---"):
        return {}, md
    m = re.match(r"---\n(.*?)\n---\n?", md, re.S)
    if not m:
        return {}, md
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, md[m.end():]


def box_class(first_line):
    s = first_line.upper()
    if "TOP 3 ACTIONS" in s or "TOP ACTIONS" in s:
        return "box action"
    if "TOP FLAG" in s:
        return "box flag"
    if "THESIS" in s:
        return "box thesis"
    return "box"


def to_html(md):
    out = []
    lines = md.split("\n")
    i = 0
    in_read = False

    while i < len(lines):
        line = lines[i]

        if line.strip() == "<!-- market-read -->":
            if not in_read:
                out.append('<div class="read">')
                in_read = True
            i += 1
            continue

        # Callout box: consecutive lines starting with "> ".
        if line.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i][1:].lstrip())
                i += 1
            first = next((b for b in block if b.strip()), "")
            inner = to_html("\n".join(block))
            out.append(f'<div class="{box_class(first)}">{inner}</div>')
            continue

        # Table.
        if (line.startswith("|") and i + 1 < len(lines)
                and re.fullmatch(r"\|[\s:\-|]+\|", lines[i + 1].strip())):
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            body = []
            while i < len(lines) and lines[i].startswith("|"):
                body.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="tw"><table><thead><tr>')
            for h in head:
                out.append(f"<th>{inline(h)}</th>")
            out.append("</tr></thead><tbody>")
            for row in body:
                out.append("<tr>" + "".join(cell(c) for c in row) + "</tr>")
            out.append("</tbody></table></div>")
            continue

        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif re.match(r"\s*[-*] ", line):
            items = []
            while i < len(lines) and re.match(r"\s*[-*] ", lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\s*[-*] ', '', lines[i]))}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif re.match(r"\s*\d+\. ", line):
            items = []
            while i < len(lines) and (re.match(r"\s*\d+\. ", lines[i])
                                      or (lines[i].startswith("   ") and items)):
                if re.match(r"\s*\d+\. ", lines[i]):
                    items.append(inline(re.sub(r"^\s*\d+\. ", "", lines[i])))
                else:
                    items[-1] += " " + inline(lines[i].strip())
                i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>")
            continue
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.strip():
            para = [line]
            i += 1
            while (i < len(lines) and lines[i].strip()
                   and not lines[i].startswith(("#", "-", "*", "|", "<!--", ">"))
                   and not re.match(r"\s*\d+\. ", lines[i])):
                para.append(lines[i])
                i += 1
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            continue

        i += 1

    if in_read:
        out.append("</div>")
    return "\n".join(out)


def page(title, body, nav=""):
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{esc(title)}</title><style>{CSS}</style></head><body>"
        f'<div class="wrap">{nav}{body}</div></body></html>'
    )


def render_folder(folder, label):
    d = ANALYSIS / folder
    if not d.exists():
        return None
    dated = sorted((p for p in d.glob("*.md")
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem)),
                   key=lambda p: p.stem)
    if not dated:
        return None

    # Appendix files (<date>-appendix.md) render to their own page but are not
    # "the brief" for that date: they never become latest.html.
    for p in d.glob("*-appendix.md"):
        meta, body_md = split_front_matter(p.read_text(encoding="utf-8"))
        body = to_html(body_md)
        if meta.get("title"):
            body = f"<h1>{esc(meta['title'])}</h1>" + (
                f'<p class="sub">{esc(meta["subtitle"])}</p>' if meta.get("subtitle") else "") + body
        (d / (p.stem + ".html")).write_text(
            page(f"{label} {p.stem}", body,
                 '<div class="nav"><a href="../index.html">&larr; Analysis home</a>'
                 '<a href="index.html">All dates</a></div>'), encoding="utf-8")

    nav = ('<div class="nav"><a href="../index.html">&larr; Analysis home</a>'
           '<a href="index.html">All dates</a></div>')
    newest_note = ""
    for p in dated:
        md = p.read_text(encoding="utf-8")
        meta, body_md = split_front_matter(md)
        body = to_html(body_md)
        if meta.get("title"):
            head = f"<h1>{esc(meta['title'])}</h1>"
            if meta.get("subtitle"):
                head += f'<p class="sub">{esc(meta["subtitle"])}</p>'
            body = head + body
        (d / (p.stem + ".html")).write_text(
            page(f"{label} {p.stem}", body, nav), encoding="utf-8")
        if p is dated[-1]:
            shutil.copyfile(d / (p.stem + ".html"), d / "latest.html")
            words = len(body_md.split())
            newest_note = f"{p.stem}, {words:,} words"

    items = []
    for p in reversed(dated):
        md = p.read_text(encoding="utf-8")
        words = len(md.split())
        mark = ""
        if folder == "digest" and "## Market read" not in md:
            mark = ' <span class="nf">no read</span>'
        appendix = ""
        if (d / (p.stem + "-appendix.md")).exists():
            appendix = f' &middot; <a href="{p.stem}-appendix.html">data appendix</a>'
        items.append(f'<li><a href="{p.stem}.html">{p.stem}</a> '
                     f'<span class="nf">{words:,} words</span>{mark}{appendix}</li>')
    index = (f"<h1>{esc(label)}</h1>"
             f'<p class="sub">{len(dated)} dated file(s). Newest first.</p>'
             f'<ul class="idx">{"".join(items)}</ul>')
    (d / "index.html").write_text(
        page(label, index, '<div class="nav"><a href="../index.html">'
                           '&larr; Analysis home</a></div>'),
        encoding="utf-8")
    return len(dated), newest_note


def main():
    if not ANALYSIS.exists():
        print("No analysis folder. Run the chain first.", file=sys.stderr)
        return 2
    cards = []
    for folder, label, blurb in FOLDERS:
        res = render_folder(folder, label)
        if res:
            n, note = res
            print(f"{folder}/: {n} page(s), newest {note}")
            cards.append(f'<div class="card"><h2><a href="{folder}/latest.html">'
                         f'{esc(label)}</a></h2><p>{esc(blurb)}</p>'
                         f'<p>Newest: {esc(note)} &middot; '
                         f'<a href="{folder}/index.html">all dates</a></p></div>')
        else:
            print(f"{folder}/: nothing to render")
    home = ('<h1>Market breadth analysis</h1>'
            '<p class="sub">Generated nightly from the Chartink dashboards.</p>'
            f'<div class="cards">{"".join(cards)}</div>')
    (ANALYSIS / "index.html").write_text(page("Market breadth analysis", home),
                                         encoding="utf-8")
    print("home: " + str(ANALYSIS / "index.html"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
