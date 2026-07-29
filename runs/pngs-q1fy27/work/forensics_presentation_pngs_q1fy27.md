# A3 FORENSIC NOTES — PNGS REVA DIAMOND JEWELLERY (PNGSREVA), Q1 FY27, doctype: PRESENTATION

Source extract: `extract_presentation_pngs_q1fy27.txt` (33-page Reg 30 investor deck).
Ledger reconciled: `ledger_presentation_pngs_q1fy27.md` — 100% of rows read verbatim at cited lines
(48 financial-statement rows B1-B3; 121 KPI/chart rows C1-C121; 6 footnotes; 8 identifiers; 9 roster).

Unit convention: Rs Mn throughout; conversion to Rs Cr = x0.1. Reg 33 audited filing figures used for
cross-document reconciliation are stated in Rs Cr (filing wins on conflict, pipeline rule 11).

---

## HEADLINE (structural finding that frames the whole deck)

The P&L (slide 10) is a genuine **Q1FY27** statement. The Balance Sheet (slide 29) and Cash Flow
(slide 30) are **NOT** — they carry **Mar-25 | Mar-26** columns (line 883, line 929), i.e. FY25/FY26
year-end, roughly 15 months and 3 months respectively before the Q1FY27 quarter-end of 30-Jun-2026.
The deck therefore does **not** disclose a 30-Jun-2026 balance sheet or a Q1FY27 cash flow. Every
Q1FY27 cash-conversion, inventory-turn and CFO/PAT test (results-review INDETERMINATE cash
conversion; tripwires #2, #3, #8) is **uncomputable from this deck**; what the deck substitutes is a
FY26 balance sheet/cash flow that is itself materially adverse (FY26 CFO negative). This is the single
most important forensic point in the document and is carried as A3-F16-01 / A3-F16-02.

---

## CROSS-DOCUMENT RECONCILIATION — deck P&L vs Reg 33 audited filing

Deck P&L (slide 10, Rs Mn ÷10 = Rs Cr) vs filing (Rs Cr). Filing wins on any conflict.

| Metric | Deck (Rs Mn, line) | Deck →Rs Cr | Filing (Rs Cr) | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 1,180 (L309) | 118.0 | 117.973 | Ties (rounding) |
| Other Income | 56 (L325) | 5.6 | 5.576 | Ties (rounding) |
| Profit Before Tax | 364 (L331) | 36.4 | 36.398 | Ties (rounding) |
| Profit After Tax | 272 (L335) | 27.2 | 27.210 | Ties (rounding) |
| EPS | not shown in deck | — | 8.58 | Deck omits EPS (see A3-F10-01) |
| Q1 finished-goods inventory build | not in deck (deck CF is FY26 annual) | — | 30.478 | Not cross-checkable (see A3-F16-01) |

Result: the deck's Q1FY27 P&L is CONSISTENT with the Reg 33 filing within rounding on every figure the
deck carries (A3-F16-06, NEUTRAL-FACT). No P&L figure disagrees with the filing. The reconciliation
gaps are (a) EPS absent from the deck, and (b) the Q1 inventory build of Rs30.478 Cr cannot be tied
because the deck's cash flow is the FY26 annual statement, not a Q1FY27 statement.

Balance-sheet / cash-flow figures the Reg 33 filing did NOT contain, extracted here for tripwire use
(all FY26 year-end, Mar-26 column):
- CFO (FY26): **-1,048 Mn = -104.8 Cr** (L931) — negative.
- Closing cash (FY26 CF): 1,142 Mn (L943) — does NOT tie to BS cash 3,242 Mn (L907); gap 2,100 Mn.
- Inventories: 1,794 Mn (Mar-25) → 3,356 Mn (Mar-26), build +1,562 Mn = +156.2 Cr (L903).
- Short-term borrowings: 907 → 1,659 Mn (L903 liab). Net debt input; cash 3,242 > borrowings 1,659.
- FY26 PAT 647 Mn (L335, FY26 col) → **FY26 CFO/PAT = -1,048/647 = -1.62x** (breaches tripwire #3
  threshold of cumulative CFO/PAT < -0.5x on an FY26 basis; Q1FY27 basis undisclosed).

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F1-01 | F1 | B46 | L939, slide 30 | "Less: Net cash and cash equivalents generated for diamond business not taken over ... 34 ... 0" | AMBIGUOUS | Standing carve-out line: a "diamond business not taken over" was excluded on formation (co. "Formerly known as Gadgil Metals & Commodities", L67). Line runs to 0 in Mar-26. A4 to ask what was carved out, tax/asset basis, and whether any residual claim remains. |
| A3-F6-01 | F6 | C7,C8,C75,C97-C100 | L167-174; L506-511; L688; L692; L698 | "15 New EBO Stores Planned, of which 2 Brand-Exclusive Stores have Already Been Launched"; "Funded By ~Rs 2,866 Mn from net IPO proceeds"; "~Rs 354 Mn from the IPO proceeds for marketing" | FORWARD-SIGNAL | Datable FY27 commitment: 15 EBOs (2 done), Rs2,866 Mn IPO capex + Rs354 Mn marketing. Feeds Role 5 promise-vs-delivery and monitoring #1 (green 6-7 FY27; only 2 launched so far). |
| A3-F6-02 | F6 | D1 / C2 | L182, slide 6 | "*One New COCO Store opened on 7th July, 2026" | FORWARD-SIGNAL | Post-quarter (subsequent-event) delivery disclosed inside a Q1FY27 slide. Status word = completed. Partially addresses the open "4th EBO/COCO location & cadence" question; A4 to confirm MH vs non-MH location. |
| A3-F6-03 | F6 | C17-C18 (context) | L197-200, slide 7 | "We remain optimistic that the upcoming festive and wedding season ... will support sustained demand and continued growth" | FORWARD-SIGNAL | Soft H2 guidance ("will support"). No number; A4 to convert into a demand/SSG question for next quarter. |
| A3-F7-01 | F7 | C7,C75,C97 (context) | L176-177; L521; L689 | "Selectively Expanding into Tier 2 and Metro Cities"; "selectively exploring Tier-2 cities and other metro cities" | AMBIGUOUS | Hedge softens the 15-store expansion geography: firm commitment to Tier-1, only "exploring" Tier-2/metro. Bears on monitoring #9 (revenue outside MH). A4 to ask which of the 15 are outside Maharashtra. |
| A3-F8 (basis) | F8 | B12-B14 | L331-335, slide 10 | ETR Q1FY27 = 92/364 = 25.3% | (PASS, no finding) | ETR in line with statutory 25.17% (Q1FY26 24.5%, Q4FY26 25.4%, FY26 25.2%). No deferred-tax detail, no earlier-year adjustment disclosed. |
| A3-F10-01 | F10 | B16,B17 | L885, L888, slide 29 | "Equity Share Capital 49 → 317"; "Other Equity 953 → 4,835" | NEUTRAL-FACT | Paid-up capital 6.5x and Other Equity 5x jump traces cleanly to the IPO (proceeds referenced L692/L698). Deck carries no basic/diluted EPS and no share count, so dilution spread cannot be checked here; filing EPS 8.58. |
| A3-F14-01 | F14 | C43 vs B3/C25 | L283 (slide 9) vs L224 (slide 8)/L315 (slide 10) | "36% Margin" (slide 9) vs "35%" (slides 8 & 10) | AMBIGUOUS | Gross margin internal discrepancy: waterfall says 36% (418/1,180 = 35.4%, rounds to 35). Slide 9's 36% is an inflated rounding. Immaterial to thesis but a drafting-control signal; A4 note. |
| A3-F14-02 | F14 | C73 vs C104 | L494/L155 (slides 17/6) vs L803-804 (slide 26) | "37 Stores across 25 cities" / "34 SIS & 3 COCO" vs "all our 33 stores across Maharashtra, Gujarat & Karnataka" | AMBIGUOUS | Store-count discrepancy 37 vs 33 (gap of 4). Likely 33 = older SIS-only count reused in an industry-narrative slide vs 37 current (34 SIS + 3 COCO). Bears directly on monitoring #1 (EBO/store cadence). A4 to reconcile the true operating store count and format split. |
| A3-F14-03 | F14 | B48 vs B37 | L943 (slide 30) vs L907 (slide 29) | "Cash & cash equivalent at the end of the year ... 1,142" vs "Cash & cash equivalents ... 3,242" (both Mar-26) | AMBIGUOUS (leaning negative) | Mar-26 closing cash fails to tie across CF (1,142 Mn) and BS (3,242 Mn); gap 2,100 Mn ≈ Rs210 Cr. Candidate reconciling items: FDs/investments classed as cash on BS but excluded from CF cash-equivalents, or an incomplete CF. Material to any net-cash / cash-conversion read. A4 must ask management to bridge. |
| A3-F14-04 | F14 | C10/C17; C64/F1 | L191 vs L222; L424 vs L455 | "119.5% year-on-year revenue growth" (CEO) vs "119%" (charts); "Ajit (Govind) Gadgil" vs "Govind Gadgil" | NEUTRAL-FACT | Precision variant (119.5 vs 119) and promoter name variant across slides 15/16. Individually immaterial; cumulatively a drafting-control data point. |
| A3-F16-01 | F16 | B16-B48 (all BS/CF) | L883 (slide 29), L929 (slide 30) | "Liabilities (Rs Mn) Mar-25 Mar-26"; "Particulars (Rs Mn) ... Mar-25 Mar-26" | FORWARD-SIGNAL | The deck's balance sheet and cash flow are FY26 year-end, NOT Q1FY27 (30-Jun-2026). No current-quarter BS/CF disclosed. Q1FY27 cash conversion, inventory turn and CFO/PAT are uncomputable from the deck — the exact metrics behind the results-review INDETERMINATE and tripwires #2/#3/#8. A4 must demand the Jun-26 balance sheet / Q1 CF. |
| A3-F16-02 | F16 | B42, B35, B14(FY26) | L931; L903; L335 (FY26 col) | "Cash from Operating Activity ... -1,048"; "Inventories 1,794 ... 3,356" | CONFIRMATORY-NEGATIVE | FY26 CFO is negative Rs1,048 Mn against FY26 PAT Rs647 Mn → CFO/PAT = -1.62x, breaching tripwire #3 (< -0.5x) on an FY26 basis. Driver is a Rs1,562 Mn inventory build. Confirms the cash-conversion concern; the deck offers no Q1FY27 CF to show whether it has reversed. |
| A3-F16-03 | F16 | C15, C16 | L175-177, slide 6 | "18.3% \| 12.6% ROCE & ROE as of 31st March, 2026" | AMBIGUOUS | Prior-period (FY26 year-end) ROCE/ROE presented under a "Financial Highlights (Q1FY27)" header. ROCE 18.3% clears tripwire #4 (>16%) but is stale; no Q1FY27 ROCE given. Reframing a FY26 metric as a current highlight. A4 to request the Q1FY27 (annualised) figures. |
| A3-F16-04 | F16 | C96 | L649-661, slide 21 | "Gargi successfully scaled into a pan-India fashion jewellery platform with ~Rs150 Cr revenue (FY26)" | AMBIGUOUS | Sister brand PNGS Gargi's Rs150 Cr FY26 revenue is placed inside Reva's deck. It is a different Group entity's number and must NOT be conflated with Reva's own Q1FY27 Rs118 Cr / FY26 Rs439 Cr revenue. Selective-disclosure / scale-halo risk. A4 to ensure any "playbook" comps keep Gargi separate. |
| A3-F16-05 | F16 | B2, B5, B6 | L311, L317, L319, slide 10 | Consumption of materials "761 ... 998 ... 3,176" with YoY/QoQ columns blank | AMBIGUOUS | P&L shows YoY%/QoQ% for revenue, GP, EBITDA, PBT, PAT but leaves those columns blank for the three cost lines (materials, employee, other). Cost-growth de-emphasised. A4 to compute and question cost-line trajectory (materials +107% YoY vs revenue +119%). |
| A3-F16-06 | F16 | B1,B9,B12,B14 | L309,L325,L331,L335 | Deck Rev/OI/PBT/PAT vs filing 117.973/5.576/36.398/27.210 Cr | NEUTRAL-FACT | Deck Q1FY27 P&L reconciles to the Reg 33 audited filing within rounding on every carried figure. No conflict; confirmatory of P&L integrity. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Check | Status | One-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | FINDING | 6 ZERO_STANDING rows read; the "diamond business not taken over" carve-out line (L939) is the material one (A3-F1-01). Others (dep Q1FY26=0 L327; fin. liab/provisions/fin.assets Mar-25=0; no parent store closures) are formation/immateriality artefacts. |
| F2 | Standalone vs consolidated | N.A. | Standalone-only deck; Notion confirms NO subsidiaries. No consolidated column exists to decompose. |
| F3 | Shell-entity detection | N.A. | No subsidiary/consolidated cost lines; no entities to test. |
| F4 | Unaudited contribution ratio | N.A. | No auditor "Other Matters" in an investor presentation. |
| F5 | Going concern / EoM scope | N.A. | No auditor EoM in a Reg 30 deck; no prior-quarter deck to diff. |
| F6 | Forward-commitment phrase mining | FINDING | 15-EBO plan (2 launched), IPO Rs2,866 Mn capex + Rs354 Mn marketing, COCO opened 7-Jul-2026, CEO festive-season guidance (A3-F6-01/02/03). See Commitment Register. |
| F7 | Hedge phrase mining | FINDING | "selectively exploring Tier-2 cities and other metro cities" (L521/L689) hedges expansion geography (A3-F7-01); disclaimer hedges (L102-109) are boilerplate. |
| F8 | Tax forensics | PASS | ETR 25.3% Q1FY27, all periods 24.5-25.4% vs statutory 25.17%; no deferred-tax detail, no earlier-year adjustment disclosed. |
| F9 | OCI forensics | N.A. | No OCI / actuarial line in the deck's statements. |
| F10 | Share count & dilution | FINDING | Paid-up 49→317 Mn and Other Equity 953→4,835 Mn trace to the IPO; deck omits EPS and share count (A3-F10-01). |
| F11 | Reserves / net worth tie-out | PASS | Other Equity 4,835 + Paid-up 317 = 5,152 = Total Equity (L888/L885/L891). Exact tie. |
| F12 | Segment forensics | N.A. | No segment tables in the deck. |
| F13 | Board outcome beyond results | N.A. | No AR/AGM/board-resolution/director-term data; org chart lists names only, no DIN/term dates. |
| F14 | Note-drafting inconsistencies | FINDING | Gross margin 36% vs 35% (A3-F14-01); store count 37 vs 33 (A3-F14-02); Mar-26 closing cash 1,142 vs 3,242 cross-table (A3-F14-03); 119.5 vs 119 and name variant (A3-F14-04). |
| F15 | Entity list diffs | N.A. | No consolidation list; no prior-quarter ledger (PRIOR_LEDGER_UNAVAILABLE). Gargi handled as other-entity under F16. |
| F16 | Presentation-specific (dropped/reframed/selective) | FINDING | BS/CF are FY26 not Q1FY27 (A3-F16-01); FY26 CFO/PAT -1.62x (A3-F16-02); ROCE/ROE FY26 shown under Q1FY27 (A3-F16-03); Gargi Rs150 Cr in Reva deck (A3-F16-04); cost-line %s suppressed (A3-F16-05); P&L reconciles to filing (A3-F16-06). DROPPED_SLIDE diff N.A. (first cycle). |
| F17 | Concall silence audit | N.A. | No transcript (doctype = presentation). Monitoring-checklist silences are logged below for A4/A5. |

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Ref (line/slide) | Status word |
|---|---|---|---|
| 15 new exclusive (EBO/COCO) stores across India | FY27 | L167-174/L506-511/L688, slides 6/17/22 | underway (2 launched) |
| 2 brand-exclusive stores already launched | Achieved by 29-Jul-2026 | L168-169/L511, slides 6/17 | completed |
| One new COCO store, Amanora Mall Pune | Opened 7-Jul-2026 (post Q1) | L182/L367, slides 6/12 | completed |
| Deploy ~Rs2,866 Mn net IPO proceeds on store expansion | FY27 rollout | L692, slide 22 | in the process of (utilisation-to-date not disclosed) |
| Deploy ~Rs354 Mn IPO proceeds on marketing/promotion | FY27 | L698, slide 22 | in the process of |
| Festive + wedding season to "support sustained demand and continued growth" | H2 FY27 | L197-200, slide 7 | intends to / outlook |
| Product diversification into high-value/customized/bridal to lift AOV | FY27+ | L698-699, slide 22 | intends to |

---

## MONITORING-CHECKLIST RESOLUTION (deck coverage, for A4/A5 — F17 silence context)

| Item | Deck says | Line | Read |
|---|---|---|---|
| #1 EBO additions (green 6-7 FY27) | 15 planned, 2 launched + 1 COCO post-Q1 | L167/L182/L688 | Below green run-rate so far; full-year open |
| #2 EBO revenue/store | not disclosed | — | SILENT |
| #4 SSG/SSSG | not disclosed | — | SILENT (open question persists) |
| #5 AOV (green >Rs1.20L; red declining) | Rs100,232 vs Rs92,624, +8% | L244-246, slide 8 | Rising (not red) but below Rs1.20L green — amber |
| #6 EBITDA margin (green 19-22%; red <18%) | 29% Q1FY27 | L323/L230 | Above green band; unusually strong, A4 to probe durability |
| #7 Inventory turn (green >1.25x; red <1.20x) | 1.29x annualised | L159/L163/L182 | Green, but computed on Mar-26 (not Jun-26) inventory — methodology unverifiable |
| #8 CFO/PAT | FY26 CFO -1,048 vs PAT 647 = -1.62x; Q1 undisclosed | L931/L335 | Negative on FY26 basis — see A3-F16-02 |
| #9 Revenue outside Maharashtra (green >10% by FY28) | 3 states (MH/Guj/Kar), 37 stores, map MH-heavy | L494/L497-499/L804 | % outside MH not quantified — SILENT |
| #11 Customer concentration / 10.77% customer identity | not disclosed | — | SILENT (open question persists) |

---

## CLASSIFICATION ROLLUP

- FORWARD-SIGNAL (flag to A4): A3-F6-01, A3-F6-02, A3-F6-03, A3-F16-01.
- AMBIGUOUS (flag to A4 → management questions): A3-F1-01, A3-F7-01, A3-F14-01, A3-F14-02, A3-F14-03, A3-F16-03, A3-F16-04, A3-F16-05.
- CONFIRMATORY-NEGATIVE: A3-F16-02.
- NEUTRAL-FACT: A3-F10-01, A3-F14-04, A3-F16-06.

All 6 A2 adjudication flags landed: gross margin 36/35 → A3-F14-01; store 37/33 → A3-F14-02;
closing-cash 1,142/3,242 → A3-F14-03; AOV plain-Rs unit → confirmed (C37-C39, L244-246, non-error
labelling, folded into monitoring #5, no separate finding needed); Gargi other-entity → A3-F16-04;
guidance-vs-actual separation → Commitment Register + A3-F16-03/A3-F6-01.

```yaml
stage: A3-forensics
company: "PNGSREVA"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/pngs-q1fy27/work/forensics_presentation_pngs_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "L939/slide30", classification: "AMBIGUOUS", implication: "Carve-out standing line 'diamond business not taken over'; ask scope/tax/residual claim"}
  - {id: "A3-F6-01", check: "F6", line: "L167-174/L692/L698", classification: "FORWARD-SIGNAL", implication: "15 EBO (2 done) + Rs2,866Mn/Rs354Mn IPO commitments; Role5 tracker + monitoring #1"}
  - {id: "A3-F6-02", check: "F6", line: "L182/slide6", classification: "FORWARD-SIGNAL", implication: "COCO store opened 7-Jul-2026 post-quarter; confirm MH vs non-MH (open Q)"}
  - {id: "A3-F6-03", check: "F6", line: "L197-200/slide7", classification: "FORWARD-SIGNAL", implication: "CEO festive/wedding H2 demand guidance; convert to SSG question"}
  - {id: "A3-F7-01", check: "F7", line: "L521/L689", classification: "AMBIGUOUS", implication: "'selectively exploring Tier-2/metro' hedges expansion geography; monitoring #9"}
  - {id: "A3-F10-01", check: "F10", line: "L885/L888/slide29", classification: "NEUTRAL-FACT", implication: "Paid-up 49->317 & OE 953->4,835 = IPO; deck omits EPS/share count"}
  - {id: "A3-F14-01", check: "F14", line: "L283 vs L224/L315", classification: "AMBIGUOUS", implication: "Gross margin 36% (slide9) vs 35% (slides8/10); drafting-control signal"}
  - {id: "A3-F14-02", check: "F14", line: "L494 vs L803-804", classification: "AMBIGUOUS", implication: "Store count 37 vs 33; reconcile true operating count/format for monitoring #1"}
  - {id: "A3-F14-03", check: "F14", line: "L943 vs L907", classification: "AMBIGUOUS", implication: "Mar-26 closing cash 1,142 (CF) != 3,242 (BS); 2,100Mn gap; management must bridge"}
  - {id: "A3-F14-04", check: "F14", line: "L191 vs L222; L424 vs L455", classification: "NEUTRAL-FACT", implication: "119.5 vs 119 precision + Gadgil name variant; drafting control"}
  - {id: "A3-F16-01", check: "F16", line: "L883/slide29; L929/slide30", classification: "FORWARD-SIGNAL", implication: "BS/CF are FY26 not Q1FY27; no Jun-26 BS/Q1 CF; tripwires #2/#3/#8 uncomputable; demand statements"}
  - {id: "A3-F16-02", check: "F16", line: "L931/L903/L335", classification: "CONFIRMATORY-NEGATIVE", implication: "FY26 CFO -1,048 vs PAT 647 = -1.62x (breaches tripwire #3); Rs1,562Mn inventory build; no Q1 CF to show reversal"}
  - {id: "A3-F16-03", check: "F16", line: "L175-177/slide6", classification: "AMBIGUOUS", implication: "ROCE 18.3%/ROE 12.6% dated 31-Mar-26 shown under Q1FY27; request Q1 figures"}
  - {id: "A3-F16-04", check: "F16", line: "L649-661/slide21", classification: "AMBIGUOUS", implication: "Sister brand Gargi Rs150 Cr FY26 in Reva deck; keep separate from Reva revenue"}
  - {id: "A3-F16-05", check: "F16", line: "L311/L317/L319", classification: "AMBIGUOUS", implication: "P&L suppresses YoY/QoQ% on cost lines only; materials +107% vs revenue +119%"}
  - {id: "A3-F16-06", check: "F16", line: "L309/L325/L331/L335", classification: "NEUTRAL-FACT", implication: "Deck Q1FY27 P&L reconciles to Reg33 filing within rounding; no conflict"}
forward_signals: ["A3-F6-01", "A3-F6-02", "A3-F6-03", "A3-F16-01"]
ambiguous: ["A3-F1-01", "A3-F7-01", "A3-F14-01", "A3-F14-02", "A3-F14-03", "A3-F16-03", "A3-F16-04", "A3-F16-05"]
commitments:
  - {commitment: "15 new exclusive EBO/COCO stores across India", implied_date: "FY27", ref: "L167-174/L688/slides6,17,22", status_word: "underway"}
  - {commitment: "2 brand-exclusive stores already launched", implied_date: "by 29-Jul-2026", ref: "L168-169/L511", status_word: "completed"}
  - {commitment: "New COCO store, Amanora Mall Pune", implied_date: "7-Jul-2026", ref: "L182/L367/slides6,12", status_word: "completed"}
  - {commitment: "Deploy ~Rs2,866 Mn net IPO proceeds on store expansion", implied_date: "FY27", ref: "L692/slide22", status_word: "in the process of"}
  - {commitment: "Deploy ~Rs354 Mn IPO proceeds on marketing", implied_date: "FY27", ref: "L698/slide22", status_word: "in the process of"}
  - {commitment: "Festive/wedding season to support demand & growth", implied_date: "H2 FY27", ref: "L197-200/slide7", status_word: "intends to"}
  - {commitment: "Product diversification into high-value/bridal to lift AOV", implied_date: "FY27+", ref: "L698-699/slide22", status_word: "intends to"}
gate_a3: pass
blank_checks: []
```
