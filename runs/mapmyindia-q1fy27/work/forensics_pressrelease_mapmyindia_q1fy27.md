# A3 FORENSIC NOTES — MapmyIndia (MAPMYINDIA) — Q1 FY27 — PRESS RELEASE (presentation-class discipline)

Source extract: `extract_pressrelease_mapmyindia_q1fy27.txt` (6 pages, 379 lines, Rs Cr, 100% page coverage, no OCR).
Ledger: `ledger_pressrelease_mapmyindia_q1fy27.md` (Table 1: 7 line items; Table 2: 29 metrics; Table 3: 1 quote / 5 paragraph sub-units; Table 4: 21 structural units).
Ledger reconciliation: 100% — every row read verbatim at its cited line before judging.

Doctype scope (per task injection): F16 applies; F6 forward-commitment phrases apply; F10/F11 apply only if the release carries such numbers (it does not); F14 is opened specifically to assess the A2 FIGURE_VARIANT flag ("grew 15%" vs 14.9%), overriding the generic balance-sheet-N.A. default per the "pay attention to" instruction; F13 applies because the release announces a board-level Joint MD appointment with a shareholder resolution incoming; F7 hedge lexicon is swept; balance-sheet checks F1-F5, F8, F9, F10, F11, F12, F15 are N.A. (no statutory statement, no auditor letter, no share/reserve/segment-asset data in the release); F17 is N.A. (no concall transcript). No true prior-release ledger was supplied, so F16 diffs against the injected FY26 baselines and says so.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| F16-1 | F16 | QT1-P2 (T3) / S17 (T4) | L127-129 (also L257-260) | "we are reporting our market-wise segmental revenues across three customer-focused verticals - Automotive, Enterprise and Government - instead of the previously reported A&M and C&E market segments" | FORWARD-SIGNAL | Market-segment taxonomy re-baselined this quarter; A&M/C&E-to-AEG switch breaks YoY comparability of the market split exactly at a quarter when the map-led core was tracking negative (FY26 baseline map-led -8.7%). Reduces external ability to track monitoring item #1 (govt revenue growth) and #5 (map/data core positive YoY) on a like-for-like basis. |
| F16-2 | F16 | T2 rows 3-4/13-14; QT1-P1 | L118 (margins L106-107) | "EBITDA remained strong at ₹56.1 crore with EBITDA margin at 40.2%" | FORWARD-SIGNAL | EBITDA framed as "remained strong" while EBITDA margin fell ~570bps YoY (45.9% Q1FY26 -> 40.2% Q1FY27, L107) and absolute EBITDA was flat (+0.4%, L106) against revenue +14.9%. Cost base grew far faster than revenue; consistent with rising lower-margin IoT mix (FY26 baseline IoT ~16% margin). Still above the 38% two-quarter tripwire (checklist #4) but trajectory is down; language softening masks the compression. |
| F16-3 | F16 | Table 1 (whole) | L102-111 | "Key Consolidated Financial Highlights for Q1 of FY2027" (table carries no segment split, no order book, no receivables, no intake) | AMBIGUOUS | Release carries none of the FY26-baseline monitored disclosures: no order book (FY26 Rs1,754 Cr), no intake (FY26 Rs785 Cr), no consolidated receivables (FY26 Rs176.4 Cr FLAG-CASH), no map-led/IoT or govt split in-line. Cannot be confirmed as a "dropped" disclosure vs a prior press release — no prior-release ledger supplied — so flagged as a comparability/omission gap for A4 to test against the investor deck. |
| F14-1 | F14 | T2 row 11 (FIGURE_VARIANT) | L117 (vs L104, L88) | "Revenue from Operations grew 15% year-on-year to ₹139.7 crore" | NEUTRAL-FACT | CMD quote rounds 14.9% (table L104 and headline L88) up to "15%". Immaterial 0.1pp, directionally optimistic; a drafting inconsistency / governance data point, not a numeric misstatement. Recorded per the FIGURE_VARIANT flag; no forward thesis impact. |
| F6-1 | F6 | QT1-P3, S18 anchor L264, QT1-P4 | L136-137, L264-266, L163-164 | "subject to shareholder approval, effective 1st July 2026"; "Now onwards, we shall report market-wise segmental revenues"; "we are leaning heavily into AI – accelerating and increasing our push into AI-native product development" | FORWARD-SIGNAL | Three dated/dateable management commitments (see Commitment Register): a governance ratification pending, a reporting-format change now live, and an undated AI-native investment push. The AI push implies rising opex ahead — ties to the F16-2 margin compression. |
| F13-1 | F13 | QT1-P3 (T3) | L135-137 | "This quarter also marks an important milestone in our leadership journey with the appointment of Rohan Verma as Joint Managing Director, subject to shareholder approval, effective 1st July 2026" | FORWARD-SIGNAL | Board-level succession event: Rohan Verma elevated to Joint MD alongside Rakesh Verma (CMD). Directly addresses monitoring item #9 (MD succession). A shareholder special/ordinary resolution is incoming (AGM record date foreshadowed); term/effective date 1 Jul 2026. Family-line succession is a governance signal to map against the thesis (FLAG-PROMOTER CONCERN). |

---

## CHECKLIST SCORECARD (all 17; exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Press release, not a statutory statement; A2 records zero_standing count = 0, no template line items to interrogate. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Only consolidated highlights disclosed (L99); no standalone column to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines; no entity-level financials in a press release. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters paragraph; press release is not an audited/reviewed filing. |
| F5 GOING CONCERN / EoM | N.A. | No going-concern or Emphasis-of-Matter language; not a Reg 33 statement. |
| F6 FORWARD-COMMITMENT PHRASES | FINDING | Lexicon hits "subject to approval" (L136), "shall report" (L264), AI-push forward language (L163-164); see F6-1 and Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Lexicon swept; only the standard boilerplate FLS disclaimer (L365-374, "subject to... risks and uncertainties", "no obligation to update"). No newly-added substantive hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | N.A. | No tax line, ETR, or deferred-tax disclosure in the release. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in the release. |
| F10 SHARE COUNT & DILUTION | N.A. | Release carries no paid-up capital, share count, or basic/diluted EPS. |
| F11 RESERVES & NET WORTH | N.A. | Release carries no other-equity/net-worth figures (Cash & Equivalents L110 is not net worth). |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities disclosed; even segment revenue split is absent this release (see F16-3). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Rohan Verma appointed Joint MD subject to shareholder approval, effective 1 Jul 2026 (L135-137); succession + incoming resolution — see F13-1. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Opened per task to assess the FIGURE_VARIANT: CMD "grew 15%" (L117) vs table/headline 14.9% (L104/L88) — see F14-1. (Overrides the generic balance-sheet-N.A. default.) |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation-entity list in a press release; nothing to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Segment taxonomy re-baselined A&M/C&E -> AEG (L127-129), EBITDA "remained strong" framing over 570bps margin fall (L118), and absent order-book/receivables/segment-split disclosures — see F16-1/2/3. |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript in scope; this is a press release. |

Scorecard tally: FINDING x4 (F6, F13, F14, F16); PASS x1 (F7); N.A. x12 (F1-F5, F8, F9, F10, F11, F12, F15, F17). No blanks — GATE A3 pass.

---

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | note/turn ref | status word |
|---|-----------|--------------|---------------|-------------|
| 1 | Rohan Verma appointed Joint Managing Director, "subject to shareholder approval" | Effective 1 Jul 2026; ratification at next AGM (FY27) | L136-137 (QT1-P3) | initiated |
| 2 | "Now onwards, we shall report market-wise segmental revenues" across Automotive / Enterprise / Government (AEG), replacing A&M/C&E | From Q1 FY27 onward (live this quarter) | L264-266 (S18 anchor); restated L127-129 / L257-260 | commenced |
| 3 | "leaning heavily into AI – accelerating and increasing our push into AI-native product development, AI-native product offerings and AI-native organizational work" | Undated / ongoing | L163-164 (QT1-P4) | underway |

Note: the release carries NO numeric forward guidance — the FY28 Rs1,000 Cr target (monitoring item #8) and any margin/order-book targets are not mentioned. Their absence is captured under F16-3 (comparability/omission gap), not as a commitment.

---

## HANDOFF TO A4

- FORWARD-SIGNAL (convert to management questions): F16-1 (why re-baseline market segments now; provide restated A&M/C&E history), F16-2 (drivers of 570bps margin compression; IoT mix vs opex/AI spend; margin trajectory guidance), F6-1 (dating/quantifying the AI-native investment push), F13-1 (succession plan, resolution terms, Rakesh Verma's continuing role/tenure).
- AMBIGUOUS (convert to management questions): F16-3 (request order book, intake, consolidated receivables, and map-led/IoT + govt split for Q1 FY27 vs the FY26 baselines — confirm nothing was dropped vs the investor deck).
- NEUTRAL-FACT (logged, no question): F14-1 (15% vs 14.9% rounding in the CMD quote).
