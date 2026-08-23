---
name: simple-management-scoring
id: 20260726T203000Z
tier: framework
domain: value-investing
author: Ava
tags: [management-scoring, capital-allocation, insider-ownership, buffett, pabrai, integrity, governance, how-to]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/simple-moat-scoring.md
  - library/value-investing/anchor-value-investing.md
---

# Simple Management Scoring -- A Practical Framework for Assessing Management Quality

This framework explains how to score a company's management using the
5-dimension system from the investment pipeline (Stage 3C). It is
designed to be used by an agent or analyst who has access to SEC
filings (proxy statements, 10-Ks, Form 4s), earnings call transcripts,
and shareholder letters.

## Why Management Scoring Matters

Warren Buffett: "In looking for people to hire, you look for three
qualities: integrity, intelligence, and energy. And if they don't have
the first, the other two will kill you."

Management quality is one of the hardest things to assess in investing
because it is fundamentally about character and judgment -- things that
do not appear in a spreadsheet. But character leaves fingerprints:

- In the proxy statement (how much are they paid, and for what?)
- In the cash flow statement (what did they do with the cash?)
- In the shareholder letter (do they admit mistakes?)
- In the share count (are they diluting you or buying back smartly?)
- In the Form 4 filings (are they buying or selling?)

A quantitative screen can find cheap stocks. It cannot tell you whether
the people running the business will allocate capital wisely, treat
shareholders as partners, or resist the temptation to empire-build with
your money. The 30-year compounding gap between identical businesses
with different management is approximately 10x: $10,000 compounding at
20% becomes $1.74M; at 10% it becomes $174K. Management is the
difference.

## What Management Scoring Is (And What It Is Not)

A management score answers: **Does this team act as owner-oriented
stewards of shareholder capital?**

It is NOT:
- A personality assessment ("they seem smart")
- A stock price performance score (good stock returns can happen despite
  bad management in a bull market)
- A substitute for moat analysis (great management of a terrible
  business still loses money)
- About charisma, media presence, or public reputation

The core principle: management quality is measured by **actions, not
words.** What management does with capital reveals their true character
more reliably than anything they say in interviews or earnings calls.

## Prerequisite Data to Gather

Before scoring, collect these from public filings:

| Data Point | Source | What It Tells You |
|:--|:--|:--|
| Insider ownership % | Proxy (DEF 14A), 10-K | Alignment with shareholders |
| CEO/CFO total compensation | Proxy statement | Are they overpaid relative to performance? |
| Share count trend (5-10yr) | 10-K cover page | Dilution or buyback discipline? |
| Buyback dollar amount + timing | Cash flow statement, 10-Q | Buying low or at peaks? |
| M&A history (5-10yr) | 10-K notes, press releases | Acquirer discipline or empire-building? |
| Insider transactions (2yr) | Form 4 filings (SEC EDGAR) | Buying = conviction, selling = red flag |
| Shareholder letter quality | Company website, annual report | Candor, clarity, accountability |
| Earnings call transcripts | Seeking Alpha, company IR | Communication style, guidance games |
| Board composition | Proxy statement | Independent oversight or rubber stamp? |
| Related-party transactions | 10-K footnotes | Self-dealing risk |

## The 5-Dimension Scoring Rubric

Each dimension is scored 1-5 with specific evidence requirements.
The dimensions are structured to emphasize what directly impacts
shareholder value creation.

### Dimension 1: Insider Ownership (Weight: 25%)

**What it measures:** Does management have meaningful personal wealth
tied to the company's long-term stock performance?

Skin in the game is the single most powerful alignment mechanism. An
executive with 50% of their net worth in company stock makes different
decisions than one collecting a salary and flipping options.

