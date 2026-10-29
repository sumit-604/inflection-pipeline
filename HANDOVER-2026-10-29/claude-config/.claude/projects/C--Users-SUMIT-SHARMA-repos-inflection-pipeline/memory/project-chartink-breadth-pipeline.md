---
name: project-chartink-breadth-pipeline
description: "Chartink breadth pipeline built 2026-09-06; \"the 34 CSV files\" means the table tiles of dashboards 133280 and 148889; two schedulers; outputs under data/chartink/analysis"
metadata: 
  node_type: memory
  type: project
  originSessionId: 282c8e93-85a3-470d-a18b-d905c3000257
  modified: 2026-10-16T01:29:45.421Z
---

Built 2026-09-06. When the operator says "the CSV files" or "the 34 CSV files"
they mean the 34 TABLE tiles across Chartink dashboards 133280 (MBM, 16 tiles)
and 148889 (market breadth, 50 tiles); chart tiles have no CSV button and do
not count in their mental model. Files land as
data/chartink/csv/<trade date>/<exact Chartink tile name>.csv.

Two schedulers, on purpose: Windows Task Scheduler "Chartink Daily Collector"
runs tools/chartink/run_daily.bat weekdays 21:00 (needs no app open); Claude
scheduled task chartink-market-read writes the brief weekdays 21:30 (only
while the desktop app is open). Front door: data/chartink/analysis/index.html.
Since 2026-10-01 (operator ruling) the brief task ends by running
tools/chartink/push_data.bat itself, so a late brief pushes the moment it
exists; the 22:15 "Chartink Data Push" Windows job stays as the safety net.
Before this, a brief that ran late missed the 22:15 push and the operator
pushed by hand.

Missed-night race (seen 2026-10-16): when the PC is off at 21:00, Task
Scheduler catches the collector up on next wake, and the Claude brief task
catches up too. On 16 Oct the brief fired at 06:43, the collector at 06:45,
so the brief reread 14 Oct while 15 Oct data landed minutes later. A
morning brief on the old date means: check csv/ for a newer folder, then
write that date's brief by hand.

Chartink API notes not in the code comments: /widget/process needs only a
CSRF token from any page GET, no login, for public dashboards; `limit`
controls grouped-row count (default 75, export gives up to 999), `size`
controls history depth; a ~1.7e308 value is their divide-by-zero sentinel.
pandoc is NOT on this machine; the operator's MarketBriefs PDFs are produced
elsewhere, so briefs render to HTML here.

Tracking, corrected 2026-09-09. The daily CSVs ARE tracked. Each trade date
lands on main as one commit titled `chartink data: <date>` (e.g. 86daad97 for
2026-09-07), carrying the 34 raw CSVs, the facts sheet, the brief, the digest
and the rollup CSVs. A date with no such commit on main has not been ferried,
whatever the working tree shows.

A past date's capture CANNOT be re-fetched. Chartink serves live dashboard
state, so re-running the collector today yields today's data under today's
folder. If a `chartink data: <date>` commit is lost, that date is gone unless
the commit object survives. On 2026-09-08 an external rebase on branch
run/iex-2026-09-08 orphaned commit 74ba79c5 (`chartink data: 2026-09-08`);
it survived only as the tip of the local-only branch rescue/iex-prerebase,
while the recovery commit 6d88e552 restored the IEX stage reports and no
chartink file. Check `git log --all --grep="chartink data"` before ever
concluding a pull did not run.
Brief voice is governed by [[feedback-market-read-narrative]]: plain story, few numbers.

**Screens funnel, 2026-09-06.** screens/cards/<TICKER>.md holds shallow cards.
Bull AI MCP (ace5a2e8...) is on a 100-calls/month plan: search_company_documents
counts, list_document_availability and get_mcp_usage do not; it returns page
citations (docs.bull-ai.in short links) and can read a document by page. Both
cloud indexes lag small-cap annual reports (FY25 only for VALIANTLAB, RUBYMILLS
on Bull AI). Neither holds credit ratings. Collector run for ASMTEC 404'd on
https://www.screener.in/company/ASMTEC/ (slug unresolved). Ruby Mills sold The
Ruby's 33rd floor to Torrent Pharma for Rs 124.08 Cr on 2026-08-19.

**Corpus mechanics learned 2026-09-06 (screens funnel).** docs.bull-ai.in/d/<code>
serves the ORIGINAL PDF with no call cost; codes come from search/chunk results.
BSE announcements API (api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w
with Referer header; strCat=Result or -1) lists filings and
xml-data/corpfiling/AttachLive/<att> serves the PDF. screener.in credit-ratings
block (class "documents credit-ratings") is public; tools/collector/
fetch_ratings.py downloads it; India Ratings and Acuite "connect" pages are JS
shells, render in the browser. screener slug for ASM Technologies is the BSE
code 526433. Bull AI chunk reads cap at ~12 pages per call and OCR garbles
tables. Operator upgraded/will upgrade Bull AI; call count is not a constraint,
but holding the files is (see [[feedback-hold-the-documents]]).
BSE: when xml-data/corpfiling/AttachLive/<att> returns an ~8 KB non-PDF, the same name under AttachHis/ serves the PDF (older filings move to the archive).
