---
name: template-company
id: 20260924T082952Z
tier: core-template
author: Neo
links:
  - agentic-brain:governance/template-library.md
  - frameworks/sector-metrics.md
  - frameworks/simple-management.md
  - frameworks/simple-moat.md
  - frameworks/financial-health.md
  - frameworks/simple-dcf.md
  - frameworks/investment-thesis.md
---

# Company Research Template -- How We Write Company Research Files

A company research file is an evidence-backed assessment of a business, its
management, competitive position, financial health and valuation. It lives in
`companies/` and presents the findings from the investment frameworks.

This template defines the frontmatter, body structure and quality checklist
for company research files. It is the format specification for full
assessments, not the research workflow or a replacement for the investment
methods. Personal company knowledge notes and research-only summaries have
different purposes.

## Company Report Checklist -- HARD GATE

Before releasing a company report, verify every applicable item against the
actual file, sources and calculation records. Keep this checklist in the
template, not in the published company report.

- [ ] Frontmatter follows the schema below: name, id, tier, author, ticker, exchange, review_date, data_cutoff, reporting_currency, tags, links. (PASS / HALT)
- [ ] New report: generate a unique id with `date -u +'%Y%m%dT%H%M%SZ'`. Update: preserve the published id and original author; identify the current reviewer in the report. Dates reflect work actually performed. (PASS / HALT)
- [ ] Exact company, listing, share class, ADR ratio where relevant, reporting basis, units, history covered and evidence cutoff are explicit. (PASS / HALT)
- [ ] Business and sector analysis explain the economics, competence boundary, selected measures and valuation-method fit. (PASS / HALT)
- [ ] Management output includes the applicable questionnaire answers, original promises versus outcomes, scorecard and any overriding concern. (PASS / HALT)
- [ ] Moat output includes applicable mechanism answers, competitive forces, separate dimensional ratings, confidence and the principal threat. (PASS / HALT)
- [ ] Financial-health findings trace to historical statements, normalization and cash/claims bridges, and dated stressed funding; decisive gaps remain visible. (PASS / HALT)
- [ ] Valuation uses sector-appropriate metrics and methods, presents Base/Bull/Bear cases with the correct cash/earnings and ownership labels, and marks unsupported case values N/A with the blocker. Calculations and material sensitivities are reproduced by a second calculation. (PASS / HALT)
- [ ] Thesis, contrary case, permanent-loss risk and review triggers agree with the business, management, moat, funding and valuation evidence. No composite investment score or trade instruction is added. (PASS / HALT)
- [ ] Investment Thesis ends with Final Verdict immediately before Sources: integrated judgment, confidence, dated matching-share price, Base/Bull/Bear values and Base-case discount/premium. Its figures agree with Valuation; missing or stale evidence cannot support a current price judgment. (PASS / HALT)
- [ ] The analytical body contains the six framework sections below. Each section states its coverage status; supported early conclusions identify skipped work without disguising gaps as neutral scores, zeros or completed valuations. (PASS / HALT)
- [ ] Every analysis table is followed immediately by a short conclusion explaining what its findings mean. Normally use 3-5 sentences, fewer when sufficient or more when material complexity warrants; do not repeat the rows or pad to a quota. (PASS / HALT)
- [ ] The report presents results and short explanations, not a calculation notebook. Routine workings stay outside the report; retained assumptions and qualifications are sufficient to interpret the results without repeated tables or caveats. (PASS / HALT)
- [ ] Material facts and figures resolve to inspected sources; assumptions and interpretation are identified. Citations, calculation links and repository references resolve. (PASS / HALT)
- [ ] Final report follows the body order below, contains no unfilled placeholders, is ASCII-only, and uses the authorized company-file destination. Existing report identity and dated thesis changes are preserved. (PASS / HALT)

**PASS:** the report supports its stated assessment, including a negative or
limited assessment. **HALT:** unsupported claims, misleading completion labels,
missing required output or an unauthorized write. A missing input may be
reported explicitly; it must not be replaced with an invented result.

