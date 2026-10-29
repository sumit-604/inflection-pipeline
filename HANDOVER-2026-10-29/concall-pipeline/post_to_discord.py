"""
post_to_discord.py — Daily Concall Intelligence Discord webhook poster

Reads the concall + announcement briefs for a batch, posts a clean multi-embed
summary to a Discord channel via webhook, and attaches a rendered PDF of the
full newsletter (same content/styling as the email version).

Usage:
    python post_to_discord.py morning              # uses today's date
    python post_to_discord.py evening              # uses yesterday's date
    python post_to_discord.py morning 2026-05-13   # explicit date
    python post_to_discord.py morning --dry-run    # build PDF + print payload, no post
    python post_to_discord.py morning --no-pdf     # skip the PDF attachment

Config (from .env in the project folder OR environment variables):
    DISCORD_WEBHOOK_URL    Required — webhook URL from Discord channel settings
    DISCORD_BOT_NAME       Optional — display name (defaults to "Concall Intelligence")
"""

import os
import sys
import json
import re
import io
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# ---------- dependency bootstrap ----------
def _ensure(pkg: str, import_name: str | None = None):
    import importlib, subprocess
    try:
        return importlib.import_module(import_name or pkg)
    except ImportError:
        print(f"Installing '{pkg}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        return importlib.import_module(import_name or pkg)

requests = _ensure("requests")
markdown = _ensure("markdown")
pdfkit = _ensure("pdfkit")

# ---------- paths ----------
PROJECT_ROOT = Path(__file__).parent.resolve()
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
ENV_PATH = PROJECT_ROOT / ".env"

# ---------- .env loader ----------
def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env

ENV = load_env(ENV_PATH)

def cfg(key, default=None):
    return os.environ.get(key) or ENV.get(key, default)

WEBHOOK_URL = cfg("DISCORD_WEBHOOK_URL", "")
BOT_NAME = cfg("DISCORD_BOT_NAME", "Concall Intelligence")
WKHTMLTOPDF_PATH = cfg("WKHTMLTOPDF_PATH", r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
WATERMARK_TEXT = cfg("WATERMARK_TEXT", "KEERTI KAUSHIK")

# ---------- embed palette ----------
COLOR_HEADER = 0x1a4d8f       # navy
COLOR_CONCALL = 0x3498db      # blue
COLOR_ANNOUNCEMENT = 0x27ae60 # green
COLOR_EMPTY = 0x95a5a6        # gray

SECTION_BUDGET = 1900         # chars per embed (stay under Discord's 6000 total)

# ---------- PDF HTML template ----------
# wkhtmltopdf uses WebKit, so it supports the full CSS spec — same as a modern
# browser. We can reuse the email newsletter's design directly.
PDF_CSS = """
@page { size: A4; margin: 1.5cm 1.8cm; }
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    color: #1a1a1a;
    line-height: 1.5;
    margin: 0;
}
.header { border-bottom: 3px solid #1a4d8f; padding-bottom: 10px; margin-bottom: 20px; }
.header h1 { color: #1a4d8f; font-size: 22pt; margin: 0; letter-spacing: -0.3pt; }
.header .subtitle { color: #666666; font-size: 10pt; margin-top: 6px; }
.section { margin-bottom: 24px; page-break-inside: avoid; }
.section-tag {
    display: inline-block;
    background: #1a4d8f; color: #ffffff;
    padding: 4px 12px; font-size: 9pt; font-weight: 600;
    letter-spacing: 0.6pt; border-radius: 3px;
    margin-bottom: 8px;
}
.brief h1 {
    color: #1a4d8f; font-size: 16pt;
    border-bottom: 2px solid #1a4d8f; padding-bottom: 4px;
    margin-top: 18px;
}
.brief h2 {
    color: #1a4d8f; font-size: 13pt;
    border-bottom: 1px solid #dddddd; padding-bottom: 3px;
    margin-top: 16px;
}
.brief h3 { color: #2a5a9f; font-size: 11pt; margin-top: 12px; }
.brief h4 { color: #444444; font-size: 10pt; margin-top: 10px; }
.brief blockquote {
    border-left: 3px solid #c8d4e3;
    padding: 4px 12px;
    color: #555555;
    background: #f4f7fb;
    margin: 6px 0;
    border-radius: 0 3px 3px 0;
}
.brief table {
    border-collapse: collapse;
    margin: 10px 0;
    width: 100%;
    font-size: 9pt;
}
.brief th, .brief td {
    border: 1px solid #dddddd;
    padding: 5px 8px;
    vertical-align: top;
    text-align: left;
}
.brief th { background: #eef3f9; color: #1a4d8f; font-weight: 600; }
.brief code {
    background: #f4f4f4;
    padding: 1px 5px;
    color: #c0392b;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
    border-radius: 3px;
}
.brief pre {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 4px;
    font-size: 9pt;
    overflow-x: auto;
}
.brief ul, .brief ol { margin: 4px 0 8px 0; padding-left: 22px; }
.brief li { margin: 2px 0; }
.brief hr { border: none; border-top: 1px solid #e0e0e0; margin: 10px 0; }
.brief strong { color: #1a1a1a; }
.empty {
    color: #888888;
    font-style: italic;
    padding: 12px;
    background: #fafafa;
    border-radius: 4px;
}
/* Sentiment dots — replace emoji with reliable CSS-styled bullets */
.signal-green, .signal-yellow, .signal-red, .signal-alert {
    font-weight: bold;
    font-size: 13pt;
    line-height: 1;
    vertical-align: -1px;
    margin-right: 3px;
}
.signal-green  { color: #27ae60; }
.signal-yellow { color: #f39c12; }
.signal-red    { color: #c0392b; }
.signal-alert  { color: #c0392b; }

/* Watermark is injected separately as a tiled background image (see build_pdf_html). */
"""

# ---------- SVG watermark generator ----------
def make_watermark_data_uri(text: str) -> str:
    """Build a base64-encoded SVG data URI for use as a tiled body background.

    wkhtmltopdf renders body background-image across all pages of the PDF, so
    a tiled SVG watermark appears on every page automatically — unlike CSS
    position:fixed elements, which wkhtmltopdf only paints on page 1.
    """
    import base64
    safe = (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    # 700x500 tile, text rotated -30° in the centre. fill-opacity controls darkness.
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'width="700" height="500" viewBox="0 0 700 500">'
        '<g transform="rotate(-30 350 250)">'
        '<text x="350" y="265" '
        'font-family="Helvetica, Arial, sans-serif" '
        'font-size="56" '
        'font-weight="bold" '
        'fill="#555555" '
        'fill-opacity="0.30" '
        'text-anchor="middle" '
        'letter-spacing="4">'
        f'{safe}'
        '</text></g></svg>'
    )
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"

# ---------- emoji stripping ----------
# Replace 🟢 / 🔴 with CSS-styled dots. Strip all other emojis (they render as
# empty glyphs in wkhtmltopdf without a color-emoji font).
STYLED_EMOJIS = {
    "🟢": '<span class="signal-green">●</span>',
    "🟡": '<span class="signal-yellow">●</span>',
    "🔴": '<span class="signal-red">●</span>',
    "🚨": '<span class="signal-alert">▲</span>',
}

_EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F680-\U0001F6FF"  # Transport & Map
    "\U0001F700-\U0001F77F"  # Alchemical
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended (incl. colored circles)
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols & Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess etc
    "\U0001FA70-\U0001FAFF"  # Symbols & Pictographs Extended-A
    "\U00002600-\U000026FF"  # Misc Symbols (⭐ ⚡ ✅ etc)
    "\U00002700-\U000027BF"  # Dingbats (❓ ❗ etc)
    "\U00002B00-\U00002BFF"  # Misc Symbols & Arrows
    "\U0001F1E0-\U0001F1FF"  # Flags
    "]",
    flags=re.UNICODE,
)

def clean_md_for_pdf(text: str) -> str:
    """Strip decorative emojis from markdown; replace 🟢/🔴 with styled dots."""
    if not text:
        return ""

    # Replace whitelisted emojis with styled HTML, strip all others
    text = _EMOJI_PATTERN.sub(
        lambda m: STYLED_EMOJIS.get(m.group(0), ""),
        text,
    )

    # Collapse runs of 2+ spaces (left over after emoji removal)
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Clean up dangling separators at end of line ("X · ", "X — ", "X · ⭐" → "X")
    text = re.sub(r"\s+[·—\-]\s*$", "", text, flags=re.MULTILINE)

    # Tighten heading lines that lost their leading emoji ("##  Title" → "## Title")
    text = re.sub(r"^(#+)\s{2,}", r"\1 ", text, flags=re.MULTILINE)

    # Clean up section navigator separator artifacts: "§ 1 · " on its own → fine,
    # but "§ 1 ·  Title" → "§ 1 · Title"
    text = re.sub(r"§\s*(\d+)\s*·\s+", r"§ \1 · ", text)

    return text

def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists", "nl2br"],
    )

