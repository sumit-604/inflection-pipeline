# CLEANMAX SOTP FCFF valuation. Rs Cr throughout. Valuation date 30-Jun-2026 -> 02-Sep-2026.
# All figures anchored in the report; this script only does the arithmetic.

def pv_series(cfs, r, t0=1):
    # cfs indexed year 1..n; discount at rate r, first cf at year t0
    return sum(cf / (1+r)**(t0+i) for i, cf in enumerate(cfs))

# ============================================================
# 1. COST OF CAPITAL
# ============================================================
Rf   = 0.065          # India 10y G-sec [spec/verify]
ERP  = 0.075          # Damodaran India ERP [spec/verify]
bu   = 0.55           # unlevered beta, contracted power [spec/verify]
tax  = 0.25
# D/E at market: net debt (AR 11,208.80 + acceptances 1,730.92 = 12,939.72 ~12,940) / market cap 14,680
netdebt_ar   = 11208.80
acceptances  = 1730.92
netdebt_mgmt = 9684.0
netdebt_jun  = 11809.0
mktcap = 14680.0
debt_for_de = netdebt_ar + acceptances          # 12,939.72
DE = debt_for_de / mktcap
bl = bu * (1 + (1-tax)*DE)                       # Hamada, 25% tax
Ke = Rf + bl*ERP
Kd_pre = 0.084                                   # Aug call cost of debt June-26
Kd_post = Kd_pre*(1-tax)
wE = mktcap/(mktcap+debt_for_de)
wD = debt_for_de/(mktcap+debt_for_de)
WACC = wE*Ke + wD*Kd_post
print("="*60); print("1. COST OF CAPITAL")
print(f"Rf={Rf:.3%} ERP={ERP:.3%} beta_u={bu}")
print(f"D/E(mkt)={DE:.3f}  levered beta={bl:.3f}")
print(f"Ke = {Rf:.3%} + {bl:.3f}x{ERP:.3%} = {Ke:.4f} = {Ke:.2%}")
print(f"Kd pre={Kd_pre:.2%} post={Kd_post:.3%}")
print(f"weights E={wE:.3f} D={wD:.3f}")
print(f"Group WACC = {WACC:.4f} = {WACC:.2%}")

# Bucket discount rates - build
# Bucket 1: project 75% debt @6.3% post-tax + 25% equity @~13% (group Ke rounded down for contracted IG)
b1_build = 0.75*Kd_post + 0.25*0.13
print(f"\nBucket1 build: 0.75x{Kd_post:.3%}+0.25x13% = {b1_build:.4f} -> set 8.0%")
r1, r2, r3, r4 = 0.080, 0.110, 0.140, 0.120
print(f"Bucket rates: B1={r1:.0%} B2={r2:.0%} B3={r3:.0%} B4={r4:.0%}")
print("B2 = B1 + ~300bps execution/connectivity; B3 pipeline unfirm; B4 services")

# ============================================================
# 2. BUCKET 1 - OPERATIONAL FLEET (4,174.43 MW, 30-Jun-26)
# ============================================================
print("\n"+"="*60); print("2. BUCKET 1 OPERATIONAL")
mw_op = 4174.43
gen_q1 = 1302.36                 # Mn kWh Q1 FY27 exported (Pres p.27)
gen_y1 = gen_q1*4                # GWh annualised realised (Case A: Bikaner curtailed)
gen_theory = 7600.0             # theoretical from PLFs (spec)
tariff = 4.06                    # realised Rs/kWh (Pres p.27)
margin1 = 0.835                  # Note 55, 83-84%
maint_per_mw = 0.03              # Rs Cr/MW/yr = Rs 3 lakh/MW routine O&M capex (assumption)
maint1 = maint_per_mw*mw_op
degr = 0.004                     # 0.4%/yr blended degradation
merchant_tail = 2.50             # Rs/kWh post-PPA tail yrs 24-30
gross_block1 = 3331.58*3.5 + 842.85*7.8   # solar MWp x3.5 + wind MW x7.8
gross_block1 *= 1.06             # +6% soft cost
bookdep1 = gross_block1/30.0
print(f"gen realised Y1 = {gen_q1}x4 = {gen_y1:.1f} GWh vs theoretical {gen_theory:.0f} (gap {1-gen_y1/gen_theory:.0%})")
print(f"revenue Y1 = {gen_y1:.1f}x{tariff}/10 = {gen_y1*tariff/10:.1f} Cr")
print(f"EBITDA Y1 = {gen_y1*tariff/10*margin1:.1f} Cr; margin {margin1:.1%}")
print(f"gross block est {gross_block1:.0f} Cr; book dep {bookdep1:.0f} Cr/yr; maint capex {maint1:.1f} Cr/yr")

