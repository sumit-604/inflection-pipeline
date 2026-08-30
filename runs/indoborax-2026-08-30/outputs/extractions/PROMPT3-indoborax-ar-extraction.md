> SUPERSEDED 2026-08-30 by PROMPT3-indoborax-ar-fy24-fy25.md once AR FY24/FY25 were uploaded. This file was the corpus-limited answer written when only the FY26 AR was held. Kept for the record.

# FERRY-BACK — PROMPT 3 (Indo Borax AR FY24 / AR FY25) + standing ROCE item

Answered by Claude Code, 2026-08-30, against the INDOBORAX run corpus.
Rules honoured: corpus only; quote-then-comment; filename + page anchor; no estimates; conflicts quoted both sides.

---

## GAP NOTICE (read first — it governs everything below)

PROMPT 3 names two source documents: **Indo Borax AR FY2023-24** and **AR FY2024-25**.
**Neither is in the run corpus.** The only Indo Borax annual report held is
**AR FY2025-26** (file `Annual_Report_2023.pdf` — the 2023 filename is wrong; the
content is the 45th AGM, year ended 31-Mar-2026). This was flagged as
`input_gaps: annual_report_fy24_fy25` on every block of the run.

Consequences, before any answer:
- The FY26 AR carries **FY26 figures with FY25 as the comparative column only**. It
  never reaches FY24. So every FY24-specific item, and every disclosure unique to
  the FY25 standalone AR (AGM Q&A, FY25 Directors' Report narrative), is **NOT IN
  CORPUS**, not "NOT DISCLOSED".
- To answer PROMPT 3 as written, push **AR FY24 and AR FY25** to
  `runs/indoborax-2026-08-30/inputs/annual-report/` (collect_to_repo.py) and re-issue.

What the FY26 AR *can* serve is below, FY26 with FY25 comparative, clearly labelled.

---

## 3A — CAPACITY, PRODUCTION, VOLUME  → NOT IN CORPUS (and not in the FY26 AR either)

Full-text search of the FY26 AR (157 pages) returns **no** "installed capacity",
"actual production", or product-wise quantity/value table in the Directors' Report or
elsewhere. The FY26 AR discloses no tonnes-sold, no nameplate MT, no utilisation %.

> Comment: the only filed volume/capacity figures for Indo Borax in the whole corpus
> live in the rating report, not the AR: "Boric acid sales volumes increased to around
> 15,365 MT in FY26 (FY25: 14,296 MT)... DOT volumes to around 983 MT in FY26 (FY25:
> 679 MT)" (rating.pdf p.2, India Ratings 23-Jul-2026). Boric-acid nameplate 20,000
> MTPA and DOT 6,000 MTPA appear in the investor presentation and concall, not the AR.
> Items 3A-1 through 3A-6 for FY24 and FY25 are **NOT IN CORPUS**; for FY26 the AR
> itself is silent — **NOT DISCLOSED in the AR**.

## 3B — LITHIUM HYDROXIDE (your highest priority)  → ZERO in corpus

The token **"lithium" appears 0 times** in the FY26 AR (full 157-page text search).
No mention of lithium, lithium hydroxide, or lithium hydroxide monohydrate anywhere.

> Comment: there is no withdrawal/deprioritisation statement, no lithium revenue,
> volume, capacity, or capex, and no impairment/reclassification of any lithium asset
> in the one AR held. Any such statement — if it exists — is in the FY24 or FY25 AR,
> or an AGM Q&A, none of which are in corpus. Items 3B-7 through 3B-10 are
> **NOT ANSWERABLE from corpus.** This is the single strongest reason to push the
> FY24/FY25 ARs: the lithium exit is a pre-transition baseline fact and it is invisible
> in the FY26 AR.

## 3C — BORON OXIDE  → partial (one forward mention in the FY26 AR)

> "Second, we are investing approximately Rs. 20 crore in a new Boron Oxide facility at
> Pithampur with a planned capacity of 4,000 MTPA, enabling us to move further up the
> value chain into higher-margin Boron chemistry products." — Annual_Report_2023.pdf
> (FY26 AR), **printed p.2**, Message from the Managing Director & CEO.

> Comment: this is a forward *intent*, not a commissioned line. Stages B03/B07 record a
> separate FY26 Board's-Report line stating boron oxide was "successfully introduced...
> in July 2025" (AR printed p.25), which **contradicts** the CEO on the 02-Jun-2026 call
> ("still a project which is going on", concall p.8) and the rating report's FY29
> commercial-operations date (rating.pdf p.2). Both sides quoted; not reconciled. No
> boron-oxide capacity/production/sales volume and **zero matching CWIP or capex** sit
> in the FY26 accounts (B03 Phase 6E). **3C-12 (first year boron oxide enters the
> portfolio): NOT IN CORPUS** — establishing "first appearance" needs the FY24/FY25 ARs.

## 3D — EXPORTS AND OTHER TREND ITEMS  → FY26 + FY25 answerable; FY24 NOT IN CORPUS

**13/14 — Foreign exchange earnings and outgo (exports Nil).** Verbatim, FY26 AR
printed p.33, section "C. Foreign Exchange Earnings and Outgo" (Rs In Lakhs):

> | Particulars | 2025-26 | 2024-25 |
> | Inflow  | —       | —       |
> | Outflow | 6625.52 | 9626.55 |

> Comment: **export (foreign-exchange inflow) is Nil in both FY26 and FY25**, quoted
> from the em-dash cells. Outflow Rs 66.26 cr (FY26) and Rs 96.27 cr (FY25) — imported
> ore plus other forex outgo. FY24 (the FY24 AR's 2023-24/2022-23 columns): **NOT IN
> CORPUS.**

**15 — Technology Absorption / R&D.** Verbatim, FY26 AR printed p.33:

> "1. Research & Development — The Company continues to lay special emphasis on
> conservation of energy... The Company has no specific Research & Development
> Department. However, in-house quality control facilities are utilized for product and
> process improvement and updation. 2. Technology Absorption — The Company has not
> imported any new technology."

> Comment: "**no specific Research & Development Department**" is the FY26-AR fact. It
> **contradicts** the same AR's MD&CEO letter (p.2): "we will increase our investment in
> research and development to create specialised boron-based solutions." Both quoted; not
> reconciled. FY24/FY25-AR wording of this section: **NOT IN CORPUS.**

**16 — Revenue / EBITDA / PBT / PAT.** Verbatim, FY26 AR printed p.2 (MD&CEO letter):

> "Operating revenue grew by 22.9% to Rs. 215.45 crore, while consolidated net profit
> increased by 18.3% to Rs. 50.27 crore. Earnings per share reached Rs. 15.67... EBITDA
> and PAT margins remained robust at approximately 20.5% and 21.8%, respectively. Our
> performance accelerated further in the fourth quarter, with revenue growing 25.7% and
> net profit rising 41.9% year-on-year."

> Comment: the "**margins remained robust**" claim is the one B03 flags against the
> MD&A's own margin table (compression) and standalone pre-exceptional PBT falling 3.75%
> YoY; the 18.3% profit growth is lifted by the Rs 10.15 cr exceptional gain on RPT asset
> sales. Exact PBT/PAT rupee lines sit in the P&L (results filing / B02-B03), FY26 vs
> FY25 only. FY24 comparative: **NOT IN CORPUS.**

**17 — Capex.** FY26 AR p.2 states the Rs 20 cr / 4,000 MTPA boron-oxide *intent*
(quoted above). B03/B07: **zero capex/CWIP incurred** against it in FY26. rating.pdf p.2
gives a ~Rs 90 cr FY27-28 total-capex plan (FY29 start) — **not in the AR**. FY24/FY25
capex announced or incurred: **NOT IN CORPUS.**

**18 — Managerial remuneration + ratio to median.** Verbatim, FY26 AR printed p.40,
Annexure II (Section 197(12)), "for the Financial Year 2025-26":

> Suresh Kalra (MD & CEO, w.e.f. 23-Jan-2026): Ratio "-", % change "-" (not comparable,
> part-year). Harsh Malhotra (ED, w.e.f. 23-Jan-2026): Ratio "-", "-". Sajal Jain (MD &
> CFO, upto 23-Jan-2026): Ratio **33.48%**, % change **-0.68%** (computed to 23-Jan-2026).
> Govind Parmar (ED, upto 23-Jan-2026): Ratio **4.57%**, **+10.88%**. Median-remuneration
> increase FY26: **13%**. Permanent employees at 31-Mar-2026: **111**. Avg increase
> non-managerial 7.29% vs managerial 2.08%.

> Comment: FY26 spans both promoter regimes (Jain family out 23-Jan-2026). Per-director
> figures from the FY24 and FY25 standalone ARs, and their ratios to median in those
> years: **NOT IN CORPUS.**

---

## VERIFICATION LINE (PROMPT 3)

- Document actually read: `Annual_Report_2023.pdf` = Indo Borax & Chemicals Annual
  Report **FY2025-26**, 45th AGM, year ended 31-Mar-2026, filed 21-May-2026.
- Pages quoted: printed **p.2** (MD&CEO letter: revenue/EBITDA/PAT, boron-oxide intent,
  R&D intent), printed **p.33** (Conservation of Energy / Technology Absorption / R&D /
  Foreign Exchange table), printed **p.40** (Annexure II remuneration ratios).
- Documents required but **NOT IN CORPUS**: Indo Borax AR FY2023-24, AR FY2024-25.
  Sections 3A (capacity/production), 3B (lithium — 0 mentions in the AR held), 3C-12
  (first-appearance year), and every FY24 figure cannot be answered until these are
  pushed.

---

## STANDING ITEM — INDOBORAX ROCE definitional gap (Pillar 1)

From corpus, the gap is confirmed to be the **treatment of the treasury book in capital
employed**, exactly as suspected:

- Filed ratio, verbatim source: AR FY26 **Note 45 (printed p.113)** reports the
  company's own "Return on Capital Employed" at **17.13% (FY26) / 17.28% (FY25)** — this
  is the 17% the pipeline used and the forum model reproduces.
- B04 (business model) finds **~46% of total assets sit in current mutual-fund
  investments alone** (AR Balance Sheet p.84, Note 9 p.98), on top of cash. B01
  `data_notes`: pre-FY25 capital-employed used Net Worth + Borrowings (borrowings ≈ Nil).
- The filed 17% puts the **entire non-operating treasury book (mutual funds + cash) in
  the denominator**. The forum's ~35-38% "ROIC" strips it out. That single choice is the
  whole 17% → ~38% gap; there is no operating-margin disagreement underneath it.

> Flag for Pillar 1 (I observe, I do not set the base): for a converter, the operating
> return is the one Section 1B Pillar 1 wants. INDOBORAX's filed ROCE understates
> operating returns because roughly half its balance sheet is a non-operating treasury
> book. The same denominator question decides the KRONOX 32% vs 70% split. **Resolve the
> cash/investments-in-capital-employed convention once, apply it identically to both
> names, before setting either Pillar 1 base.** I cannot resolve the KRONOX side here —
> no Kronox document is in this container.

---

## PROMPTS 1 and 2 (Kronox RHP, Kronox AR FY24) — NOT ANSWERABLE HERE

This container holds **no Kronox documents** (no RHP, no Kronox AR FY24) and I cannot
read the separate "Kronox Lab Science" web thread — it is a different conversation with
no shared filesystem. To have Claude Code answer Prompts 1 and 2, push the Kronox RHP
(June 2024) and Kronox AR FY2023-24 into a run folder here. Otherwise answer them in the
Kronox thread, where those PDFs already live.
