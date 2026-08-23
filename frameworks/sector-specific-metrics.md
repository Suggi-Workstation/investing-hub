---
name: sector-specific-metrics
id: 20260726T212000Z
tier: framework
domain: value-investing
author: Ava
tags: [sector-metrics, screening, valuation, SaaS, banks, REITs, insurance, energy, industrials, composite-ranking]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/dcf-intrinsic-value.md
  - library/value-investing/anchor-value-investing.md
---

# Sector-Specific Metrics -- Choosing the Right Yardstick for Every Business (Phase A)

This framework explains how to select and apply the correct growth,
quality, and cheapness metrics for each sector in the pipeline's
Stage 1 (composite ranking) and Stage 2 (broad screen). A one-size-
fits-all screening approach systematically misranks banks, SaaS
companies, REITs, insurers, and cyclicals. The right metric for
one sector is meaningless or misleading for another.

## Why One Metric Cannot Rule Them All

Two companies trade at 12x earnings. One is an automaker coming off
record profits; the other is a software company growing 20% annually
with 85% gross margins. Same P/E, opposite verdicts: the automaker is
expensive (cyclical peak earnings); the software company is cheap
(durable, capital-light earnings).

Five structural forces explain why sectors need different metrics:

1. **Capital intensity:** A railroad pours billions into track to grow;
   software grows on marginal server costs. A dollar of railroad
   earnings converts to far less free cash flow than a dollar of
   software earnings.

2. **Leverage as raw material:** For most companies, debt is a financing
   choice. For banks and insurers, deposits and premiums are the raw
   material of the business. Metrics that strip out debt (EV/EBITDA)
   destroy what you are trying to measure.

3. **Accounting distortions:** REITs must depreciate buildings that
   often appreciate, making reported earnings meaningless. Insurance
   accounting obscures the value of float. Energy companies deplete
   assets that depreciation does not capture.

4. **Cyclicality:** Commodity producers, semiconductor makers, and
   homebuilders see earnings swing 50% or more through a cycle. Any
   single year's earnings are a snapshot of a moving target.

5. **Growth durability:** A multiple is an implicit forecast of how
   long above-average returns persist. That horizon differs enormously
   between a niche software monopoly and a regional airline.

**The golden rule:** Compare companies only against sector peers. A
cross-sector P/E ranking is not finding bargains -- it is finding
automakers at cycle peaks, banks with hidden credit risk, and shrinking
legacy businesses.

## The Sector Metric Matrix

The pipeline's Stage 1 uses three metrics per sector: a **growth**
metric (how fast is the business compounding?), a **quality** metric
(how good are the returns on capital?), and a **cheapness** metric
(how much are you paying for it?).

| Sector | Growth Metric | Quality Metric | Cheapness Metric |
|:--|:--|:--|:--|
| Industrial / Consumer | Revenue CAGR (5-10yr) | ROIC | EV/EBIT |
| Technology (SaaS) | Revenue CAGR | Rule of 40 (Rev Growth + FCF Margin) | EV/Revenue |
| Financial (Banks) | Book Value per Share Growth | ROE | P/B |
| Financial (Insurance) | Premium Growth | Combined Ratio | P/B |
| REITs | FFO/Share Growth | ROE | P/FFO |
| Energy / Materials | Production Volume Growth | ROCE | EV/EBITDA |
| Healthcare (Pharma) | Revenue CAGR | ROIC | EV/EBIT |
| Utilities | Regulated Asset Growth | Allowed ROE vs Earned ROE | P/B or Dividend Yield |
| Default | Revenue CAGR | ROIC | EV/EBIT |

### Composite Ranking Formula

```
Composite Rank = 0.25 * growth_percentile + 0.25 * quality_percentile + 0.50 * cheapness_percentile
```

Cheapness gets double weight (50%) because the pipeline is a value
investing system -- the goal is to find cheap companies first, then
filter for quality. Sort ascending (lower rank = better).

## Sector Deep Dives

