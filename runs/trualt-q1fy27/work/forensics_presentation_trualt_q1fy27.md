# A3 FORENSIC NOTES — TRUALT Q1FY27 — Investor Presentation (doctype: presentation)

Source extract: `extract_presentation_trualt_q1fy27.txt` (955 lines, 32 slides)
Ledger: `ledger_presentation_trualt_q1fy27.md` (Tables A/B/C/D)
Ledger reconciliation: 100% — every row read verbatim at its cited line before judging.
Units: Rs Cr (x1). Fresh coverage: no prior-quarter deck / no Notion checklist; prior-period baselines flagged where a check needs them.

Doctype weighting applied: F16 primary; F6/F7/F11/F12 carry the deck's forward signals; F3/F4/F5/F9/F10/F13/F15/F17 are results-filing / concall checks that a Reg-30 deck does not carry (marked N.A. with basis, not left blank).

---

## FINDINGS TABLE

| id | check | ledger row | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F1-01 | F1 | B3.1 | S17 / L531 | "10.20  NA  Leafiniti Bioenergy  Operational" | NEUTRAL-FACT | The one dash-valued "Strategic Partner" cell marks the ONLY operational CBG unit (Jamkhandi, 10.20 TPD). The entire current CBG P&L (TI 11.31 Cr) rests on this single non-JV plant; all JV units (Sumitomo/GAIL) are still under construction and contribute zero revenue this quarter. |
| A3-F2-01 | F2 | C6.5-C6.12 | S10 / L348-361 | "₹ 641.41 Cr. (Q1 FY 27) … ₹ 630.37 Cr. (Q1 FY 27)" | AMBIGUOUS | Consolidation adds only +11.04 Cr TI and +4.26 Cr PAT over standalone (FY26: +4.70 Cr PAT). Standalone ≈ ethanol segment (PAT 55.01 vs ethanol seg 54.96); the whole consol uplift is CBG+Retail subsidiaries, and that uplift is SHRINKING as CBG PAT falls YoY. No consolidated cost lines or eliminations shown to verify. |
| A3-F6-01 | F6 | B3.2-B3.6, C3.9, C11.*, C12.*, B4.4 | S17/L537-554, S21/L699-711, S22/L728, S7/L212 | "expected to be operational by the end of Q2 FY 27" / "Plant commissioning targeted for August 2026" / "commissioning within 24–30 months, subject to the necessary approvals" | FORWARD-SIGNAL | 17 dated/dateable management commitments (see Commitment Register). Dense Aug–Dec 2026 and Q2–Q4 FY27 commissioning wall feeds the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. Every one is verifiable next quarter. |
| A3-F6-02 | F6 | C5.5 | S9 / L295 | "DDGS production commenced from Q3" | AMBIGUOUS | Status word "commenced" (past) but fiscal year of "Q3" unspecified (AMBIGUOUS_PERIOD). If FY26 Q3, DDGS revenue is already in the base; if FY27 Q3 it is future — materially different for the "value-accretive revenue stream" claim. A4 question. |
| A3-F7-01 | F7 | C-slide7 (catalogued) | S7 / L216-217 | "the pace of expansion in our downstream fuel retail business may appear measured, this was a conscious strategic decision" | AMBIGUOUS | Newly-drafted pre-emptive cover on slow retail rollout (7 operational of a 100-outlet target). Paired with Retail PAT -54.55% YoY, the hedge is telling us retail unit economics / pace disappoint; next-quarter retail is likely soft. A4 question. |
| A3-F11-01 | F11 | B6.1-B6.7 | S28 / L834-841 | "ROCE 20.35%  ROE 14.42%" | AMBIGUOUS | "Consolidated Basis" ratios sit on a single-quarter P&L with no annualisation basis stated; ROE (14.42%) < ROCE (20.35%). No paid-up capital / other-equity given, so statutory net-worth tie-out is impossible from the deck — only D/E 0.59 and TOL/TNW 1.28 anchor leverage. Ratio period basis is a KPI-definition gap for A4. |
| A3-F12-01 | F12 | C7.5-C7.8, C9.1-C9.7 | S11/L375-391, S18/L586-608 | "(6.16)% (QoQ)" EBITDA; "(10.51)% (QoQ)" PBT/PAT | CONFIRMATORY-NEGATIVE | CBG margins deteriorating YoY (EBITDA margin 66.74%→55.64%, PBT margin 57.88%→46.68%) while the segment absorbs the ₹340 Cr Phase-I capex build. Retail PAT -54.55%. Deck carries NO segment assets/liabilities, so the equity-funded-build test cannot be run — flag: segment balance-sheet disclosure absent. Margin compression precedes the capex wave. |
| A3-F14-01 | F14 | C11.4-C11.6 vs B3.3 | S21/L703-711 vs S17/L540-543 | "Kedarnath (Bagalkot, Karnataka)" vs "Unit 3 … Kerakalmatti, Karnataka" | AMBIGUOUS | Same Sumitomo-JV site named "Kedarnath" on the execution slide and "Kerakalmatti" on the deployment table; commissioning also differs (Sep 2026 vs "end of Q3 FY27"). Entity-name + date inconsistency across tables — is this one site or two? A4 must confirm the JV site list. |
| A3-F14-02 | F14 | B1.5 | S13 / L417-419 | "200 KLPD … Dual Feed Integration - 300 KLPD" | AMBIGUOUS | Unit 4 (Kerakalmatti) stated dual-feed capacity 300 KLPD EXCEEDS its own installed 200 KLPD — arithmetically impossible at unit level, though platform totals (2,000 installed / 1,300 dual-feed) still foot. A capacity-claim data error on the headline "multi-feed platform" narrative; likely transposition, but flag as unreconciled. |
| A3-F16-01 | F16 | C6.*, C7.*, C8.*, C9.* | S10/L350-359, S11/L378-388 | "96.37%  (QoQ)" / "1252.63%  (QoQ)" | AMBIGUOUS | Every "(QoQ)" growth tag in the deck actually compares Q1FY26 to Q1FY27 = a YoY figure mislabelled as sequential (LABEL_ERROR, confirmed at chart-OCR L511/L618). Reframes the momentum optics; a reader taking "+96% QoQ" as sequential overstates run-rate. A4 clarification. |
| A3-F16-02 | F16 | B5.10-B5.12, C6.6/C6.8/C6.12 | S27/L817-819 | "Profit / (Loss) Before Tax  73.31  0.13  … 55481%" | NEUTRAL-FACT | Headline growth percentages (PBT +55,481%, PAT +213,933%, ethanol seg PBT +334,424%) are artefacts of a near-zero Q1FY26 base (PBT 0.13, PAT 0.03). Not misstatement, but the easy-comp base normalises after Q1 — YoY optics collapse from Q2 onward regardless of operations. |
| A3-F16-03 | F16 | C6.4 / C8.2 | S10 / L341-342 | "Current capacity utilisation of 60.57% … without significant additional capital expenditure" | FORWARD-SIGNAL | ~40% idle installed capacity presented as growth headroom. Genuine near-costless volume optionality: the ethanol platform can scale ~65% of PAT-generating output with no new capex if allocations/demand appear. Also the single biggest swing factor on FY27 volumes. |
| A3-F16-04 | F16 | B4.8 | S19 / L628-633 | "₹180 crore committed across three locations … separate equity commitment of ₹60 crore for the same three locations" | AMBIGUOUS | Phase I is "Four CBG units" (₹340 Cr total) but the NABARD debt (₹180 Cr) + equity (₹60 Cr = ₹240 Cr) financing is named for only THREE locations. Funding of the 4th unit's ~₹85 Cr is unstated — possible unfunded gap / future raise. A4 question. |

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| # | Check | Status | Basis (one line) |
|---|---|---|---|
| F1 | Zero-value standing line items | FINDING | Sole ZERO_STANDING (B3.1): CBG Unit-1 "Strategic Partner = NA" — the only operational, non-JV CBG plant (L531). |
| F2 | Standalone vs consolidated decomposition | FINDING | Consol adds only +4.26 Cr PAT (all CBG+Retail subs), and shrinking; no consol cost lines / eliminations to verify (L348-361). |
| F3 | Shell-entity detection | N.A. | Deck carries no consolidated P&L cost lines; S-vs-C cost comparison impossible. CBG sub (TruAlt Gas) has real revenue, not a shell. |
| F4 | Unaudited contribution ratio | N.A. | No auditor Other-Matters para in a Reg-30 deck; results are un-audited throughout (L25, L32). |
| F5 | Going concern / EoM scope | N.A. | No auditor report / EoM paragraph in a presentation. |
| F6 | Forward-commitment phrase mining | FINDING | 17 dated commitments (commissioning Aug–Dec 2026, Q2–Q4 FY27, SAF 24-30 months) + DDGS ambiguous period (L295); see register. |
| F7 | Hedge phrase mining | FINDING | Newly-drafted retail-pace hedge (L216-217) plus SAF "subject to necessary approvals" (L212); pre-emptive cover on soft retail. |
| F8 | Tax forensics | PASS | Standalone ETR 18.30/73.31 = 24.96% vs statutory 25.17% — in line. Q1FY26 base near-zero (not meaningful). No "earlier years" tax line; no deferred-tax detail in deck. |
| F9 | OCI forensics | N.A. | No OCI / actuarial disclosure in the deck. |
| F10 | Share count & dilution | N.A. | Deck carries no paid-up capital, share count or EPS (basic/diluted). |
| F11 | Reserves & net-worth tie-out | FINDING | No paid-up/other-equity given; ratios (ROE 14.42% < ROCE 20.35%) on a single-quarter basis with undisclosed annualisation (L834-841). |
| F12 | Segment forensics | FINDING | CBG margins compressing (66.74%→55.64% EBITDA) into a ₹340 Cr capex build; Retail PAT -54.55%; segment assets/liabilities absent (L375-391, L586-608). |
| F13 | Board outcome beyond results | N.A. | Investor deck, not a board-outcome / AGM / director-appointment filing; no such content. |
| F14 | Note drafting inconsistencies | FINDING | Kedarnath vs Kerakalmatti entity-name split (L703 vs L542); Unit-4 dual-feed 300>200 installed (L417-419); typos "reznewable"/"foward"/"by in the coming months". |
| F15 | Entity list diffs | N.A. | No formal consolidation list in deck; fresh coverage — no prior-quarter baseline (PRIOR_LEDGER_UNAVAILABLE). Entities named: TruAlt Gas Pvt Ltd, Leafiniti Bioenergy. |
| F16 | Dropped & reframed disclosures | FINDING | QoQ-labelled-YoY mislabel (L350-388); near-zero-base mega-% (L817-819); 60.57% utilisation spun as capex-free upside (L341); Phase-I financing covers 3 of 4 units (L628-633). Prior-deck diff impossible — baseline missing (flagged). |
| F17 | Concall silence audit | N.A. | Not a transcript; no Notion monitoring checklist provided. |