## Frontmatter Schema

This is the company report's frontmatter, not the template's own metadata.
Replace placeholders; do not copy this template's id into a company report.

```yaml
---
name: <company-research-slug>
id: <YYYYMMDDTHHMMSSZ>
tier: company-research
author: <original-author>
ticker: <exact-ticker>
exchange: <exchange>
review_date: <YYYY-MM-DD>
data_cutoff: <YYYY-MM-DDTHH:MM:SSZ>
reporting_currency: <currency-code>
tags: [<sector-tag>, <business-model-tag>]
links:
  - governance/template-company.md
  - <relevant-existing-repository-path>
---
```

- Use a descriptive lowercase, hyphenated `name` and tags. Preserve ticker
  spelling and punctuation; the ticker is an identifier, not a prose slug.
- `review_date` is the actual review date in UTC. `data_cutoff` is the UTC
  information cutoff, not the year-end or the latest filing's period end.
  A formatting-only update does not refresh either date without a new review.
- `reporting_currency` is the financial-statement currency. Identify any
  different valuation or quoted-share currency in the body.
- `links` use repository-root paths within Investing Hub, and exact
  `repo:path` prefixes across repositories. Include only existing targets.
- Preserve an existing company's filename and permanent identity on updates.
  For a new file, use the authorized company naming convention; resolve the
  entity and listing before selecting the destination.

## Body Structure

Begin with `# <Company Name> -- <Central Research Finding>` and a short opening
that explains the business and the assessment. State **thesis status**,
**confidence** and **valuation status** separately; a supported business thesis
is not proof that the shares are attractively priced.

Follow with a compact identity line: legal entity; ticker/exchange; share class
and ADR ratio if applicable; review date/reviewer; information cutoff; accounting
standard, consolidation perimeter and fiscal year-end; currency/units; history
and latest interim period covered. State unavailable history explicitly.

The analytical body consists of the six framework sections below, in order.
Use their level-2 report headings. In each section, state **Coverage: Assessed /
Limited / Not applicable / Not assessed**, with the reason for a limitation or
exclusion. Assessed means the applicable questions were addressed, not that the
result was favorable. Keep coverage and supporting-record links in the relevant
section rather than adding a separate coverage section or scorecard.

Keep table cells short without compressing away decisive evidence. Immediately
below every analysis table, add a **Summary:** paragraph explaining the main
conclusion, why it matters and the uncertainty or trigger that could change it.
Normally use 3-5 sentences; fewer are appropriate for a simple finding and more
when needed to explain a material issue. This applies to each table within a
section, not just once after the whole section. Interpret the evidence rather
than repeat each row, introduce unsupported claims or manufacture prose.

Put uncertainty beside the affected claim. Present concise results tables and
short explanations, retaining the material assumptions, valuation basis and
source references rather than every calculation. Keep detailed workings in
temporary research records for verification; link only existing retained records,
never deleted scratch files. A single Markdown deliverable does not require
embedding the working notebook or creating companion files. Sources and optional
related references follow the analytical body as supporting material.

The referenced frameworks own their methods, scoring and overrides. This
template controls company-report presentation: include the short summaries even
where a standalone framework requests table-only output. Do not change its
analytical rules. If a framework changes, reconcile the affected output here
before using a stale table. Do not import the Library's topic word counts or
source quotas into a company assessment.

### 1. Business and Method

Report heading: `## Business and Method`.
Apply `frameworks/sector-metrics.md`; classify the actual economics, with
separate rows for materially different segments where needed. Carry these
selected metrics into Financial Health and Valuation; do not impose the same
ratios or valuation method on every sector.

| Question | Assessment / evidence |
|:--|:--|
| Who pays, for what, and why do customers return? | |
| Segments, geography and principal competitors | |
| Main revenue, margin and cash-generation drivers | |
| Capital required and who bears financing risk | |
| Sector-specific measures and historical comparison | |
| Circle of competence and decisive limitations | |
| Principal valuation method / useful cross-check | |

