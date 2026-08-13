# A3 FORENSIC NOTES — Asian Energy Services Limited (ASIANENE), Q1 FY27 — doctype: pressrelease

Source extract: `/home/user/inflection-pipeline/runs/asianene-q1fy27/work/extract_pressrelease_asianene_q1fy27.txt`
Reconciled against A2 ledger: `/home/user/inflection-pipeline/runs/asianene-q1fy27/work/ledger_pressrelease_asianene_q1fy27.md`
Prior-quarter baseline: NONE (first quarterly review). Ledger rows read: HN1–HN19, Q1–Q2, FS1–FS8, OC1–OC12, appendix, ZERO-STANDING (=0). Reconciliation: 100%.

Doctype note: this is a 4-page narrative press release (management's chosen framing). Per task scope, F6 and F7 apply FULLY; F16 applies in spirit (no prior baseline; capture this release's framing). Headline-number checks (F1/F2/F8/F10/F11) are run to the extent the number appears. Balance-sheet-deep checks with no data in a press release (F3, F4, F5, F9, F12, F13, F14, F15, F17) are N.A. with basis.

---

## FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| FN1 | F2 | HN8 / HN15 | 89 & 117 | "Performance Highlights Consolidated – Q1 FY27" (89) vs "Asian Energy's standalone order book stood at ₹1,754 crore" (117) | FORWARD-SIGNAL | P&L (rev/EBITDA/PAT) is CONSOLIDATED; the Rs1,754cr order book is STANDALONE. The "multi-year revenue visibility" claim mixes bases. Tripwire 4 (standalone revenue ex-Kuiper vs 30–40% order-backed guide) is NOT verifiable from this release because no standalone P&L is given. A4 must obtain the standalone P&L from the filing before any order-book/revenue coverage ratio is trusted. |
| FN2 | F6 | FS4 | 115–116 | "Approval of Shareholders has been received for the Merger and it is expected to be completed by September/October 2026" | FORWARD-SIGNAL | Directly hits ACTIVE TRIPWIRE 1 (Oilmax reverse merger, 35–51% EPS dilution). Dated commitment: completion Sep/Oct 2026. Release is SILENT on the accounting basis (fair-value vs pooling-at-book) and on the dilution ratio. This date is checkable in the Q2 FY27 ledger; the silence on basis/dilution is a management question for A4. |
| FN3 | F6 | FS1 / FS5 / FS7 | 75, 119–120, 144 | "company on track to achieve growth targets" (75); "declared the preferred bidder for an offshore block and a critical mineral mine" (119–120); "We remain confident of achieving our FY27 guidance for both Asian Energy Services and Kuiper" (144) | FORWARD-SIGNAL | Multiple dateable commitments. Guidance reaffirmed for FY27 (by Mar-2027) but never quantified in absolute terms. "Preferred bidder" = pre-award, not a signed contract; A4 to track conversion to executed order. These feed the Role 5 promise-vs-delivery tracker. |
| FN4 | F7 | OC5 | 141 | "strong execution across all verticals despite volatile Middle East situation" | AMBIGUOUS | Pre-emptive hedge acknowledging an operating-environment / geographic-concentration risk (Kuiper Nigeria / international ops). In a bullish release this is the one downside verb — leans toward revenue lumpiness risk next quarter. Convert to a management question on Middle East / international exposure as % of revenue. |
| FN5 | F16 | HN3 / HN11–HN12 | 73, 96, 98 | "EBITDA at Rs 21.9 crore (▲81% YoY)" | FORWARD-SIGNAL | Reframing/emphasis: the headline touts +81% EBITDA growth but the implied consolidated EBITDA margin FELL from 10.5% (12.1/115.4, Q1FY26) to 8.1% (21.9/271.2, Q1FY27), ~240bps compression — already BELOW the 12% floor in ACTIVE TRIPWIRE 5. No margin figure is stated anywhere in the release (disclosure by omission). A4 must recompute margin from the filing and test tripwire 5 (two consecutive quarters <12%). |
| FN6 | F16 | HN2–HN4 / HN9–HN14 | 73–74, 95–98 | "revenue increasing by 135%… net profit rising by 129%… EBITDA … ▲81%" | AMBIGUOUS | Growth-rate divergence: PAT (+129%) grew far faster than EBITDA (+81%) while EBITDA margin compressed. PAT outpacing EBITDA despite margin fall implies a below-EBITDA tailwind (other income, lower effective tax, or a lower D&A/interest ratio). Not verifiable in a press release (no tax/interest/D&A lines). A4 must decompose EBITDA→PAT bridge from the filing to test earnings quality. |
| FN7 | F16 | HN5 / HN15 / HN16 | 77, 117–118 | "Strong order book of Rs 1,754 crore provides multi-year revenue visibility" (77); "~60% … Oil & Gas, ~40% from Mineral services" (117–118) | AMBIGUOUS | Order-book definition is undefined as to gross/net-of-GST and executed/pending; no prior baseline exists so no trend is checkable this quarter, but the definition is now the baseline for future diff. Segment split is order-book-based (not P&L segment reporting). A4 to pin the order-book definition and confirm the Rs1,754cr is standalone gross. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 | N.A. | Narrative press release with no tabular note structure; A2 ledger ZERO-STANDING count = 0 — no zero/nil/dash line item exists to interrogate. |
| F2 | FINDING | Both bases appear but for different metrics: consolidated P&L (line 89) vs standalone order book (line 117). No same-metric both-basis to compute a gap; basis-mixing flagged (FN1). Tripwire 4 unverifiable without standalone P&L. |
| F3 | N.A. | No standalone-vs-consolidated cost lines (Cost of Materials, Employee Benefits, Depreciation) disclosed in a press release; shell detection not possible. |
| F4 | N.A. | No auditor "Other Matters" / component-auditor disclosure in a press release; unaudited contribution ratio not computable. |
| F5 | N.A. | No auditor report or Going Concern / Emphasis-of-Matter paragraph in a press release; and first quarterly review (no prior EoM to verbatim-diff). |
| F6 | FINDING | Full forward-commitment mining applied. Dated/dateable commitments: merger completion Sep/Oct 2026 (115–116), FY27 guidance "on track"/"remain confident" (75, 144), "preferred bidder" pre-award (119–120), "commenced FY27" (124). See FN2, FN3 and Commitment Register. |
| F7 | FINDING | Full hedge mining applied. One material hedge: "despite volatile Middle East situation" (141) — operating-environment / geographic-concentration cover (FN4). Balance of release is unhedged/bullish. |
| F8 | N.A. | No tax expense, deferred-tax, or ETR line stated in the release (only EBITDA and PAT); ETR vs 25.17% not computable. Note: PAT-vs-EBITDA growth divergence captured under FN6 for A4 bridge work. |
| F9 | N.A. | No OCI / actuarial gains-losses disclosed in a press release. |
| F10 | N.A. | No paid-up capital, share count, or basic/diluted EPS stated. (OEPL 55.99% holding at line 171 is an ownership stat, not a share-count movement; merger dilution risk carried under FN2.) |
| F11 | N.A. | No Other Equity / net-worth / reserves figure stated; no third-party (rating/slide) net-worth number to tie out. |
| F12 | N.A. | No segment assets/liabilities disclosed; the 60/40 split (117–118) is an order-book split, not Ind AS 108 segment reporting. |
| F13 | N.A. | This is a Reg-30 press release, not a Board Outcome letter; no board-meeting times, AR/AGM approval, record date, or director-term dates disclosed (A2 appendix line 94 confirms). |
| F14 | N.A. | No auditor letter or numbered notes to cross-check for audit-vs-review or entity-name inconsistency. (Minor: "EBIDTA" typo at line 142 vs "EBITDA" at 73 — cosmetic, not a note-drafting governance flag.) |
| F15 | N.A. | No consolidation entity list disclosed and no prior quarter to diff (first quarterly review). |
| F16 | FINDING | Applied in spirit. Framing captured: consolidated headline vs standalone order book (FN1); +81% EBITDA growth headline masks ~240bps margin compression to 8.1%, already below tripwire-5 floor (FN5); PAT growth outpacing EBITDA (FN6); guidance "unchanged" but never quantified and order-book definition undefined (FN7). Sets the baseline for future dropped/reframed-disclosure diffs. |
| F17 | N.A. | Not a concall; no transcript. Silence audit against F6 commitments / Notion tripwires is performed inline in the notes below for A4 hand-off, but the check itself is N.A. for this doctype. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|-----------|--------------|------------|-------------|
| Oilmax merger completion | September/October 2026 | 115–116 (FS4) | underway (shareholder approval received; completion pending) |
| Achieve FY27 guidance / growth targets — Asian Energy + Kuiper | FY27 (by Mar-2027) | 75, 144 (FS1/FS7) | underway ("on track" / "remain confident") |
| Convert "preferred bidder" status to signed contract — offshore block + critical mineral mine | undated (pending formal award) | 119–120 (FS5) | initiated (pre-award) |
| Commenced FY27 execution across verticals | Q1 FY27 (done) | 124 (Q1) | completed |

