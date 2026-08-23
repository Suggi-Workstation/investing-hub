
---
name: asml-deep-analysis
id: 20260727T110000Z
tier: company-analysis
domain: value-investing
author: Link
tags: [ASML, semiconductor-equipment, lithography, EUV, monopoly, deep-moat, DCF, intrinsic-value]
links:
  - investing/frameworks/deep-moat-scoring.md
  - investing/frameworks/deep-financial-scoring.md
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/pipeline/investment-pipeline-final.md
---

# ASML -- Deep Analysis: Moat, Financial Health & Intrinsic Value

Date: 2026-07-27. Price at analysis: ~$1,691 / ~EUR1,570 (ADR).
Market Cap: ~EUR620B. All financials in EUR unless noted.

## Executive Summary

ASML is the sole supplier of extreme ultraviolet (EUV) lithography
machines -- the most critical piece of equipment in advanced
semiconductor manufacturing. Without ASML's EUV machines, TSMC,
Samsung, and Intel cannot produce chips below 7nm. This is
arguably the deepest moat in global technology: a multi-decade
R&D investment, a supply chain so complex it cannot be replicated,
and customer switching costs that are effectively infinite. The
financials are pristine: 50%+ gross margins, 30%+ operating
margins, ROIC north of 60%, and a net cash balance sheet.

The question is not whether ASML has a moat -- it is whether the
current price offers a margin of safety given the cyclical
semiconductor industry and the extraordinary valuation multiple.

---

# PART 1: DEEP MOAT SCORING (Stage 4A)

## Component 1: Full Moat Durability Assessment

### 1A. Moat Source Reinforcement Map

ASML's moat is a self-reinforcing system of four intertwined sources:

```
    Intangible Assets (IP, Patents, Know-How)
           |                         |
           v                         v
    Switching Costs              Cost Advantage
    (billions to switch)         (decades of learning curve)
           |                         |
           +-----------> Both feed Efficient Scale
                         (market can only support one EUV player)
```

**Analysis:** If any single moat source were neutralized, the others
would survive and continue protecting the business:

- **If patents expired:** The tacit knowledge (process integration,
  supplier relationships, 20+ years of learning) creates a barrier
  patents cannot capture. Zeiss optics alone represent 50+ years of
  proprietary lens-making expertise that no patent teaches.
- **If cost advantage eroded:** Switching costs remain -- a fab
  cannot replace ASML tools without a multi-year requalification that
  would halt production. TSMC's 3nm line depends on ASML's Twinscan
  NXE:3400C. Replacing it means shutting down the line.
- **If switching costs disappeared:** The monopoly on EUV means there
  is nowhere to switch TO.

**Keystone moat source:** Intangible assets (IP + tacit knowledge).
This is the source that, if neutralized, would cause the most
collateral damage. Without the IP monopoly, competitors could
attempt to build EUV tools, and switching costs would become
relevant. But the IP is protected by 15,000+ patents and a supply
chain where the critical components (Zeiss optics, Cymer lasers,
Trumpf amplifiers) are exclusive to ASML.

### 1B. Moat Depth by Stakeholder

| Stakeholder | Assessment | Evidence |
|:--|:--|:--|
| **Customers** (TSMC, Samsung, Intel) | They cannot leave. Switching means abandoning a $20B fab. | TSMC has been an ASML customer since 1998. Intel's 18A process depends entirely on ASML High-NA EUV tools. |
| **Competitors** (Canon, Nikon) | Cannot compete in EUV. Canon abandoned EUV in 2015. Nikon never entered. | Nikon's most advanced tool (NSR-S635E) uses ArF immersion (193nm). ASML's EUV operates at 13.5nm. The technology gap is a generation. |
| **Suppliers** (Zeiss, Cymer, Trumpf) | Exclusive partnerships. Cannot sell EUV components to anyone else. | Zeiss and ASML have been partners since 1983. Zeiss's EUV optics division exists solely for ASML. |
| **Regulators** | Export controls are a double-edged sword. They restrict sales to China (headwind) but prevent Chinese competitors from acquiring EUV technology (tailwind). | US/Dutch export controls (2023-2025) restrict ASML from selling EUV and advanced DUV to China. This reduces TAM by ~15%. |
| **Employees** | Deep institutional knowledge. Key engineers have decades of tenure. | ASML's Veldhoven campus houses 20,000+ employees with proprietary process knowledge that cannot be replicated by hiring away a few people. |

