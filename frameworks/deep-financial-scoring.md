---
name: deep-financial-scoring
id: 20260726T210500Z
tier: framework
domain: value-investing
author: Ava
tags: [financial-health, earnings-quality, red-flags, FCF, debt-analysis, ROIIC, forensic-accounting, Beneish-M-Score, Altman-Z-Score]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/simple-management-scoring.md
  - library/value-investing/anchor-value-investing.md
---

# Deep Financial Scoring -- Financial Health & Red Flag Analysis (Stage 4B)

This framework explains how to perform the full financial health
analysis from Stage 4B of the investment pipeline. While the simple
scoring frameworks assess moat and management quality, Stage 4B
answers a different question: **"Are the reported numbers trustworthy,
and can this company survive a crisis?"**

A company can have a wide moat and exceptional management but still
destroy shareholder value through excessive leverage, aggressive
accounting, or deteriorating financial health. This analysis catches
what moat and management scoring miss.

## The Five Components of Financial Health Analysis

### Component 1: Normalized Earnings

**Goal:** Determine what the company ACTUALLY earns, stripping out
one-time items, cyclical effects, and accounting choices that inflate
or deflate reported earnings.

Reported earnings are an accounting construct. Normalized earnings are
an economic reality. The gap between them is the "quality of earnings"
question.

#### 1A. Earnings Normalization Adjustments

For each of the last 5 years, adjust reported net income for:

| Adjustment Category | What to Look For | Adjustment Direction |
|:--|:--|:--|
| Non-recurring gains/losses | Asset sales, litigation settlements, insurance recoveries | Remove entirely |
| Restructuring charges | "One-time" charges that appear repeatedly | If recurring, treat as operating expense |
| Goodwill impairment | Non-cash write-downs of past acquisitions | Remove (but note as red flag) |
| Gains/losses from investments | Mark-to-market changes, sale of securities | Remove for operating earnings |
| Discontinued operations | Earnings from sold/closed business units | Remove entirely |
| Changes in accounting estimates | Depreciation method changes, reserve changes | Flag; assess if aggressive |
| Stock-based compensation | Often added back in "adjusted" earnings | Do NOT add back. SBC is a real cost. |
| Currency gains/losses | FX translation effects | Remove for operating earnings |
| Tax rate anomalies | One-time tax benefits or charges | Normalize to effective rate |

**The SBC rule:** Many companies present "adjusted" earnings that add
back stock-based compensation. This is misleading. SBC is a real
economic cost -- it transfers value from shareholders to employees.
Never add back SBC when normalizing earnings. If a company's GAAP
earnings are substantially below "adjusted" earnings primarily due to
SBC, the company is more expensive than it appears.

#### 1B. Cyclical Normalization

For cyclical businesses (commodities, industrials, energy, materials),
normalize earnings across the full cycle:

```
Normalized EBIT = Average EBIT margin over full cycle * Current Revenue
```

The "full cycle" should span at least 7-10 years, covering both peak
and trough. A company at a cyclical peak will show unsustainably high
margins. A company at a trough will show unsustainably low margins.
Neither is the right basis for valuation.

**Check:** Is the company currently at peak margins or trough margins?
If operating margins are at 10-year highs, normalize DOWN. If at
10-year lows, normalize UP. Valuing a cyclical at peak earnings is the
most common value trap.

#### 1C. Normalized Earnings Output

Produce a table:

| Year | Reported NI | Adjustments | Normalized NI | Normalized EPS |
|:--|--:|--:|--:|--:|
| Y-4 | $X | +/- $Y | $Z | $Z/Shares |
| Y-3 | ... | ... | ... | ... |
| Y-2 | ... | ... | ... | ... |
| Y-1 | ... | ... | ... | ... |
| Current | ... | ... | ... | ... |

The 3-5 year average of normalized EPS is the basis for earnings-based
valuation (P/E normalization, EPV calculation). The variance tells you
how stable earnings are -- high variance = less predictable = wider
margin of safety required.

