# B12d — Verifier D: Peer Coverage Audit
Company: Venus Remedies Ltd (VENUSREM) | Run date: 2026-09-02
Auditing: outputs/reports/06-peers.md + outputs/blocks/B06-peers.yaml, against the
23 raw peer transcripts in inputs/peer-concalls/ and the 7-question peer_questions
list injected by B05 (05-concall.md, Section 4B).

Scope note: B06 operates against 23 peer transcripts (7 tickers x 2-4 quarters
each: BETA, CAPLIPOINT, GLAND, KILITCH, LINCOLN, SHILPAMED, WOCKPHARMA), not the
12-transcript baseline named generically in the Verifier D prompt template. This
audit follows the actual artifact set (23 transcripts) as instructed in the task
message. Tooling note confirmed: Grep silently respects the run folder's
.gitignore on inputs/**/*.txt; an explicit glob:"*.txt" override was required and
used throughout this audit, matching B06's own documented workaround.

---

## 1. Corpus confirmation

Directory listing (glob override) confirms all 23 files present, matching B06's
Part 3 coverage map exactly by ticker and quarter: BETA (Nov24/May25/Nov25/May26),
CAPLIPOINT (Nov25/Feb26/May26/Aug26), GLAND (Nov25/Feb26/May26/Aug26), KILITCH
(Jun23/Jun24), LINCOLN (May24/Feb26), SHILPAMED (Nov25/Feb26/May26/Aug26),
WOCKPHARMA (Feb23/Jun25/Jun26). No file named in B06 is missing; no unlisted file
exists in the directory. B06's "23 of 23 read" claim is confirmed.

Two corpus-wide negative claims independently re-run and confirmed:
- "Venus" / "Venus Remedies": zero hits across all 23 files (direct grep,
  case-sensitive on "Venus", no matches). Confirms Claim 5 and 2D "informative
  silence" findings.
- "Red Sea" / "Suez": zero hits across all 23 files (case-insensitive). Confirms
  the Claim 7 informative-silence finding, the single most consequential claim in
  B06's Part 4 summary.
- "Intas": exactly 4 files match — BETA Nov24, BETA May25, KILITCH Jun23, KILITCH
  Jun24 — precisely the four citations B06 uses for Claim 5 circumstantial
  context. No other file contains "Intas"; B06 did not over- or under-claim this.

---

## 2. Citation spot-checks (SUBSTANTIVE claims, extraction-marker page verified)

Methodology: for each checked quote, the claimed page was checked against the
file's own `===== PAGE n of N =====` extraction markers (the anchor convention
B06 states it uses), by locating the source line and interpolating between
marker lines.

| # | Peer / quarter | B06 citation | Quote located | Extraction-marker page | Verdict |
|---|---|---|---|---|---|
| 1 | GLAND Feb 2026 | p.10 | "running out... next 1-1.5 years... Lyo capacities"; "most of the lines are at 90% capacity" | p.10 | MATCH |
| 2 | BETA May 2026 | p.8 | "In Lyo... we are using around 85%... planning to install two more Lyo's" | p.8 | MATCH |
| 3 | BETA May 2026 | p.19 | "Carboplatin NPPA price is INR2850... costing... INR2300, INR2400... no margins for hospitals" | p.19 | MATCH |
| 4 | CAPLIPOINT May 2026 | p.16 | "it is in the region of 20%-30%" (China outsourcing); "less than 1.5% to 2%" (RM/COGS impact) | p.16 (both) | MATCH |
| 5 | GLAND Aug 2026 | p.6 (Claim 4) | "in-licensing agreement with a China-based development company... liposomal product" | p.6 | MATCH |
| 6 | GLAND Aug 2026 | p.4-5 (2E) / p.5-6 (Claim 6) | "impacted by supply disruptions in Saudi Arabia"; "NUPCO tenders... delayed" | p.4 | MATCH (2E); Claim-6 citation (p.5-6) is one page off the true anchor (p.4) — MINOR |
| 7 | SHILPAMED Aug 2026 | p.12-13 | "recent political situation globally -- raw material prices have gone up" | p.13 | MATCH |
| 8 | LINCOLN Feb 2026 | p.7 | "we had an audit from EU Germany, but Germany was full. So now we are targeting even Hungary" | p.7 | MATCH (exact) |
| 9 | SHILPAMED Nov 2025 | p.8-9 | "USFDA is here for the final inspection at our Jadcherla plant" (question) | p.9 | MATCH |
| 10 | CAPLIPOINT Feb 2026 | p.11 | "the freight cost as a percentage of turnover has also come down" | p.11 | MATCH (exact) |
| 11 | CAPLIPOINT Aug 2026 | p.10-11 (2A/2C) | "booked out till almost February of next year"; "running 5 sterile lines and moving towards 17" | p.11 and p.9 respectively | Both quotes genuine; the "17 lines" quote sits on p.9, one page outside the cited p.10-11 range — MINOR |
| 12 | KILITCH Jun 2023 / Jun 2024 | (Intas as named client) | "Intas" appears in both files | confirmed present | MATCH |

