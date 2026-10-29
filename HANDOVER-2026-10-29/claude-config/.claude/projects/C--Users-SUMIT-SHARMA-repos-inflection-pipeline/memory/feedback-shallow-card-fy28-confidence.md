---
name: shallow-card-fy28-confidence
description: "Operator wants every shallow card's step 13 to carry an FY28 PAT and forward PE plus a confidence band (asked 2026-10-29); not yet in the framework text"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7afbdba0-3a51-4f1f-bd72-b2731c181472
  modified: 2026-10-28T23:11:23.635Z
---

On 2026-10-29 the operator asked the shallow screen for FY27 and FY28 expected earnings, the forward PE on each, and "the probability of your analysis", screening for names cheap on forward earnings with high probability.

**Why:** Step 13 of `screens/SHALLOW_ANALYSIS_FRAMEWORK.md` only defines FY+1. The run carried the two additions inside step 13 under "Operator additions, 2026-10-29": FY28 on the same tier rules (usually one notch weaker), and confidence as the probability actual PAT lands within 15% of the estimate (HIGH about 70%+, MEDIUM about 50%, LOW under 40%) with the one observation that moves the band. The framework text was not amended; that needs an operator ruling and a framework PR.

**How to apply:** Put both additions on every shallow card until the framework is amended. Rank the run on FY27 forward PE and read it against confidence; say plainly when no name is both cheap and HIGH. Also: NSE and BSE both refuse scripted announcement calls (29-Oct-2026); the BSE API works from a bseindia.com page in the in-app browser, 12-month windows, paginate per window; never resume a BSE download with curl -C. See [[chartink-breadth-pipeline]] for the other scheduled data route.
