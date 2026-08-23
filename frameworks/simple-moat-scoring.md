---
name: simple-moat-scoring
id: 20260726T200000Z
tier: framework
domain: value-investing
author: Ava
tags: [moat-scoring, competitive-advantage, framework, morningstar, buffett, roic, durability, how-to]
links:
  - investing/pipeline/investment-pipeline-final.md
  - library/value-investing/economic-moats.md
  - library/value-investing/margin-of-safety.md
---

# Simple Moat Scoring -- A Practical Framework for Assessing Durable Competitive Advantage

This framework explains how to score a company's economic moat using the
4-dimension system from the investment pipeline (Stage 3B). It is designed
to be used by an agent or analyst who has access to financial data, annual
reports, and web search. It produces a consistent, evidence-backed moat
score on a 1-5 scale with a PASS/HALT threshold.

## What Moat Scoring Is (And What It Is Not)

A moat score answers one question: **How durable is this company's
competitive advantage?**

It is NOT:
- A measure of current profitability (high margins can be temporary)
- A brand popularity score (brand recognition != pricing power)
- A market cap classification (size != moat)
- A substitute for valuation (moat quality determines HOW you value, not
  whether the price is right)

The core concept: a moat is a structural feature that allows a company to
sustain returns on invested capital (ROIC) above its cost of capital
(WACC) for an extended period. If you cannot identify the specific
structural feature, you have not found the moat.

## Prerequisites: The ROIC-WACC Foundation

Before scoring moat sources, establish the quantitative baseline. A moat
that doesn't show up in the numbers is a story, not an advantage.

**Step 1: Calculate ROIC.**

```
ROIC = NOPAT / Invested Capital

Where:
  NOPAT = Operating Income * (1 - Effective Tax Rate)
  Invested Capital = Total Debt + Shareholders' Equity - Cash & Equivalents
```

Use 5-year and 10-year averages, not just the most recent year. A single
year of high ROIC proves nothing. A decade of 20%+ ROIC is evidence.

**Step 2: Estimate WACC.**

For US large caps, 8-10% is a reasonable baseline. Use 9% as default
unless you have sector-specific data. A stable utility might be 6-7%;
a volatile tech startup might be 11-13%.

**Step 3: Compute the spread.**

```
ROIC-WACC Spread = Average ROIC (5yr) - Estimated WACC
```

Interpretation:

| Spread | Signal |
|:--|:--|
| >15% | Very strong evidence of moat |
| 10-15% | Strong evidence |
| 5-10% | Moderate -- moat may exist but check trend |
| 0-5% | Weak -- returns barely exceed cost |
| <0% | No moat -- company destroys value on invested capital |

Key insight from research: the median ROIC for ~7,000 US non-financial
companies from 1963-2004 was ~10%, roughly equal to the long-term cost
of capital (Morgan Stanley). Most companies create no excess value. A
persistent positive spread IS the signal.

**Step 4: Check margin stability.**

Gross margin variation within +/-3 percentage points over 5 years
supports moat durability. Variation exceeding +/-5 points suggests
volatile pricing power. Use the coefficient of variation (CV):

```
CV = Standard Deviation of Gross Margins / Mean Gross Margin

CV < 5%  = Very stable (strong evidence of pricing power)
CV < 10% = Stable
CV < 20% = Moderate volatility
CV > 20% = High volatility (weak pricing power -- likely no moat)
```

**Step 5: Check the trend.**

Is the ROIC-WACC spread widening, stable, or narrowing?

- Widening: moat is strengthening (+1 bonus to final score)
- Stable for 5+ years: moat is maintained (neutral)
- Narrowing for 2+ years: moat is eroding (-1 penalty)
- Narrowing >2 percentage points/year: moat is in active decline
  (auto-DISCARD unless exceptional evidence of turnaround)

**Decision gate:** If the company does not have a positive ROIC-WACC
spread over 5+ years AND stable/expanding margins, skip the qualitative
scoring. The company has no quantitative evidence of a moat. Score: 1.0
(no moat).