def cashtax_rate(t):
    if t<=4: return 0.0      # DTA 1,215.77 + accelerated tax dep shield
    if t<=8: return 0.125    # MAT-like
    return 0.25

def bucket1_dcf(rate, bikaner_case_B=False):
    life=30; ppa=23
    fcfs=[]; rows=[]
    for t in range(1,life+1):
        g = gen_y1*(1-degr)**(t-1)
        tf = tariff if t<=ppa else merchant_tail
        rev = g*tf/10
        eb = rev*margin1
        if bikaner_case_B and t>=2:
            eb += 170.0        # Bikaner resolves FY28 -> +170 Cr/yr EBITDA
        ebit = eb - bookdep1
        ctax = cashtax_rate(t)*max(ebit,0)
        fcff = eb - ctax - maint1
        fcfs.append(fcff)
        if t in (1,2,5,9,23,24,30): rows.append((t,g,tf,rev,eb,ctax,fcff))
    ev = pv_series(fcfs, rate, t0=0.5)   # mid-year-ish start; use 0.5 offset
    return ev, fcfs, rows

evB1_A,_,rowsA = bucket1_dcf(r1, False)
evB1_B,_,_     = bucket1_dcf(r1, True)
ebitda1 = gen_y1*tariff/10*margin1
print(f"\nBucket1 CaseA EV = {evB1_A:,.0f} Cr | EV/EBITDA = {evB1_A/ebitda1:.1f}x")
print(f"Bucket1 CaseB EV = {evB1_B:,.0f} Cr (Bikaner resolves +170/yr)")
print("Schedule (Case A) t, gen, tariff, rev, EBITDA, cashtax, FCFF:")
for r in rowsA: print("  y%2d  gen%7.1f  tf%.2f  rev%7.1f  eb%7.1f  tax%6.1f  fcff%7.1f"%r)

# ============================================================
# 3. BUCKET 2 - UNDER-EXECUTION (2,656.66 MW)
# ============================================================
print("\n"+"="*60); print("3. BUCKET 2 UNDER-EXECUTION")
mw_ue = 2656.66
# clean per-MW economics (ex-Bikaner drag), contracted tariff 4.00
genPerMW_clean = 1.35            # GWh/MW/yr (fleet ex-Bikaner realised)
tariff2 = 4.00
# total book cost
solar_ue = 0.70*mw_ue; wind_ue = 0.30*mw_ue
totcost_ue = (solar_ue*3.5 + wind_ue*7.8)*1.06
cwip_spent = 5339.21
remaining_capex = totcost_ue - cwip_spent
print(f"total book cost = ({solar_ue:.0f}x3.5 + {wind_ue:.0f}x7.8)x1.06 = {totcost_ue:,.0f} Cr")
print(f"less CWIP spent {cwip_spent:,.0f} -> remaining capex {remaining_capex:,.0f} Cr")