12 of 18 SUBSTANTIVE-marked peer-quarter rows directly citation-checked (67%
coverage by row; the checked rows are weighted toward the claims carrying the
most decision weight in B06's Part 4 — Claims 2, 3, 4, 7, and the 2E risk
register). Zero fabricated or non-findable citations. Two MINOR page-anchor
imprecisions found (items 6 and 11 above); in both cases the underlying quote is
genuine, correctly attributed to the right company and quarter, and locatable
within one page of the cited anchor — not a source-fidelity failure, but a
precision gap worth naming. Not independently re-checked in this pass: BETA Nov
2024, BETA Nov 2025, BETA May 2025, GLAND Nov 2025, GLAND May 2026, SHILPAMED Feb
2026, WOCKPHARMA Jun 2026 (content spot-checked for the China Q&A, page not
verified).

---

## 3. UNUSED / CITED-ONLY audit (did B06 miss anything claim-relevant)

Read in full or targeted-searched against all seven claims and the five Part-2
cross-read themes.

**CAPLIPOINT Nov 2025 (UNUSED)** — Full read. Confirms B06's "no matches" call
for the seven claims. One adjacent, minor data point not in B06: management
states tariff "status quo remains... generic products are not tariff" and "we
are in the same boat as everybody else" — a live, contemporaneous (Nov 2025)
negative data point on the same US-tariff risk theme B06 later sources from
CAPLIPOINT's Aug 2026 call. Not citing it is defensible (UNUSED is the right
top-line label; the tariff line is industry-context, not claim-decisive) — MINOR,
not MAJOR, per the rubric's own industry-context-miss standard.

**LINCOLN May 2024 (UNUSED)** — Full read. Confirms B06's call: no China, no
Red Sea/freight, no lyophilisation, no platinum content; predates the industry
conditions in question, consistent with B06's own explanation. No finding.

**SHILPAMED May 2026 (labeled CITED-ONLY, "nothing decisive for any claim")** —
Full read. This label is WRONG. The transcript contains two directly
claim-relevant statements B06 did not surface:
1. p.15: asked directly about RM/key-starting-material supply-chain
   disruption, CFO Alpesh Dalal answers "we don't see any major challenges on
   that, but only the prices have gone up significantly" — a third independent
   peer (after BETA's Carboplatin/NPPA squeeze and SHILPAMED's own Aug 2026
   "political situation... raw material prices have gone up") corroborating
   the general input-cost-inflation direction underlying Claim 3 and the 2B
   cross-read theme. It reinforces an existing finding (SHILPAMED's own Aug
   2026 statement) rather than introducing a new peer, which is why this is
   MAJOR rather than CRITICAL — it does not change a verdict, but it is a
   directly claim-relevant statement left unused, which the rubric (rule 3)
   grades MAJOR on its face.
2. p.16: asked about the Jadcherla USFDA situation directly, management states
   "majority of products which are being sold in U.S. are now being done from
   third-party CMO sites... There is no issue with the FDA... we are again
   waiting for the reaudit... it will not have any impact on our revenues" —
   this is a materially more current and more complete answer on the same
   Jadcherla risk thread B06 does track (via SHILPAMED Nov 2025 and Feb 2026),
   filling the timeline gap between those two calls and the Aug 2026 call. Its
   omission understates continuity of the risk and the mitigation management
   describes (CMO substitution), which is relevant to how the operator should
   weigh the 2E risk item.
Net effect: SHILPAMED May 2026 should have been classified SUBSTANTIVE, not
CITED-ONLY, and both statements belong in Claim 3/2B and 2E respectively.
**MAJOR finding.**

**WOCKPHARMA Feb 2023 / Jun 2025 (CITED-ONLY)** — Targeted search across all
seven claim keywords plus China/lyophilisation/platinum/freight/tariff/Saudi.
Confirms B06's characterization exactly: Feb 2023 contains only the China
in-licensing deal (Jemincare) and TAM background; Jun 2025 contains only the
Saudi BMP regulatory-approval background. Both correctly downgraded from
SUBSTANTIVE; no miss.

---

## 4. Verdict-discipline audit