**Evidence required:**
- Income statement for 5 years (10-K filings)
- Notes to financial statements (restructuring, impairments, unusual items)
- Management discussion of non-recurring items
- Industry cycle data (for cyclical normalization)

### Component 2: Free Cash Flow Conversion Quality

**Goal:** Determine whether reported earnings translate into actual
cash available to shareholders.

Earnings can be manipulated through accounting choices. Cash flow
cannot. If a company reports growing earnings but declining free cash
flow, something is wrong.

#### 2A. The Core Ratios

**Ratio 1: Operating Cash Flow / Net Income (OCF/NI)**

```
OCF/NI = Cash from Operations / Net Income
```

| OCF/NI Ratio | Signal |
|:--|:--|
| >1.2x | Strong cash conversion. Earnings are conservative. |
| 1.0x - 1.2x | Healthy. Earnings are cash-backed. |
| 0.8x - 1.0x | Moderate concern. Some earnings may be accrual-based. Check why. |
| 0.5x - 0.8x | Significant concern. Large gap between reported and cash earnings. |
| <0.5x | CRITICAL RED FLAG. Earnings are substantially non-cash. Investigate immediately. |

Calculate for each of the last 5 years. A declining trend (OCF/NI ratio
falling from 1.2 to 0.7 over 5 years) is a red flag even if current
ratio is above 0.8.

**Ratio 2: Free Cash Flow / Net Income (FCF/NI)**

```
FCF = Operating Cash Flow - Maintenance CapEx
FCF/NI = FCF / Net Income
```

Where maintenance CapEx is estimated as depreciation (or, for
conservatism, use total CapEx).

| FCF/NI Ratio | Signal |
|:--|:--|
| >0.8x | Healthy. The business generates real cash after sustaining itself. |
| 0.5x - 0.8x | Moderate. Heavy reinvestment or earnings quality issue. |
| 0.2x - 0.5x | Concerning. Most earnings are consumed by CapEx or are non-cash. |
| <0.2x | RED FLAG. The business consumes cash despite reporting profits. |

**Ratio 3: FCF Consistency**

Count how many of the last 8 quarters (or 5 years for annual data) were
FCF-positive.

| FCF-positive periods | Signal |
|:--|:--|
| 8/8 quarters or 5/5 years | Excellent consistency |
| 6-7/8 quarters or 4/5 years | Generally reliable |
| 4-5/8 quarters or 3/5 years | Inconsistent. Cyclical or poor conversion. |
| <4/8 quarters or <3/5 years | CRITICAL RED FLAG. Business cannot sustain cash generation. |

#### 2B. The Accruals Test

High accruals relative to cash earnings are a leading indicator of
earnings manipulation. The simple accruals ratio:

```
Accruals = (Net Income - Operating Cash Flow) / Total Assets
```

| Accruals Ratio | Signal |
|:--|:--|
| <5% | Conservative accounting. Earnings are cash-backed. |
| 5-10% | Normal range. |
| 10-15% | Above normal. Watch for trend. |
| >15% | RED FLAG. High probability of aggressive accounting or manipulation. |

**The accruals anomaly (Sloan, 1996):** Companies with high accruals
(large gap between earnings and cash flow) tend to underperform
companies with low accruals. The market systematically overvalues
accrual-heavy earnings. This is one of the most robust findings in
accounting research.

#### 2C. Cash Conversion Cycle

```
CCC = DSO + DIO - DPO

Where:
  DSO = Accounts Receivable / Revenue * 365
  DIO = Inventory / COGS * 365
  DPO = Accounts Payable / COGS * 365
```

Track the CCC over 5 years. A deteriorating CCC (rising DSO, rising
inventory days, falling payables days) means the company is tying up
more cash in operations. This consumes FCF even if earnings grow.

**Warning patterns:**
- DSO rising 10%+ without corresponding revenue growth (aggressive
  revenue recognition or deteriorating customer quality)
- Inventory days rising 20%+ (obsolescence risk or channel stuffing)
- DPO falling (suppliers demanding faster payment = they see risk)

