---
name: screening-data-guide
id: 20260729T080627Z
tier: framework
domain: value-investing
author: Ava
tags: [screening, data, api, financial-statements, fmp, simfin, alpha-vantage, yfinance, global]
links:
  - investing/frameworks/screening-template.md
  - investing/pipeline/intrinsic-value-pipeline.md
---

# Screening Data Guide -- How to Pull Global Financial Data for the Screener

## Purpose

This guide documents every free financial data source available to
Suggi-Workstation agents for populating the screening template
(`investing/frameworks/screening-template.md`). It covers what each
source provides, its rate limits, exact API endpoints, code examples,
and the practical strategy for assembling a global screening universe.

This guide is self-contained. A new agent with zero context can read
it, register for the necessary API keys, and begin pulling data.

## What Data the Screener Needs

The screening template requires these fields per company:

| Field | Source Statement | Used In |
|:--|:--|:--|
| Ticker | -- | Identifier |
| Company Name | Profile | Identifier |
| Country / Region | Profile | Universe grouping |
| Sector | Profile | Filtering |
| Market Cap (MC) | Profile / Key Metrics | MC/EBIT ratio |
| Enterprise Value (TEV) | Key Metrics | Reference (not used in formulas) |
| Revenue (base year) | Income Statement | Revenue CAGR |
| Revenue (LTM) | Income Statement | Op Margin, Rev CAGR |
| Operating Income (LTM) | Income Statement | Op Margin, ROIC, MC/EBIT |
| Shareholders' Equity | Balance Sheet | Invested Capital |
| Long-Term Debt | Balance Sheet | Invested Capital |

**Derived formulas (calculated, not pulled):**
- Op Mrg LTM = OpInc / Revenue
- Rev Grwth = (Rev_LTM / Rev_Base)^(1/years) - 1
- Inv Cap = MAX(Equity, 0) + MAX(LT_Debt, 0)
- ROIC = OpInc / InvCap
- MC/EBIT = MC / OpInc

## The Global Data Landscape -- Summary

| Source | US Stocks | Non-US | History | Daily Calls | Bulk? | Cost |
|:--|:--|:--|:--|:--|:--|:--|
| **SimFin** | 5,000 | None | 5yr (free), 10yr ($15/mo) | Credit-based | **Yes** | Free |
| **FMP** | Full (free) | Paid tiers | 5yr | 250 | No (free) | Free |
| **Alpha Vantage** | Full | ADRs only (free) | **20yr** | 25 | No | Free |
| **yfinance** | Full | **Global** | 5-10yr | Rate-limited | No | Free |
| **Finnhub** | Quotes only | Quotes only (free) | N/A | 60/min | No | Free* |

*Finnhub financial statements are Premium-only despite claiming
"global" on their marketing page.

**Key insight:** No single free source covers global markets with
fundamental data. The pipeline must be multi-source by design.

---

## Source 1: SimFin (Recommended for US)

### What It Provides

SimFin offers bulk-downloadable, standardized financial statements
for ~5,000 US stocks. Data is AI-extracted from SEC filings and
manually reviewed. Quality is higher than any other free source.

**Free tier:**
- 5,000 US stocks
- 5 years of fundamentals (income statement, balance sheet, cash flow)
- Daily share prices
- 500 high-speed credits per month
- Bulk download via Python library

**Paid tiers (for 10-year history):**
- START ($15/mo): 10 years
- BASIC ($35/mo): 15 years, premium bulk datasets
- PRO ($71/mo): 20+ years

### How to Access

1. Register at https://simfin.com/login (free, no credit card)
2. Get your API key from https://simfin.com/data/api
3. Install the Python library:

```bash
pip install simfin
```

### Key Endpoints (via Python Library)

```python
import simfin as sf
from simfin.names import *

# Set your API key
sf.set_api_key('YOUR_FREE_API_KEY')

# Set data directory (created automatically)
sf.set_data_dir('~/simfin_data/')

# Load ALL US company annual income statements
df_income = sf.load_income(variant='annual', market='us')

# Load ALL US company annual balance sheets
df_balance = sf.load_balance(variant='annual', market='us')

# Load ALL US company annual cash flow statements
df_cashflow = sf.load_cashflow(variant='annual', market='us')

# Load daily share prices for ALL US companies
df_prices = sf.load_shareprices(market='us', variant='daily')
```

