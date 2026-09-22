# Not screened, 2026-09-22: CRESTO and PCS

Two of the fourteen names on the operator's list could not be screened. Neither
is a business verdict. Both are identity and coverage failures, recorded here so
the gap is on the record rather than silently dropped.

This is the same class of outcome the 2026-09-21 run recorded for LIBAS.

---

## Bull AI identifier resolver defect, 2026-09-22

**The resolver silently substitutes a wrong company for an unmatched numeric
identifier.** `list_document_availability` with the nonsense identifier
`999999` returned a full, confident document map for **Balaji Amines Ltd, BSE
530999**, with `"single_company": true` and no warning of any kind.

Adjacent unused codes return a different failure: both `535043` and `535044`
returned "Multiple companies match the supplied identifier", so that message is
noise and is **not** evidence that a company exists.

Valid exact codes resolve correctly: `544091` returned Qualitek Labs.

**Control for this defect by reading the `company` block echoed in every
response and confirming the name before using any figure.** Every call used in
this run was checked that way and every one resolved to the intended company.

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
| "Cresto Techno", 50 results requested | **No Cresto at any rank.** Returned 50 unrelated "Techno"/"Technologies" names. |
| "Cresto Techno Limited Bangalore" | 2 results, neither related: Newjaisa Technologies, Agri-Tech (India). |
| "multimedia BPO data processing engineering real estate" | **Zero results.** |
| `list_document_availability` on "535043" | "Multiple companies match". **Noise: code 535044 returns the same.** |

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
| "PCS Tech" | No match. Returned HCL Tech, Tech Mahindra, Hi-Tech Pipes, VA Tech Wabag. |
| "P C S Technology" | No match. Returned LTTS, HCL Tech, OnEMI, Syrma. |
| `list_document_availability` on "517119" | **"No listed company was found for the supplied identifier."** |

The identity was never resolved. The same egress block applies.

**To screen it, next time:** resolve the ISIN from the BSE scrip master for code
517119 in a session with egress, then re-query Bull AI by ISIN. PCS Technology
is a long-listed company with decades of filings, so if the ISIN resolves, the
corpus should be deep. The failure here looks like a search-index gap on a
BSE-only micro-cap rather than an absence of filings, which is the opposite of
the STEAMHOUSE case.

---

## Third pass, 2026-09-22: operator supplied confirmed ISINs

The operator supplied both ISINs, each confirmed across two independent
sources, plus the fact that **Cresto Techno was formerly Silly Monks
Entertainment** and is **NSE-listed as CRESTO**.

| Identity | Value |
|---|---|
| Cresto Techno Ltd (formerly Silly Monks Entertainment) | NSE CRESTO, BSE 535043, **ISIN INE203Y01012** |
| PCS Technology Ltd | BSE 517119, not NSE-listed, **ISIN INE834B01012** |

**Result: both are absent from the Bull AI index. Confirmed through the lookup
path that demonstrably works.**

| Probe | Cresto | PCS |
|---|---|---|
| `list_document_availability` on ISIN | No listed company found | No listed company found |
| `list_document_availability` on NSE symbol | No listed company found | n/a |
| `search_companies` on ISIN | 0 results | 0 results |
| `search_companies` on former name "Silly Monks Entertainment" | 0 relevant | n/a |

## Second Bull AI defect: `search_companies` ignores ISINs

The tool description says it searches "by company name, NSE symbol, BSE code, or
ISIN". **It does not match ISINs.** Control: `search_companies("INE303A01010")`
returns **zero results**, although DIC India is fully indexed under that exact
ISIN. The same ISIN passed to `list_document_availability` resolves DIC India
correctly.

**Correct procedure, superseding the earlier recommendation:** resolve an
identity with **`list_document_availability(identifier=<ISIN>)`**, not with
`search_companies`. The availability endpoint accepts ISINs and returns the
resolved `company` block. It is also free.

## The pattern claim from the first pass was wrong

The first pass recorded that both failures shared the shape "BSE-only listings
with no NSE symbol". **That is disproved.** Cresto is NSE-listed as CRESTO and
is still absent from the index. BSE-only-ness is not the cause.

The actual finding is simpler and less useful: these two companies are not in
the Bull AI company index at all. Both are micro-caps, one of them recently
renamed, and the index does not carry them. There is no query form that
retrieves them.

**Recommendation for the collector and for future screens:** for any BSE-only
name, resolve the ISIN before the run starts, out of session, and pass the ISIN
rather than the name or the code.

**Second pass, 2026-09-22, after the operator supplied the two codes.** The
codes are BSE scrip codes, not ISINs; an ISIN is twelve characters beginning
`INE`, such as `INE303A01010`. Eight further query forms were tried across the
two names, listed in the tables above, including a fifty-result sweep on "Cresto
Techno" that returned no Cresto at any rank. **Both companies are absent from
the Bull AI company index**, not merely hard to address. `517119` returns a
clean "no listed company found"; `535043` returns an ambiguity message that a
control on `535044` proves is noise.

Supplying the real ISINs is still worth one attempt each, because
`search_companies` accepts an ISIN and matches it exactly. If the ISIN also
fails, these two names need a live-web session and cannot be screened from this
container at all.
