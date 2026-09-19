# Stage 12, Verifier B: Concall Red Flags. eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19. Model: claude-opus-5. Fresh context. I did not read any
other verifier output.

Inputs read in full, oldest first:
- Q3 FY26 call, 03-Feb-2026: `inputs/concalls/Concall_Feb_2026_Q3FY26_Transcript.txt`
- 3i Infotech special investor call, 06-Feb-2026: `inputs/announcements/20260209-3i-Infotech-Investor-Call-Transcript.txt`
- Q4 FY26 call, 07-May-2026: `inputs/concalls/Concall_May_2026_Transcript.txt`
- Q1 FY27 call, 30-Jul-2026: `inputs/concalls/Concall_Aug_2026_Transcript.txt`
- Peers: PROTEAN Aug-2026 and May-2026, NEWGEN Jul-2026, QUICKHEAL May-2026
  read in full. NEWGEN May-2026 read in part (pages 3-4, 9-12). The other
  seven peer files were searched by keyword (eSign, DSC, token, H-1B, DPDP,
  hardware, pricing, competition, delay, decision-making).
- Used to check two pipeline claims only: Reg 30 letters
  `inputs/announcements/20260204-d507034d.txt` and `20260818-7509d90d.txt`.
- Pipeline analyses: `outputs/reports/05-concall.md`, `outputs/reports/06-peers.md`.

Scope note. Both B05 and B06 already carry a "Correction (Verifier B)"
section from an earlier pass. I audit the reports as they stand now. I made
my independent list from the transcripts before I read either report.

Anchor format: (call, speaker, file page marker). "[page N]" is the page
marker in the .txt file, not the printed page number.

---

## 1. Independent red-flag list (from raw transcripts only)

### 1A. Material items (CRITICAL + MAJOR)

No CRITICAL item. I found no question that went unanswered in two or more
quarters. Candidates I tested and rejected as repeats: international
profitability (Q3 was a misunderstood question that got an answer, Q1 was a
refusal), deal size (Q3 answered, Q4 refused once), order book (Q3 vague, Q4
disclosed Rs 238 Cr).

| # | Severity | Item | Anchor |
|---|---|---|---|
| M1 | MAJOR | The Executive Chairman has a personal investment link to Capital MXT. Capital MXT bought 5% of 3i Infotech, the party that brought the fraud complaint. He disclosed this only when an analyst asked. | Q1 FY27, V. Srinivasan, [page 23]-[page 24]: "Not related to eMudhra. That is related to my personal investment." |
| M2 | MAJOR | Management told a different Cryptas profit story on each call, and never reconciled them. Q3: Cryptas "improving overall margin quality", PAT "positive at INR 1 crore or INR 1.25 crores", then "INR 1.4 crores or INR 1.5 crores" later in the same call. Q4: FY26 "almost a break-even... totally 1 or 2 crores profit", and FY27 "over a million dollar of profit" expected. Q1: "roughly around INR 100 crore business, which was not profitable at all". The B.V. entity that holds Cryptas lost about Rs 4 Cr. | Q3 FY26, VS, [page 3], [page 6], [page 8]; Q4 FY26, VS, [page 12]; Q1 FY27, VS, [page 11], [page 12] |
| M3 | MAJOR | The 3i Infotech allegations were not disclosed on any earnings call before they became public. 3i first raised them by letter in January 2024 and raised them again in September 2024. The company replied in January 2025. The Q3 FY26 call on 03-Feb-2026 was silent on the matter. 3i filed its EOW complaint that same day, 03-Feb-2026. The company spoke only after 3i's own Reg 30 disclosure on 04-Feb, and then held a special call on 06-Feb. That call drew no analyst questions. | 3i special call, VS, [page 6] (letters Jan-2024, Sep-2024, Jan-2025); Reg 30 letter 04-Feb-2026, [page 1] ("first raised via a letter... in January 2024"; complaint "filed... on 03 February 2026"); Q3 FY26 call, full transcript, no mention; special call [page 7] "we have no questions" |
| M4 | MAJOR | The FY27 PAT guidance softened, but management called it "unchanged". Q4: "between 25% to 30%. Could be around 27%-28%". Q1: "work towards achieving a PAT growth of 25%... guidance remains unchanged". | Q4 FY26, VS, [page 8]; Q1 FY27, VS opening, [page 5], and [page 12] |
| M5 | MAJOR | Management itself says part of the Q1 FY27 EBITDA margin gain (26.2%) came from a temporary fall in low-margin token sales. Its own sustainable guide is about 25%. On this reading, the Q1 margin is partly a denominator effect from a revenue dip that management expects to reverse. It is not clean evidence of the product-mix shift. | Q1 FY27, VS, [page 20]: "the margin slightly improved because the token sales are less, which has a less margin... we may be able to maintain this EBITDA at 25%"; token GM "10% or something", [page 10] |
| M6 | MAJOR | Trust Services reversed. Partners stocked tokens in FY26 and destocked in Q1 FY27 ahead of the September FIPS 140-3 cut-off. Management expects the top line to stay weak in Q2 as well. One token supplier (ProxKey) is not recertifying. The main token (ePass) is waiting on the CCA. The FY26 beat (32% against a 22-25% guide) therefore includes pulled-forward demand. | Q1 FY27, VS opening, [page 4]; VS, [page 9] ("ProxKey, I don't think they are getting re-certified"); VS, [page 10] ("this time everybody was stocking... almost INR 5-7 crore volume got less... top-line may continue to be less during the next quarter"); Q4 FY26, VS, [page 11] (token portal sales drove growth) |
| M7 | MAJOR | Management frames ROE at about 14.5-15% as the level it "can maintain". It defends ROCE without giving a number, by pointing to peer margins and its no-leverage policy. The analyst asked twice in the same call. | Q1 FY27, VS, [page 25] |