| Score | Insider Ownership (%) | Additional Criteria |
|:--|:--|:--|
| 1 | <1% | Token ownership; hired-gun CEO with no meaningful stake |
| 2 | 1-3% | Modest ownership; may reflect option grants rather than open-market purchases |
| 3 | 3-10% | Meaningful ownership; CEO's net worth materially tied to stock |
| 4 | 10-20% | Significant skin in the game; founder-level alignment or long-tenured owner-operator |
| 5 | >20% | Founder/owner-operator with wealth almost entirely in the business |

**Adjustments to the raw percentage:**

**Downward adjustment (-1):**
- Insider is a net seller over the last 2 years (selling > buying in
  dollar terms)
- Ownership comes from option grants, not open-market purchases
- Insider has hedged their position (collars, prepaid variable forwards)
- Shares are held through opaque offshore entities

**Upward adjustment (+1):**
- Insider is a net buyer over the last 2 years (open-market purchases)
- Shares held for 5+ years without selling (check Form 4 history)
- Insider bought more during a stock price decline (conviction signal)
- Dollar value of holdings is >10x annual compensation

**The mega-cap scale adjustment:**

A 1% insider stake at a $2 trillion company ($20B personal stake) is
different from 1% at a $200M company ($2M). For mega-caps (>$100B
market cap), use dollar-value benchmarks:

| Dollar Value of Insider Holdings | Equivalent Score |
|:--|:--|
| >$500M | 4 |
| $50M - $500M | 3 |
| $5M - $50M | 2 |
| <$5M | 1 |

Use whichever method (percentage or dollar absolute) yields the HIGHER
score. The point is alignment, and both matter.

**Evidence required:**
- Proxy statement (DEF 14A) for beneficial ownership table
- Form 4 filings for transaction history (SEC EDGAR)
- Insider ownership data from financial data providers

### Dimension 2: Buyback Quality (Weight: 20%)

**What it measures:** Does management repurchase shares at attractive
prices, or do they buy at peaks and dilute through stock-based
compensation?

Buybacks are the most common capital allocation tool and the most
commonly misused. The golden rule: buybacks only create value when
shares are purchased BELOW intrinsic value. Buying at or above
intrinsic value destroys value for remaining shareholders.

| Score | Buyback Behavior | Signals |
|:--|:--|:--|
| 1 | Value-destructive | Buys at cycle peaks, suspends at bottoms, buybacks merely offset SBC dilution, buys with debt at high prices |
| 2 | Undisciplined | Buys regardless of valuation (flat dollar amount per quarter), no evidence of price sensitivity |
| 3 | Moderate discipline | Generally buys below intrinsic value, occasional mistimed purchases, share count slowly declining |
| 4 | Disciplined | Consistently buys below intrinsic value, share count meaningfully declining (2%+/year net of dilution), reduced buybacks when stock is expensive |
| 5 | Exceptional discipline | Only buys at large discounts to intrinsic value, aggressively buys during market panics, share count declined significantly over 5-10 years |

**How to assess buyback quality:**

1. **Check share count trend (5-10 years).** Is shares outstanding
   declining, flat, or growing? A flat share count with billions in
   announced buybacks means the program is mostly offsetting stock-based
   compensation dilution -- it is compensation expense by another name,
   not a return of capital.

2. **Compare buyback timing to price history.** Did the company buy
   heavily at stock price peaks and reduce buybacks at troughs? This
   is the most common error. Check the cash flow statement for buyback
   dollar amounts by quarter against the stock chart.

3. **Check for the SBC treadmill.** Formula:
   ```
   Net Buyback = Gross Buybacks - Stock-Based Compensation Expense
   ```
   If net buyback is negative or near zero, management is returning
   your capital to themselves through dilution. This is a buyback scam,
   not capital allocation.

4. **Ask the two questions.** (a) Does management have a credible
   estimate of intrinsic value and are they buying below it? (b) Is the
   share count actually shrinking? If the answer to either is no, the
   buyback program is theater.

**Red flags specific to buybacks:**
- Announcing large buyback authorizations while insiders are selling
- Funding buybacks with debt at cycle peaks
- Buybacks concentrated in quarters when stock was at all-time highs
- "Buyback program" announced but share count is flat or rising