**Evidence required:**
- Cash flow statements (5 years)
- Balance sheets for working capital components (5 years)
- Notes on depreciation, CapEx by category

### Component 3: Debt Structure Analysis

**Goal:** Determine whether the company's debt load and structure create
financial vulnerability, regardless of business quality.

A wonderful business with a terrible balance sheet is not wonderful.
Debt amplifies returns in good times and destroys equity in bad times.
A company that cannot survive a recession does not deserve a DCF
valuation -- it deserves a survival probability.

#### 3A. Leverage Ratios

| Ratio | Formula | Safe | Caution | Danger |
|:--|:--|:--|:--|:--|
| Debt/Equity | Total Debt / Shareholders' Equity | <0.5x | 0.5-1.5x | >1.5x |
| Debt/EBITDA | Total Debt / EBITDA | <2.0x | 2.0-4.0x | >4.0x |
| Net Debt/EBITDA | (Total Debt - Cash) / EBITDA | <1.5x | 1.5-3.0x | >3.0x |
| Interest Coverage | EBIT / Interest Expense | >8x | 3-8x | <3x |
| Debt/FCF | Total Debt / FCF | <5x | 5-10x | >10x |
| Current Ratio | Current Assets / Current Liabilities | >1.5x | 1.0-1.5x | <1.0x |

**The Debt/FCF ratio is the most important for value investors.**
It answers: "If the company devoted 100% of FCF to debt repayment,
how many years would it take?" A ratio above 10x means a decade of
full debt service -- any disruption to cash flow is catastrophic.

**NMC Health case study:** Before its collapse in 2020, NMC Health
reported debt/equity of 1.5x in 2018 -- within the "caution" zone.
However, $4 billion of undisclosed debt was later uncovered, pushing
the actual ratio to 4.86x. Debt/FCF went from 9x to 29x. The lesson:
reported leverage ratios are only as good as the reported debt figure.
Always check for off-balance-sheet items.

#### 3B. Debt Maturity Ladder

Map out when debt matures:

```
Year      Debt Maturing    % of Total    FCF Available    Coverage
2026      $200M           15%           $300M            1.5x
2027      $150M           11%           $300M            2.0x
2028      $500M           38%           $300M            0.6x <-- REFINANCE RISK
2029      $100M            8%           $300M            3.0x
2030+     $370M           28%           $300M            N/A
```

**Red flags in the maturity ladder:**
- Any single year where maturing debt > FCF (the company MUST refinance
  or raise capital -- it has no choice)
- Heavy concentration in one year (refinancing risk if credit markets
  are tight)
- Balloon maturity (large principal due at end, typical of leveraged
  loans)
- Most debt maturing within 2 years with uncertain refinancing capacity

#### 3C. Debt Structure Quality

| Factor | Favorable | Unfavorable |
|:--|:--|:--|
| Fixed vs floating | >70% fixed rate | >50% floating (rate hike vulnerability) |
| Currency match | Debt in same currency as revenue | Mismatched (FX risk doubles leverage risk) |
| Covenant headroom | Wide headroom (>30% buffer) | Tight covenants (risk of technical default) |
| Secured vs unsecured | Unsecured (flexibility) | Fully secured (assets encumbered, less flexibility) |
| Lender concentration | Diversified lenders, public bonds | Single bank or concentrated lenders |

#### 3D. Altman Z-Score (Financial Distress Test)

The Altman Z-Score predicts bankruptcy probability using five weighted
financial ratios. For public manufacturing companies:

```
Z = 1.2(X1) + 1.4(X2) + 3.3(X3) + 0.6(X4) + 0.99(X5)

Where:
  X1 = Working Capital / Total Assets
  X2 = Retained Earnings / Total Assets
  X3 = EBIT / Total Assets
  X4 = Market Cap / Total Liabilities
  X5 = Sales / Total Assets
```

