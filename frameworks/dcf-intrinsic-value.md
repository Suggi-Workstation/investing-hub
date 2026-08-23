---
name: dcf-intrinsic-value
id: 20260726T211500Z
tier: framework
domain: value-investing
author: Ava
tags: [dcf, valuation, intrinsic-value, EPV, margin-of-safety, bull-bear-scenarios, wacc, terminal-value, sensitivity]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/deep-financial-scoring.md
  - investing/frameworks/deep-moat-scoring.md
  - library/value-investing/margin-of-safety.md
  - library/value-investing/intrinsic-value-estimation-methods.md
---

# DCF Intrinsic Value -- Valuation Framework with Bull/Base/Bear Cases (Stage 7A)

This framework explains how to build a discounted cash flow (DCF)
model with bull, base, and bear scenarios, cross-check it against EPV
and multiples, and arrive at a defensible intrinsic value proposition.
It implements Stage 7A of the investment pipeline.

## Philosophy: Why DCF, and Why With Scenarios

A DCF model values a business as the present value of all future free
cash flows it will generate. This is the most theoretically grounded
approach to equity valuation. But DCF is only as good as its inputs.
Small changes in growth or discount rate assumptions can swing the
output by 50% or more.

A single-point DCF produces false precision. A DCF with bull/base/bear
scenarios acknowledges uncertainty while remaining actionable. The
goal is not to find THE exact intrinsic value -- it is to find a RANGE
of plausible intrinsic values and determine whether the current market
price offers a sufficient margin of safety even under pessimistic
assumptions.

## Prerequisites: What You Need Before Starting

The DCF model should be the LAST analytical step, not the first. Before
building it, you should have completed:

- **Stage 3B (Simple Moat Scoring):** Moat quality determines how long
  excess returns persist (terminal value assumptions)
- **Stage 4A (Deep Moat Analysis):** Competitive position determines
  margin sustainability and growth trajectory
- **Stage 4B (Financial Health):** Normalized earnings and FCF quality
  are the raw inputs for the DCF
- **Stage 6 (Investment Thesis):** Growth assumptions should flow from
  the thesis pillars, not from spreadsheet extrapolation

Data required:
- 5 years of historical financials (income statement, balance sheet,
  cash flow statement)
- Current market price and shares outstanding
- Risk-free rate (10-year government bond yield)
- Company-specific beta or reasonable estimate

## Part 1: The Two-Stage DCF Model

### Stage 1: Explicit Forecast Period (Years 1-5)

Project free cash flow for each of the next 5 years, then discount
each year back to present value.

```
FCF = EBIT * (1 - Tax Rate) + Depreciation - CapEx - Change in Working Capital

PV of Explicit Period = Sum of [FCF_YearN / (1 + WACC)^N] for N = 1 to 5
```

**Revenue growth path:**

The revenue growth rate for each year should be grounded in the
investment thesis, not extrapolated from history. A company that grew
25% for the last 5 years may grow 12%, 10%, 8%, 7%, 6% over the next
5 as it matures. The growth path should DECLINE toward a sustainable
rate -- no company grows 20% forever.

| Year | Growth Rate | Rationale |
|:--|:--|:--|
| 1 | 12% | Thesis pillar: product Y gaining share in growing market Z |
| 2 | 10% | Continued share gains, slightly moderating |
| 3 | 8% | Market approaching maturity, comps getting harder |
| 4 | 7% | Growth converging toward industry rate |
| 5 | 6% | Approaching terminal growth rate |

**Margin path:**

Margins should reflect competitive dynamics from Stage 4A:
- Widening moat: margins can expand modestly
- Stable moat: margins hold at normalized levels
- Narrowing moat: margins should contract toward industry average

Do NOT project margins above historical peaks without extraordinary
evidence. The most common DCF error is projecting peak margins into
perpetuity.

**Reinvestment assumptions:**

- CapEx as % of revenue: use 5-year historical average, adjusted for
  any known changes in capital intensity
- Depreciation: should roughly track CapEx over time (if CapEx
  consistently exceeds depreciation, the business is growing its asset
  base; if depreciation exceeds CapEx, it is underinvesting)