**Evidence required:**
- 10-K share count data (5-10 years)
- Cash flow statement (financing activities -- share repurchases)
- Stock price history chart overlaid with buyback timing
- SBC expense from income statement or 10-K footnotes

### Dimension 3: Acquisition Track Record (Weight: 20%)

**What it measures:** Has management's M&A history created or destroyed
shareholder value?

Most acquisitions destroy value. The research is consistent: acquirers
routinely overpay, synergies disappoint, and integration costs balloon.
This dimension asks whether THIS management team is the exception or
the rule.

| Score | Acquisition Track Record | Signals |
|:--|:--|:--|
| 1 | Serial value destroyer | Frequent, large acquisitions at peak valuations, multiple goodwill write-downs, financed with stock at depressed prices |
| 2 | Poor discipline | Mixed record, some questionable deals, overpaid in at least one major acquisition |
| 3 | Moderate discipline | Infrequent acquisitions, generally reasonable, some integration issues but no major write-downs |
| 4 | Disciplined acquirer | Infrequent, strategic acquisitions at fair prices, clear integration success, no significant write-downs |
| 5 | Exceptional discipline | Bolt-on acquisitions only, walks away when prices are too high, track record of high-ROIC deals, or no acquisitions because they return capital instead |

**How to assess M&A track record:**

1. **Inventory the last 5-10 years of acquisitions.** List each deal:
   price paid, method of payment (cash vs stock), rationale stated at
   the time, and what actually happened.

2. **Calculate implied ROIC on each deal.** Price paid / pre-tax
   operating income of acquired business. If >15x, the deal is
   unlikely to earn adequate returns. If >20x, value destruction is
   almost certain.

3. **Check for goodwill write-downs.** Search the 10-K for "goodwill
   impairment." A write-down is management admitting they overpaid.
   Multiple write-downs over 5 years = systemic overpayment problem.

4. **Check financing method.** Cash-funded acquisitions signal
   confidence. Stock-funded acquisitions signal management thinks their
   own stock is overvalued -- if they are willing to give it away, ask
   yourself why.

5. **Look at what happened after the deal.** Did acquired revenue grow
   or shrink? Were "synergies" achieved? Did key acquired talent leave?

