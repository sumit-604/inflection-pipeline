# Data gaps, liquidity vs small caps

Status 2026-11-05: no raw file downloaded yet. Every series is NOT FOUND.
build_data.py rewrites this file with day-level gaps once the laptop fetch
in README.md has run.

| Series | Source tried | Result in the cloud shell, 2026-11-05 |
|---|---|---|
| Net LAF, Rs crore | data.rbi.org.in, www.rbi.org.in | NOT FOUND. Policy 403 on direct fetch. Needs a DBIE browser export. |
| FBIL 3M CD rate | www.fbil.org.in | NOT FOUND. Page renders via Firecrawl, but history sits behind the site's date picker. Needs a browser csv export. |
| MTF book NSE+BSE | indiamtf.com/history/snapshots.json | NOT FOUND. Policy 403 direct; CSV blocked by the site's bot check; JSON call denied by the session's auto-mode classifier. |
| Nifty Smallcap 250 | niftyindices.com | NOT FOUND. Policy 403. Yahoo has only ETFs for this index; ETF prices are not index closes, so not used. |
| Nifty Microcap 250 | niftyindices.com | NOT FOUND. Policy 403. No Yahoo symbol. |
| Nifty 50 | niftyindices.com | NOT FOUND. Policy 403. |
