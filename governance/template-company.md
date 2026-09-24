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
- [ ] Valuation follows an applicable framework, states its cash/earnings and ownership basis, and retains the correct valuation-type labels. Calculations and material sensitivities are reproduced by a second calculation. (PASS / HALT)
- [ ] Thesis, contrary case, permanent-loss risk and review triggers agree with the business, management, moat, funding and valuation evidence. No composite investment score or trade instruction is added. (PASS / HALT)
- [ ] Every framework has a coverage status. Supported early conclusions identify skipped work; missing evidence is not disguised as a neutral score, zero or completed valuation. (PASS / HALT)
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

Use the level-2 report headings below in order. Keep table cells short without
compressing away decisive evidence. Put uncertainty beside the affected claim.
Detailed statements, questionnaires and calculation workings may live in linked
supporting records; all material conclusions belong in the report.

The referenced frameworks own their methods, scoring, overrides and finished
outputs. The tables here arrange those outputs; they do not replace the
frameworks. If a framework changes, reconcile this template before using a stale
table. Do not import the Library's topic word counts or source quotas into a
company assessment.

### 1. Business and Method

Report heading: `## Business and Method`.
Apply `frameworks/sector-metrics.md`; classify the actual economics, with
separate rows for materially different segments where needed.

| Question | Assessment / evidence |
|:--|:--|
| Who pays, for what, and why do customers return? | |
| Segments, geography and principal competitors | |
| Main revenue, margin and cash-generation drivers | |
| Capital required and who bears financing risk | |
| Sector-specific measures and historical comparison | |
| Circle of competence and decisive limitations | |
| Principal valuation method / useful cross-check | |

Explain the selected method's fit and its main accounting or industry trap.
This section selects the lens; it does not assign a sector score.

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

| Category | Answers / decisive fact | Score /5 | Confidence | Concern / reassessment trigger |
|:--|:--|--:|:--|:--|
| Integrity and candor | | | | |
| Capital allocation | | | | |
| Ownership and incentives | | | | |
| Execution and adaptability | | | | |
| Governance and minority treatment | | | | |
| **Overall** | **Framework classification / applicable override** | | | |

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

| Force / question | Pressure | Evidence-based answer | Confidence |
|:--|:--|:--|:--|
| Rivalry: can rivals compete away profit through price or capacity? | | | |
| Entry: what prevents a funded newcomer from winning customers? | | | |
| Suppliers: can essential providers capture the margin? | | | |
| Buyers: can concentrated or price-sensitive customers force concessions? | | | |
| Substitutes: can another solution meet the need more cheaply or better? | | | |

| Protection /5 | Economics /5 | Durability /5 | Trend /5 | Class / trend | Confidence | Decisive evidence / limitation | Threat / reassessment trigger |
|--:|--:|--:|--:|:--|:--|:--|:--|
| | | | | | | | |

Use the framework's classification and early-conclusion rules. Do not add an
overall average or let a low share price improve the moat assessment.

### 4. Financial Health

Report heading: `## Financial Health`.
Apply `frameworks/financial-health.md`. State the review period and link the
historical statements, reported-to-normalized earnings bridge, valuation
cash/claims bridge and dated liquidity stress schedule. The table must show
what those checks imply, including the first shortfall or credible headroom.
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

Follow the framework's early-conclusion option when decisive weakness or
uncertainty makes other work unnecessary; identify the gaps in Overall.
Do not average away a survival problem.

### 5. Valuation

Report heading: `## Valuation`.
Use `frameworks/simple-dcf.md` only when applicable; otherwise use the selected
alternative in `frameworks/sector-metrics.md`. State the valuation date, method,
currency/units, normalized starting basis, claimholders, ownership perimeter,
equity adjustments, current share basis and valuation type. Link the inputs,
claims reconciliation and reproducible calculation. Value independently before
introducing a dated, matching-share market price.

For an applicable simple DCF, show its input line (V0, A, S and optional P),
required-return convention and exactly the framework's scenario output below.
Keep earnings-proxy, market-multiple-hybrid and cash-DCF labels distinct.

| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Value/share (valuation type) | Price at 30% discount | Price at 50% discount |
|:--|:--|--:|--:|--:|--:|--:|
| Base | | | | | | |
| Bull | | | | | | |
| Bear | | | | | | |

For an alternative method, replace the DCF table with a compact method-specific
table showing the principal components or dated cash flows, valuation basis,
attributable ownership, claims/cost adjustments and common value per share.
Identify market-priced components. Mark simple DCF Not applicable with its
reason; do not force unsuitable inputs into a growth model.

For either route, give confidence, decisive uncertainty, material sensitivities,
the useful cross-check and a reassessment trigger. For DCF, include the required
no-growth check and terminal dependence, with details in linked workings.
Use intrinsic-value and margin-of-safety language only where the method and
evidence justify it; a discount to quoted NAV or an earnings proxy is not an
established margin of safety. Neither a Bear case nor asset book value is a floor.

If conclusion-critical cash, ownership or funding inputs remain unresolved,
state **Not calculable**, show the blocker and use N/A for unsupported values.
Any supplementary what-if calculation must remain separately labeled and must
not turn a limited report into a completed intrinsic valuation.

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

Keep the strongest contrary case and observable review triggers explicit.
Preserve the original thesis and dated changes in the supporting record.
Use the framework's supported early-conclusion form where applicable. A research
verdict is not an instruction to trade, select a position size or set Suggi's
required margin of safety.

### 7. Coverage and Supporting Records

Report heading: `## Coverage and Supporting Records`.
Use **Assessed / Limited / Not applicable / Not assessed**. Explain each limit
or exclusion, including work skipped after a supported early conclusion.
Assessed means the applicable questions were addressed, not that the result
was favorable. Avoid a completed-analysis claim for partial work.

| Framework | Status | Material limitation / linked supporting record |
|:--|:--|:--|
| `frameworks/sector-metrics.md` | | |
| `frameworks/simple-management.md` | | |
| `frameworks/simple-moat.md` | | |
| `frameworks/financial-health.md` | | |
| `frameworks/simple-dcf.md` | | |
| `frameworks/investment-thesis.md` | | |

Link only records that exist: statement history, source ledger, valuation model
and dated reassessment evidence as applicable. Do not create empty companion
files merely to satisfy the table.

### 8. Sources

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

### 9. See Also

Report heading: `## See Also`.
Finish with relevant, verified repository references and a short explanation
of each connection. Link related company or industry research where useful;
do not add unrelated links to meet a quota. Keep this after Sources, with no
further company-report sections.