- Working capital: use historical NWC/Revenue ratio

### Stage 2: Terminal Value

Terminal value captures all cash flows beyond the explicit forecast
period. It typically represents 60-80% of total intrinsic value --
which means terminal assumptions dominate the result. This is why the
moat quality from Stage 3B/4A is so critical: moat durability
determines how long and at what level terminal cash flows persist.

**Method 1: Gordon Growth Model (Perpetuity)**

```
Terminal Value = FCF_Year5 * (1 + g) / (WACC - g)

Where g = terminal (perpetual) growth rate
```

**Choosing the terminal growth rate (g):**

| Business Type | Typical g | Rationale |
|:--|:--|:--|
| Wide moat, growing industry | 3.0-4.0% | Can grow with GDP + modest pricing power |
| Narrow moat, mature industry | 2.0-3.0% | Grows roughly with nominal GDP |
| No moat, competitive industry | 1.0-2.0% | Struggles to maintain share |
| Declining industry | 0.0-1.0% | Growth at or below inflation |

**Critical rule:** g must be less than the long-term nominal GDP growth
rate of the company's primary market (typically 3-4% for developed
economies). A terminal growth rate above 4% implies the company will
eventually become larger than the entire economy. This is impossible.

**Method 2: Exit Multiple Cross-Check**

Convert the terminal value to an implied exit multiple:

```
Implied Exit EV/EBIT = Terminal Value / EBIT_Year5
```

This implied multiple should fall within the observable range for
mature businesses in the sector. If the Gordon Growth terminal value
implies a 30x EV/EBIT exit for a manufacturing business where comps
trade at 8-12x, the terminal growth rate is too aggressive.

**Cross-check table:**

| Terminal Growth (g) | Implied Exit EV/EBIT | Plausible? |
|:--|:--|:--|
| 4.0% | 18.2x | Only for premium compounders (wide moat, high ROIC) |
| 3.0% | 14.3x | Reasonable for above-average businesses |
| 2.5% | 12.9x | Reasonable for mature, stable businesses |
| 2.0% | 11.8x | Conservative baseline |
| 1.5% | 10.8x | For challenged or declining businesses |

### From Enterprise Value to Equity Value Per Share

```
Enterprise Value = PV of Explicit FCFs + PV of Terminal Value
Equity Value = Enterprise Value - Total Debt + Cash & Equivalents
Intrinsic Value Per Share = Equity Value / Diluted Shares Outstanding
```

Use diluted shares outstanding (including stock options, RSUs,
convertibles). Using basic shares understates dilution risk.

## Part 2: WACC Estimation

The Weighted Average Cost of Capital is the discount rate that reflects
the risk of the company's cash flows.

```
WACC = (E/V * Ke) + (D/V * Kd * (1 - t))

Where:
  E = Market value of equity
  D = Market value of debt
  V = E + D
  Ke = Cost of equity
  Kd = Cost of debt (pre-tax)
  t = Corporate tax rate
```

### Cost of Equity (CAPM)

```
Ke = Rf + Beta * ERP

Where:
  Rf = Risk-free rate (10-year government bond yield)
  Beta = Company's equity beta (measure of systematic risk)
  ERP = Equity Risk Premium (typically 4.5-5.5% for developed markets)
```

**Typical WACC ranges (mid-2026, with ~4.3% risk-free rate):**

| Business Type | WACC Range | Examples |
|:--|:--|:--|
| Stable, predictable, wide moat | 7-9% | KO, PG, WMT, waste management |
| Quality compounders | 8-10% | MSFT, V, MA, Costco |
| Average large cap | 9-11% | Most S&P 500 industrials |
| Cyclical or leveraged | 10-13% | Autos, airlines, energy |
| High uncertainty | 12-15%+ | Biotech, early-stage, distressed |

**Moat quality WACC adjustment:**

Companies with wide moats and predictable cash flows deserve lower
discount rates -- not because CAPM says so, but because their cash
flows are genuinely less risky. Apply a moat discount:

| Moat Score (Stage 3B) | WACC Adjustment |
|:--|:--|
| 4.0-5.0 (Wide) | -0.5% to -1.0% from CAPM-derived WACC |
| 3.0-3.9 (Narrow) | No adjustment |
| 2.0-2.9 (Weak) | +0.5% to +1.0% (higher uncertainty) |

**Cost of debt:**

Use the company's actual weighted average interest rate on outstanding
debt (total interest expense / total debt) or the yield on its bonds.
For companies with investment-grade credit ratings, use the current
yield on similarly-rated bonds of comparable maturity.

## Part 3: Bull / Base / Bear Scenario Construction

A single DCF is a single guess. Three scenarios provide a range that
acknowledges uncertainty. The key principle: use absolute
percentage-point shifts, not percentage-of-base haircuts. A 20%
haircut on a 5% growth rate (-1pp) is very different from a 20%
haircut on a 20% growth rate (-4pp). Absolute shifts ensure the spread
between scenarios is driven by genuine uncertainty, not the starting
level.

### Scenario Definitions

| Parameter | Bear Case | Base Case | Bull Case |
|:--|:--|:--|:--|
| Revenue growth (Years 1-3 avg) | Base - 2.0pp | Thesis-driven estimate | Base + 1.5pp |
| Revenue growth (Years 4-5 avg) | Base - 1.5pp | Converging to terminal | Base + 1.0pp |
| Operating margin (terminal) | Base - 2.0pp | Normalized estimate | Base + 1.5pp |
| CapEx as % of Revenue | Base + 0.4pp | 5-year historical avg | Base - 0.3pp |
| WACC | Base + 1.5pp | CAPM-derived + moat adj | Base - 1.0pp |
| Terminal growth rate | Base - 0.5pp | GDP-based estimate | Base + 0.3pp |

### Why Asymmetric Shifts?

Bear shifts are intentionally larger than bull shifts. This reflects
how risk materializes: downside shocks (recessions, competitive
attacks, regulatory changes, credit stress) tend to be sudden and
non-linear. Upside surprises tend to be gradual.

The bear case is a stress-test floor: "Even if things go wrong, what is
this business worth?" The bull case is the maximum achievable ceiling
under favorable conditions: "If everything goes right, what's the
upside?" The base case is your central estimate.

### Scenario Probability Weighting

For the final intrinsic value proposition, you can probability-weight
the scenarios:

```
Weighted IV = P(bear) * Bear_IV + P(base) * Base_IV + P(bull) * Bull_IV

Typical weights for a stable business: 25% bear, 50% base, 25% bull
For a binary-outcome business: 40% bear, 40% base, 20% bull
```

**Do not use probability weighting to justify a buy.** If the bear case
produces an intrinsic value below the current price, the margin of
safety is negative under pessimistic assumptions. Probability-weighting
does not make that risk go away.

## Part 4: EPV Cross-Check (Greenwald)

Earnings Power Value provides a "no-growth floor" -- the value of the
business assuming it never grows but maintains current earnings power
indefinitely.

```
EPV = Adjusted Earnings / Cost of Capital

Where:
  Adjusted Earnings = Normalized EBIT * (1 - Tax Rate)
    + 0.5 * Depreciation (excess depreciation add-back, after-tax)
    - Maintenance CapEx (assume = depreciation for no-growth)

  Cost of Capital = WACC (same as used in DCF)
```

**Steps to calculate Adjusted Earnings:**

1. Start with normalized EBIT (from Stage 4B normalized earnings)
2. Multiply by (1 - effective tax rate)
3. Add back 50% of depreciation (after-tax) as a proxy for excess
   depreciation (the portion of depreciation that is not needed for
   maintenance capex at a constant-size firm)
4. Subtract maintenance CapEx (assume = depreciation for a no-growth
   steady state)

**Interpreting the EPV:**

```
EPV per Share = (Enterprise Value from EPV - Net Debt) / Shares Outstanding

If EPV > Market Price: GROWTH COMES FREE. The business is undervalued
  even assuming zero future growth. This is the ultimate margin of safety.

If EPV is 50-80% of Market Price: The market is pricing in reasonable
  growth. The DCF must justify this growth with moat-based evidence.

If EPV < 30% of Market Price: The market is pricing in aggressive growth.
  Requires exceptional moat + thesis evidence to justify.
```