**Summary:** Explain how the business earns money, which drivers matter most,
and why the selected measures and valuation method fit. State the main
competence limit or accounting trap. Do not assign a sector score.

### 2. Management

Report heading: `## Management`.
Apply `frameworks/simple-management.md`. Identify the chief executive,
principal capital allocator, tenure and controlling owners on one line.
Use dated decisions, capital deployment, funding and actual share-count
reconciliations as evidence, not reputation or share-price performance.

Show the framework's promises-versus-results record before the scorecard.
Cover its required material commitments, preserve original scope and deadlines,
and distinguish unavailable, not-yet-due and noncomparable outcomes from misses.

| Statement date / original commitment | Metric, scope / target horizon | Actual year 1 / 2 / 3 | Delivery pattern / explanation |
|:--|:--|:--|:--|
| | | | |

**Summary:** Explain the pattern of delivery and candor, separating decisions
management controlled from external conditions. Distinguish a missed commitment
from dishonesty and targets not yet due from failures.

| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
|:--|:--|--:|:--|:--|
| Integrity and candor | | | | |
| Capital allocation | | | | |
| Ownership and incentives | | | | |
| Execution and adaptability | | | | |
| Governance and minority treatment | | | | |
| **Overall** | **Framework classification / applicable override** | | | |

**Summary:** State whether the evidence supports trusting management with owner
capital, why, and what could change that view. Explain any overriding concern
instead of allowing a favorable average to obscure it.

Answer every applicable framework question, with a limitation or counterexample
per category. Follow its early-conclusion option when warranted: retain Overall,
the decisive evidence, override and unassessed work rather than inventing scores.

### 3. Moat

Report heading: `## Moat`.
Apply `frameworks/simple-moat.md`. Define the customer/product/geographic
perimeter. Separate structural protection from execution, growth runway and
industry conditions; corroborate decisive claims beyond management's assertion.

| Mechanism | Present / Absent / Unknown | Answer / evidence | Contrary evidence | Confidence |
|:--|:--|:--|:--|:--|
| Switching costs | | | | |
| Network effects | | | | |
| Brand, patents or licenses | | | | |
| Structural cost advantage | | | | |
| Efficient scale | | | | |
| Scale economies shared | | | | |

**Summary:** Identify the supported competitive defense, or explain why none
is established. Connect the mechanism to customer behavior and distinguish
observed protection from an attractive but unverified story.

| Force / question | Pressure | Evidence-based answer | Confidence |
|:--|:--|:--|:--|
| Rivalry: can rivals compete away profit through price or capacity? | | | |
| Entry: what prevents a funded newcomer from winning customers? | | | |
| Suppliers: can essential providers capture the margin? | | | |
| Buyers: can concentrated or price-sensitive customers force concessions? | | | |
| Substitutes: can another solution meet the need more cheaply or better? | | | |

**Summary:** Identify the strongest pressure on industry profits and whether
the company's defense offsets it. Explain which competitor, supplier, customer
or substitute could capture the economic benefit.

| Protection /5 | Economics /5 | Durability /5 | Trend /5 | Class / trend | Confidence | Decisive evidence / limitation | Threat / reassessment trigger |
|--:|--:|--:|--:|:--|:--|:--|:--|
| | | | | | | | |

**Summary:** Explain the moat classification and trend using the decisive
economic evidence. State the principal threat, confidence limit and observable
change that would warrant reassessment.

Use the framework's classification and early-conclusion rules. Do not add an
overall average or let a low share price improve the moat assessment.

### 4. Financial Health

Report heading: `## Financial Health`.
Apply `frameworks/financial-health.md`. State the review period and summarize
what the historical statements, normalization, cash/claims reconciliation and
dated liquidity stress imply. Keep full schedules and intermediate arithmetic
in working records, not extra report tables by default. The assessment table
must show the decisive results, including the first shortfall or credible headroom.
Use sector-appropriate capital and funding analysis where corporate ratios
would mislead. Do not treat unavailable data as zero or a diagnostic cash
subtotal as automatically distributable owner cash.