| Z-Score | Zone | Interpretation |
|:--|:--|:--|
| >2.99 | Safe | Low probability of bankruptcy within 2 years |
| 1.81 - 2.99 | Grey | Moderate risk; monitor closely |
| <1.81 | Distress | High probability of bankruptcy within 2 years |

The model predicts bankruptcy with 72-80% accuracy up to 2 years before
the event. It is not perfect -- NMC Health had a Z-score of 2.93 in
2018 before its collapse (misleading because debt was hidden). But a
Z-score below 1.81 is a strong signal to DISCARD or demand an extremely
wide margin of safety.

**Tracking the trend is more important than the absolute score.** A
Z-score declining from 3.5 to 2.1 over 3 years is a warning signal even
if technically still in the "grey" zone. A stable Z-score above 3.0
for 5+ years supports the thesis that financial health is durable.

**Evidence required:**
- Balance sheet (5 years of total debt, equity, current assets/liabilities)
- Debt maturity schedule (10-K notes on debt)
- Income statement for interest expense and EBIT
- Credit rating (if available)
- Covenant details (10-K or credit agreement filings)

### Component 4: Return on Incremental Invested Capital (ROIIC)

**Goal:** Determine whether management's recent capital allocation
decisions are earning adequate returns.

ROIC tells you what the company has earned historically. ROIIC tells
you what management is earning on the NEW capital they are deploying
RIGHT NOW. A company with a 25% ROIC but a 5% ROIIC is coasting on
past investments while destroying value on new ones.

#### 4A. ROIIC Calculation

```
ROIIC = (NOPAT_Year2 - NOPAT_Year1) / (Invested Capital_Year1 - Invested Capital_Year0)

Where:
  NOPAT = EBIT * (1 - Effective Tax Rate)
  Invested Capital = Total Debt + Shareholders' Equity - Cash
```

Use a 3-5 year lookback to smooth annual volatility:

```
3-Year ROIIC = (NOPAT_Current - NOPAT_3YearsAgo) /
               (Invested Capital_3YearsAgo - Invested Capital_4YearsAgo)
               [averaged across each annual increment]
```

**Microsoft example (FY2019-FY2022):** NOPAT grew from $34.6B to
$70.1B (+$35.5B). Invested capital grew from $70.9B to $120.2B
(+$49.3B). ROIIC = $35.5B / $49.3B = 72.1%. Every dollar of new
capital generated $0.72 in incremental after-tax profit. Exceptional.

#### 4B. ROIIC Interpretation

| ROIIC | Signal | Implication |
|:--|:--|:--|
| >30% | Exceptional | Management creates enormous value on every dollar deployed. High-return reinvestment opportunities exist. |
| 15-30% | Strong | Healthy reinvestment returns. Good capital allocation. |
| 8-15% | Adequate | Covers cost of capital but no significant value creation on new investment. |
| 0-8% | Poor | Barely covers or doesn't cover cost of capital. New investment is value-neutral or destructive. |
| <0% | Value-destroying | Negative returns on new capital. Management should return all cash to shareholders, not reinvest. |

#### 4C. The ROIIC Trend

More important than the absolute level is the direction:

- **Rising ROIIC:** The company is finding better reinvestment
  opportunities. Moat may be strengthening. Growth creates value.
- **Stable ROIIC:** Steady-state business. Growth is neither creating
  nor destroying exceptional value.
- **Falling ROIIC:** The company is running out of high-return
  reinvestment opportunities but deploying capital anyway. This is
  the early warning sign of a growth-at-any-cost mindset that
  eventually destroys value.
- **ROIIC falling below WACC:** The company should stop reinvesting
  and return capital to shareholders. If it continues reinvesting,
  management is either incompetent or empire-building.

**Evidence required:**
- NOPAT calculation for 5 years (EBIT * (1-tax rate))
- Invested capital for 5 years
- Segment data if company has multiple business units with different
  reinvestment profiles

### Component 5: Structured Red Flag Scan

**Goal:** Systematically check for warning signs across five
categories. A single red flag is a warning. Multiple red flags in the
same category or across categories is a potential dealbreaker.

#### 5A. Earnings Quality Red Flags