### Industrial / Consumer (Default Sector)

These sectors encompass most non-financial, non-resource businesses:
manufacturing, retail, consumer goods, business services, healthcare
services, and general industrials.

**Why these metrics:**

ROIC is the correct quality metric because these businesses deploy
tangible capital (factories, inventory, distribution networks).
ROIC measures how efficiently that capital generates operating profits,
independent of how the business is financed. EV/EBIT is the correct
cheapness metric because it is capital-structure neutral -- it values
the whole enterprise, not just the equity, making it comparable across
companies with different debt levels.

**Growth metric: Revenue CAGR (5-10 years)**

```
Revenue CAGR = (Revenue_Today / Revenue_5YearsAgo)^(1/5) - 1
```

Use 5 years minimum, 10 years if available. A longer window smooths
cyclicality. For companies with significant M&A, prefer organic revenue
growth if disclosed.

**Quality metric: ROIC**

```
ROIC = EBIT * (1 - Tax Rate) / (Total Debt + Shareholders' Equity - Cash)
```

Use 5-year average ROIC, not the most recent year. A single year of
high ROIC may reflect a cyclical peak.

| ROIC (5yr avg) | Quality Signal |
|:--|:--|
| >25% | Exceptional -- wide moat likely |
| 15-25% | Strong |
| 10-15% | Adequate |
| 5-10% | Mediocre -- barely above cost of capital |
| <5% | Poor -- likely destroying value |

**Cheapness metric: EV/EBIT**

```
EV = Market Cap + Total Debt - Cash
EV/EBIT = Enterprise Value / EBIT
```

| EV/EBIT | Cheapness Signal |
|:--|:--|
| <8x | Very cheap (investigate -- may be cheap for a reason) |
| 8-12x | Reasonably priced |
| 12-16x | Fair to slightly expensive |
| 16-20x | Expensive (requires strong growth to justify) |
| >20x | Very expensive |

**Stage 2 thresholds (industrial/consumer):**
- Revenue CAGR >= 10% (5-10yr)
- ROIC >= 15% (5yr avg)
- MVP tightened: CAGR >= 15%, ROIC >= 20%

**What NOT to use:** P/E alone (ignores debt structure). P/B for
asset-light businesses (book value is meaningless for companies whose
primary assets are intangible).

### Technology / SaaS

SaaS businesses break standard valuation because their economics are
fundamentally different: 70-85% gross margins, negative near-term
earnings from heavy growth investment, capital-light expansion, and
recurring revenue that makes current earnings a poor proxy for future
earnings.

**Why these metrics:**

Rule of 40 is the standard SaaS quality metric because it acknowledges
the growth-profitability tradeoff. A company growing 40% with -10%
margins (Rule of 40 = 30) is investing for the future. A company growing
5% with 35% margins (Rule of 40 = 40) is harvesting. Both can create
value. The metric captures this. EV/Revenue is correct for cheapness
because many SaaS companies have no earnings yet -- you must value the
revenue stream and assess whether margins will emerge at scale.

**Growth metric: Revenue CAGR**

Same calculation as industrial. Revenue growth is the primary driver of
SaaS valuation. For subscription businesses, also check ARR (Annual
Recurring Revenue) growth if disclosed.

**Quality metric: Rule of 40**

```
Rule of 40 = Revenue Growth Rate (%) + FCF Margin (%)
            or Revenue Growth Rate (%) + EBITDA Margin (%)
```

FCF margin is preferred (harder to manipulate). EBITDA margin is an
acceptable alternative.

| Rule of 40 Score | Quality Signal | Typical EV/Revenue (2026) |
|:--|:--|:--|
| >50 | Exceptional -- growth AND profitability | 12-20x |
| 40-50 | Strong -- healthy balance | 8-14x |
| 30-40 | Adequate -- tradeoff reasonable | 5-9x |
| 20-30 | Below par -- one side suffering | 3-6x |
| <20 | Poor -- neither growing nor profitable | 2-4x |

