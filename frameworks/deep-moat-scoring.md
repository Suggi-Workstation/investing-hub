---
name: deep-moat-scoring
id: 20260726T210000Z
tier: framework
domain: value-investing
author: Ava
tags: [deep-moat, competitive-dynamics, porters-five-forces, destination-analysis, competitor-benchmarking, moat-durability, sleep, deep-dive]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/simple-moat-scoring.md
  - library/value-investing/economic-moats.md
  - library/industries-sectors/porters-five-forces.md
---

# Deep Moat Scoring -- Full Competitive Dynamics Analysis (Stage 4A)

This framework explains how to perform the full deep-dive moat and
competitive dynamics analysis from Stage 4A of the investment pipeline.
It extends `simple-moat-scoring.md` (Stage 3B triage) into an
analyst-grade assessment. Where Stage 3B asks "does this company have
a moat?", Stage 4A asks "how deep is the moat, what is it made of, who
is trying to cross it, and where will it be in 10 years?"

## How This Differs from Simple Moat Scoring

| Aspect | Simple Moat Scoring (Stage 3B) | Deep Moat Scoring (Stage 4A) |
|:--|:--|:--|
| Purpose | Triage: PASS or DISCARD | Deep analysis: full competitive understanding |
| Moat sources | Identify which of 6 apply | Map how sources interact and reinforce |
| Competitors | Not assessed | Full benchmarking against top 3-5 |
| Industry | Not assessed | Porter's Five Forces structural analysis |
| Customers | Not assessed | Value proposition + switching cost depth |
| Future | Basic trend (widening/stable/narrowing) | 10+ year destination projection |
| Output | 1-5 composite score | Full narrative report + conviction calibration |

The deep moat analysis produces a narrative that the investment thesis
(Stage 6), valuation (Stage 7), and checklist (Stage 8) all depend on.
A Stage 3B score of 4.5 tells you the moat is wide. Stage 4A tells you
WHY it is wide, HOW it could narrow, and WHAT that means for an
investment decision.

## The Five Components of Deep Moat Analysis

### Component 1: Full Moat Durability Assessment

**Goal:** Go beyond the 4-dimension scoring from Stage 3B to a
comprehensive, evidence-rich analysis of what makes the moat durable
and how the moat sources interact.

#### 1A. Moat Source Reinforcement Map

The six moat sources (switching costs, network effects, intangible
assets, cost advantage, efficient scale, scale economies shared) do
not operate in isolation. The strongest moats have sources that
reinforce each other, creating a system that is harder to breach than
any single source alone.

**Process: Map the reinforcement relationships.**

For each identified moat source, ask: "Does this strengthen any other
source?" Document the connections.

```
Example: Microsoft (Office/365 ecosystem)

Switching Costs <--> Network Effects
       |                  |
       v                  v
   Documents in       Everyone uses
   Office format      Word/Excel
       |                  |
       +-----> Both feed Intangible Assets (brand, trust)
                         |
                         v
                  Cost Advantage (scale in cloud infra)
```

**Analysis prompt:** "If one moat source were neutralized, would the
others survive? Would the business still be protected?"

A single-source moat that collapses if neutralized is fragile.
Microsoft's moat survives even if Office file formats were standardized
because the network effect (everyone uses it) and switching costs
(institutional workflows) provide independent reinforcement.

**Evidence required:**
- For each reinforcement link, provide an example or data point
- Identify which source is the "keystone" (the one that, if removed,
  causes the most collateral damage to other sources)
- Map the dependency hierarchy

#### 1B. Moat Depth by Stakeholder

A moat looks different depending on whose perspective you take. Test
the moat against each key stakeholder group:

| Stakeholder | Question | What to Check |
|:--|:--|:--|
| Customers | Why do they stay? | Switching cost quantification, satisfaction data, churn rates |
| Competitors | Why can't they compete? | Barriers to entry, failed competitive attempts, cost structure comparison |
| Suppliers | Do they have alternatives? | Supplier concentration, switching costs in reverse |
| Regulators | Could they remove the moat? | Regulatory dependency, political risk assessment |
| Employees | Can key talent leave? | Non-compete enforceability, institutional knowledge concentration |

**Key insight:** A moat that looks strong from the customer perspective
(high switching costs) may look weak from the regulator perspective
(pending antitrust action). Deep moat analysis examines all angles.

#### 1C. Historical Stress Test

The best evidence of moat durability is how the business performed
during past industry-wide challenges.