If the quantitative signals are present, proceed to the qualitative
scoring dimensions.

## The Six Moat Sources

Morningstar identifies five structural sources. We add a sixth (scale
economies shared) from the Sleep/Zakaria framework. A company may possess
one or more. The strongest moats combine two or three in mutually
reinforcing ways.

### 1. Switching Costs

Customers would incur significant financial, procedural, or operational
costs to leave.

**Identification cues:**
- High customer retention rates (90%+)
- Long-term contracts with auto-renewal
- Products deeply embedded in customer operations (ERP, payroll, core
  banking)
- Data migration or retraining would be required to switch
- Revenue is recurring/subscription-based with low churn

**Weakness signals:**
- Open APIs or regulation (e.g., open banking) reducing integration
  friction
- Competitor offering free migration services
- Customer complaints about being "locked in" (neglect, not moat)

**Example:** Apple's 2.2 billion active devices create ecosystem lock-in
across hardware, software, and services. Moving to Android means losing
iMessage, App Store purchases, Apple Watch compatibility, and years of
accumulated data.

### 2. Network Effects

The product becomes more valuable as more people use it, creating a
self-reinforcing cycle.

**Identification cues:**
- User growth increases value for existing users
- Two-sided marketplace where buyers attract sellers and vice versa
- Dominant market share (>50%) in a winner-take-most market
- Metcalfe's Law dynamics: value grows with N^2

**Weakness signals:**
- User growth slowing or reversing (network effects can unravel)
- Competitor gaining tipping-point share
- Multi-homing is easy (users can use multiple platforms simultaneously)

**Example:** Visa/Mastercard: more merchants accept them because more
consumers carry their cards, and more consumers carry them because more
merchants accept them. A new payment network must solve for both sides
simultaneously.

### 3. Intangible Assets

Patents, brands, regulatory licenses, or other legal/intellectual
property that blocks competition.

**Identification cues:**
- Patent portfolio with 5+ years of remaining protection
- Brand that commands a measurable price premium vs generic alternatives
- Government-granted exclusivity (FDA approvals, casino licenses,
  spectrum rights)
- Proprietary technology or trade secrets that competitors cannot
  replicate

**Weakness signals:**
- Patent cliffs approaching without replacement pipeline (<3 years)
- Brand premium declining (private-label gaining share)
- Regulatory change threatening license value
- Brand spending rising while pricing power flatlines

**Example:** Coca-Cola's brand allows it to charge roughly 30% more than
private-label cola while maintaining volume share. This has persisted for
over a century. But note: the brand premium requires measurement -- brand
recognition without pricing power is not a moat.

### 4. Cost Advantage

A structural ability to produce at sustainably lower cost than
competitors.

**Identification cues:**
- Gross margin consistently above industry average by 500+ bps
- Proprietary process or technology that competitors cannot replicate
- Scale-based fixed-cost spreading (unit costs decline with volume)
- Access to unique, low-cost resources (high-grade ore, favorable
  geography)
- Vertical integration that eliminates middleman costs

**Weakness signals:**
- Competitor building equivalent scale (diminishing the advantage)
- Input cost advantage is tied to a depleting resource
- "Cost advantage" is actually just aggressive cost-cutting (cutting R&D,
  maintenance) which is value extraction, not moat widening

**Example:** GEICO's direct-to-consumer model bypasses insurance agents,
producing a structural cost advantage. Walmart's logistics scale produces
unit costs smaller retailers cannot match.

### 5. Efficient Scale

A market where the total size supports only one or a few profitable
competitors -- adding another would destroy returns for everyone.

**Identification cues:**
- Natural monopoly or duopoly in a limited market
- High fixed costs relative to market size
- New competitor would need to capture 30%+ share just to break even
- Industry has had stable competitive structure for 10+ years

**Weakness signals:**
- Market growing large enough to support another competitor
- Technology reducing fixed costs (lowering barriers)
- Regulatory changes removing geographic protections

**Example:** A regional water utility. The market cannot support two
competing water distribution networks. A rural telecom or pipeline in a
territory bounded by geography or regulation.

