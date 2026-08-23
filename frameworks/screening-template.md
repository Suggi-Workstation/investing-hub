---
name: screening-template
id: 20260728T113924Z
tier: framework
domain: value-investing
author: Ava
tags: [screening, quality, composite, growth, roic, cheapness, percentile-rank, 25-25-50]
links:
  - investing/pipeline/intrinsic-value-pipeline.md
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/frameworks/deep-financial-scoring.md
---

# Screening Template -- 25/25/50 Composite Scorer

## Purpose

This framework documents Suggi's screening methodology. It takes raw
financial data for a universe of companies (by region), calculates
derived metrics, percentile-ranks each company within its universe,
and produces a composite score. The score identifies companies that
combine growth, profitability, and cheapness.

This is Suggi's domain -- the screening identifies candidates. My domain
is intrinsic value calculation for the quality companies that emerge.
See the framework files for the separation of concerns.

## Sheet Structure

The Excel workbook contains six sheets:

| Sheet | Purpose | Growth Window |
|:--|:--|:--|
| `Broad 6Y` | US stocks, 6-year CAGR | (Rev LTM / Rev 2018)^(1/6) - 1 |
| `Broad 10y (Avg)` | US stocks, 10-year average growth | (Rev LTM / Rev 2014)^(1/10) - 1 |
| `EU <date>` | European stocks, dated screening run | 10-year |
| `Indo <date>` | Indonesian stocks, dated screening run | 10-year |

Each sheet has the same 26-column layout. Dated sheets (EU 05.08.25,
EU 08.09.25, Indo 27.07.25, Indo 11.09.25) are historical screening
runs. Broad sheets are templates waiting for US data.

## Column Schema (26 columns)

### Input Columns (A-L)

| Col | Header | Description | Example |
|:--|:--|:--|:--|
| A | (notes) | Manual label, e.g. "Financial Investor", "Polish Snack" | -- |
| B | Ticker | Stock ticker symbol | WAWI |
| C | Company Name | Full company name | Wallenius Wilhelmsen ASA |
| D | Region | 3-letter country code | NOR, GBR, IDN |
| E | MC | Market Capitalization (millions, local currency) | 3797 |
| F | TEV | Total Enterprise Value (millions) | 5486 |
| G | Sector | GICS-style sector | Industrials |
| H | Rev <base> | Revenue in base year (varies by sheet) | 285 |
| I | Rev LTM | Revenue last twelve months | 5350 |
| J | Op Inc LTM | Operating Income last twelve months | 1304 |
| K | Equity | Shareholders' equity (book value) | 3001 |
| L | LT Debt | Long-term debt | 1147 |

### Flag Columns (M-P)

| Col | Header | Description |
|:--|:--|:--|
| M | (blank) | Separator |
| N | Low Growth | 1 if flagged for low growth, 0 otherwise |
| O | Reason | Manual note, e.g. "earnings" if earnings issues |
| P | Excluded | 1 if manually excluded from scoring, 0 if active |

### Calculated Columns (Q-V)

| Col | Header | Formula | Units |
|:--|:--|:--|:--|
| Q | (blank) | Separator | -- |
| R | Op Mrg LTM | `=J/I` | Decimal |
| S | Rev Grwth | `=(I/H)^(1/N)-1` where N = years in window | Decimal |
| T | Inv Cap | `=MAX(K,0)+MAX(L,0)` | Millions |
| U | ROIC | `=IF(T>0, (I*R)/T, 1000%)` | Decimal |
| V | MC/EBIT | `=IF(R>0, E/(I*R), 100000)` | Multiple |

**Formula details:**

**Op Mrg LTM (R):** Operating margin. Operating Income divided by
Revenue. Measures what percentage of revenue becomes operating
profit. Health check: a negative or near-zero margin means the
company is unprofitable at the operating level.

**Rev Grwth (S):** Compound Annual Growth Rate over the window.
`(Rev LTM / Rev Base)^(1/years) - 1`. For 6Y sheets: years=6,
base=Rev 2018. For 10Y sheets: years=10, base=Rev 2014.
Captures how fast the top line has expanded. A negative CAGR
means the business is shrinking.

**Inv Cap (T):** Invested Capital. Floored at zero:
`MAX(Equity,0) + MAX(LT_Debt,0)`. This is the capital the business
employs, excluding negative equity situations. Used as the
denominator for ROIC.

**ROIC (U):** Return on Invested Capital.
`(Revenue_LTM * Op_Mrg_LTM) / Inv_Cap` which simplifies to
`Op_Inc_LTM / Inv_Cap`. Measures how efficiently the business
converts invested capital into operating profit. A 1000% sentinel
is assigned when Invested Capital is zero or negative.
Buffett/Munger threshold: >15% is desirable for a quality business.

**MC/EBIT (V):** Market Cap to Operating Income multiple.
`MC / (Rev_LTM * Op_Mrg_LTM)` = `MC / Op_Inc_LTM`. A lower
multiple means the market is pricing each dollar of operating
earnings cheaply. A 100,000 sentinel is assigned when margin is
zero or negative. This is an EV/EBIT-like cheapness metric using
market cap instead of enterprise value.

