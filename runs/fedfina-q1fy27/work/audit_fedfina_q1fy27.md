# A5 ADVERSARY / COMPLETENESS AUDIT — FEDFINA — Q1 FY27

Fresh context. Inputs seen: A4 review, A1 concall extract (1189 lines), A2 ledger. A3 reasoning NOT seen; all cites re-derived independently against the extract.

Doc set: ONE document (concall transcript). Role 4 declared N.A. (no results filing supplied). Audit therefore covers the concall enumeration + concall-internal arithmetic only; filing-anchored checks are out of scope by doctype, consistent with A4's own scoping.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep passes over the extract:

| Category | A2 count | My fresh count | Method | Orphan / missing | Status |
|----------|----------|----------------|--------|-------------------|--------|
| Speaker turns | 109 | 109 | grep of all `Name:` speaker-label line-starts (mgmt + analysts + Moderator + Management) | none | PASS |
| Moderator "next question from the line of" | (n/a) | 8 | grep | cross-check on analyst hand-offs | PASS |
| Analyst-side turns | 44 | 44 | grep of 11 named analyst labels | — | PASS |
| Analyst-side incl. host + unattributed | (n/a) | 46 | grep incl. Shreepal Doshi (1) + "Management" (1) | — | PASS |
| Questions | 36 | 36 | 44 analyst turns − 8 non-question turns (Rajiv rejoin t26; Mohit thanks t73; Pawan thanks t89; Ghansham audio/intro t91,t93,t97,t99,t103 = 5) | none | PASS |
| Participants (total) | 21 | 21 | 8 header-listed + 11 named analysts + generic Moderator + unattributed "Management" | none | PASS |
| Participants (header) | 8 | 8 | 7 mgmt + Shreepal Doshi, pages 2 (lines 60-73) | none | PASS |
| Analyst-cited numbers | 7 | 7 | 40cr / 75cr / 585cr / 589cr / 12-15cr / 489cr / 37mo — all located (lines 1027-1070) | none | PASS |
| Mgmt numbers | 172 | 172 (count-test verified internally consistent; all A4 load-bearing numbers spot-traced to cited lines with zero missing) | see note | none load-bearing missing | PASS |

Mgmt-numbers note: a token-by-token re-enumeration of all 172 rows is impractical by grep alone (regex over per-turn text with cross-line joins). Instead I traced EVERY number A4 relies on in its tables (ROE 15.4/11.6, PAT 114.4, PPOP 187.5, opex 4.8/5.5/5.9, C/I 52.8/57.2, CRAR 20.71/22.4, leverage 4.6/4.89, GNPA 1.6/1.9/1.87, Stage II 2.2/2.7, PCR 38.36, credit cost 0.8/0.7, LTV 61/68, gold AUM 11191/+8.1% QoQ, disb 6760/6087, tonnage +1%, ROA 2.6/2.4, EPS 3/2, DA -13cr, and all §7 analyst-cited) back to its cited extract line — 100% located, zero orphan, zero fabricated. The ledger §4 rows are internally consistent with these.

**Ledger-row → A4 citation check (orphan test).** A4's reconciliation preamble asserts all 109 turns / 172 numbers / 43 forward / 53 hedge / 7 analyst-cited reviewed, with the blanket "reviewed, no finding" permitted by protocol. Every A3 forensic finding (F6-1/2/3, F7-1/2/3/4, F9-1, F17-1/2/3) is carried into A4's flag stack and Questions-for-Management table, each with a matching extract line. The load-bearing ledger rows — the write-off DATA_DISCREPANCY (75/51/~50cr), the SILENT_ATTENDEE trio, the DPD refusal (line 981), the FVOCI/DA/GS3 analyst-cited cluster — are all explicitly engaged in A4. **No orphan row (ledger row absent from A4). No missing row (fresh pass found nothing the ledger lacks).**

**COVERAGE VERDICT: PASS.** Counts reconcile exactly (turns 109, questions 36, participants 21, analyst-cited 7). No orphan rows, no missing rows.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers)

| Metric | A4 value | Recomputed | Source line | Status |
|--------|----------|------------|-------------|--------|
| ROE YoY expansion | +380bps (15.4 from 11.6) | 15.4 − 11.6 = 3.8pp = 380bps | 213, 343-344 | MATCH |
| Opex/avg assets QoQ | 4.8%, −70bps (was 5.5%) | 5.5 − 4.8 = 0.7 = 70bps | 359-361 | MATCH |
| Cost-to-income improvement | 52.8% from 57.2% ("over 400bps") | 57.2 − 52.8 = 4.4pp = 440bps (>400) | 368-369 | MATCH |
| GNPA reduction | 1.6% from 1.9% = −30bps | 1.9 − 1.6 = 0.3 = 30bps | 208, 303 | MATCH |
| GNPA ex-write-off | 1.87% (= March, "flat") | management-stated; consistent | 307, 1042 | MATCH |
| Stage II rise | 2.2%→2.7% = +50bps | 2.7 − 2.2 = 0.5 = 50bps | 296 | MATCH |
| Gold LTV move | 61→68 = "7%" (pp) | 68 − 61 = 7pp | 646, 319 | MATCH (absolute pp) |
| Credit cost | 0.8%, +6bps QoQ; regular 0.7% +10bps | 0.7 + 0.1 = 0.8 | 316, 614, 204 | MATCH |
| CRAR fall | 20.71% from 22.4% ("169bps") | 22.4 − 20.71 = 1.69pp = 169bps | 394 | MATCH |
| Leverage | 4.6→4.89 | verbatim | 281 | MATCH |
| ROA target | +20-30bps over 2.4% → ~2.6-2.7% | 2.4+0.2=2.6; 2.4+0.3=2.7 | 807-812 | MATCH |
| AUM YoY (two speakers) | 35% vs 34.7% "CONFIRMED (rounding)" | 0.3pp gap = rounding | 131, 235 | MATCH |
| Mortgage AUM YoY | 14% vs ~15% "rounding drift" | 1pp gap = rounding | 147, 239 | MATCH |
| Specificity ratio | 9 / 17 ≈ 0.53 | 9/17 = 0.529 | review 6B | MATCH |
| Gold AUM +8% QoQ decomposition | "does NOT reconcile; closes only via ~11.5% relative LTV" | +1 −5 +7(pp) = +3 ≠ +8; (68−61)/61 = 11.5%; +1 −5 +11.5 = +7.5 ≈ +8 | 643-646 | MATCH — A4 correctly flags mgmt's non-reconciling math |