Every 10-point improvement in Rule of 40 corresponds to approximately
1.0-1.5x higher EV/Revenue multiple.

**Cheapness metric: EV/Revenue**

```
EV/Revenue = Enterprise Value / Trailing 12-Month Revenue
```

| EV/Revenue | Cheapness Signal |
|:--|:--|
| <3x | Very cheap (but check growth -- low growth SaaS deserves low multiples) |
| 3-6x | Reasonable for moderate-growth SaaS |
| 6-10x | Fair for above-average growth |
| 10-15x | Expensive for established; reasonable for hypergrowth |
| >15x | Very expensive (requires 30%+ growth to justify) |

**Additional SaaS quality checks for Stage 2:**
- Gross margin > 70% (below 70% = not a true SaaS business model)
- Net Revenue Retention > 100% (existing customers expanding, not shrinking)
- CAC Payback < 18 months (efficient customer acquisition)

**Stage 2 thresholds (SaaS):**
- Revenue CAGR >= 15% (MVP: >= 20%)
- Rule of 40 >= 30 (MVP: >= 35)
- Gross margin >= 70% (hard filter -- below this, not SaaS economics)

**What NOT to use:** P/E (most SaaS companies have no E). P/B (book
value is meaningless -- primary assets are code and customers, not on
the balance sheet). EV/EBITDA for early-stage (distorted by growth
spending).

### Financial / Banks

Banks are unlike any other business. Their assets (loans) and
liabilities (deposits) are marked close to market. Interest is both
revenue and cost of goods sold. Debt is not financing -- it is raw
material.

**CRITICAL: EV/EBITDA DOES NOT EXIST FOR BANKS.** Enterprise value adds
debt to market cap, but a bank's "debt" (deposits) is its business
input. Stripping out interest removes the business itself. Any screener
showing EV/EBITDA for a bank is producing a calculation artifact, not
information.

**Why these metrics:**

P/B is the natural valuation anchor because a bank's balance sheet is
its business. Book value represents shareholder equity invested in
loans and securities. ROE measures how productively that equity is
deployed. Justified P/B = (ROE - g) / (Ke - g). A bank earning 15% ROE
deserves a premium to book; one earning 6% deserves a discount.

**Growth metric: Book Value per Share Growth**

```
BV/Share Growth = (BVPS_Today / BVPS_5YearsAgo)^(1/5) - 1
Tangible BV/Share Growth = Same, using tangible book value
```

Tangible book value (excluding goodwill and intangibles) is preferred
for banks with significant acquisition history.

| BV/Share CAGR | Signal |
|:--|:--|
| >10% | Strong compounding (rare for large banks) |
| 6-10% | Healthy growth |
| 3-6% | Modest growth |
| <3% | Stagnant |

**Quality metric: ROE**

```
ROE = Net Income / Average Shareholders' Equity
```

Use 5-year average. Bank earnings are cyclical (credit losses surge in
recessions). A single year of high ROE may reflect an unsustainably
benign credit environment.

| ROE (5yr avg) | Quality Signal |
|:--|:--|
| >15% | Exceptional franchise (JPMorgan tier) |
| 12-15% | Strong |
| 10-12% | Adequate |
| 8-10% | Mediocre |
| <8% | Below cost of equity -- destroying value |

**Cheapness metric: P/B**

```
P/B = Market Cap / Book Value of Equity
P/TBV = Market Cap / Tangible Book Value (preferred)
```

| P/B | Cheapness Signal |
|:--|:--|
| <0.8x | Very cheap (investigate credit quality -- cheap banks are often cheap for a reason) |
| 0.8-1.2x | Reasonably priced for average ROE |
| 1.2-1.8x | Premium pricing (requires above-average ROE to justify) |
| 1.8-2.5x | Expensive (requires exceptional ROE >15%) |
| >2.5x | Very expensive |

