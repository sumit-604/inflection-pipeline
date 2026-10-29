---
name: daily-watchlist-deep-review
description: Reads every Screener watchlist announcement downloaded at 05:00 and writes a deep REVIEW.md tested against the Notion theses.
---

Produce today's deep watchlist announcement review. The operator reads it at 06:00. Every announcement must be read in full and tested against the operator's Notion thesis. Never shallow: the bar is C:\ConcallPipeline\Daily Concall Intelligence\review_spec\STYLE_SAMPLE.md.

BASE = C:\ConcallPipeline\Daily Concall Intelligence
Specs: BASE\review_spec\COMPANY_ANALYST.md (analysts), BASE\review_spec\ASSEMBLER.md (assembler), BASE\review_spec\STYLE_SAMPLE.md (style bar), BASE\review_spec\notion_map.json (Screener name -> Notion page URL, null = not in COMPANIES MASTER).

STEP 1. Find today's folder.
- The Windows task "Watchlist Announcements 0500" runs BASE\fetch_announcements.bat at 05:00. It writes BASE\announcements\<since>_to_<now>\ with INDEX.md and the PDFs, and logs to BASE\fetch_announcements.log (last line "SUMMARY: ...").
- Take the newest folder under BASE\announcements\ whose name ends with today's date. If none exists, or the log shows an error, run `python -u fetch_announcements.py` from BASE once (it resumes from announcements\last_run.txt). If it still fails, write BASE\announcements\REVIEW_FAILED_<today>.md with the log tail and stop.
- If INDEX.md lists 0 announcements, write REVIEW.md in that folder saying "No announcements in the window" and stop.

STEP 2. Prep (mechanical). Run `python prep_review.py "<folder>"` from BASE. It writes text\, page_images\, deep\work\T##.json (in COMPANIES MASTER), deep\work\N##.json (not in master), deep\work\unmapped.json.
- If unmapped.json is not empty: for each name, search Notion (notion-search, the COMPANIES MASTER data source collection://345bb2b9-d3ab-8032-9b46-000ba16ab827) for the company. Add each name to notion_map.json with its page URL, or null if it is not in COMPANIES MASTER. Then re-run prep_review.py. Do not use notion-query-data-sources (the workspace query quota runs out).
- Prices: run `python refresh_prices.py "<folder>"` from BASE, before the analysts start. It reads price, 52-week high / low and market cap for every company from screener.in (NSE, then BSE as backup) and writes deep\prices.json and deep\prices.md. The PRICES line shows refreshed / not_refreshed. Do not use Trendlyne for prices. Check any "found by search" note in prices.md: that name's screener page was matched by search and may be the wrong company; fix it in review_spec\screener_map.json and re-run.

STEP 3. Company analysts, in parallel (max 20 at once; launch more as slots free).
- For each deep\work\T##.json: Agent, subagent_type general-purpose, model opus. Prompt: "Follow exactly: BASE\review_spec\COMPANY_ANALYST.md (read STYLE_SAMPLE.md in the same folder first). Work file: <full path to T##.json>. All relative paths in the work file are under its "root". Write your output to root\<output>."
- For each deep\work\N##.json: same, model sonnet, and add: "These companies are NOT in COMPANIES MASTER (notion_page is null): skip the Notion step, explain each filing properly, and name any cross-link to companies that are on file."
- When all finish, check coverage: every item number in INDEX.md must appear in an items_covered line of some deep\out\*.md. Re-run any group whose items are missing, once.

STEP 4. Write <folder>\deep\notes.md with verified facts: window, announcement / company / PDF / page counts, image-page count, count in vs not in COMPANIES MASTER, the "Key documents" block from INDEX.md (annual reports, transcripts, presentations, meeting notices), duplicate postings, any link that served the wrong company's file, and any tool limits met.

STEP 5. Assembler: Agent, general-purpose, model opus. Prompt: "Follow exactly: BASE\review_spec\ASSEMBLER.md. Run folder: <folder>. Write to that folder's deep\assembly\ (order.json, front.md, back.md)."

STEP 6. Run `python holdings_table.py "<folder>"` from BASE. It writes deep\assembly\holdings.md, the holdings price table (current price, buy price, entry / MoS, stop, trim, exit, bold where a line was crossed since the last run). The HOLDINGS line must show unreadable=0; if not, fix the named levels lines in deep\out\*.md (one-line JSON) and re-run. Then run `python stitch_review.py "<folder>"` from BASE. It writes <folder>\REVIEW.md. The STITCH line must show items_covered N/N and order_names_not_found=[]. If not, fix order.json names and re-run.

STEP 7. Append one line to BASE\review_spec\run_log.md: date, window, announcements, companies, pages, groups (T/N), start and end time, and any problem.

RULES
- Read-only on Notion. Never write, edit or comment in Notion. Never change Decision Status. The operator reads REVIEW.md, then brainstorms and saves to Notion from Claude web (claude.ai). Appendix A is the hand-over for that.
- Never estimate a missing number. NOT FOUND is valid.
- Every reply and report in plain, simple English. Short sentences. No em-dashes.
- Annual reports, concall transcripts and investor presentations are read in full, every page, and listed in the Key documents section.

FINAL MESSAGE (short): the REVIEW.md path; announcements, companies and pages read; prices refreshed / not refreshed; any holding that crossed a stop, trim or exit line; how many material companies; the top five rulings needed, one line each; any problem in the run.