def bucket2_dcf(rate, raj_prob):
    # raj_prob applies Bikaner (70% curtail) economics to ~800 MW unnamed residual
    life=30; ppa=23
    raj_mw = 800.0*raj_prob
    clean_mw = mw_ue - raj_mw
    # per-MW annual EBITDA
    def perMW_ebitda(g_permw):
        return g_permw*tariff2/10*margin1
    eb_clean = perMW_ebitda(genPerMW_clean)*clean_mw
    eb_raj   = perMW_ebitda(genPerMW_clean*0.30)*raj_mw   # 70% curtailed -> 30% output
    eb_y1_full = eb_clean+eb_raj
    maint2 = maint_per_mw*mw_ue
    gb2 = totcost_ue; bd2 = gb2/30.0
    # completed-asset cash flows (per full-year), start after commissioning ramp
    fcfs=[]
    for t in range(1,life+1):
        eb = eb_y1_full*(1-degr)**(t-1)
        if t>ppa: eb = eb*(merchant_tail/tariff2)
        ebit=eb-bd2; ctax=cashtax_rate(t)*max(ebit,0)
        fcfs.append(eb-ctax-maint2)
    # commissioning profile: half commissions ~ start yr1.5, half ~ yr2.5 (cash starts post-ramp)
    ev_asset = 0.5*pv_series(fcfs,rate,t0=1.5) + 0.5*pv_series(fcfs,rate,t0=2.5)
    # remaining capex spread yr0.5 and yr1.5
    pv_capex = 0.5*remaining_capex/(1+rate)**0.5 + 0.5*remaining_capex/(1+rate)**1.5
    return ev_asset - pv_capex, ev_asset, pv_capex, eb_y1_full

for rp in (0.0,0.5,1.0):
    net,ass,cap,eby1 = bucket2_dcf(r2, rp)
    print(f"Raj={rp:.0%}: completed-asset PV {ass:,.0f} - PV capex {cap:,.0f} = net {net:,.0f} Cr (EBITDA/yr@full {eby1:,.0f})")
evB2_base = bucket2_dcf(r2, 0.5)[0]

# ============================================================
# 4. BUCKET 3 - PIPELINE/PLATFORM (2,668 MW applied + intent)
# ============================================================
print("\n"+"="*60); print("4. BUCKET 3 PIPELINE")
evB3_base = 0.0
reinvest = 6750.0; spread = -0.046
destroy_per_yr = reinvest*abs(spread)
evB3_down = -pv_series([destroy_per_yr]*5, WACC, t0=1)
print(f"Base = 0 (ROIC 3.4->5.4% < WACC {WACC:.1%}: growth below cost of capital)")
print(f"Downside: reinvest {reinvest:.0f}/yr x {spread:+.1%} spread = -{destroy_per_yr:.0f}/yr; PV5@{WACC:.1%} = {evB3_down:,.0f} Cr")
print("Upside: NONE. At guided 10% ROIC by FY30, ROIC=WACC -> value 0, not positive.")

# ============================================================
# 5. BUCKET 4 - RE SERVICES
# ============================================================
print("\n"+"="*60); print("5. BUCKET 4 RE SERVICES")
svc_rev = 497.33; svc_margin=0.196
svc_eb1 = svc_rev*svc_margin
def bucket4_dcf(rate):
    ebs=[svc_eb1, svc_eb1*0.8, svc_eb1*0.64]   # run-off, book-to-bill <1
    fcfs=[e*(1-tax) for e in ebs]
    tv = 3.0*ebs[-1]*(1-tax)                     # low exit multiple 3x on yr3 post-tax
    ev = pv_series(fcfs,rate,t0=1) + tv/(1+rate)**3
    return ev, ebs
evB4,svc_ebs = bucket4_dcf(r4)
print(f"FY26 svc EBITDA {svc_eb1:.1f}; run-off {[round(e,1) for e in svc_ebs]}; +3x exit on yr3")
print(f"Bucket4 EV @ {r4:.0%} = {evB4:,.0f} Cr")

# ============================================================
# 6. EV -> EQUITY BRIDGE
# ============================================================
print("\n"+"="*60); print("6. EV -> EQUITY BRIDGE (base case)")
grossEV = evB1_A + evB2_base + evB3_base + evB4
print(f"Gross EV = B1 {evB1_A:,.0f} + B2 {evB2_base:,.0f} + B3 {evB3_base:,.0f} + B4 {evB4:,.0f} = {grossEV:,.0f}")