Blank checks: none. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| # | commitment | implied date | slide/line ref | status word |
|---|---|---|---|---|
| 1 | CBG Unit 2 Mudhol operational | end Q2 FY27 | S17 / L535-537 | "in construction phase, expected to be operational" |
| 2 | CBG Unit 3 Kerakalmatti operational | end Q3 FY27 | S17 / L540-543 | in construction / expected |
| 3 | CBG Unit 4 Badami operational | end Q3 FY27 | S17 / L546-548 | in construction / expected |
| 4 | CBG Unit 5 Daund operational | end Q4 FY27 | S17 / L551-554 | in construction / expected |
| 5 | Mudhol (Sumitomo) plant commissioning | August 2026 | S21 / L699 | 95% civil, 70% mechanical — targeted |
| 6 | Kedarnath plant commissioning | September 2026 | S21 / L711 | 90% civil, 65% mechanical — targeted |
| 7 | Badami plant commissioning | December 2026 | S22 / L728 | 90% civil, 65% mechanical — targeted |
| 8 | Bhima Patas (Daund) construction start | none given (silence) | S22 / L739 | "to commence upon completion of documentation" |
| 9 | GAIL/Leafiniti 6 CBG plants construction | "coming months", phased | S7 / L192-194 | "preparatory activities … progressing"; "expected to commence" |
| 10 | SAF Srikakulam financial closure & commissioning | 24–30 months (subject to approvals) | S7 / L210-212 | FEED stage w/ Honeywell UOP — "progressing"; hedged |
| 11 | PM JI-VAN Yojana grant ₹150 Cr | sanctioned (past) | S7 / L206 | "sanctioned … important milestone" |
| 12 | Share purchase for Sumitomo JV (TruAlt Gas) | completed | S9 / L286 | "completed" |
| 13 | Share purchase for GAIL JV | completed | S9 / L310-311 | "also completed" |
| 14 | CBG Phase-I capacity ramp-up | FY27 40% / FY28 85% / FY29 ~90% | S19 / L634 | guidance |
| 15 | Retail: +4 outlets launch; Phase-I 100 stations (11 in KA) | "coming months" / Phase 1 | S24 / L761-765 | 7 operational — "set to launch" |
| 16 | DDGS production | "commenced from Q3" (FY unspecified) | S9 / L295 | "commenced" — AMBIGUOUS period |
| 17 | CBG phased commissioning (general) | "from Q2 FY27 onwards" | S9 / L298 | "targeted" |

Silence flag inside register: item 8 (Bhima Patas) is the only Sumitomo-JV site with NO commissioning month, unlike the other three named sites — track for a slip signal next quarter.

---

## NOTES FOR A4 (question generation)
- FORWARD-SIGNAL: A3-F6-01 (commissioning wall), A3-F16-03 (40% idle-capacity optionality).
- AMBIGUOUS → convert to management questions: A3-F2-01, A3-F6-02, A3-F7-01, A3-F11-01, A3-F14-01, A3-F14-02, A3-F16-01, A3-F16-04.
- Missing-baseline flags (fresh coverage): F15 entity-list diff and F16 dropped-metric diff could not be run — source the Q4FY26 deck independently if a dropped-disclosure signal is needed.
- Cross-doc reconciliation caveat: only the STANDALONE P&L (S27) is line-item reconcilable to a filing; every consolidated and segment figure in the deck (incl. all Table B6 ratios) has NO audited/reviewed line to tie to within this document.
