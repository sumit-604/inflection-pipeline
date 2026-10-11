#!/usr/bin/env python3
"""URL liveness check for /step1 identity resolution (operator ruling 2026-10-11).

Replaces the model doing the HTTP 200 check by hand. No model, no third-party
packages, runs the same on Windows and Linux.

Usage:  python3 tools/check_url.py <url> [<url> ...]

Prints one line per URL:
  OK   <status> <final url>  title="<page title>"
  FAIL <status or error> <url>  <what to do>
A 200 whose title contains "404" or "Page Not Found" is a FAIL (screener
serves its not-found page with a 200), and so is a 200 bot-challenge page.
Exit 0 when every URL is OK, 1 otherwise.
"""
import re
import sys
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
DEAD_TITLE = re.compile(r"404|page not found", re.I)
# Bot walls answer 200 with a challenge page; the real page was never seen.
CHALLENGE_TITLE = re.compile(r"client challenge|just a moment|attention required|captcha|access denied", re.I)


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            status, final = r.status, r.geturl()
            body = r.read(200_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return False, f"FAIL {e.code} {url}  Try the other URL variant (standalone /company/<TICKER>/ or the BSE code)."
    except Exception as e:
        return False, f"FAIL {type(e).__name__} {url}  Check network access, then rerun: python3 tools/check_url.py {url}"
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    if status != 200 or DEAD_TITLE.search(title):
        return False, f'FAIL {status} {final}  title="{title}"  Try the other URL variant (standalone /company/<TICKER>/ or the BSE code).'
    if CHALLENGE_TITLE.search(title):
        return False, f'FAIL challenge {final}  title="{title}"  A bot wall answered, not the page. Open the URL in a browser to confirm it loads.'
    return True, f'OK   {status} {final}  title="{title}"'


def main(urls):
    if not urls:
        print(__doc__.strip())
        return 2
    ok_all = True
    for u in urls:
        ok, line = check(u)
        ok_all = ok_all and ok
        print(line)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