**EPV-DCF divergence:** If the DCF base case is significantly above
EPV (>2x), the difference is entirely attributable to growth
assumptions. Ask: "Does the moat (Stage 4A) and thesis (Stage 6)
support this much value from growth?" If the answer is uncertain,
the DCF assumptions are too aggressive.

## Part 5: Multiple-Based Sanity Check

A DCF can produce any number you want by tweaking assumptions. Market
multiples provide an external reality check.

### Historical Multiples vs Current

| Multiple | Current | 5-Year Avg | 5-Year Low | 5-Year High | Industry Avg |
|:--|:--|:--|:--|:--|:--|
| P/E (Normalized) | Xx | Xx | Xx | Xx | Xx |
| EV/EBIT | Xx | Xx | Xx | Xx | Xx |
| P/B | Xx | Xx | Xx | Xx | Xx |
| FCF Yield | X% | X% | X% | X% | X% |

**Assessment questions:**
1. Is the company trading above or below its historical range? Why?
2. Is the multiple justified by the company's competitive position
   relative to peers? A wide-moat company SHOULD trade at a premium
   to peers.
3. Does the multiple narrative match the fundamental narrative? If
   the stock trades at 8x earnings (value multiple) but the thesis
   calls for 15% growth for 5 years, either the market sees something
   you don't, or you have identified a genuine mispricing. Either way,
   explain the discrepancy.

### Implied Multiple from DCF

Calculate what multiple your DCF implies:

```
Implied P/E = DCF Intrinsic Value / Normalized EPS
Implied EV/EBIT = (DCF Enterprise Value) / Normalized EBIT
```

If your DCF implies a P/E of 30x for a business where peers trade at
15x, your growth assumptions are aggressive relative to what the
market assigns to comparable businesses. This does not mean you are
wrong -- it means you need exceptionally strong evidence.

## Part 6: Sensitivity Analysis (5x5 Matrix)

The bear/base/bull scenarios show three points. A sensitivity matrix
shows the continuous relationship between the two most impactful
assumptions: WACC and terminal growth rate.

### Matrix Construction

Build a 5x5 grid centered on your base case assumptions:

| WACC \ TG | g - 1.0% | g - 0.5% | **Base g** | g + 0.5% | g + 1.0% |
|:--|:--|:--|:--|:--|:--|
| **WACC - 2.0%** | $X | $X | $X | $X | $X |
| **WACC - 1.0%** | $X | $X | $X | $X | $X |
| **Base WACC** | $X | $X | **$BASE** | $X | $X |
| **WACC + 1.0%** | $X | $X | $X | $X | $X |
| **WACC + 2.0%** | $X | $X | $X | $X | $X |

**How to read the matrix:**
- The center cell is your base case
- Moving UP = lower WACC (higher value, more optimistic)
- Moving RIGHT = higher terminal growth (higher value)
- The upper-right is your "best case" (low WACC, high growth)
- The lower-left is your "worst case" (high WACC, low growth)

**Interpretation guide:**
- If most of the upper-left cells are above the current market price,
  the stock is undervalued under a wide range of assumptions
- If only the lower-right cells (high growth, low WACC) are above the
  market price, you are betting on optimistic outcomes
- The main diagonal (upper-left to lower-right) shows combinations
  with similar WACC-g spreads; if values are stable along the diagonal,
  the model is internally consistent

### Sanity Bounds

Before publishing any intrinsic value, check:

| Bound | Limit | Action if Exceeded |
|:--|:--|:--|
| IV / Market Price | 0.1x to 10x | Values outside this range indicate model error or extreme speculation |
| Bull / Market Price | <15x | A bull case 15x the current price is wishful thinking, not analysis |
| Bear IV | Must be >0 | A negative bear case means the assumptions are incompatible with the capital structure |
| TV as % of Total IV | 50-90% | If TV is >90%, the explicit forecast window is meaningless. If <50%, extend the forecast period. |

## Part 7: The Intrinsic Value Proposition

