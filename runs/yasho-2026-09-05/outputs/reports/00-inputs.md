# B00 — Input Validation & Corpus Audit — YASHO 2026-09-05

Orchestrator-run stage 0 (validation done by the orchestrator per run-pipeline).
manifest.yaml present and parses. inputs/ tree non-empty. Run proceeds.

## Folder inventory (by subfolder, not filename)
| Folder | Count | Note |
|---|---|---|
| prospectus | 0 | Long-listed (BSE SME 2018, main board ~2021). Prospectus NOT expected; not a gap. |
| annual-report | 2 | AR FY2026 (primary, latest audited), AR FY2025 (backward baseline). Contract is 0-1; extra year kept for stage-3 backward dive. |
| results | 0 | GAP. No quarterly results PDFs. Gate 0 extracts from screening Data_Sheet + AR financials + the Q1FY27 investor presentation figures. Stage 10 latest-period fields marked unresolved where no filing backs them. |
| rating | 0 | GAP. No rating PDF/rationale. Presentation reports a CRISIL/ICRA upgrade BBB+ -> A- (pres p.12); that is presentation-sourced, not a rating rationale. Stage 10 rating_wc_quote unresolved; Pillar 2 defaults conservative. |
| concalls | 4 | Nov-2025 (Q2FY26), Feb-2026 (Q3FY26), May-2026 (Q4FY26), Aug-2026 (Q1FY27). concalls_available: true. Contract caps stage 5 at 3 most recent -> Feb/May/Aug 2026, oldest first. Nov-2025 retained as extra promise/delivery context. |
| peer-concalls | 11 | CAMLINFINE x4, FINEORG x3, NOCIL x4. Feeds stage 6. |
| announcements | 0 | GAP. No Reg 30 / exchange filings. Documented-ACTION record absent; stages 5/7/8 intent-and-action cross-check runs on concall+AR only; stage 8 leans on web search. |
| shareholding | 0 | GAP. No quarterly shareholding filing. Presentation p.18 (30-Jun-2026): Promoters 67.94%, Public 24.11%, FII 5.74%, DII 2.21% — presentation-sourced, not a filing. Stage 10 FII+DII treated as pres-derived; UA institutional-absence qualifier cannot be filing-affirmed, so UA withheld unless a stage anchors it. |
| research | 0 | No broker notes. No effect on anchored evidence (research is never anchored). |
| screening | 24 | 4 entities x 6 CSVs. YASHO P&L/BS/CF/Quarters CSVs are the known collect_to_repo v3 defect: header-only, no data. Only YASHO Data_Sheet.csv populated (63 rows). Gate 0 uses Data_Sheet + AR. Peer CSVs to be used as available. |
| presentation | 1 | Q1FY27 investor presentation (filed to BSE/NSE 31-Jul-2026). |
| other | 0 | none |

## Freshness Pair Check (four pairs)
| # | Pair | Trigger present? | Mate | Status |
|---|---|---|---|---|
| 1 | Newest results -> same-quarter concall | No results filing in inputs/results/ | n/a | PASS (not triggered; results folder empty) |
| 2 | Rating bulletin -> full rationale | No rating filing | n/a | PASS (not triggered) |
| 3 | Referenced SEBI order -> order text | No SEBI order referenced in AR/concalls corpus | n/a | PASS (none referenced) |
| 4 | AR not older than latest audited annual results | AR FY2026 present; no newer audited annual result in corpus | AR FY2026 is latest annual | PASS |

freshness_verdict: FRESHNESS PAIRS OK.
Corpus audit verdict: CORPUS GAPPED (plain) — gaps in results, rating, announcements, shareholding; not a freshness gap. Gate recommendation NOT capped by freshness. Gaps degrade per the DEGRADATION MAP and go on the operator's Halt 1 upload list.

## Empty-folder confirmation (SUPPRESSED per Step-1 AUTONOMY CONTRACT)
Standing answer: proceed with the gaps. Empty folders: results, rating, announcements, shareholding, research. No prospectus gap (long-listed). Recorded here; no operator pause.

## COMPANY MEMORY carried to every stage
companies/YASHO.md (Spear OVERRIDE 2026-09-05) + runs/yasho-2026-09-05/step1-business-brief.md load-bearing facts (guidance-vs-delivery, margin step-up durability, cash conversion, MNC-contract concentration). Weighed, never anchored.

```yaml
stage: B00-inputs
company: YASHO
run_date: 2026-09-05
model: orchestrator
status: complete
input_gaps:
  - results (no quarterly results PDFs; Gate 0 from Data_Sheet + AR + Q1FY27 presentation)
  - rating (no rating rationale; A- upgrade is presentation-sourced only)
  - announcements (no Reg 30 documented-ACTION record)
  - shareholding (no filing; holding pattern is presentation-sourced)
  - screening_csv_partial (YASHO P&L/BS/CF/Quarters CSVs empty; only Data_Sheet populated — collector v3 defect)
freshness_pairs:
  - {pair: results_to_concall, trigger_doc: none, mate_expected: same_quarter_concall, status: PASS, missing_doc: none}
  - {pair: rating_bulletin_to_rationale, trigger_doc: none, mate_expected: rating_rationale, status: PASS, missing_doc: none}
  - {pair: sebi_order_to_text, trigger_doc: none, mate_expected: order_text, status: PASS, missing_doc: none}
  - {pair: ar_to_latest_audited_annual, trigger_doc: AR_FY2026, mate_expected: not_older_than_latest_annual, status: PASS, missing_doc: none}
freshness_verdict: FRESHNESS PAIRS OK
corpus_verdict: CORPUS GAPPED
listed_status: long-listed (prospectus not expected)
sector_cap_row: "Specialty chemicals"
flags: []
analyst_note: "Two ARs present (FY25+FY26); stage 5 capped at 3 most recent concalls (Feb/May/Aug 2026 oldest-first), Nov-2025 extra. YASHO screening P&L/BS/CF/Quarters empty (collector defect); Gate 0 leans on Data_Sheet + AR + Q1FY27 pres. Holding and rating are presentation-sourced, not filings."
```