**Additional bank quality checks:**
- CET1 Ratio > 11% (regulatory capital strength)
- Net Interest Margin (NIM) trend (stable or expanding = good)
- Efficiency Ratio < 60% (lower is better)
- Non-Performing Loan ratio < 2%
- Loan Loss Reserve / NPLs > 100%

**Stage 2 thresholds (banks):**
- BV/Share CAGR >= 5%
- ROE >= 10% (5yr avg)
- CET1 >= 11%

**What NOT to use:** EV/EBITDA (meaningless), EV/EBIT (meaningless),
DCF with standard WACC (debt is operational, not financing), P/E alone
(ignores credit cycle).

### Financial / Insurance

Insurance shares the financial-sector caveat (debt is raw material) but
adds its own complexity: the combined ratio determines whether the
core business creates or destroys value, and float is an asset that
standard accounting ignores.

**Why these metrics:**

Premium growth measures organic expansion. The combined ratio is THE
quality metric -- it tells you whether underwriting is profitable.
Combined ratio below 100% means the insurer makes money on underwriting
BEFORE investment income. The best insurers (GEICO, Progressive) run
combined ratios in the low 90s. P/B works for cheapness because
insurance balance sheets are marked close to market.

**Growth metric: Premium Growth**

```
Gross Written Premium Growth = (GWP_Today / GWP_LastYear - 1)
Net Written Premium Growth (preferred) = Same using net premiums
```

| Premium Growth (5yr CAGR) | Signal |
|:--|:--|
| >12% | Aggressive growth (watch combined ratio -- growing into bad risks?) |
| 7-12% | Healthy growth |
| 3-7% | Modest |
| <3% | Stagnant or shrinking |

**Quality metric: Combined Ratio**

```
Combined Ratio = Loss Ratio + Expense Ratio
Loss Ratio = Claims Paid + Change in Reserves / Earned Premiums
Expense Ratio = Underwriting Expenses / Written Premiums
```

| Combined Ratio (5yr avg) | Quality Signal |
|:--|:--|
| <92% | Exceptional underwriting discipline |
| 92-96% | Strong |
| 96-100% | Adequate (profit from float, not underwriting) |
| 100-105% | Underwriting loss (investment income must compensate) |
| >105% | Serious underwriting problems |

**Cheapness metric: P/B**

Same as banks. Most insurers trade between 0.8x and 2.0x book. P/B
premiums are justified by combined ratios consistently below 95%.

**Float value adjustment:** A superior insurer generates "free float"
that standard P/B misses. Estimate:

```
Float Value = Float * (1 - Combined Ratio / Cost of Capital)

Where Float = Unearned Premium Reserve + Loss Reserves
```

If combined ratio < 100% and stable, the float has positive value above
book. If combined ratio > 100%, float is a liability.

**Stage 2 thresholds (insurance):**
- Premium Growth >= 5% (5yr CAGR)
- Combined Ratio <= 98% (5yr avg)

**What NOT to use:** EV/EBITDA, standard P/E (earnings distorted by
reserve changes and catastrophe losses).

### REITs (Real Estate Investment Trusts)

REITs are the clearest case of accounting rules breaking a metric.
GAAP requires depreciating buildings over decades, producing large
non-cash charges -- even though well-maintained property often
appreciates. Reported net income drastically understates the cash
properties actually generate.

**Why these metrics:**

FFO (Funds From Operations) adds back depreciation and strips out
property sale gains, giving a truer picture of operating cash flow.
FFO/share growth is the correct growth metric. ROE measures management's
skill at deploying equity. P/FFO is the standard cheapness multiple.

**Growth metric: FFO per Share Growth**

```
FFO = Net Income + Real Estate Depreciation - Gains on Property Sales
FFO/Share = FFO / Diluted Shares Outstanding
FFO/Share Growth = (FFOPS_Today / FFOPS_5YearsAgo)^(1/5) - 1
```

**Why P/E lies for REITs:** A REIT with $1.10 EPS (including $1.65
depreciation) may show a P/E of 40 -- absurd. But FFO = $1.10 + $1.65
= $2.75, and P/FFO = 16, which is normal for a quality REIT.