This is the output section -- the answer to "what is this company
worth?" It must be clear, defensible, and honest about uncertainty.

### Intrinsic Value Range Table

| Scenario | IV per Share | vs Current Price | MOS |
|:--|:--|:--|:--|
| Bear Case | $X | +X% / -X% | X% |
| Base Case | $X | +X% / -X% | X% |
| Bull Case | $X | +X% / -X% | X% |
| Probability-Weighted | $X | +X% / -X% | X% |
| EPV (No-Growth) | $X | +X% / -X% | -- |

### Margin of Safety Calculation

```
MOS = 1 - (Market Price / Intrinsic Value_Base Case)

Or more conservatively:
MOS = 1 - (Market Price / Intrinsic Value_Bear Case)
```

**MOS Classification:**

| MOS (Base Case) | Classification | Action |
|:--|:--|:--|
| >= 50% | Exceptional discount | BUY CANDIDATE (highest conviction) |
| 30-50% | Significant discount | BUY CANDIDATE |
| 20-30% | Moderate discount | WATCHLIST (monitor for better entry) |
| 10-20% | Narrow discount | WATCHLIST (only if moat is WIDE) |
| <10% | Fairly to overvalued | DISCARD (or WATCHLIST for price decline) |

**MOS calibration by business quality:**

| Moat Score | Required MOS | Rationale |
|:--|:--|:--|
| Wide (4-5) | >= 20% | High confidence in durability justifies tighter MOS |
| Narrow (3-3.9) | >= 30% | Standard value-investing cushion |
| Weak (2-2.9) | >= 40% | Large cushion needed for uncertainty |
| None (<2) | N/A | Do not value; DISCARD |

### Key Assumptions Disclosure

State your most impactful assumptions explicitly so they can be
challenged:

| Assumption | Base Case Value | Rationale | What Would Change It |
|:--|:--|:--|:--|
| Revenue CAGR (Years 1-5) | X% | Thesis pillar Y, market Z growth | Competitor entry, market slowdown |
| Terminal Operating Margin | X% | 5-year avg normalized, moat supports | Competitive pressure, input cost inflation |
| WACC | X% | CAPM + moat adjustment | Rising rates, beta change |
| Terminal Growth Rate | X% | GDP-based estimate | Structural industry decline |

### Investment Verdict

Based on the DCF, EPV cross-check, multiple sanity check, and
sensitivity analysis:

```
INTRINSIC VALUE RANGE: $X to $Y per share
BASE CASE: $Z per share
CURRENT PRICE: $W
MARGIN OF SAFETY (Base): X%

VERDICT: [BUY CANDIDATE / WATCHLIST / DISCARD]
CONVICTION: [HIGH / MODERATE / LOW]

Key risk to the valuation: [single most impactful assumption that,
if wrong, most changes the result]
```

## Sector-Specific Methodology

The standard 2-stage DCF works for most industrial, consumer, and
technology businesses. For specific sectors, adapt the methodology:

### SaaS / Subscription Businesses

**Key differences:**
- Focus on revenue retention (gross retention rate, net retention rate)
- Model customer acquisition cost (CAC) and lifetime value (LTV)
- Revenue-based DCF (use revenue growth rather than FCF growth in early
  years; FCF emerges as growth matures)
- Key metric: Rule of 40 (Revenue Growth % + FCF Margin % > 40%)

### REITs

**Key differences:**
- Use FFO (Funds From Operations) or AFFO (Adjusted FFO) instead of FCF
- FFO = Net Income + Depreciation - Gains on Property Sales
- AFFO = FFO - Recurring CapEx - Straight-Line Rent Adjustments
- Valuation: P/FFO multiple + NAV (Net Asset Value of property portfolio)
- DCF using AFFO as the cash flow proxy

### Banks / Financials

**Key differences:**
- DCF does not work well for banks (debt is raw material, not financing)
- Use Excess Returns Model:
  ```
  Value = Book Value + PV of Future Excess Returns
  Excess Return = (ROE - Cost of Equity) * Book Value
  ```
- Project ROE converging to cost of equity over 5-10 years
- Terminal value = Book Value (when ROE = Cost of Equity)

