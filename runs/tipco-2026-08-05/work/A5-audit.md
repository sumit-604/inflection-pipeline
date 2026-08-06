# A5 — Adversary / Completeness Audit — TIPCO Board Outcome (Acquisitions), 05 Aug 2026

Doctype under audit: Regulation 30 Board Outcome (corporate action). Reg 33 results-protocol
checks (segments, auditor paragraphs, Board-Outcome-beyond-item-1, PAT bridge, tax rate) have
no analog here and are correctly not applied. Audit re-derived independently from the A1 spine;
A3/A4 cites were re-checked, not trusted.

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)
Plain-language brief present at review L62-71 with all four labelled parts non-empty:
| Part | Location | Status |
|---|---|---|
| (1) Summary narrative (10-20 lines) | L62-67 (three paragraphs + Net) | PRESENT |
| (2) SECTOR intelligence | L69 | PRESENT |
| (3) BUSINESS-MODEL intelligence | L70 | PRESENT |
| (4) COMPETITION intelligence | L71 ("not addressed; no peer data — provenance: none") | PRESENT |
Note: COMPETITION is thin but is honest, provenanced content (no peer/Notion context loaded this
run), not a placeholder. Gate PASSES.

## 1. COVERAGE AUDIT
Fresh grep/read pass over the spine (174 lines, 6 pages) diffed against A2 ledger.

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Board approvals (cover) | 2 | 2 (L20-24, L25-30) | none | PASS |
| Annexures | 2 | 2 (Ann I L48-114, Ann II L116-174) | none | PASS |
| Annexure particulars (each) | 10 | 10 + 10 (S.No 1-10 both) | none skipped | PASS |
| Turnover history rows | 6 | 6 (Ranks 3: L112-114; Hanu 3: L172-174) | none | PASS |
| Considerations | 2 | 2 (L95, L156) | none | PASS |
| Cover-letter DUs (0.1-0.9) | 9 | 9 | see below | PASS |

Ledger-row-to-review trace (every substantive row cited in A4 or reviewed-no-finding):
- DU-0.4 board date → review header + L11. DU-0.5/0.6 approvals → review table L13-21.
- DU-0.7 board timing 30 min → flag L37. DU-0.8 signatory Sonia Sharma → flag L37 / Q7 L52.
- DU-0.9 "Formerly Known as ... Private Limited" → C11 context / Q8 L53.
- DU-1/DU-2 all 10 particulars each → review table + flags + arithmetic.
- DU-0.1 (BSE addressee), 0.2 (Symbol/Scrip/ISIN), 0.3 (subject line) are non-substantive
  identification metadata; reviewed, no finding. Not analytical orphans.

No ledger row is un-reviewed. No fresh unit found that the ledger lacks. No invented fact in the
review: seller identity, incorporation/establishment dates, arm's-length wording, and the
"no valuer named" absence all trace to the spine (verified below). COVERAGE PASS.

## 2. ARITHMETIC AUDIT
Raw spine figures: Ranks consideration ₹1,31,62,900 (=13,162,900) / 10,000 sh / 50% (L95, L70-71,
L97-98); Ranks FY26 turnover ₹11,11,10,002 (=111,110,002) (L65, L114). Hanutech consideration
₹1,66,59,971 (=16,659,971) / 50% (L156, L158-160); Hanutech turnover FY24 143,936,075, FY25
167,724,091, FY26 195,383,559 (L172-174).

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Ranks price/share | ₹1,316.29 | 13,162,900 / 10,000 = 1,316.29 | L95, L97 | TIES |
| Ranks implied 100% value | ₹2.63 cr | 13,162,900 × 2 = 26,325,800 | L95 | TIES |
| Ranks P/S (whole/FY26 sales) | ~0.24x | 26,325,800 / 111,110,002 = 0.2369 | L95, L65/114 | TIES |
| Hanutech implied 100% value | ₹3.33 cr | 16,659,971 × 2 = 33,319,942 | L156 | TIES |
| Hanutech P/S | ~0.17x | 33,319,942 / 195,383,559 = 0.1705 | L156, L174 | TIES |
| Combined cash outflow | ₹2,98,22,871 (~2.98 cr) | 13,162,900 + 16,659,971 = 29,822,871 | L95, L156 | TIES |
| Hanutech CAGR FY24-26 | ~16.5% | (195,383,559/143,936,075)^(1/2) − 1 = 0.1651 | L172-174 | TIES |
| Hanutech YoY (steady) | ~16.5% | FY24→25 = 16.53%; FY25→26 = 16.49% | L172-174 | TIES |

No mismatch above rounding. ARITHMETIC PASS.

## 3. ADVERSARIAL READ
Line-cite integrity check on the load-bearing claims:
- RPT / seller identity: "from Mr. Ritesh Sharma, who is the Promoter and Managing Director"
  — Ranks L71-72, Hanutech L130-131. Review claim MATCHES.
- Incorporation/establishment dates: Ranks inc. 03 Mar 2025 (L56-57, L102); Hanutech Deed dated
  12 Jan 2021 / Date of Establishment 12 Jan 2021 (L124-125, L168). Review MATCHES (correctly
  labels Ranks "incorporated" and Hanutech a partnership "formed/established").
- "Arm's length": asserted only — "would be undertaken on an arm's length basis" (L73-76,
  L133-136), no supporting evidence. Review's "asserted, not evidenced" MATCHES.
- "No valuer named": fresh grep for valuer/valuation/registered valuer over the full spine
  returns ZERO matches. Absence confirmed. Review claim MATCHES.
- Governance: Sonia Sharma WTD (L43) shares surname with Ritesh Sharma (L71); relationship not
  disclosed in spine — MATCHES. 30-minute board meeting (L31, 07:00-07:30 PM) — MATCHES.

Strongest bear counters to the three most positive claims, tested against the extract:
1. "Prices look cheap (<0.25x sales), pro-minority direction." Counter: low P/S with only turnover
   disclosed (no PAT/EBITDA/net worth/debt, L65/114/172-174) can equally signal thin/negative
   margins or debt-laden targets. SURVIVES — but already grafted in review L28, L34, mitigant 10.
2. "Strategically coherent / adjacent lines." Counter: adjacency rests on the issuer's own objects
   language (L79-83, L139-143), unverified; Ranks at ~17 months with ₹11 cr sales (L56/114) could
   be a seeded/novated shell. SURVIVES — already grafted in flag 4 (L35) and Q4 (L49).
3. "Hanutech is a real business, steady ~16.5% growth." Counter: growth is unaudited turnover only;
   rising sales with unknown/negative margins is not value. SURVIVES — already grafted via C3 /
   flag 3 (L34) and the "not yet interpretable" caveat (L28).
All three surviving counters are ALREADY incorporated in A4's symmetric flags. No un-incorporated
bear counter remains. No graft-back to A4 required.

## VERDICT
VERDICT: COMPLETE
All four brief parts present; coverage reconciles with no orphan/missing rows; every derived number
ties to spine figures within rounding; every claim, flag, and management question traces to a valid
line cite that says what the review claims. No loop-back required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "TIPCO"
quarter: "2026-08-05-corporate-action"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