### 6. Scale Economies Shared (Sleep/Zakaria)

A company achieves scale economies and shares the benefits with customers
through lower prices rather than higher margins. This creates a
self-reinforcing cycle: lower prices -> more customers -> greater scale
-> even lower prices -> competitors cannot match.

**Identification cues:**
- Consistently lowest-cost provider in the industry
- Growing market share while maintaining or lowering prices
- Margins that are good but not extraordinary (the excess goes to
  customers, creating the moat)
- Competitors struggling to match pricing without losing money

**Weakness signals:**
- Margins rising while market share growth slows (company is extracting
  the benefit rather than reinvesting in the moat)
- Competitor matching the scale (the flywheel can stall)

**Example:** Costco: legendary low margins on merchandise, makes profit
from membership fees. Amazon in its first two decades: plowed scale
benefits into lower prices and faster delivery, making it impossible for
competitors to match.

**Note on source classification:** A company with a single moat source
has a narrower moat than one with multiple reinforcing sources. Microsoft
(switching costs + network effects) is more durable than a single-patent
pharma company (intangible assets only). When scoring, multi-source
reinforcement is a positive signal; single-source dependence is a risk
factor.

## The 4-Dimension Scoring Rubric

This is the core of the framework. Each of the four dimensions is scored
1-5 with specific evidence requirements. The dimensions are weighted to
reflect their relative importance.

### Dimension 1: Source Clarity (Weight: 20%)

**What it measures:** How clearly can you identify WHICH of the six moat
sources apply, and how well-documented is the evidence?

| Score | Criteria | Evidence Required |
|:--|:--|:--|
| 1 | Cannot identify any moat source with confidence | N/A (company has no identifiable moat) |
| 2 | Vague possibility of a moat source; evidence is thin or anecdotal | One source mentioned but not documented |
| 3 | One moat source clearly identified with specific supporting evidence | One source cited with at least one data point |
| 4 | Multiple sources identified OR single source with strong, multi-year evidence | Multiple sources each cited, OR single source with 3+ data points |
| 5 | Multiple reinforcing sources, each with specific evidence and cross-validation | 2+ sources cited with data, AND sources reinforce each other |

**Scoring guidance:**

- "Strong brand" without pricing-power evidence is a 2, not a 4.
- "Has patents" without checking expiry dates and replacement pipeline
  is a 2, not a 4.
- "Everyone uses it" without measuring network effects or user growth
  is a 2, not a 4.
- Every moat source claim MUST cite: which source, what specific
  mechanism creates the advantage, and at least one verifiable data
  point (ROIC data, market share trend, price premium measurement,
  retention rate).

**Common failure mode:** Naming a moat source without evidence. "Apple
has a strong brand" is a 2. "Apple's brand allows it to price iPhones
at a 40% premium to comparable Android devices while maintaining 50%+
US market share -- evidence from ASP comparisons and market share data"
is a 4.

### Dimension 2: Moat Width (Weight: 30%)

**What it measures:** How strong is the competitive advantage? This is
the magnitude dimension -- does the moat produce narrow or wide protection?

| Score | Classification | Expected Durability | Typical ROIC Profile | Evidence Required |
|:--|:--|:--|:--|:--|
| 1 | No moat | <5 years | ROIC near or below WACC | ROIC-WACC spread negative or negligible |
| 2 | Weak narrow moat | 5-10 years | ROIC 5-10% above WACC | Positive spread for 5+ years but narrow |
| 3 | Narrow moat | 10-15 years | ROIC 10-15% above WACC, stable margins | Clear moat source, consistent 5+ year spread, stable margins |
| 4 | Wide moat | 15-20 years | ROIC >15% above WACC, expanding or stable margins | Multiple sources or one very strong source, 10+ years of superior returns |
| 5 | Very wide moat | 20+ years | ROIC >25% for 10+ years, margins stable within 3pp band | Multiple reinforcing sources, multi-decade track record, no credible threats |

**Scoring guidance:**