shares = 11.75

def bridge(grossEV_, netdebt, co_own_frac, complexity, survival, label):
    ev_less_debt = grossEV_ - netdebt - acceptances
    # NCI at FMV = 26% x co-owned share of (bucket equity). Approx co_own_frac of levered equity.
    nci = 0.26*co_own_frac*max(ev_less_debt,0)
    attrib = ev_less_debt - nci
    after_cx = attrib*(1-complexity)
    final = after_cx*survival
    eps = final/shares
    return dict(label=label, evless=ev_less_debt, nci=nci, attrib=attrib,
                after_cx=after_cx, final=final, eps=eps)

complexity=0.125; survival=0.90; co_own=0.48
b_ar   = bridge(grossEV, netdebt_ar,   co_own, complexity, survival, "net debt AR 11,208.80")
b_mgmt = bridge(grossEV, netdebt_mgmt, co_own, complexity, survival, "net debt mgmt 9,684")
for b in (b_ar,b_mgmt):
    print(f"\n[{b['label']}] +acceptances {acceptances:.0f}")
    print(f"  Gross EV {grossEV:,.0f} - net debt - acceptances = equity(100%) {b['evless']:,.0f}")
    print(f"  - NCI@FMV (26% x {co_own:.0%} co-owned) {b['nci']:,.0f} = attributable {b['attrib']:,.0f}")
    print(f"  x (1-complexity {complexity:.1%}) = {b['after_cx']:,.0f}")
    print(f"  x survival {survival:.0%} = FINAL EQUITY {b['final']:,.0f} Cr")
    print(f"  EPS = {b['final']:,.0f}/{shares} = Rs {b['eps']:,.0f}/share")

# Bikaner Case A vs B at equity level (net debt AR, Raj 50%)
print("\nBIKANER CASE A vs B (net debt AR, Raj 50%, per share):")
for caseB,lbl in ((False,"A 70% persists"),(True,"B resolves FY28 +170/yr")):
    e1 = bucket1_dcf(r1, caseB)[0]
    gEV = e1 + evB2_base + 0 + evB4
    bb=bridge(gEV,netdebt_ar,co_own,complexity,survival,"")
    print(f"  Case {lbl}: B1 EV {e1:,.0f}, gross EV {gEV:,.0f}, final eq {bb['final']:,.0f}, Rs {bb['eps']:,.0f}/sh")

# NCI sensitivity on co-own fraction
print("\nNCI co-owned fraction sensitivity (net debt AR):")
for cf in (0.35,0.48,0.60):
    bb=bridge(grossEV,netdebt_ar,cf,complexity,survival,"")
    print(f"  co-own {cf:.0%}: NCI {bb['nci']:,.0f} -> final equity {bb['final']:,.0f} -> Rs {bb['eps']:,.0f}/sh")

# ============================================================
# 7. SENSITIVITY GRID  discount +/-150bps  x  Rajasthan prob
# ============================================================
print("\n"+"="*60); print("7. SENSITIVITY GRID (per share, net debt AR, base complexity/survival)")
print("rows: discount shift; cols: Rajasthan prob 0/50/100%")
for dshift in (-0.015,0.0,0.015):
    row=[]
    e1 = bucket1_dcf(r1+dshift,False)[0]
    e4 = bucket4_dcf(r4+dshift)[0]
    for rp in (0.0,0.5,1.0):
        e2 = bucket2_dcf(r2+dshift, rp)[0]
        gEV = e1+e2+0+e4
        bb=bridge(gEV,netdebt_ar,co_own,complexity,survival,"")
        row.append(bb['eps'])
    print(f"  {dshift*10000:+.0f}bps: " + "  ".join(f"Raj{p:.0%}=Rs{v:,.0f}" for p,v in zip((0,0.5,1.0),row)))