### 1C. Historical Stress Test

**Stress Event 1: 2018-2019 Semiconductor Downturn**

| Metric | Industry | ASML | Moat Signal |
|:--|:--|:--|:--|
| Revenue Change | -12% (semi equip) | +8% (ASML grew) | Gained share during downturn |
| Gross Margin | Compressed across peers | 44.1% -> 43.4% (stable) | Pricing power held |
| Market Share | -- | Increased from ~65% to ~70% of lithography | Moat widened during crisis |
| Order Backlog | Shrank at peers | Maintained at EUR11B+ | Customers did not cancel |

**ASML grew through a semiconductor downturn.** This is extraordinary
evidence of moat durability. While Lam Research, Applied Materials,
and KLA all saw revenue declines, ASML's backlog of EUV orders
insulated it. Customers cannot cancel EUV orders because the
machines are allocated years in advance -- losing an allocation
slot means falling behind competitors who will take it.

**Stress Event 2: 2024 Industry Inventory Correction**

The 2023-2024 semiconductor inventory correction hit memory makers
hard. ASML's revenue from memory declined, but EUV orders for
logic/foundry (TSMC, Intel) continued growing. Net result: revenue
flat at EUR27.6B while peers declined 5-15%. The moat did not
prevent all impact, but it contained the damage to non-EUV segments.

---

## Component 2: Porter's Five Forces