**Process:** Identify the 2-3 most significant industry disruptions or
downturns in the last 15 years. For each, document:

1. What happened to industry volumes/revenue?
2. What happened to THIS company's volumes/revenue?
3. What happened to THIS company's margins?
4. Did the company gain or lose market share during the disruption?
5. What specific moat characteristic protected it (or failed to)?

**Example: Coca-Cola during the 2008-2009 recession.**
- Industry: beverage volumes declined
- Coca-Cola: volumes declined but less than industry (brand moat
  maintained demand)
- Margins: held stable (pricing power intact)
- Market share: gained (weaker competitors cut marketing, Coke
  maintained spend)
- Moat characteristic: brand intangible asset + distribution cost
  advantage

A company that gained share and maintained margins during a crisis
has demonstrated moat durability. A company whose margins collapsed
and share eroded during the same period has a moat that only works
in good times -- which is no moat at all.

**Evidence required:**
- Revenue and margin data for both the company and the industry during
  each disruption period
- Market share data (before, during, after)

### Component 2: Porter's Five Forces -- Industry Structural Analysis

**Goal:** Determine whether the industry STRUCTURE supports or
undermines the company's moat. A great company in a terrible industry
structure fights headwinds that eventually erode even the best
competitive positions.

Porter's framework examines five forces that determine industry
profitability. For each force, rate it as Favorable (protects industry
profits), Neutral, or Unfavorable (compresses industry profits). Then
assess how THIS company's moat interacts with each force.

#### Force 1: Threat of New Entrants

**Key question:** How easy is it for a new competitor to enter and
capture meaningful market share?

**Assessment factors:**

| Factor | Favorable (High Barriers) | Unfavorable (Low Barriers) |
|:--|:--|:--|
| Capital requirements | $1B+ to reach minimum efficient scale | <$10M to launch |
| Regulatory barriers | License required, multi-year approval | No regulatory hurdles |
| Brand/customer loyalty | 90%+ retention, deep switching costs | Easy to switch, low loyalty |
| Access to distribution | Proprietary or exclusive channels | Open distribution |
| Learning curve/IP | Decades of proprietary knowledge | Commodity knowledge |
| Network effects | Strong, self-reinforcing | No network effects |

**Scoring:** Rate the overall force as Low/Medium/High threat. Cite
specific evidence for the 2-3 most important factors.

**Company-moat interaction:** Does the company's moat specifically
target the highest barriers? Does the moat CREATE barriers that
wouldn't exist in the industry otherwise?

#### Force 2: Bargaining Power of Suppliers

**Key question:** Can suppliers squeeze the company's margins?

**Assessment factors:**

| Factor | Favorable (Low Supplier Power) | Unfavorable (High Supplier Power) |
|:--|:--|:--|
| Supplier concentration | Many suppliers, commodity inputs | Few suppliers, concentrated |
| Switching cost (company side) | Easy to switch suppliers | Difficult/costly to switch |
| Threat of forward integration | Suppliers can't become competitors | Suppliers could bypass the company |
| Input differentiation | Commodity inputs | Unique/differentiated inputs |
| Company purchase volume | Company is large customer | Company is small customer |

**Scoring:** Low/Medium/High supplier power.

**Red flag:** A single supplier represents >20% of COGS. This creates
a single point of failure unrelated to the company's competitive
position.

#### Force 3: Bargaining Power of Buyers

**Key question:** Can customers force prices down or demand better
terms?

**Assessment factors:**

| Factor | Favorable (Low Buyer Power) | Unfavorable (High Buyer Power) |
|:--|:--|:--|
| Buyer concentration | Many small customers, none >10% | One customer >20% of revenue |
| Switching cost (buyer side) | High switching costs | Easy to switch |
| Product differentiation | Unique, essential product | Commodity product |
| Price sensitivity | Low (product is small % of buyer cost) | High (product is large % of buyer cost) |
| Threat of backward integration | Buyers can't make it themselves | Buyers could self-produce |

**Scoring:** Low/Medium/High buyer power.

**Critical check:** Any customer representing >15% of revenue? If so,
the loss of that customer is an existential risk regardless of moat
quality. Document the relationship: contract length, switching cost,
customer health.

#### Force 4: Threat of Substitutes

**Key question:** Can a different product or service fulfill the same
need, potentially at lower cost or with better performance?

**Assessment factors:**