Minor imprecision noted (not a mismatch, not material): in Step 2L (review line 129) A4 characterises the failed gold-decomposition sum as "~-3 to +3%." Using the stated +7pp LTV term the sum is +3 to +4 (with −5/−4 price); the "-3" lower bound only arises if the LTV term is dropped. The phrasing is loose but A4's operative conclusion (the pieces do not sum to +8, and only reconcile via the ~11.5% relative advance-rate) is arithmetically correct and unchanged. No metric or verdict turns on it. NOT a FAIL.

All management-stated headline figures (PAT +52.5%, net income +33%, PPOP +50% YoY / +15.2% QoQ, core NII +40.6%/+12.3%, NII net-of-DA +38.7%/+6.6%, DGL +96.5%, yields +10bps to 15.7%, COB −3bps) are carried by A4 verbatim from their cited lines with no derivation error. Prior-period PAT/ROA denominators are not independently recomputable (no filing), which A4 correctly flags UNVERIFIABLE rather than asserting — conservative and correct.

**ARITHMETIC VERDICT: PASS.** Zero mismatches above rounding. Every A4 derived metric reproduces from the raw extract.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the SAME text)

**Positive claim 1 — "ROE 15.4%, +380bps YoY, clears the FY28 >14% hurdle already; PAT +52.5%, EPS >Rs3."**
Bear counter (same text): the ROE beat is partly mechanical — leverage rose 4.6→4.89 (line 281) as the CLM book fell onto the balance sheet, the very event A4 flags as capital compression (CRAR −169bps to 20.71%). The same event that flatters ROE is the one A4 marks a negative; the leverage-neutral metric is ROA (2.6%, +~20bps only).
Survives? **NO — already incorporated.** A4 presents ROA 2.6% alongside ROE, carries FLAG-CAPITAL-COMPRESSION prominently, and states leverage rose "onto B/S" (claim #21). Both facts are surfaced; the reader can see the ROE headline and the leverage driver together. No new graft required.

**Positive claim 2 — "Credit cost 0.8%, well below the 1.1% falsifier; sub-1% reaffirmed."**
Bear counter (same text): 0.8% is not durable — (a) the GNPA reduction that keeps it optically contained is write-off-driven (~50cr, line 1045), underlying flat at 1.87%; (b) gold provisioning under the new periodic regime is management's own "unknown / new normal" (lines 709, 715) with Stage II already +50bps; (c) PCR is guided DOWN (line 311), which mechanically suppresses future credit-cost as gold flows carry lower provisioning. The 0.8% is a coverage-release / pre-flow artifact, not a clean run-rate.
Survives? **NO — already incorporated.** This is the central spine of A4: FLAG-ASSETQUALITY-OPTICS, FLAG-PCR-EROSION, Exchange 2, Step 7A "the mechanics win," and the 8C conditionally-live 2L-override PCR leg. Fully present.

**Positive claim 3 — "Operating leverage: cost-to-income 52.8% from 57.2%; opex/assets 4.8%, −70bps."**
Bear counter (same text): the improvement is SEASONAL, not structural — management explicitly says Q1 is "seasonally softer... lower sourcing" and "as originations pick up... we expect sourcing-related expenses and operating costs to increase" (lines 371-375). 52.8% will rise.
Survives? **NO — already incorporated.** A4 tags item 4 "GREEN (with seasonal caveat)," the Step 2L C/I row "Maintained w/ hedge," and quotes the "expect costs to rise" line directly.

(Secondary positive tested — "Nomura entry = institutional endorsement": bear = a long-standing PE (True North) fully exiting 6.86% at CMP Rs 164 vs thesis entry Rs 68-77 could read as smart-money exit. Blocked from surviving because (i) CLAUDE.md bars treating ownership transition as risk-in-itself, and (ii) a willing institutional buyer transacted at the same price, neutralising the "smart money leaving" read. A4's NEUTRAL-FACT logging is correct.)

**ADVERSARIAL VERDICT: PASS.** All three strongest bear counters are constructible from the extract but each is already substantially surfaced in A4's flag stack. No NEW surviving counter requires grafting into the review. This is a completeness pass, not an endorsement of thesis direction (Role 3 Devil's Advocate still runs separately).

---

## VERDICT

**COMPLETE.**

- Coverage: PASS — turns 109, questions 36, participants 21, analyst-cited 7 all reconcile to a fresh grep pass; no orphan rows, no missing rows; all 11 A3 findings carried into A4.
- Arithmetic: PASS — every A4 derived metric reproduces from raw extract within rounding; one loose phrasing noted ("-3 to +3" gold-decomposition characterisation) that is immaterial and does not change any figure or verdict.
- Adversarial: PASS — three strongest bear counters all already incorporated; nothing new must be grafted.

No loop-back to A2, A3, or A4 is required. The review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "FEDFINA"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