Rule 4 (≥2 independent peer anchors required for VERIFIED; single-peer VERIFIED
is MAJOR): B06 records **zero VERIFIED claims** — all seven claims land at
PARTIALLY VERIFIED (3) or UNVERIFIABLE (4), so this failure mode cannot occur
in this report. Checked the three PARTIALLY VERIFIED claims for correct peer
counts: Claim 2 (lyophilisation) cites 2 independent peers (GLAND, BETA) —
correctly not upgraded to VERIFIED because the specific "~2x" magnitude is
unconfirmed by either; Claim 3 (platinum) cites 1 peer (BETA) — correctly held
at PARTIALLY VERIFIED, not VERIFIED, per the report's own stated one-peer cap;
Claim 4 (China+1) cites a split, contradictory peer set (BETA, CAPLIPOINT vs.
GLAND) and is correctly labeled "mixed/complicating" rather than either
VERIFIED or CONTRADICTED. No verdict-discipline violation found; the report is
conservative in exactly the direction the rubric rewards.

Rule 5 (every injected peer_questions claim receives a verdict): B05 Section 4B
lists exactly 7 questions for stage-6 peer verification. B06's seven claims map
1:1 to these seven questions (injectable CAGRs / lyophilisation / platinum /
China+1 / named CM counterparties / first-ever registrations / freight-Red
Sea), each with a stated verdict. **All 7 addressed. No skipped claim.**

---

## 5. Findings summary

| Severity | Item | Location |
|---|---|---|
| MAJOR | SHILPAMED May 2026 mischaracterized CITED-ONLY ("nothing decisive"); contains a directly claim-relevant RM/input-cost corroboration (Claim 3 / 2B) and a Jadcherla continuity update (2E) that were left unused | B06 Part 3 coverage map row "SHILPAMED, May 2026"; source: SHILPAMED-Concall_May_2026_Transcript.txt p.15-16 |
| MINOR | GLAND Aug 2026 page citation inconsistency: Claim 4 cites p.6 (correct) but Claim 6 context cites p.5-6 for the same Saudi/NUPCO material actually anchored at p.4 | B06 Part 1, Claim 6 |
| MINOR | CAPLIPOINT Aug 2026 "5 sterile lines to 17" quote cited within a p.10-11 range; actual anchor is p.9 (the "booked out" quote is correctly at p.11) | B06 Part 2A / Part 3 coverage map |

No CRITICAL findings. No fabricated citations. No verdict upgraded from
silence. No claim in the peer_questions handoff skipped.

---

## 6. Overall assessment

B06 is a well-anchored, appropriately conservative peer-triangulation report.
Every spot-checked SUBSTANTIVE citation resolves to a genuine, correctly
attributed quote in the named transcript; the report's two headline
findings — the Red Sea/Suez informative silence (Claim 7) and the
lyophilisation-tightness corroboration (Claim 2) — both independently
reproduce under a fresh full-corpus search. Verdict discipline is sound: zero
claims were inflated to VERIFIED, and the one-peer and split-peer situations
are correctly capped at PARTIALLY VERIFIED. The primary defect found in this
audit is a single coverage-map misclassification (SHILPAMED May 2026,
CITED-ONLY instead of SUBSTANTIVE) that undercounts peer utilisation by one
transcript and omits two claim-relevant statements, neither of which would
have changed a verdict but both of which belong in the record. A secondary,
cosmetic pattern of one-page citation drift (2 of 12 checked citations) does
not rise to a source-fidelity failure.

---

```yaml
stage: B12d
company: "VENUSREM"
run_date: "2026-09-02"
model: claude-sonnet-5
status: complete
peers_audited: 23
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant:
  - {peer: "SHILPAMED", missed_item: "May 2026 call mischaracterized CITED-ONLY ('nothing decisive for any claim'); contains RM/input-cost price-increase corroboration relevant to Claim 3 (platinum/API cost drag) and 2B pricing theme, plus a Jadcherla USFDA audit continuity update relevant to the 2E risk register", anchor: "SHILPAMED-Concall_May_2026_Transcript.txt p.15 (RM cost) and p.16 (Jadcherla Q&A)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", item: "SHILPAMED May 2026 coverage-map label wrong (CITED-ONLY should be SUBSTANTIVE); two claim-relevant statements left unused", location: "B06 Part 3 coverage map"}
  - {severity: "MINOR", item: "GLAND Aug 2026 page citation drift: Claim 6 cites p.5-6, true anchor p.4 (2E citation for the same material, p.4-5, is correct)", location: "B06 Part 1 Claim 6"}
  - {severity: "MINOR", item: "CAPLIPOINT Aug 2026 '5 to 17 sterile lines' quote cited within p.10-11 range, true anchor p.9", location: "B06 Part 2A / Part 3"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 96
peer_utilisation: "18/23 substantive as classified by B06 (78%); audit finds 19/23 (83%) warranted given the SHILPAMED May 2026 misclassification"
```
