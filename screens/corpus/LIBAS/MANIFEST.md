# LIBAS corpus manifest

Company: Libas Consumer Products Ltd
Operator's note: the intended target of the screen.
Screened: 2026-09-21
Documents held: NONE.

## Why the corpus is empty

Two independent routes were tried and both failed.

1. **Bull AI index.** `search_companies` was run twice, on "Libas Consumer
   Products" and on "Libas". Neither returned this company. The best matches
   were unrelated names scoring on the words "consumer products" and "life".
   The company does not appear to be in the Bull AI index.
2. **Direct collection.** This session had no egress. The network policy denied
   the CONNECT to docs.bull-ai.in, www.bseindia.com, www.screener.in and every
   credit rating agency site, each returning a 403 from the gateway. The
   collector could not run and no PDF could be downloaded.

The identity was therefore never resolved: no BSE scrip code, no ISIN and no
confirmation that Bull AI's absence is a coverage gap rather than a naming
mismatch.

## What the operator can do next

1. Supply the BSE scrip code or the ISIN. A code-based lookup may succeed where
   the name search failed.
2. Collect the filings directly from BSE when a session with egress is
   available, using `tools/collector/`.
3. Re-run the shallow screen once any financial statement is on disk.

No card was written for LIBAS. Writing one from nothing would breach the
framework rule that every number traces to a corpus file and a page.