**Red flags specific to M&A:**
- Serial acquisitions (more than one major deal every 2-3 years)
- "Transformational" deals (euphemism for "we overpaid to change the
  narrative")
- Paying with stock when management's own shares are cheap
- Goodwill >50% of total assets (the balance sheet is a museum of
  overpriced acquisitions)
- Frequent "restructuring charges" (integration costs that keep
  recurring)

**Evidence required:**
- 10-K notes on acquisitions (list of deals, prices, goodwill)
- Search for "goodwill impairment" in 10-K filings
- Revenue and operating income trends of acquired businesses (if
  disclosed)
- Cash flow statement (cash used for acquisitions vs FCF generated)

### Dimension 4: Shareholder Communication (Weight: 15%)

**What it measures:** Is management candid, clear, and accountable in
how they communicate with shareholders?

Buffett: "I want managers who report the bad news early. I can handle
surprises; I can't handle deception."

| Score | Communication Quality | Signals |
|:--|:--|:--|
| 1 | Opaque/deceptive | Hides behind adjusted metrics, blames external factors, earnings guidance games, never admits mistakes |
| 2 | Vague | Generic, promotional language, minimal detail on challenges, "macro headwinds" as universal excuse |
| 3 | Adequate | Reasonably clear, occasional candor, standard reporting, some discussion of challenges |
| 4 | Candid | Admits mistakes, explains business in plain language, discusses what went wrong, avoids hype |
| 5 | Exceptional | Buffett-level: plain language, detailed mistake analysis, long-term focus, educates shareholders, under-promises and over-delivers |

**How to assess communication quality:**

1. **Read the last 3-5 annual shareholder letters.** (If there is no
   letter, that itself is a signal -- score 2 or lower.) Ask:
   - Does the CEO explain the business in plain language?
   - Does the letter discuss what went WRONG, not just what went right?
   - Are problems attributed to specific causes or vague "headwinds"?
   - Does the letter read like it was written by a human, or by a PR
     committee?

2. **Scan earnings call transcripts.** Look for:
   - "Adjusted EBITDA" or "non-GAAP earnings" mentioned more often than
     GAAP earnings (reaching for wallet signal)
   - Blame-shifting: "challenging macro environment" as explanation for
     every miss
   - Guidance games: lowball estimates, then "beat" them quarter after
     quarter
   - Promotional language: "revolutionary," "transformative,"
     "game-changing" -- real moats don't need adjectives

3. **Check the gap between GAAP and non-GAAP earnings.** If "adjusted"
   earnings are consistently 20%+ higher than GAAP earnings, and
   "one-time" charges occur every quarter, management is adjusting the
   truth.

4. **Look at what happened AFTER the communication.** Did management do
   what they said they would do? A track record of broken promises is
   worse than no promises at all.

**Red flags specific to communication:**
- "Adjusted" earnings consistently higher than GAAP (annual "one-time"
  charges)
- Blaming external factors for poor results, taking personal credit for
  good results
- Earnings guidance lowballing ("beat and raise" game)
- Promotional language, superlatives, "transformative" narratives
- No annual shareholder letter, or letter written entirely by IR
- "We don't give guidance" as an excuse for never communicating strategy
  (vs Berkshire, which famously doesn't give quarterly guidance but
  writes extensively about the business)

**Evidence required:**
- Last 3 annual shareholder letters (read them, don't just skim)
- Last 4 quarters of earnings call transcripts (scan for patterns)
- GAAP vs non-GAAP earnings comparison (income statement + earnings
  releases)
- Track record of stated plans vs actual outcomes

### Dimension 5: Capital Allocation (Weight: 20%)

**What it measures:** Does management make rational decisions about
how to deploy the cash the business generates?

This is the meta-dimension. Capital allocation is the CEO's most
important job -- deciding what to do with every dollar of free cash
flow. The five uses of capital, from best to worst:

1. Reinvest at high returns (ROIC > WACC) -- the ideal
2. Return to shareholders via buybacks (if below intrinsic value)
3. Return to shareholders via dividends (tax-inefficient but honest)
4. Pay down debt (reduces risk, has opportunity cost)
5. Acquire other businesses (most likely to destroy value)

Great capital allocators maximize per-share intrinsic value. Poor
capital allocators maximize revenue, ego, or short-term optics.

| Score | Capital Allocation | Signals |
|:--|:--|:--|
| 1 | Value-destroying | ROIC < WACC, empire-building M&A, dividends exceed FCF, chronic dilution, hoards cash while earning 0% |
| 2 | Poor | Mixed decisions, occasional value destruction, return on incremental capital declining |
| 3 | Adequate | Generally rational, some mistakes, reasonable balance of reinvestment and returns |
| 4 | Disciplined | Consistently rational decisions, high-ROIC reinvestment, buybacks at discounts, walks away from bad deals |
| 5 | Exceptional | Ruthlessly rational: reinvests only at high returns, returns excess cash, never overpays, long-term orientation, counter-cyclical behavior |

**How to assess capital allocation quality:**

1. **Track return on incremental invested capital (ROIIC).**
   ```
   ROIIC = (Change in NOPAT) / (Change in Invested Capital)
   ```
   This measures what returns management earns on NEW capital deployed.
   ROIIC declining over time means management is running out of good
   reinvestment opportunities but deploying capital anyway. ROIIC above
   15% consistently means management allocates capital well.

2. **Analyze the 10-year cash flow statement.** Where did the cash go?
   Set up a simple table:

   | Use of Cash | 10-Year Total | % of Total |
   |:--|--:|--:|
   | CapEx (maintenance + growth) | $X | X% |
   | Acquisitions | $X | X% |
   | Dividends | $X | X% |
   | Buybacks (net of issuance) | $X | X% |
   | Debt repayment | $X | X% |

   The allocation pattern reveals management's philosophy. Companies
   that spend 50%+ of cash on acquisitions but earn declining ROIC
   are empire-building. Companies that buy back stock consistently but
   whose share count is flat are running the SBC treadmill.

3. **Check dividend sustainability.** Dividends > free cash flow =
   funded by debt. Unsustainable. Eventually the dividend gets cut and
   the stock follows.

4. **Assess cash management.** Large cash hoards earning near-zero
   returns while the business has high-ROIC reinvestment opportunities
   is poor capital allocation. Cash hoards while the stock trades below
   intrinsic value is poor capital allocation (buy back your own stock!).

5. **Check for trend resistance (Buffett).** Does management blindly
   follow industry trends (serial M&A when peers are acquiring, cost
   cutting to hit quarterly numbers, chasing hot markets) or do they
   make independent, rational decisions even when unpopular?

**Red flags specific to capital allocation:**
- ROIIC declining for 3+ years while capex or M&A spending increases
- Dividends exceeding free cash flow (funded by debt)
- "Growth at any cost" narrative without evidence of returns
- Cash hoarding while earning below-inflation returns and diluting
  shareholders
- Buying back stock at all-time highs, suspending buybacks at lows

**Evidence required:**
- 10-year cash flow statement analysis (capital allocation table)
- ROIIC calculation (NOPAT change / Invested Capital change)
- FCF vs dividends comparison (5+ years)
- Share count trend + SBC expense (to assess net buyback effect)

## Composite Score Calculation

```
Management Score = (Insider Ownership        * 0.25)
                 + (Buyback Quality          * 0.20)
                 + (Acquisition Track Record * 0.20)
                 + (Shareholder Communication* 0.15)
                 + (Capital Allocation       * 0.20)
```

### Quick Reference Table

| Composite Score | Management Classification | Pipeline Verdict |
|:--|:--|:--|
| 4.0 - 5.0 | Exceptional | PASS (strong conviction) |
| 3.0 - 3.9 | Good | PASS |
| 2.0 - 2.9 | Adequate | Conditional -- only PASS if moat score >= 4.0 and business quality compensates |
| 1.0 - 1.9 | Poor | DISCARD (even great businesses fail with bad management) |

### PASS/HALT Threshold

**Management score < 3.0 = DISCARD.** The only exception: if moat score
>= 4.0 AND there is a credible catalyst for management change within
2 years (activist investor, succession plan, regulatory pressure).

Buffett: "I'd rather have a Class A CEO running a Class B business than
a Class B CEO running a Class A business." The moat compensates for
mediocre management only up to a point. Below 3.0, no amount of business
quality compensates for people who will destroy it.

### The Moat-Management Matrix

| Moat / Management | Exceptional (4-5) | Good (3-3.9) | Adequate (2-2.9) | Poor (1-1.9) |
|:--|:--|:--|:--|:--|
| **Wide (4-5)** | Ideal: PASS | PASS | Conditional PASS | DISCARD |
| **Narrow (3-3.9)** | PASS | PASS | Conditional PASS | DISCARD |
| **Weak (2-2.9)** | Conditional PASS | WATCHLIST | WATCHLIST | DISCARD |
| **None (<2)** | WATCHLIST | DISCARD | DISCARD | DISCARD |

The top-left cell (Wide Moat + Exceptional Management) is the Buffett
ideal. The bottom-right cells are guaranteed value destruction.

## Evidence Requirements Per Dimension

| Dimension | Minimum Evidence |
|:--|:--|
| Insider Ownership | Proxy statement ownership table + 2 years of Form 4 transaction data |
| Buyback Quality | 5-year share count trend + net buyback calculation (gross - SBC) + price chart overlay |
| Acquisition Track Record | List of acquisitions (5-10 years) + goodwill impairment check + financing method per deal |
| Shareholder Communication | Last 3 annual letters read + 4 quarters of earnings call transcripts scanned + GAAP vs non-GAAP gap |
| Capital Allocation | 10-year cash flow allocation table + ROIIC trend + dividend sustainability check |

Every score of 4 or 5 requires at least one primary source (SEC filing,
proxy statement, company-published letter). Every score of 1 or 2
requires a specific red flag with a citation.

## The Red Flag Catalog

These are deal-breakers. Any single one should trigger an automatic
downgrade of at least 2 points on the composite score and a mandatory
written explanation if the company is not discarded.

### Integrity Red Flags (Weight: automatic DISCARD if 2+ present)

1. **Accounting manipulation.** Frequent restatements, large and
   recurring "one-time" charges, GAAP vs non-GAAP gap >30%, unusual
   revenue recognition. Source: 10-K footnotes, SEC comment letters.

2. **Excessive compensation without performance.** CEO pay rising
   faster than earnings or stock price for 3+ years. Source: Proxy
   statement compensation table vs stock chart.

3. **Related-party transactions.** Company paying rent to CEO-owned
   real estate, hiring CEO's family members, loans to executives.
   Source: 10-K footnotes (Related Party Transactions).

4. **Insider selling while promoting the stock.** CEO sells significant
   stock while issuing optimistic guidance. Source: Form 4 filings vs
   earnings call transcripts (compare the dates).

5. **Stock-based compensation treadmill.** Share count rising 3%+/year
   while management describes buybacks as "returning capital to
   shareholders." Source: Share count trend + SBC expense.

6. **Serial restructuring charges.** "One-time" restructuring charges
   appearing every year for 3+ years. The charges are not one-time;
   management is smoothing earnings. Source: Income statement.

7. **Earnings guidance manipulation.** Systematic lowballing followed by
   "beats." Source: Compare guidance to actual results over 8+ quarters.

### Competence Red Flags (Weight: downgrade 1-2 points)

1. **Declining ROIIC.** Return on NEW invested capital declining for
   3+ years. Source: NOPAT change / Invested Capital change.

2. **Acquisition write-downs.** Goodwill impairment in 2+ of the last
   5 years. Source: 10-K notes, goodwill impairment section.

3. **Buybacks at peaks, suspension at troughs.** Source: Buyback
   dollar amounts overlayed on stock chart.

4. **Frequent CEO/CFO turnover.** New CEO or CFO every 2-3 years.
   Source: Executive history in proxy statement or 10-K.

5. **Dividend cut after years of borrowing to pay.** Source: FCF vs
   dividend comparison.

6. **Strategy pivots.** New "strategic direction" announced every year.
   Source: Annual shareholder letters over 5 years.

## Worked Example: Management Scoring Applied

### Company A: A Well-Governed Compounder (hypothetical, inspired by Berkshire)

**Background:** Long-tenured founder-CEO (25+ years), no stock sales in
a decade, annual shareholder letter famous for candor, no acquisitions
in 5 years ("prices too high"), buys back stock only below 1.2x book
value.

**Dimension 1 -- Insider Ownership: Score 5**
- CEO owns 37% of shares outstanding
- Has never sold a share in 25 years
- 99% of personal net worth in company stock
- Evidence: Proxy statement, Form 4 history

**Dimension 2 -- Buyback Quality: Score 5**
- Share count declined 15% over 10 years
- Only buys back below 1.2x book value (stated policy, consistently
  followed)
- Massively accelerated buybacks during 2009 and 2020 panics
- Net buyback (gross - SBC) is strongly positive
- Evidence: 10-K share count data, cash flow statement, annual letter

**Dimension 3 -- Acquisition Track Record: Score 4**
- No acquisitions in 5 years ("prices too high")
- Past acquisitions have been disciplined, at fair prices
- No goodwill impairments in 10+ years
- One major acquisition 8 years ago that has exceeded projections
- Not 5 because of one borderline-expensive deal 12 years ago
- Evidence: 10-K notes, goodwill impairment check

**Dimension 4 -- Shareholder Communication: Score 5**
- Annual letter is considered the gold standard in investing
- Discusses what went WRONG in detail every year
- Plain language; no "adjusted" metrics
- Under-promises, over-delivers
- No earnings guidance given
- Evidence: Annual letters (read all 5)

**Dimension 5 -- Capital Allocation: Score 5**
- ROIIC consistently >15% for 10+ years
- Cash allocation over 10 years: 45% reinvested at high returns, 30%
  buybacks at discounts, 15% acquisitions (disciplined), 10% cash
  reserves
- Maintains large cash reserves for opportunistic deployment
- No dividends (compounds better internally)
- Evidence: Cash flow statement analysis, ROIIC calculation

**Composite Score:**

```
(5 * 0.25) + (5 * 0.20) + (4 * 0.20) + (5 * 0.15) + (5 * 0.20)
= 1.25 + 1.00 + 0.80 + 0.75 + 1.00
= 4.80
```

**Verdict: EXCEPTIONAL MANAGEMENT. PASS with maximum conviction.**

### Company B: The Dilutive Serial Acquirer

**Background:** Professional CEO hired 4 years ago. Stock flat over
tenure. 3 major acquisitions, 2 with subsequent goodwill write-downs.
Share count rising 3% annually from SBC. "Adjusted EBITDA" is primary
earnings metric. CEO sold 60% of holdings since joining.

**Dimension 1 -- Insider Ownership: Score 1**
- CEO owns <0.5% of shares (mostly unvested options)
- Net seller: sold $12M of stock in 2 years
- Evidence: Proxy + Form 4

**Dimension 2 -- Buyback Quality: Score 1**
- Announces $500M buyback program annually
- Share count RISING 3%/year (SBC dilution exceeds buybacks)
- Buys regardless of price
- Evidence: Share count trend, gross buybacks vs SBC

**Dimension 3 -- Acquisition Track Record: Score 1**
- 3 major acquisitions in 4 years
- 2 with goodwill impairments within 2 years
- Paid with stock (diluting shareholders further)
- "Transformational deal" language in every press release
- Evidence: 10-K notes, goodwill impairment section

**Dimension 4 -- Shareholder Communication: Score 2**
- "Adjusted EBITDA" exceeds GAAP earnings by 40%+ every quarter
- Blames "macro headwinds" for misses
- No annual shareholder letter (investor presentation slides only)
- Evidence: Earnings releases, earnings call transcripts

**Dimension 5 -- Capital Allocation: Score 1**
- ROIIC negative (acquisitions earn less than cost of capital)
- 10-year cash allocation: 55% M&A, 25% CapEx (declining returns),
  20% SBC, negative net return to shareholders
- Dividend maintained at level exceeding FCF for 2 years
- Evidence: Cash flow statement analysis, ROIIC calculation

**Composite Score:**

```
(1 * 0.25) + (1 * 0.20) + (1 * 0.20) + (2 * 0.15) + (1 * 0.20)
= 0.25 + 0.20 + 0.20 + 0.30 + 0.20
= 1.15
```

**Verdict: POOR MANAGEMENT. DISCARD. No moat quality compensates for
this level of value destruction.**

## Common Mistakes in Management Assessment

1. **Confusing stock performance with management quality.** A company's
   stock can rise in a bull market despite terrible capital allocation.
   The rising tide lifts all boats temporarily. Judge management by
   their decisions, not their stock chart.

2. **Overweighting charisma.** Some of the worst CEOs in history were
   extremely charismatic (Adam Neumann, Elizabeth Holmes, Bernie Ebbers).
   Charisma is a liability if it obscures substance. Judge actions,
   not presentation skills.

3. **Ignoring dilution.** A company that grows earnings 15% annually
   but dilutes shares 10% annually is only growing per-share value 5%.
   Always check per-share metrics, not absolute totals.

4. **Giving credit for buybacks without checking the share count.**
   A buyback "program" with a flat or rising share count is not
   returning capital -- it is offsetting compensation expense. This is
   the most common deception in corporate finance.

5. **Assuming long tenure equals good management.** Some of the worst
   value destroyers stayed in the CEO role for decades. Long tenure
   without evidence of rational capital allocation is entrenchment,
   not excellence.

6. **Overlooking the compensation structure.** The proxy statement tells
   you what management is actually incentivized to do. If bonuses are
   tied to revenue or EBITDA rather than ROIC or per-share value growth,
   management will optimize for revenue and EBITDA at the expense of
   shareholder returns.

7. **Trusting "adjusted" earnings.** When "one-time" charges appear
   every quarter, they are not one-time. The gap between GAAP and
   non-GAAP earnings is a rough measure of management's honesty. A
   wide and persistent gap = dishonesty, not "better reflection of
   underlying economics."

8. **Ignoring the track record of stated goals vs actual outcomes.**
   Management that consistently says "we will achieve X" and then
   achieves X+1 is competent and trustworthy. Management that says
   "we will achieve X" and achieves 0.7X while blaming external
   factors is neither. Track this over 5+ years.

## Integration with the Pipeline

This framework feeds into Stage 3C of the investment pipeline
(`investing/pipeline/investment-pipeline-final.md`). The management
score is the second half of the Stage 3 triage:

- Management score >= 3.0 AND Moat score >= 3.0 -> PASS to Stage 4
- Management score < 3.0 AND Moat score < 3.0 -> DISCARD
- Management score < 3.0 AND Moat score >= 4.0 -> conditional PASS with
  explanation (rare -- requires credible catalyst for management change)
- Management score >= 3.0 AND Moat score < 3.0 -> WATCHLIST (good
  stewards of a mediocre business)

The management score also feeds into:
- Stage 7E Position Sizing (management score >= 4.0 earns a +1 position
  increment)
- Stage 8 Investment Checklist (able and honest management item)
- The "too hard" pile: if management scoring cannot be completed due to
  opaque disclosures, the company goes to TOO HARD regardless of other
  scores

## Sources

1. Morningstar. "Equity Research Methodology." October 2020. Section on
   Capital Allocation Rating.
   https://advisor.morningstar.com/Enterprise/VTC/MasterEquityResearchMethodology_Oct2020.pdf

2. SafetyMargin.io. "Management Quality: Buffett's Evaluation
   Framework." March 12, 2026.
   https://safetymargin.io/blog/management-quality-guide

3. PlanMyRetire. "Management Quality Assessment: Evaluating Capital
   Allocators." Finance University.
   https://planmyretire.com/university/investing-fundamentals/deep-dives/management-quality-assessment.html

4. WorldlyInvest. "How to Evaluate Management and Capital Allocation
   Like a Professional Investor." June 20, 2025.
   https://www.worldlyinvest.com/p/how-to-evaluate-management

5. GuruFocus. "Insider Ownership -- Definition, Formula & Calculator."
   https://www.gurufocus.com/term/insider-ownership

6. FairPriceIndex. "Buybacks and Capital Allocation: The Investor's
   Guide." July 6, 2026.
   https://www.fairpriceindex.com/education/buybacks-and-capital-allocation

7. Buffett, Warren. Berkshire Hathaway Annual Letters (1965-present).
   https://www.berkshirehathaway.com/letters/letters.html

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- the full pipeline
  architecture this framework belongs to (Stage 3C)
- `investing/frameworks/simple-moat-scoring.md` -- the companion
  framework for moat assessment (Stage 3B)
- `library/value-investing/anchor-value-investing.md` -- domain anchor
- `library/investors/charlie-munger.md` -- Munger on incentives, human
  misjudgment, and management quality