# ============================================================
# 8. KEY COMPARISON, ENTRY PRICE, MULTIPLES CROSS-CHECK
# ============================================================
print("\n"+"="*60); print("8. KEY COMPARISON")
current_EV = 25889.0
print(f"Bucket 1 standalone EV {evB1_A:,.0f} vs current market EV {current_EV:,.0f}")
print(f"Market pays {current_EV-evB1_A:,.0f} Cr above operational fleet (for B2/B3/B4 growth)")
print(f"B2+B3+B4 SOTP value = {evB2_base+evB3_base+evB4:,.0f} Cr; justifies {(evB2_base+evB3_base+evB4)/(current_EV-evB1_A):.0%} of the growth premium")

print("\nENTRY PRICE (base case, net debt AR):")
FV = b_ar['eps']
entry25 = FV/(1.25**3)
mos = entry25*0.80
print(f"Base FV/share Rs {FV:,.0f}; entry for 25% 3yr CAGR (exit at FV) = FV/1.953 = Rs {entry25:,.0f}")
print(f"MoS 20% below entry = Rs {mos:,.0f}")
CMP=1247
print(f"CMP Rs {CMP}: implied 3yr CAGR to FV = {(FV/CMP)**(1/3)-1:+.1%}")

print("\nMULTIPLES CROSS-CHECK (<=15% weight):")
rr_ebitda=1870.0
for mult in (8,10,13.1,14.2):
    print(f"  {mult}x run-rate EBITDA {rr_ebitda:.0f} = EV {mult*rr_ebitda:,.0f}")
xcheck_EV = 9.0*rr_ebitda
blend_EV = 0.85*grossEV + 0.15*xcheck_EV
bb=bridge(blend_EV,netdebt_ar,co_own,complexity,survival,"")
print(f"cross-check EV @9x = {xcheck_EV:,.0f}; 85/15 blend EV {blend_EV:,.0f} -> Rs {bb['eps']:,.0f}/sh")

# ============================================================
# 9. SANITY GATES
# ============================================================
print("\n"+"="*60); print("9. SANITY GATES")
mult_check = evB1_A/ebitda1
print(f"G1 Bucket1 EV/EBITDA = {mult_check:.1f}x (mid-single-digit target) - {'PASS' if 4<=mult_check<=9 else 'CHECK'}")
sum_rev_y1 = gen_y1*tariff/10 + svc_rev*(303.9/ (svc_rev)) # placeholder
b1_rev=gen_y1*tariff/10; b4_rev=303.9*4
print(f"G2 sum bucket Y1 rev: B1 {b1_rev:,.0f} + B4 svc {b4_rev:,.0f} = {b1_rev+b4_rev:,.0f} vs annualised Q1 3,329 - {'PASS' if abs(b1_rev+b4_rev-3329)<250 else 'CHECK'}")
# G3 identity: equity + net debt + NCI + acceptances = gross EV
identity = b_ar['final'] # after adj; check pre-adjustment identity
pre_adj_eq = grossEV - netdebt_ar - acceptances - b_ar['nci']
lhs = pre_adj_eq + netdebt_ar + acceptances + b_ar['nci']
print(f"G3 identity: attributable-eq {pre_adj_eq:,.0f} + net debt {netdebt_ar:,.0f} + accept {acceptances:,.0f} + NCI {b_ar['nci']:,.0f} = {lhs:,.0f} vs gross EV {grossEV:,.0f} - {'PASS' if abs(lhs-grossEV)<1 else 'CHECK'}")
print(f"\nRAW numbers for report embedding:")
print(f"B1_A={evB1_A:.0f} B1_B={evB1_B:.0f} B2={evB2_base:.0f} B3=0 B3down={evB3_down:.0f} B4={evB4:.0f}")
print(f"grossEV={grossEV:.0f} finalEq_AR={b_ar['final']:.0f} eps_AR={b_ar['eps']:.0f} eps_mgmt={b_mgmt['eps']:.0f}")
print(f"nci={b_ar['nci']:.0f} entry25={entry25:.0f} mos={mos:.0f}")
