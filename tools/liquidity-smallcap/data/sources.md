# Data sources, liquidity vs small caps

Written by build_data.py. Raw files are in data/raw/; data/raw/manifest.json records each file's URL and download date.

| File | Value | First | Last | Rows | Source URL | Downloaded | Note |
|---|---|---|---|---|---|---|---|
| net_laf.csv | net_laf_cr | 2023-01-01 | 2026-11-15 | 1380 | https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx (Money Market Operations releases; per-row URL in release_url) | 2026-11-17 | Rs crore. Stored as surplus positive, deficit negative. RBI reports net injection as positive; that sign is flipped here (sign_rule column). |
| cd_3m.csv | cd_3m_pct | 2023-01-02 | 2026-11-09 | 931 | https://www.fbil.org.in/wasdm/cd/fetchfiltered?fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD&authenticated=false | 2026-11-16 | FBIL CD curve, 3-month tenor, % p.a. |
| mtf_book.csv | mtf_combined_cr | 2023-01-02 | 2026-11-13 | 957 | https://indiamtf.com/history/snapshots.json | 2026-11-16 | INR crore, whole-book daily net. BSE values run daily from 2017-07-03 in this file, so no coverage break in the window (indiamtf openapi.json says about 2025-10-15; the data disagrees). |
| nifty_50.csv | close | 2023-01-02 | 2026-11-16 | 953 | https://nsearchives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv | 2026-11-17 | Index close, price return. NSE ind_close_all daily files (NSE Indices publishes niftyindices.com); per-day file URL in the source_url column |
| nifty_smallcap_250.csv | close | 2023-01-02 | 2026-11-16 | 953 | https://nsearchives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv | 2026-11-17 | Index close, price return. NSE ind_close_all daily files (NSE Indices publishes niftyindices.com); per-day file URL in the source_url column |
| nifty_microcap_250.csv | close | 2023-01-02 | 2026-11-16 | 953 | https://nsearchives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv | 2026-11-17 | Index close, price return. NSE ind_close_all daily files (NSE Indices publishes niftyindices.com); per-day file URL in the source_url column |