**Quality metric: ROE**

```
ROE = Net Income / Average Shareholders' Equity
```

Use FFO-based ROE for a cleaner picture:
```
FFO-ROE = FFO / Average Shareholders' Equity
```

| FFO-ROE | Quality Signal |
|:--|:--|
| >12% | Exceptional |
| 8-12% | Strong |
| 5-8% | Adequate |
| <5% | Poor |

**Cheapness metric: P/FFO**

```
P/FFO = Market Cap / FFO (or Price per Share / FFO per Share)
```

| P/FFO | Cheapness Signal |
|:--|:--|
| <12x | Very cheap |
| 12-16x | Reasonable |
| 16-20x | Fair to slightly expensive |
| 20-25x | Expensive |
| >25x | Very expensive |

**Additional REIT quality checks:**
- AFFO (Adjusted FFO) = FFO - Recurring CapEx - Straight-Line Rent Adj
- Occupancy rate trend
- Debt / Gross Asset Value < 50%
- Same-property NOI growth

**Stage 2 thresholds (REITs):**
- FFO/Share CAGR >= 5%
- ROE >= 8%
- Occupancy >= 90%

**What NOT to use:** P/E (distorted by depreciation), EV/EBITDA
(distorted by depreciation + debt structure).

### Energy / Materials

These are cyclicals with depleting assets. Earnings swing violently
with commodity prices. Using current earnings guarantees buying at the
peak and selling at the trough.

**Why these metrics:**

Production volume growth is a better growth metric than revenue growth
because revenue is dominated by commodity price swings (a company did
not "grow" if revenue doubled because oil went from $40 to $80).
ROCE (Return on Capital Employed) is preferred over ROIC for capital-
intensive resource businesses. EV/EBITDA is the standard cheapness
metric because D&A varies enormously across companies with different
asset ages and accounting policies.

**Growth metric: Production Volume Growth**

```
Volume Growth = (Current Year Production / Prior Year Production) - 1
```

Use physical units: barrels of oil equivalent per day (BOE/d), tonnes
of copper, million cubic feet of gas. This isolates operational growth
from commodity price noise.

**Quality metric: ROCE**

```
ROCE = EBIT / (Total Assets - Current Liabilities)
     = EBIT / Capital Employed
```

| ROCE (5yr avg, cycle-normalized) | Quality Signal |
|:--|:--|
| >15% | Exceptional (low-cost producer advantage) |
| 10-15% | Strong |
| 7-10% | Adequate |
| <7% | High-cost producer -- vulnerable in downturns |

The key distinction: a low-cost producer with 12% ROCE at mid-cycle
prices is a better business than a high-cost producer with 20% ROCE
at peak prices.

**Cheapness metric: EV/EBITDA**

```
EV/EBITDA = Enterprise Value / EBITDA
```

Use cycle-normalized EBITDA (5-7 year average), not current EBITDA.

| EV/EBITDA (normalized) | Cheapness Signal |
|:--|:--|
| <5x | Very cheap |
| 5-7x | Reasonable |
| 7-9x | Fair |
| 9-12x | Expensive |
| >12x | Very expensive (peak-cycle EBITDA likely) |

**Reserve life check:** For oil & gas and mining companies:
```
Reserve Life = Proven Reserves / Annual Production
```

Reserve life < 8 years = the company is depleting faster than it
replaces. This is a red flag regardless of how cheap it looks on EV/
EBITDA.

**Stage 2 thresholds (energy/materials):**
- Production volume not declining (>0% CAGR)
- ROCE >= 10% (cycle-normalized)
- Reserve life > 8 years (for extractive industries)

**What NOT to use:** Current P/E (cyclical peak illusion), P/B (book
value may not reflect reserve value).

### Healthcare / Pharma

Pharma companies combine two distinct business models: a manufacturing
business (producing and selling drugs) and an R&D pipeline (future
optionality). The pipeline value is not on the balance sheet.