---

## TRIPWIRE SILENCE / RELEVANCE NOTES (hand-off to A4; F17 check itself N.A.)

- Tripwire 1 (Oilmax merger fair-value basis, 35–51% dilution): PARTIALLY addressed — completion date given (FN2), but SILENT on fair-value-vs-pooling basis and dilution magnitude. Question for A4.
- Tripwire 2 (negative CFO / TTM CFO/PAT <0.5x): SILENT — no cash-flow data in release.
- Tripwire 3 (RP receivable ageing >180 days; RP 56.4% of gross book): SILENT — no balance sheet.
- Tripwire 4 (standalone revenue ex-Kuiper vs 30–40% order-backed guide): NOT verifiable — only consolidated P&L given (FN1).
- Tripwire 5 (consolidated EBITDA margin <12% two consecutive quarters; net debt/EBITDA >1.5x): Q1 FY27 implied consolidated EBITDA margin = 8.1% (21.9/271.2), already below 12% (FN5); net debt not disclosed. A4 to recompute from filing and track consecutive-quarter test.

## ARITHMETIC ITEMS FOR A4 TO CHECK AGAINST THE FILING

- Revenue growth: 115.4 → 271.2 = +135.0% (matches stated 135%). OK.
- EBITDA growth: 12.1 → 21.9 = +81.0% (matches stated 81%). OK.
- PAT growth: 5.6 → 12.8 = +128.6% ≈ 129% (matches stated 129% / headline title). OK.
- Consolidated EBITDA margin: Q1FY27 8.07% vs Q1FY26 10.49% — ~242bps compression; verify against filing (FN5).
- Consolidated PAT margin: Q1FY27 4.72% vs Q1FY26 4.85% — roughly flat despite EBITDA-margin fall → below-EBITDA tailwind to reconcile (FN6).
- All headline figures are CONSOLIDATED; order book Rs1,754cr is STANDALONE — do not net or ratio across bases without the standalone P&L (FN1).