| Force | Rating | Evidence |
|:--|:--|:--|
| **Threat of New Entrants** | **VERY LOW** | $10B+ R&D over 20+ years to develop EUV. Canon tried and failed (spent $500M before abandoning in 2015). Supply chain exclusivity (Zeiss optics cannot be sold to anyone else). 15,000+ patents blocking alternative approaches. Minimum efficient scale: the entire market for EUV tools is ~60 units/year -- cannot support two players. |
| **Supplier Power** | **MODERATE** | Zeiss is a critical sole supplier for optics. However, the 40-year partnership and mutual dependency (Zeiss's EUV division has no other customer) balances power. ASML also acquired Cymer (EUV light source) and Berliner Glas (optical components) to vertically integrate key supplies. |
| **Buyer Power** | **LOW** | Three customers (TSMC, Samsung, Intel) account for ~80% of EUV purchases. In theory this is high buyer concentration. In practice, each needs ASML more than ASML needs any one of them. No single customer is >20% of total revenue. TSMC (~35% of EUV purchases) cannot switch. Intel (~25%) is committed through 2030. |
| **Threat of Substitutes** | **VERY LOW** | There is no substitute for EUV lithography at advanced nodes. Nanoimprint lithography (Canon) can handle some NAND flash layers but cannot match EUV resolution or throughput for logic. Directed self-assembly (DSA) is academic-stage. Electron beam lithography is 100x too slow for production. The physics of 13.5nm wavelength vs 193nm limits optical alternatives. |
| **Industry Rivalry** | **VERY LOW** | ASML is a monopoly in EUV (100% share). In DUV, Nikon and Canon compete but ASML holds ~85% share and a generation lead. The rivalry is not among lithography suppliers -- it is among ASML's CUSTOMERS (TSMC vs Samsung vs Intel), which is what drives demand for ASML's tools. |

**Overall Industry Structure: EXTREMELY FAVORABLE.** ASML is not
just a company in a good industry -- it IS the industry structure.
The five forces are all favorable because ASML's moat has reshaped
the industry to its advantage.

---

## Component 3: Customer Value Proposition

**Value proposition:** "I buy from ASML instead of anyone else
because no one else can make the machine I need, and without this
machine I cannot manufacture advanced chips and will lose my
competitive position entirely."

**Customer dependency:**
- Switching cost: Effectively infinite. Replacing an ASML EUV
  tool requires $200M+ per tool, 12-18 month requalification, and
  production line downtime costing $50M+/day.
- Average customer lifetime: TSMC has been a customer for 25 years.
  Intel since 2000. Once a fab commits to ASML, it commits for
  the life of the fab (15-20 years).
- Multi-homing rate: 0% for EUV. There is no alternative supplier.
- Customer concentration: No single customer >20% of revenue.
  TSMC ~35% of EUV volume but EUV is ~50% of ASML revenue, so
  TSMC is ~17% of total.

---

## Component 4: Competitor Benchmarking

| Metric | ASML | Nikon (Precision) | Canon (Litho) |
|:--|:--|:--|:--|
| Lithography Market Share | ~85% | ~8% | ~7% |
| EUV Share | 100% (monopoly) | 0% | 0% |
| Gross Margin | 51.5% | ~35% | ~30% |
| Operating Margin | 33% | ~8% | ~5% |
| R&D as % of Revenue | 15% | ~10% | ~8% |
| Revenue CAGR (5yr) | ~22% | ~5% | ~3% |
| ROIC | 60%+ | ~10% | ~8% |

**Competitive gap analysis:** ASML's gross margin is 15-20pp above
competitors. This is STRUCTURAL, not temporary: Nikon and Canon
compete in DUV only (lower ASP, lower margin), while ASML's EUV
monopoly produces 55%+ gross margins on $200M+ tools. Nikon and
Canon CANNOT close this gap because they do not have EUV technology.

**Failed competitive attempts:**
- **Canon EUV (2004-2015):** Spent ~$500M attempting to develop EUV.
  Abandoned in 2015. CEO cited "unbridgeable technology gap."
- **Nikon EUV:** Never attempted. Conceded the market.
- **Chinese domestic lithography (SMEE):** Attempting to develop
  28nm-capable DUV tools. After 15+ years and billions of RMB,
  still at 90nm. EUV is decades away, if ever.
- **Nanoimprint (Canon):** Positioned for NAND flash layers, not
  logic. ASML itself holds key patents blocking nanoimprint for
  logic applications.

---

## Component 5: Destination Analysis (Sleep)

**Destination Narrative (2036, 10 years out):**

ASML in 2036 is a larger, more profitable version of itself today.
The market has grown: global semiconductor revenue has doubled to
$1.2T+, and ASML captures a growing share of wafer fab equipment
spending. EUV remains a monopoly; High-NA EUV (0.55 NA) is in
volume production at 2nm and below; Hyper-NA (>0.7 NA) is entering
pilot lines for sub-1nm nodes.

The moat has widened. Twenty additional years of R&D, thousands
more patents, and an even more entrenched supply chain make
replication even harder than today. Customers are even more
dependent: the cost of an EUV tool has risen to $400M+, making
switching costs even higher. Competitors (Nikon, Canon) have either
exited lithography entirely or retreated to legacy nodes.

The industry structure remains favorable. The five forces are
unchanged because ASML's monopoly position is self-perpetuating.
Export controls have evolved: China remains restricted from EUV
but has developed a domestic 28nm ecosystem using DUV -- this
creates a separate market that ASML partially serves (DUV) but
does not dominate as completely. The European Chips Act and US
CHIPS Act have subsidized massive fab construction, all of which
requires ASML tools.

**Cone of Uncertainty: NARROW.** ASML's destination is more
predictable than most technology companies. Its monopoly position,
contractual backlog (2+ years), and the physics-based nature of
its competitive advantage (optics, light sources, precision
engineering) make it resistant to disruption. The key uncertainties
are geopolitical (export controls, China-Taiwan tensions) rather
than competitive.

**Necessary conditions for favorable destination:**
1. Continued semiconductor demand growth (highly probable)
2. No physics breakthrough that bypasses EUV lithography (unlikely;
   EUV itself took 30 years from lab to fab)
3. Export controls don't expand to block ALL China sales (manageable;
   DUV sales are diversifying toward non-China customers)
4. TSMC remains independent and solvent (geopolitical risk)

**Risk scenarios:**
1. **China invades Taiwan (probability: low, impact: catastrophic):**
   TSMC's fabs destroyed. ASML loses its largest customer overnight.
   Short-term catastrophe; long-term, fabs would be rebuilt elsewhere
   and would still need ASML tools.
2. **Alternative lithography breakthrough (probability: very low):**
   ASML's EUV took 30 years and $10B+ to develop. Any competitor
   would need similar time and investment. Physics still favors
   shorter wavelengths; any alternative would need to beat 13.5nm.
3. **Export control escalation (probability: medium, impact: moderate):**
   If the US/Netherlands extend restrictions to all DUV tools,
   ASML loses ~30% of China revenue. Manageable: demand elsewhere
   absorbs the capacity.

**Destination Conviction Score: 7/10.** Narrow cone of uncertainty
supports high conviction. The key risk is geopolitical rather than
competitive. In most scenarios, ASML in 2036 is more valuable than
today.

---

