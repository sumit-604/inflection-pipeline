# FORENSIC NOTES — Concall Transcript — UFBL Q1 FY27
Agent: A3 | Model: claude-opus-4-8 | Doctype: concall | Company: United Foodbrands Limited (UFBL) | Quarter: Q1 FY27
Inputs: extract_concall_ufbl_q1fy27.txt (1218 lines) + ledger_concall_ufbl_q1fy27.md
Ledger reconciliation: 100% — every A2 row (P1-P17 participants, 63 turns, 22 questions, MN1-MN88, FH1-FH14) read verbatim at its cited line before judging.

Doctype applicability note: on a concall F6/F7/F17 are the live checks; balance-sheet / auditor / entity-list / OCI / tax / share-count checks (F1-F5, F8-F13, F15) have no source object in a transcript and are marked N.A. with a one-line reason. F14 is adapted to transcript drafting/governance data points. F16 is presentation-only.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/turn | verbatim quote (short) | classification | forward implication |
|----|-------|----------------|-----------|------------------------|----------------|---------------------|
| F6-1 | F6 | FH1 / MN44 | L385, turn 4 | "We are committed to reaching 300 restaurants by FY27" | FORWARD-SIGNAL | Hard dated store-count promise; Role 5 promise-vs-delivery anchor for FY27 close. |
| F6-2 | F6 | MN30 | L293-294, turn 4 | "15 restaurants that are under construction, and these will operationalize through Q2 and Q3" | FORWARD-SIGNAL | Datable milestone; if <15 open by Q3 FY27, expansion slippage. |
| F6-3 | F6 | MN82 / FH10 | L1048-1050, turn 52 | "We guided previously capex for full year would be around INR140 crores" | FORWARD-SIGNAL | Reaffirmed (not raised) despite store-target and ~600 capacity talk; funding envelope fixed. |
| F6-4 | F6 | FH2 | L190-191, L362-364, L400-402, turns 3-4 | "funded largely through our internal accruals" (repeated 3x) | FORWARD-SIGNAL | Thrice-repeated = pre-empting an equity-raise question; watch net debt trajectory vs 140cr capex. |
| F6-5 | F6 | MN26 | L286-288, turn 4 | premium CDR Q4 cohort "expected to lift the segment restaurant operating margin as we move further in the year" | FORWARD-SIGNAL | Dated (FY27) margin-lift promise; trackable at Q2/Q3. |
| F7-1 | F7 | FH7 | L701-702, turn 26 | "rather than chasing a number, I think we should look at what are the margin levers" | FORWARD-SIGNAL | Explicit refusal of double-digit pre-Ind AS EBITDA-margin timeline the analyst asked for. |
| F7-2 | F7 | FH8 | L784-789, turn 33 | "rather than looking at a number for the full year, what's important is to look at how the overall business... is moving" | FORWARD-SIGNAL | Declines to reaffirm Q4's high-single/early-double-digit SSSG guide; management is de-anchoring SSSG. |
| F7-3 | F7 | FH12 | L1138, turn 58 | "I won't comment it is one-off or not" | AMBIGUOUS | Will not defend durability of the 28.7% print — leans to a base-effect fade management already telegraphs (L182, L371). |
| F7-4 | F7 | FH4 / FH6 | L574 & L691, turns 17/24 | "I won't say that the mature portfolio margin caps at 18%" / "8% or 8.5% or 9% or 7.5%... I don't know that right now" | AMBIGUOUS | No numeric mature-margin destination given despite direct asks; open-ended upside claim with no floor/ceiling. |
| F7-5 | F7 | MN75 / narrative | L858-859, turn 36 | "some reversal will happen and some reversal will not happen also" (International GM) | FORWARD-SIGNAL | Concedes part of the International gross-margin hit is permanent, not "temporary" as the deck framed it. |
| F7-6 | F7 | MN83-84 / narrative | L1100-1103, turn 55 | "I don't know which video is there... So I can't comment on that" | AMBIGUOUS | Deflects a specific food-quality/lab allegation; reputational/food-safety risk left unquantified. |
| F14-1 | F14 | TRANSCRIPT_FORMAT_ANOMALY | L933 & L948, turns 43/45 | "Disha Chamriya" (speaker label, no colon) | NEUTRAL-FACT | Vendor (MUFG Intime) formatting defect on 2 of 63 turns; data-quality watch for future transcripts. |
| F14-2 | F14 | THIN_MGMT_PARTICIPATION | L1048 (CFO only turn), turn 52 | CFO speaks once (capex); MD takes zero Q&A | AMBIGUOUS | CFO near-silence is why every finance-detail Notion item (DTA/ETR, vanished investments, net-debt base, TTM) went unaddressed. |
| F14-3 | F14 | MN69 | L746-747, turn 29 | "Second is BBQ, which is more towards meals and bowls" | NEUTRAL-FACT | "BBQ" is used both as a distinct delivery brand and as shorthand for "BBQ India" (e.g. L983) — nomenclature ambiguity in the numbers. |
| F17-1 | F17 | MN1 / MN16 + checklist#1 | L130 & L222, turns 3/4 | "Consolidated same-store sales growth for the quarter was 28.7%" | AMBIGUOUS | Call restates 28.7% but never reconciles the deck's 4.7% figure on its own 12-yr chart; base contradiction left open. |
| F17-2 | F17 | MN88 vs MN10/MN22 + checklist#1 | L1139-1140 vs L256, turn 58 | "Q3 was around 8%... 14.5% in Q4... 28% in Q1" | AMBIGUOUS | A2 labelled this "International," but 28% = consolidated (Int'l Q1 SSSG = 8.5%); management conflates segment/consol in the one-off answer. |
| F17-3 | F17 | MN43 + checklist#3 | L356-358, turn 4 | net debt "moved marginally up from INR102 crores... to INR106 crores" | AMBIGUOUS | "Marginally up 102->106" contradicts deck's "net debt ex-leases doubled to 106.7"; different base/definition unreconciled. |
| F17-4 | F17 | checklist#2 (silence) | (whole call) refusal at L701 | no PAT figure or dated PAT-positive guidance anywhere on call | CONFIRMATORY-NEGATIVE | FY26 was a loss; call gives no dated path to sustained PAT-positive. Sustained silence on the profitability inflection. |
| F17-5 | F17 | checklist#5 (silence) | (whole call) | ₹12.1 Cr non-current Investments -> nil never mentioned | CONFIRMATORY-NEGATIVE | Balance-sheet item that vanished is not explained; CFO domain, CFO barely spoke (see F14-2). |
| F17-6 | F17 | checklist#7 (silence) | (whole call) | ETR ~4.2% / ₹59.6 Cr DTA never mentioned | CONFIRMATORY-NEGATIVE | No normalisation / EPS-drag discussion; future ETR step-up risk unaddressed. |
| F17-7 | F17 | checklist#8 (silence) | (whole call) | ₹17,036 Mn annualised vs FY26 ₹13,387 Mn never mentioned | CONFIRMATORY-NEGATIVE | Annualisation/TTM optics not addressed; annualising a peak quarter is left standing. |
| F17-8 | F17 | MN86 + checklist#6 | L1078 & L1084-1089, turn 55 | "that number is intact" / NPS "improving over the last 3 months" | CONFIRMATORY-NEGATIVE | GSI/NPS still disclosed only qualitatively; no score given on deck or call across coverage. |
| F17-9 | F17 | MN87 + checklist#4 | L1133-1135, turn 58 | International "gross margin is lower by around 3 percentage points" | FORWARD-SIGNAL | Partly resolves checklist#4: hit now quantified (~3pp, commodity +30-40%) but recovery hedged (see F7-5). |
| F17-10 | F17 | checklist#3 (silence) | (whole call) | FY30 400-425 store target never mentioned | CONFIRMATORY-NEGATIVE | Call gives only FY27 (300) and a ~600 capacity ceiling; the deck's FY30 400-425 target is absent — no funding envelope tied to it. |