### 1B. Minor items

| # | Item | Anchor |
|---|---|---|
| m1 | 3i escalation. Q4: "we have not got the complaint from the police or any inquiry from the police". Q1: "There is no update", then "They called me for a statement on Monday". | Q4 FY26, VS, [page 7]; Q1 FY27, VS, [page 23] |
| m2 | Q3 said "we expect to continue with this level of margin" (23.1% reported). The Q4 reported EBITDA margin was 22.4%. Q4 gave no one-off explanation. | Q3 FY26, VS, [page 8]; Q4 FY26, CFO, [page 5] |
| m3 | Acquisition stance. Q3: "Currently, we are not evaluating any acquisition... another six months to nine months, it may not be required". Q4: "open to selective bolt-on acquisitions" but "nothing in the pipeline". Q1: "nothing immediately". | Q3 FY26, VS, [page 11]; Q4 FY26, VS, [page 5], [page 7]; Q1 FY27, Kaushik S., [page 19] |
| m4 | Management declined to give an outlook for the international segment margin. | Q1 FY27, VS, [page 12] |
| m5 | Management declined to put a size on the InCommon deal. | Q4 FY26, VS, [page 6] |
| m6 | eSign daily volume: "more than 4 lakh per day" in Q3, then "well over 3 lakh daily" in Q4. No reason given. | Q3 FY26, VS, [page 10]; Q4 FY26, VS, [page 4] |
| m7 | Q3 said the stock-in-trade drag (about Rs 3 Cr a quarter) would take "another one or two quarters". Neither later call revisits it. | Q3 FY26, VS, [page 12]-[page 13] |
| m8 | Enterprise growth guidance drifted. Q4: "25% to 30%" for FY27. Q1: Arvind says "about 25%, which we are maintaining", and the 3-year vision says "maybe 20-25% per year". | Q4 FY26, VS, [page 9]; Q1 FY27, Arvind S., [page 14]; VS, [page 21] |
| m9 | Trust Services guidance drifted. Q4: "This year we estimate 20%". Q1 3-year vision: "Trust Service may grow 15-20%". | Q4 FY26, VS, [page 9]; Q1 FY27, VS, [page 21] |
| m10 | The AI Cyber Forge acquisition has no separate revenue line ("no separate tracking"), so the acquisition's return cannot be audited. | Q3 FY26, VS, [page 6] |
| m11 | The Rs 4 Cr B.V. loss was put down to "some legal expenses", which management did not specify. The Chairman first asked for the number ("A loss of how many crores?"). | Q1 FY27, VS, [page 12] |
| m12 | Asked for the order-book level at nine months, management gave a vague answer: "working in proportion to our growth numbers". Q4 later disclosed the number. | Q3 FY26, VS, [page 13] |
| m13 | Q4 said the Middle East war delayed orders. In the same answer, management raised the order-book-to-revenue multiple to 2.2-2.3x (from the usual 2x). | Q4 FY26, VS, [page 6] |
| m14 | Self-graded track record: "last 4-5 years, whatever guidance we have given, we have achieved 100%". | Q4 FY26, VS, [page 9] |
| m15 | Cryptas quarterly revenue went from about Rs 24 Cr (Q2) to 34 (Q3) to about 27 (Q4, implied by the Rs 85 Cr full year) to 20 (Q1 FY27). Management gives seasonality as the reason. | Q3 FY26, VS, [page 6]; Q4 FY26, VS, [page 12]; Q1 FY27, VS, [page 4], [page 10] |
| m16 | Token supply is concentrated. ePass is waiting on the CCA, ProxKey is not recertifying, and a third token ("innate") has low capacity. | Q1 FY27, VS, [page 9] |
| p1 | Peer read-across, collections. NEWGEN reports slower Middle East/EMEA collections, a rising DSO, and India licence revenue down 20-30%. eMudhra (11% MEA, government-heavy) never discusses receivables or collections on any call, and no analyst asks. | NEWGEN May-2026, [page 4], [page 11]; NEWGEN Jul-2026, [page 10] |
| p2 | Peer read-across, hardware inputs. QUICKHEAL reports "IT hardware... price inflation of up to 400% during 2026". PROTEAN reports geopolitical procurement cost inflation. eMudhra resells hardware tokens and built data centres, but is silent on input costs. | QUICKHEAL May-2026, [page 4]; PROTEAN Aug-2026, [page 5] |
| p3 | Peer competition. PROTEAN's eSign Pro, which covers the workflow through stamping to signing, targets BFSI directly and calls itself "a unique moat". It overlaps emSigner/eSign. | PROTEAN Aug-2026, Ajay Rajan, [page 6] |
| p4 | Peer timing. QUICKHEAL already has "several large BFSI customers" on its DPDP product. eMudhra's PrivaTrust is at "pilots, proof of concepts". | QUICKHEAL May-2026, [page 3]; eMudhra Q1 FY27, Kaushik S., [page 6] |
| p5 | eMudhra says "nobody is achieving more than 25% EBITDA margin". NEWGEN says "we usually have 23% to 25% EBITDA margin for the entire year". This partly contradicts the claim. | eMudhra Q1 FY27, VS, [page 25]; NEWGEN Jul-2026, Tarun Nandwani, [page 5] |