| Area | Key measure / trend | Assessment | Confidence | Main vulnerability / trigger |
|:--|:--|:--|:--|:--|
| Earnings reliability | | | | |
| Cash generation and conversion | | | | |
| Debt and solvency | | | | |
| Liquidity under stress | | | | |
| Growth and reinvestment returns | | | | |
| **Overall** | **First stress shortfall, or headroom** | **Framework verdict** | | |

**Summary:** Explain whether earning power is reliable and obligations remain
fundable under the stated stress. Connect cash conversion, reinvestment and
claims to the overall verdict; identify the principal vulnerability rather
than repeat every ratio.

Follow the framework's early-conclusion option when decisive weakness or
uncertainty makes other work unnecessary; identify the gaps in Overall.
Do not average away a survival problem.

### 5. Valuation

Report heading: `## Valuation`.
Use `frameworks/simple-dcf.md` only when applicable; otherwise use the selected
alternative in `frameworks/sector-metrics.md`. State the valuation date, method,
currency/units, normalized starting basis, claimholders, ownership perimeter,
equity adjustments, current share basis and valuation type. Briefly explain the
material assumptions and adjustments; verify full calculations in working
records rather than reproducing them all here. Value independently before
introducing a dated, matching-share market price. Present Base, Bull and Bear
cases for the selected method, not only when a simple DCF is applicable.

For an applicable simple DCF, show its input line (V0, A, S and optional P),
required-return convention and exactly the framework's scenario output below.
Keep earnings-proxy, market-multiple-hybrid and cash-DCF labels distinct.

| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Value/share (valuation type) | Price at 30% discount | Price at 50% discount |
|:--|:--|--:|--:|--:|--:|--:|
| Base | | | | | | |
| Bull | | | | | | |
| Bear | | | | | | |

**Summary:** Explain what drives the valuation range, which assumptions matter
most and how much confidence the cash/claims basis warrants. Keep the valuation
type explicit and separate business value from the subsequent price comparison.

For an alternative method, replace the DCF table with a compact method-specific
Base/Bull/Bear table using the selected sector drivers and common value per
share. Briefly explain principal components, attributable ownership and
claims/cost adjustments; identify market-priced components. Mark simple DCF
Not applicable with its reason; do not force unsuitable inputs into a growth
model or substitute three arbitrary multiples for reasoned scenarios.

For either route, give confidence, decisive uncertainty, material sensitivities,
the useful cross-check and a reassessment trigger. For DCF, summarize the
required no-growth check and terminal dependence; keep detailed workings outside
the report.
Use intrinsic-value and margin-of-safety language only where the method and
evidence justify it; a discount to quoted NAV or an earnings proxy is not an
established margin of safety. Neither a Bear case nor asset book value is a floor.

If conclusion-critical cash, ownership or funding inputs remain unresolved,
state **Not calculable**, show the blocker and use N/A for unsupported case values.
Any supplementary what-if calculation must remain separately labeled and must
not turn a limited report into a completed intrinsic valuation.
An alternative-method or Not calculable table also needs its own short summary.

### 6. Investment Thesis

Report heading: `## Investment Thesis`.
Apply `frameworks/investment-thesis.md`. State its research status and confidence
on one line, then connect the findings rather than repeat the preceding tables.

| Area | Conclusion / decisive evidence | Contrary evidence / limitation | Review trigger / date |
|:--|:--|:--|:--|
| Business / competence | | | |
| Source of value / critical assumptions | | | |
| Permanent-loss case / protection | | | |
| Quality, funding and valuation consistency | | | |
| Value versus price / possible mispricing | | | |
| **Overall / change since prior review** | | | |

**Summary:** Explain the weakest critical assumption and the next observable
evidence that would strengthen, weaken or invalidate the thesis. Keep the closing
quality-and-price judgment for Final Verdict rather than repeating it here.

