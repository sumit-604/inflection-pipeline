"""
send_newsletter.py — Daily Concall Intelligence email newsletter

Reads the concall brief and announcement brief for a given batch, renders
them as a single HTML email, and sends via Gmail SMTP using credentials
from .env in the same folder.

Usage:
    python send_newsletter.py morning              # uses today's date
    python send_newsletter.py evening              # uses yesterday's date
    python send_newsletter.py morning 2026-05-13   # explicit date
    python send_newsletter.py morning --dry-run    # write HTML to disk, do not send
"""

import os
import sys
import smtplib
import argparse
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from pathlib import Path

# ---------- dependency bootstrap ----------
try:
    import markdown
except ImportError:
    print("Installing 'markdown' package...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

# ---------- paths ----------
PROJECT_ROOT = Path(__file__).parent.resolve()
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
ENV_PATH = PROJECT_ROOT / ".env"

# ---------- .env loader (no external dep) ----------
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

SMTP_HOST = cfg("NEWSLETTER_SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(cfg("NEWSLETTER_SMTP_PORT", "587"))
SENDER_EMAIL = cfg("NEWSLETTER_SENDER_EMAIL")
SENDER_PASSWORD = cfg("NEWSLETTER_GMAIL_APP_PASSWORD")
RECIPIENT_EMAIL = cfg("NEWSLETTER_RECIPIENT_EMAIL")

# ---------- email template ----------
CSS = """
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  max-width: 760px;
  margin: 0 auto;
  padding: 24px 16px;
  color: #1a1a1a;
  line-height: 1.55;
  background: #f7f7f7;
}
.wrap { background: #ffffff; padding: 28px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
.header { border-bottom: 3px solid #1a4d8f; padding-bottom: 14px; margin-bottom: 22px; }
.header h1 { color: #1a4d8f; margin: 0; font-size: 22px; letter-spacing: -0.2px; }
.header .subtitle { color: #666; font-size: 13px; margin-top: 6px; }
.section { margin-bottom: 28px; }
.section-tag {
  display: inline-block; padding: 4px 10px; background: #1a4d8f; color: white;
  border-radius: 4px; font-size: 12px; font-weight: 600; letter-spacing: 0.5px;
  margin-bottom: 10px;
}
.brief h1 { font-size: 19px; color: #1a4d8f; border-bottom: 2px solid #1a4d8f; padding-bottom: 4px; margin-top: 22px; }
.brief h2 { font-size: 16px; color: #1a4d8f; margin-top: 22px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
.brief h3 { font-size: 14px; color: #2a5a9f; margin-top: 16px; }
.brief h4 { font-size: 13px; color: #444; margin-top: 12px; }
.brief blockquote { border-left: 3px solid #c8d4e3; padding: 4px 12px; color: #555; margin: 8px 0; background: #f4f7fb; }
.brief table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 13px; }
.brief th, .brief td { border: 1px solid #ddd; padding: 6px 10px; text-align: left; vertical-align: top; }
.brief th { background: #eef3f9; color: #1a4d8f; font-weight: 600; }
.brief code { background: #f4f4f4; padding: 1px 5px; border-radius: 3px; font-size: 12px; color: #c0392b; }
.brief pre { background: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; font-size: 12px; }
.brief ul, .brief ol { margin: 6px 0 10px 0; padding-left: 22px; }
.brief li { margin: 3px 0; }
.brief strong { color: #1a1a1a; }
.brief hr { border: none; border-top: 1px solid #e0e0e0; margin: 16px 0; }
.empty { color: #999; font-style: italic; padding: 12px; background: #fafafa; border-radius: 4px; }
.footer { margin-top: 28px; padding-top: 14px; border-top: 1px solid #eee; color: #999; font-size: 11px; }
"""

def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists", "nl2br"],
    )

def build_email_html(batch: str, analysis_date: str, concall_md: str | None, announce_md: str | None) -> str:
    label = "MORNING" if batch == "morning" else "EVENING"
    date_obj = datetime.strptime(analysis_date, "%Y-%m-%d")
    nice_date = date_obj.strftime("%A, %B %d, %Y")

    concall_html = (
        f'<div class="brief">{md_to_html(concall_md)}</div>'
        if concall_md
        else '<div class="empty">No concall brief generated for this batch.</div>'
    )
    announce_html = (
        f'<div class="brief">{md_to_html(announce_md)}</div>'
        if announce_md
        else '<div class="empty">No announcement brief generated for this batch.</div>'
    )

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily Concall Intelligence — {label} — {nice_date}</title>
<style>{CSS}</style>
</head>
<body>
  <div class="wrap">
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

    <div class="footer">
      Generated automatically from the Daily Concall Intelligence pipeline.<br>
      Concall framework: v2 &middot; Announcement framework: v1
    </div>
  </div>
</body>
</html>"""

def load_brief(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return None
    return text

def send_email(html: str, subject: str) -> None:
    missing = [
        name
        for name, val in [
            ("NEWSLETTER_SENDER_EMAIL", SENDER_EMAIL),
            ("NEWSLETTER_GMAIL_APP_PASSWORD", SENDER_PASSWORD),
            ("NEWSLETTER_RECIPIENT_EMAIL", RECIPIENT_EMAIL),
        ]
        if not val
    ]
    if missing:
        raise RuntimeError(
            "Missing required configuration: "
            + ", ".join(missing)
            + f"\nAdd them to {ENV_PATH} or your environment."
        )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText("View this newsletter in an HTML-capable email client.", "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print(f"Sent: {subject} -> {RECIPIENT_EMAIL}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Send Daily Concall Intelligence newsletter")
    parser.add_argument("batch", choices=["morning", "evening"])
    parser.add_argument("date", nargs="?", help="YYYY-MM-DD (default: today for morning, yesterday for evening)")
    parser.add_argument("--dry-run", action="store_true", help="Write HTML to outputs/newsletter_preview.html and do not send")
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

    concall_md = load_brief(concall_path)
    announce_md = load_brief(announce_path)

    if concall_md is None and announce_md is None:
        print(f"Both briefs missing or empty for {analysis_date} {args.batch}. Skipping send.")
        print(f"  Expected concall:      {concall_path}")
        print(f"  Expected announcement: {announce_path}")
        sys.exit(0)

    html = build_email_html(args.batch, analysis_date, concall_md, announce_md)

    nice_date = datetime.strptime(analysis_date, "%Y-%m-%d").strftime("%a %d %b %Y")
    subject = f"Concall Intelligence — {args.batch.capitalize()} — {nice_date}"

    if args.dry_run:
        preview = PROJECT_ROOT / f"newsletter_preview_{args.batch}_{analysis_date}.html"
        preview.write_text(html, encoding="utf-8")
        print(f"Dry run: wrote preview to {preview}")
        return

    send_email(html, subject)

if __name__ == "__main__":
    main()