List total: 28 items. 7 material (0 CRITICAL, 7 MAJOR) and 21 MINOR.

---

## 2. Comparison against the pipeline (B05, B06)

| # | Sev | Item | Pipeline status | Where / note |
|---|---|---|---|---|
| M1 | MAJOR | Capital MXT personal stake | CAUGHT | B05 4D row 1, 2D, 3C |
| M2 | MAJOR | Cryptas profit narrative drift | CAUGHT | B05 4D row 2, 2B, 4C |
| M3 | MAJOR | 3i allegations known since Jan-2024, absent from Q3 call held the day the complaint was filed | **MISSED** | B05 2B credits the 06-Feb call as "raised proactively... within two business days of the allegation". The transcripts support the opposite reading. The allegation was 2 years old, and the special call answered 3i's public disclosure. It did not come first. B05 never mentions the Jan-2024 to Jan-2025 correspondence or the silence on the Q3 call. |
| M4 | MAJOR | PAT guidance softened while called "unchanged" | CAUGHT | B05 1B, 4D (Medium) |
| M5 | MAJOR | Q1 margin partly a token-mix artefact | **MISSED** | B05 1C and 4A trigger 1 treat 26.2% as mix-shift evidence ("highest of the three quarters"; confirm = ">25% for 2+ quarters"). B05 never cites management's own statement that low token sales lifted the Q1 margin, or its ~25% sustainable guide. |
| M6 | MAJOR | Trust Services reversal and pull-forward | CAUGHT | B05 1C, 2A row 2 caveat, 2B |
| M7 | MAJOR | ROE "can maintain" ~15%, ROCE deflected | CAUGHT | B05 2B, 3C, 4D (Medium) |
| m1 | MINOR | 3i "no update" vs police statement | CAUGHT | B05 correction MAJOR 3, 4D |
| m2 | MINOR | Q4 margin dip vs Q3 "continue" | CAUGHT | B05 2A row 3 |
| m3 | MINOR | Acquisition stance | PARTIALLY CAUGHT (misread) | B05 1C says "Q3 FY26: live consideration, '6-9 months.'" The transcript says "not evaluating any acquisition... may not be required". B05 reverses the meaning, so its "narrowing" trajectory is wrong. The stance went from closed (Q3) to open but empty (Q4) to "nothing immediately" (Q1). |
| m4 | MINOR | International margin outlook declined | CAUGHT | B05 3C, 4D |
| m5 | MINOR | InCommon size declined | CAUGHT | B05 3C |
| m6 | MINOR | eSign 4 lakh to 3 lakh | CAUGHT | B05 1C, 4D |
| m7 | MINOR | Stock-in-trade not revisited | CAUGHT | B05 2A row 6 |
| m8 | MINOR | Enterprise growth guide drift | MISSED | B05 1B records 25-30% only |
| m9 | MINOR | Trust guide drift 20% to 15-20% | PARTIALLY CAUGHT | B05 marks the trigger "Weakening" but does not record the lower guide |
| m10 | MINOR | AI Cyber Forge untracked | MISSED | B05 3C says "Cryptas / AI Cyber Forge quarterly numbers... Full numbers given". That is wrong for AI Cyber Forge, which management says is not tracked separately. |
| m11 | MINOR | B.V. loss "legal expenses" unexplained | PARTIALLY CAUGHT | B05 cites the Rs 4 Cr loss, not the unexplained legal cost |
| m12 | MINOR | Q3 order-book vagueness | MISSED | Not repeated, low weight |
| m13 | MINOR | ME delays vs raised multiple | CAUGHT | B05 2B |
| m14 | MINOR | "100%" guidance self-claim | CAUGHT | B05 3C |
| m15 | MINOR | Cryptas revenue trend down | PARTIALLY CAUGHT | Numbers present, trend not flagged |
| m16 | MINOR | Token supplier concentration | PARTIALLY CAUGHT | B05 1B has "mostly by September", not the supplier detail |
| p1 | MINOR | Peer collections/DSO read-across | PARTIALLY CAUGHT | B06 coverage map notes NEWGEN DSO. B05 2D notes WC silence. Neither connects the two. |
| p2 | MINOR | Peer hardware inflation vs token/DC inputs | PARTIALLY CAUGHT | B06 2B withdrew the link on a false premise (see Section 3, item 2) |
| p3 | MINOR | PROTEAN eSign Pro | CAUGHT | B06 Q7, 2D |
| p4 | MINOR | QUICKHEAL DPDP lead | CAUGHT | B06 2D |
| p5 | MINOR | NEWGEN margin vs "nobody above 25%" | CAUGHT | B06 Q5 (Nov-2025 data; the Jul-2026 annual-range quote also supports it) |