- Err toward conservatism. Overestimating width is costlier than
  underestimating it. Score 3 if uncertain between 3 and 4.
- A single moat source can only achieve a maximum of 4 on this
  dimension. Score 5 requires multiple reinforcing sources.
- Morningstar's classification maps roughly: No Moat = 1-2, Narrow
  Moat = 3, Wide Moat = 4-5.
- The ROIC profiles are guidelines, not rigid rules. A regulated
  utility with a 7% ROIC-WACC spread and a guaranteed monopoly
  (efficient scale) may warrant a 4. A biotech with a 30% spread
  but a patent expiring in 2 years is a 2. Context matters.

**The ROIC-WACC spread is the primary quantitative anchor for this
dimension.** If the spread is narrow (<5%), you cannot score higher
than 3 regardless of qualitative story. The numbers must support the
narrative.

### Dimension 3: Threat Horizon (Weight: 25%)

**What it measures:** What is the credible competitive threat within
a defined time horizon? How long before the moat could realistically
be breached?

| Score | Threat Horizon | Description |
|:--|:--|:--|
| 1 | Imminent (0-2 years) | Active competitive threat, moat already eroding |
| 2 | Near-term (2-5 years) | Well-funded competitor emerging, technology shift visible |
| 3 | Medium-term (5-10 years) | Threat exists but distant; moat has time to adapt |
| 4 | Long-term (10-15 years) | No credible threat on horizon; high barriers |
| 5 | Very long-term (15+ years) | Structural characteristics make entry nearly impossible |

**Assessment prompts (answer with specific evidence for each):**

1. **Patent/regulatory threats:** Any patent cliffs in the next 5 years?
   Regulatory changes proposed? (Source: 10-K risk factors, industry news)
2. **Competitive threats:** Is there a well-funded competitor targeting
   this market? Has a new entrant gained >5% share in the last 3 years?
3. **Technology threats:** Is there a technology shift that could reduce
   switching costs, enable new entrants, or make the product obsolete?
   (e.g., open banking for banking moats, ARM for x86, streaming for
   cable)
4. **Customer behavior threats:** Are customer preferences shifting
   away? (Check same-store sales, customer acquisition cost trends,
   churn rates)
5. **Disruption risk:** Could a startup with a fundamentally different
   model attack this business? (Clayton Christensen's disruption theory:
   is the incumbent serving its best customers and ignoring the low end?)

**Scoring guidance:**

- A score of 4 or 5 requires the absence of ALL material threats. This is
  rare. Most companies score 2-3.
- Morningstar's methodology explicitly checks for "substantial threat of
  value destruction, stemming from ESG, industry disruption, financial
  health, or other idiosyncratic issues." If the probability is
  sufficiently high, the company is rated no-moat. Apply the same logic.
- Do not default to 3 because "uncertainty exists." Score the specific
  threats you find. If you find none after thorough search, score 4-5.

### Dimension 4: Moat Trend (Weight: 25%)

**What it measures:** Is the competitive advantage widening, stable, or
narrowing? This is the DIRECTION dimension -- moat trend is often more
important than moat width for investment decisions.

| Score | Trend | Signals |
|:--|:--|:--|
| 1 | Rapidly narrowing | ROIC declining >2pp/year, margins compressing, market share falling, credible competitor gaining share |
| 2 | Narrowing | ROIC declining >1pp/year, margins under pressure, competitor activity increasing |
| 3 | Stable | ROIC and margins stable within narrow band for 3+ years, market share holding |
| 4 | Widening | ROIC expanding, margins widening, market share growing, moat sources deepening |
| 5 | Strongly widening | Multiple reinforcing trends: ROIC expanding, moat sources multiplying, competitive gap widening |

**Specific trend indicators to check:**

| Indicator | Widening | Stable | Narrowing |
|:--|:--|:--|:--|
| ROIC-WACC spread (trend) | Expanding by 1+ pp/year | Within 1pp band | Contracting by 1+ pp/year |
| Gross margin (5-year) | Expanding | Within 3pp band | Contracting |
| Market share | Growing | Holding | Declining |
| Customer retention | Improving >1pp/year | Stable within 1pp | Declining >1pp/year |
| Competitor entry | No new entrants, incumbents exiting | Stable competitive landscape | New entrants gaining share |
| Moat source depth | New moat sources developing | Existing sources maintained | Sources weakening |

