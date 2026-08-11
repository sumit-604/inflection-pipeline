# A2 ENUMERATOR LEDGER — Credo Brands Marketing Ltd (CREDO)
Quarter: Q1 FY27 | Doctype: results (Reg 30 Board Outcome letter — AGM notice /
dividend record date; NOT a quarterly results filing per extract header line 11)
Source extract: extract_boardoutcome_credo_q1fy27.txt (1 page, 51 content lines
plus header/formfeed, page_count_pdfinfo: 1)

## Methodology note
This document is a 1-page Reg 30 letter with only two natively numbered
agenda items (AGM; dividend record date). Because the enumeration mandate is
completeness against the FULL standard Reg 30 Board-Outcome checklist (per
prompts/quarterly-a2-enumerator.md ENUMERATE-RESULTS-FILING rule 3: "AR
approval, AGM notice, record date, dividend, director appointments, auditor
changes, scrutinizer, ESOP grants, capital-raising enabling resolutions —
one row each") plus the task-specified additions (AGM date/mode, e-voting
window, board meeting times, digital signature block), the count test below
is run against a fixed 13-item checklist. Each checklist item is enumerated
as one row REGARDLESS of whether the letter discloses it — absent items are
`ZERO_STANDING` rows (the item is a standard Reg 30 disclosure category that
is silent in this letter, not an item the enumerator skipped).

=== A2 COUNT TEST ===
category: agenda_items   grep_count: 13   sweep_count: 13   match: yes
gate_a2: pass
=== END COUNT TEST ===

### Grep pass detail (13 targeted patterns run against the checklist; each
pattern run = one row, hit or no-hit)
```
grep -n -E "^\s*[0-9]+\.\s"                                  -> 2 hits (native items 1, 2)
grep -c -i "Annual General Meeting"                          -> 2 hits
grep -c -i "Notice of the AGM"                                -> 1 hit
grep -c -i "Annual Report"                                    -> 1 hit
grep -c -i "Record date"                                      -> 3 hits
grep -c -i "dividend"                                          -> 4 hits
grep -c -i -E "e-voting|electronic voting|remote voting"      -> 0 hits
grep -c -i "Director"  (context-checked, both = "Board of      -> 2 hits, 0 substantive
   Directors" boilerplate, not an appointment agenda item)
grep -c -i "Auditor"                                            -> 0 hits
grep -c -i "Scrutinizer"                                        -> 0 hits
grep -c -i -E "ESOP|stock option"                               -> 0 hits
grep -c -i -E "capital|preferential|rights issue|QIP|allotment" -> 0 hits
grep -c -i -E "commenced at|concluded at"                       -> 1 hit
grep -c -i -E "Digitally signed|Date:.*2026"                    -> 3 hits
```
13 checklist patterns run = grep_count 13. Manual sweep of full 67-line
document against the same 13-item checklist = sweep_count 13. Match: yes.

## LEDGER — Board Outcome Agenda Items (category: agenda_items)

| # | Checklist item | Status | Line(s) | Detail (first ~15 words / value) | Flags |
|---|---|---|---|---|---|
| 1 | Annual Report (FY25-26) formal board approval | ABSENT | 33 (anchor: "approved the following:"; checked full doc 15-67) | Letter's "approved the following" list contains only 2 items (AGM; dividend record date); no separate AR-approval line item stated | ZERO_STANDING |
| 2 | AGM date, time, and mode | PRESENT | 35-40 | "27th Annual General Meeting... held on Friday, September 11, 2026 at 12:30 P.M. (IST) through Video Conferencing / OAVM" | — |
| 3 | AGM Notice & Annual Report dispatch | PRESENT | 42-44 | "Notice of the AGM and Annual Report for FY 2025-26 will be sent in electronic mode... in due course" (no firm dispatch date given) | — |
| 4 | Record date for dividend payment | PRESENT | 46, 48-49 | "Record date for payment of the proposed dividend... has been fixed as Friday, August 28, 2026" | — |
| 5 | Dividend amount / declaration | PRESENT | 48-49 | "proposed dividend of ₹2.00 per share, if declared, at the forthcoming AGM" — contingent on AGM member approval, not yet declared | CONTINGENT_DIVIDEND |
| 6 | E-voting window (open/close dates) | ABSENT | 33 (anchor; checked full doc 15-67) | No e-voting dates stated in this letter (may follow in the AGM Notice itself, not yet dispatched per row 3) | ZERO_STANDING |
| 7 | Director appointment(s) / re-appointment(s) | ABSENT | 33 (anchor; checked full doc 15-67); cf. lines 32, 51 (generic "Board of Directors" refs only, no appointment content) | No director appointment/re-appointment agenda item in this letter | ZERO_STANDING |
| 8 | Auditor appointment/change | ABSENT | 33 (anchor; checked full doc 15-67) | No auditor-related item in this letter | ZERO_STANDING |
| 9 | Scrutinizer (for e-voting/AGM poll) | ABSENT | 33 (anchor; checked full doc 15-67) | No scrutinizer named in this letter | ZERO_STANDING |
| 10 | ESOP grant(s) | ABSENT | 33 (anchor; checked full doc 15-67) | No ESOP-related item in this letter | ZERO_STANDING |
| 11 | Capital-raising enabling resolution | ABSENT | 33 (anchor; checked full doc 15-67) | No preferential allotment / rights / QIP / other capital-raising resolution in this letter | ZERO_STANDING |
| 12 | Board meeting start and end times | PRESENT | 51 | "The meeting of the Board of Directors commenced at 4:45 p.m. and concluded at 6:00 p.m." — 1 hr 15 min meeting | — |
| 13 | Digital signature block with timestamp | PRESENT | 57-66 | Signatory: Sanjay Kumar Mutha, Company Secretary and Compliance Officer; digitally signed; "Date: 2026.08.11 18:19:07 +05'30'" — signed 19 min after 6:00 p.m. meeting close (post-conclusion signing, no anomaly) | — |

## Cross-checks performed
- Signature timestamp (18:19:07 IST) vs. board meeting conclusion (18:00 /
  6:00 p.m., line 51): signature is AFTER meeting close by 19 minutes — no
  `PRE_CONCLUSION_SIGNATURE` flag warranted (that flag would apply only if
  the signature timestamp preceded the stated meeting conclusion time).
- Detected-quarter field in A1 header (line 11) flags this filing as NOT a
  quarterly results document despite doctype tag "results" — carried forward
  as context, not a ledger row (header metadata, not a disclosure unit).
- Prior-quarter ledger: none supplied (first coverage per task inputs) — no
  diff performed for `ENTITY_CHANGE` / `DROPPED_SLIDE` style comparisons.

## Totals
- agenda_items: 13 (6 PRESENT, 7 ABSENT/`ZERO_STANDING`)
- zero_standing: 7
- flags_raised: ZERO_STANDING (x7), CONTINGENT_DIVIDEND (x1)