Tally: CAUGHT 16, PARTIALLY CAUGHT 7, MISSED 5.
Material: 7 found, 5 caught (M1, M2, M4, M6, M7), 2 missed (M3, M5).

---

## 3. Pipeline flags I did not find independently

| Pipeline claim | Assessment | Evidence |
|---|---|---|
| B05 2A row 5 and 4D: "UAE QTSP licence slippage", promise marked MISSED | OVERSTATED | The Q3 promise concerned the UAE data centre: a 2-3 month audit, "Then we can commission" (Q3, VS, [page 9]-[page 10]). Q4 says the data centres are "operating in the United States, Europe and the UAE and India" (Q4, VS, [page 4]). The QTSP licence date first appears in Q1 (Arvind S., [page 8]) and is not yet due. B05 ties the Q3 DC promise to the Q1 licence by inference. The earlier call contains no licence promise. |
| B06 2B correction and flag: "eMudhra's own Jul-2026 call attributes the stock-in-trade item to DSC-token partner stocking and a FIPS-140-3 recertification transition" | NOT SUPPORTED | The Q1 FY27 transcript never mentions stock-in-trade or the Q3 "stock issue". It discusses token sales volume and token gross margin ([page 10]). B05 2A row 6 states the item was "never revisited in Q4 FY26 or Q1 FY27 calls". B05 and B06 now contradict each other on the same item. The link may be true, since tokens are resold stock. But it is an inference stated as the call's own attribution. It was also used to withdraw the hardware-inflation hypothesis, even though tokens are hardware. |
| B05 2A row 7: "management attributes the shortfall to the temporary Trust Services decline" | OVERSTATED (weak) | Q1 management names the Trust decline in its opening, [page 4]. On guidance it says only "little bit here and there it will adjust" ([page 12]). It does not explicitly tie the organic gap to the Trust decline. |
| B05 4D: "EOW closed the complaint as civil, not criminal" | SUPPORTED | Reg 30 letter 18-Aug-2026, lines 30-34 |
| B05 2D: "Rs 128 Cr+ alleged" | SUPPORTED | Reg 30 letter 04-Feb-2026, [page 1] |
| B05 4D: no customer-concentration disclosure | SUPPORTED (absence) | None of the three calls discloses it |
| B06 2E: eMudhra never raises AI-driven deferral for its enterprise pipeline | SUPPORTED as scoped | eMudhra blames "AI" only for US services stagnation (Q3, [page 6], [page 8]) |
| B06 Q8 (corrected): H-1B claim is services-scoped | SUPPORTED | Q3 FY26, VS, [page 6] |