Keep the strongest contrary case and observable review triggers explicit.
Preserve the original thesis and dated changes in the supporting record.
Use the framework's supported early-conclusion form where applicable. A research
verdict is not an instruction to trade, select a position size or set Suggi's
required margin of safety.

#### Final Verdict

Report subheading: `### Final Verdict`. This closes Investment Thesis immediately
before `## Sources`; it is not a seventh framework section. In a brief synthesis,
normally 3-5 sentences, combine business economics and moat, management, financial
resilience and valuation into a judgment rather than another checklist or score.
Include the current price and quote timestamp, Bear/Base/Bull value per share,
the Base-case percentage discount or premium, confidence and the decisive risk
or reassessment trigger. Reuse the researched values from Valuation, on the same
share class, currency, ADR/FX and whole-company ownership basis.

Use the discount-to-value convention in `frameworks/simple-dcf.md`: the positive
Base value, not market price, is the percentage denominator. State a discount as
"X% below Base estimated intrinsic value" and a premium as "X% above"; distinguish
this from upside/downside measured against purchase price. Judge undervalued,
approximately fairly valued or overvalued relative to that stated basis, without
presenting an uncertain estimate as fact or a discount as guaranteed protection.
For a proxy or quoted NAV retain that label, not intrinsic-value/MoS language.
If value is unsupported, the price is stale/missing, the bases do not match or
Base value is zero, show the affected comparison N/A and the reason. A partial
business valuation cannot establish whole-stock under/overvaluation. Do not
manufacture numbers to fill the closing section.

**Supported-valuation wording example -- synthetic assumed inputs, not research:**

"The business has durable customer economics, adequate management and funding
that survives the modeled stress. At the assumed USD80 ordinary-share quote as
of <verified quote timestamp>, Bear/Base/Bull estimated intrinsic values of
USD70/100/130 imply a 20% discount to Base, although the price is above Bear.
My judgment is undervalued relative to Base, with Medium confidence; the apparent
discount must be weighed against the downside case. Sustained cash-conversion
deterioration would invalidate the thesis."

## Sources and Supporting References

Report heading: `## Sources`.
Use one combined numbered list. Cite claims with `[1]` or `[1][3]`, without
outer parentheses or automatic Markdown footnotes. Every number must resolve
to the inspected source supporting that claim, including filing date and page,
note, table or section where useful.

For external sources, give institution/author, date if known, title, direct URL
and authority rating: `[high]`, `[medium]` or `[low]`. Favor issuer filings and
regulator originals for financial facts; independent evidence matters for
load-bearing competitive or conduct claims. Authority does not establish
neutrality, and repeated versions of one origin are not corroboration.
For repository sources use `repo:path -- brief relevance` across repositories,
or a repository-root path within Investing Hub. Preserve a specific revision
when the claim depends on it. Do not invent publication dates.

Link supporting records in the relevant framework section: statement history,
source ledger, valuation model and dated reassessment evidence as applicable.
Link only records that exist; do not create empty companion files to satisfy
the format. An optional final `## See Also` may link related company or industry
research, explaining each connection. Do not add unrelated links to meet a quota.

## Example -- Abbreviated Company Report

This fictional example illustrates the minimum writing pattern: frontmatter,
identity, six framework sections, tables with summaries beneath each, a closing
Final Verdict within Investment Thesis, and sources. The business observations are illustrative assumptions, not claims
about a real company. Source entries and angle-bracket fields are placeholders
to replace with verified evidence; this is not a publishable research result.
The example uses a limited, Not calculable conclusion rather than inventing a
valuation. A completed valuation populates Base/Bull/Bear using the selected
method; the synthetic wording example above illustrates a supported comparison.