| Factor | Favorable (Low Threat) | Unfavorable (High Threat) |
|:--|:--|:--|
| Price-performance of substitutes | Substitutes are inferior or more expensive | Substitutes offer better value |
| Buyer switching cost to substitute | High cost to switch | Low cost to switch |
| Buyer propensity to substitute | Low (habit, loyalty, integration) | High (price-sensitive, experimental) |
| Technology disruption risk | Low (stable technology) | High (rapid tech evolution) |

**Scoring:** Low/Medium/High threat.

**The disruption lens (Christensen):** Is the company vulnerable to
low-end disruption? Does it serve its best customers with high-margin
products while ignoring a low-end segment where a disruptor could
gain a foothold? This is how steel mini-mills destroyed integrated
mills, how digital cameras destroyed film, and how cloud computing
is disrupting on-premise IT.

#### Force 5: Rivalry Among Existing Competitors

**Key question:** How intense is competition among current industry
players? Is it a price war or a stable oligopoly?

**Assessment factors:**

| Factor | Favorable (Low Rivalry) | Unfavorable (High Rivalry) |
|:--|:--|:--|
| Number of competitors | 2-3 dominant players | Many fragmented competitors |
| Industry growth | Growing (no need to steal share) | Stagnant/declining (zero-sum) |
| Exit barriers | Low (easy to leave) | High (assets can't be repurposed) |
| Product differentiation | Differentiated products | Commodity products |
| Pricing behavior | Rational, disciplined | Price wars, irrational discounting |
| Fixed costs as % of total | Low | High (pressure to fill capacity) |

**Scoring:** Low/Medium/High rivalry.

#### Five Forces Synthesis

After analyzing each force, produce a summary:

```
Industry: [Name]

Force                          Rating       Impact on Moat
Threat of New Entrants         Low/Med/High [Explanation]
Supplier Power                 Low/Med/High [Explanation]
Buyer Power                    Low/Med/High [Explanation]
Threat of Substitutes          Low/Med/High [Explanation]
Industry Rivalry               Low/Med/High [Explanation]

Overall Industry Structure: [Favorable / Neutral / Unfavorable]

The company's moat [strengthens / is independent of / is threatened by]
the industry structure because: [specific reasoning]
```

**Key insight from Porter:** "The point of industry analysis is not to
declare the industry attractive or unattractive but to understand the
underpinnings of competition and the root causes of profitability."
A company in an unfavorable industry structure needs an exceptionally
strong moat to earn above-average returns. A company in a favorable
industry structure can earn above-average returns with only a moderate
moat. The analysis must distinguish between returns earned by industry
structure (available to all participants) and returns earned by
company-specific advantage (available only to this company).

**Evidence required:**
- For each force: at least 2 specific data points or source citations
- Industry growth rate, market concentration (HHI or top-3 share)
- Any customer >15% of revenue must be named with contract details

### Component 3: Customer Value Proposition Analysis

**Goal:** Understand WHY customers choose this company over
alternatives and how deep that preference runs.

#### 3A. The Value Proposition Statement

In one paragraph, articulate the customer's perspective: "I buy from
[Company] instead of [Competitor] because..."

This must be specific and testable. "Because the brand is strong" is
not a value proposition. "Because switching to a competitor would
require retraining 10,000 employees on a new ERP system, risking
operational disruption that could cost $50M in downtime" is a value
proposition that quantifies the switching cost moat.

#### 3B. Customer Dependency Assessment

| Question | Data to Find | Moat Signal |
|:--|:--|:--|
| What % of customers would face material disruption if they left? | Churn rate, contract length, integration depth | High % = strong switching cost moat |
| How much would it cost a typical customer to switch? | Migration cost data, retraining estimates, downtime risk | Quantify in dollars or months |
| How long does a typical customer stay? | Average customer lifetime, retention rates | >10 years = deep moat |
| What happens when a customer tries to leave? | Win-back rates, churn reasons | High win-back = the grass wasn't greener |
| Do customers use multiple providers (multi-home)? | Multi-homing rate | High multi-homing = weak moat |

#### 3C. Customer Concentration Risk

| Concentration Level | Risk | Mitigation Question |
|:--|:--|:--|
| Top customer >20% of revenue | HIGH | Is the relationship contractual? For how long? What would cause them to leave? |
| Top 3 customers >40% | HIGH | Are they in the same industry? Correlated risk? |
| Top customer 10-20% | MODERATE | Monitor dependency trend |
| No customer >10% | LOW | Healthy customer diversification |

**Evidence required:**
- Customer concentration data from 10-K
- Churn/retention data (if disclosed) or proxy metrics
- Any publicly available customer case studies or testimonials
- Pricing data (list prices, discounting patterns, price increases)

### Component 4: Competitor Benchmarking

**Goal:** Compare the company against its top 3-5 competitors on the
metrics that matter for competitive position: market share, growth,
profitability, returns on capital, and moat-specific metrics.

#### 4A. Competitor Selection

Select the top 3-5 direct competitors. "Direct" means they compete
for the same customers in the same market with similar products. If
the company operates in multiple segments, select competitors for
the PRIMARY segment (where the moat claim is strongest).

#### 4B. Benchmarking Table

Create a side-by-side comparison table:

| Metric | Company | Competitor A | Competitor B | Competitor C | Industry Avg |
|:--|:--|:--|:--|:--|:--|
| Market Share (%) | X% | X% | X% | X% | -- |
| Market Share Trend (5yr) | +/- Xpp | +/- Xpp | +/- Xpp | +/- Xpp | -- |
| Revenue CAGR (5yr) | X% | X% | X% | X% | X% |
| Gross Margin (5yr avg) | X% | X% | X% | X% | X% |
| Operating Margin (5yr avg) | X% | X% | X% | X% | X% |
| ROIC (5yr avg) | X% | X% | X% | X% | X% |
| ROIC-WACC Spread | Xpp | Xpp | Xpp | Xpp | Xpp |
| FCF Margin | X% | X% | X% | X% | X% |
| R&D as % of Revenue | X% | X% | X% | X% | X% |
| CapEx as % of Revenue | X% | X% | X% | X% | X% |

#### 4C. Competitive Position Assessment

For each metric where the company significantly outperforms (>30%
better than next competitor), ask:

1. **Is the outperformance structural or temporary?** Structural =
   competitors cannot replicate it. Temporary = they haven't tried
   yet or it is a cyclical tailwind.

2. **Why can't competitors close the gap?** The explanation must
   reference specific moat sources. "They have a better brand" is
   insufficient. "Their distribution network reaches 200K locations
   vs 50K for the next competitor, and building 150K locations would
   require $5B and 10+ years" is sufficient.

3. **Is the gap widening or narrowing?** Competitive gaps that are
   narrowing suggest the moat is under attack. Gaps that are widening
   suggest the moat is strengthening.

#### 4D. Failed Competitive Attempts

Search for instances where a competitor tried to attack the company's
position and failed. These are among the strongest evidence of moat
durability.

**Questions to research:**
- Has a competitor launched a directly competing product? What happened?
- Has a well-funded entrant tried to enter this market? Did they succeed
  or retreat?
- Has a competitor tried to undercut on price? Did they gain share or
  just destroy their own margins?

Document at least one such example if it exists. A history of failed
competitive attacks is a powerful signal that the moat is real and
defensible.

**Evidence required:**
- 10-K filings for company and competitors (financial data)
- Market share data from industry reports or company disclosures
- News articles on competitive dynamics, market entries/exits
- Industry reports (IBISWorld, Statista, trade publications)

### Component 5: Destination Analysis (Sleep/Zakaria)

**Goal:** Project the company's competitive position 10+ years into the
future. This is not a financial forecast -- it is a strategic assessment
of where the business will be, what its moat will be worth, and what
must go right (and wrong) for that destination to materialize.

Sleep: "Destination analysis is consciously central to how we analyze
businesses." And: "The only real, long-term risk is the risk of
mis-analyzing a company's destination."

#### 5A. The Destination Narrative

Write a narrative describing what this business looks like in 10-15
years. This is not a spreadsheet exercise. It is a qualitative
projection grounded in the moat analysis from Components 1-4.

**Answer these questions in prose:**

1. **Market position:** What market share does the company hold? Has
   the market itself grown, shrunk, or transformed?

2. **Moat evolution:** Which moat sources are stronger than today?
   Which are weaker? Have new sources emerged? Have old ones
   atrophied?

3. **Competitive landscape:** Who are the competitors in 10 years?
   Are they the same as today? Have new entrants succeeded? Have old
   competitors exited?

4. **Industry structure:** Has Porter's Five Forces shifted? Is the
   industry more or less profitable than today?

5. **Threats realized and avoided:** Which of today's identified
   threats materialized? Which were successfully defended against?

6. **The business model:** Has it changed fundamentally, or is the
   company doing essentially the same thing at greater scale?

#### 5B. The Cone of Uncertainty

Sleep's concept: every destination projection has a "cone of
uncertainty." The radius of that cone is the range of plausible
outcomes. A wide-moat company with predictable cash flows has a
narrow cone (high confidence in the destination). A company in a
rapidly changing industry has a wide cone (low confidence).

**Rate the cone of uncertainty:**

| Cone Width | Meaning | Examples |
|:--|:--|:--|
| Very Narrow | Destination highly predictable 10+ years out | Coke, Moody's, waste management utility |
| Narrow | Reasonably predictable, moderate unknowns | Visa, Microsoft, Costco |
| Moderate | Several plausible divergent paths | Apple, Google, most industrials |
| Wide | Significant uncertainty, technology-dependent | Most tech, biotech, cyclical commodities |
| Very Wide | Destination fundamentally unknowable | Early-stage, pre-revenue, unproven technologies |

A narrow cone supports higher conviction. A wide cone demands a larger
margin of safety. If the cone is "very wide," the company should NOT
proceed to valuation -- it belongs in the TOO HARD pile.

#### 5C. The Path to Destination

What must go right for the favorable destination to materialize?
List 3-5 necessary conditions.

What could derail the journey? List 3-5 risk scenarios with estimated
probabilities.

For each risk scenario: "If X happens, what does the business look
like afterwards? Is it permanently impaired or temporarily disrupted?"

**Example (Costco):**

Necessary conditions for favorable destination:
1. Continued membership growth (membership model intact)
2. Scale economies shared discipline maintained (margins stay low,
   prices stay lowest)
3. No competitor matches the scale-efficiency flywheel
4. E-commerce complements rather than disrupts warehouse model

Risk scenarios:
1. Amazon/Walmart match the value proposition (probability: low-medium)
   -> if realized: margin compression but not existential
2. Management succession fails to maintain culture (probability: low)
   -> if realized: slow erosion over years, not sudden collapse
3. Consumer shift entirely to delivery (probability: medium)
   -> if realized: requires business model adaptation; warehouse
   footprint becomes liability

#### 5D. Destination Conviction Score

Based on the narrative, cone of uncertainty, and path analysis, assign
a conviction score (1-10) for the favorable destination:

| Score | Conviction | Pipeline Implication |
|:--|:--|:--|
| 1-3 | Low | Do not proceed to valuation (WATCHLIST or DISCARD) |
| 4-6 | Moderate | Proceed with wide margin of safety (>=40% MOS) |
| 7-8 | High | Proceed with standard margin of safety (>=30% MOS) |
| 9-10 | Very High | Proceed with tighter margin of safety (>=20% MOS) |

**This score directly feeds Stage 5 (Conviction Check) and Stage 7
(Position Sizing).**

**Evidence required:**
- The destination narrative must reference specific evidence from
  Components 1-4
- Risk scenarios should cite specific competitive threats identified
  in the Porter's Five Forces and competitor benchmarking
- The cone-of-uncertainty rating should reference industry stability,
  technology risk, and regulatory risk

## Synthesis: The Deep Moat Report

The output of Stage 4A is not a score -- it is a structured narrative
report. The report format:

### 1. Executive Summary (3-5 sentences)

What kind of moat does this company have? How durable is it? What is
the single most important thing an investor needs to know about this
company's competitive position?

### 2. Moat Architecture

- Moat source reinforcement map diagram (text-based)
- Deepest moat source (keystone)
- Most vulnerable moat source
- Historical stress test results

### 3. Industry Structure (Porter's Five Forces)

- Five Forces summary table with ratings
- Company-moat interaction analysis
- Key industry trend that most threatens or supports the moat

### 4. Competitive Position

- Competitor benchmarking table
- Competitive gap analysis (where the company leads, where it lags)
- Failed competitive attempts (if any)

### 5. Customer Dependency

- Value proposition statement
- Customer concentration risk
- Switching cost depth assessment

### 6. Destination Analysis

- Destination narrative (prose, 2-3 paragraphs)
- Cone of uncertainty rating with justification
- Path to destination (necessary conditions + risk scenarios)
- Destination conviction score (1-10)

### 7. Key Uncertainties and Monitoring Triggers

- Top 3 things that could change the moat assessment
- Specific metrics to monitor (with current values and warning
  thresholds)
- Re-assessment trigger events

## Integration with the Pipeline

This deep analysis feeds multiple downstream stages:

- **Stage 5 (Conviction Check):** The destination conviction score
  directly answers the Sleep question ("Can I describe what this
  business looks like in 5-10 years with confidence?")

- **Stage 6 (Investment Thesis):** The moat architecture and
  destination analysis provide the foundation for thesis pillars

- **Stage 7 (Valuation):** The cone of uncertainty and competitive
  position determine DCF assumptions (excess return period, fade
  rate, terminal growth)

- **Stage 8 (Checklist):** The report provides evidence for the
  "durable moat," "favourable destination," and "simple and
  predictable" checklist items

- **Stage 10 (Monitoring):** The key uncertainties and monitoring
  triggers define what to watch between screening cycles

## Evidence Quality Standards

A deep moat analysis without sources is opinion dressed as analysis.

| Analysis Component | Minimum Sources | Source Types |
|:--|:--|:--|
| Moat source claims | 2+ per claim | 10-K, industry reports, competitor filings |
| Porter's Five Forces | 3+ data points per force | Industry reports, news, regulatory filings |
| Customer concentration | 1 source | 10-K (risk factors or revenue concentration note) |
| Competitor metrics | 5+ data points per competitor | 10-K filings, investor presentations |
| Market share data | 1 source | Industry report, company disclosure, or reasoned estimate |
| Destination analysis | N/A (synthesis) | Must reference evidence from Components 1-4 |

If market share data is unavailable, state that explicitly and use
revenue as a proxy. Never fabricate market share numbers.

## Common Mistakes in Deep Moat Analysis

1. **Confusing industry tailwinds with company moats.** A rising tide
   lifts all boats. If all competitors are also growing 20% and earning
   30% ROIC, the company's returns may come from favorable industry
   structure, not company-specific advantage. The Porter's Five Forces
   analysis is designed to isolate this.

2. **Ignoring the worst competitor.** The benchmarking table should
   include the company's most dangerous competitor, not the easiest
   ones to beat. If you only compare against weak competitors, the
   moat will look stronger than it is.

3. **Destination as wishful thinking.** The destination narrative must
   be constrained by the competitive analysis. If the Porter's Five
   Forces show high rivalry and low barriers, projecting market share
   gains 10 years out is speculation, not analysis.

4. **Over-indexing on the past.** A 20-year history of moat durability
   is strong evidence but not a guarantee. Kodak had 100 years of
   dominance. The historical stress test is necessary but insufficient.
   The destination analysis must account for structural shifts, not
   just extrapolate history.

5. **Ignoring the "cone of uncertainty."** If you cannot describe the
   destination with reasonable confidence, do not proceed to valuation
   with standard assumptions. Use a wider margin of safety or classify
   as TOO HARD.

6. **Treating Porter's Five Forces as a checklist.** The framework
   produces insight only when you analyze HOW the forces interact and
   HOW the company's moat reshapes them. Listing five ratings without
   connecting them to the moat analysis is a waste of time.

## Sources

1. Porter, Michael E. "The Five Competitive Forces That Shape Strategy."
   Harvard Business Review, January 2008.
   https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy

2. Sleep, Nick & Zakaria, Qais. Nomad Investment Partnership Letters
   (2001-2013). https://igyfoundation.org.uk/wp-content/uploads/2021/03/Full-Collection-of-Nomad-Letters-.pdf

3. Green, William. "Richer, Wiser, Happier." Chapter 6: Nick Sleep and
   Qais Zakaria. Scribner, 2021.

4. Sleepy Capital. "Destination Analysis: On Reading the Future."
   June 2021.
   https://www.sleepycapital.com/investing/destination-analysis-on-reading-the-future/

5. Morningstar. "Economic Moat Ratings: How to Measure a Company's
   Competitive Advantage." March 11, 2026.
   https://www.morningstar.com/business/insights/blog/equity-economic-moat-ratings

6. MassiveMoats. "A Deep Dive into the Nomad Investment Partnership."
   July 2025.
   https://massivemoats.substack.com/p/a-deep-dive-analysis-into-the-nomad

## See Also

- `investing/pipeline/investment-pipeline-final.md` -- Stage 4A specification
- `investing/frameworks/simple-moat-scoring.md` -- Stage 3B triage scoring
- `library/value-investing/economic-moats.md` -- moat theory and evidence
- `library/industries-sectors/porters-five-forces.md` -- Porter's framework
- `library/industries-sectors/disruption-theory.md` -- Christensen disruption