---

## 4. Promise-delivery spot checks

| B05 row | Promise in earlier call? | Outcome in later call? | Result |
|---|---|---|---|
| 1. FY26 Rs 700 Cr | Yes, Q3 [page 6]: "we will achieve that Rs.700 crores" | Yes, Q4 [page 3]: total income INR 7,132 Mn | CONFIRMED |
| 2. FY26 Trust 22-25% | Yes, Q3 [page 10]: "INR 120 crores or INR 122 crores... 22% to 25%" | Yes, Q4 [page 3]: "up 32%"; CFO [page 5] Rs 1,400 Mn | CONFIRMED |
| 5. UAE DC commissioning, marked MISSED | Promise was DC audit and commissioning, not the QTSP licence | Q4 [page 4] reports the UAE DC "operating" | WRONG (direction not supported as stated; see Section 3) |
| 6. Stock-in-trade to normalise | Yes, Q3 [page 12]-[page 13] | Neither later call revisits it | CONFIRMED |
| 7. FY27 organic 18%, Q1 ~15% | Yes, Q4 [page 8] | Yes, Q1 [page 4]: 28% total, ~13% Cryptas | CONFIRMED |
| 8. FY27 PAT 25-30% | Yes, Q4 [page 8] | Yes, Q1 [page 5]: PAT +27.9% | CONFIRMED |

Checked 6, confirmed 5, wrong 1.

---

## 5. Credibility grade

B05 grades management C (Mixed), revised down from B. I concur. Two items
this audit adds point the same way. First, the 3i allegations were known for
two years and stayed off the earnings calls, including the Q3 call on the
day the complaint was filed. Second, management's own admission that token
mix inflated the Q1 margin sits beside a "guidance unchanged" line that in
fact trimmed the PAT band. The positives hold: the Rs 700 Cr and Trust
guides were met and beaten, Q1 PAT landed inside the band, and segment
disclosure is granular. These keep the grade above D.

---

## 6. Consolidated findings