### Data Fields for the Screener

**Income Statement (df_income):**
- `REVENUE` -- Total revenue
- `OPERATING_INCOME` -- Operating income (EBIT)
- Indexed by ticker and report date. Filter for most recent fiscal year.

**Balance Sheet (df_balance):**
- `TOTAL_EQUITY` -- Total shareholders' equity
- `LONG_TERM_DEBT` -- Long-term debt
- `TOTAL_DEBT` -- Total debt (short + long)

**Share Prices (df_prices):**
- `CLOSE` -- Daily closing price (use latest for market cap proxy)
- Note: Multiply shares outstanding by price for market cap, or use
  SimFin's calculated metrics.

### Practical Notes

- The first `load_*` call downloads data; subsequent calls use cache.
- Data is returned as pandas DataFrames with MultiIndex (Ticker,
  Report Date).
- SimFin's fiscal years may not align with calendar years. Use the
  most recent report for LTM data.
- The free tier gives 5 full fiscal years. Paid unlocks 10+ years.
- SimFin does NOT cover non-US stocks. For EU/Asia, use other sources.

### Rate Limits

SimFin uses a credit system, not daily request limits. Free tier
gets 500 high-speed credits/month. Bulk download operations use
few credits (typically 1-3 credits per dataset load).

---

## Source 2: Financial Modeling Prep (FMP)

### What It Provides

FMP offers financial data via REST API for 70,000+ securities
globally on paid tiers. The free tier is US-focused.

**Free tier (Basic):**
- 250 API calls per day
- End-of-day data only
- 5 years of history
- US exchanges (NYSE, NASDAQ, AMEX)
- No bulk endpoints
- No stock lists or screeners

**Paid tiers:**
- Starter ($22/mo): US coverage, 300 calls/min
- Premium ($59/mo): US+UK+Canada, 30yr history, 750 calls/min
- Ultimate ($149/mo): Global coverage, bulk endpoints, transcripts

### How to Access

1. Register at https://financialmodelingprep.com/register
2. API key is available in your dashboard
3. All requests use the `/stable/` endpoint prefix

### Key Endpoints (Free Tier)

**IMPORTANT:** All v3 endpoints (`/api/v3/`) are DEPRECATED for
free users. Use only `/stable/` endpoints. v4 bulk endpoints are
Professional-only (402 error on free tier).

#### Company Profile

Returns symbol, name, sector, industry, country, market cap, exchange,
beta, price, and more.

```bash
curl "https://financialmodelingprep.com/stable/profile?symbol=AAPL&apikey=YOUR_KEY"
```

Python:
```python
import requests
resp = requests.get(
    "https://financialmodelingprep.com/stable/profile",
    params={"symbol": "AAPL", "apikey": "YOUR_KEY"}
)
data = resp.json()[0]
# Fields: symbol, companyName, marketCap, sector, industry, country,
#         exchange, price, beta, currency, isEtf, isActivelyTrading
```

**Cost:** 1 call per company.

#### Income Statement (Annual)

Returns annual income statements. `limit` controls how many years.
Maximum on free tier is 5.

```bash
curl "https://financialmodelingprep.com/stable/income-statement?symbol=AAPL&limit=5&apikey=YOUR_KEY"
```

Python:
```python
resp = requests.get(
    "https://financialmodelingprep.com/stable/income-statement",
    params={"symbol": "AAPL", "limit": 5, "apikey": "YOUR_KEY"}
)
data = resp.json()
for year in data:
    print(f"{year['date'][:4]}: revenue={year['revenue']}, "
          f"operatingIncome={year['operatingIncome']}")
```

**Cost:** 1 call per company (gives all years at once with limit=5).

**Free tier constraint:** `limit` must be between 0 and 5. Values >5
return HTTP 402 "Premium Query Parameter."

#### Balance Sheet

Returns annual balance sheets. Use `limit=1` for latest period.

```bash
curl "https://financialmodelingprep.com/stable/balance-sheet-statement?symbol=AAPL&limit=1&apikey=YOUR_KEY"
```

