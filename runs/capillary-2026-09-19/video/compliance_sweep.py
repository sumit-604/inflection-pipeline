import re, sys, importlib.util, pathlib

BANNED = [
    r"\bbuy\b", r"\bsell\b", r"\bhold\b", r"\bwatchlist\b", r"\bavoid\b",
    r"₹\s?490\b", r"\bshare price\b", r"\bmarket cap", r"\bfair value\b",
    r"\btarget price\b", r"\bprice target\b",
    r"\b\d+(\.\d+)?\s?(x|times)\s+(p/?e|earnings|profit|forward)",
    r"\b(p/?e|price to earnings)\b[^.]{0,20}\b\d+(\.\d+)?\s?(x|times)?\b",
    r"\bsynthetic voice\b", r"\bai voice\b", r"\bdoes not hold\b", r"\bholds? (this|the) stock\b",
]
ALLOWED = [
    r"1\.4 times its adjusted ebitda",
    r"about one point four times its adjusted e bit da",
    r"operating profit × a multiple",
    r"take operating profit a year ahead, and multiply it",
]

def lines_from_script(path):
    spec = importlib.util.spec_from_file_location("script", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    scenes = getattr(mod, "SCENES", None) or getattr(mod, "scenes", None)
    out = []
    for sc in scenes:
        sid, title, rows = sc[0], sc[1], sc[2]
        out.append((sid, "title", str(title)))
        for row in rows:
            for part in row[1:]:
                out.append((sid, row[0], str(part)))
    return out

def lines_from_html(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    text = re.sub(r"<script[^>]*src=[^>]*></script>", "", text)
    strings = re.findall(r"[\"'`]([^\"'`\n]{3,})[\"'`]", text)
    strings += re.findall(r">([^<>]{3,})<", text)
    return [("html", "text", s) for s in strings]

def check(items):
    fails = 0
    for where, who, s in items:
        low = s.lower()
        if any(re.search(a, low) for a in ALLOWED):
            continue
        for pat in BANNED:
            if re.search(pat, low):
                print(f"FAIL [{where} / {who}] pattern {pat!r}: {s}")
                fails += 1
    return fails

if __name__ == "__main__":
    script_path = sys.argv[1] if len(sys.argv) > 1 else "script.py"
    html_path = sys.argv[2] if len(sys.argv) > 2 else "video.html"
    items = lines_from_script(script_path) + lines_from_html(html_path)
    n = check(items)
    print(f"compliance sweep: {len(items)} strings checked, {n} failures")
    sys.exit(1 if n else 0)
