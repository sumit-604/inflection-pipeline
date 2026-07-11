# Notion save payload — Karnika Industries Ltd (KARNIKA)

Phase 2 stop. This is a pre valuation save. The run stopped after FTTCP deliberation;
stages 10, 11, 14, 15 (assembly, valuation, thesis, devil's advocate) did NOT run, so
there is no destination PE, no fair value, no entry zone, and no BUY / WATCHLIST / AVOID.
Do not add any of those here.

## Save target and operation

- Database: COMPANIES MASTER
- data_source_id: 345bb2b9-d3ab-8032-9b46-000ba16ab827
- Operation: search KARNIKA first. If the page exists, FETCH it live, then APPEND the
  Key Notes entry below and update only the evidence properties listed. If it does not
  exist, create it with the properties below.
- Decision Status: DO NOT SET or overwrite from this pipeline run. Leave whatever the
  human has set, or blank on a new page. Decision Status is a human ruling and this is a
  pre valuation save.
- Character hygiene (per LESSONS 2026-07-09): Notion text properties reject the less than
  sign and the right arrow. All values below are already cleaned (use "above" and "toward"
  in words). If EM Classification select has no MODEST option or Promoter Verdict select
  has no CONCERN option, write the value to the matching text field instead.

## Page properties (set on create, or update on append)

| Property | Value | Field type note |
|---|---|---|
| Company | Karnika Industries Ltd | title |
| Ticker | KARNIKA | text |
| Exchange / ISIN | NSE KARNIKA / INE0MGA01012 | text |
| Sector | Apparel and textiles, children's wear (kidswear) manufacturing plus Kidcity retail | text. Manifest label "Pharma / CDMO" is WRONG; corrected here |
| CMP (run date) | Rs 120.0 as of 2026-07-11 (manifest, not a live quote) | number or text |
| Market cap | Rs 742 Cr (manifest) | number or text |
| Gate 0 score | 82 / 160 | number/text |
| Gate 0 classification | AVERAGE (capped by under 3 year history; raw matrix mapped GOOD or better) | text |
| Emerging Moat score | 18.3 | number/text |
| EM classification | MODEST | select or text; write to text if the select lacks this option |
| Promoter verdict | CONCERN | select or text; write to text if the select lacks this option |
| Management / credibility grade | C | text |
| FTTCP verdict | DEEP WATCH leaning AVOID (composite plus 2 of 8) | text |
| Cash conversion flag | FLAG-CASH, determination INDETERMINATE (capped, missing evidence named) | text |
| Phase 1 confidence delta (overall) | 65 (band 60 to 74) | number/text |
| Run type | full, Phase 2 stop (pre valuation) | text |
| Decision Status | LEAVE AS IS (human ruling; not set by this run) | do not overwrite |
| Drive / run folder | runs/karnika-2026-07-11 (repo); attach the Drive folder link if used | url/text |

## Key Notes append (prepend this dated block)

2026-07-11 — Phase 1 evidence plus FTTCP deliberation, pre valuation. Kidswear job work
manufacturer out of Howrah, moving into Kidcity branded retail. FY26 consolidated revenue
about Rs 248 Cr, PAT about Rs 28 Cr (inflated by a one time securities gain of about
Rs 9 Cr). Gate 0 82 of 160, capped AVERAGE on under 3 year history. EM MODEST, combined
AVERAGE. Promoter verdict CONCERN: the Board's Report RPT clean claim and the "no
remuneration increase" claim are both contradicted by Note 33 inside the same filing, and
assurance roles carry the promoter surname. Credibility grade C: one of eight tracked
promises delivered, guidance escalated after a Kidcity miss, FY26 PAT growth carried by a
one time gain. Cash conversion INDETERMINATE: receivables grew 45 percent against revenue
36 percent, cash drained into an unnamed inter corporate loan and a securities book, and
the confirming evidence (credit rating rationale, receivables ageing) is not in the file.
Peers contradict the margin squeeze and weak demand framing. FTTCP composite plus 2 of 8,
DEEP WATCH leaning AVOID: revenue FIRING, margin and cash and ROCE all STAGNANT. Pending
Phase 3: FY26 ROCE and FY26 debtor days are NOT FOUND and must be anchored; sector cap set
to 25x apparel manufacturing (weak pricing power, not a pricing power brand); valuation,
thesis, and devil's advocate not yet run. No Decision Status change from this run.

## Watch triggers to carry (top 5)

1. Consolidated EBITDA margin above 17 percent for two quarters (up) or below 13 percent (down).
2. Debtor days disclosed inside 90 days (cash up) or above 160 days (cash down).
3. Credit rating obtained and working capital rationale read (resolves the cash flag).
4. Kidcity above 75 counters and Rs 30 Cr plus run rate (up) or stalls below Rs 25 Cr (kills catalyst).
5. Note 19 inter corporate loan counterparty named or repaid (governance and ROCE drag).

## Publish

No publish candidate this analysis.

## Not included (Phase 3 only)

Destination PE, fair value (bear / base / bull), entry zone, MoS price, Hurdle verdict,
BUY / WATCHLIST / AVOID, position sizing. These require stages 10, 11, 14, 15 and are not
part of this save.