Python:
```python
resp = requests.get(
    "https://financialmodelingprep.com/stable/balance-sheet-statement",
    params={"symbol": "AAPL", "limit": 1, "apikey": "YOUR_KEY"}
)
data = resp.json()[0]
# Fields: totalEquity, longTermDebt, totalDebt, totalAssets,
#         totalLiabilities, shortTermDebt
```

**Cost:** 1 call per company.

#### Key Metrics TTM

Returns trailing-twelve-month metrics including market cap and
enterprise value.

```bash
curl "https://financialmodelingprep.com/stable/key-metrics-ttm?symbol=AAPL&apikey=YOUR_KEY"
```

Python:
```python
resp = requests.get(
    "https://financialmodelingprep.com/stable/key-metrics-ttm",
    params={"symbol": "AAPL", "apikey": "YOUR_KEY"}
)
data = resp.json()[0]
# Fields: marketCap, enterpriseValueTTM, returnOnInvestedCapitalTTM,
#         returnOnEquityTTM, and 30+ calculated ratios
```

**Cost:** 1 call per company.

#### Key Metrics (Historical)

Returns annual historical metrics. On free tier, also limited to
5 periods.

```bash
curl "https://financialmodelingprep.com/stable/key-metrics?symbol=AAPL&limit=5&apikey=YOUR_KEY"
```

**Cost:** 1 call per company.

#### Symbol Search

The ONLY working listing endpoint on free tier. Searches by ticker
prefix. Maximum 500 results per call.

```bash
curl "https://financialmodelingprep.com/stable/search-symbol?query=A&limit=500&apikey=YOUR_KEY"
```

Python (building a ticker list):
```python
import string, requests, time

tickers = []
for letter in string.ascii_uppercase:
    resp = requests.get(
        "https://financialmodelingprep.com/stable/search-symbol",
        params={"query": letter, "limit": 500, "apikey": "YOUR_KEY"}
    )
    data = resp.json()
    tickers.extend(data)
    time.sleep(0.5)  # Be polite

# Filter for US stocks (NYSE, NASDAQ, AMEX)
us_tickers = [t for t in tickers
              if t['exchange'] in ('NYSE', 'NASDAQ', 'AMEX')
              and not t.get('symbol', '').count('.')]  # Exclude preferred shares
```

**Cost:** 26 calls to cover A-Z. Returns ~13,000 symbols.

#### Endpoints That DO NOT Work on Free Tier

| Endpoint | Error | Why |
|:--|:--|:--|
| `/stable/income-statement-bulk` | 402 | Professional+ only |
| `/stable/balance-sheet-statement-bulk` | 402 | Professional+ only |
| `/stable/company-screener` | 402 | Restricted |
| `/stable/stock-screener` | 404 | Deprecated |
| `/stable/stock/list` | 404 | Deprecated |
| `/stable/financial-statement-symbol-lists` | 404 | Deprecated |
| `/stable/actively-trading-list` | 402 | Restricted |
| `/api/v3/*` (all v3) | 403 | Legacy -- discontinued Aug 2025 |

#### Batch Endpoint (Works on Free)

Multiple quotes in one call:

```bash
curl "https://financialmodelingprep.com/stable/quote/AAPL,MSFT,GOOGL?apikey=YOUR_KEY"
```

Note: This returns quotes only (price, volume, change), not profiles.

### FMP Daily Budget Strategy

With 250 calls/day on free tier:

- 26 calls: Build US ticker list (A-Z search)
- Remaining 224 calls: At 3 calls per stock (profile + income + balance),
  this covers ~74 US stocks per day.
- Over 1 week (7 days): ~520 US stocks.
- To get 3,000 US stocks: approximately 6 weeks of daily runs.

**This is impractically slow for screening.** Use SimFin for US stocks
and FMP only for non-US stocks where no bulk alternative exists, or
for incremental updates after the initial bulk download.

---

## Source 3: Alpha Vantage

### What It Provides

Alpha Vantage provides company overviews, income statements, balance
sheets, and cash flow statements via REST API. It has the longest
free history of any provider (20+ years).

**Free tier:**
- 25 API calls per day
- 1 call per second rate limit (strict)
- Full US exchange coverage
- Non-US stocks limited to ADRs only on free tier
- 20+ years of annual history per statement