def build_pdf_html(batch: str, analysis_date: str, concall_md: str | None, announce_md: str | None) -> str:
    """Build the HTML that gets converted to PDF via wkhtmltopdf (WebKit)."""
    label = "MORNING" if batch == "morning" else "EVENING"
    date_obj = datetime.strptime(analysis_date, "%Y-%m-%d")
    nice_date = date_obj.strftime("%A, %B %d, %Y")

    concall_html = (
        f'<div class="brief">{md_to_html(clean_md_for_pdf(concall_md))}</div>'
        if concall_md else
        '<div class="empty">No concall brief generated for this batch.</div>'
    )
    announce_html = (
        f'<div class="brief">{md_to_html(clean_md_for_pdf(announce_md))}</div>'
        if announce_md else
        '<div class="empty">No announcement brief generated for this batch.</div>'
    )

    # Inject the watermark as a tiled background-image on body so it repeats on every page
    watermark_css = ""
    if WATERMARK_TEXT:
        uri = make_watermark_data_uri(WATERMARK_TEXT)
        watermark_css = (
            f'body {{ background-image: url("{uri}"); '
            'background-repeat: repeat; '
            'background-position: top left; }}'
        )

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Daily Concall Intelligence — {label} — {nice_date}</title>
<style>{PDF_CSS}
{watermark_css}
</style>
</head>
<body>
  <div class="header">
    <h1>Daily Concall Intelligence</h1>
    <div class="subtitle">{label} Brief &middot; {nice_date}</div>
  </div>

  <div class="section">
    <span class="section-tag">CONCALL ANALYSIS</span>
    {concall_html}
  </div>

  <div class="section">
    <span class="section-tag">ANNOUNCEMENT ANALYSIS</span>
    {announce_html}
  </div>