| Severity | Location | Finding |
|---|---|---|
| MAJOR | B05 2B, 2D, 4C "Governance/legal handling" | MISSED: the 3i allegations date from Jan-2024 (letters Jan-2024 and Sep-2024, company reply Jan-2025), yet no earnings call mentions them. The Q3 FY26 call on 03-Feb-2026, the day the EOW complaint was filed, is silent. B05 calls the response "proactive". It was reactive to 3i's 04-Feb disclosure. Anchors: 3i special call [page 6]; Reg 30 04-Feb-2026 [page 1]. |
| MAJOR | B05 1C, 4A trigger 1 | MISSED: management says low-margin token sales falling helped lift the Q1 FY27 margin to 26.2%, and guides to ~25% sustainable (Q1, VS, [page 20]; token GM ~10%, [page 10]). B05 treats 26.2% as clean mix-shift evidence. This matters for the 26.2 margin bridge: part of the Q1 print reverses when token volume returns after September. |
| MINOR | B05 1C, "Bolt-on AI-cybersecurity acquisition" | Misread: Q3 said "not evaluating any acquisition... may not be required" (Q3, VS, [page 11]). B05 records this as "live consideration", which reverses the trajectory. |
| MINOR | B05 2A row 5, 4D "UAE QTSP licence slippage" | OVERSTATED: the Q3 promise was DC commissioning, and Q4 reports the DC operating (Q4 [page 4]). The licence date first appears in Q1. |
| MINOR | B06 2B correction, flags, industry_cross_read.pricing_inputs | NOT SUPPORTED attribution: the Q1 FY27 call never mentions the stock-in-trade item. B06 contradicts B05 2A row 6. Using this premise to withdraw the hardware-inflation read-across is unsound, because tokens are hardware. |
| MINOR | B05 1B | MISSED guidance drift: Enterprise 25-30% (Q4 [page 9]) became "about 25%" and "20-25% per year" (Q1 [page 14], [page 21]). Trust 20% (Q4 [page 9]) became "15-20%" (Q1 [page 21]). |
| MINOR | B05 3C, Cryptas / AI Cyber Forge row | OVERSTATED "Full numbers given": AI Cyber Forge revenue is "not separately" tracked (Q3 [page 6]), so that acquisition cannot be audited. |
| MINOR | B05 2A row 7 | Weak: the claim that management attributed the organic shortfall to the Trust decline is not stated explicitly (Q1 [page 12]). |
| MINOR | B05 2D, B06 2A | Peer read-across not connected: NEWGEN reports ME/EMEA collection slowdown and DSO pressure (May-2026 [page 4], [page 11]). eMudhra is silent on receivables and has MEA and government exposure. Carry to stage 3 working-capital checks. |

---

## 7. Coverage basis

28 items on my independent list. 7 are material (0 CRITICAL, 7 MAJOR), and
the pipeline caught 5 of them. The material count is 4 or more, so
acceptance_rate is computed: 5 / 7 = 71.4%, reported as 71.