**Why these metrics:**

Revenue CAGR captures both marketed drug growth and new product
launches. ROIC is the right quality metric because pharma is a
capital-allocation business (R&D spending, M&A). EV/EBIT is standard
for cheapness. Pipeline value requires separate analysis.

**Growth metric: Revenue CAGR**

Same as industrial. Watch for patent cliff risk: revenue concentration
in drugs with patents expiring within 3 years. A company growing 10%
overall but whose top 3 drugs (60% of revenue) lose patent protection
in 2 years is not a growth story.

**Quality metric: ROIC**

Same as industrial. Pharma ROIC should be adjusted for R&D
capitalization (R&D is an investment in future revenue, not a current
period expense in economic terms):

```
Adjusted ROIC = (EBIT + R&D Expense) * (1 - Tax Rate) /
                (Total Debt + Equity - Cash + Capitalized R&D Asset)
```

| ROIC (adjusted, 5yr) | Quality Signal |
|:--|:--|
| >30% | Exceptional pipeline productivity |
| 20-30% | Strong |
| 12-20% | Adequate |
| <12% | Poor returns on R&D investment |

**Pipeline quality overlay:** A qualitative score based on:
- Number of Phase 3 candidates / Market Cap (higher = more pipeline
  optionality per dollar)
- Recent FDA approval success rate
- Patent cliff exposure (% of revenue losing protection in 5 years)

**Cheapness metric: EV/EBIT**

Same as industrial. Pharma typically trades at 10-18x EV/EBIT depending
on pipeline quality and patent cliff proximity.

**Stage 2 thresholds (pharma):**
- Revenue CAGR >= 5% (adjust for patent cliff)
- ROIC >= 15%
- Patent cliff exposure < 40% of revenue (within 5 years)

**What NOT to use:** P/E without adjusting for one-time charges,
ignoring the patent cliff, valuing purely on current products.

### Utilities

Regulated utilities are the closest thing equities offer to bonds. They
have guaranteed returns (regulated ROE), stable demand, and high
dividends. Growth is limited by regulation.

**Growth metric: Regulated Asset Base Growth**

```
RAB Growth = (Current RAB / Prior RAB) - 1
```

RAB (or "rate base") is the value of assets on which the utility is
allowed to earn a return. RAB growth comes from capital investment
approved by regulators.

**Quality metric: Allowed vs Earned ROE**

```
ROE Spread = Earned ROE - Allowed ROE
```

If earned ROE > allowed ROE, management is outperforming regulatory
expectations. If earned < allowed, the utility is under-earning
(operational issues or unfavorable rate cases).

| ROE Spread | Quality Signal |
|:--|:--|
| >+2% | Exceptional operational efficiency |
| 0 to +2% | Meeting or slightly exceeding allowed returns |
| -2 to 0% | Slight underperformance |
| <-2% | Operational problems or unfavorable regulation |

**Cheapness metric: P/B or Dividend Yield**

Utilities typically trade at 1.0-2.5x P/B. A P/B below 1.2x may
indicate regulatory risk or stranded asset risk. Dividend yield is
the primary return driver -- compare to risk-free rate:

| Dividend Yield vs 10yr Treasury | Signal |
|:--|:--|
| Yield > Treasury + 2% | Attractive (rare in low-rate environments) |
| Yield > Treasury + 1% | Reasonable |
| Yield ~ Treasury | Fully valued |
| Yield < Treasury | Overvalued unless growth compensates |

**Stage 2 thresholds (utilities):**
- RAB Growth >= 3%
- Earned ROE >= Allowed ROE

## Screening Implementation Guide

### Sector Classification

Before applying any metric, classify the company into the correct
sector. The pipeline should use a mapping from standard industry
classifications (GICS, ICB, or NAICS) to the pipeline sector buckets.

**Classification rules of thumb:**