**Scoring guidance:**

- A stable moat (score 3) is the baseline. Most good businesses maintain,
  they don't widen.
- A narrowing moat (score 1-2) is a red flag regardless of other scores.
  A company with a Wide Moat (Dimension 2 = 5) but a Narrowing Trend
  (Dimension 4 = 2) is a worse investment than a Narrow Moat company with
  a Widening Trend. You are buying the future, not the past.
- Munger: "The durability of the moat is the key." The trend dimension
  captures durability directly.

## Composite Score Calculation

```
Moat Score = (Source Clarity * 0.20)
           + (Moat Width     * 0.30)
           + (Threat Horizon * 0.25)
           + (Moat Trend     * 0.25)
```

### Quick Reference Table

| Composite Score | Moat Classification | Pipeline Verdict |
|:--|:--|:--|
| 4.0 - 5.0 | Wide Moat | PASS (strong conviction) |
| 3.0 - 3.9 | Narrow Moat | PASS |
| 2.0 - 2.9 | Weak/Narrowing Moat | WATCHLIST (monitor for improvement or further erosion) |
| 1.0 - 1.9 | No Moat | DISCARD |

### PASS/HALT Threshold

**Moat score < 3.0 = DISCARD.** The pipeline gate is hard: a company
with a composite moat score below 3.0 does not proceed to deep dive
(Stage 4) unless exceptional management compensates. "Exceptional
management" must be demonstrated with specific evidence:
- Management score >= 4.0 on the management scoring rubric
- AND a specific turnaround thesis (not "management seems good")

### The Margin-of-Safety Link

Moat score directly affects the required margin of safety:

| Moat Score | Required MOS | Rationale |
|:--|:--|:--|
| 4.0 - 5.0 (Wide) | >= 20% | High confidence in durability justifies tighter MOS |
| 3.0 - 3.9 (Narrow) | >= 30% | Moderate confidence; require standard MOS cushion |
| 2.0 - 2.9 (Weak) | >= 40% | Low confidence; require large MOS to compensate |
| < 2.0 (None) | N/A | Do not value; discard |

## Evidence Requirements Per Scoring Dimension

Every dimension score must be supported by evidence. A score without a
citation is an opinion, not an assessment. The minimum requirement:

| Dimension | Minimum Evidence |
|:--|:--|
| Source Clarity | 1+ specific moat source named WITH mechanism explanation AND 1+ data point |
| Moat Width | ROIC-WACC spread calculation (5-year average) WITH source filing years |
| Threat Horizon | 2+ specific threat assessments (patents, competitors, technology, regulation) |
| Moat Trend | 3+ of the six trend indicators checked WITH directional call |

**Evidence quality ladder:**
1. **Primary (best):** 10-K/10-Q filings, SEC EDGAR, company investor
   presentations
2. **Secondary:** Morningstar analyst reports, industry publications,
   reputable financial journalism
3. **Tertiary (use sparingly):** General web articles, blog posts,
   company marketing materials
4. **Unacceptable:** "The brand is strong because everyone knows it."
   "They've been around a long time." "The CEO seems smart."

Every moat claim MUST include a source URL or filing reference. A score
of 4 or 5 on any dimension requires at least one primary source.

## Detection Signals: When You Are Overestimating the Moat

These are the most common failure modes in moat analysis. If you
recognize yourself doing any of these, downgrade your score:

1. **Outcome-based reasoning.** "Their margins are high, therefore they
   have a moat." High margins are the RESULT of a moat, not the moat
   itself. You must identify the structural feature that prevents
   competitors from compressing those margins.

2. **Single-source overconfidence.** A company with only one moat source
   (especially intangible assets, which expire) cannot score above 4 on
   Moat Width. Single-source moats are inherently narrower. If the only
   moat source is "patents" and the patent cliff is within 5 years,
   maximum Moat Width = 2.