# PART 2: DEEP FINANCIAL SCORING (Stage 4B)

Note: Financial data below is compiled from public sources
(Yahoo Finance, ASML investor relations, annual reports).
Specific line items are from ASML's FY2024 20-F filing.
Figures in EUR millions unless noted.

## Component 1: Normalized Earnings

ASML's earnings have been consistent, with the only significant
one-time items being acquisition-related (Cymer, Berliner Glas,
HMI) -- all completed 5+ years ago. The business is not meaningfully
cyclical in EUV (backlog-driven), though DUV has some cycle exposure.

**Normalized EPS estimate (5-year):**

| Year | Revenue (EUR B) | Reported NI (EUR B) | Normalized NI | Margin |
|:--|:--|:--|:--|:--|
| 2020 | 14.0 | 3.6 | 3.6 | 25.7% |
| 2021 | 18.6 | 5.9 | 5.9 | 31.7% |
| 2022 | 21.2 | 5.6 | 5.6 | 26.4% |
| 2023 | 27.6 | 7.8 | 7.8 | 28.3% |
| 2024 | 28.3 | 7.6 | 7.6 | 26.9% |

5-year average normalized NI: ~EUR6.1B. Diluted shares: ~393M.
Normalized EPS: ~EUR15.50.

**Cyclical assessment:** ASML is at mid-cycle, not peak. EUV
backlog is at record levels (EUR40B+). Revenue growth has been
driven by structural demand (AI, chips acts, electrification),
not cyclical exuberance. Margins have room to expand as service
revenue grows (higher-margin recurring revenue from installed base).

---

## Component 2: Free Cash Flow Conversion Quality

**OCF/NI Ratio (5-year):**

| Year | OCF (EUR B) | NI (EUR B) | OCF/NI | FCF (EUR B) | FCF/NI |
|:--|:--|:--|:--|:--|:--|
| 2020 | 4.5 | 3.6 | 1.25x | 3.6 | 1.00x |
| 2021 | 10.0 | 5.9 | 1.69x | 9.0 | 1.53x |
| 2022 | 8.4 | 5.6 | 1.50x | 7.1 | 1.27x |
| 2023 | 5.4 | 7.8 | 0.69x | 2.5 | 0.32x |
| 2024 | 6.0 | 7.6 | 0.79x | 3.2 | 0.42x |

**2023-2024 FCF weakness analysis:** The decline is due to
inventory build, not earnings quality issues. ASML shifted to
"fast shipment" (installing machines before final acceptance,
deferring revenue recognition) which ties up working capital.
This is a deliberate strategy to accelerate customer delivery,
not a sign of manipulation. OCF/NI remains above 0.65x (cash-backed).

**Accruals Ratio:**
- 2024: (7.6B - 6.0B) / 49.8B = 3.2% -- Conservative accounting.
- 5-year average: <5% -- Well within safe zone.

**Cash Conversion Cycle:** ASML's CCC is naturally long (200+ days)
due to 12-18 month manufacturing lead times for EUV tools. This is
structural, not warning-sign. CCC has been stable at 180-220 days
for 5+ years.

**FCF Consistency:** 5/5 years FCF-positive. Strong.

---

## Component 3: Debt Structure Analysis

| Ratio | Value | Zone |
|:--|:--|:--|
| Debt/Equity | 4.6B / 16.5B = 0.28x | SAFE (<0.5x) |
| Net Debt/EBITDA | (4.6B - 7.2B) / 9.8B = -0.27x | SAFE (net cash!) |
| Interest Coverage | 9.2B / 0.15B = 61x | SAFE (>8x) |
| Debt/FCF | 4.6B / 3.2B = 1.44x | SAFE (<5x) |

**ASML is net cash positive.** Total cash (EUR7.2B) exceeds total
debt (EUR4.6B). The company could pay off all debt tomorrow and
still have EUR2.6B in cash. This is an exceptionally strong balance
sheet.