**Note on global coverage:** Alpha Vantage's marketing claims
"global coverage" but on the free tier, non-US tickers (e.g.,
Nestle S.A. as NESN.SW) return empty responses. Only US-listed
ADRs of foreign companies work (e.g., TM for Toyota, BABA for
Alibaba, both listed on NYSE).

### How to Access

API key from https://www.alphavantage.co/support/#api-key
(free registration).

### Key Endpoints

#### Company Overview

```bash
curl "https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=YOUR_KEY"
```

Python:
```python
import requests
resp = requests.get("https://www.alphavantage.co/query", params={
    "function": "OVERVIEW",
    "symbol": "AAPL",
    "apikey": "YOUR_KEY"
})
data = resp.json()
# Fields: Symbol, Name, Sector, Industry, Country,
#         MarketCapitalization, Exchange, Currency, Description,
#         PERatio, PEGRatio, BookValue, DividendYield, and 50+ more
```

**Cost:** 1 call per company.

**Important:** If the response is `{}` (empty JSON), the ticker is
not available on your plan (likely non-US). Check with a known
US ticker first to confirm your key is working.

#### Income Statement (Annual)

```bash
curl "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=AAPL&apikey=YOUR_KEY"
```

Python:
```python
resp = requests.get("https://www.alphavantage.co/query", params={
    "function": "INCOME_STATEMENT",
    "symbol": "AAPL",
    "apikey": "YOUR_KEY"
})
data = resp.json()
for year in data['annualReports'][:10]:
    print(f"{year['fiscalDateEnding'][:4]}: "
          f"revenue={year['totalRevenue']}, "
          f"opInc={year['operatingIncome']}")

# Total years available: len(data['annualReports']) -- typically 20+
```

**Cost:** 1 call per company (returns ALL years in one response).

#### Balance Sheet (Annual)

```bash
curl "https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=AAPL&apikey=YOUR_KEY"
```

Python:
```python
resp = requests.get("https://www.alphavantage.co/query", params={
    "function": "BALANCE_SHEET",
    "symbol": "AAPL",
    "apikey": "YOUR_KEY"
})
data = resp.json()
latest = data['annualReports'][0]
# Fields: totalShareholderEquity, longTermDebt, totalAssets,
#         totalLiabilities, shortTermDebt, and 40+ more
```

**Cost:** 1 call per company (returns ALL years).

### Alpha Vantage Daily Budget Strategy

With 25 calls/day and 20+ years of history:

- Per company: 3 calls (overview + income + balance)
- 8 companies per day
- 1 week: ~56 companies
- 1 month: ~240 companies

**Best use case:** Deep-dive valuation on individual companies where
20-year history matters. Alpha Vantage is the superior choice for
DCF model inputs (the intrinsic value pipeline), NOT for screening
thousands of stocks.

**Rate limit etiquette:** Add `time.sleep(1.5)` between calls.
Alpha Vantage enforces the 1/second limit aggressively and will
return an error message instead of data if you exceed it.

---

## Source 4: yfinance

### What It Provides

yfinance scrapes Yahoo Finance's public data. It is the ONLY free
source with truly global coverage. It provides financial statements,
prices, and company info for stocks on virtually every global exchange.

**No API key required.** Install with `pip install yfinance`.

**Coverage includes:**
- US: NYSE, NASDAQ, AMEX (plain tickers: AAPL, MSFT)
- India: NSE (.NS suffix), BSE (.BO suffix)
- China: Shanghai (.SS), Shenzhen (.SZ)
- Japan: Tokyo (.T)
- Hong Kong: HKEX (.HK)
- UK: London (.L, .IL for IO)
- Germany: XETRA (.DE), Frankfurt (.F)
- France: Euronext Paris (.PA)
- Brazil: Bovespa (.SA)
- Indonesia: IDX (.JK)
- Australia: ASX (.AX)
- Canada: TSX (.TO), TSX-V (.V)
- And many more (see Yahoo Finance for full list)

### Key Limitations

- Unofficial API -- breaks when Yahoo changes their endpoints
- Rate-limited: bulk downloads of thousands of tickers will trigger
  "Too Many Requests" errors
- Fundamental data quality varies by market: best for US, variable
  for emerging markets
- Survivorship bias: delisted tickers disappear from Yahoo
- No bulk financial statement download (per-ticker only)