| Red Flag | How to Detect | Severity |
|:--|:--|:--|
| Growing DSO | DSO rising 20%+ in 2 years without revenue mix change | HIGH |
| DSI divergence | Inventory days rising while revenue grows (channel stuffing risk) | HIGH |
| Aggressive revenue recognition | Revenue growth far exceeds industry + cash collection lagging | CRITICAL |
| Serial "one-time" charges | Restructuring/impairment charges in 3+ of last 5 years | HIGH |
| GAAP vs non-GAAP gap | "Adjusted" earnings >30% higher than GAAP for 3+ years | CRITICAL |
| Deferred revenue decline | Deferred revenue falling while reported revenue rises | HIGH |
| Capitalizing expenses | Suddenly capitalizing costs previously expensed | CRITICAL |
| Change in depreciation method | Lengthening useful lives to boost earnings | HIGH |
| Premature revenue recognition | Revenue booked before delivery/acceptance | CRITICAL |
| Cookie jar reserves | Large reserve releases boosting earnings in weak quarters | MEDIUM |

#### 5B. Balance Sheet Red Flags

| Red Flag | How to Detect | Severity |
|:--|:--|:--|
| Goodwill >50% of assets | Goodwill / Total Assets > 50% | HIGH |
| Goodwill impairment pattern | Impairment in 2+ of last 5 years | HIGH |
| Off-balance-sheet items | Operating leases, SPVs, guarantees (check footnotes) | CRITICAL |
| Pension underfunding | Projected benefit obligation > plan assets by 30%+ | HIGH |
| Hidden debt | Unconsolidated entities, factoring receivables, take-or-pay contracts | CRITICAL |
| Intangible-heavy balance sheet | Intangibles + Goodwill > 70% of assets | MEDIUM |
| Negative tangible book value | Shareholders' Equity - Goodwill - Intangibles < 0 | HIGH |
| Rising debt while cash hoard grows | Taking on debt while sitting on cash (why?) | MEDIUM |
| Deferred tax assets > equity | DTA / Equity > 50% (may never be realized) | HIGH |

#### 5C. Cash Flow Red Flags

| Red Flag | How to Detect | Severity |
|:--|:--|:--|
| Persistent earnings-FCF gap | FCF < 50% of Net Income for 3+ years | CRITICAL |
| FCF declining while earnings grow | Divergence over 2+ years | CRITICAL |
| Operating cash flow boosted by working capital | OCF growth driven by stretching payables, not operations | HIGH |
| CapEx < Depreciation for 3+ years | Underinvesting to boost FCF (value extraction, not moat widening) | HIGH |
| Dividends > FCF | Paying dividends with debt or asset sales | CRITICAL |
| Sale-leaseback transactions | Selling assets and leasing them back to generate cash | HIGH |

#### 5D. Governance Red Flags

| Red Flag | How to Detect | Severity |
|:--|:--|:--|
| Related-party transactions | 10-K footnotes (Related Party Transactions section) | CRITICAL |
| Frequent auditor changes | New auditor every 2-3 years | CRITICAL |
| Dual-class shares with poor alignment | Super-voting shares held by insiders with low economic ownership | HIGH |
| Auditor resignation (not dismissal) | Auditor quit rather than being fired | CRITICAL |
| Late filings | 10-K/10-Q filed after deadline | HIGH |
| SEC investigation or comment letters | EDGAR correspondence search | CRITICAL |
| Board dominated by insiders | >50% of board not independent | HIGH |
| Auditor is not Big 4 | Smaller auditors have higher failure rates | MEDIUM |

#### 5E. Munger Psychology Flags (from Link)

