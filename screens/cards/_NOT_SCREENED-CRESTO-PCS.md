# Not screened, 2026-09-22: CRESTO and PCS

Two of the fourteen names on the operator's list could not be screened. Neither
is a business verdict. Both are identity and coverage failures, recorded here so
the gap is on the record rather than silently dropped.

This is the same class of outcome the 2026-09-21 run recorded for LIBAS.

---

## CRESTO — Cresto Techno Ltd (BSE 535043)

**Not in the Bull AI index. No card written.**

Operator description: media and entertainment, IT, engineering, BPO, data
processing, multimedia and real estate; market capitalisation about Rs 22 crore;
loss-making; promoter holding 50.04%.

**Searches run, all returning no match for this company:**

| Query | Result |
|---|---|
| "Cresto Techno" | No Cresto entity. Best matches were Crest Ventures, Golden Crest Education, Cressanda Railway Solutions. |
| "Cresto" | Same set. No Cresto entity at any score. |
| "535043" (the BSE code) | No match. The code-shaped query returned unrelated 5353xx and 5356xx codes. |
| "Cresto Techno Ltd media entertainment" | No match. Returned Shemaroo, Imagicaaworld, Touchwood, Optimystix, Zee. |

The identity was never resolved to a scrip code or ISIN that the service
recognises. With no egress, the BSE and screener.in routes were both closed:
this session's network policy answered 403 to the CONNECT for www.bseindia.com,
www.screener.in and docs.bull-ai.in.

**Writing a card would have breached the rule that every number traces to a file
and a page.** None was written.

**To screen it, next time:** resolve the identity first, from a session with
egress, via the BSE scrip master for code 535043, and capture the ISIN. Then
re-query Bull AI by ISIN, which is the most reliable identifier the service
accepts.

**One note on priority.** On the operator's own description this is a Rs 22
crore, loss-making micro-cap spanning six unrelated activities including real
estate. Under the framework that combination, no profit and no coherent single
engine, would face a difficult step 2 and step 6 even with a full corpus. It is
the lowest-priority retrieval of the two.

---

## PCS — PCS Technology Ltd (BSE 517119 only)

**Not in the Bull AI index. No card written.**

Operator description: IT enabled services; market capitalisation about Rs 38
crore; Patni-family promoted.

**Searches run, all returning no match for this company:**

| Query | Result |
|---|---|
| "PCS Technology" | No PCS entity. Returned HCL Tech, Kaynes, Syrma, LTTS, Cambridge Technology. |
| "PCS Technology Ltd" | Same pattern. Returned Syrma, Clean Science, Le Travenues, Standard Engineering, Ideaforge. |
| "517119" (the BSE code) | No match. Returned unrelated 517xxx codes including Motherson, Havells, KEI. |
| "Patni Computer PCS" | Two results, neither related: Computer Age Management Services and Master Components. |

The identity was never resolved. The same egress block applies.

**To screen it, next time:** resolve the ISIN from the BSE scrip master for code
517119 in a session with egress, then re-query Bull AI by ISIN. PCS Technology
is a long-listed company with decades of filings, so if the ISIN resolves, the
corpus should be deep. The failure here looks like a search-index gap on a
BSE-only micro-cap rather than an absence of filings, which is the opposite of
the STEAMHOUSE case.

---

## The pattern worth recording

Both failures share one shape: **BSE-only listings with no NSE symbol.** Bull
AI's `search_companies` resolves NSE symbols and company names well, and BSE
codes poorly. QLL (BSE 544091) resolved only because the company name matched;
the bare code "544091" was never tried as a search term, but "535043" and
"517119" both failed.

**Recommendation for the collector and for future screens:** for any BSE-only
name, resolve the ISIN before the run starts, out of session, and pass the ISIN
rather than the name or the code. This belongs in `screens/README.md` under
corpus building and is carried into the run record.