```markdown
---
name: example-components-company-research
id: <generated-UTC-creation-id>
tier: company-research
author: <original-author>
ticker: <exact-ticker>
exchange: <exchange>
review_date: <YYYY-MM-DD>
data_cutoff: <YYYY-MM-DDTHH:MM:SSZ>
reporting_currency: <currency-code>
tags: [industrials, replacement-components]
links:
  - governance/template-company.md
---

# Example Components -- Repeat Orders Do Not Yet Establish Owner Value

Example Components is a fictional supplier of replacement parts for industrial
equipment. In this illustrative case, repeat orders suggest customer dependence,
but incomplete cash and ownership evidence prevents an intrinsic valuation.

**Thesis status:** Investigate. **Confidence:** Low. **Valuation status:** Not calculable.

**Identity and basis:** <legal entity>; <ticker/exchange/share class>; <ADR ratio
or not applicable>; <review date and reviewer>; <information cutoff>; <accounting
standard and consolidation perimeter>; <fiscal year-end>; <currency/units>.
**History covered:** <annual and interim periods inspected; missing periods>.

## Business and Method

**Coverage: Limited** -- customer economics are described, but normalized owner
cash remains unresolved.

| Question | Assessment / evidence |
|:--|:--|
| Who pays, for what, and why do customers return? | Industrial operators buy replacement parts to keep installed equipment running.[1] |
| Segments, geography and principal competitors | One replacement-parts segment; competitors and geographic exposure require fuller comparison.[1][3] |
| Main revenue, margin and cash-generation drivers | Installed equipment, replacement frequency, pricing and inventory requirements.[1] |
| Capital required and who bears financing risk | The supplier funds tooling and inventory before collecting from customers.[1] |
| Sector-specific measures and historical comparison | Repeat orders, cash after investment and working-capital trends matter; through-cycle evidence is incomplete.[1] |
| Circle of competence and decisive limitations | The replacement model is understandable; tooling replacement cost is not yet established.[1] |
| Principal valuation method / useful cross-check | Normalized equity cash valuation if the cash bridge can be built; asset recoverability as a separate cross-check. |

**Summary:** Demand depends on maintaining installed equipment, not only on
sales of new machines. Repeat purchasing may support resilience, but inventory
and tooling still tie up owner capital. The key missing input is the investment
needed to preserve earning power, not another revenue-growth forecast.

## Management

**Coverage: Limited** -- capital-allocation and ownership evidence is incomplete.
**Decision-makers:** <CEO and capital allocator, tenure and controlling owners>.

| Statement date / original commitment | Metric, scope / target horizon | Actual year 1 / 2 / 3 | Delivery pattern / explanation |
|:--|:--|:--|:--|
| <date>: expand service capacity | <original operating target and deadline> | Delivered / later years not applicable | Operating commitment broadly matched; economic return remains unproven.[2] |
| <date>: reduce inventory | <original inventory measure and deadline> | Missed / revised / not yet due | A missed target was disclosed; original and revised baselines remain separate.[2] |
| <date>: return surplus capital | <original distribution commitment and horizon> | Partial / not yet due / not yet due | Distributions occurred, but whether the cash was surplus is unresolved.[2] |

**Summary:** The illustrative record is mixed rather than uniformly strong or
weak. Disclosing the inventory miss is relevant to candor, but does not repair
the operating result. The distribution commitment cannot be judged without
knowing the capital the business needed to retain.

| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
|:--|:--|--:|:--|:--|
| Integrity and candor | A missed commitment was acknowledged; the wider conduct record is incomplete.[2] | N/A | Low | Check treatment of recurring adjustments and setbacks. |
| Capital allocation | Expansion and distributions compete for cash; returns are not established.[1][2] | N/A | Low | Reconcile investment outcomes and funding. |
| Ownership and incentives | Current award claims and economic exposure remain unclear.[2] | N/A | Low | Reconcile ownership, compensation and dilution. |
| Execution and adaptability | Service expansion was delivered, while inventory performance lagged.[2] | N/A | Low | Test whether the inventory problem persists. |
| Governance and minority treatment | Board challenge and related-party safeguards require evidence.[2] | N/A | Low | Resolve material minority-owner questions. |
| **Overall** | **INVESTIGATE: conclusion-critical allocation and ownership gaps.** | N/A | Low | Complete the cash deployment and claims review. |

**Summary:** An operating success is not enough to establish strong stewardship.
The missing allocation and ownership evidence prevents a meaningful overall
score. This is an incomplete assessment, not an allegation of dishonesty.

## Moat

**Coverage: Limited** -- a possible customer defense is visible, but economic
proof and its durability remain incomplete.

| Mechanism | Present / Absent / Unknown | Answer / evidence | Contrary evidence | Confidence |
|:--|:--|:--|:--|:--|
| Switching costs | Unknown | Qualification and downtime may discourage supplier changes.[3] | Large customers can qualify alternatives. | Low |
| Network effects | Absent | More buyers do not directly improve the product for other buyers in this case.[3] | Shared service coverage would need a separate test. | Low |
| Brand, patents or licenses | Unknown | Reliability may matter more than brand recognition.[3] | No protected pricing advantage is established. | Low |
| Structural cost advantage | Unknown | Installed tooling may support efficient production.[1] | Competitor unit costs are unavailable. | Low |
| Efficient scale | Unknown | Niche demand may constrain entrants.[3] | No market-capacity evidence establishes this. | Low |
| Scale economies shared | Unknown | Customer savings have not been demonstrated.[1][3] | Lower prices alone would not establish the loop. | Low |

**Summary:** Qualification and downtime are the most plausible sources of
customer attachment in this case. They are hypotheses to test, not proven
switching costs. Repeat orders alone cannot show that customers lack attractive
alternatives or that the supplier captures excess returns.

| Force / question | Pressure | Evidence-based answer | Confidence |
|:--|:--|:--|:--|
| Rivalry: can rivals compete away profit through price or capacity? | Medium | Qualified competitors can bid for replacement contracts.[3] | Low |
| Entry: what prevents a funded newcomer from winning customers? | Unknown | Qualification may delay entry, but the delay is unmeasured.[3] | Low |
| Suppliers: can essential providers capture the margin? | Unknown | Specialized inputs may restrict sourcing options.[1] | Low |
| Buyers: can concentrated or price-sensitive customers force concessions? | High | Large industrial buyers can negotiate across multiple plants.[3] | Low |
| Substitutes: can another solution meet the need more cheaply or better? | Unknown | Redesign or third-party servicing could reduce part demand.[3] | Low |

**Summary:** Buyer bargaining power is the clearest pressure in the illustrative
case. Customer dependence on a part does not mean dependence on one supplier.
The analysis needs evidence that qualification barriers protect the supplier's
economics rather than merely slow procurement.

| Protection /5 | Economics /5 | Durability /5 | Trend /5 | Class / trend | Confidence | Decisive evidence / limitation | Threat / reassessment trigger |
|--:|--:|--:|--:|:--|:--|:--|:--|
| N/A | N/A | N/A | N/A | Unclear / Unknown | Low | Customer attachment is plausible; returns after necessary investment are unproven. | Lost qualifications, pricing concessions or evidence of durable excess returns. |

**Summary:** The moat remains Unclear because neither economic proof nor
durability has been established. That differs from a supported finding of no
moat. Evidence on customer alternatives and returns after reinvestment could
change the classification in either direction.

## Financial Health

**Coverage: Limited** -- normalized owner cash and usable stressed liquidity
are unresolved. **Supporting records:** <verified statement and bridge links>.

| Area | Key measure / trend | Assessment | Confidence | Main vulnerability / trigger |
|:--|:--|:--|:--|:--|
| Earnings reliability | Exceptional and recurring costs still need reconciliation.[1] | Unknown | Low | Adjusted profit may omit ongoing costs. |
| Cash generation and conversion | Inventory and tooling consume cash; sustaining needs remain uncertain.[1] | Unknown | Low | Weak collections or replacement spending. |
| Debt and solvency | Claims and accessible cash are not fully reconciled.[1] | Unknown | Low | Undisclosed restrictions or obligations. |
| Liquidity under stress | No defensible dated headroom figure is available.[1] | Unknown | Low | Maturities before usable funding arrives. |
| Growth and reinvestment returns | Added capacity has not yet demonstrated owner returns.[1] | Unknown | Low | Growth absorbs cash without earning its cost. |
| **Overall** | **Stress headroom not established.** | **Unclear** | Low | Complete the cash, claims and dated funding bridges. |

**Summary:** Reported profitability does not yet establish financial resilience.
Working capital and replacement investment could consume much of the apparent
earning power. Without a dated funding bridge, the report cannot claim that the
company would survive the chosen stress without new financing.

## Valuation

**Coverage: Limited.** Simple DCF is not calculable until the cash/claims basis
is resolved. **Basis:** <valuation date, currency/units, equity perimeter and
current share basis>; no price comparison is made before a defensible value.

| Case | Valuation status / missing basis | Value/share | Price comparison |
|:--|:--|--:|:--|
| Base | Not calculable: normalized owner cash, reinvestment and equity claims.[1][2] | N/A | N/A |
| Bull | Same missing basis; optimistic growth cannot repair the cash/claims gap. | N/A | N/A |
| Bear | Same missing basis; no supported downside value or floor. | N/A | N/A |

**Summary:** The missing economic inputs prevent an intrinsic-value conclusion,
not merely a more precise estimate. Substituting reported profit would change
the result into an earnings proxy rather than solve the problem. The next step
is to resolve the cash and ownership bridges, not apply a larger discount to an
unsupported number.

## Investment Thesis

**Coverage: Limited. Thesis status: Investigate. Confidence: Low.**

| Area | Conclusion / decisive evidence | Contrary evidence / limitation | Review trigger / date |
|:--|:--|:--|:--|
| Business / competence | Replacement demand is understandable.[1] | Sustaining tooling economics remain unclear. | Obtain replacement-cost evidence. |
| Source of value / critical assumptions | Repeat orders may support durable earning power.[1][3] | Customer bargaining and reinvestment may absorb the benefit. | Verify returns after necessary investment. |
| Permanent-loss case / protection | Cash absorption combined with obligations could damage owners.[1] | Usable funding and recoverable asset values are not established. | Complete the dated stress case. |
| Quality, funding and valuation consistency | No completed valuation is claimed. | Plausible customer attachment cannot fill the cash gap. | Reconcile the decisive inputs together. |
| Value versus price / possible mispricing | N/A until value is supportable. | An apparently low multiple would not establish a bargain. | Compare only after independent valuation. |
| **Overall / change since prior review** | **Investigate; initial assessment.** | **Cash, ownership and durability remain unresolved.** | **Review at the next relevant filing or earlier decisive disclosure.** |

**Summary:** Customers or reinvestment may capture the benefit of repeat demand.
The next decisive evidence is owner cash after necessary investment and stressed
funding, not a share-price movement alone.

### Final Verdict

The replacement business is understandable, but durable excess returns and
management's allocation record remain unproven.[1][2][3]
Unresolved cash requirements and stressed funding prevent a supported investment
case, so my judgment is **Investigate, Low confidence**.[1][2]
Current price is **N/A (no verified quote in this illustration)**;
**Bear/Base/Bull intrinsic values and discount/premium are N/A** because the
cash and ownership basis is unresolved; no under/overvaluation is established.
Reassess when the necessary investment and claims can be reconciled.

## Sources

These are source-format placeholders for the fictional example, not citations
to real evidence. Replace each with the inspected document and appropriate
authority rating before using this format for a real company.

1. <Issuer>. <Date>. "<Annual/interim report title>." <Direct URL and relevant pages/notes>. <Authority rating>.
2. <Issuer or regulator>. <Date>. "<Ownership, compensation and original-commitment disclosures>." <Direct URLs and sections>. <Authority rating>.
3. <Independent customer, competitor or industry source>. <Date>. "<Title>." <Direct URL and relevant section>. <Authority rating>.
```