### How to Access

```bash
pip install yfinance pandas
```

### Key Commands

#### Company Info (Profile + Fundamentals)

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
info = ticker.info

# Key fields for screener:
# info['symbol']           -- ticker
# info['longName']         -- company name
# info['sector']           -- sector
# info['industry']         -- industry
# info['country']          -- country
# info['marketCap']        -- market capitalization
# info['enterpriseValue']  -- enterprise value
# info['currency']         -- reporting currency
```

**Cost:** 1 HTTP request per ticker. Rate-limit by adding sleeps.

#### Income Statement (Annual)

```python
ticker = yf.Ticker("AAPL")
income = ticker.financials  # Annual income statement (DataFrame)

# Transpose for row-per-year format
income_t = income.T
# Columns: Total Revenue, Operating Income, Net Income, etc.
# Index: fiscal year dates

# Get specific fields:
revenue = income_t['Total Revenue']
op_income = income_t['Operating Income']
```

Note: Yahoo Finance column names vary by market. For non-US stocks,
column names may differ. Always inspect `.columns` first.

#### Balance Sheet (Annual)

```python
ticker = yf.Ticker("AAPL")
balance = ticker.balance_sheet  # Annual balance sheet (DataFrame)
balance_t = balance.T

# Key fields (names may vary):
# 'Total Equity Gross Minority Interest'
# 'Long Term Debt'
# 'Stockholders Equity'
# 'Total Debt'
```

**Warning:** Balance sheet field naming is inconsistent across
markets. US stocks typically have standardized names. For non-US
stocks, inspect the columns and adapt.

#### Historical Prices (for Market Cap alternative)

```python
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="5y")  # 5 years of daily prices
# Columns: Open, High, Low, Close, Volume, Dividends, Stock Splits
```

### Non-US Ticker Format

Yahoo Finance uses exchange suffixes to distinguish markets:

| Country | Exchange | Suffix | Example |
|:--|:--|:--|:--|
| India | NSE | .NS | RELIANCE.NS, TCS.NS |
| India | BSE | .BO | RELIANCE.BO |
| China | Shanghai | .SS | 600519.SS (Kweichow Moutai) |
| China | Shenzhen | .SZ | 000858.SZ (Wuliangye) |
| Japan | Tokyo | .T | 7203.T (Toyota) |
| Hong Kong | HKEX | .HK | 0700.HK (Tencent) |
| UK | London | .L | HSBA.L (HSBC) |
| Germany | XETRA | .DE | SAP.DE |
| France | Paris | .PA | MC.PA (LVMH) |
| Brazil | Bovespa | .SA | PETR4.SA (Petrobras) |
| Indonesia | IDX | .JK | BBCA.JK (Bank Central Asia) |
| Canada | TSX | .TO | SHOP.TO (Shopify) |
| Australia | ASX | .AX | BHP.AX |

### yfinance Bulk Strategy

For non-US markets, yfinance is the only free option. The key
challenge is rate limiting. Practical approach:

1. **Get ticker lists from exchange websites** or compile from known
   indices (S&P BSE 500 for India, CSI 300 for China, etc.)
2. **Batch download with delays:**

```python
import yfinance as yf
import time

tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", ...]  # Your list
results = []

for i, tck in enumerate(tickers):
    try:
        t = yf.Ticker(tck)
        info = t.info
        if info and 'marketCap' in info:
            results.append({
                'ticker': tck,
                'name': info.get('longName'),
                'sector': info.get('sector'),
                'country': info.get('country'),
                'marketCap': info.get('marketCap'),
                'revenue': None,  # From income statement
                'opIncome': None,
            })
    except Exception as e:
        print(f"Failed {tck}: {e}")

    time.sleep(0.5)  # Rate limit protection

    # Save progress every 100 tickers
    if i % 100 == 0:
        # Write to disk
        pass