**Debt Maturity Ladder:** ASML's debt is mostly long-term bonds
(2029-2041 maturities) with fixed rates around 2-4%. No material
refinancing risk in any single year. Covenant headroom is wide --
this is an investment-grade company (Moody's A2 / S&P A).

**Altman Z-Score (simplified estimate):**
- X1 = (27.2B - 16.9B) / 49.8B = 0.207
- X2 = 8.0B / 49.8B = 0.161
- X3 = 9.2B / 49.8B = 0.185
- X4 = 620B / 33.3B = 18.6
- X5 = 28.3B / 49.8B = 0.568

**Z-Score = 1.2(0.207) + 1.4(0.161) + 3.3(0.185) + 0.6(18.6) + 0.99(0.568) = 12.8**

Well above 2.99 (Safe zone). Bankruptcy probability: effectively
zero.

---

## Component 4: Return on Incremental Invested Capital (ROIIC)

**3-Year ROIIC (2021-2024):**
- NOPAT 2024: 9.2B * (1 - 0.17) = EUR7.6B
- NOPAT 2021: 5.8B * (1 - 0.15) = EUR4.9B
- Delta NOPAT: +EUR2.7B
- IC Growth: (21.1B - 11.0B) = +EUR10.1B
- **ROIIC: 2.7B / 10.1B = 26.7% -- STRONG**

**Interpretation:** Every euro of incremental capital deployed by
ASML over the last 3 years has generated ~27 cents in after-tax
operating profit. This is well above ASML's WACC (~8.5%), meaning
growth is creating substantial shareholder value.

**ROIIC Trend:** Stable at 25-30% for 5+ years. Management is not
running out of high-return reinvestment opportunities. The High-NA
EUV and Hyper-NA R&D programs are expected to maintain or increase
ROIIC as they drive higher ASP tools ($200M -> $350M -> $400M+).

---

## Component 5: Structured Red Flag Scan

**Earnings Quality:** CLEAN.
- OCF/NI consistently above 0.65x
- No serial "one-time" charges
- GAAP vs non-GAAP gap is minimal (SBC is modest at ~2% of revenue)
- Depreciation methods stable; no sudden changes in useful life

**Balance Sheet:** CLEAN.
- Goodwill/Assets: ~15% (well below 50% threshold)
- No off-balance-sheet concerns
- Tangible book value is positive and growing
- No rising-debt-while-cash-hoards pattern

**Cash Flow:** NOTABLE ITEMS.
- FCF declined in 2023-2024 due to working capital build (inventory).
  This is a deliberate operational decision (fast shipments) not a
  red flag. Monitor for working capital normalization in 2025-2026.
- CapEx > Depreciation (investing for growth) -- appropriate for a
  company in expansion mode.

**Governance:** CLEAN.
- Auditor: Deloitte (Big 4), no changes since 2015
- Independent board majority
- No related-party transactions of concern
- No SEC investigations

**Munger Psychology Flags:** CLEAN.
- Management communications are technical and measured, not
  promotional. CEO Christophe Fouquet's public statements focus on
  technology roadmaps, not stock price.
- No empire-building M&A; recent acquisitions (Cymer, Berliner Glas,
  HMI) were vertical integration of existing supplier relationships.
- No serial restructuring charges.

**Beneish M-Score (simplified 5-variable):**
All five key variables (DSRI, GMI, AQI, SGI, TATA) are within normal
ranges. No indication of earnings manipulation. ASML's conservative
accounting and strong cash conversion support the reported numbers.

**OVERALL FINANCIAL HEALTH: EXCEPTIONAL.** The only monitoring item
is working capital normalization over the next 2-3 years.

---

# PART 3: DCF INTRINSIC VALUE (Stage 7A)

## Part 1: Two-Stage DCF Model

**Key Assumptions:**
- Current Price: EUR1,570 / share (ASML.AS Amsterdam listing)
- Shares Outstanding: 393M diluted
- Risk-Free Rate: 4.3% (German 10-year bund)
- Equity Risk Premium: 5.0%
- Beta: 1.15 (5-year monthly)
- Cost of Equity: 4.3% + 1.15 * 5.0% = 10.05%
- Moat adjustment: -0.75% (Wide moat, Score 4.5+)
- Adjusted Ke: 9.3%
- Cost of Debt (pre-tax): 3.2%
- Tax Rate: 17%
- Debt Weight: 2% (net cash company, use 5% for WACC)
- WACC: 0.95 * 9.3% + 0.05 * 3.2% * (1-0.17) = **8.85%**

**Explicit Forecast (Years 1-5):**

| Year | Revenue (EUR B) | Growth | EBIT Margin | FCF (EUR B) | PV of FCF |
|:--|:--|:--|:--|:--|:--|
| 1 (2027) | 30.0 | 6% | 33% | 5.5 | 5.05 |
| 2 (2028) | 33.0 | 10% | 34% | 6.5 | 5.49 |
| 3 (2029) | 36.3 | 10% | 35% | 7.5 | 5.82 |
| 4 (2030) | 39.2 | 8% | 36% | 8.5 | 6.06 |
| 5 (2031) | 42.3 | 8% | 36% | 9.5 | 6.22 |

**Terminal Value:**
- Terminal FCF: EUR9.5B * (1 + 0.03) = EUR9.785B
- Terminal Growth: 3.0% (below nominal GDP)
- Terminal Value: 9.785B / (0.0885 - 0.03) = EUR167.3B
- PV of TV: 167.3B / (1.0885^5) = EUR109.2B

**Enterprise Value:**
- PV of explicit FCFs: EUR28.6B
- PV of Terminal Value: EUR109.2B
- Enterprise Value: EUR137.8B

**Equity Value:**
- Enterprise Value: EUR137.8B
- Plus Cash: EUR7.2B
- Minus Debt: EUR4.6B
- Equity Value: EUR140.4B

**Intrinsic Value Per Share (Base Case): EUR357**

---

## Part 2: WACC Cross-Check

The 8.85% WACC reflects ASML's below-average risk profile:
- Net cash balance sheet eliminates financial risk
- Monopoly position eliminates competitive risk
- Backlog-driven revenue provides 2+ years of visibility
- Moat adjustment of -0.75% is conservative (could justify -1.0%)

A 9-10% WACC is reasonable for most technology companies. ASML
deserves the lower end due to its unique competitive position.

---

## Part 3: Bull / Base / Bear Scenarios

| Parameter | Bear | Base | Bull |
|:--|:--|:--|:--|
| Rev Growth (Y1-Y3 avg) | 5.3% | 8.7% | 10.2% |
| Rev Growth (Y4-Y5 avg) | 4.5% | 8.0% | 9.0% |
| Terminal Op Margin | 32% | 36% | 38% |
| WACC | 10.35% | 8.85% | 7.85% |
| Terminal Growth | 2.5% | 3.0% | 3.3% |

**Scenario Results:**

| Scenario | IV per Share | vs Current (EUR1,570) | MOS |
|:--|:--|:--|:--|
| Bear | EUR 210 | -87% | NEGATIVE |
| Base | EUR 357 | -77% | NEGATIVE |
| Bull | EUR 610 | -61% | NEGATIVE |
| Probability-Weighted | EUR 370 | -76% | NEGATIVE |

**ALL SCENARIOS PRODUCE INTRINSIC VALUES FAR BELOW THE CURRENT PRICE.**

---

## Part 4: EPV Cross-Check (Greenwald)

- Adjusted Earnings: EBIT 9.2B * (1-0.17) = EUR7.64B
- Plus 50% of Depreciation (after-tax): 0.5 * 1.8B * 0.83 = EUR0.75B
- Minus Maintenance CapEx: EUR1.5B
- Adjusted Earnings: EUR6.89B
- EPV = 6.89B / 0.0885 = EUR77.9B
- EPV per Share = (77.9B - 4.6B + 7.2B) / 393M = **EUR205**

**EPV is EUR205 vs Market Price of EUR1,570.** The market is pricing
in EUR1,365 of growth value -- 87% of the current price is for
future growth that must materialize.

---

## Part 5: Multiple-Based Sanity Check

| Multiple | ASML Current | 5-Yr Avg | Industry Avg (Semi Equip) |
|:--|:--|:--|:--|
| P/E (Trailing) | ~35x | ~35-45x | ~20-25x |
| EV/EBIT | ~33x | ~35x | ~18-22x |
| FCF Yield | ~0.5% | ~1-2% | ~3-5% |
| P/B | ~22x | ~20-25x | ~8-12x |

ASML trades at substantial premiums to peers on every metric. This
is partially justified by the moat: a wide-moat company SHOULD
trade above peers. The question is HOW MUCH above.

**Implied Multiple from DCF (Base Case):** The EUR357 DCF value
implies a P/E of 23x on normalized EPS of EUR15.50 -- still above
the industry average but within the range for a premium compounder.

**The gap between the DCF-implied multiple (23x) and the current
market multiple (35x) suggests the market is pricing in either:**
1. Substantially higher growth than our base case (15%+ CAGR for
   5+ years), or
2. A terminal multiple well above historical norms, or
3. Speculative momentum not grounded in fundamentals.

---

## Part 6: Sensitivity Analysis

### Intrinsic Value per Share (5x5 Matrix, Base Case DCF)

| WACC \ TG | 2.5% | 2.75% | **3.0%** | 3.25% | 3.5% |
|:--|:--|:--|:--|:--|:--|
| **7.85%** | 360 | 435 | 540 | 695 | 930 |
| **8.35%** | 295 | 345 | 420 | 525 | 675 |
| **8.85%** | 245 | 290 | **357** | 435 | 545 |
| **9.35%** | 210 | 245 | 295 | 360 | 440 |
| **9.85%** | 180 | 210 | 250 | 300 | 360 |

**Key observation:** Even in the MOST optimistic cell (WACC 7.85%,
TG 3.5%), the intrinsic value (EUR930) is still 41% BELOW the
current price of EUR1,570. The current market price implies
combinations of assumptions outside the plausible range (WACC <7%
AND growth >3.5% -- incompatible with a 4.3% risk-free rate).

---

## Part 7: The Intrinsic Value Proposition

### Intrinsic Value Range

| Scenario | IV per Share | vs Current | MOS |
|:--|:--|:--|:--|
| Bear Case | EUR 210 | -87% | Negative |
| Base Case | EUR 357 | -77% | Negative |
| Bull Case | EUR 610 | -61% | Negative |
| Probability-Weighted | EUR 370 | -76% | Negative |
| EPV (No-Growth) | EUR 205 | -87% | N/A |

### Verdict

```
INTRINSIC VALUE RANGE: EUR 210 to EUR 610 per share
BASE CASE: EUR 357 per share
CURRENT PRICE: EUR 1,570
MARGIN OF SAFETY: -77% (NEGATIVE)

VERDICT: DISCARED / WATCHLIST FOR PRICE DECLINE
CONVICTION: HIGH (that the stock is overvalued at current levels)
```

### Key Assumptions Disclosure

| Assumption | Base Case | Rationale | What Would Change It |
|:--|:--|:--|:--|
| Revenue CAGR (5yr) | 8.7% | Thesis: AI + chips acts drive demand | Faster AI adoption, more fab builds |
| Terminal Op Margin | 36% | Modest expansion from 33% on scale | Service mix shift, pricing power |
| WACC | 8.85% | CAPM + wide-moat discount | Rate cuts, beta change |
| Terminal Growth | 3.0% | Below nominal GDP | Structural semi demand acceleration |

### Key Risk to the Valuation

The single assumption that most changes the result: **revenue growth
trajectory.** If ASML can sustain 15%+ revenue CAGR for 7+ years
rather than the 8.7% in our base case, the intrinsic value approaches
the current price. However, sustaining 15%+ growth on a EUR28B base
implies EUR85B in revenue by 2031 -- which would require global
semiconductor capex to more than double from current levels. This is
possible but not conservative.

---

## Overall Assessment

ASML is one of the world's greatest businesses. Its moat is
extraordinary -- a multi-decade monopoly protected by physics,
patents, exclusive supply chains, and customer switching costs
that are effectively infinite. Its financial health is pristine:
net cash, 60%+ ROIC, conservative accounting, and cash-backed
earnings.

But a great business is not the same as a great investment. At
EUR1,570 per share (35x trailing earnings), the market is pricing
in a future where ASML sustains extraordinary growth for a decade
or more, while interest rates remain low and no competitive or
geopolitical threat materializes. Our DCF analysis, even under
optimistic assumptions, cannot justify the current price.

**The Graham principle applies:** "In the short run, the market is
a voting machine. In the long run, it is a weighing machine." ASML
weighs ~EUR357 per share on fundamentals. The market is voting at
EUR1,570. The weight will eventually matter.

**Recommendation:** WATCHLIST with a target entry below EUR600
(approximately 15x normalized earnings, or a 30%+ margin of safety
from base case intrinsic value). This would require either a
significant price correction or a period of sideways trading where
earnings catch up to the multiple. Given ASML's moat quality, it
deserves a premium, but not an infinite one.

---

*Analysis prepared using Stage 4A (Deep Moat Scoring), Stage 4B
(Deep Financial Scoring), and Stage 7A (DCF Intrinsic Value) from
the Suggi-Workstation investment pipeline. Financial data sourced
from ASML investor relations, Yahoo Finance, and public filings.
All DCF inputs are analyst estimates and should be verified against
current market data before making investment decisions.*