3. **Ignoring the trend.** A company with a historically wide moat that
   is narrowing is a worse investment than a company with a narrow but
   widening moat. Do not anchor on past greatness.

4. **Brand inflation.** Every company claims to have a "strong brand."
   A brand is only a moat if it produces measurable pricing power. Test:
   would customers pay more for this product than a functionally
   identical generic? If you cannot find evidence of a price premium,
   it is not a brand moat.

5. **The "too complex to fail" fallacy.** "Their technology is so
   complex that no one can replicate it." Complexity is not a moat -- it
   is a cost. Companies with genuinely unassailable technology can
   explain it simply. If you cannot explain the advantage in plain
   language, you may not understand it.

6. **Capital-light misinterpretation.** Low CapEx/Revenue can signal
   moat (asset-light competitive advantage) OR underinvestment (value
   trap). The difference: asset-light companies grow revenue. Companies
   that spend little AND have stagnant revenue are deferring necessary
   investment.

7. **Regulatory moat complacency.** "They have a government license, so
   competition is impossible." Regulatory moats can disappear with a
   single policy change. Always assess the political sustainability of
   regulatory protection.

## Worked Example: Moat Scoring Applied

### Apple Inc. (AAPL)

**Quantitative foundation:**
- 5-year average ROIC: ~29% (well above 9% WACC)
- ROIC-WACC spread: ~20 percentage points
- Gross margin: 38-44% over 5 years, stable within band
- Trend: ROIC has been consistently high for 10+ years

**Step 3 (quantitative gate):** CLEAR PASS. Massive and persistent
positive spread.

**Dimension 1 -- Source Clarity: Score 5**
- Switching costs: 2.2 billion active devices; ecosystem lock-in across
  hardware, software, services; iMessage, App Store, iCloud integration
  create friction against leaving
- Network effects: App Store ecosystem (developers build for iOS because
  users are there, and vice versa); 1B+ active iPhones create a
  developers' market they cannot ignore
- Intangible assets: Design patents, App Store control, brand
  consistently ranked top 5 globally
- Cost advantage: Vertical integration of chip design (M-series,
  A-series); supply chain scale unmatched in the industry
- Evidence: 10-K filings, market share data, ASP comparisons vs Android

**Dimension 2 -- Moat Width: Score 5**
- Multiple reinforcing sources (4 of 6 identified)
- ROIC >25% for 10+ years
- Services revenue of $96B+ in 2024 creating recurring subscription
  lock-in
- Morningstar assigns Apple a Wide Moat rating (>20 years)
- Evidence: 10-K ROIC trend, Morningstar rating, services revenue growth

**Dimension 3 -- Threat Horizon: Score 4**
- No credible near-term competitive threat (Apple's ecosystem is
  self-reinforcing, not single-point)
- Main risk: regulatory (app store antitrust cases in EU, US)
- Technology risk: low. Smartphone form factor is mature; Apple's
  vertical integration makes leapfrogging difficult
- Not 5 because: regulatory action could force app store changes that
  weaken the ecosystem lock-in
- Evidence: EU Digital Markets Act filings, antitrust case tracking

**Dimension 4 -- Moat Trend: Score 4**
- Services revenue growing at double digits (deepens switching costs)
- Active installed base growing (2.2B devices, up from 1.5B in 2019)
- Gross margins stable to slightly expanding
- Ecosystem expanding into new categories (Vision Pro, services,
  financial products)
- Not 5 because: smartphone unit growth has plateaued; China market
  faces geopolitical and competitive pressure
- Evidence: quarterly earnings, installed base disclosures, segment
  revenue trends

**Composite Score:**

```
(5 * 0.20) + (5 * 0.30) + (4 * 0.25) + (4 * 0.25)
= 1.00 + 1.50 + 1.00 + 1.00
= 4.50
```

**Verdict: WIDE MOAT. PASS with high conviction.**

### Hypothetical: A Commodity Producer