---

## 2. CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | No financial-statement line items in a transcript; no ZERO_STANDING rows (A2 §6 confirms none). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No S-vs-C tables; only spoken consolidated/segment numbers. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines (materials/employee/depreciation) to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters paragraph in a concall. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No EoM / going-concern language present. |
| F6 FORWARD-COMMITMENT MINING | FINDING | 5 dated commitments extracted (F6-1..F6-5); see Commitment Register §3. |
| F7 HEDGE PHRASE MINING | FINDING | Systematic refusal to quantify forward SSSG/margins across repeat questions + deflection on food-quality allegation (F7-1..F7-6). |
| F8 TAX FORENSICS | N.A. | No ETR/deferred-tax data spoken; the ₹59.6 Cr DTA silence is logged as F17-6, not here. |
| F9 OCI FORENSICS | N.A. | No OCI/actuarial data in transcript. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital or EPS discussed. |
| F11 RESERVES / NET WORTH | N.A. | No net-worth reconciliation; only net debt (logged as F17-3). |
| F12 SEGMENT FORENSICS | N.A. | Segment revenue/margin narrated, but no segment assets/liabilities to trend. |
| F13 BOARD OUTCOME | N.A. | No board agenda / AR / AGM / director-term content in a transcript. |
| F14 DRAFTING / GOVERNANCE INCONSISTENCIES | FINDING | Transcript format anomaly (F14-1), thin mgmt participation (F14-2), "BBQ" dual nomenclature (F14-3). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list present. |
| F16 PRESENTATION-SPECIFIC (dropped/reframed) | N.A. | Doctype is concall, not deck; SSSG reframing captured under F7-2 / F17-1. |
| F17 CONCALL SILENCE AUDIT | FINDING | 6 of 8 Notion monitoring items unaddressed or qualitative-only; 3 cross-doc contradictions (F17-1..F17-10). |