```yaml
stage: A3-forensics
company: "ASIANENE"
quarter: "Q1 FY27"
doctype: "pressrelease"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/asianene-q1fy27/work/forensics_pressrelease_asianene_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN1", check: "F2", line: "89 & 117", classification: "FORWARD-SIGNAL", implication: "Consolidated P&L vs standalone order book; tripwire 4 unverifiable without standalone filing P&L"}
  - {id: "FN2", check: "F6", line: "115-116", classification: "FORWARD-SIGNAL", implication: "Merger completion Sep/Oct 2026 (tripwire 1); silent on fair-value basis and dilution"}
  - {id: "FN3", check: "F6", line: "75, 119-120, 144", classification: "FORWARD-SIGNAL", implication: "FY27 guidance reaffirmed but unquantified; preferred-bidder awards pre-contract"}
  - {id: "FN4", check: "F7", line: "141", classification: "AMBIGUOUS", implication: "Middle East volatility hedge signals possible revenue lumpiness / geographic concentration"}
  - {id: "FN5", check: "F16", line: "73, 96, 98", classification: "FORWARD-SIGNAL", implication: "81% EBITDA-growth headline masks ~240bps margin compression to 8.1%, below tripwire-5 12% floor"}
  - {id: "FN6", check: "F16", line: "73-74, 95-98", classification: "AMBIGUOUS", implication: "PAT +129% outpaces EBITDA +81% despite margin fall; below-EBITDA bridge needs filing verification"}
  - {id: "FN7", check: "F16", line: "77, 117-118", classification: "AMBIGUOUS", implication: "Order-book definition undefined (gross/net GST, executed/pending); sets baseline for future diffs"}
forward_signals: ["FN1", "FN2", "FN3", "FN5"]
ambiguous: ["FN4", "FN6", "FN7"]
commitments:
  - {commitment: "Oilmax merger completion", implied_date: "September/October 2026", ref: "line 115-116", status_word: "underway"}
  - {commitment: "Achieve FY27 guidance / growth targets (Asian Energy + Kuiper)", implied_date: "FY27 (by Mar-2027)", ref: "line 75, 144", status_word: "underway"}
  - {commitment: "Convert preferred-bidder status to signed contract (offshore block + critical mineral mine)", implied_date: "undated (pending award)", ref: "line 119-120", status_word: "initiated"}
  - {commitment: "Commenced FY27 execution across verticals", implied_date: "Q1 FY27", ref: "line 124", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