| Red Flag | How to Detect | Severity |
|:--|:--|:--|
| Promotional management language | "Revolutionary," "transformative," "game-changing" in official communications | MEDIUM |
| Excessive M&A ("empire building") | >1 major acquisition per year for 3+ years | HIGH |
| Serial restructuring charges | "One-time" charges in 3+ consecutive years | HIGH |
| Blame-shifting | "Macro headwinds" as explanation for every miss while taking credit for every beat | MEDIUM |
| Obsession with stock price | Frequent commentary on stock price in earnings calls | MEDIUM |
| Earnings guidance obsession | Lowballing then "beating" quarter after quarter | HIGH |
| Grandiose long-term projections | Revenue targets for 5+ years out with no credible path | MEDIUM |

#### 5F. Beneish M-Score (Earnings Manipulation Test)

The Beneish M-Score is a statistical model that detects earnings
manipulation using 8 financial ratios. It was developed by Professor
Messod Beneish and is considered the best available model for detecting
earnings manipulators.

The 8 variables:

1. **DSRI (Days Sales in Receivables Index):** Receivables/Revenue
   this year vs last year. Rising = accelerated revenue recognition.
2. **GMI (Gross Margin Index):** Last year's gross margin / this
   year's. >1 = deteriorating margins (motivation to manipulate).
3. **AQI (Asset Quality Index):** Non-current assets (excl. PPE) /
   Total Assets, this year vs last. Rising = cost deferral.
4. **SGI (Sales Growth Index):** Revenue this year / last year. High
   growth companies have more incentive to manipulate.
5. **DEPI (Depreciation Index):** Last year's depreciation rate /
   this year's. >1 = slowing depreciation (boosting earnings).
6. **SGAI (SG&A Index):** SG&A/Revenue this year vs last year.
7. **LVGI (Leverage Index):** Debt/Assets this year vs last year.
   Rising = motivation to manipulate to avoid covenant breaches.
8. **TATA (Total Accruals to Total Assets):** Accruals / Total Assets.
   High accruals = earnings not backed by cash.

The M-Score formula combines these with specific coefficients:

```
M-Score = -4.84 + 0.920*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI
          + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI
```

| M-Score | Interpretation |
|:--|:--|
| <-2.22 | Unlikely to be a manipulator |
| -2.22 to -1.78 | Possible manipulator (grey zone) |
| >-1.78 | Likely manipulator |

**Practical note:** The full 8-variable Beneish model requires detailed
financial statement data including depreciation rates, asset mix, and
accrual calculations. For the pipeline, use a simplified 5-variable
version focusing on DSRI, GMI, AQI, SGI, and TATA -- the variables
with the highest predictive power. If any two of these five are at
manipulation levels, flag as HIGH concern.

**Evidence required:**
- All red flag categories checked against 10-K filings
- Specific footnote/page references for each flag found
- Beneish M-Score calculation (or simplified version) for 2 years

## Synthesis: The Financial Health Report

### 1. Financial Health Summary (1 paragraph)

Is this company financially healthy? Can it survive a 2-year recession
without raising capital? Are reported earnings trustworthy?

### 2. Earnings Quality Assessment

- Normalized EPS (3-5 year average) vs reported EPS
- Key normalization adjustments (list the 3 largest)
- OCF/NI ratio trend (table, 5 years)
- FCF/NI ratio trend (table, 5 years)
- Accruals test result
- **Verdict: Earnings quality is [HIGH / MODERATE / LOW / CRITICAL CONCERN]**

### 3. Cash Flow Health

- FCF consistency score
- Cash conversion cycle trend
- FCF yield (FCF / Market Cap)
- **Verdict: Cash flow generation is [STRONG / ADEQUATE / WEAK / CONCERNING]**

### 4. Balance Sheet Strength

- Key leverage ratios table
- Debt maturity ladder
- Altman Z-Score
- Off-balance-sheet items found
- **Verdict: Balance sheet is [STRONG / ADEQUATE / LEVERAGED / DANGEROUS]**

### 5. Capital Allocation Efficiency

- ROIIC (3-year)
- ROIIC trend (rising/stable/falling)
- ROIC-WACC spread (link to moat analysis)
- **Verdict: Reinvestment returns are [EXCEPTIONAL / STRONG / ADEQUATE / POOR / VALUE-DESTROYING]**

### 6. Red Flag Inventory