### Scoring Columns (W-Z)

| Col | Header | Formula | Weight |
|:--|:--|:--|:--|
| W | Grwth Scr | `=PERCENTRANK.EXC(universe_S, S)` | 25% |
| X | ROIC Scr | `=PERCENTRANK.EXC(universe_U, U)` | 25% |
| Y | MC/EV Scr | `=1 - PERCENTRANK.EXC(universe_V, V)` | 50% |
| Z | Total Scr | `=IF(Excluded=0, 25%*W + 25%*X + 50%*Y, 0)` | 100% |

**Scoring logic:**

All three component scores are percentile ranks within the universe
(all companies in the same sheet/region). `PERCENTRANK.EXC` returns
a value from 0 to 1 representing the percentage of the universe
scoring below this value.

- **Growth Score (25%):** Higher revenue CAGR = higher percentile
  rank = higher score. The fastest-growing companies score near 1.0.

- **ROIC Score (25%):** Higher ROIC = higher percentile rank = higher
  score. Companies earning high returns on invested capital score
  near 1.0. The sentinel 1000% ROIC (no invested capital) ranks at
  the top.

- **MC/EV Score (50%):** *Inverted* percentile rank. Lower MC/EBIT =
  higher percentile rank (before inversion) = lower score after
  inversion? Wait -- the formula is `1 - PERCENTRANK.EXC(...)`.
  This means: a LOW MC/EBIT (cheap) gets a HIGH percentile rank,
  which is subtracted from 1, producing... a low score? No.

  Re-read: `=1 - PERCENTRANK.EXC(universe_V, V)`. If MC/EBIT is
  very low (cheap), its PERCENTRANK is low (few companies below it).
  1 - low_rank = HIGH score. So LOW MC/EBIT -> HIGH cheapness score.
  Correct: the inversion makes "cheap" companies score higher.

  The 100,000 sentinel (unprofitable companies) gets a very high
  percentile rank -> `1 - near_1.0` = near-zero cheapness score.
  Effectively excluded.

**Total Score:** Weighted sum: 25% Growth + 25% ROIC + 50% Cheapness.
Excluded companies (flag P=1) score zero regardless of metrics.

The 50% weight on cheapness is intentional -- Suggi's approach
emphasizes buying quality at a discount. Growth and profitability
each get 25%. The result: a company must be good AND cheap to
score high. A fast-growing, high-ROIC company at an expensive
multiple will score lower than a decent company at a cheap price.

## Data Sources Required

For each company in the universe, the screener needs:

| Field | Source | Notes |
|:--|:--|:--|
| Ticker, Name, Region, Sector | Any provider | Static identifiers |
| Market Cap | Real-time/daily price feed | Changes daily -- Suggi's domain |
| Enterprise Value | Financial data API | TEV = MC + Debt - Cash |
| Revenue (base year + LTM) | Alpha Vantage, FMP, yfinance | Income statement |
| Operating Income LTM | Alpha Vantage, FMP, yfinance | Income statement |
| Equity (book value) | Alpha Vantage, FMP, yfinance | Balance sheet |
| Long-Term Debt | Alpha Vantage, FMP, yfinance | Balance sheet |

## Workflow

1. **Define universe:** All stocks in a region (US, EU, Indonesia, etc.)
2. **Pull raw data:** Financial statements for every company via API
3. **Populate columns A-L:** Fill the Excel template or equivalent CSV
4. **Calculate R-V:** Excel formulas compute derived metrics
5. **Score W-Z:** PERCENTRANK.EXC across the universe, weighted composite
6. **Sort by Total Score:** Highest = best combination of growth, ROIC,
   and cheapness
7. **Review flags:** Low Growth (N) and Reason (O) columns flag
   edge cases for manual review. Excluded (P) removes from scoring.
8. **Output to screening folder:** Save dated results to
   `investing/screening/<region>-<date>.md` or `.xlsx`

## Integration with Intrinsic Value Pipeline

This screener identifies candidates. It does NOT calculate intrinsic
value. The pipeline takes the quality
companies from the screener output and:

1. Applies moat scoring (`simple-moat-scoring.md`, `deep-moat-scoring.md`)
2. Applies management scoring (`simple-management-scoring.md`)
3. Applies financial health scoring (`deep-financial-scoring.md`)
4. Applies sector-specific metrics (`sector-specific-metrics.md`)
5. Calculates DCF intrinsic value with bull/base/bear cases
   (`dcf-intrinsic-value.md`)

The screener's Growth Score and ROIC Score are precursor signals.
Companies scoring high on both but low on cheapness may still be worth
valuing -- they are wonderful businesses that just aren't cheap right
now. The pipeline values every quality company regardless of price.
The screener helps Suggi decide which ones to act on.

## File Location

Screening results are stored in `investing/screening/`. Raw financial
data used to populate the screener is stored in `investing/data/`.