</body>
</html>"""

def render_pdf(html: str) -> bytes:
    """Convert HTML to a PDF byte string via wkhtmltopdf."""
    config = None
    if WKHTMLTOPDF_PATH and Path(WKHTMLTOPDF_PATH).exists():
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

    options = {
        "page-size": "A4",
        "margin-top": "15mm",
        "margin-bottom": "15mm",
        "margin-left": "18mm",
        "margin-right": "18mm",
        "encoding": "UTF-8",
        "enable-local-file-access": None,
        "footer-center": "Daily Concall Intelligence — Page [page] of [topage]",
        "footer-font-size": "8",
        "footer-spacing": "5",
        "footer-line": None,
        "quiet": "",
    }

    try:
        return pdfkit.from_string(html, output_path=False, options=options, configuration=config)
    except OSError as e:
        msg = str(e)
        if "wkhtmltopdf" in msg.lower() or "No such file or directory" in msg:
            raise RuntimeError(
                "wkhtmltopdf binary not found. Install it with one of:\n"
                "  winget install --id wkhtmltopdf.wkhtmltopdf -e\n"
                "  Download MSI from https://wkhtmltopdf.org/downloads.html\n"
                f"Expected at: {WKHTMLTOPDF_PATH}\n"
                "Or set WKHTMLTOPDF_PATH in .env to the actual install path."
            ) from e
        raise

# ---------- markdown cleaner (for Discord embed text) ----------
def clean_for_discord(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"^-{3,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\|.*\|\s*$\n?", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^>\s*\*\*(?:Rule|Trigger|Why this matters|The strongest [a-z\-]+ setup|The mispricing thesis)[^\n]*\n?",
        "", text, flags=re.MULTILINE | re.IGNORECASE,
    )
    text = re.sub(
        r"\*\*(?:🎯\s*)?SECTION NAVIGATOR\*\*[^\n]*\n(?:[^\n]*\n){0,3}",
        "", text, flags=re.MULTILINE | re.IGNORECASE,
    )
    text = re.sub(r"^####\s+(.+)$", r"__\1__", text, flags=re.MULTILINE)
    text = re.sub(r"^###\s+(.+)$", r"\n**\1**", text, flags=re.MULTILINE)
    text = re.sub(r"^##\s+(.+)$", r"\n**\1**", text, flags=re.MULTILINE)
    text = re.sub(r"^#\s+(.+)$", r"**\1**", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def extract_section(md_text: str, patterns: list[str]) -> str | None:
    for pat in patterns:
        match = re.search(
            r"^##\s*" + pat + r"[^\n]*\n(.*?)(?=^##\s|\Z)",
            md_text, flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if match:
            return match.group(1)
    return None

def extract_corpus_line(md_text: str) -> str | None:
    match = re.search(r"^\*\*Corpus:?\*\*\s*(.+?)$", md_text, flags=re.MULTILINE)
    return match.group(1).strip() if match else None

def truncate(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    trimmed = text[:max_chars].rsplit("\n", 1)[0]
    return trimmed + "\n\n_…(truncated — full content in the attached PDF)_"

def build_concall_summary(md_text: str) -> str:
    section = extract_section(md_text, [
        r"PART\s*1[^\n]*EXECUTIVE", r"PART\s*1\b",
        r"⚡\s*TL;DR", r"TL;DR", r"§\s*1",
    ])
    return truncate(clean_for_discord(section), SECTION_BUDGET) if section else "_See attached PDF._"

def build_announcement_summary(md_text: str) -> str:
    tldr = extract_section(md_text, [r"⚡\s*TL;DR", r"TL;DR"])
    callouts = extract_section(md_text, [
        r"§\s*1[^\n]*HIGH-SIGNAL", r"PART\s*1[^\n]*HIGH-SIGNAL",
    ])
    parts = []
    if tldr:
        parts.append(clean_for_discord(tldr))
    if callouts and callouts is not tldr:
        parts.append("**🎯 Top Callouts**\n" + clean_for_discord(callouts))
    if not parts:
        return "_See attached PDF._"
    return truncate("\n\n".join(parts), SECTION_BUDGET)

# ---------- payload builder ----------
def build_payload(batch: str, analysis_date: str, concall_md: str | None, announce_md: str | None) -> dict:
    label = batch.upper()
    date_obj = datetime.strptime(analysis_date, "%Y-%m-%d")
    nice_date = date_obj.strftime("%a, %d %b %Y")

    concall_corpus = extract_corpus_line(concall_md) if concall_md else None
    announce_corpus = extract_corpus_line(announce_md) if announce_md else None

    embeds = []
    stats_lines = []
    if concall_corpus:
        stats_lines.append(f"📞 **Concalls:** {concall_corpus[:200]}")
    if announce_corpus:
        stats_lines.append(f"📋 **Announcements:** {announce_corpus[:200]}")
    if not stats_lines:
        stats_lines = ["_No briefs available for this batch._"]

    embeds.append({
        "title": f"Daily Concall Intelligence — {label}",
        "description": "\n".join(stats_lines) + "\n\n_Full brief attached as PDF below ↓_",
        "color": COLOR_HEADER,
        "footer": {"text": nice_date},
    })

    if concall_md:
        embeds.append({
            "title": "📞 Concall Highlights",
            "description": build_concall_summary(concall_md),
            "color": COLOR_CONCALL,
        })
    else:
        embeds.append({
            "title": "📞 Concall Highlights",
            "description": "_No concall brief generated for this batch._",
            "color": COLOR_EMPTY,
        })

    if announce_md:
        embeds.append({
            "title": "📋 Announcement Highlights",
            "description": build_announcement_summary(announce_md),
            "color": COLOR_ANNOUNCEMENT,
        })
    else:
        embeds.append({
            "title": "📋 Announcement Highlights",
            "description": "_No announcement brief generated for this batch._",
            "color": COLOR_EMPTY,
        })

    return {"username": BOT_NAME, "embeds": embeds}

# ---------- HTTP post ----------
def post(payload: dict, attachments: list[tuple[str, bytes, str]]) -> None:
    if not WEBHOOK_URL:
        raise RuntimeError(
            f"DISCORD_WEBHOOK_URL not set. Add it to {ENV_PATH} or the environment."
        )

    multipart = [("payload_json", (None, json.dumps(payload), "application/json"))]
    for i, (filename, content, mime) in enumerate(attachments):
        multipart.append((f"files[{i}]", (filename, content, mime)))

    resp = requests.post(WEBHOOK_URL, files=multipart, timeout=60)
    if resp.status_code >= 300:
        raise RuntimeError(
            f"Discord webhook failed: HTTP {resp.status_code}\nResponse: {resp.text[:500]}"
        )
    title = payload["embeds"][0]["title"] if payload.get("embeds") else "(no title)"
    print(f"Posted to Discord: {title}")

# ---------- main ----------
def main() -> None:
    parser = argparse.ArgumentParser(description="Post Daily Concall Intelligence to Discord")
    parser.add_argument("batch", choices=["morning", "evening"])
    parser.add_argument("date", nargs="?", help="YYYY-MM-DD (default: today for morning, yesterday for evening)")
    parser.add_argument("--dry-run", action="store_true", help="Build PDF + print payload but do not post")
    parser.add_argument("--no-pdf", action="store_true", help="Skip the PDF attachment (embeds only)")
    parser.add_argument("--save-pdf", action="store_true", help="Also save the PDF to the project folder for inspection")
    args = parser.parse_args()

    if args.date:
        analysis_date = args.date
    elif args.batch == "morning":
        analysis_date = datetime.now().strftime("%Y-%m-%d")
    else:
        analysis_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    if args.batch == "morning":
        concall_path = ANALYSIS_DIR / f"{analysis_date}_morning.md"
        announce_path = ANALYSIS_DIR / f"{analysis_date}_announcements_morning.md"
    else:
        concall_path = ANALYSIS_DIR / f"{analysis_date}_evening.md"
        announce_path = ANALYSIS_DIR / f"{analysis_date}_announcements_evening.md"

    concall_md = concall_path.read_text(encoding="utf-8") if concall_path.exists() else None
    announce_md = announce_path.read_text(encoding="utf-8") if announce_path.exists() else None

    if not concall_md and not announce_md:
        print(f"Both briefs missing or empty for {analysis_date} {args.batch}. Skipping post.")
        sys.exit(0)

    payload = build_payload(args.batch, analysis_date, concall_md, announce_md)

    attachments = []
    if not args.no_pdf:
        print("Rendering PDF...")
        html = build_pdf_html(args.batch, analysis_date, concall_md, announce_md)
        pdf_bytes = render_pdf(html)
        pdf_name = f"Concall_Intelligence_{analysis_date}_{args.batch}.pdf"
        attachments.append((pdf_name, pdf_bytes, "application/pdf"))
        print(f"  PDF generated: {pdf_name} ({len(pdf_bytes) // 1024} KB)")

        if args.save_pdf:
            out = PROJECT_ROOT / pdf_name
            out.write_bytes(pdf_bytes)
            print(f"  Also saved to: {out}")

    if args.dry_run:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print(f"\nWould attach: {[a[0] for a in attachments] or '(no files)'}")
        return

    post(payload, attachments)

if __name__ == "__main__":
    main()