| If the company... | Classify as... |
|:--|:--|
| Takes deposits and makes loans | Banks |
| Underwrites insurance policies | Insurance |
| Owns and operates income-producing real estate, pays 90%+ of income as dividends | REITs |
| Sells subscription software with >70% gross margins | SaaS |
| Extracts and sells commodities (oil, gas, metals, mining) | Energy/Materials |
| Develops and sells patented drugs | Pharma |
| Operates a regulated monopoly (electricity, gas, water) | Utilities |
| Everything else | Industrial/Consumer (default) |

### Metric Calculation Order

1. Calculate the growth metric and rank within sector
2. Calculate the quality metric and rank within sector
3. Calculate the cheapness metric and rank within sector
4. Compute composite: 0.25 * growth_rank + 0.25 * quality_rank + 0.50 * cheapness_rank
5. Sort ascending

Owner earnings normalization (Link G2) is applied to the cheapness
calculation for ALL sectors that use an earnings-based metric:

```
Owner Earnings = Net Income + Depreciation - Maintenance CapEx
Maintenance CapEx = (5yr Avg CapEx/Depreciation Ratio) * Current Depreciation
```

This replaces raw earnings/FCF/EBIT in the cheapness calculation. It
particularly matters for asset-heavy companies (industrials, energy)
where the gap between owner earnings and reported earnings can be
substantial.

### Data Quality Checks by Sector

| Sector | Critical Data Checks |
|:--|:--|
| Banks | Verify regulatory capital ratios from regulatory filings, not just 10-K |
| Insurance | Combined ratio should reconcile across GAAP and statutory filings |
| REITs | FFO should be calculated, not taken from company press release (companies sometimes adjust FFO to their advantage) |
| Energy | Use SEC-standardized reserve reports (PV-10), not company estimates |
| SaaS | Gross margin must be calculated from GAAP COGS, not "adjusted" COGS |
| Pharma | Separate product revenue from collaboration/royalty revenue |

### The Golden Rules

1. **Never compare multiples across sectors.** A bank at 10x P/E and
   a SaaS company at 10x P/E are not equally cheap. They are
   fundamentally different businesses with different earnings quality.

2. **Never use EV/EBITDA for banks or insurers.** Interest is their
   cost of goods sold. Stripping it out removes the business.

3. **Never value a cyclical at current earnings.** Use cycle-normalized
   earnings (5-10 year average). The stock that looks cheapest on
   current P/E is often the most expensive on normalized earnings.

4. **Never use P/E for early-stage SaaS or biotech.** If there are no
   earnings, the P/E is undefined (or negative). Use revenue-based or
   pipeline-based approaches.

5. **Never trust reported FFO without checking the calculation.** Some
   REITs add back items beyond standard NAREIT FFO definition.
   Calculate your own.

6. **Owner earnings over reported earnings, always.** The gap between
   what a company reports and what it actually earns for owners is
   the difference between a screening result and a value trap.

## Sources

1. Fair Price Index. "Why Sector Determines How You Should Value a
   Stock." July 2026.
   https://www.fairpriceindex.com/education/sector-specific-valuation

2. Corporate Finance Institute. "The SaaS Rule of 40 Explained."
   October 2024.
   https://corporatefinanceinstitute.com/resources/valuation/rule-of-40/

3. Aventis Advisors. "Rule of 40 in SaaS: 2026 Data, Benchmarks and
   Valuation." May 2026.
   https://aventis-advisors.com/rule-of-40-in-saas-2026/

4. Damodaran, Aswath. "Damodaran on Valuation." 2nd Edition. Wiley,
   2006. (Sector-specific cost of capital and multiples)

5. Greenwald, Bruce. "Value Investing: From Graham to Buffett and
   Beyond." Wiley, 2001. (EPV and sector-appropriate methodology)

6. NAREIT. "Funds From Operations (FFO) -- A Standardized Measure
   for REIT Performance." https://www.nareit.com

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- Stages 1-2 specification
- `investing/frameworks/dcf-intrinsic-value.md` -- sector-specific DCF methods
- `library/value-investing/anchor-value-investing.md` -- domain anchor