```

3. **For financial statements**, download separately after filtering
   to quality companies (skip micro-caps with missing data).

---

## The Multi-Source Strategy

### Regional Assignment

| Region | Primary Source | Fallback | Estimated Stocks |
|:--|:--|:--|:--|
| United States | SimFin (bulk, free) | FMP | ~5,000 |
| Europe | yfinance (.DE, .PA, .L, etc.) | FMP Starter ($22/mo) | ~500-1,000 |
| China | yfinance (.SS, .SZ) | -- | ~500 |
| India | yfinance (.NS, .BO) | -- | ~500 |
| Japan | yfinance (.T) | -- | ~500 |
| Hong Kong | yfinance (.HK) | -- | ~200 |
| Brazil | yfinance (.SA) | -- | ~200 |
| Indonesia | yfinance (.JK) | -- | ~100 |
| Canada/Australia | yfinance (.TO, .AX) | -- | ~300 |
| Other emerging | yfinance (various suffixes) | -- | ~200 |

**Total achievable universe: ~8,000-9,000 stocks**, of which
~5,000 US stocks can be downloaded in one shot via SimFin.

### Workflow Order

1. **Download US stocks via SimFin** (one script, bulk) into
   `investing/data/us/`
2. **For each non-US region**, compile ticker lists (from exchange
   indices, Suggi's existing screener sheets, or yfinance discovery)
3. **Download non-US stocks via yfinance**, region by region, into
   `investing/data/<region>/`
4. **Store in standardized format** (see "Data Storage Format" below)

### 10-Year Data Upgrade Path

The free tier of every provider is capped at 5 years. To get 10
years for the screening template's `Broad 10y` sheet:

| Source | 10-Year Cost | What You Get |
|:--|:--|:--|
| SimFin START | **$15/mo** | 5,000 US stocks, 10yr fundamentals |
| FMP Premium | $59/mo | US+UK+Canada, 30yr history |
| FMP Ultimate | $149/mo | Global, 30yr, bulk endpoints |

**Recommendation:** SimFin START at $15/mo is the cheapest path to
10-year US data -- the market where screening produces the most
candidates.

---

## Data Storage Format

Store downloaded data in `investing/data/` with this structure:

```
investing/data/
  us/
    profiles.csv         # symbol, name, sector, industry, country, exchange, marketCap
    income_annual.csv    # symbol, year, revenue, operatingIncome
    balance_annual.csv   # symbol, year, totalEquity, longTermDebt, totalDebt
  eu/
    profiles.csv
    income_annual.csv
    balance_annual.csv
  cn/
    profiles.csv
    income_annual.csv
    balance_annual.csv
  in/
    ...
  jp/
    ...
  br/
    ...
  id/
    ...
```

### CSV Schema

**profiles.csv:**
```
symbol,name,sector,industry,country,exchange,marketCap,currency,source
AAPL,Apple Inc.,Technology,Consumer Electronics,US,NASDAQ,4994876028480,USD,simfin
```

**income_annual.csv:**
```
symbol,year,revenue,operatingIncome,currency,source
AAPL,2025,416161000000,133050000000,USD,simfin
AAPL,2024,391035000000,123216000000,USD,simfin
```

**balance_annual.csv:**
```
symbol,year,totalEquity,longTermDebt,totalDebt,currency,source
AAPL,2025,73733000000,78328000000,112377000000,USD,simfin
```

### Source Field Values

- `simfin` -- SimFin bulk download
- `fmp` -- Financial Modeling Prep API
- `alphavantage` -- Alpha Vantage API
- `yfinance` -- Yahoo Finance via yfinance

---

## Appendix: Provider Registration Links

| Provider | Registration | API Key Location |
|:--|:--|:--|
| SimFin | https://simfin.com/login | https://simfin.com/data/api |
| FMP | https://financialmodelingprep.com/register | Dashboard |
| Alpha Vantage | https://www.alphavantage.co/support/#api-key | Email delivery |
| yfinance | None needed | N/A (pip install) |

---

## Appendix: Suggi's API Keys

As of 2026-07-29, Suggi has active API keys for:

- **FMP:** `8alJOFxR8NkvXMluV53LRceVfsummEq3` (free tier, 250 calls/day)
- **Alpha Vantage:** `N0P4Y67NLZFJBX9U` (free tier, 25 calls/day)

These keys MUST NOT be committed to any public repository. Store
them as environment variables or in `~/.openclaw/.env`.

SimFin registration is pending -- see the Recommendation section.

---

*Last updated: 2026-07-29 by Ava. This guide is living documentation.
Update it when new sources are discovered or rate limits change.*