Gate A3: every F1-F17 carries exactly one status; no blanks. PASS.

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | turn/line ref | status word |
|------------|--------------|---------------|-------------|
| Reach 300 restaurants (net +40 in FY27; FY26 added ~35) | FY27 | turn 4 / L385-386; turn 21 / L626 | committed / underway |
| 15 restaurants under construction operationalize | Q2 & Q3 FY27 | turn 4 / L293-294 | underway |
| FY27 total capex ~INR140 cr (~120 new outlets, ~20 maintenance) | FY27 | turn 52 / L1048-1050 | reaffirmed |
| Expansion funded largely from internal accruals | ongoing | turns 3-4 / L190, L362-364, L400-402 | reaffirmed (x3) |
| Premium CDR Q4 FY26 cohort to lift segment ROM | through FY27 | turn 4 / L286-288 | underway |
| BBQ India capacity re-rated to ~600 restaurants (was ~400-450) | no date (capacity estimate) | turn 7 / L442-443 | estimate (not a firm target) |
| Gross-margin / mature-ROM / new-cohort / back-end levers "expect to continue delivering throughout the year" | FY27 | turn 4 / L378-382 | soft guidance |

---

## 4. FLAGGED-INPUT DISPOSITION (A2 flags investigated)

- TRANSCRIPT_FORMAT_ANOMALY -> F14-1: confirmed formatting defect only (L933, L948), no content gap.
- THIN_MGMT_PARTICIPATION -> F14-2: CFO one turn (L1048), MD zero Q&A; directly explains the finance-item silences (F17-5/6/7).
- REPEAT_QUESTION -> F7-2/F7-3 + cross-ref: three analysts (Q12 L768, Q18 L974, Q21 L1127) probe SSSG durability; all get consistently hedged, non-numeric answers (FH6/FH7/FH8/FH12) — consistency-of-hedge pattern for A4/A5.
- FORWARD_GUIDANCE -> F6-1/F6-3 + Commitment Register: 300 stores, ~600 capacity, ~140cr capex all logged and datable.
- HEDGE -> F7-1..F7-4: refusals to quantify forward SSSG and EBITDA/mature margins.

## 5. FOR A4 — FINDINGS TO CONVERT INTO MANAGEMENT QUESTIONS
FORWARD-SIGNAL: F6-1, F6-2, F6-3, F6-4, F6-5, F7-1, F7-2, F7-5, F17-9.
AMBIGUOUS (priority A4 questions): F7-3, F7-4, F7-6, F14-2, F17-1, F17-2, F17-3.
CONFIRMATORY-NEGATIVE (silence, escalate to A5): F17-4, F17-5, F17-6, F17-7, F17-8, F17-10.
