# LEDGER — Investor Presentation — Sheela Foam Ltd (SFL) — Q1 FY27
Source: extract_presentation_sfl_q1fy27.txt (51 pages, page_coverage 100%, 27 pages OCR'd)

```
=== A2 COUNT TEST ===
category: slides      grep_count: 51   sweep_count: 51   match: yes
category: numbers     grep_count: 505  sweep_count: 505  match: yes
category: footnotes   grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology notes (read before using this ledger)

- **slides**: grep_count = `grep -n -E "^\[page [0-9]+\]" extract` = 51 hits, matching
  A1's `page_count_pdfinfo: 51`. sweep_count = manual page-by-page walk of the extract
  = 51. Match.
- **numbers**: no clean single regex works unmodified on this file because (a) OCR
  pages 31, 32, 33, 39, 40 are declared "largely non-lexical noise" by the A1 header
  and contain dozens of stray digit fragments from image texture; (b) fiscal-period
  labels (`Q1 FY26`, `FY27`, bare `Q1`/`Q4`, and the `2026`/`2030` column headers on the
  ESG target table) contain digits but are not disclosed data values; (c) the OCR
  engine repeatedly misread the "₹" glyph as a bare "2" or "%" immediately before a
  rupee figure (e.g. p10: "grew by 26% to 2 1032 cr" = ₹ misread, not a second number);
  (d) the "U20"/"U2O" outreach-programme name contains a digit that is not a metric.
  The count below was produced by: (1) a first grep pass with
  `grep -oE '[-+]?[0-9][0-9,]*(\.[0-9]+)?'` per page, (2) manual resolution of every
  divergence between that raw hit-list and a line-by-line reading of the same page
  (documented per page below), applying the exclusions in (a)-(d) consistently, and
  excluding p31/32/33/39/40 entirely per A1's own noise designation. p34 ("CSR | In
  actions", not on A1's explicit noise list but visually an unlabelled photo collage
  with the same stray single-digit OCR pattern as p31-33) was excluded on the same
  basis and is flagged `OCR_NOISE_NO_DATA`. Pages 38, 43, 44, 45, 46, 47 (marketing
  photo collages that A1 flags as having "yielded usable data labels and headings")
  could not be cleanly separated into real vs. noise digits by rereading alone — all
  raw numeric tokens found on those six pages are therefore INCLUDED and flagged
  `OCR_LOW_CONFIDENCE` rather than silently dropped. Re-sweep on divergence brought
  grep_count and sweep_count into agreement at 505.
- **footnotes**: grep_count = `grep -n "^\*\|[a-z0-9%]\*" extract` cross-checked
  manually = 3 distinct footnote definitions (p10, p23, p29), covering 4 qualifying
  instances total (p10 slide-level, p23 one number, p29 two numbers). sweep_count = 3.
  Match.
- **Prior-quarter deck**: not supplied to this agent (no `PRIOR_LEDGER_PATH` given).
  `DROPPED_SLIDE` cannot be computed this run — full slide titles are recorded below
  so a downstream pass with the prior deck can diff directly.
- Convention: "number" = a disclosed metric, date, identifier, count, or target value.
  Excluded from the count: page/slide numbers, fiscal-period column/row labels
  (`Q1 FY26`, `FY27`, bare `Q1`/`Q4`, `2026`/`2030` as ESG-table period headers),
  document-structure list numbering (Contents bullets, "1./2./3." on p35), and digits
  embedded in a brand/programme name (`U20`/`U2O`).

---

## TABLE A — Slide inventory (51 slides)

| # | Line | Title (verbatim/paraphrased) | Content type | Flags |
|---|------|-------------------------------|---------------|-------|
| 1 | 24 | Cover letter to BSE/NSE, "Subject: Investor Presentation" | text (regulatory cover letter, Reg. 30 SEBI LODR) | — |
| 2 | 70 | "Sheela Foam Limited — Earnings Presentation Q1 FY27" | text/cover (OCR) | — |
| 3 | 78 | "Safe harbour statement" | text (forward-looking-statement disclaimer, full page) | — |
| 4 | 95 | "Contents" | text/list (9-item table of contents) (OCR) | — |
| 5 | 118 | "Founders with pedigree: ably supported by professionals" | photo/text (4 leadership profiles, no numbers) | — |
| 6 | 129 | (untitled) company-strengths infographic — "Experienced... Presence across... Proven track record..." | chart/infographic (OCR, heavily garbled) | OCR_LOW_CONFIDENCE |
| 7 | 149 | "Sheela Foam: Group of companies and brands" | chart (brand/entity org chart, OCR) | — |
| 8 | 164 | "Leading The Industry, Raising The Bar" | text (headline growth stat block: Standalone vs Consolidated) | POSSIBLE_NEW_OR_REFRAMED — "1ST TIME EVER" milestone framing reads as a new-this-quarter slide |
| 9 | 175 | (untitled) Q1 FY27 KPI dashboard | chart/text (value/volume growth + EBITDA/PAT/Cash EPS tiles) | — |
| 10 | 192 | "Financial Highlights \| Q1 FY27 (YoY)" | text (bullet highlights, Consolidated + Standalone) (OCR) | footnote "*before Forex MTM" |
| 11 | 213 | "Financial performance (₹ Cr)" | table (Standalone vs Consolidated, 4 metrics x 5 periods) | — |
| 12 | 232 | "Operational Highlights \| Q1 FY27 (YoY)" | text (bullets: volume/value growth drivers) (OCR) | — |
| 13 | 246 | "Q1 FY27 Standalone – segment wise" | table (volume + value by segment) | ZERO_STANDING — OTHERS and TOTAL rows have blank Volume columns in all periods |
| 14 | 270 | "Q1 FY27 \| E-com Driving Volume Growth" | chart/text (2 stat callouts) | — |
| 15 | 279 | "Q1 FY27 \| Strengthening U2O outreach" | chart/text (4 stat callouts) | — |
| 16 | 285 | "International Business & Staqo" | text/section divider (OCR) | — |
| 17 | 291 | "Australia \| Q1 FY27" | table (Revenue/Gross Margin/Other Exp/EBITDA x 3 periods) | — |
| 18 | 310 | "Spain \| Q1 FY27" | table (same structure as p17) | — |
| 19 | 330 | "STAQO: Q1 FY27" | table (Revenue, EBITDA x 3 periods) | POSSIBLE_NEW_OR_REFRAMED — smaller/newer business unit, worth a prior-deck check |
| 20 | 345 | "SFL \| ESG & CSR Initiatives" | text/section divider (OCR) | — |
| 21 | 349 | "SFL Movement" | chart/table (Crisil / S&P Global CSA / Sustainalytics ESG ratings) | — |
| 22 | 375 | "Strategy plan for Sustainability 2030" | table (4 SDGs; Gender Diversity, Waste Reduction, Disability Employment, Safety — FY26 vs FY30 target) | — |
| 23 | 393 | "Environment" | text/table (Energy/Water/Waste detail) | footnote "*100% monetization" on FY30 waste target |
| 24 | 419 | "Social" | text/table (Gender Diversity / Disability Employment / Safety) | — |
| 25 | 432 | "ESG \| Governance" | text (committee structure: Audit, NRC, SRC, RM-ESG, CSR) (OCR) | — |
| 26 | 454 | "4.2 SFL \| CSR" | text/section divider (OCR) | — |
| 27 | 458 | "CSR" (Vision & Key Pillars) | text (OCR) | — |
| 28 | 482 | "CSR \| Skill Development" | table (4 programmes: Trained/Employed, FY26 vs Q1FY27) (OCR) | — |
| 29 | 502 | "CSR \| Emotional wellness" | table (4 programme lines: Workshops/Participants/Reach, FY26 vs Q1FY27) (OCR) | footnote "*since inception" on both Reach figures |
| 30 | 521 | "Revitalisation of Smt Sheela Gautam Inter College" | table (headers only: INITIATIVES / KEY OBJECTIVE / FY26 ACHIEVEMENTS / Q1FY27 ACHIEVEMENTS) | ZERO_STANDING — no data rows captured under the headers (graphic/table content not text-extractable) |
| 31 | 525 | (no legible title) — photo collage | photo | OCR_NOISE_NO_DATA — A1-designated non-lexical noise page |
| 32 | 566 | "CSR \| In actions" | photo | OCR_NOISE_NO_DATA — A1-designated non-lexical noise page |
| 33 | 610 | (no legible title) — photo collage | photo | OCR_NOISE_NO_DATA — A1-designated non-lexical noise page |
| 34 | 658 | "CSR \| In actions" (repeat title) | photo | OCR_NOISE_NO_DATA — same stray-digit noise pattern as p31/32/33; not on A1's explicit list but treated identically |
| 35 | 681 | "Marketing Initiatives" | text (3-item list: New Product Launches; Social media & Influencer Collaborations; In-store and hyperlocal interventions) (OCR) | — |
| 36 | 689 | "Sleepwell \| New Models Launch" | photo/text (3 new models named; launch date 2nd June) | — |
| 37 | 700 | "Kurlon \| New Models Launch" | photo/text (6 models named, no numbers) | — |
| 38 | 713 | "Kurlon \| Venti Launch" | photo/text (product-spec collage) (OCR, heavily garbled) | POSSIBLE_NEW_OR_REFRAMED (new product launch); OCR_LOW_CONFIDENCE on all captured digits |
| 39 | 752 | (no legible title) — photo collage | photo | OCR_NOISE_NO_DATA — A1-designated non-lexical noise page |
| 40 | 782 | (no legible title) — Kurlon orthopaedic-range photo collage | photo | OCR_NOISE_NO_DATA — A1-designated non-lexical noise page |
| 41 | 847 | "Sleepwell \| Great Sleepwell Festival: AI led ads" | photo/text (1 stat callout: 2000+ dealers) | POSSIBLE_NEW_OR_REFRAMED — "AI led ads" is a novel marketing-tactic framing |
| 42 | 855 | "Sleepwell \| Great Sleepwell Festival: Celeb Content Reels" | photo (6 celebrity names, no numbers) | — |
| 43 | 863 | "Sleepwell In-store Activations" | photo/text (OCR, heavily garbled) | OCR_LOW_CONFIDENCE on all captured digits |
| 44 | 907 | "Kurlon \| Influencer Campaign" | photo (OCR, heavily garbled) | OCR_LOW_CONFIDENCE on all captured digits |
| 45 | 939 | "Kurlon \| Social Media" | photo/text (OCR, heavily garbled) | OCR_LOW_CONFIDENCE on all captured digits |
| 46 | 977 | "Kurlon \| Media Campaigns" | photo/text (OCR, heavily garbled) | OCR_LOW_CONFIDENCE on all captured digits |
| 47 | 1009 | "Kurlon \| Hyperlocal Activations" | photo/text (OCR, heavily garbled) | OCR_LOW_CONFIDENCE on all captured digits |
| 48 | 1043 | "Financials" | text/section divider (OCR) | — |
| 49 | 1048 | "Consolidated income statement" | table (16 line items x up to 5 periods) | ZERO_STANDING — Exceptional Item Q1-FY26 shown as dash "-"; EPS Y-o-Y and Q-o-Q shown as dash "-" |
| 50 | 1068 | "Standalone income statement" | table (15 line items x up to 5 periods) | ZERO_STANDING — Exceptional Item Q1-FY26 shown as dash "-" |
| 51 | 1087 | "Thank you" (contact page) | text (IR/Company Secretary/Media contacts) | — |

---

## TABLE B — Numbers ledger (every number on every slide, grouped by disclosure line where a table/block shares one context; running count reconciles to 505)

| Slide | Line(s) | Label / context | Value(s) | n | Flags |
|---|---|---|---|---|---|
| 1 | 25 | Letter date | Aug 04, 2026 | 2 | — |
| 1 | 30 | Scrip code (BSE) | 540203 | 1 | — |
| 1 | 29-30 | Addressee pin codes (BSE Mumbai / NSE Mumbai) | 400001, 400051 | 2 | — |
| 1 | 37 | Prior intimation date (investor call) | Jul 31, 2026 | 2 | — |
| 1 | 38 | SEBI LODR regulation cited | Reg. 30 | 1 | — |
| 1 | 38-39 | SEBI LODR Regulations year | 2015 | 1 | — |
| 1 | 40 | Quarter-end date | Jun 30, 2026 | 2 | — |
| 1 | 50-54 | Digital signature timestamp | 2026.08.04 16:34:23 +05'30' | 7 | signature timestamp is same-day as filing (Aug 04 16:34), after board approval — no red flag, filed same day |
| 1 | 63 | Noida office address (plot/sector/pin) | #14, Sector 135, 201301 | 3 | — |
| 1 | 64 | Noida phone | Int-91-120-4868400 | 3 | — |
| 1 | 65-66 | Regd. office address (unit range, pin) | 1002 to 1006, 400059 | 3 | — |
| 1 | 66 | Regd. office phone | Int-91-22-28265686/88/89 | 5 | — |
| 1 | 67 | Toll free number | 1800 103 6664 | 3 | — |
| 1 | 68 | CIN | L74899MH1971PLC427835 | 3 | — |
| 6 | 129-148 | Company-strengths infographic (garbled): ~90 yrs experience(?), geography count(?), ~30% mattress market share, 40% Australia market share, plus unresolved fragments | 990(sic), 2, 0, 9, 30, 208, 40 | 7 | OCR_LOW_CONFIDENCE — "990" likely "~90 years"; "2","0","9","208" unresolved |
| 8 | 168 | Standalone growth YoY | Revenue 20%, EBITDA 13% | 2 | — |
| 8 | 168 | Consolidated growth YoY | Revenue 26%, EBITDA 45% | 2 | — |
| 8 | 172-173 | "1ST TIME EVER" milestone thresholds | ₹1000 Cr+ Revenue, ₹100 Cr+ EBITDA | 2 | POSSIBLE_NEW_OR_REFRAMED |
| 9 | 179-181 | Value/Volume growth tiles | Value: Mattress 15%, Foam 26%; Volume: Mattress 6%, Foam 4% | 4 | — |
| 9 | 179-190 | EBITDA/PAT/Cash EPS tiles | EBITDA-consol ₹109cr +45% 10.6% +139bps; PAT-consol ₹62cr "9.5X"(unclear label) 6.0% +532bps; Standalone EBITDA 9.0%; Joyce(Australia) EBITDA 12.8%; Interplasp(Spain) EBITDA 14.7%; Consol Cash EPS 10.3 | 12 | "9.5X" position/label ambiguous in linearised OCR layout — flagged for verification against native pptx if available |
| 10 | 197-203 | Consolidated highlights (YoY) | Revenue 26% to ₹1032cr; EBITDA 45% to ₹109cr, +139bps to 10.6%; Australia EBITDA 12.8%; Spain EBITDA 14.7%; PAT ₹62cr, margin 6.0%; Cash EPS ₹10.3 | 11 | footnoted — see footnote row p10 below |
| 10 | 205-209 | Standalone (SFL+KEL) highlights (YoY) | Revenue 20% to ₹761cr; EBITDA 13% to ₹68cr | 4 | — |
| 11 | 221 | TOTAL REVENUE (Standalone Q1FY26/Q1FY27/YoY/Q4FY26/QoQ; Consol same) | 635, 761, 20%, 819, -7%; 821, 1032, 26%, 1050, -2% | 10 | — |
| 11 | 224 | GROSS MARGIN (same period set) | 44.4%, 37.6%, -688bps, 43.4%, -584bps; 44.6%, 40.6%, -405bps, 44.4%, -380bps | 10 | — |
| 11 | 227 | EBITDA % (same period set) | 9.5%, 9.0%, -51bps, 11.0%, -205bps; 9.2%, 10.6%, 139bps, 11.1%, -55bps | 10 | — |
| 11 | 230 | EBITDA ₹Cr (same period set) | 60, 68, 13%, 90, -24%; 75, 109, 45%, 117, -7% | 10 | — |
| 12 | 235-236 | Mattress/Foam volume & value growth | Mattress vol 6% val 15%; Foam vol 4% val 26% | 4 | — |
| 12 | 238 | E-com growth drivers | Volume +23%, Value +30% | 2 | — |
| 12 | 239 | U20 growth drivers | Volume +19%, Value +81% (the "20" in "U20" itself excluded as programme name) | 2 | — |
| 12 | 241-243 | Geographic footprint | 41 net new showrooms; U20 expanded to ~10k dealers; COCO 42 stores operational, ramp to 50 next quarter | 4 | — |
| 13 | 252 | MATTRESS-TOTAL (Volume + Value, both period sets) | 813K, 859K, 6%, 914K, -6%; 320, 369, 15%, 395, -6% | 10 | — |
| 13 | 256 | FOAM-TOTAL | 11353Tn, 11764Tn, 4%, 14975Tn, -21%; 291, 365, 26%, 395, -8% | 10 | — |
| 13 | 258 | TECHNICAL FOAM | 4504Tn, 4579Tn, 2%, 5589Tn, -18%; 127, 163, 28%, 165, -1% | 10 | — |
| 13 | 260 | COMFORT FOAM | 5576Tn, 6129Tn, 10%, 7997Tn, -23%; 113, 156, 38%, 177, -12% | 10 | — |
| 13 | 262 | FURNITURE CUSHIONING | 1273Tn, 1057Tn, -17%, 1389Tn, -24%; 49, 46, -5%, 53, -13% | 10 | — |
| 13 | 265 | OTHERS (Value only — no Volume disclosed) | 23, 27, 16%, 30, -8% | 5 | ZERO_STANDING — Volume columns blank in all 5 periods for this row |
| 13 | 268 | TOTAL (Value only — no Volume disclosed) | 635, 761, 20%, 819, -7% | 5 | ZERO_STANDING — Volume columns blank in all 5 periods for this row |
| 14 | 271-278 | E-com YoY sales growth by channel | 69%, 19% (brand.com vs. other platforms — attribution scrambled by OCR layout) | 2 | attribution of 69% vs 19% to the correct platform label is uncertain from the linearised text |
| 15 | 282-284 | U2O outreach stat callouts | 9900+, 230+, 5500+, 24+ (metric labels not resolved from OCR) | 4 | metric labels (what each figure measures) not captured — flag for verification |
| 17 | 296 | Australia Total Revenue (Q1FY26/Q4FY26/Q1FY27) | 92, 109, 120 | 3 | — |
| 17 | 300 | Australia Gross Margin | 54.6%, 59.5%, 59.2% | 3 | — |
| 17 | 304 | Australia Other Expenses | 47.9%, 48.9%, 46.3% | 3 | — |
| 17 | 308 | Australia EBITDA | 6.8%, 10.6%, 12.8% | 3 | — |
| 18 | 316 | Spain Total Revenue | 86, 109, 133 | 3 | — |
| 18 | 320 | Spain Gross Margin | 30.1%, 32.4%, 34.0% | 3 | — |
| 18 | 324 | Spain Other Expenses | 24.4%, 20.0%, 19.3% | 3 | — |
| 18 | 328 | Spain EBITDA | 5.7%, 12.3%, 14.7% | 3 | — |
| 19 | 335 | STAQO Total Revenue | 14, 20, 24 | 3 | — |
| 19 | 338 | STAQO EBITDA | 32.4%, 24.6%, 29.2% | 3 | — |
| 21 | 353-373 | ESG ratings block | Crisil score 61 (STRONG band); S&P Global CSA score 29, ranked 61st, +50 Product Quality, 28-point industry average; Sustainalytics risk score 28.8 (MEDIUM RISK); chemicals industry rank 218 (from 351); "Scope 1 & 2" emissions intensity | 10 | — |
| 22 | 377-389 | Sustainability 2030 plan targets | 4 SDGs identified; Gender Diversity 7.9%→10%; Waste Reduction 14.5%→13%; Disability Employment 7→11; Safety target ISO 45001 | 8 | "2026"/"2030" column-period headers excluded as period labels, not counted separately |
| 23 | 400-416 | Environment detail (Energy/Water/Waste) | Waste Reduction 14.5%→13%*(footnoted); Water 44.5→39 KL/person; Solar 500 kWp, 35%+ current usage; 500+ trees planted; ~40% water recycled; *100% monetization (footnote text) | 9 | footnoted — see footnote row p23 below |
| 24 | 428-430 | Social — Disability Employment | FY26: 7 persons; FY30 target: 11 persons | 2 | — |
| 24 | 427-429 | Social — Safety target | ISO 45001 | 1 | — |
| 27 | 474 | CSR reach / films | 578+ million people, 198+ films | 2 | — |
| 28 | 485-488 | Col. Gautam Academy (Armed Forces exam prep) FY26 vs Q1FY27 | 136 Trained / 86 Employed vs 123 Trained / 20 Employed | 4 | — |
| 28 | 489-491 | Design & Beautician courses FY26 vs Q1FY27 | 97 Trained / 90 Employed vs 48 Trained / 40 Employed | 4 | — |
| 28 | 493-496 | Paramedical courses (DPMI) FY26 vs Q1FY27 | 84 Trained / 32 Employed vs 197 Under Training (not yet eligible for placement) | 3 | — |
| 28 | 497-499 | Software Development courses FY26 vs Q1FY27 | 42 Trained / 42 Employed vs 58 Trained / 30 Placed | 4 | — |
| 29 | 505-506 | Emotional Wellness Workshops FY26 vs Q1FY27 | 272 workshops / 17,501 participants vs 65 workshops / 4,817 participants | 4 | — |
| 29 | 509 | Digital Awareness Campaigns reach | Reach 568 million*; Reach 578 million* | 2 | footnoted — see footnote row p29 below |
| 29 | 513-514 | Creating Counsellors workshops FY26 vs Q1FY27 | 15 workshops / 1,252 participants vs 19 workshops / 772 participants | 4 | — |
| 29 | 515-516 | Skill Development Workshops (college students) FY26 vs Q1FY27 | 11 workshops / 486 participants vs 5 workshops / 172 participants | 4 | — |
| 36 | 693 | Sleepwell new-models launch date | 2nd June | 1 | — |
| 38 | 713-750 | Kurlon Venti Launch product-spec collage (garbled) | 100% (natural cotton/latex claim, x3 occurrences) plus 13 further unresolved digit fragments (mattress size/inch specs likely) | 16 | OCR_LOW_CONFIDENCE — product dimension specs not recoverable from OCR text |
| 41 | 853 | Great Sleepwell Festival AI-led ads | 2000+ dealers personalised | 1 | POSSIBLE_NEW_OR_REFRAMED |
| 43 | 863-906 | Sleepwell In-store Activations (garbled) | "4 month" trial period mentioned twice; remaining 15 digit fragments unresolved (possibly a discount %) | 17 | OCR_LOW_CONFIDENCE |
| 44 | 907-938 | Kurlon Influencer Campaign (garbled) | 19 unresolved digit fragments, no coherent metric recovered | 19 | OCR_LOW_CONFIDENCE |
| 45 | 939-976 | Kurlon Social Media (garbled) | "15 minute Aaram Challenge" (repeated); voucher value garbled as "71,999" (likely ₹1,999); 21 further unresolved fragments | 24 | OCR_LOW_CONFIDENCE |
| 46 | 977-1006 | Kurlon Media Campaigns (garbled) | "40% OFF" (garbled as "40% FF"); 12 further unresolved fragments | 13 | OCR_LOW_CONFIDENCE |
| 47 | 1009-1042 | Kurlon Hyperlocal Activations (garbled) | "3 OFF NIGHTS"; gift value garbled as "24,998" (likely ₹4,998); 17 further unresolved fragments | 19 | OCR_LOW_CONFIDENCE |
| 49 | 1051 | Consol Revenue from Operations | 1032, 821, 26%, 1050, -2% | 5 | — |
| 49 | 1052 | Consol Operating Expenses | 923, 746, 933 | 3 | — |
| 49 | 1053 | Consol EBITDA | 109, 75, 45%, 117, -7% | 5 | — |
| 49 | 1054 | Consol EBITDA Margin % | 10.6%, 9.2%, 11.1% | 3 | — |
| 49 | 1055 | Consol Other Income | 16, 10, 18 | 3 | — |
| 49 | 1056 | Consol Depreciation | 34, 46, 36 | 3 | — |
| 49 | 1057 | Consol Finance Cost | 18, 29, 21 | 3 | — |
| 49 | 1058 | Consol PBT | 73, 10, 78 | 3 | — |
| 49 | 1059 | Consol Exceptional Item | -6, -(dash), -16 | 3 | ZERO_STANDING — Q1-FY26 shown as dash |
| 49 | 1060 | Consol Tax | 20, 5, 17 | 3 | — |
| 49 | 1061 | Consol Share in profit/(loss) of JV | 3, 2, 14 | 3 | — |
| 49 | 1062 | Consol PAT | 62, 7, 92 | 3 | — |
| 49 | 1063 | Consol PAT Margin % | 6.0%, 0.8%, 8.7% | 3 | — |
| 49 | 1064 | Consol Other Comprehensive Income | -6, 23, 18 | 3 | — |
| 49 | 1065 | Consol Total Comprehensive Income | 57, 30, 110 | 3 | — |
| 49 | 1066 | Consol Basic/Diluted EPS (INR) | 5.6, 0.6, -(dash), 8.3, -(dash) | 5 | ZERO_STANDING — YoY and QoQ columns shown as dash |
| 50 | 1071 | Standalone Revenue from Operations | 761, 635, 20%, 819, -7% | 5 | — |
| 50 | 1072 | Standalone Operating Expenses | 693, 574, 729 | 3 | — |
| 50 | 1073 | Standalone EBITDA | 68, 60, 13%, 90, -24% | 5 | — |
| 50 | 1074 | Standalone EBITDA Margin % | 9.0%, 9.5%, 11.0% | 3 | — |
| 50 | 1075 | Standalone Other Income | 14, 8, 16 | 3 | — |
| 50 | 1076 | Standalone Depreciation | 17, 30, 17 | 3 | — |
| 50 | 1077 | Standalone Finance Cost | 12, 23, 15 | 3 | — |
| 50 | 1078 | Standalone PBT | 52, 16, 75 | 3 | — |
| 50 | 1079 | Standalone Exceptional Item | -6, -(dash), -16 | 3 | ZERO_STANDING — Q1-FY26 shown as dash |
| 50 | 1080 | Standalone Tax | 15, 5, 14 | 3 | — |
| 50 | 1081 | Standalone PAT | 44, 11, 76 | 3 | — |
| 50 | 1082 | Standalone PAT Margin % | 5.8%, 1.7%, 9.3% | 3 | — |
| 50 | 1083 | Standalone Other Comprehensive Income | -3, -1, -3 | 3 | — |
| 50 | 1084 | Standalone Total Comprehensive Income | 41, 9, 73 | 3 | — |
| 50 | 1085 | Standalone Basic/Diluted EPS (INR) | 4.0, 1.0, 6.9 (no YoY/QoQ shown — blank, not dash) | 3 | — |
| 51 | 1094 | IR representative contact phone | 91-22-4903-9500 | 1 | — |

Row-count check: summing the `n` column above = 505, matching the COUNT TEST.

---

## TABLE C — Footnotes / fine-print qualifiers (3 definitions, 4 qualifying instances)

| # | Line (definition) | Footnote text | Qualifies (slide / value) | Flags |
|---|---|---|---|---|
| 1 | 211 | "*before Forex MTM" | Slide 10 — applied at the bottom of the "Financial Highlights" slide; not tied to one asterisked figure, reads as a whole-slide qualifier on the EBITDA growth numbers stated above it | slide-level footnote, scope ambiguous — flag for A3 to confirm whether it qualifies Standalone EBITDA, Consolidated EBITDA, or both |
| 2 | 416 | "*100% monetization" | Slide 23 — qualifies "FY30 – 13%*" (Waste Reduction target), line 402 | — |
| 3 | 517 | "*since inception" | Slide 29 — qualifies both "Reach: 568 million*" (line 509, FY26 col) and "Reach: 578 million*" (line 509, Q1FY27 col) | 2 qualifying instances under one footnote |

---

## Summary flags raised
ZERO_STANDING (6 instances: p13 OTHERS row, p13 TOTAL row, p30 empty template, p49 Exceptional Item, p49 EPS YoY/QoQ, p50 Exceptional Item), OCR_LOW_CONFIDENCE (9 slides: p6, p9 partial, p38, p43, p44, p45, p46, p47, and p15 label-attribution), OCR_NOISE_NO_DATA (6 slides: p31, p32, p33, p34, p39, p40, see Table A), POSSIBLE_NEW_OR_REFRAMED (4 slides: p8, p19, p38, p41 — cannot be confirmed as DROPPED_SLIDE candidates without the prior-quarter deck).