```yaml
stage: B12b
company: "EMUDHRA"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 28
caught: 16
partially_caught: 7
missed:
  - {severity: "MAJOR", item: "3i Infotech allegations known since Jan-2024 (letters Jan-2024, Sep-2024; reply Jan-2025) never raised on any earnings call; Q3 FY26 call on 03-Feb-2026, the day the EOW complaint was filed, silent; B05 frames the 06-Feb special call as proactive when it was reactive to 3i's 04-Feb disclosure", anchor: "3i special call 06-Feb-2026 [page 6]; Reg 30 letter 04-Feb-2026 [page 1]; Q3 FY26 transcript (no mention)"}
  - {severity: "MAJOR", item: "Q1 FY27 EBITDA margin 26.2% partly a mix artefact of temporarily lower low-margin token sales, per management; sustainable guide ~25%; B05 treats 26.2% as clean mix-shift evidence", anchor: "Q1 FY27, V. Srinivasan, [page 20]; token GM ~10%, [page 10]"}
  - {severity: "MINOR", item: "Enterprise growth guide drift 25-30% (Q4) to 'about 25%' / '20-25% per year' (Q1)", anchor: "Q4 FY26 VS [page 9]; Q1 FY27 Arvind S. [page 14], VS [page 21]"}
  - {severity: "MINOR", item: "AI Cyber Forge revenue not separately tracked; acquisition return unauditable; B05 says 'full numbers given'", anchor: "Q3 FY26 VS [page 6]"}
  - {severity: "MINOR", item: "Q3 order-book question answered vaguely ('working in proportion to our growth numbers'); disclosed in Q4", anchor: "Q3 FY26 VS [page 13]"}
pipeline_flags_not_supported:
  - "B06 2B correction/flags: 'eMudhra's own Jul-2026 call attributes the stock-in-trade item to DSC-token partner stocking and a FIPS-140-3 transition' - the Q1 FY27 transcript never mentions stock-in-trade; contradicts B05 2A row 6 ('never revisited')"
promise_delivery_spot_checks: {checked: 6, confirmed: 5, wrong: 1}
credibility_grade_concur: "concur - C (Mixed) holds; the 2-year undisclosed 3i dispute and the token-flattered Q1 margin beside a trimmed-but-'unchanged' PAT guide weigh down, the met FY26 Rs 700 Cr and Trust guides keep it above D"
findings:
  - {severity: "MAJOR", location: "B05 2B, 2D, 4C governance row", finding: "MISSED 3i non-disclosure: allegations known since Jan-2024, silent on Q3 FY26 call held 03-Feb-2026 (complaint filing date); 'proactive' framing wrong", anchor: "3i special call [page 6]; Reg 30 04-Feb-2026 [page 1]"}
  - {severity: "MAJOR", location: "B05 1C, 4A trigger 1", finding: "MISSED: Q1 FY27 26.2% EBITDA margin partly lifted by lower low-margin token sales per management; guide ~25%; affects margin-bridge evidence", anchor: "Q1 FY27 VS [page 20], [page 10]"}
  - {severity: "MINOR", location: "B05 1C bolt-on acquisition", finding: "Q3 stance misread as 'live consideration'; transcript says 'not evaluating any acquisition... may not be required'", anchor: "Q3 FY26 VS [page 11]"}
  - {severity: "MINOR", location: "B05 2A row 5, 4D", finding: "UAE promise OVERSTATED as missed: Q3 promise was DC commissioning, Q4 reports DC operating; QTSP licence first timed in Q1", anchor: "Q3 [page 9]-[page 10]; Q4 [page 4]; Q1 [page 8]"}
  - {severity: "MINOR", location: "B06 2B, flags, pricing_inputs", finding: "NOT SUPPORTED attribution of stock-in-trade item to Jul-2026 call; B05/B06 contradict; hardware-inflation read-across withdrawn on an unsound premise", anchor: "Q1 FY27 [page 10]; Q3 FY26 [page 12]-[page 13]"}
  - {severity: "MINOR", location: "B05 1B", finding: "Guidance drift not recorded: Enterprise 25-30% to 20-25%; Trust 20% to 15-20%", anchor: "Q4 [page 9]; Q1 [page 14], [page 21]"}
  - {severity: "MINOR", location: "B05 3C", finding: "'Full numbers given' overstated; AI Cyber Forge revenue untracked", anchor: "Q3 FY26 [page 6]"}
  - {severity: "MINOR", location: "B05 2A row 7", finding: "Attribution of organic shortfall to Trust decline not stated explicitly by management", anchor: "Q1 FY27 [page 12]"}
  - {severity: "MINOR", location: "B05 2D, B06 2A", finding: "NEWGEN ME/EMEA collections slowdown and DSO pressure not connected to eMudhra's receivables silence", anchor: "NEWGEN May-2026 [page 4], [page 11]"}
critical_count: 0
major_count: 2
minor_count: 7
material_found: 7
material_caught: 5
acceptance_rate: 71
coverage_basis: "7 material (0 CRITICAL, 7 MAJOR) of 28 listed; 5 material caught (M1 Capital MXT, M2 Cryptas drift, M4 PAT guide, M6 Trust reversal, M7 ROE); 2 material missed (3i non-disclosure, token-flattered Q1 margin)"
```