- Total red flags found: X (HIGH: Y, CRITICAL: Z)
- Top 3 most concerning red flags with evidence
- Beneish M-Score result
- **Verdict: [CLEAN / MINOR CONCERNS / SIGNIFICANT CONCERNS / DEALBREAKER]**

### 7. Financial Health Score (1-10)

| Score | Classification | Pipeline Implication |
|:--|:--|:--|
| 8-10 | Excellent | Proceed with standard analysis |
| 6-7 | Good | Proceed, note specific concerns in thesis risks |
| 4-5 | Adequate | Proceed with caution; wider MOS required |
| 2-3 | Weak | Conditional -- only proceed if moat is WIDE and leverage is the ONLY concern |
| 1 | Critical | DISCARD. The numbers are not trustworthy or the company cannot survive a recession. |

### 8. Key Monitoring Triggers

- Leverage ratio thresholds to watch
- Refinancing dates
- Earnings release events to scrutinize
- Specific red flags to re-check at each filing

## Common Mistakes in Financial Health Analysis

1. **Trusting reported earnings.** Always normalize. "Adjusted EBITDA"
   is a marketing metric, not an earnings figure. Start with GAAP net
   income and make your own adjustments.

2. **Ignoring off-balance-sheet items.** Operating leases, pension
   obligations, and factoring arrangements are real liabilities that
   do not appear in the debt total. Read the footnotes.

3. **Valuing cyclicals at peak earnings.** If margins are at 10-year
   highs, the company is not as cheap as it appears. Normalize across
   the cycle.

4. **Missing the SBC dilution.** Companies that add back stock-based
   compensation to "adjusted" earnings are misleading you. SBC is a
   real cost. A company trading at 15x "adjusted" earnings may trade
   at 25x when SBC is properly expensed.

5. **Stopping at leverage ratios.** Debt/EBITDA < 3x does not mean
   "safe." Check the maturity ladder. A company with low total leverage
   but a $500M maturity in 12 months with $50M FCF is in trouble.

6. **Ignoring the ROIIC trend.** A high historical ROIC masks the fact
   that new capital is being deployed at low returns. ROIIC tells you
   whether growth creates or destroys value.

7. **Assuming the Z-Score is definitive.** The Z-score is a screening
   tool, not a verdict. A company with a Z-score of 3.5 can still
   fail. A company with a Z-score of 1.7 can survive. Use it as one
   input among many.

8. **Red flag overload.** Finding one red flag is not a dealbreaker.
   Finding four in the same category or red flags across earnings,
   balance sheet, AND cash flow categories simultaneously IS a
   dealbreaker. The pattern matters more than any single flag.

## Sources

1. Beneish, Messod D. "The Detection of Earnings Manipulation."
   Financial Analysts Journal, 1999.

2. Altman, Edward I. "Financial Ratios, Discriminant Analysis and
   the Prediction of Corporate Bankruptcy." Journal of Finance, 1968.

3. CFA Institute. "Quality of Earnings: A Critical Lens for Financial
   Analysts." Enterprising Investor, March 2025.
   https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/quality-of-earnings-a-critical-lens-for-financial-analysts

4. Wall Street Prep. "Return on Incremental Invested Capital (ROIIC)."
   February 2024.
   https://www.wallstreetprep.com/knowledge/incremental-return-on-invested-capital-roiic

5. Sloan, Richard G. "Do Stock Prices Fully Reflect Information in
   Accruals and Cash Flows About Future Earnings?" The Accounting
   Review, 1996.

6. GMT Research. "Beneish's M-Score."
   https://www.gmtresearch.com/en/accounting-ratio/beneishs-m-score

7. MetricDuck. "Earnings Quality Analysis Hub." December 2025.
   https://www.metricduck.com/blog/earnings-quality-analysis

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- Stage 4B specification
- `investing/frameworks/simple-management-scoring.md` -- Stage 3C management triage
- `investing/frameworks/deep-moat-scoring.md` -- Stage 4A competitive dynamics (companion deep dive)