**Quantitative foundation:**
- 5-year average ROIC: 12% (varies from 5% to 22% with commodity cycle)
- ROIC-WACC spread: 3% average, but highly volatile
- Gross margin: ranges from 8% to 28% depending on commodity prices
- CV of gross margins: 35% (high volatility)
- Trend: ROIC near zero in down-cycle years

**Step 3 (quantitative gate):** FAIL. Spread is both narrow AND
volatile. The business earns above WACC only in favorable commodity
cycles -- this is not a moat, it is cyclical luck. No structural
feature prevents competitors from entering when prices are high.

**Verdict: NO MOAT. Score 1.0. DISCARD (unless bought as a deep-value
cyclical play where moat is irrelevant -- but then it does not proceed
through the moat-scoring pipeline stage).**

## Erosion Signals to Monitor

A moat score is a snapshot, not a permanent rating. These signals
indicate moat erosion and should trigger a re-scoring:

| Signal | Severity | Action |
|:--|:--|:--|
| ROIC-WACC spread declining >2pp/year for 2+ years | HIGH | Re-score immediately; expect 1-2 point downgrade |
| Gross margin compression >3pp in a single year | HIGH | Investigate cause; if competitive pressure, downgrade Trend |
| New entrant gains >5% market share in 2 years | HIGH | Threat Horizon likely downgraded |
| Customer retention declining >2pp/year | MEDIUM | Monitor; possible early erosion signal |
| Patent cliff within 3 years without replacement | MEDIUM-HIGH | Downgrade Source Clarity and Threat Horizon |
| Regulatory action threatening business model | HIGH | Re-evaluate entire moat thesis |
| Management pivoting strategy away from core moat | MEDIUM | Moat may be narrowing faster than financials show |

## Integration with the Pipeline

This framework feeds directly into Stage 3B of the investment pipeline
(`investing/pipeline/investment-pipeline-final.md`). The composite moat
score is one half of the Stage 3 triage (alongside management scoring).
A company must achieve:

- Moat score >= 3.0 AND Management score >= 3.0 -> PASS to Stage 4
- Moat score >= 3.0 AND Management score < 3.0 -> DISCARD (good
  business, bad stewards)
- Moat score < 3.0 AND Management score >= 4.0 -> possible PASS with
  exceptional management override (rare; requires specific evidence)
- Moat score < 3.0 -> DISCARD

The moat score also feeds into:
- Stage 5 Conviction Check (the three Sleep/Pabrai/Munger questions)
- Stage 7 Position Sizing (moat score >= 4.0 earns a +1 position
  increment)
- Stage 8 Investment Checklist (durable moat item)
- Required margin of safety (wider moat = lower required MOS)

## Sources

1. Morningstar. "Economic Moat Ratings: How to Measure a Company's
   Competitive Advantage." March 11, 2026.
   https://www.morningstar.com/business/insights/blog/equity-economic-moat-ratings

2. Morningstar. "Equity Research Methodology." October 2020.
   https://advisor.morningstar.com/Enterprise/VTC/MasterEquityResearchMethodology_Oct2020.pdf

3. Morgan Stanley Counterpoint Global. "Measuring the Moat." 2022.
   https://www.morganstanley.com/im/publication/insights/articles/article_measuringthemoat.pdf

4. Equicurious. "Moats and Competitive Advantage Frameworks." Updated
   March 2026.
   https://equicurious.com/learn/investing-basics/evaluating-investments/moats-and-competitive-advantage-frameworks

5. SafetyMargin.io. "Economic Moat Score: Quantifying Competitive
   Advantage." March 14, 2026.
   https://safetymargin.io/blog/economic-moat-score-guide

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- the full pipeline
  architecture this framework belongs to (Stage 3B)
- `library/value-investing/economic-moats.md` -- comprehensive library
  topic on moat theory, the five sources, and historical evidence
- `library/value-investing/margin-of-safety.md` -- the MOS concept:
  moat quality determines how much MOS is required
- `library/investors/charlie-munger.md` -- Munger: "The durability of
  the moat is the key"