### Insurance

**Key differences:**
- Valuation = Float Value + PV of Underwriting Profits + Investment
  Portfolio Value
- Float = unearned premium reserves + loss reserves
- Value of float = float * (1 - combined ratio / cost of capital)
  (this is the value of "free money" if combined ratio < 100%)
- Combined ratio trend (ideally <95% consistently)

### Energy / Materials / Cyclicals

**Key differences:**
- Do NOT use current earnings -- normalize across the cycle
- Use cycle-average EBIT margins (7-10 year average)
- Use cycle-average commodity prices, not spot
- Reserve valuation: PV of proven + probable reserves at normalized
  prices minus extraction costs
- DCF with normalized earnings as the base case

## Common DCF Mistakes

1. **Using peak margins as terminal margins.** The single most common
   error. If today's margins are at 10-year highs, normalize DOWN.

2. **Terminal growth rate > GDP growth.** A company cannot grow faster
   than the economy forever. Terminal g above 3.5-4% for developed
   markets is almost certainly wrong.

3. **WACC too low.** A WACC of 7% with a risk-free rate of 4.3% implies
   an equity risk premium of less than 3% after accounting for beta.
   That is aggressive. WACC below 7% requires extraordinary evidence
   of low-risk, predictable cash flows.

4. **Ignoring dilution.** Using basic shares outstanding instead of
   diluted shares. SBC is a real cost. If diluted shares are 5-10%
   higher than basic, your IV per share is 5-10% too high.

5. **Forecasting FCF without checking against historical conversion.**
   If the company has never generated FCF above 50% of net income,
   projecting 80% conversion in Year 3 is wishful thinking unless you
   have a specific catalyst.

6. **Terminal value cross-check gap.** If the implied exit multiple
   from your terminal growth assumption is wildly different from
   observable comps, your growth assumption is wrong.

7. **Discarding the bear case.** If the bear case intrinsic value is
   below the current price, you are NOT buying with a margin of safety
   -- you are betting against the bear case materializing. That is
   speculation, not value investing.

8. **Sensitivity matrix blindness.** If only 3 of 25 cells in the
   sensitivity matrix show upside, you are betting on a narrow set of
   outcomes. The matrix should show upside in a majority of reasonable
   WACC/growth combinations.

9. **The circular DCF.** If your DCF says "buy" but you cannot explain
   in plain English why the market is mispricing this business, you
   have probably made an assumption error. The market may be smarter
   than your spreadsheet.

10. **Forgetting the EPV test.** If the DCF value is 5x the EPV, growth
    assumptions dominate the valuation. Are you confident enough in a
    10-year growth trajectory to bet on it? If not, the DCF is too
    aggressive.

## Sources

1. Greenwald, Bruce. "Value Investing: From Graham to Buffett and
   Beyond." Wiley, 2001. (EPV methodology)

2. Damodaran, Aswath. "Damodaran on Valuation." 2nd Edition. Wiley,
   2006. (DCF, WACC, sector-specific methodology)
   https://pages.stern.nyu.edu/~adamodar/

3. VCP Scanner. "DCF Intrinsic Value Methodology." 2026.
   https://vcpscanner.com/methodology/dcf

4. AL Capital Advisory. "DCF Valuation: How to Calculate Intrinsic
   Value." July 2026.
   https://alcapitaladvisory.com/research/frameworks/dcf.html

5. Wall Street Prep. "Terminal Value (DCF)." April 2025.
   https://www.wallstreetprep.com/knowledge/terminal-value

6. StableBread. "How to Use Bruce Greenwald's Earnings Power Value
   (EPV) to Value Mature Companies." November 2025.
   https://stablebread.com/earnings-power-value

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- Stages 7A-7D specification
- `investing/frameworks/deep-financial-scoring.md` -- normalized earnings and FCF quality inputs
- `investing/frameworks/deep-moat-scoring.md` -- moat quality feeds terminal value assumptions
- `library/value-investing/margin-of-safety.md` -- the principle this framework implements
- `library/value-investing/intrinsic-value-estimation-methods.md` -- broader valuation context
